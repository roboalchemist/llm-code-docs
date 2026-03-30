# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/beyondcorp/v1alpha

Title: beyondcorp package - google.golang.org/api/beyondcorp/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/beyondcorp/v1alpha

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
 
v1alpha
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
Overview
Index
Constants
Variables
Functions
Types
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

import "google.golang.org/api/beyondcorp/v1alpha"
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
type ApplicationEndpoint
func (s ApplicationEndpoint) MarshalJSON() ([]byte, error)
type CloudPubSubNotificationConfig
func (s CloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig
func (s CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails
type CloudSecurityZerotrustApplinkAppConnectorProtoGateway
func (s CloudSecurityZerotrustApplinkAppConnectorProtoGateway) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails
type Connection
func (s Connection) MarshalJSON() ([]byte, error)
type ConnectionDetails
func (s ConnectionDetails) MarshalJSON() ([]byte, error)
type ConnectionOperationMetadata
func (s ConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type Connector
func (s Connector) MarshalJSON() ([]byte, error)
type ConnectorInstanceConfig
func (s ConnectorInstanceConfig) MarshalJSON() ([]byte, error)
type ConnectorOperationMetadata
func (s ConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type ContainerHealthDetails
func (s ContainerHealthDetails) MarshalJSON() ([]byte, error)
type Empty
type Gateway
func (s Gateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails
func (s GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails
type GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata
func (s GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata
func (s GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata
func (s GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata
func (s GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON() ([]byte, error)
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
type ImageConfig
func (s ImageConfig) MarshalJSON() ([]byte, error)
type ListAppGatewaysResponse
func (s ListAppGatewaysResponse) MarshalJSON() ([]byte, error)
type ListConnectionsResponse
func (s ListConnectionsResponse) MarshalJSON() ([]byte, error)
type ListConnectorsResponse
func (s ListConnectorsResponse) MarshalJSON() ([]byte, error)
type NotificationConfig
func (s NotificationConfig) MarshalJSON() ([]byte, error)
type OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Aggregation(aggregation string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Context(ctx context.Context) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter(customGroupingFieldFilter string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields(customGroupingGroupFields ...string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse, ...)
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) EndTime(endTime string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) FieldFilter(fieldFilter string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Group(group string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Header() http.Header
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) PageSize(pageSize int64) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) PageToken(pageToken string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Pages(ctx context.Context, ...) error
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) StartTime(startTime string) *OrganizationsLocationsInsightsConfiguredInsightCall
type OrganizationsLocationsInsightsGetCall
func (c *OrganizationsLocationsInsightsGetCall) Context(ctx context.Context) *OrganizationsLocationsInsightsGetCall
func (c *OrganizationsLocationsInsightsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight, error)
func (c *OrganizationsLocationsInsightsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsGetCall
func (c *OrganizationsLocationsInsightsGetCall) Header() http.Header
func (c *OrganizationsLocationsInsightsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsGetCall
func (c *OrganizationsLocationsInsightsGetCall) View(view string) *OrganizationsLocationsInsightsGetCall
type OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Aggregation(aggregation string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Context(ctx context.Context) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse, error)
func (c *OrganizationsLocationsInsightsListCall) EndTime(endTime string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Filter(filter string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Header() http.Header
func (c *OrganizationsLocationsInsightsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) OrderBy(orderBy string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) PageSize(pageSize int64) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) PageToken(pageToken string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) Pages(ctx context.Context, ...) error
func (c *OrganizationsLocationsInsightsListCall) StartTime(startTime string) *OrganizationsLocationsInsightsListCall
func (c *OrganizationsLocationsInsightsListCall) View(view string) *OrganizationsLocationsInsightsListCall
type OrganizationsLocationsInsightsService
func NewOrganizationsLocationsInsightsService(s *Service) *OrganizationsLocationsInsightsService
func (r *OrganizationsLocationsInsightsService) ConfiguredInsight(insight string) *OrganizationsLocationsInsightsConfiguredInsightCall
func (r *OrganizationsLocationsInsightsService) Get(name string) *OrganizationsLocationsInsightsGetCall
func (r *OrganizationsLocationsInsightsService) List(parent string) *OrganizationsLocationsInsightsListCall
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
type OrganizationsLocationsSubscriptionsCancelCall
func (c *OrganizationsLocationsSubscriptionsCancelCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsCancelCall
func (c *OrganizationsLocationsSubscriptionsCancelCall) Do(opts ...googleapi.CallOption) (...)
func (c *OrganizationsLocationsSubscriptionsCancelCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsCancelCall
func (c *OrganizationsLocationsSubscriptionsCancelCall) Header() http.Header
func (c *OrganizationsLocationsSubscriptionsCancelCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsCancelCall
func (c *OrganizationsLocationsSubscriptionsCancelCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsCancelCall
type OrganizationsLocationsSubscriptionsCreateCall
func (c *OrganizationsLocationsSubscriptionsCreateCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsCreateCall
func (c *OrganizationsLocationsSubscriptionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)
func (c *OrganizationsLocationsSubscriptionsCreateCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsCreateCall
func (c *OrganizationsLocationsSubscriptionsCreateCall) Header() http.Header
type OrganizationsLocationsSubscriptionsGetCall
func (c *OrganizationsLocationsSubscriptionsGetCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsGetCall
func (c *OrganizationsLocationsSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)
func (c *OrganizationsLocationsSubscriptionsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsGetCall
func (c *OrganizationsLocationsSubscriptionsGetCall) Header() http.Header
func (c *OrganizationsLocationsSubscriptionsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsGetCall
type OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) Do(opts ...googleapi.CallOption) (...)
func (c *OrganizationsLocationsSubscriptionsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) Header() http.Header
func (c *OrganizationsLocationsSubscriptionsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) PageSize(pageSize int64) *OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) PageToken(pageToken string) *OrganizationsLocationsSubscriptionsListCall
func (c *OrganizationsLocationsSubscriptionsListCall) Pages(ctx context.Context, f func(...) error) error
type OrganizationsLocationsSubscriptionsPatchCall
func (c *OrganizationsLocationsSubscriptionsPatchCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsPatchCall
func (c *OrganizationsLocationsSubscriptionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)
func (c *OrganizationsLocationsSubscriptionsPatchCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsPatchCall
func (c *OrganizationsLocationsSubscriptionsPatchCall) Header() http.Header
func (c *OrganizationsLocationsSubscriptionsPatchCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsPatchCall
func (c *OrganizationsLocationsSubscriptionsPatchCall) UpdateMask(updateMask string) *OrganizationsLocationsSubscriptionsPatchCall
type OrganizationsLocationsSubscriptionsRestartCall
func (c *OrganizationsLocationsSubscriptionsRestartCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsRestartCall
func (c *OrganizationsLocationsSubscriptionsRestartCall) Do(opts ...googleapi.CallOption) (...)
func (c *OrganizationsLocationsSubscriptionsRestartCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsRestartCall
func (c *OrganizationsLocationsSubscriptionsRestartCall) Header() http.Header
func (c *OrganizationsLocationsSubscriptionsRestartCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsRestartCall
func (c *OrganizationsLocationsSubscriptionsRestartCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsRestartCall
type OrganizationsLocationsSubscriptionsService
func NewOrganizationsLocationsSubscriptionsService(s *Service) *OrganizationsLocationsSubscriptionsService
func (r *OrganizationsLocationsSubscriptionsService) Cancel(name string) *OrganizationsLocationsSubscriptionsCancelCall
func (r *OrganizationsLocationsSubscriptionsService) Create(parent string, ...) *OrganizationsLocationsSubscriptionsCreateCall
func (r *OrganizationsLocationsSubscriptionsService) Get(name string) *OrganizationsLocationsSubscriptionsGetCall
func (r *OrganizationsLocationsSubscriptionsService) List(parent string) *OrganizationsLocationsSubscriptionsListCall
func (r *OrganizationsLocationsSubscriptionsService) Patch(name string, ...) *OrganizationsLocationsSubscriptionsPatchCall
func (r *OrganizationsLocationsSubscriptionsService) Restart(name string) *OrganizationsLocationsSubscriptionsRestartCall
type OrganizationsService
func NewOrganizationsService(s *Service) *OrganizationsService
type PrincipalInfo
func (s PrincipalInfo) MarshalJSON() ([]byte, error)
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
func (c *ProjectsLocationsAppConnectionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection, error)
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
func (c *ProjectsLocationsAppConnectionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse, error)
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
func (c *ProjectsLocationsAppConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse, ...)
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
func (c *ProjectsLocationsAppConnectorsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector, error)
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
func (c *ProjectsLocationsAppConnectorsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse, error)
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
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse, error)
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
type ProjectsLocationsApplicationDomainsGetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsGetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsGetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationDomainsGetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationDomainsGetIamPolicyCall
type ProjectsLocationsApplicationDomainsService
func NewProjectsLocationsApplicationDomainsService(s *Service) *ProjectsLocationsApplicationDomainsService
func (r *ProjectsLocationsApplicationDomainsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationDomainsGetIamPolicyCall
func (r *ProjectsLocationsApplicationDomainsService) SetIamPolicy(resource string, ...) *ProjectsLocationsApplicationDomainsSetIamPolicyCall
func (r *ProjectsLocationsApplicationDomainsService) TestIamPermissions(resource string, ...) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall
type ProjectsLocationsApplicationDomainsSetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsSetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsSetIamPolicyCall
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApplicationDomainsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetIamPolicyCall
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationsGetIamPolicyCall
type ProjectsLocationsApplicationsService
func NewProjectsLocationsApplicationsService(s *Service) *ProjectsLocationsApplicationsService
func (r *ProjectsLocationsApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationsGetIamPolicyCall
func (r *ProjectsLocationsApplicationsService) SetIamPolicy(resource string, ...) *ProjectsLocationsApplicationsSetIamPolicyCall
func (r *ProjectsLocationsApplicationsService) TestIamPermissions(resource string, ...) *ProjectsLocationsApplicationsTestIamPermissionsCall
type ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsSetIamPolicyCall
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsConnectionsCreateCall
func (c *ProjectsLocationsConnectionsCreateCall) ConnectionId(connectionId string) *ProjectsLocationsConnectionsCreateCall
func (c *ProjectsLocationsConnectionsCreateCall) Context(ctx context.Context) *ProjectsLocationsConnectionsCreateCall
func (c *ProjectsLocationsConnectionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsCreateCall
func (c *ProjectsLocationsConnectionsCreateCall) Header() http.Header
func (c *ProjectsLocationsConnectionsCreateCall) RequestId(requestId string) *ProjectsLocationsConnectionsCreateCall
func (c *ProjectsLocationsConnectionsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsCreateCall
type ProjectsLocationsConnectionsDeleteCall
func (c *ProjectsLocationsConnectionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsConnectionsDeleteCall
func (c *ProjectsLocationsConnectionsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsDeleteCall
func (c *ProjectsLocationsConnectionsDeleteCall) Header() http.Header
func (c *ProjectsLocationsConnectionsDeleteCall) RequestId(requestId string) *ProjectsLocationsConnectionsDeleteCall
func (c *ProjectsLocationsConnectionsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsDeleteCall
type ProjectsLocationsConnectionsGetCall
func (c *ProjectsLocationsConnectionsGetCall) Context(ctx context.Context) *ProjectsLocationsConnectionsGetCall
func (c *ProjectsLocationsConnectionsGetCall) Do(opts ...googleapi.CallOption) (*Connection, error)
func (c *ProjectsLocationsConnectionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsGetCall
func (c *ProjectsLocationsConnectionsGetCall) Header() http.Header
func (c *ProjectsLocationsConnectionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsGetCall
type ProjectsLocationsConnectionsGetIamPolicyCall
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectionsGetIamPolicyCall
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsGetIamPolicyCall
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsGetIamPolicyCall
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsConnectionsGetIamPolicyCall
type ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) Context(ctx context.Context) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) Do(opts ...googleapi.CallOption) (*ListConnectionsResponse, error)
func (c *ProjectsLocationsConnectionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) Filter(filter string) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) Header() http.Header
func (c *ProjectsLocationsConnectionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) OrderBy(orderBy string) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) PageSize(pageSize int64) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) PageToken(pageToken string) *ProjectsLocationsConnectionsListCall
func (c *ProjectsLocationsConnectionsListCall) Pages(ctx context.Context, f func(*ListConnectionsResponse) error) error
type ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) Context(ctx context.Context) *ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) Header() http.Header
func (c *ProjectsLocationsConnectionsPatchCall) RequestId(requestId string) *ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsConnectionsPatchCall
func (c *ProjectsLocationsConnectionsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsPatchCall
type ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) ConnectorId(connectorId string) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) Context(ctx context.Context) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*ResolveConnectionsResponse, error)
func (c *ProjectsLocationsConnectionsResolveCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) Header() http.Header
func (c *ProjectsLocationsConnectionsResolveCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) PageSize(pageSize int64) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) PageToken(pageToken string) *ProjectsLocationsConnectionsResolveCall
func (c *ProjectsLocationsConnectionsResolveCall) Pages(ctx context.Context, f func(*ResolveConnectionsResponse) error) error
type ProjectsLocationsConnectionsService
func NewProjectsLocationsConnectionsService(s *Service) *ProjectsLocationsConnectionsService
func (r *ProjectsLocationsConnectionsService) Create(parent string, connection *Connection) *ProjectsLocationsConnectionsCreateCall
func (r *ProjectsLocationsConnectionsService) Delete(name string) *ProjectsLocationsConnectionsDeleteCall
func (r *ProjectsLocationsConnectionsService) Get(name string) *ProjectsLocationsConnectionsGetCall
func (r *ProjectsLocationsConnectionsService) GetIamPolicy(resource string) *ProjectsLocationsConnectionsGetIamPolicyCall
func (r *ProjectsLocationsConnectionsService) List(parent string) *ProjectsLocationsConnectionsListCall
func (r *ProjectsLocationsConnectionsService) Patch(name string, connection *Connection) *ProjectsLocationsConnectionsPatchCall
func (r *ProjectsLocationsConnectionsService) Resolve(parent string) *ProjectsLocationsConnectionsResolveCall
func (r *ProjectsLocationsConnectionsService) SetIamPolicy(resource string, ...) *ProjectsLocationsConnectionsSetIamPolicyCall
type ProjectsLocationsConnectionsSetIamPolicyCall
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectionsSetIamPolicyCall
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsSetIamPolicyCall
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsConnectorsCreateCall
func (c *ProjectsLocationsConnectorsCreateCall) ConnectorId(connectorId string) *ProjectsLocationsConnectorsCreateCall
func (c *ProjectsLocationsConnectorsCreateCall) Context(ctx context.Context) *ProjectsLocationsConnectorsCreateCall
func (c *ProjectsLocationsConnectorsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectorsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsCreateCall
func (c *ProjectsLocationsConnectorsCreateCall) Header() http.Header
func (c *ProjectsLocationsConnectorsCreateCall) RequestId(requestId string) *ProjectsLocationsConnectorsCreateCall
func (c *ProjectsLocationsConnectorsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsCreateCall
type ProjectsLocationsConnectorsDeleteCall
func (c *ProjectsLocationsConnectorsDeleteCall) Context(ctx context.Context) *ProjectsLocationsConnectorsDeleteCall
func (c *ProjectsLocationsConnectorsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectorsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsDeleteCall
func (c *ProjectsLocationsConnectorsDeleteCall) Header() http.Header
func (c *ProjectsLocationsConnectorsDeleteCall) RequestId(requestId string) *ProjectsLocationsConnectorsDeleteCall
func (c *ProjectsLocationsConnectorsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsDeleteCall
type ProjectsLocationsConnectorsGetCall
func (c *ProjectsLocationsConnectorsGetCall) Context(ctx context.Context) *ProjectsLocationsConnectorsGetCall
func (c *ProjectsLocationsConnectorsGetCall) Do(opts ...googleapi.CallOption) (*Connector, error)
func (c *ProjectsLocationsConnectorsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsGetCall
func (c *ProjectsLocationsConnectorsGetCall) Header() http.Header
func (c *ProjectsLocationsConnectorsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsGetCall
type ProjectsLocationsConnectorsGetIamPolicyCall
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectorsGetIamPolicyCall
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsGetIamPolicyCall
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsGetIamPolicyCall
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsConnectorsGetIamPolicyCall
type ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) Context(ctx context.Context) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) Do(opts ...googleapi.CallOption) (*ListConnectorsResponse, error)
func (c *ProjectsLocationsConnectorsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) Filter(filter string) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) Header() http.Header
func (c *ProjectsLocationsConnectorsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) OrderBy(orderBy string) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) PageSize(pageSize int64) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) PageToken(pageToken string) *ProjectsLocationsConnectorsListCall
func (c *ProjectsLocationsConnectorsListCall) Pages(ctx context.Context, f func(*ListConnectorsResponse) error) error
type ProjectsLocationsConnectorsPatchCall
func (c *ProjectsLocationsConnectorsPatchCall) Context(ctx context.Context) *ProjectsLocationsConnectorsPatchCall
func (c *ProjectsLocationsConnectorsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectorsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsPatchCall
func (c *ProjectsLocationsConnectorsPatchCall) Header() http.Header
func (c *ProjectsLocationsConnectorsPatchCall) RequestId(requestId string) *ProjectsLocationsConnectorsPatchCall
func (c *ProjectsLocationsConnectorsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsConnectorsPatchCall
func (c *ProjectsLocationsConnectorsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsPatchCall
type ProjectsLocationsConnectorsReportStatusCall
func (c *ProjectsLocationsConnectorsReportStatusCall) Context(ctx context.Context) *ProjectsLocationsConnectorsReportStatusCall
func (c *ProjectsLocationsConnectorsReportStatusCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsConnectorsReportStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsReportStatusCall
func (c *ProjectsLocationsConnectorsReportStatusCall) Header() http.Header
type ProjectsLocationsConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Context(ctx context.Context) *ProjectsLocationsConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*ResolveInstanceConfigResponse, error)
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Header() http.Header
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsResolveInstanceConfigCall
type ProjectsLocationsConnectorsService
func NewProjectsLocationsConnectorsService(s *Service) *ProjectsLocationsConnectorsService
func (r *ProjectsLocationsConnectorsService) Create(parent string, connector *Connector) *ProjectsLocationsConnectorsCreateCall
func (r *ProjectsLocationsConnectorsService) Delete(name string) *ProjectsLocationsConnectorsDeleteCall
func (r *ProjectsLocationsConnectorsService) Get(name string) *ProjectsLocationsConnectorsGetCall
func (r *ProjectsLocationsConnectorsService) GetIamPolicy(resource string) *ProjectsLocationsConnectorsGetIamPolicyCall
func (r *ProjectsLocationsConnectorsService) List(parent string) *ProjectsLocationsConnectorsListCall
func (r *ProjectsLocationsConnectorsService) Patch(name string, connector *Connector) *ProjectsLocationsConnectorsPatchCall
func (r *ProjectsLocationsConnectorsService) ReportStatus(connector string, reportstatusrequest *ReportStatusRequest) *ProjectsLocationsConnectorsReportStatusCall
func (r *ProjectsLocationsConnectorsService) ResolveInstanceConfig(connector string) *ProjectsLocationsConnectorsResolveInstanceConfigCall
func (r *ProjectsLocationsConnectorsService) SetIamPolicy(resource string, ...) *ProjectsLocationsConnectorsSetIamPolicyCall
type ProjectsLocationsConnectorsSetIamPolicyCall
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectorsSetIamPolicyCall
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsSetIamPolicyCall
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Aggregation(aggregation string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Context(ctx context.Context) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter(customGroupingFieldFilter string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields(customGroupingGroupFields ...string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse, ...)
func (c *ProjectsLocationsInsightsConfiguredInsightCall) EndTime(endTime string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) FieldFilter(fieldFilter string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Group(group string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Header() http.Header
func (c *ProjectsLocationsInsightsConfiguredInsightCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) PageSize(pageSize int64) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) PageToken(pageToken string) *ProjectsLocationsInsightsConfiguredInsightCall
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Pages(ctx context.Context, ...) error
func (c *ProjectsLocationsInsightsConfiguredInsightCall) StartTime(startTime string) *ProjectsLocationsInsightsConfiguredInsightCall
type ProjectsLocationsInsightsGetCall
func (c *ProjectsLocationsInsightsGetCall) Context(ctx context.Context) *ProjectsLocationsInsightsGetCall
func (c *ProjectsLocationsInsightsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight, error)
func (c *ProjectsLocationsInsightsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsGetCall
func (c *ProjectsLocationsInsightsGetCall) Header() http.Header
func (c *ProjectsLocationsInsightsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsGetCall
func (c *ProjectsLocationsInsightsGetCall) View(view string) *ProjectsLocationsInsightsGetCall
type ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Aggregation(aggregation string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Context(ctx context.Context) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse, error)
func (c *ProjectsLocationsInsightsListCall) EndTime(endTime string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Filter(filter string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Header() http.Header
func (c *ProjectsLocationsInsightsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) OrderBy(orderBy string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) PageSize(pageSize int64) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) PageToken(pageToken string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) Pages(ctx context.Context, ...) error
func (c *ProjectsLocationsInsightsListCall) StartTime(startTime string) *ProjectsLocationsInsightsListCall
func (c *ProjectsLocationsInsightsListCall) View(view string) *ProjectsLocationsInsightsListCall
type ProjectsLocationsInsightsService
func NewProjectsLocationsInsightsService(s *Service) *ProjectsLocationsInsightsService
func (r *ProjectsLocationsInsightsService) ConfiguredInsight(insight string) *ProjectsLocationsInsightsConfiguredInsightCall
func (r *ProjectsLocationsInsightsService) Get(name string) *ProjectsLocationsInsightsGetCall
func (r *ProjectsLocationsInsightsService) List(parent string) *ProjectsLocationsInsightsListCall
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
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication, error)
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
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse, error)
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
func (c *ProjectsLocationsSecurityGatewaysGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway, error)
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
func (c *ProjectsLocationsSecurityGatewaysListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse, ...)
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
type RemoteAgentDetails
type ReportStatusRequest
func (s ReportStatusRequest) MarshalJSON() ([]byte, error)
type ResolveConnectionsResponse
func (s ResolveConnectionsResponse) MarshalJSON() ([]byte, error)
type ResolveInstanceConfigResponse
func (s ResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type ResourceInfo
func (s ResourceInfo) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type ServiceAccount
func (s ServiceAccount) MarshalJSON() ([]byte, error)
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
func (s AllocatedConnection) MarshalJSON() ([]byte, error)
type AppGateway ¶
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
func (s AppGateway) MarshalJSON() ([]byte, error)
type AppGatewayOperationMetadata ¶
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
func (s AppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type ApplicationEndpoint ¶
type ApplicationEndpoint struct {
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

ApplicationEndpoint: ApplicationEndpoint represents a remote application endpoint.

func (ApplicationEndpoint) MarshalJSON ¶
func (s ApplicationEndpoint) MarshalJSON() ([]byte, error)
type CloudPubSubNotificationConfig ¶
type CloudPubSubNotificationConfig struct {
	// PubsubSubscription: The Pub/Sub subscription the connector uses to receive
	// notifications.
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

CloudPubSubNotificationConfig: The configuration for Pub/Sub messaging for the connector.

func (CloudPubSubNotificationConfig) MarshalJSON ¶
func (s CloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
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

type Connection ¶
type Connection struct {
	// ApplicationEndpoint: Required. Address of the remote application endpoint
	// for the BeyondCorp Connection.
	ApplicationEndpoint *ApplicationEndpoint `json:"applicationEndpoint,omitempty"`
	// Connectors: Optional. List of
	// [google.cloud.beyondcorp.v1main.Connector.name] that are authorised to be
	// associated with this Connection.
	Connectors []string `json:"connectors,omitempty"`
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the connection.
	// Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Gateway: Optional. Gateway used by the connection.
	Gateway *Gateway `json:"gateway,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Required. Unique resource name of the connection. The name is ignored
	// when creating a connection.
	Name string `json:"name,omitempty"`
	// State: Output only. The current state of the connection.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - Connection is being created.
	//   "CREATED" - Connection has been created.
	//   "UPDATING" - Connection's configuration is being updated.
	//   "DELETING" - Connection is being deleted.
	//   "DOWN" - Connection is down and may be restored in the future. This
	// happens when CCFE sends ProjectState = OFF.
	State string `json:"state,omitempty"`
	// Type: Required. The type of network connectivity used by the connection.
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

Connection: A BeyondCorp Connection resource represents a BeyondCorp protected connection to a remote application. It creates all the necessary GCP components needed for creating a BeyondCorp protected connection. Multiple connectors can be authorised for a single Connection.

func (Connection) MarshalJSON ¶
func (s Connection) MarshalJSON() ([]byte, error)
type ConnectionDetails ¶
type ConnectionDetails struct {
	// Connection: A BeyondCorp Connection in the project.
	Connection *Connection `json:"connection,omitempty"`
	// RecentMigVms: If type=GCP_REGIONAL_MIG, contains most recent VM instances,
	// like
	// "https://www.googleapis.com/compute/v1/projects/{project_id}/zones/{zone_id}/
	// instances/{instance_id}".
	RecentMigVms []string `json:"recentMigVms,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Connection") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Connection") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConnectionDetails: Details of the Connection.

func (ConnectionDetails) MarshalJSON ¶
func (s ConnectionDetails) MarshalJSON() ([]byte, error)
type ConnectionOperationMetadata ¶
type ConnectionOperationMetadata struct {
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

ConnectionOperationMetadata: Represents the metadata of the long-running operation.

func (ConnectionOperationMetadata) MarshalJSON ¶
func (s ConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type Connector ¶
type Connector struct {
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the connector.
	// Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Required. Unique resource name of the connector. The name is ignored
	// when creating a connector.
	Name string `json:"name,omitempty"`
	// PrincipalInfo: Required. Principal information about the Identity of the
	// connector.
	PrincipalInfo *PrincipalInfo `json:"principalInfo,omitempty"`
	// ResourceInfo: Optional. Resource info of the connector.
	ResourceInfo *ResourceInfo `json:"resourceInfo,omitempty"`
	// State: Output only. The current state of the connector.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - Connector is being created.
	//   "CREATED" - Connector has been created.
	//   "UPDATING" - Connector's configuration is being updated.
	//   "DELETING" - Connector is being deleted.
	//   "DOWN" - Connector is down and may be restored in the future. This happens
	// when CCFE sends ProjectState = OFF.
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

Connector: A BeyondCorp connector resource that represents an application facing component deployed proximal to and with direct access to the application instances. It is used to establish connectivity between the remote enterprise environment and GCP. It initiates connections to the applications and can proxy the data from users over the connection.

func (Connector) MarshalJSON ¶
func (s Connector) MarshalJSON() ([]byte, error)
type ConnectorInstanceConfig ¶
type ConnectorInstanceConfig struct {
	// ImageConfig: ImageConfig defines the GCR images to run for the remote
	// agent's control plane.
	ImageConfig *ImageConfig `json:"imageConfig,omitempty"`
	// InstanceConfig: The SLM instance agent configuration.
	InstanceConfig googleapi.RawMessage `json:"instanceConfig,omitempty"`
	// NotificationConfig: NotificationConfig defines the notification mechanism
	// that the remote instance should subscribe to in order to receive
	// notification.
	NotificationConfig *NotificationConfig `json:"notificationConfig,omitempty"`
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

ConnectorInstanceConfig: ConnectorInstanceConfig defines the instance config of a connector.

func (ConnectorInstanceConfig) MarshalJSON ¶
func (s ConnectorInstanceConfig) MarshalJSON() ([]byte, error)
type ConnectorOperationMetadata ¶
type ConnectorOperationMetadata struct {
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

ConnectorOperationMetadata: Represents the metadata of the long-running operation.

func (ConnectorOperationMetadata) MarshalJSON ¶
func (s ConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type ContainerHealthDetails ¶
type ContainerHealthDetails struct {
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

ContainerHealthDetails: ContainerHealthDetails reflects the health details of a container.

func (ContainerHealthDetails) MarshalJSON ¶
func (s ContainerHealthDetails) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Gateway ¶
type Gateway struct {
	// Type: Required. The type of hosting used by the gateway.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "GCP_REGIONAL_MIG" - Gateway hosted in a GCP regional managed instance
	// group.
	Type string `json:"type,omitempty"`
	// Uri: Output only. Server-defined URI for this resource.
	Uri string `json:"uri,omitempty"`
	// UserPort: Output only. User port reserved on the gateways for this
	// connection, if not specified or zero, the default port is 19443.
	UserPort int64 `json:"userPort,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Type") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Type") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Gateway: Gateway represents a user facing component that serves as an entrance to enable connectivity.

func (Gateway) MarshalJSON ¶
func (s Gateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata ¶
added in v0.88.0
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
added in v0.88.0
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection struct {
	// ApplicationEndpoint: Required. Address of the remote application endpoint
	// for the BeyondCorp AppConnection.
	ApplicationEndpoint *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint `json:"applicationEndpoint,omitempty"`
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
	Gateway *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway `json:"gateway,omitempty"`
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

GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection: A BeyondCorp AppConnection resource represents a BeyondCorp protected AppConnection to a remote application. It creates all the necessary GCP components needed for creating a BeyondCorp protected AppConnection. Multiple connectors can be authorised for a single AppConnection.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint struct {
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

GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint: ApplicationEndpoint represents a remote application endpoint.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway struct {
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

GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway: Gateway represents a user facing component that serves as an entrance to enable connectivity.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway) MarshalJSON() ([]byte, error)
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
type GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse struct {
	// AppConnections: A list of BeyondCorp AppConnections in the project.
	AppConnections []*GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection `json:"appConnections,omitempty"`
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

GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse: Response message for BeyondCorp.ListAppConnections.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse struct {
	// AppConnectionDetails: A list of BeyondCorp AppConnections with details in
	// the project.
	AppConnectionDetails []*GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails `json:"appConnectionDetails,omitempty"`
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

GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse: Response message for BeyondCorp.ResolveAppConnections.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails struct {
	// AppConnection: A BeyondCorp AppConnection in the project.
	AppConnection *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection `json:"appConnection,omitempty"`
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

GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppCon nectionDetails: Details of the AppConnection.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata ¶
added in v0.88.0
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
added in v0.88.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails ¶
added in v0.88.0
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
added in v0.88.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails ¶
added in v0.88.0
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails struct {
}

GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector struct {
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
	PrincipalInfo *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo `json:"principalInfo,omitempty"`
	// ResourceInfo: Optional. Resource info of the connector.
	ResourceInfo *GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo `json:"resourceInfo,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector: A BeyondCorp connector resource that represents an application facing component deployed proximal to and with direct access to the application instances. It is used to establish connectivity between the remote enterprise environment and GCP. It initiates connections to the applications and can proxy the data from users over the connection.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig struct {
	// ImageConfig: ImageConfig defines the GCR images to run for the remote
	// agent's control plane.
	ImageConfig *GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig `json:"imageConfig,omitempty"`
	// InstanceConfig: The SLM instance agent configuration.
	InstanceConfig googleapi.RawMessage `json:"instanceConfig,omitempty"`
	// NotificationConfig: NotificationConfig defines the notification mechanism
	// that the remote instance should subscribe to in order to receive
	// notification.
	NotificationConfig *GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig `json:"notificationConfig,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig: AppConnectorInstanceConfig defines the instance config of a AppConnector.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig) MarshalJSON() ([]byte, error)
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
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo struct {
	// ServiceAccount: A GCP service account.
	ServiceAccount *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount `json:"serviceAccount,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo: PrincipalInfo represents an Identity oneof.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount struct {
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

GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAcco unt: ServiceAccount represents a GCP service account.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails ¶
added in v0.86.0
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
added in v0.86.0
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig struct {
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

GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig: ImageConfig defines the control plane images to run.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse struct {
	// AppConnectors: A list of BeyondCorp AppConnectors in the project.
	AppConnectors []*GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector `json:"appConnectors,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse: Response message for BeyondCorp.ListAppConnectors.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig struct {
	// PubsubNotification: Cloud Pub/Sub Configuration to receive notifications.
	PubsubNotification *GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig `json:"pubsubNotification,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig: NotificationConfig defines the mechanisms to notify instance agent.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig struct {
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

GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotific ationConfig: The configuration for Pub/Sub messaging for the AppConnector.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails ¶
added in v0.86.0
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails struct {
}

GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest struct {
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
	ResourceInfo *GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo `json:"resourceInfo,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest: Request report the connector status.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse struct {
	// InstanceConfig: AppConnectorInstanceConfig.
	InstanceConfig *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig `json:"instanceConfig,omitempty"`

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

GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse: Response message for BeyondCorp.ResolveInstanceConfig.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo struct {
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
	Sub []*GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo `json:"sub,omitempty"`
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

GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo: ResourceInfo represents the information/status of an app connector resource. Such as: - remote_agent - container - runtime - appgateway - appconnector - appconnection - tunnel - logagent

func (GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata ¶
added in v0.88.0
type GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata struct {
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

GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata) MarshalJSON ¶
added in v0.88.0
func (s GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
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
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig struct {
	// Aggregation: Output only. Aggregation type applied.
	//
	// Possible values:
	//   "AGGREGATION_UNSPECIFIED" - Unspecified.
	//   "HOURLY" - Insight should be aggregated at hourly level.
	//   "DAILY" - Insight should be aggregated at daily level.
	//   "WEEKLY" - Insight should be aggregated at weekly level.
	//   "MONTHLY" - Insight should be aggregated at monthly level.
	//   "CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date
	// range passed in as the start and end time in the request.
	Aggregation string `json:"aggregation,omitempty"`
	// CustomGrouping: Output only. Customised grouping applied.
	CustomGrouping *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping `json:"customGrouping,omitempty"`
	// EndTime: Output only. Ending time for the duration for which insight was
	// pulled.
	EndTime string `json:"endTime,omitempty"`
	// FieldFilter: Output only. Filters applied.
	FieldFilter string `json:"fieldFilter,omitempty"`
	// Group: Output only. Group id of the grouping applied.
	Group string `json:"group,omitempty"`
	// StartTime: Output only. Starting time for the duration for which insight was
	// pulled.
	StartTime string `json:"startTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Aggregation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Aggregation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig: The configuration that was applied to generate the result.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse struct {
	// AppliedConfig: Output only. Applied insight config to generate the result
	// data rows.
	AppliedConfig *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig `json:"appliedConfig,omitempty"`
	// NextPageToken: Output only. Next page token to be fetched. Set to empty or
	// NULL if there are no more pages available.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Rows: Output only. Result rows returned containing the required value(s) for
	// configured insight.
	Rows []*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow `json:"rows,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppliedConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppliedConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse: The response for the configured insight.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping struct {
	// FieldFilter: Optional. Filterable parameters to be added to the grouping
	// clause. Available fields could be fetched by calling insight list and get
	// APIs in `BASIC` view. `=` is the only comparison operator supported. `AND`
	// is the only logical operator supported. Usage:
	// field_filter="fieldName1=fieldVal1 AND fieldName2=fieldVal2". NOTE: Only
	// `AND` conditions are allowed. NOTE: Use the `filter_alias` from
	// `Insight.Metadata.Field` message for the filtering the corresponding fields
	// in this filter field. (These expressions are based on the filter language
	// described at https://google.aip.dev/160).
	FieldFilter string `json:"fieldFilter,omitempty"`
	// GroupFields: Required. Fields to be used for grouping. NOTE: Use the
	// `filter_alias` from `Insight.Metadata.Field` message for declaring the
	// fields to be grouped-by here.
	GroupFields []string `json:"groupFields,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldFilter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping: Customised grouping option that allows setting the group_by fields and also the filters togather for a configured insight request.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight struct {
	// AppliedConfig: Output only. Applied insight config to generate the result
	// data rows.
	AppliedConfig *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig `json:"appliedConfig,omitempty"`
	// Metadata: Output only. Metadata for the Insight.
	Metadata *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata `json:"metadata,omitempty"`
	// Name: Output only. The insight resource name. e.g.
	// `organizations/{organization_id}/locations/{location_id}/insights/{insight_id
	// }` OR `projects/{project_id}/locations/{location_id}/insights/{insight_id}`.
	Name string `json:"name,omitempty"`
	// Rows: Output only. Result rows returned containing the required value(s).
	Rows []*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow `json:"rows,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppliedConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppliedConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight: The Insight object with configuration that was returned and actual list of records.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata struct {
	// Aggregations: Output only. List of aggregation types available for insight.
	//
	// Possible values:
	//   "AGGREGATION_UNSPECIFIED" - Unspecified.
	//   "HOURLY" - Insight should be aggregated at hourly level.
	//   "DAILY" - Insight should be aggregated at daily level.
	//   "WEEKLY" - Insight should be aggregated at weekly level.
	//   "MONTHLY" - Insight should be aggregated at monthly level.
	//   "CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date
	// range passed in as the start and end time in the request.
	Aggregations []string `json:"aggregations,omitempty"`
	// Category: Output only. Category of the insight.
	Category string `json:"category,omitempty"`
	// DisplayName: Output only. Common name of the insight.
	DisplayName string `json:"displayName,omitempty"`
	// Fields: Output only. List of fields available for insight.
	Fields []*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField `json:"fields,omitempty"`
	// Groups: Output only. List of groupings available for insight.
	Groups []string `json:"groups,omitempty"`
	// SubCategory: Output only. Sub-Category of the insight.
	SubCategory string `json:"subCategory,omitempty"`
	// Type: Output only. Type of the insight. It is metadata describing whether
	// the insight is a metric (e.g. count) or a report (e.g. list, status).
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Aggregations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Aggregations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata: Insight filters, groupings and aggregations that can be applied for the insight. Examples: aggregations, groups, field filters.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField struct {
	// Description: Output only. Description of the field.
	Description string `json:"description,omitempty"`
	// DisplayName: Output only. Name of the field.
	DisplayName string `json:"displayName,omitempty"`
	// FilterAlias: Output only. Field name to be used in filter while requesting
	// configured insight filtered on this field.
	FilterAlias string `json:"filterAlias,omitempty"`
	// Filterable: Output only. Indicates whether the field can be used for
	// filtering.
	Filterable bool `json:"filterable,omitempty"`
	// Groupable: Output only. Indicates whether the field can be used for grouping
	// in custom grouping request.
	Groupable bool `json:"groupable,omitempty"`
	// Id: Output only. Field id for which this is the metadata.
	Id string `json:"id,omitempty"`
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

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField: Field metadata. Commonly understandable name and description for the field. Multiple such fields constitute the Insight.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse struct {
	// Insights: Output only. List of all insights.
	Insights []*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight `json:"insights,omitempty"`
	// NextPageToken: Output only. Next page token to be fetched. Set to empty or
	// NULL if there are no more pages available.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Insights") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Insights") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse: The response for the list of insights.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow struct {
	// FieldValues: Output only. Columns/entries/key-vals in the result.
	FieldValues []*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal `json:"fieldValues,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldValues") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow: Row of the fetch response consisting of a set of entries.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal ¶
added in v0.92.0
type GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal struct {
	// DisplayName: Output only. Name of the field.
	DisplayName string `json:"displayName,omitempty"`
	// FilterAlias: Output only. Field name to be used in filter while requesting
	// configured insight filtered on this field.
	FilterAlias string `json:"filterAlias,omitempty"`
	// Id: Output only. Field id.
	Id string `json:"id,omitempty"`
	// Value: Output only. Value of the field in string format. Acceptable values
	// are strings or numbers.
	Value string `json:"value,omitempty"`
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

GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal: Column or key value pair from the request as part of key to use in query or a single pair of the fetch response.

func (GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal) MarshalJSON ¶
added in v0.92.0
func (s GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse ¶
added in v0.178.0
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse struct {
	// EffectiveCancellationTime: Time when the cancellation will become effective
	EffectiveCancellationTime string `json:"effectiveCancellationTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EffectiveCancellationTime")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EffectiveCancellationTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionRespon se: Response message for BeyondCorp.CancelSubscription

func (GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse) MarshalJSON ¶
added in v0.178.0
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse ¶
added in v0.101.0
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse struct {
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Subscriptions: A list of BeyondCorp Subscriptions in the organization.
	Subscriptions []*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription `json:"subscriptions,omitempty"`

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

GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsRespons e: Response message for BeyondCorp.ListSubscriptions.

func (GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse) MarshalJSON ¶
added in v0.101.0
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse ¶
added in v0.182.0
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionRespo nse: Response message for BeyondCorp.RestartSubscription

type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription ¶
added in v0.101.0
type GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription struct {
	// AutoRenewEnabled: Output only. Represents that, if subscription will renew
	// or end when the term ends.
	AutoRenewEnabled bool `json:"autoRenewEnabled,omitempty"`
	// BillingAccount: Optional. Name of the billing account in the format. e.g.
	// billingAccounts/123456-123456-123456 Required if Subscription is of Paid
	// type.
	BillingAccount string `json:"billingAccount,omitempty"`
	// CreateTime: Output only. Create time of the subscription.
	CreateTime string `json:"createTime,omitempty"`
	// CsgCustomer: Optional. Whether the subscription is being created as part of
	// the Citrix flow. If this field is set to true, the subscription should have
	// both the start_time and end_time set in the request and the billing account
	// used will be the Citrix master billing account regardless of what its set to
	// in the request. This field can only be set to true in create requests.
	CsgCustomer bool `json:"csgCustomer,omitempty"`
	// EndTime: Optional. End time of the subscription.
	EndTime string `json:"endTime,omitempty"`
	// Name: Identifier. Unique resource name of the Subscription. The name is
	// ignored when creating a subscription.
	Name string `json:"name,omitempty"`
	// SeatCount: Optional. Number of seats in the subscription.
	SeatCount int64 `json:"seatCount,omitempty,string"`
	// Sku: Required. SKU of subscription.
	//
	// Possible values:
	//   "SKU_UNSPECIFIED" - Default value. This value is unused.
	//   "BCE_STANDARD_SKU" - Represents BeyondCorp Standard SKU.
	Sku string `json:"sku,omitempty"`
	// StartTime: Optional. Start time of the subscription.
	StartTime string `json:"startTime,omitempty"`
	// State: Output only. The current state of the subscription.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "ACTIVE" - Represents an active subscription.
	//   "INACTIVE" - Represents an upcomming subscription.
	//   "COMPLETED" - Represents a completed subscription.
	State string `json:"state,omitempty"`
	// SubscriberType: Output only. Type of subscriber.
	//
	// Possible values:
	//   "SUBSCRIBER_TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "ONLINE" - Represents an online subscription.
	//   "OFFLINE" - Represents an offline subscription.
	SubscriberType string `json:"subscriberType,omitempty"`
	// Type: Required. Type of subscription.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "TRIAL" - Represents a trial subscription.
	//   "PAID" - Represents a paid subscription.
	//   "ALLOWLIST" - Reresents an allowlisted subscription.
	Type string `json:"type,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AutoRenewEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoRenewEnabled") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription: A BeyondCorp Subscription resource represents BeyondCorp Enterprise Subscription. BeyondCorp Enterprise Subscription enables BeyondCorp Enterprise permium features for an organization.

func (GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription) MarshalJSON ¶
added in v0.101.0
func (s GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription) MarshalJSON() ([]byte, error)
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
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication ¶
added in v0.193.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication struct {
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
	EndpointMatchers []*GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher `json:"endpointMatchers,omitempty"`
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
	Upstreams []*GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream `json:"upstreams,omitempty"`

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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication: The information about an application resource.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication) MarshalJSON ¶
added in v0.193.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream struct {
	// EgressPolicy: Optional. Routing policy information.
	EgressPolicy *GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy `json:"egressPolicy,omitempty"`
	// External: List of the external endpoints to forward traffic to.
	External *GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal `json:"external,omitempty"`
	// Network: Network to forward traffic to.
	Network *GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork `json:"network,omitempty"`
	// ProxyProtocol: Optional. Enables proxy protocol configuration for the
	// upstream.
	ProxyProtocol *GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig `json:"proxyProtocol,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream: Which upstream resource to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal struct {
	// Endpoints: Required. List of the endpoints to forward traffic to.
	Endpoints []*GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint `json:"endpoints,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal: Endpoints to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork: Network to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders struct {
	// DeviceInfo: Optional. The device information configuration.
	DeviceInfo *GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo `json:"deviceInfo,omitempty"`
	// GroupInfo: Optional. Group details.
	GroupInfo *GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo `json:"groupInfo,omitempty"`
	// OutputType: Optional. Default output type for all enabled headers.
	//
	// Possible values:
	//   "OUTPUT_TYPE_UNSPECIFIED" - The unspecified output type.
	//   "PROTOBUF" - Protobuf output type.
	//   "JSON" - JSON output type.
	//   "NONE" - Explicitly disable header output.
	OutputType string `json:"outputType,omitempty"`
	// UserInfo: Optional. User details.
	UserInfo *GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo `json:"userInfo,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders: Contextual headers configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceI nfo: The delegated device information configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupIn fo: The delegated group configuration details.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInf o: The configuration information for the delegated user.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy: Routing policy information.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint: Internet Gateway endpoint to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher ¶
added in v0.198.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher: EndpointMatcher contains the information of the endpoint that will match the application.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher) MarshalJSON ¶
added in v0.198.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub ¶
added in v0.193.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub struct {
	// InternetGateway: Optional. Internet Gateway configuration.
	InternetGateway *GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway `json:"internetGateway,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub: The Hub message contains information pertaining to the regional data path deployments.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub) MarshalJSON ¶
added in v0.193.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway ¶
added in v0.201.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway: Represents the Internet Gateway configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway) MarshalJSON ¶
added in v0.201.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse ¶
added in v0.193.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse struct {
	// Applications: A list of BeyondCorp Application in the project.
	Applications []*GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication `json:"applications,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse: Message for response to listing Applications.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse) MarshalJSON ¶
added in v0.193.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse ¶
added in v0.170.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse struct {
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SecurityGateways: A list of BeyondCorp SecurityGateway in the project.
	SecurityGateways []*GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway `json:"securityGateways,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse: Message for response to listing SecurityGateways.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse) MarshalJSON ¶
added in v0.170.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig struct {
	// AllowedClientHeaders: Optional. List of the allowed client header names.
	AllowedClientHeaders []string `json:"allowedClientHeaders,omitempty"`
	// ClientIp: Optional. Client IP configuration. The client IP address is
	// included if true.
	ClientIp bool `json:"clientIp,omitempty"`
	// ContextualHeaders: Optional. Configuration for the contextual headers.
	ContextualHeaders *GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders `json:"contextualHeaders,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig: The configuration for the proxy.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway ¶
added in v0.170.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway struct {
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
	Hubs map[string]GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub `json:"hubs,omitempty"`
	// Name: Identifier. Name of the resource.
	Name string `json:"name,omitempty"`
	// ProxyProtocolConfig: Optional. Shared proxy configuration for all apps.
	ProxyProtocolConfig *GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig `json:"proxyProtocolConfig,omitempty"`
	// ServiceDiscovery: Optional. Settings related to the Service Discovery.
	ServiceDiscovery *GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery `json:"serviceDiscovery,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway: The information about a security gateway resource.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway) MarshalJSON ¶
added in v0.170.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway) MarshalJSON() ([]byte, error)
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
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery struct {
	// ApiGateway: Required. External API configuration.
	ApiGateway *GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway `json:"apiGateway,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery: Settings related to the Service Discovery.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway struct {
	// ResourceOverride: Required. Enables fetching resource model updates to alter
	// service behavior per Chrome profile.
	ResourceOverride *GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor `json:"resourceOverride,omitempty"`
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway: If Service Discovery is done through API, defines its settings.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor struct {
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

GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperati onDescriptor: API operation descriptor.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON() ([]byte, error)
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
type ImageConfig ¶
type ImageConfig struct {
	// StableImage: The stable image that the remote agent will fallback to if the
	// target image fails.
	StableImage string `json:"stableImage,omitempty"`
	// TargetImage: The initial image the remote agent will attempt to run for the
	// control plane.
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

ImageConfig: ImageConfig defines the control plane images to run.

func (ImageConfig) MarshalJSON ¶
func (s ImageConfig) MarshalJSON() ([]byte, error)
type ListAppGatewaysResponse ¶
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
func (s ListAppGatewaysResponse) MarshalJSON() ([]byte, error)
type ListConnectionsResponse ¶
type ListConnectionsResponse struct {
	// Connections: A list of BeyondCorp Connections in the project.
	Connections []*Connection `json:"connections,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Connections") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Connections") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListConnectionsResponse: Response message for BeyondCorp.ListConnections.

func (ListConnectionsResponse) MarshalJSON ¶
func (s ListConnectionsResponse) MarshalJSON() ([]byte, error)
type ListConnectorsResponse ¶
type ListConnectorsResponse struct {
	// Connectors: A list of BeyondCorp Connectors in the project.
	Connectors []*Connector `json:"connectors,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Connectors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Connectors") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListConnectorsResponse: Response message for BeyondCorp.ListConnectors.

func (ListConnectorsResponse) MarshalJSON ¶
func (s ListConnectorsResponse) MarshalJSON() ([]byte, error)
type NotificationConfig ¶
type NotificationConfig struct {
	// PubsubNotification: Pub/Sub topic for Connector to subscribe and receive
	// notifications from `projects/{project}/topics/{pubsub_topic}`
	PubsubNotification *CloudPubSubNotificationConfig `json:"pubsubNotification,omitempty"`
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

NotificationConfig: NotificationConfig defines the mechanisms to notify instance agent.

func (NotificationConfig) MarshalJSON ¶
func (s NotificationConfig) MarshalJSON() ([]byte, error)
type OrganizationsLocationsInsightsConfiguredInsightCall ¶
added in v0.92.0
type OrganizationsLocationsInsightsConfiguredInsightCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsInsightsConfiguredInsightCall) Aggregation ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Aggregation(aggregation string) *OrganizationsLocationsInsightsConfiguredInsightCall

Aggregation sets the optional parameter "aggregation": Required. Aggregation type. Available aggregation could be fetched by calling insight list and get APIs in `BASIC` view.

Possible values:

"AGGREGATION_UNSPECIFIED" - Unspecified.
"HOURLY" - Insight should be aggregated at hourly level.
"DAILY" - Insight should be aggregated at daily level.
"WEEKLY" - Insight should be aggregated at weekly level.
"MONTHLY" - Insight should be aggregated at monthly level.
"CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date


range passed in as the start and end time in the request.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Context ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Context(ctx context.Context) *OrganizationsLocationsInsightsConfiguredInsightCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter(customGroupingFieldFilter string) *OrganizationsLocationsInsightsConfiguredInsightCall

CustomGroupingFieldFilter sets the optional parameter "customGrouping.fieldFilter": Filterable parameters to be added to the grouping clause. Available fields could be fetched by calling insight list and get APIs in `BASIC` view. `=` is the only comparison operator supported. `AND` is the only logical operator supported. Usage: field_filter="fieldName1=fieldVal1 AND fieldName2=fieldVal2". NOTE: Only `AND` conditions are allowed. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields(customGroupingGroupFields ...string) *OrganizationsLocationsInsightsConfiguredInsightCall

CustomGroupingGroupFields sets the optional parameter "customGrouping.groupFields": Required. Fields to be used for grouping. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for declaring the fields to be grouped-by here.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Do ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse, error)

Do executes the "beyondcorp.organizations.locations.insights.configuredInsight" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse.Se rverResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) EndTime ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) EndTime(endTime string) *OrganizationsLocationsInsightsConfiguredInsightCall

EndTime sets the optional parameter "endTime": Required. Ending time for the duration for which insight is to be pulled.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) FieldFilter ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) FieldFilter(fieldFilter string) *OrganizationsLocationsInsightsConfiguredInsightCall

FieldFilter sets the optional parameter "fieldFilter": Other filterable/configurable parameters as applicable to the selected insight. Available fields could be fetched by calling insight list and get APIs in `BASIC` view. `=` is the only comparison operator supported. `AND` is the only logical operator supported. Usage: field_filter="fieldName1=fieldVal1 AND fieldName2=fieldVal2". NOTE: Only `AND` conditions are allowed. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Fields ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsConfiguredInsightCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Group ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Group(group string) *OrganizationsLocationsInsightsConfiguredInsightCall

Group sets the optional parameter "group": Group id of the available groupings for the insight. Available groupings could be fetched by calling insight list and get APIs in `BASIC` view.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Header ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) IfNoneMatch ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsConfiguredInsightCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) PageSize ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) PageSize(pageSize int64) *OrganizationsLocationsInsightsConfiguredInsightCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) PageToken ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) PageToken(pageToken string) *OrganizationsLocationsInsightsConfiguredInsightCall

PageToken sets the optional parameter "pageToken": Used to fetch the page represented by the token. Fetches the first page when not set.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) Pages ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*OrganizationsLocationsInsightsConfiguredInsightCall) StartTime ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsConfiguredInsightCall) StartTime(startTime string) *OrganizationsLocationsInsightsConfiguredInsightCall

StartTime sets the optional parameter "startTime": Required. Starting time for the duration for which insight is to be pulled.

type OrganizationsLocationsInsightsGetCall ¶
added in v0.92.0
type OrganizationsLocationsInsightsGetCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsInsightsGetCall) Context ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) Context(ctx context.Context) *OrganizationsLocationsInsightsGetCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsInsightsGetCall) Do ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight, error)

Do executes the "beyondcorp.organizations.locations.insights.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsInsightsGetCall) Fields ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsInsightsGetCall) Header ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsInsightsGetCall) IfNoneMatch ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsInsightsGetCall) View ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsGetCall) View(view string) *OrganizationsLocationsInsightsGetCall

View sets the optional parameter "view": Required. Metadata only or full data view.

Possible values:

"INSIGHT_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Include basic metadata about the insight, but not the insight


data. This is the default value (for both ListInsights and GetInsight).

"FULL" - Include everything.

type OrganizationsLocationsInsightsListCall ¶
added in v0.92.0
type OrganizationsLocationsInsightsListCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsInsightsListCall) Aggregation ¶
added in v0.191.0
func (c *OrganizationsLocationsInsightsListCall) Aggregation(aggregation string) *OrganizationsLocationsInsightsListCall

Aggregation sets the optional parameter "aggregation": Aggregation type. The default is 'DAILY'.

Possible values:

"AGGREGATION_UNSPECIFIED" - Unspecified.
"HOURLY" - Insight should be aggregated at hourly level.
"DAILY" - Insight should be aggregated at daily level.
"WEEKLY" - Insight should be aggregated at weekly level.
"MONTHLY" - Insight should be aggregated at monthly level.
"CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date


range passed in as the start and end time in the request.

func (*OrganizationsLocationsInsightsListCall) Context ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Context(ctx context.Context) *OrganizationsLocationsInsightsListCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsInsightsListCall) Do ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse, error)

Do executes the "beyondcorp.organizations.locations.insights.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse.ServerR esponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsInsightsListCall) EndTime ¶
added in v0.191.0
func (c *OrganizationsLocationsInsightsListCall) EndTime(endTime string) *OrganizationsLocationsInsightsListCall

EndTime sets the optional parameter "endTime": Ending time for the duration for which insights are to be pulled. The default is the current time.

func (*OrganizationsLocationsInsightsListCall) Fields ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsInsightsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsInsightsListCall) Filter ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Filter(filter string) *OrganizationsLocationsInsightsListCall

Filter sets the optional parameter "filter": Filter expression to restrict the insights returned. Supported filter fields: * `type` * `category` * `subCategory` Examples: * "category = application AND type = count" * "category = application AND subCategory = iap" * "type = status" Allowed values: * type: [count, latency, status, list] * category: [application, device, request, security] * subCategory: [iap, caa, webprotect] NOTE: Only equality based comparison is allowed. Only `AND` conjunction is allowed. NOTE: The 'AND' in the filter field needs to be in capital letters only. NOTE: Just filtering on `subCategory` is not allowed. It should be passed in with the parent `category` too. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*OrganizationsLocationsInsightsListCall) Header ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsInsightsListCall) IfNoneMatch ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsInsightsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsInsightsListCall) OrderBy ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) OrderBy(orderBy string) *OrganizationsLocationsInsightsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results. This is currently ignored.

func (*OrganizationsLocationsInsightsListCall) PageSize ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) PageSize(pageSize int64) *OrganizationsLocationsInsightsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. NOTE: Default page size is 50.

func (*OrganizationsLocationsInsightsListCall) PageToken ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) PageToken(pageToken string) *OrganizationsLocationsInsightsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*OrganizationsLocationsInsightsListCall) Pages ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*OrganizationsLocationsInsightsListCall) StartTime ¶
added in v0.191.0
func (c *OrganizationsLocationsInsightsListCall) StartTime(startTime string) *OrganizationsLocationsInsightsListCall

StartTime sets the optional parameter "startTime": Starting time for the duration for which insights are to be pulled. The default is 7 days before the current time.

func (*OrganizationsLocationsInsightsListCall) View ¶
added in v0.92.0
func (c *OrganizationsLocationsInsightsListCall) View(view string) *OrganizationsLocationsInsightsListCall

View sets the optional parameter "view": Required. List only metadata or full data.

Possible values:

"INSIGHT_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Include basic metadata about the insight, but not the insight


data. This is the default value (for both ListInsights and GetInsight).

"FULL" - Include everything.

type OrganizationsLocationsInsightsService ¶
added in v0.92.0
type OrganizationsLocationsInsightsService struct {
	// contains filtered or unexported fields
}
func NewOrganizationsLocationsInsightsService ¶
added in v0.92.0
func NewOrganizationsLocationsInsightsService(s *Service) *OrganizationsLocationsInsightsService
func (*OrganizationsLocationsInsightsService) ConfiguredInsight ¶
added in v0.92.0
func (r *OrganizationsLocationsInsightsService) ConfiguredInsight(insight string) *OrganizationsLocationsInsightsConfiguredInsightCall

ConfiguredInsight: Gets the value for a selected particular insight based on the provided filters. Use the organization level path for fetching at org level and project level path for fetching the insight value specific to a particular project.

insight: The resource name of the insight using the form: `organizations/{organization_id}/locations/{location_id}/insights/{insight_ id}` `projects/{project_id}/locations/{location_id}/insights/{insight_id}`.
func (*OrganizationsLocationsInsightsService) Get ¶
added in v0.92.0
func (r *OrganizationsLocationsInsightsService) Get(name string) *OrganizationsLocationsInsightsGetCall

Get: Gets the value for a selected particular insight with default configuration. The default aggregation level is 'DAILY' and no grouping will be applied or default grouping if applicable. The data will be returned for recent 7 days starting the day before. The insight data size will be limited to 50 rows. Use the organization level path for fetching at org level and project level path for fetching the insight value specific to a particular project. Setting the `view` to `BASIC` will only return the metadata for the insight.

name: The resource name of the insight using the form: `organizations/{organization_id}/locations/{location_id}/insights/{insight_ id}` `projects/{project_id}/locations/{location_id}/insights/{insight_id}`.
func (*OrganizationsLocationsInsightsService) List ¶
added in v0.92.0
func (r *OrganizationsLocationsInsightsService) List(parent string) *OrganizationsLocationsInsightsListCall

List: Lists for all the available insights that could be fetched from the system. Allows to filter using category. Setting the `view` to `BASIC` will let you iterate over the list of insight metadatas.

parent: The resource name of InsightMetadata using the form: `organizations/{organization_id}/locations/{location}` `projects/{project_id}/locations/{location_id}`.
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
added in v0.92.0
type OrganizationsLocationsService struct {
	Insights *OrganizationsLocationsInsightsService

	Operations *OrganizationsLocationsOperationsService

	Subscriptions *OrganizationsLocationsSubscriptionsService
	// contains filtered or unexported fields
}
func NewOrganizationsLocationsService ¶
added in v0.92.0
func NewOrganizationsLocationsService(s *Service) *OrganizationsLocationsService
type OrganizationsLocationsSubscriptionsCancelCall ¶
added in v0.178.0
type OrganizationsLocationsSubscriptionsCancelCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsCancelCall) Context ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsCancelCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsCancelCall) Do ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.cancel" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionRespo nse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsCancelCall) Fields ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsCancelCall) Header ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsSubscriptionsCancelCall) IfNoneMatch ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsCancelCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsSubscriptionsCancelCall) RequestId ¶
added in v0.178.0
func (c *OrganizationsLocationsSubscriptionsCancelCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsCancelCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type OrganizationsLocationsSubscriptionsCreateCall ¶
added in v0.101.0
type OrganizationsLocationsSubscriptionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsCreateCall) Context ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsCreateCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsCreateCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsCreateCall) Do ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.ServerResp onse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsCreateCall) Fields ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsCreateCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsCreateCall) Header ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsLocationsSubscriptionsGetCall ¶
added in v0.101.0
type OrganizationsLocationsSubscriptionsGetCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsGetCall) Context ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsGetCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsGetCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsGetCall) Do ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.ServerResp onse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsGetCall) Fields ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsGetCall) Header ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsSubscriptionsGetCall) IfNoneMatch ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrganizationsLocationsSubscriptionsListCall ¶
added in v0.101.0
type OrganizationsLocationsSubscriptionsListCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsListCall) Context ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsListCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsListCall) Do ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsRespon se.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsListCall) Fields ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsListCall) Header ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsSubscriptionsListCall) IfNoneMatch ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsSubscriptionsListCall) PageSize ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) PageSize(pageSize int64) *OrganizationsLocationsSubscriptionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*OrganizationsLocationsSubscriptionsListCall) PageToken ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) PageToken(pageToken string) *OrganizationsLocationsSubscriptionsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListSubscriptionsRequest, if any.

func (*OrganizationsLocationsSubscriptionsListCall) Pages ¶
added in v0.101.0
func (c *OrganizationsLocationsSubscriptionsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type OrganizationsLocationsSubscriptionsPatchCall ¶
added in v0.177.0
type OrganizationsLocationsSubscriptionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsPatchCall) Context ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsPatchCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsPatchCall) Do ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.ServerResp onse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsPatchCall) Fields ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsPatchCall) Header ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsSubscriptionsPatchCall) RequestId ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*OrganizationsLocationsSubscriptionsPatchCall) UpdateMask ¶
added in v0.177.0
func (c *OrganizationsLocationsSubscriptionsPatchCall) UpdateMask(updateMask string) *OrganizationsLocationsSubscriptionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Subscription resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. Mutable fields: seat_count.

type OrganizationsLocationsSubscriptionsRestartCall ¶
added in v0.182.0
type OrganizationsLocationsSubscriptionsRestartCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsSubscriptionsRestartCall) Context ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) Context(ctx context.Context) *OrganizationsLocationsSubscriptionsRestartCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsSubscriptionsRestartCall) Do ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse, error)

Do executes the "beyondcorp.organizations.locations.subscriptions.restart" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResp onse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsSubscriptionsRestartCall) Fields ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) Fields(s ...googleapi.Field) *OrganizationsLocationsSubscriptionsRestartCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsSubscriptionsRestartCall) Header ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsSubscriptionsRestartCall) IfNoneMatch ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) IfNoneMatch(entityTag string) *OrganizationsLocationsSubscriptionsRestartCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsSubscriptionsRestartCall) RequestId ¶
added in v0.182.0
func (c *OrganizationsLocationsSubscriptionsRestartCall) RequestId(requestId string) *OrganizationsLocationsSubscriptionsRestartCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type OrganizationsLocationsSubscriptionsService ¶
added in v0.101.0
type OrganizationsLocationsSubscriptionsService struct {
	// contains filtered or unexported fields
}
func NewOrganizationsLocationsSubscriptionsService ¶
added in v0.101.0
func NewOrganizationsLocationsSubscriptionsService(s *Service) *OrganizationsLocationsSubscriptionsService
func (*OrganizationsLocationsSubscriptionsService) Cancel ¶
added in v0.178.0
func (r *OrganizationsLocationsSubscriptionsService) Cancel(name string) *OrganizationsLocationsSubscriptionsCancelCall

Cancel: Cancels an existing BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization. Returns the timestamp for when the cancellation will become effective

- name: Name of the resource.

func (*OrganizationsLocationsSubscriptionsService) Create ¶
added in v0.101.0
func (r *OrganizationsLocationsSubscriptionsService) Create(parent string, googlecloudbeyondcorpsaasplatformsubscriptionsv1alphasubscription *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription) *OrganizationsLocationsSubscriptionsCreateCall

Create: Creates a new BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization.

parent: The resource name of the subscription location using the form: `organizations/{organization_id}/locations/{location}`.
func (*OrganizationsLocationsSubscriptionsService) Get ¶
added in v0.101.0
func (r *OrganizationsLocationsSubscriptionsService) Get(name string) *OrganizationsLocationsSubscriptionsGetCall

Get: Gets details of a single Subscription.

name: The resource name of Subscription using the form: `organizations/{organization_id}/locations/{location}/subscriptions/{subscr iption_id}`.
func (*OrganizationsLocationsSubscriptionsService) List ¶
added in v0.101.0
func (r *OrganizationsLocationsSubscriptionsService) List(parent string) *OrganizationsLocationsSubscriptionsListCall

List: Lists Subscriptions in a given organization and location.

parent: The resource name of Subscription using the form: `organizations/{organization_id}/locations/{location}`.
func (*OrganizationsLocationsSubscriptionsService) Patch ¶
added in v0.177.0
func (r *OrganizationsLocationsSubscriptionsService) Patch(name string, googlecloudbeyondcorpsaasplatformsubscriptionsv1alphasubscription *GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription) *OrganizationsLocationsSubscriptionsPatchCall

Patch: Updates an existing BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization.

name: Identifier. Unique resource name of the Subscription. The name is ignored when creating a subscription.
func (*OrganizationsLocationsSubscriptionsService) Restart ¶
added in v0.182.0
func (r *OrganizationsLocationsSubscriptionsService) Restart(name string) *OrganizationsLocationsSubscriptionsRestartCall

Restart: Restarts an existing BeyondCorp Enterprise Subscription in a given organization, that is scheduled for cancellation. Location will always be global as BeyondCorp subscriptions are per organization. Returns the timestamp for when the cancellation will become effective

- name: Name of the resource.

type OrganizationsService ¶
added in v0.92.0
type OrganizationsService struct {
	Locations *OrganizationsLocationsService
	// contains filtered or unexported fields
}
func NewOrganizationsService ¶
added in v0.92.0
func NewOrganizationsService(s *Service) *OrganizationsService
type PrincipalInfo ¶
type PrincipalInfo struct {
	// ServiceAccount: A GCP service account.
	ServiceAccount *ServiceAccount `json:"serviceAccount,omitempty"`
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

PrincipalInfo: PrincipalInfo represents an Identity oneof.

func (PrincipalInfo) MarshalJSON ¶
func (s PrincipalInfo) MarshalJSON() ([]byte, error)
type ProjectsLocationsAppConnectionsCreateCall ¶
type ProjectsLocationsAppConnectionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsCreateCall) AppConnectionId ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) AppConnectionId(appConnectionId string) *ProjectsLocationsAppConnectionsCreateCall

AppConnectionId sets the optional parameter "appConnectionId": User-settable AppConnection resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppConnectionsCreateCall) Context ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsCreateCall) Do ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsCreateCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsCreateCall) Header ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsCreateCall) RequestId ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectionsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsDeleteCall ¶
type ProjectsLocationsAppConnectionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsDeleteCall) Context ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsDeleteCall) Do ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsDeleteCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsDeleteCall) Header ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsDeleteCall) RequestId ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectionsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsGetCall ¶
type ProjectsLocationsAppConnectionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsGetCall) Context ¶
func (c *ProjectsLocationsAppConnectionsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsGetCall) Do ¶
func (c *ProjectsLocationsAppConnectionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection, error)

Do executes the "beyondcorp.projects.locations.appConnections.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsGetCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsGetCall) Header ¶
func (c *ProjectsLocationsAppConnectionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsGetCall) IfNoneMatch ¶
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
type ProjectsLocationsAppConnectionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsListCall) Context ¶
func (c *ProjectsLocationsAppConnectionsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsListCall) Do ¶
func (c *ProjectsLocationsAppConnectionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnections.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse.ServerR esponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsListCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsListCall) Filter ¶
func (c *ProjectsLocationsAppConnectionsListCall) Filter(filter string) *ProjectsLocationsAppConnectionsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppConnectionsListCall) Header ¶
func (c *ProjectsLocationsAppConnectionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectionsListCall) OrderBy ¶
func (c *ProjectsLocationsAppConnectionsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectionsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppConnectionsListCall) PageSize ¶
func (c *ProjectsLocationsAppConnectionsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectionsListCall) PageToken ¶
func (c *ProjectsLocationsAppConnectionsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppConnectionsRequest, if any.

func (*ProjectsLocationsAppConnectionsListCall) Pages ¶
func (c *ProjectsLocationsAppConnectionsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectionsPatchCall ¶
type ProjectsLocationsAppConnectionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsAppConnectionsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set as true, will create the resource if it is not found.

func (*ProjectsLocationsAppConnectionsPatchCall) Context ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsPatchCall) Do ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsPatchCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsPatchCall) Header ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsPatchCall) RequestId ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.AppConnection]: * `labels` * `display_name` * `application_endpoint` * `connectors`

func (*ProjectsLocationsAppConnectionsPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectionsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsResolveCall ¶
type ProjectsLocationsAppConnectionsResolveCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsResolveCall) AppConnectorId ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectionsResolveCall

AppConnectorId sets the optional parameter "appConnectorId": Required. BeyondCorp Connector name of the connector associated with those AppConnections using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_i d}`

func (*ProjectsLocationsAppConnectionsResolveCall) Context ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsResolveCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsResolveCall) Do ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnections.resolve" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse.Serv erResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsResolveCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsResolveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsResolveCall) Header ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsResolveCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsResolveCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectionsResolveCall) PageSize ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsResolveCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectionsResolveCall) PageToken ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsResolveCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ResolveAppConnectionsResponse, if any.

func (*ProjectsLocationsAppConnectionsResolveCall) Pages ¶
func (c *ProjectsLocationsAppConnectionsResolveCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectionsService ¶
type ProjectsLocationsAppConnectionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppConnectionsService ¶
func NewProjectsLocationsAppConnectionsService(s *Service) *ProjectsLocationsAppConnectionsService
func (*ProjectsLocationsAppConnectionsService) Create ¶
func (r *ProjectsLocationsAppConnectionsService) Create(parent string, googlecloudbeyondcorpappconnectionsv1alphaappconnection *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection) *ProjectsLocationsAppConnectionsCreateCall

Create: Creates a new AppConnection in a given project and location.

parent: The resource project name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectionsService) Delete ¶
func (r *ProjectsLocationsAppConnectionsService) Delete(name string) *ProjectsLocationsAppConnectionsDeleteCall

Delete: Deletes a single AppConnection.

name: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/appConnections/{app_connecti on_id}`.
func (*ProjectsLocationsAppConnectionsService) Get ¶
func (r *ProjectsLocationsAppConnectionsService) Get(name string) *ProjectsLocationsAppConnectionsGetCall

Get: Gets details of a single AppConnection.

name: BeyondCorp AppConnection name using the form: `projects/{project_id}/locations/{location_id}/appConnections/{app_connecti on_id}`.
func (*ProjectsLocationsAppConnectionsService) GetIamPolicy ¶
func (r *ProjectsLocationsAppConnectionsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectionsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectionsService) List ¶
func (r *ProjectsLocationsAppConnectionsService) List(parent string) *ProjectsLocationsAppConnectionsListCall

List: Lists AppConnections in a given project and location.

parent: The resource name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectionsService) Patch ¶
func (r *ProjectsLocationsAppConnectionsService) Patch(name string, googlecloudbeyondcorpappconnectionsv1alphaappconnection *GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection) *ProjectsLocationsAppConnectionsPatchCall

Patch: Updates the parameters of a single AppConnection.

name: Unique resource name of the AppConnection. The name is ignored when creating a AppConnection.
func (*ProjectsLocationsAppConnectionsService) Resolve ¶
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
type ProjectsLocationsAppConnectorsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsCreateCall) AppConnectorId ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectorsCreateCall

AppConnectorId sets the optional parameter "appConnectorId": User-settable AppConnector resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppConnectorsCreateCall) Context ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsCreateCall) Do ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsCreateCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsCreateCall) Header ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsCreateCall) RequestId ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectorsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsDeleteCall ¶
type ProjectsLocationsAppConnectorsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsDeleteCall) Context ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsDeleteCall) Do ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsDeleteCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsDeleteCall) Header ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsDeleteCall) RequestId ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectorsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsGetCall ¶
type ProjectsLocationsAppConnectorsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsGetCall) Context ¶
func (c *ProjectsLocationsAppConnectorsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsGetCall) Do ¶
func (c *ProjectsLocationsAppConnectorsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector, error)

Do executes the "beyondcorp.projects.locations.appConnectors.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsGetCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsGetCall) Header ¶
func (c *ProjectsLocationsAppConnectorsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsGetCall) IfNoneMatch ¶
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
type ProjectsLocationsAppConnectorsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsListCall) Context ¶
func (c *ProjectsLocationsAppConnectorsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsListCall) Do ¶
func (c *ProjectsLocationsAppConnectorsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnectors.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse.ServerRes ponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsListCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsListCall) Filter ¶
func (c *ProjectsLocationsAppConnectorsListCall) Filter(filter string) *ProjectsLocationsAppConnectorsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppConnectorsListCall) Header ¶
func (c *ProjectsLocationsAppConnectorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectorsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectorsListCall) OrderBy ¶
func (c *ProjectsLocationsAppConnectorsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectorsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppConnectorsListCall) PageSize ¶
func (c *ProjectsLocationsAppConnectorsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectorsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectorsListCall) PageToken ¶
func (c *ProjectsLocationsAppConnectorsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectorsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppConnectorsRequest, if any.

func (*ProjectsLocationsAppConnectorsListCall) Pages ¶
func (c *ProjectsLocationsAppConnectorsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectorsPatchCall ¶
type ProjectsLocationsAppConnectorsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsPatchCall) Context ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsPatchCall) Do ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsPatchCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsPatchCall) Header ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsPatchCall) RequestId ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectorsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.AppConnector]: * `labels` * `display_name`

func (*ProjectsLocationsAppConnectorsPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsAppConnectorsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsReportStatusCall ¶
type ProjectsLocationsAppConnectorsReportStatusCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsReportStatusCall) Context ¶
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsReportStatusCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Do ¶
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.reportStatus" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsReportStatusCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Header ¶
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppConnectorsResolveInstanceConfigCall ¶
type ProjectsLocationsAppConnectorsResolveInstanceConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Context ¶
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do ¶
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse, error)

Do executes the "beyondcorp.projects.locations.appConnectors.resolveInstanceConfig" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse.Serve rResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Header ¶
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAppConnectorsService ¶
type ProjectsLocationsAppConnectorsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppConnectorsService ¶
func NewProjectsLocationsAppConnectorsService(s *Service) *ProjectsLocationsAppConnectorsService
func (*ProjectsLocationsAppConnectorsService) Create ¶
func (r *ProjectsLocationsAppConnectorsService) Create(parent string, googlecloudbeyondcorpappconnectorsv1alphaappconnector *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector) *ProjectsLocationsAppConnectorsCreateCall

Create: Creates a new AppConnector in a given project and location.

parent: The resource project name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectorsService) Delete ¶
func (r *ProjectsLocationsAppConnectorsService) Delete(name string) *ProjectsLocationsAppConnectorsDeleteCall

Delete: Deletes a single AppConnector.

name: BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector _id}`.
func (*ProjectsLocationsAppConnectorsService) Get ¶
func (r *ProjectsLocationsAppConnectorsService) Get(name string) *ProjectsLocationsAppConnectorsGetCall

Get: Gets details of a single AppConnector.

name: BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector _id}`.
func (*ProjectsLocationsAppConnectorsService) GetIamPolicy ¶
func (r *ProjectsLocationsAppConnectorsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectorsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectorsService) List ¶
func (r *ProjectsLocationsAppConnectorsService) List(parent string) *ProjectsLocationsAppConnectorsListCall

List: Lists AppConnectors in a given project and location.

parent: The resource name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectorsService) Patch ¶
func (r *ProjectsLocationsAppConnectorsService) Patch(name string, googlecloudbeyondcorpappconnectorsv1alphaappconnector *GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector) *ProjectsLocationsAppConnectorsPatchCall

Patch: Updates the parameters of a single AppConnector.

name: Unique resource name of the AppConnector. The name is ignored when creating a AppConnector.
func (*ProjectsLocationsAppConnectorsService) ReportStatus ¶
func (r *ProjectsLocationsAppConnectorsService) ReportStatus(appConnector string, googlecloudbeyondcorpappconnectorsv1alphareportstatusrequest *GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest) *ProjectsLocationsAppConnectorsReportStatusCall

ReportStatus: Report status for a given connector.

appConnector: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`.
func (*ProjectsLocationsAppConnectorsService) ResolveInstanceConfig ¶
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
type ProjectsLocationsAppGatewaysCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysCreateCall) AppGatewayId ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) AppGatewayId(appGatewayId string) *ProjectsLocationsAppGatewaysCreateCall

AppGatewayId sets the optional parameter "appGatewayId": User-settable AppGateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppGatewaysCreateCall) Context ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysCreateCall) Do ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appGateways.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysCreateCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysCreateCall) Header ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysCreateCall) RequestId ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppGatewaysCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsAppGatewaysCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppGatewaysDeleteCall ¶
type ProjectsLocationsAppGatewaysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysDeleteCall) Context ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysDeleteCall) Do ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appGateways.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysDeleteCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysDeleteCall) Header ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysDeleteCall) RequestId ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppGatewaysDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsAppGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppGatewaysGetCall ¶
type ProjectsLocationsAppGatewaysGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysGetCall) Context ¶
func (c *ProjectsLocationsAppGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysGetCall) Do ¶
func (c *ProjectsLocationsAppGatewaysGetCall) Do(opts ...googleapi.CallOption) (*AppGateway, error)

Do executes the "beyondcorp.projects.locations.appGateways.get" call. Any non-2xx status code is an error. Response headers are in either *AppGateway.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysGetCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysGetCall) Header ¶
func (c *ProjectsLocationsAppGatewaysGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysGetCall) IfNoneMatch ¶
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
type ProjectsLocationsAppGatewaysListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysListCall) Context ¶
func (c *ProjectsLocationsAppGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysListCall) Do ¶
func (c *ProjectsLocationsAppGatewaysListCall) Do(opts ...googleapi.CallOption) (*ListAppGatewaysResponse, error)

Do executes the "beyondcorp.projects.locations.appGateways.list" call. Any non-2xx status code is an error. Response headers are in either *ListAppGatewaysResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysListCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysListCall) Filter ¶
func (c *ProjectsLocationsAppGatewaysListCall) Filter(filter string) *ProjectsLocationsAppGatewaysListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppGatewaysListCall) Header ¶
func (c *ProjectsLocationsAppGatewaysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysListCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppGatewaysListCall) OrderBy ¶
func (c *ProjectsLocationsAppGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsAppGatewaysListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppGatewaysListCall) PageSize ¶
func (c *ProjectsLocationsAppGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsAppGatewaysListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppGatewaysListCall) PageToken ¶
func (c *ProjectsLocationsAppGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsAppGatewaysListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppGatewaysRequest, if any.

func (*ProjectsLocationsAppGatewaysListCall) Pages ¶
func (c *ProjectsLocationsAppGatewaysListCall) Pages(ctx context.Context, f func(*ListAppGatewaysResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppGatewaysService ¶
type ProjectsLocationsAppGatewaysService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppGatewaysService ¶
func NewProjectsLocationsAppGatewaysService(s *Service) *ProjectsLocationsAppGatewaysService
func (*ProjectsLocationsAppGatewaysService) Create ¶
func (r *ProjectsLocationsAppGatewaysService) Create(parent string, appgateway *AppGateway) *ProjectsLocationsAppGatewaysCreateCall

Create: Creates a new AppGateway in a given project and location.

parent: The resource project name of the AppGateway location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppGatewaysService) Delete ¶
func (r *ProjectsLocationsAppGatewaysService) Delete(name string) *ProjectsLocationsAppGatewaysDeleteCall

Delete: Deletes a single AppGateway.

name: BeyondCorp AppGateway name using the form: `projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id} `.
func (*ProjectsLocationsAppGatewaysService) Get ¶
func (r *ProjectsLocationsAppGatewaysService) Get(name string) *ProjectsLocationsAppGatewaysGetCall

Get: Gets details of a single AppGateway.

name: BeyondCorp AppGateway name using the form: `projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id} `.
func (*ProjectsLocationsAppGatewaysService) GetIamPolicy ¶
func (r *ProjectsLocationsAppGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsAppGatewaysGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppGatewaysService) List ¶
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

type ProjectsLocationsApplicationDomainsGetIamPolicyCall ¶
added in v0.140.0
type ProjectsLocationsApplicationDomainsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) Context ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) Do ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.applicationDomains.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) Fields ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) Header ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) IfNoneMatch ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationDomainsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationDomainsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationDomainsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApplicationDomainsService ¶
added in v0.140.0
type ProjectsLocationsApplicationDomainsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationDomainsService ¶
added in v0.140.0
func NewProjectsLocationsApplicationDomainsService(s *Service) *ProjectsLocationsApplicationDomainsService
func (*ProjectsLocationsApplicationDomainsService) GetIamPolicy ¶
added in v0.140.0
func (r *ProjectsLocationsApplicationDomainsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationDomainsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationDomainsService) SetIamPolicy ¶
added in v0.140.0
func (r *ProjectsLocationsApplicationDomainsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsApplicationDomainsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationDomainsService) TestIamPermissions ¶
added in v0.140.0
func (r *ProjectsLocationsApplicationDomainsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApplicationDomainsSetIamPolicyCall ¶
added in v0.140.0
type ProjectsLocationsApplicationDomainsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationDomainsSetIamPolicyCall) Context ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationDomainsSetIamPolicyCall) Do ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.applicationDomains.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationDomainsSetIamPolicyCall) Fields ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationDomainsSetIamPolicyCall) Header ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationDomainsTestIamPermissionsCall ¶
added in v0.140.0
type ProjectsLocationsApplicationDomainsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Context ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Do ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.applicationDomains.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Fields ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationDomainsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Header ¶
added in v0.140.0
func (c *ProjectsLocationsApplicationDomainsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsGetIamPolicyCall ¶
added in v0.86.0
type ProjectsLocationsApplicationsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsGetIamPolicyCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.applications.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApplicationsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsApplicationsService ¶
added in v0.86.0
type ProjectsLocationsApplicationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApplicationsService ¶
added in v0.86.0
func NewProjectsLocationsApplicationsService(s *Service) *ProjectsLocationsApplicationsService
func (*ProjectsLocationsApplicationsService) GetIamPolicy ¶
added in v0.86.0
func (r *ProjectsLocationsApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsApplicationsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationsService) SetIamPolicy ¶
added in v0.86.0
func (r *ProjectsLocationsApplicationsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsApplicationsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsApplicationsService) TestIamPermissions ¶
added in v0.86.0
func (r *ProjectsLocationsApplicationsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsApplicationsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsApplicationsSetIamPolicyCall ¶
added in v0.86.0
type ProjectsLocationsApplicationsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsSetIamPolicyCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApplicationsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.applications.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsSetIamPolicyCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsTestIamPermissionsCall ¶
added in v0.86.0
type ProjectsLocationsApplicationsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Context ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApplicationsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Do ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.applications.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Fields ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApplicationsTestIamPermissionsCall) Header ¶
added in v0.86.0
func (c *ProjectsLocationsApplicationsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsConnectionsCreateCall ¶
type ProjectsLocationsConnectionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsCreateCall) ConnectionId ¶
func (c *ProjectsLocationsConnectionsCreateCall) ConnectionId(connectionId string) *ProjectsLocationsConnectionsCreateCall

ConnectionId sets the optional parameter "connectionId": User-settable connection resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsConnectionsCreateCall) Context ¶
func (c *ProjectsLocationsConnectionsCreateCall) Context(ctx context.Context) *ProjectsLocationsConnectionsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsCreateCall) Do ¶
func (c *ProjectsLocationsConnectionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connections.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsCreateCall) Fields ¶
func (c *ProjectsLocationsConnectionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsCreateCall) Header ¶
func (c *ProjectsLocationsConnectionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsCreateCall) RequestId ¶
func (c *ProjectsLocationsConnectionsCreateCall) RequestId(requestId string) *ProjectsLocationsConnectionsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectionsCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectionsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectionsDeleteCall ¶
type ProjectsLocationsConnectionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsDeleteCall) Context ¶
func (c *ProjectsLocationsConnectionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsConnectionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsDeleteCall) Do ¶
func (c *ProjectsLocationsConnectionsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connections.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsDeleteCall) Fields ¶
func (c *ProjectsLocationsConnectionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsDeleteCall) Header ¶
func (c *ProjectsLocationsConnectionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsDeleteCall) RequestId ¶
func (c *ProjectsLocationsConnectionsDeleteCall) RequestId(requestId string) *ProjectsLocationsConnectionsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectionsDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectionsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectionsGetCall ¶
type ProjectsLocationsConnectionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsGetCall) Context ¶
func (c *ProjectsLocationsConnectionsGetCall) Context(ctx context.Context) *ProjectsLocationsConnectionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsGetCall) Do ¶
func (c *ProjectsLocationsConnectionsGetCall) Do(opts ...googleapi.CallOption) (*Connection, error)

Do executes the "beyondcorp.projects.locations.connections.get" call. Any non-2xx status code is an error. Response headers are in either *Connection.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsGetCall) Fields ¶
func (c *ProjectsLocationsConnectionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsGetCall) Header ¶
func (c *ProjectsLocationsConnectionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsConnectionsGetIamPolicyCall ¶
type ProjectsLocationsConnectionsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectionsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.connections.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsConnectionsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsConnectionsListCall ¶
type ProjectsLocationsConnectionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsListCall) Context ¶
func (c *ProjectsLocationsConnectionsListCall) Context(ctx context.Context) *ProjectsLocationsConnectionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsListCall) Do ¶
func (c *ProjectsLocationsConnectionsListCall) Do(opts ...googleapi.CallOption) (*ListConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.connections.list" call. Any non-2xx status code is an error. Response headers are in either *ListConnectionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsListCall) Fields ¶
func (c *ProjectsLocationsConnectionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsListCall) Filter ¶
func (c *ProjectsLocationsConnectionsListCall) Filter(filter string) *ProjectsLocationsConnectionsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsConnectionsListCall) Header ¶
func (c *ProjectsLocationsConnectionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsConnectionsListCall) OrderBy ¶
func (c *ProjectsLocationsConnectionsListCall) OrderBy(orderBy string) *ProjectsLocationsConnectionsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsConnectionsListCall) PageSize ¶
func (c *ProjectsLocationsConnectionsListCall) PageSize(pageSize int64) *ProjectsLocationsConnectionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsConnectionsListCall) PageToken ¶
func (c *ProjectsLocationsConnectionsListCall) PageToken(pageToken string) *ProjectsLocationsConnectionsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListConnectionsRequest, if any.

func (*ProjectsLocationsConnectionsListCall) Pages ¶
func (c *ProjectsLocationsConnectionsListCall) Pages(ctx context.Context, f func(*ListConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsConnectionsPatchCall ¶
type ProjectsLocationsConnectionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsConnectionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsConnectionsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set as true, will create the resource if it is not found.

func (*ProjectsLocationsConnectionsPatchCall) Context ¶
func (c *ProjectsLocationsConnectionsPatchCall) Context(ctx context.Context) *ProjectsLocationsConnectionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsPatchCall) Do ¶
func (c *ProjectsLocationsConnectionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connections.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsPatchCall) Fields ¶
func (c *ProjectsLocationsConnectionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsPatchCall) Header ¶
func (c *ProjectsLocationsConnectionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsPatchCall) RequestId ¶
func (c *ProjectsLocationsConnectionsPatchCall) RequestId(requestId string) *ProjectsLocationsConnectionsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectionsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsConnectionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsConnectionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.Connection]: * `labels` * `display_name` * `application_endpoint` * `connectors`

func (*ProjectsLocationsConnectionsPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectionsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectionsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectionsResolveCall ¶
type ProjectsLocationsConnectionsResolveCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsResolveCall) ConnectorId ¶
func (c *ProjectsLocationsConnectionsResolveCall) ConnectorId(connectorId string) *ProjectsLocationsConnectionsResolveCall

ConnectorId sets the optional parameter "connectorId": Required. BeyondCorp Connector name of the connector associated with those connections using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector_id}`

func (*ProjectsLocationsConnectionsResolveCall) Context ¶
func (c *ProjectsLocationsConnectionsResolveCall) Context(ctx context.Context) *ProjectsLocationsConnectionsResolveCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsResolveCall) Do ¶
func (c *ProjectsLocationsConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*ResolveConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.connections.resolve" call. Any non-2xx status code is an error. Response headers are in either *ResolveConnectionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsResolveCall) Fields ¶
func (c *ProjectsLocationsConnectionsResolveCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsResolveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsResolveCall) Header ¶
func (c *ProjectsLocationsConnectionsResolveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectionsResolveCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectionsResolveCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectionsResolveCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsConnectionsResolveCall) PageSize ¶
func (c *ProjectsLocationsConnectionsResolveCall) PageSize(pageSize int64) *ProjectsLocationsConnectionsResolveCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsConnectionsResolveCall) PageToken ¶
func (c *ProjectsLocationsConnectionsResolveCall) PageToken(pageToken string) *ProjectsLocationsConnectionsResolveCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ResolveConnectionsResponse, if any.

func (*ProjectsLocationsConnectionsResolveCall) Pages ¶
func (c *ProjectsLocationsConnectionsResolveCall) Pages(ctx context.Context, f func(*ResolveConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsConnectionsService ¶
type ProjectsLocationsConnectionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsConnectionsService ¶
func NewProjectsLocationsConnectionsService(s *Service) *ProjectsLocationsConnectionsService
func (*ProjectsLocationsConnectionsService) Create ¶
func (r *ProjectsLocationsConnectionsService) Create(parent string, connection *Connection) *ProjectsLocationsConnectionsCreateCall

Create: Creates a new Connection in a given project and location.

parent: The resource project name of the connection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsConnectionsService) Delete ¶
func (r *ProjectsLocationsConnectionsService) Delete(name string) *ProjectsLocationsConnectionsDeleteCall

Delete: Deletes a single Connection.

name: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`.
func (*ProjectsLocationsConnectionsService) Get ¶
func (r *ProjectsLocationsConnectionsService) Get(name string) *ProjectsLocationsConnectionsGetCall

Get: Gets details of a single Connection.

name: BeyondCorp Connection name using the form: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`.
func (*ProjectsLocationsConnectionsService) GetIamPolicy ¶
func (r *ProjectsLocationsConnectionsService) GetIamPolicy(resource string) *ProjectsLocationsConnectionsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsConnectionsService) List ¶
func (r *ProjectsLocationsConnectionsService) List(parent string) *ProjectsLocationsConnectionsListCall

List: Lists Connections in a given project and location.

parent: The resource name of the connection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsConnectionsService) Patch ¶
func (r *ProjectsLocationsConnectionsService) Patch(name string, connection *Connection) *ProjectsLocationsConnectionsPatchCall

Patch: Updates the parameters of a single Connection.

name: Unique resource name of the connection. The name is ignored when creating a connection.
func (*ProjectsLocationsConnectionsService) Resolve ¶
func (r *ProjectsLocationsConnectionsService) Resolve(parent string) *ProjectsLocationsConnectionsResolveCall

Resolve: Resolves connections details for a given connector. An internal method called by a connector to find connections to connect to.

parent: The resource name of the connection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsConnectionsService) SetIamPolicy ¶
func (r *ProjectsLocationsConnectionsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsConnectionsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsConnectionsSetIamPolicyCall ¶
type ProjectsLocationsConnectionsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectionsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectionsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectionsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.connections.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectionsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectionsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectionsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsConnectionsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsConnectorsCreateCall ¶
type ProjectsLocationsConnectorsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsCreateCall) ConnectorId ¶
func (c *ProjectsLocationsConnectorsCreateCall) ConnectorId(connectorId string) *ProjectsLocationsConnectorsCreateCall

ConnectorId sets the optional parameter "connectorId": User-settable connector resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsConnectorsCreateCall) Context ¶
func (c *ProjectsLocationsConnectorsCreateCall) Context(ctx context.Context) *ProjectsLocationsConnectorsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsCreateCall) Do ¶
func (c *ProjectsLocationsConnectorsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connectors.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsCreateCall) Fields ¶
func (c *ProjectsLocationsConnectorsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsCreateCall) Header ¶
func (c *ProjectsLocationsConnectorsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsCreateCall) RequestId ¶
func (c *ProjectsLocationsConnectorsCreateCall) RequestId(requestId string) *ProjectsLocationsConnectorsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectorsCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectorsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectorsDeleteCall ¶
type ProjectsLocationsConnectorsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsDeleteCall) Context ¶
func (c *ProjectsLocationsConnectorsDeleteCall) Context(ctx context.Context) *ProjectsLocationsConnectorsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsDeleteCall) Do ¶
func (c *ProjectsLocationsConnectorsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connectors.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsDeleteCall) Fields ¶
func (c *ProjectsLocationsConnectorsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsDeleteCall) Header ¶
func (c *ProjectsLocationsConnectorsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsDeleteCall) RequestId ¶
func (c *ProjectsLocationsConnectorsDeleteCall) RequestId(requestId string) *ProjectsLocationsConnectorsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectorsDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectorsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectorsGetCall ¶
type ProjectsLocationsConnectorsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsGetCall) Context ¶
func (c *ProjectsLocationsConnectorsGetCall) Context(ctx context.Context) *ProjectsLocationsConnectorsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsGetCall) Do ¶
func (c *ProjectsLocationsConnectorsGetCall) Do(opts ...googleapi.CallOption) (*Connector, error)

Do executes the "beyondcorp.projects.locations.connectors.get" call. Any non-2xx status code is an error. Response headers are in either *Connector.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsGetCall) Fields ¶
func (c *ProjectsLocationsConnectorsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsGetCall) Header ¶
func (c *ProjectsLocationsConnectorsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectorsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsConnectorsGetIamPolicyCall ¶
type ProjectsLocationsConnectorsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectorsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.connectors.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsConnectorsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsConnectorsListCall ¶
type ProjectsLocationsConnectorsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsListCall) Context ¶
func (c *ProjectsLocationsConnectorsListCall) Context(ctx context.Context) *ProjectsLocationsConnectorsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsListCall) Do ¶
func (c *ProjectsLocationsConnectorsListCall) Do(opts ...googleapi.CallOption) (*ListConnectorsResponse, error)

Do executes the "beyondcorp.projects.locations.connectors.list" call. Any non-2xx status code is an error. Response headers are in either *ListConnectorsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsListCall) Fields ¶
func (c *ProjectsLocationsConnectorsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsListCall) Filter ¶
func (c *ProjectsLocationsConnectorsListCall) Filter(filter string) *ProjectsLocationsConnectorsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsConnectorsListCall) Header ¶
func (c *ProjectsLocationsConnectorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectorsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsConnectorsListCall) OrderBy ¶
func (c *ProjectsLocationsConnectorsListCall) OrderBy(orderBy string) *ProjectsLocationsConnectorsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsConnectorsListCall) PageSize ¶
func (c *ProjectsLocationsConnectorsListCall) PageSize(pageSize int64) *ProjectsLocationsConnectorsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsConnectorsListCall) PageToken ¶
func (c *ProjectsLocationsConnectorsListCall) PageToken(pageToken string) *ProjectsLocationsConnectorsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListConnectorsRequest, if any.

func (*ProjectsLocationsConnectorsListCall) Pages ¶
func (c *ProjectsLocationsConnectorsListCall) Pages(ctx context.Context, f func(*ListConnectorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsConnectorsPatchCall ¶
type ProjectsLocationsConnectorsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsPatchCall) Context ¶
func (c *ProjectsLocationsConnectorsPatchCall) Context(ctx context.Context) *ProjectsLocationsConnectorsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsPatchCall) Do ¶
func (c *ProjectsLocationsConnectorsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connectors.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsPatchCall) Fields ¶
func (c *ProjectsLocationsConnectorsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsPatchCall) Header ¶
func (c *ProjectsLocationsConnectorsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsPatchCall) RequestId ¶
func (c *ProjectsLocationsConnectorsPatchCall) RequestId(requestId string) *ProjectsLocationsConnectorsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsConnectorsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsConnectorsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsConnectorsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.Connector]: * `labels` * `display_name`

func (*ProjectsLocationsConnectorsPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsConnectorsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsConnectorsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsConnectorsReportStatusCall ¶
type ProjectsLocationsConnectorsReportStatusCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsReportStatusCall) Context ¶
func (c *ProjectsLocationsConnectorsReportStatusCall) Context(ctx context.Context) *ProjectsLocationsConnectorsReportStatusCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsReportStatusCall) Do ¶
func (c *ProjectsLocationsConnectorsReportStatusCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.connectors.reportStatus" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsReportStatusCall) Fields ¶
func (c *ProjectsLocationsConnectorsReportStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsReportStatusCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsReportStatusCall) Header ¶
func (c *ProjectsLocationsConnectorsReportStatusCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsConnectorsResolveInstanceConfigCall ¶
type ProjectsLocationsConnectorsResolveInstanceConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsResolveInstanceConfigCall) Context ¶
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Context(ctx context.Context) *ProjectsLocationsConnectorsResolveInstanceConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsResolveInstanceConfigCall) Do ¶
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*ResolveInstanceConfigResponse, error)

Do executes the "beyondcorp.projects.locations.connectors.resolveInstanceConfig" call. Any non-2xx status code is an error. Response headers are in either *ResolveInstanceConfigResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsResolveInstanceConfigCall) Fields ¶
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsResolveInstanceConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsResolveInstanceConfigCall) Header ¶
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsConnectorsResolveInstanceConfigCall) IfNoneMatch ¶
func (c *ProjectsLocationsConnectorsResolveInstanceConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsConnectorsResolveInstanceConfigCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsConnectorsService ¶
type ProjectsLocationsConnectorsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsConnectorsService ¶
func NewProjectsLocationsConnectorsService(s *Service) *ProjectsLocationsConnectorsService
func (*ProjectsLocationsConnectorsService) Create ¶
func (r *ProjectsLocationsConnectorsService) Create(parent string, connector *Connector) *ProjectsLocationsConnectorsCreateCall

Create: Creates a new Connector in a given project and location.

parent: The resource project name of the connector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsConnectorsService) Delete ¶
func (r *ProjectsLocationsConnectorsService) Delete(name string) *ProjectsLocationsConnectorsDeleteCall

Delete: Deletes a single Connector.

name: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector_id}`.
func (*ProjectsLocationsConnectorsService) Get ¶
func (r *ProjectsLocationsConnectorsService) Get(name string) *ProjectsLocationsConnectorsGetCall

Get: Gets details of a single Connector.

name: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector_id}`.
func (*ProjectsLocationsConnectorsService) GetIamPolicy ¶
func (r *ProjectsLocationsConnectorsService) GetIamPolicy(resource string) *ProjectsLocationsConnectorsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsConnectorsService) List ¶
func (r *ProjectsLocationsConnectorsService) List(parent string) *ProjectsLocationsConnectorsListCall

List: Lists Connectors in a given project and location.

parent: The resource name of the connector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsConnectorsService) Patch ¶
func (r *ProjectsLocationsConnectorsService) Patch(name string, connector *Connector) *ProjectsLocationsConnectorsPatchCall

Patch: Updates the parameters of a single Connector.

name: Unique resource name of the connector. The name is ignored when creating a connector.
func (*ProjectsLocationsConnectorsService) ReportStatus ¶
func (r *ProjectsLocationsConnectorsService) ReportStatus(connector string, reportstatusrequest *ReportStatusRequest) *ProjectsLocationsConnectorsReportStatusCall

ReportStatus: Report status for a given connector.

connector: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`.
func (*ProjectsLocationsConnectorsService) ResolveInstanceConfig ¶
func (r *ProjectsLocationsConnectorsService) ResolveInstanceConfig(connector string) *ProjectsLocationsConnectorsResolveInstanceConfigCall

ResolveInstanceConfig: Gets instance configuration for a given connector. An internal method called by a connector to get its container config.

connector: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`.
func (*ProjectsLocationsConnectorsService) SetIamPolicy ¶
func (r *ProjectsLocationsConnectorsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsConnectorsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsConnectorsSetIamPolicyCall ¶
type ProjectsLocationsConnectorsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsConnectorsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsConnectorsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsConnectorsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.connectors.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsConnectorsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsConnectorsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsConnectorsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsConnectorsSetIamPolicyCall) Header() http.Header

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

type ProjectsLocationsInsightsConfiguredInsightCall ¶
added in v0.92.0
type ProjectsLocationsInsightsConfiguredInsightCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInsightsConfiguredInsightCall) Aggregation ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Aggregation(aggregation string) *ProjectsLocationsInsightsConfiguredInsightCall

Aggregation sets the optional parameter "aggregation": Required. Aggregation type. Available aggregation could be fetched by calling insight list and get APIs in `BASIC` view.

Possible values:

"AGGREGATION_UNSPECIFIED" - Unspecified.
"HOURLY" - Insight should be aggregated at hourly level.
"DAILY" - Insight should be aggregated at daily level.
"WEEKLY" - Insight should be aggregated at weekly level.
"MONTHLY" - Insight should be aggregated at monthly level.
"CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date


range passed in as the start and end time in the request.

func (*ProjectsLocationsInsightsConfiguredInsightCall) Context ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Context(ctx context.Context) *ProjectsLocationsInsightsConfiguredInsightCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingFieldFilter(customGroupingFieldFilter string) *ProjectsLocationsInsightsConfiguredInsightCall

CustomGroupingFieldFilter sets the optional parameter "customGrouping.fieldFilter": Filterable parameters to be added to the grouping clause. Available fields could be fetched by calling insight list and get APIs in `BASIC` view. `=` is the only comparison operator supported. `AND` is the only logical operator supported. Usage: field_filter="fieldName1=fieldVal1 AND fieldName2=fieldVal2". NOTE: Only `AND` conditions are allowed. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) CustomGroupingGroupFields(customGroupingGroupFields ...string) *ProjectsLocationsInsightsConfiguredInsightCall

CustomGroupingGroupFields sets the optional parameter "customGrouping.groupFields": Required. Fields to be used for grouping. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for declaring the fields to be grouped-by here.

func (*ProjectsLocationsInsightsConfiguredInsightCall) Do ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse, error)

Do executes the "beyondcorp.projects.locations.insights.configuredInsight" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse.Se rverResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInsightsConfiguredInsightCall) EndTime ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) EndTime(endTime string) *ProjectsLocationsInsightsConfiguredInsightCall

EndTime sets the optional parameter "endTime": Required. Ending time for the duration for which insight is to be pulled.

func (*ProjectsLocationsInsightsConfiguredInsightCall) FieldFilter ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) FieldFilter(fieldFilter string) *ProjectsLocationsInsightsConfiguredInsightCall

FieldFilter sets the optional parameter "fieldFilter": Other filterable/configurable parameters as applicable to the selected insight. Available fields could be fetched by calling insight list and get APIs in `BASIC` view. `=` is the only comparison operator supported. `AND` is the only logical operator supported. Usage: field_filter="fieldName1=fieldVal1 AND fieldName2=fieldVal2". NOTE: Only `AND` conditions are allowed. NOTE: Use the `filter_alias` from `Insight.Metadata.Field` message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*ProjectsLocationsInsightsConfiguredInsightCall) Fields ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsConfiguredInsightCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInsightsConfiguredInsightCall) Group ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Group(group string) *ProjectsLocationsInsightsConfiguredInsightCall

Group sets the optional parameter "group": Group id of the available groupings for the insight. Available groupings could be fetched by calling insight list and get APIs in `BASIC` view.

func (*ProjectsLocationsInsightsConfiguredInsightCall) Header ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInsightsConfiguredInsightCall) IfNoneMatch ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsConfiguredInsightCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsInsightsConfiguredInsightCall) PageSize ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) PageSize(pageSize int64) *ProjectsLocationsInsightsConfiguredInsightCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsInsightsConfiguredInsightCall) PageToken ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) PageToken(pageToken string) *ProjectsLocationsInsightsConfiguredInsightCall

PageToken sets the optional parameter "pageToken": Used to fetch the page represented by the token. Fetches the first page when not set.

func (*ProjectsLocationsInsightsConfiguredInsightCall) Pages ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsInsightsConfiguredInsightCall) StartTime ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsConfiguredInsightCall) StartTime(startTime string) *ProjectsLocationsInsightsConfiguredInsightCall

StartTime sets the optional parameter "startTime": Required. Starting time for the duration for which insight is to be pulled.

type ProjectsLocationsInsightsGetCall ¶
added in v0.92.0
type ProjectsLocationsInsightsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInsightsGetCall) Context ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) Context(ctx context.Context) *ProjectsLocationsInsightsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInsightsGetCall) Do ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight, error)

Do executes the "beyondcorp.projects.locations.insights.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInsightsGetCall) Fields ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInsightsGetCall) Header ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInsightsGetCall) IfNoneMatch ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsInsightsGetCall) View ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsGetCall) View(view string) *ProjectsLocationsInsightsGetCall

View sets the optional parameter "view": Required. Metadata only or full data view.

Possible values:

"INSIGHT_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Include basic metadata about the insight, but not the insight


data. This is the default value (for both ListInsights and GetInsight).

"FULL" - Include everything.

type ProjectsLocationsInsightsListCall ¶
added in v0.92.0
type ProjectsLocationsInsightsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInsightsListCall) Aggregation ¶
added in v0.191.0
func (c *ProjectsLocationsInsightsListCall) Aggregation(aggregation string) *ProjectsLocationsInsightsListCall

Aggregation sets the optional parameter "aggregation": Aggregation type. The default is 'DAILY'.

Possible values:

"AGGREGATION_UNSPECIFIED" - Unspecified.
"HOURLY" - Insight should be aggregated at hourly level.
"DAILY" - Insight should be aggregated at daily level.
"WEEKLY" - Insight should be aggregated at weekly level.
"MONTHLY" - Insight should be aggregated at monthly level.
"CUSTOM_DATE_RANGE" - Insight should be aggregated at the custom date


range passed in as the start and end time in the request.

func (*ProjectsLocationsInsightsListCall) Context ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Context(ctx context.Context) *ProjectsLocationsInsightsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInsightsListCall) Do ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse, error)

Do executes the "beyondcorp.projects.locations.insights.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse.ServerR esponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInsightsListCall) EndTime ¶
added in v0.191.0
func (c *ProjectsLocationsInsightsListCall) EndTime(endTime string) *ProjectsLocationsInsightsListCall

EndTime sets the optional parameter "endTime": Ending time for the duration for which insights are to be pulled. The default is the current time.

func (*ProjectsLocationsInsightsListCall) Fields ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsInsightsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInsightsListCall) Filter ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Filter(filter string) *ProjectsLocationsInsightsListCall

Filter sets the optional parameter "filter": Filter expression to restrict the insights returned. Supported filter fields: * `type` * `category` * `subCategory` Examples: * "category = application AND type = count" * "category = application AND subCategory = iap" * "type = status" Allowed values: * type: [count, latency, status, list] * category: [application, device, request, security] * subCategory: [iap, caa, webprotect] NOTE: Only equality based comparison is allowed. Only `AND` conjunction is allowed. NOTE: The 'AND' in the filter field needs to be in capital letters only. NOTE: Just filtering on `subCategory` is not allowed. It should be passed in with the parent `category` too. (These expressions are based on the filter language described at https://google.aip.dev/160).

func (*ProjectsLocationsInsightsListCall) Header ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInsightsListCall) IfNoneMatch ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsInsightsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsInsightsListCall) OrderBy ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) OrderBy(orderBy string) *ProjectsLocationsInsightsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results. This is currently ignored.

func (*ProjectsLocationsInsightsListCall) PageSize ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) PageSize(pageSize int64) *ProjectsLocationsInsightsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. NOTE: Default page size is 50.

func (*ProjectsLocationsInsightsListCall) PageToken ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) PageToken(pageToken string) *ProjectsLocationsInsightsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsInsightsListCall) Pages ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsInsightsListCall) StartTime ¶
added in v0.191.0
func (c *ProjectsLocationsInsightsListCall) StartTime(startTime string) *ProjectsLocationsInsightsListCall

StartTime sets the optional parameter "startTime": Starting time for the duration for which insights are to be pulled. The default is 7 days before the current time.

func (*ProjectsLocationsInsightsListCall) View ¶
added in v0.92.0
func (c *ProjectsLocationsInsightsListCall) View(view string) *ProjectsLocationsInsightsListCall

View sets the optional parameter "view": Required. List only metadata or full data.

Possible values:

"INSIGHT_VIEW_UNSPECIFIED" - The default / unset value. The API will


default to the BASIC view.

"BASIC" - Include basic metadata about the insight, but not the insight


data. This is the default value (for both ListInsights and GetInsight).

"FULL" - Include everything.

type ProjectsLocationsInsightsService ¶
added in v0.92.0
type ProjectsLocationsInsightsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsInsightsService ¶
added in v0.92.0
func NewProjectsLocationsInsightsService(s *Service) *ProjectsLocationsInsightsService
func (*ProjectsLocationsInsightsService) ConfiguredInsight ¶
added in v0.92.0
func (r *ProjectsLocationsInsightsService) ConfiguredInsight(insight string) *ProjectsLocationsInsightsConfiguredInsightCall

ConfiguredInsight: Gets the value for a selected particular insight based on the provided filters. Use the organization level path for fetching at org level and project level path for fetching the insight value specific to a particular project.

insight: The resource name of the insight using the form: `organizations/{organization_id}/locations/{location_id}/insights/{insight_ id}` `projects/{project_id}/locations/{location_id}/insights/{insight_id}`.
func (*ProjectsLocationsInsightsService) Get ¶
added in v0.92.0
func (r *ProjectsLocationsInsightsService) Get(name string) *ProjectsLocationsInsightsGetCall

Get: Gets the value for a selected particular insight with default configuration. The default aggregation level is 'DAILY' and no grouping will be applied or default grouping if applicable. The data will be returned for recent 7 days starting the day before. The insight data size will be limited to 50 rows. Use the organization level path for fetching at org level and project level path for fetching the insight value specific to a particular project. Setting the `view` to `BASIC` will only return the metadata for the insight.

name: The resource name of the insight using the form: `organizations/{organization_id}/locations/{location_id}/insights/{insight_ id}` `projects/{project_id}/locations/{location_id}/insights/{insight_id}`.
func (*ProjectsLocationsInsightsService) List ¶
added in v0.92.0
func (r *ProjectsLocationsInsightsService) List(parent string) *ProjectsLocationsInsightsListCall

List: Lists for all the available insights that could be fetched from the system. Allows to filter using category. Setting the `view` to `BASIC` will let you iterate over the list of insight metadatas.

parent: The resource name of InsightMetadata using the form: `organizations/{organization_id}/locations/{location}` `projects/{project_id}/locations/{location_id}`.
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
added in v0.193.0
type ProjectsLocationsSecurityGatewaysApplicationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Context ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Do ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Fields ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Header ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) RequestId ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) ValidateOnly ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsSecurityGatewaysApplicationsGetCall ¶
added in v0.193.0
type ProjectsLocationsSecurityGatewaysApplicationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Context ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Fields ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Header ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) IfNoneMatch ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall ¶
added in v0.198.0
type ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Context ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Do ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Fields ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Header ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) IfNoneMatch ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsSecurityGatewaysApplicationsListCall ¶
added in v0.193.0
type ProjectsLocationsSecurityGatewaysApplicationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Context ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Do ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse.ServerR esponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Fields ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Filter ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation. All fields in the Application message are supported. For example, the following query will return the Application with displayName "test-application" For more information, please refer to https://google.aip.dev/160.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Header ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) IfNoneMatch ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) OrderBy ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) PageSize ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysApplicationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) PageToken ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListApplicationsRequest, if any.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Pages ¶
added in v0.193.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse) error) error

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
added in v0.193.0
type ProjectsLocationsSecurityGatewaysApplicationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsSecurityGatewaysApplicationsService ¶
added in v0.193.0
func NewProjectsLocationsSecurityGatewaysApplicationsService(s *Service) *ProjectsLocationsSecurityGatewaysApplicationsService
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Create ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Create(parent string, googlecloudbeyondcorpsecuritygatewaysv1alphaapplication *GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

Create: Creates a new Application in a given project and location.

parent: The resource name of the parent SecurityGateway using the form: `projects/{project_id}/locations/global/securityGateways/{security_gateway_ id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Delete ¶
added in v0.193.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Delete(name string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Delete: Deletes a single application.

- name: Name of the resource.

func (*ProjectsLocationsSecurityGatewaysApplicationsService) Get ¶
added in v0.193.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Get(name string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Get: Gets details of a single Application.

name: The resource name of the Application using the form: `projects/{project_id}/locations/global/securityGateway/{security_gateway_i d}/applications/{application_id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) GetIamPolicy ¶
added in v0.198.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) List ¶
added in v0.193.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) List(parent string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

List: Lists Applications in a given project and location.

parent: The parent location to which the resources belong. `projects/{project_id}/locations/global/securityGateways/{security_gateway_ id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Patch ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Patch(name string, googlecloudbeyondcorpsecuritygatewaysv1alphaapplication *GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

Patch: Updates the parameters of a single Application.

- name: Identifier. Name of the resource.

func (*ProjectsLocationsSecurityGatewaysApplicationsService) SetIamPolicy ¶
added in v0.198.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) TestIamPermissions ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall ¶
added in v0.198.0
type ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Context ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Do ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Fields ¶
added in v0.198.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Header ¶
added in v0.198.0
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
added in v0.173.0
type ProjectsLocationsSecurityGatewaysCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysCreateCall) Context ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Do ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Fields ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Header ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysCreateCall) RequestId ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

func (*ProjectsLocationsSecurityGatewaysCreateCall) SecurityGatewayId ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) SecurityGatewayId(securityGatewayId string) *ProjectsLocationsSecurityGatewaysCreateCall

SecurityGatewayId sets the optional parameter "securityGatewayId": User-settable SecurityGateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or letter.

type ProjectsLocationsSecurityGatewaysDeleteCall ¶
added in v0.173.0
type ProjectsLocationsSecurityGatewaysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysDeleteCall) Context ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Do ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Fields ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Header ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) RequestId ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysDeleteCall) ValidateOnly ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsSecurityGatewaysGetCall ¶
added in v0.173.0
type ProjectsLocationsSecurityGatewaysGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysGetCall) Context ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysGetCall) Do ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway, error)

Do executes the "beyondcorp.projects.locations.securityGateways.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysGetCall) Fields ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysGetCall) Header ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysGetCall) IfNoneMatch ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsSecurityGatewaysGetIamPolicyCall ¶
added in v0.182.0
type ProjectsLocationsSecurityGatewaysGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Context ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Do ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Fields ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Header ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) IfNoneMatch ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsSecurityGatewaysListCall ¶
added in v0.173.0
type ProjectsLocationsSecurityGatewaysListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysListCall) Context ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysListCall) Do ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse.Ser verResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysListCall) Fields ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysListCall) Filter ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation. All fields in the SecurityGateway message are supported. For example, the following query will return the SecurityGateway with displayName "test-security-gateway" For more information, please refer to https://google.aip.dev/160.

func (*ProjectsLocationsSecurityGatewaysListCall) Header ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysListCall) IfNoneMatch ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysListCall) OrderBy ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsSecurityGatewaysListCall) PageSize ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsSecurityGatewaysListCall) PageToken ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListSecurityGatewayRequest, if any.

func (*ProjectsLocationsSecurityGatewaysListCall) Pages ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsSecurityGatewaysPatchCall ¶
added in v0.173.0
type ProjectsLocationsSecurityGatewaysPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysPatchCall) Context ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Do ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Fields ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Header ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysPatchCall) RequestId ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysPatchCall) UpdateMask ¶
added in v0.173.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) UpdateMask(updateMask string) *ProjectsLocationsSecurityGatewaysPatchCall

UpdateMask sets the optional parameter "updateMask": Mutable fields include: display_name, hubs.

type ProjectsLocationsSecurityGatewaysService ¶
added in v0.173.0
type ProjectsLocationsSecurityGatewaysService struct {
	Applications *ProjectsLocationsSecurityGatewaysApplicationsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsSecurityGatewaysService ¶
added in v0.173.0
func NewProjectsLocationsSecurityGatewaysService(s *Service) *ProjectsLocationsSecurityGatewaysService
func (*ProjectsLocationsSecurityGatewaysService) Create ¶
added in v0.173.0
func (r *ProjectsLocationsSecurityGatewaysService) Create(parent string, googlecloudbeyondcorpsecuritygatewaysv1alphasecuritygateway *GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway) *ProjectsLocationsSecurityGatewaysCreateCall

Create: Creates a new Security Gateway in a given project and location.

parent: The resource project name of the SecurityGateway location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsSecurityGatewaysService) Delete ¶
added in v0.173.0
func (r *ProjectsLocationsSecurityGatewaysService) Delete(name string) *ProjectsLocationsSecurityGatewaysDeleteCall

Delete: Deletes a single SecurityGateway.

name: BeyondCorp SecurityGateway name using the form: `projects/{project_id}/locations/{location_id}/securityGateways/{security_g ateway_id}`.
func (*ProjectsLocationsSecurityGatewaysService) Get ¶
added in v0.173.0
func (r *ProjectsLocationsSecurityGatewaysService) Get(name string) *ProjectsLocationsSecurityGatewaysGetCall

Get: Gets details of a single SecurityGateway.

name: The resource name of the PartnerTenant using the form: `projects/{project_id}/locations/{location_id}/securityGateway/{security_ga teway_id}`.
func (*ProjectsLocationsSecurityGatewaysService) GetIamPolicy ¶
added in v0.182.0
func (r *ProjectsLocationsSecurityGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysService) List ¶
added in v0.173.0
func (r *ProjectsLocationsSecurityGatewaysService) List(parent string) *ProjectsLocationsSecurityGatewaysListCall

List: Lists SecurityGateways in a given project and location.

parent: The parent location to which the resources belong. `projects/{project_id}/locations/{location_id}/`.
func (*ProjectsLocationsSecurityGatewaysService) Patch ¶
added in v0.173.0
func (r *ProjectsLocationsSecurityGatewaysService) Patch(name string, googlecloudbeyondcorpsecuritygatewaysv1alphasecuritygateway *GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway) *ProjectsLocationsSecurityGatewaysPatchCall

Patch: Updates the parameters of a single SecurityGateway.

- name: Identifier. Name of the resource.

func (*ProjectsLocationsSecurityGatewaysService) SetIamPolicy ¶
added in v0.182.0
func (r *ProjectsLocationsSecurityGatewaysService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysService) TestIamPermissions ¶
added in v0.182.0
func (r *ProjectsLocationsSecurityGatewaysService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsSecurityGatewaysSetIamPolicyCall ¶
added in v0.182.0
type ProjectsLocationsSecurityGatewaysSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Context ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Do ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Fields ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Header ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsSecurityGatewaysTestIamPermissionsCall ¶
added in v0.182.0
type ProjectsLocationsSecurityGatewaysTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Context ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Do ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Fields ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Header ¶
added in v0.182.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	AppConnections *ProjectsLocationsAppConnectionsService

	AppConnectors *ProjectsLocationsAppConnectorsService

	AppGateways *ProjectsLocationsAppGatewaysService

	ApplicationDomains *ProjectsLocationsApplicationDomainsService

	Applications *ProjectsLocationsApplicationsService

	Connections *ProjectsLocationsConnectionsService

	Connectors *ProjectsLocationsConnectorsService

	Insights *ProjectsLocationsInsightsService

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
type RemoteAgentDetails ¶
type RemoteAgentDetails struct {
}

RemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type ReportStatusRequest ¶
type ReportStatusRequest struct {
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
	ResourceInfo *ResourceInfo `json:"resourceInfo,omitempty"`
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

ReportStatusRequest: Request report the connector status.

func (ReportStatusRequest) MarshalJSON ¶
func (s ReportStatusRequest) MarshalJSON() ([]byte, error)
type ResolveConnectionsResponse ¶
type ResolveConnectionsResponse struct {
	// ConnectionDetails: A list of BeyondCorp Connections with details in the
	// project.
	ConnectionDetails []*ConnectionDetails `json:"connectionDetails,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ConnectionDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConnectionDetails") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ResolveConnectionsResponse: Response message for BeyondCorp.ResolveConnections.

func (ResolveConnectionsResponse) MarshalJSON ¶
func (s ResolveConnectionsResponse) MarshalJSON() ([]byte, error)
type ResolveInstanceConfigResponse ¶
type ResolveInstanceConfigResponse struct {
	// InstanceConfig: ConnectorInstanceConfig.
	InstanceConfig *ConnectorInstanceConfig `json:"instanceConfig,omitempty"`

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

ResolveInstanceConfigResponse: Response message for BeyondCorp.ResolveInstanceConfig.

func (ResolveInstanceConfigResponse) MarshalJSON ¶
func (s ResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type ResourceInfo ¶
type ResourceInfo struct {
	// Id: Required. Unique Id for the resource.
	Id string `json:"id,omitempty"`
	// Resource: Specific details for the resource.
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
	Sub []*ResourceInfo `json:"sub,omitempty"`
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

ResourceInfo: ResourceInfo represents the information/status of the associated resource.

func (ResourceInfo) MarshalJSON ¶
func (s ResourceInfo) MarshalJSON() ([]byte, error)
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

type ServiceAccount ¶
type ServiceAccount struct {
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

ServiceAccount: ServiceAccount represents a GCP service account.

func (ServiceAccount) MarshalJSON ¶
func (s ServiceAccount) MarshalJSON() ([]byte, error)
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
