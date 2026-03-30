# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apihub/v1

Title: apihub package - google.golang.org/api/apihub/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apihub/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
apihub
 
v1
apihub
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

Package apihub provides access to the API hub API.

For product documentation, see: https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/apihub/v1"
...
ctx := context.Background()
apihubService, err := apihub.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

apihubService, err := apihub.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apihubService, err := apihub.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Empty
type GoogleCloudApihubV1APIMetadata
func (s GoogleCloudApihubV1APIMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ActionExecutionDetail
func (s GoogleCloudApihubV1ActionExecutionDetail) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AdditionalSpecContent
func (s GoogleCloudApihubV1AdditionalSpecContent) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Addon
func (s GoogleCloudApihubV1Addon) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AddonConfig
func (s GoogleCloudApihubV1AddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AllDataAddonConfig
func (s GoogleCloudApihubV1AllDataAddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AllowedValue
func (s GoogleCloudApihubV1AllowedValue) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Api
func (s GoogleCloudApihubV1Api) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiData
func (s GoogleCloudApihubV1ApiData) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiHubInstance
func (s GoogleCloudApihubV1ApiHubInstance) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiHubResource
func (s GoogleCloudApihubV1ApiHubResource) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiKeyConfig
func (s GoogleCloudApihubV1ApiKeyConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiMetadataList
func (s GoogleCloudApihubV1ApiMetadataList) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiOperation
func (s GoogleCloudApihubV1ApiOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiView
func (s GoogleCloudApihubV1ApiView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeEdgeConfig
func (s GoogleCloudApihubV1ApigeeEdgeConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeOPDKConfig
func (s GoogleCloudApihubV1ApigeeOPDKConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeXHybridConfig
func (s GoogleCloudApihubV1ApigeeXHybridConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApplicationIntegrationEndpointDetails
func (s GoogleCloudApihubV1ApplicationIntegrationEndpointDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Attribute
func (s GoogleCloudApihubV1Attribute) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AttributeValues
func (s GoogleCloudApihubV1AttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AuthConfig
func (s GoogleCloudApihubV1AuthConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AuthConfigTemplate
func (s GoogleCloudApihubV1AuthConfigTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CollectApiDataRequest
func (s GoogleCloudApihubV1CollectApiDataRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Config
func (s GoogleCloudApihubV1Config) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigTemplate
func (s GoogleCloudApihubV1ConfigTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigValueOption
func (s GoogleCloudApihubV1ConfigValueOption) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigVariable
func (s GoogleCloudApihubV1ConfigVariable) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigVariableTemplate
func (s GoogleCloudApihubV1ConfigVariableTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Curation
func (s GoogleCloudApihubV1Curation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CurationConfig
func (s GoogleCloudApihubV1CurationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CustomCuration
func (s GoogleCloudApihubV1CustomCuration) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Definition
func (s GoogleCloudApihubV1Definition) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Dependency
func (s GoogleCloudApihubV1Dependency) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DependencyEntityReference
func (s GoogleCloudApihubV1DependencyEntityReference) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DependencyErrorDetail
func (s GoogleCloudApihubV1DependencyErrorDetail) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Deployment
func (s GoogleCloudApihubV1Deployment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DeploymentMetadata
func (s GoogleCloudApihubV1DeploymentMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DisablePluginInstanceActionRequest
func (s GoogleCloudApihubV1DisablePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DisablePluginRequest
type GoogleCloudApihubV1DiscoveredApiObservation
func (s GoogleCloudApihubV1DiscoveredApiObservation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DiscoveredApiOperation
func (s GoogleCloudApihubV1DiscoveredApiOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Documentation
func (s GoogleCloudApihubV1Documentation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnablePluginInstanceActionRequest
func (s GoogleCloudApihubV1EnablePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnablePluginRequest
type GoogleCloudApihubV1Endpoint
func (s GoogleCloudApihubV1Endpoint) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnumAttributeValues
func (s GoogleCloudApihubV1EnumAttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnvironmentFilter
func (s GoogleCloudApihubV1EnvironmentFilter) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExecutePluginInstanceActionRequest
func (s GoogleCloudApihubV1ExecutePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExecutionStatus
func (s GoogleCloudApihubV1ExecutionStatus) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExternalApi
func (s GoogleCloudApihubV1ExternalApi) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FetchAdditionalSpecContentResponse
func (s GoogleCloudApihubV1FetchAdditionalSpecContentResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FlattenedApiVersionDeploymentView
func (s GoogleCloudApihubV1FlattenedApiVersionDeploymentView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView
func (s GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GatewayPluginAddonConfig
func (s GoogleCloudApihubV1GatewayPluginAddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GatewayPluginConfig
func (s GoogleCloudApihubV1GatewayPluginConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GoogleServiceAccountConfig
func (s GoogleCloudApihubV1GoogleServiceAccountConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Header
func (s GoogleCloudApihubV1Header) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HostProjectRegistration
func (s GoogleCloudApihubV1HostProjectRegistration) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HostingService
func (s GoogleCloudApihubV1HostingService) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpOperation
func (s GoogleCloudApihubV1HttpOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpOperationDetails
func (s GoogleCloudApihubV1HttpOperationDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpRequest
func (s GoogleCloudApihubV1HttpRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpResponse
func (s GoogleCloudApihubV1HttpResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Issue
func (s GoogleCloudApihubV1Issue) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LastExecution
func (s GoogleCloudApihubV1LastExecution) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LintResponse
func (s GoogleCloudApihubV1LintResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LintSpecRequest
type GoogleCloudApihubV1ListAddonsResponse
func (s GoogleCloudApihubV1ListAddonsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListApiOperationsResponse
func (s GoogleCloudApihubV1ListApiOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListApisResponse
func (s GoogleCloudApihubV1ListApisResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListAttributesResponse
func (s GoogleCloudApihubV1ListAttributesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListCurationsResponse
func (s GoogleCloudApihubV1ListCurationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDependenciesResponse
func (s GoogleCloudApihubV1ListDependenciesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDeploymentsResponse
func (s GoogleCloudApihubV1ListDeploymentsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDiscoveredApiObservationsResponse
func (s GoogleCloudApihubV1ListDiscoveredApiObservationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDiscoveredApiOperationsResponse
func (s GoogleCloudApihubV1ListDiscoveredApiOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListExternalApisResponse
func (s GoogleCloudApihubV1ListExternalApisResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListHostProjectRegistrationsResponse
func (s GoogleCloudApihubV1ListHostProjectRegistrationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListPluginInstancesResponse
func (s GoogleCloudApihubV1ListPluginInstancesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListPluginsResponse
func (s GoogleCloudApihubV1ListPluginsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse
func (s GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListSpecsResponse
func (s GoogleCloudApihubV1ListSpecsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListVersionsResponse
func (s GoogleCloudApihubV1ListVersionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LookupApiHubInstanceResponse
func (s GoogleCloudApihubV1LookupApiHubInstanceResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse
func (s GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManageAddonConfigRequest
func (s GoogleCloudApihubV1ManageAddonConfigRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest
func (s GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse
type GoogleCloudApihubV1MatchResult
func (s GoogleCloudApihubV1MatchResult) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1McpTool
func (s GoogleCloudApihubV1McpTool) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiIntValues
func (s GoogleCloudApihubV1MultiIntValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiSelectValues
func (s GoogleCloudApihubV1MultiSelectValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiStringValues
func (s GoogleCloudApihubV1MultiStringValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Oauth2ClientCredentialsConfig
func (s GoogleCloudApihubV1Oauth2ClientCredentialsConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OpenApiSpecDetails
func (s GoogleCloudApihubV1OpenApiSpecDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationDetails
func (s GoogleCloudApihubV1OperationDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationMetadata
func (s GoogleCloudApihubV1OperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationSchema
func (s GoogleCloudApihubV1OperationSchema) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Owner
func (s GoogleCloudApihubV1Owner) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Path
func (s GoogleCloudApihubV1Path) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PathParam
func (s GoogleCloudApihubV1PathParam) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Plugin
func (s GoogleCloudApihubV1Plugin) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginActionConfig
func (s GoogleCloudApihubV1PluginActionConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstance
func (s GoogleCloudApihubV1PluginInstance) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceAction
func (s GoogleCloudApihubV1PluginInstanceAction) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceActionID
func (s GoogleCloudApihubV1PluginInstanceActionID) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceActionSource
func (s GoogleCloudApihubV1PluginInstanceActionSource) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Point
func (s GoogleCloudApihubV1Point) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1QueryParam
func (s GoogleCloudApihubV1QueryParam) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Range
func (s GoogleCloudApihubV1Range) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ResourceConfig
func (s GoogleCloudApihubV1ResourceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1RetrieveApiViewsResponse
func (s GoogleCloudApihubV1RetrieveApiViewsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1RuntimeProjectAttachment
func (s GoogleCloudApihubV1RuntimeProjectAttachment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Schema
func (s GoogleCloudApihubV1Schema) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResourcesRequest
func (s GoogleCloudApihubV1SearchResourcesRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResourcesResponse
func (s GoogleCloudApihubV1SearchResourcesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResult
func (s GoogleCloudApihubV1SearchResult) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Secret
func (s GoogleCloudApihubV1Secret) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SourceEnvironment
func (s GoogleCloudApihubV1SourceEnvironment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SourceMetadata
func (s GoogleCloudApihubV1SourceMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Spec
func (s GoogleCloudApihubV1Spec) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecContents
func (s GoogleCloudApihubV1SpecContents) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecDetails
func (s GoogleCloudApihubV1SpecDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecMetadata
func (s GoogleCloudApihubV1SpecMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StringAttributeValues
func (s GoogleCloudApihubV1StringAttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StyleGuide
func (s GoogleCloudApihubV1StyleGuide) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StyleGuideContents
func (s GoogleCloudApihubV1StyleGuideContents) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SummaryEntry
func (s GoogleCloudApihubV1SummaryEntry) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ToolAnnotations
func (s GoogleCloudApihubV1ToolAnnotations) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1UserPasswordConfig
func (s GoogleCloudApihubV1UserPasswordConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Version
func (s GoogleCloudApihubV1Version) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1VersionMetadata
func (s GoogleCloudApihubV1VersionMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudCommonOperationMetadata
func (s GoogleCloudCommonOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudLocationListLocationsResponse
func (s GoogleCloudLocationListLocationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudLocationLocation
func (s GoogleCloudLocationLocation) MarshalJSON() ([]byte, error)
type GoogleLongrunningCancelOperationRequest
type GoogleLongrunningListOperationsResponse
func (s GoogleLongrunningListOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleLongrunningOperation
func (s GoogleLongrunningOperation) MarshalJSON() ([]byte, error)
type GoogleRpcStatus
func (s GoogleRpcStatus) MarshalJSON() ([]byte, error)
type ProjectsLocationsAddonsGetCall
func (c *ProjectsLocationsAddonsGetCall) Context(ctx context.Context) *ProjectsLocationsAddonsGetCall
func (c *ProjectsLocationsAddonsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Addon, error)
func (c *ProjectsLocationsAddonsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsGetCall
func (c *ProjectsLocationsAddonsGetCall) Header() http.Header
func (c *ProjectsLocationsAddonsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAddonsGetCall
type ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) Context(ctx context.Context) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListAddonsResponse, error)
func (c *ProjectsLocationsAddonsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) Filter(filter string) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) Header() http.Header
func (c *ProjectsLocationsAddonsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) PageSize(pageSize int64) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) PageToken(pageToken string) *ProjectsLocationsAddonsListCall
func (c *ProjectsLocationsAddonsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListAddonsResponse) error) error
type ProjectsLocationsAddonsManageConfigCall
func (c *ProjectsLocationsAddonsManageConfigCall) Context(ctx context.Context) *ProjectsLocationsAddonsManageConfigCall
func (c *ProjectsLocationsAddonsManageConfigCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAddonsManageConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsManageConfigCall
func (c *ProjectsLocationsAddonsManageConfigCall) Header() http.Header
type ProjectsLocationsAddonsService
func NewProjectsLocationsAddonsService(s *Service) *ProjectsLocationsAddonsService
func (r *ProjectsLocationsAddonsService) Get(name string) *ProjectsLocationsAddonsGetCall
func (r *ProjectsLocationsAddonsService) List(parent string) *ProjectsLocationsAddonsListCall
func (r *ProjectsLocationsAddonsService) ManageConfig(name string, ...) *ProjectsLocationsAddonsManageConfigCall
type ProjectsLocationsApiHubInstancesCreateCall
func (c *ProjectsLocationsApiHubInstancesCreateCall) ApiHubInstanceId(apiHubInstanceId string) *ProjectsLocationsApiHubInstancesCreateCall
func (c *ProjectsLocationsApiHubInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesCreateCall
func (c *ProjectsLocationsApiHubInstancesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsApiHubInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesCreateCall
func (c *ProjectsLocationsApiHubInstancesCreateCall) Header() http.Header
type ProjectsLocationsApiHubInstancesDeleteCall
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesDeleteCall
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesDeleteCall
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Header() http.Header
type ProjectsLocationsApiHubInstancesGetCall
func (c *ProjectsLocationsApiHubInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesGetCall
func (c *ProjectsLocationsApiHubInstancesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiHubInstance, error)
func (c *ProjectsLocationsApiHubInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesGetCall
func (c *ProjectsLocationsApiHubInstancesGetCall) Header() http.Header
func (c *ProjectsLocationsApiHubInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApiHubInstancesGetCall
type ProjectsLocationsApiHubInstancesLookupCall
func (c *ProjectsLocationsApiHubInstancesLookupCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesLookupCall
func (c *ProjectsLocationsApiHubInstancesLookupCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1LookupApiHubInstanceResponse, error)
func (c *ProjectsLocationsApiHubInstancesLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesLookupCall
func (c *ProjectsLocationsApiHubInstancesLookupCall) Header() http.Header
func (c *ProjectsLocationsApiHubInstancesLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsApiHubInstancesLookupCall
type ProjectsLocationsApiHubInstancesService
func NewProjectsLocationsApiHubInstancesService(s *Service) *ProjectsLocationsApiHubInstancesService
func (r *ProjectsLocationsApiHubInstancesService) Create(parent string, ...) *ProjectsLocationsApiHubInstancesCreateCall
func (r *ProjectsLocationsApiHubInstancesService) Delete(name string) *ProjectsLocationsApiHubInstancesDeleteCall
func (r *ProjectsLocationsApiHubInstancesService) Get(name string) *ProjectsLocationsApiHubInstancesGetCall
func (r *ProjectsLocationsApiHubInstancesService) Lookup(parent string) *ProjectsLocationsApiHubInstancesLookupCall
type ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) ApiId(apiId string) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Context(ctx context.Context) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)
func (c *ProjectsLocationsApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisCreateCall
func (c *ProjectsLocationsApisCreateCall) Header() http.Header
type ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Force(force bool) *ProjectsLocationsApisDeleteCall
func (c *ProjectsLocationsApisDeleteCall) Header() http.Header
type ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Context(ctx context.Context) *ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)
func (c *ProjectsLocationsApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetCall
func (c *ProjectsLocationsApisGetCall) Header() http.Header
func (c *ProjectsLocationsApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetCall
type ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Context(ctx context.Context) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListApisResponse, error)
func (c *ProjectsLocationsApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Filter(filter string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Header() http.Header
func (c *ProjectsLocationsApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) PageSize(pageSize int64) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) PageToken(pageToken string) *ProjectsLocationsApisListCall
func (c *ProjectsLocationsApisListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListApisResponse) error) error
type ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Context(ctx context.Context) *ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)
func (c *ProjectsLocationsApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisPatchCall
func (c *ProjectsLocationsApisPatchCall) Header() http.Header
func (c *ProjectsLocationsApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisPatchCall
type ProjectsLocationsApisService
func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService
func (r *ProjectsLocationsApisService) Create(parent string, googlecloudapihubv1api *GoogleCloudApihubV1Api) *ProjectsLocationsApisCreateCall
func (r *ProjectsLocationsApisService) Delete(name string) *ProjectsLocationsApisDeleteCall
func (r *ProjectsLocationsApisService) Get(name string) *ProjectsLocationsApisGetCall
func (r *ProjectsLocationsApisService) List(parent string) *ProjectsLocationsApisListCall
func (r *ProjectsLocationsApisService) Patch(name string, googlecloudapihubv1api *GoogleCloudApihubV1Api) *ProjectsLocationsApisPatchCall
type ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)
func (c *ProjectsLocationsApisVersionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsCreateCall
func (c *ProjectsLocationsApisVersionsCreateCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsCreateCall) VersionId(versionId string) *ProjectsLocationsApisVersionsCreateCall
type ProjectsLocationsApisVersionsDefinitionsGetCall
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDefinitionsGetCall
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Definition, error)
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDefinitionsGetCall
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsDefinitionsGetCall
type ProjectsLocationsApisVersionsDefinitionsService
func NewProjectsLocationsApisVersionsDefinitionsService(s *Service) *ProjectsLocationsApisVersionsDefinitionsService
func (r *ProjectsLocationsApisVersionsDefinitionsService) Get(name string) *ProjectsLocationsApisVersionsDefinitionsGetCall
type ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsDeleteCall
func (c *ProjectsLocationsApisVersionsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)
func (c *ProjectsLocationsApisVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetCall
func (c *ProjectsLocationsApisVersionsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetCall
type ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListVersionsResponse, error)
func (c *ProjectsLocationsApisVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Filter(filter string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsListCall
func (c *ProjectsLocationsApisVersionsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListVersionsResponse) error) error
type ProjectsLocationsApisVersionsOperationsCreateCall
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) ApiOperationId(apiOperationId string) *ProjectsLocationsApisVersionsOperationsCreateCall
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsCreateCall
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsCreateCall
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Header() http.Header
type ProjectsLocationsApisVersionsOperationsDeleteCall
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsDeleteCall
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsDeleteCall
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsOperationsGetCall
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsGetCall
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsGetCall
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsOperationsGetCall
type ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListApiOperationsResponse, error)
func (c *ProjectsLocationsApisVersionsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) Filter(filter string) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsOperationsListCall
func (c *ProjectsLocationsApisVersionsOperationsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsApisVersionsOperationsPatchCall
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsPatchCall
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsPatchCall
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsOperationsPatchCall
type ProjectsLocationsApisVersionsOperationsService
func NewProjectsLocationsApisVersionsOperationsService(s *Service) *ProjectsLocationsApisVersionsOperationsService
func (r *ProjectsLocationsApisVersionsOperationsService) Create(parent string, ...) *ProjectsLocationsApisVersionsOperationsCreateCall
func (r *ProjectsLocationsApisVersionsOperationsService) Delete(name string) *ProjectsLocationsApisVersionsOperationsDeleteCall
func (r *ProjectsLocationsApisVersionsOperationsService) Get(name string) *ProjectsLocationsApisVersionsOperationsGetCall
func (r *ProjectsLocationsApisVersionsOperationsService) List(parent string) *ProjectsLocationsApisVersionsOperationsListCall
func (r *ProjectsLocationsApisVersionsOperationsService) Patch(name string, googlecloudapihubv1apioperation *GoogleCloudApihubV1ApiOperation) *ProjectsLocationsApisVersionsOperationsPatchCall
type ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)
func (c *ProjectsLocationsApisVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsPatchCall
func (c *ProjectsLocationsApisVersionsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsPatchCall
type ProjectsLocationsApisVersionsService
func NewProjectsLocationsApisVersionsService(s *Service) *ProjectsLocationsApisVersionsService
func (r *ProjectsLocationsApisVersionsService) Create(parent string, googlecloudapihubv1version *GoogleCloudApihubV1Version) *ProjectsLocationsApisVersionsCreateCall
func (r *ProjectsLocationsApisVersionsService) Delete(name string) *ProjectsLocationsApisVersionsDeleteCall
func (r *ProjectsLocationsApisVersionsService) Get(name string) *ProjectsLocationsApisVersionsGetCall
func (r *ProjectsLocationsApisVersionsService) List(parent string) *ProjectsLocationsApisVersionsListCall
func (r *ProjectsLocationsApisVersionsService) Patch(name string, googlecloudapihubv1version *GoogleCloudApihubV1Version) *ProjectsLocationsApisVersionsPatchCall
type ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsCreateCall
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) SpecId(specId string) *ProjectsLocationsApisVersionsSpecsCreateCall
type ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1FetchAdditionalSpecContentResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) SpecContentType(specContentType string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
type ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetCall
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetCall
type ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1SpecContents, error)
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetContentsCall
type ProjectsLocationsApisVersionsSpecsLintCall
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsLintCall
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsLintCall
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Header() http.Header
type ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListSpecsResponse, error)
func (c *ProjectsLocationsApisVersionsSpecsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListCall
func (c *ProjectsLocationsApisVersionsSpecsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListSpecsResponse) error) error
type ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsPatchCall
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Header() http.Header
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsSpecsPatchCall
type ProjectsLocationsApisVersionsSpecsService
func NewProjectsLocationsApisVersionsSpecsService(s *Service) *ProjectsLocationsApisVersionsSpecsService
func (r *ProjectsLocationsApisVersionsSpecsService) Create(parent string, googlecloudapihubv1spec *GoogleCloudApihubV1Spec) *ProjectsLocationsApisVersionsSpecsCreateCall
func (r *ProjectsLocationsApisVersionsSpecsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsDeleteCall
func (r *ProjectsLocationsApisVersionsSpecsService) FetchAdditionalSpecContent(name string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall
func (r *ProjectsLocationsApisVersionsSpecsService) Get(name string) *ProjectsLocationsApisVersionsSpecsGetCall
func (r *ProjectsLocationsApisVersionsSpecsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsGetContentsCall
func (r *ProjectsLocationsApisVersionsSpecsService) Lint(name string, ...) *ProjectsLocationsApisVersionsSpecsLintCall
func (r *ProjectsLocationsApisVersionsSpecsService) List(parent string) *ProjectsLocationsApisVersionsSpecsListCall
func (r *ProjectsLocationsApisVersionsSpecsService) Patch(name string, googlecloudapihubv1spec *GoogleCloudApihubV1Spec) *ProjectsLocationsApisVersionsSpecsPatchCall
type ProjectsLocationsAttributesCreateCall
func (c *ProjectsLocationsAttributesCreateCall) AttributeId(attributeId string) *ProjectsLocationsAttributesCreateCall
func (c *ProjectsLocationsAttributesCreateCall) Context(ctx context.Context) *ProjectsLocationsAttributesCreateCall
func (c *ProjectsLocationsAttributesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)
func (c *ProjectsLocationsAttributesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesCreateCall
func (c *ProjectsLocationsAttributesCreateCall) Header() http.Header
type ProjectsLocationsAttributesDeleteCall
func (c *ProjectsLocationsAttributesDeleteCall) Context(ctx context.Context) *ProjectsLocationsAttributesDeleteCall
func (c *ProjectsLocationsAttributesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsAttributesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesDeleteCall
func (c *ProjectsLocationsAttributesDeleteCall) Header() http.Header
type ProjectsLocationsAttributesGetCall
func (c *ProjectsLocationsAttributesGetCall) Context(ctx context.Context) *ProjectsLocationsAttributesGetCall
func (c *ProjectsLocationsAttributesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)
func (c *ProjectsLocationsAttributesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesGetCall
func (c *ProjectsLocationsAttributesGetCall) Header() http.Header
func (c *ProjectsLocationsAttributesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAttributesGetCall
type ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) Context(ctx context.Context) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListAttributesResponse, error)
func (c *ProjectsLocationsAttributesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) Filter(filter string) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) Header() http.Header
func (c *ProjectsLocationsAttributesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) PageSize(pageSize int64) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) PageToken(pageToken string) *ProjectsLocationsAttributesListCall
func (c *ProjectsLocationsAttributesListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListAttributesResponse) error) error
type ProjectsLocationsAttributesPatchCall
func (c *ProjectsLocationsAttributesPatchCall) Context(ctx context.Context) *ProjectsLocationsAttributesPatchCall
func (c *ProjectsLocationsAttributesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)
func (c *ProjectsLocationsAttributesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesPatchCall
func (c *ProjectsLocationsAttributesPatchCall) Header() http.Header
func (c *ProjectsLocationsAttributesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAttributesPatchCall
type ProjectsLocationsAttributesService
func NewProjectsLocationsAttributesService(s *Service) *ProjectsLocationsAttributesService
func (r *ProjectsLocationsAttributesService) Create(parent string, googlecloudapihubv1attribute *GoogleCloudApihubV1Attribute) *ProjectsLocationsAttributesCreateCall
func (r *ProjectsLocationsAttributesService) Delete(name string) *ProjectsLocationsAttributesDeleteCall
func (r *ProjectsLocationsAttributesService) Get(name string) *ProjectsLocationsAttributesGetCall
func (r *ProjectsLocationsAttributesService) List(parent string) *ProjectsLocationsAttributesListCall
func (r *ProjectsLocationsAttributesService) Patch(name string, googlecloudapihubv1attribute *GoogleCloudApihubV1Attribute) *ProjectsLocationsAttributesPatchCall
type ProjectsLocationsCollectApiDataCall
func (c *ProjectsLocationsCollectApiDataCall) Context(ctx context.Context) *ProjectsLocationsCollectApiDataCall
func (c *ProjectsLocationsCollectApiDataCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsCollectApiDataCall) Fields(s ...googleapi.Field) *ProjectsLocationsCollectApiDataCall
func (c *ProjectsLocationsCollectApiDataCall) Header() http.Header
type ProjectsLocationsCurationsCreateCall
func (c *ProjectsLocationsCurationsCreateCall) Context(ctx context.Context) *ProjectsLocationsCurationsCreateCall
func (c *ProjectsLocationsCurationsCreateCall) CurationId(curationId string) *ProjectsLocationsCurationsCreateCall
func (c *ProjectsLocationsCurationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)
func (c *ProjectsLocationsCurationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsCreateCall
func (c *ProjectsLocationsCurationsCreateCall) Header() http.Header
type ProjectsLocationsCurationsDeleteCall
func (c *ProjectsLocationsCurationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsCurationsDeleteCall
func (c *ProjectsLocationsCurationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsCurationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsDeleteCall
func (c *ProjectsLocationsCurationsDeleteCall) Header() http.Header
type ProjectsLocationsCurationsGetCall
func (c *ProjectsLocationsCurationsGetCall) Context(ctx context.Context) *ProjectsLocationsCurationsGetCall
func (c *ProjectsLocationsCurationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)
func (c *ProjectsLocationsCurationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsGetCall
func (c *ProjectsLocationsCurationsGetCall) Header() http.Header
func (c *ProjectsLocationsCurationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsCurationsGetCall
type ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) Context(ctx context.Context) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListCurationsResponse, error)
func (c *ProjectsLocationsCurationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) Filter(filter string) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) Header() http.Header
func (c *ProjectsLocationsCurationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) PageSize(pageSize int64) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) PageToken(pageToken string) *ProjectsLocationsCurationsListCall
func (c *ProjectsLocationsCurationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListCurationsResponse) error) error
type ProjectsLocationsCurationsPatchCall
func (c *ProjectsLocationsCurationsPatchCall) Context(ctx context.Context) *ProjectsLocationsCurationsPatchCall
func (c *ProjectsLocationsCurationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)
func (c *ProjectsLocationsCurationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsPatchCall
func (c *ProjectsLocationsCurationsPatchCall) Header() http.Header
func (c *ProjectsLocationsCurationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsCurationsPatchCall
type ProjectsLocationsCurationsService
func NewProjectsLocationsCurationsService(s *Service) *ProjectsLocationsCurationsService
func (r *ProjectsLocationsCurationsService) Create(parent string, googlecloudapihubv1curation *GoogleCloudApihubV1Curation) *ProjectsLocationsCurationsCreateCall
func (r *ProjectsLocationsCurationsService) Delete(name string) *ProjectsLocationsCurationsDeleteCall
func (r *ProjectsLocationsCurationsService) Get(name string) *ProjectsLocationsCurationsGetCall
func (r *ProjectsLocationsCurationsService) List(parent string) *ProjectsLocationsCurationsListCall
func (r *ProjectsLocationsCurationsService) Patch(name string, googlecloudapihubv1curation *GoogleCloudApihubV1Curation) *ProjectsLocationsCurationsPatchCall
type ProjectsLocationsDependenciesCreateCall
func (c *ProjectsLocationsDependenciesCreateCall) Context(ctx context.Context) *ProjectsLocationsDependenciesCreateCall
func (c *ProjectsLocationsDependenciesCreateCall) DependencyId(dependencyId string) *ProjectsLocationsDependenciesCreateCall
func (c *ProjectsLocationsDependenciesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)
func (c *ProjectsLocationsDependenciesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesCreateCall
func (c *ProjectsLocationsDependenciesCreateCall) Header() http.Header
type ProjectsLocationsDependenciesDeleteCall
func (c *ProjectsLocationsDependenciesDeleteCall) Context(ctx context.Context) *ProjectsLocationsDependenciesDeleteCall
func (c *ProjectsLocationsDependenciesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsDependenciesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesDeleteCall
func (c *ProjectsLocationsDependenciesDeleteCall) Header() http.Header
type ProjectsLocationsDependenciesGetCall
func (c *ProjectsLocationsDependenciesGetCall) Context(ctx context.Context) *ProjectsLocationsDependenciesGetCall
func (c *ProjectsLocationsDependenciesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)
func (c *ProjectsLocationsDependenciesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesGetCall
func (c *ProjectsLocationsDependenciesGetCall) Header() http.Header
func (c *ProjectsLocationsDependenciesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDependenciesGetCall
type ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) Context(ctx context.Context) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDependenciesResponse, error)
func (c *ProjectsLocationsDependenciesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) Filter(filter string) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) Header() http.Header
func (c *ProjectsLocationsDependenciesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) PageSize(pageSize int64) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) PageToken(pageToken string) *ProjectsLocationsDependenciesListCall
func (c *ProjectsLocationsDependenciesListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsDependenciesPatchCall
func (c *ProjectsLocationsDependenciesPatchCall) Context(ctx context.Context) *ProjectsLocationsDependenciesPatchCall
func (c *ProjectsLocationsDependenciesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)
func (c *ProjectsLocationsDependenciesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesPatchCall
func (c *ProjectsLocationsDependenciesPatchCall) Header() http.Header
func (c *ProjectsLocationsDependenciesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsDependenciesPatchCall
type ProjectsLocationsDependenciesService
func NewProjectsLocationsDependenciesService(s *Service) *ProjectsLocationsDependenciesService
func (r *ProjectsLocationsDependenciesService) Create(parent string, googlecloudapihubv1dependency *GoogleCloudApihubV1Dependency) *ProjectsLocationsDependenciesCreateCall
func (r *ProjectsLocationsDependenciesService) Delete(name string) *ProjectsLocationsDependenciesDeleteCall
func (r *ProjectsLocationsDependenciesService) Get(name string) *ProjectsLocationsDependenciesGetCall
func (r *ProjectsLocationsDependenciesService) List(parent string) *ProjectsLocationsDependenciesListCall
func (r *ProjectsLocationsDependenciesService) Patch(name string, googlecloudapihubv1dependency *GoogleCloudApihubV1Dependency) *ProjectsLocationsDependenciesPatchCall
type ProjectsLocationsDeploymentsCreateCall
func (c *ProjectsLocationsDeploymentsCreateCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsCreateCall
func (c *ProjectsLocationsDeploymentsCreateCall) DeploymentId(deploymentId string) *ProjectsLocationsDeploymentsCreateCall
func (c *ProjectsLocationsDeploymentsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)
func (c *ProjectsLocationsDeploymentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsCreateCall
func (c *ProjectsLocationsDeploymentsCreateCall) Header() http.Header
type ProjectsLocationsDeploymentsDeleteCall
func (c *ProjectsLocationsDeploymentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsDeleteCall
func (c *ProjectsLocationsDeploymentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsDeploymentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsDeleteCall
func (c *ProjectsLocationsDeploymentsDeleteCall) Header() http.Header
type ProjectsLocationsDeploymentsGetCall
func (c *ProjectsLocationsDeploymentsGetCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsGetCall
func (c *ProjectsLocationsDeploymentsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)
func (c *ProjectsLocationsDeploymentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsGetCall
func (c *ProjectsLocationsDeploymentsGetCall) Header() http.Header
func (c *ProjectsLocationsDeploymentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDeploymentsGetCall
type ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDeploymentsResponse, error)
func (c *ProjectsLocationsDeploymentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) Filter(filter string) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) Header() http.Header
func (c *ProjectsLocationsDeploymentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) PageSize(pageSize int64) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) PageToken(pageToken string) *ProjectsLocationsDeploymentsListCall
func (c *ProjectsLocationsDeploymentsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListDeploymentsResponse) error) error
type ProjectsLocationsDeploymentsPatchCall
func (c *ProjectsLocationsDeploymentsPatchCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsPatchCall
func (c *ProjectsLocationsDeploymentsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)
func (c *ProjectsLocationsDeploymentsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsPatchCall
func (c *ProjectsLocationsDeploymentsPatchCall) Header() http.Header
func (c *ProjectsLocationsDeploymentsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsDeploymentsPatchCall
type ProjectsLocationsDeploymentsService
func NewProjectsLocationsDeploymentsService(s *Service) *ProjectsLocationsDeploymentsService
func (r *ProjectsLocationsDeploymentsService) Create(parent string, googlecloudapihubv1deployment *GoogleCloudApihubV1Deployment) *ProjectsLocationsDeploymentsCreateCall
func (r *ProjectsLocationsDeploymentsService) Delete(name string) *ProjectsLocationsDeploymentsDeleteCall
func (r *ProjectsLocationsDeploymentsService) Get(name string) *ProjectsLocationsDeploymentsGetCall
func (r *ProjectsLocationsDeploymentsService) List(parent string) *ProjectsLocationsDeploymentsListCall
func (r *ProjectsLocationsDeploymentsService) Patch(name string, googlecloudapihubv1deployment *GoogleCloudApihubV1Deployment) *ProjectsLocationsDeploymentsPatchCall
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1DiscoveredApiOperation, error)
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDiscoveredApiOperationsResponse, error)
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService
func NewProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService(s *Service) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService
func (r *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) Get(name string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall
func (r *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) List(parent string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall
type ProjectsLocationsDiscoveredApiObservationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1DiscoveredApiObservation, error)
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsGetCall
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsGetCall
type ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDiscoveredApiObservationsResponse, error)
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Header() http.Header
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredApiObservationsListCall
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsDiscoveredApiObservationsService
func NewProjectsLocationsDiscoveredApiObservationsService(s *Service) *ProjectsLocationsDiscoveredApiObservationsService
func (r *ProjectsLocationsDiscoveredApiObservationsService) Get(name string) *ProjectsLocationsDiscoveredApiObservationsGetCall
func (r *ProjectsLocationsDiscoveredApiObservationsService) List(parent string) *ProjectsLocationsDiscoveredApiObservationsListCall
type ProjectsLocationsExternalApisCreateCall
func (c *ProjectsLocationsExternalApisCreateCall) Context(ctx context.Context) *ProjectsLocationsExternalApisCreateCall
func (c *ProjectsLocationsExternalApisCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)
func (c *ProjectsLocationsExternalApisCreateCall) ExternalApiId(externalApiId string) *ProjectsLocationsExternalApisCreateCall
func (c *ProjectsLocationsExternalApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisCreateCall
func (c *ProjectsLocationsExternalApisCreateCall) Header() http.Header
type ProjectsLocationsExternalApisDeleteCall
func (c *ProjectsLocationsExternalApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsExternalApisDeleteCall
func (c *ProjectsLocationsExternalApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsExternalApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisDeleteCall
func (c *ProjectsLocationsExternalApisDeleteCall) Header() http.Header
type ProjectsLocationsExternalApisGetCall
func (c *ProjectsLocationsExternalApisGetCall) Context(ctx context.Context) *ProjectsLocationsExternalApisGetCall
func (c *ProjectsLocationsExternalApisGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)
func (c *ProjectsLocationsExternalApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisGetCall
func (c *ProjectsLocationsExternalApisGetCall) Header() http.Header
func (c *ProjectsLocationsExternalApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsExternalApisGetCall
type ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) Context(ctx context.Context) *ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListExternalApisResponse, error)
func (c *ProjectsLocationsExternalApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) Header() http.Header
func (c *ProjectsLocationsExternalApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) PageSize(pageSize int64) *ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) PageToken(pageToken string) *ProjectsLocationsExternalApisListCall
func (c *ProjectsLocationsExternalApisListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsExternalApisPatchCall
func (c *ProjectsLocationsExternalApisPatchCall) Context(ctx context.Context) *ProjectsLocationsExternalApisPatchCall
func (c *ProjectsLocationsExternalApisPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)
func (c *ProjectsLocationsExternalApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisPatchCall
func (c *ProjectsLocationsExternalApisPatchCall) Header() http.Header
func (c *ProjectsLocationsExternalApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsExternalApisPatchCall
type ProjectsLocationsExternalApisService
func NewProjectsLocationsExternalApisService(s *Service) *ProjectsLocationsExternalApisService
func (r *ProjectsLocationsExternalApisService) Create(parent string, googlecloudapihubv1externalapi *GoogleCloudApihubV1ExternalApi) *ProjectsLocationsExternalApisCreateCall
func (r *ProjectsLocationsExternalApisService) Delete(name string) *ProjectsLocationsExternalApisDeleteCall
func (r *ProjectsLocationsExternalApisService) Get(name string) *ProjectsLocationsExternalApisGetCall
func (r *ProjectsLocationsExternalApisService) List(parent string) *ProjectsLocationsExternalApisListCall
func (r *ProjectsLocationsExternalApisService) Patch(name string, googlecloudapihubv1externalapi *GoogleCloudApihubV1ExternalApi) *ProjectsLocationsExternalApisPatchCall
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsHostProjectRegistrationsCreateCall
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsCreateCall
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1HostProjectRegistration, error)
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsCreateCall
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Header() http.Header
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) HostProjectRegistrationId(hostProjectRegistrationId string) *ProjectsLocationsHostProjectRegistrationsCreateCall
type ProjectsLocationsHostProjectRegistrationsGetCall
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsGetCall
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1HostProjectRegistration, error)
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsGetCall
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Header() http.Header
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsHostProjectRegistrationsGetCall
type ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListHostProjectRegistrationsResponse, error)
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Filter(filter string) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Header() http.Header
func (c *ProjectsLocationsHostProjectRegistrationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) OrderBy(orderBy string) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) PageSize(pageSize int64) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) PageToken(pageToken string) *ProjectsLocationsHostProjectRegistrationsListCall
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsHostProjectRegistrationsService
func NewProjectsLocationsHostProjectRegistrationsService(s *Service) *ProjectsLocationsHostProjectRegistrationsService
func (r *ProjectsLocationsHostProjectRegistrationsService) Create(parent string, ...) *ProjectsLocationsHostProjectRegistrationsCreateCall
func (r *ProjectsLocationsHostProjectRegistrationsService) Get(name string) *ProjectsLocationsHostProjectRegistrationsGetCall
func (r *ProjectsLocationsHostProjectRegistrationsService) List(parent string) *ProjectsLocationsHostProjectRegistrationsListCall
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
type ProjectsLocationsLookupRuntimeProjectAttachmentCall
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsLookupRuntimeProjectAttachmentCall
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse, error)
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsLookupRuntimeProjectAttachmentCall
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Header() http.Header
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) IfNoneMatch(entityTag string) *ProjectsLocationsLookupRuntimeProjectAttachmentCall
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
type ProjectsLocationsPluginsCreateCall
func (c *ProjectsLocationsPluginsCreateCall) Context(ctx context.Context) *ProjectsLocationsPluginsCreateCall
func (c *ProjectsLocationsPluginsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)
func (c *ProjectsLocationsPluginsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsCreateCall
func (c *ProjectsLocationsPluginsCreateCall) Header() http.Header
func (c *ProjectsLocationsPluginsCreateCall) PluginId(pluginId string) *ProjectsLocationsPluginsCreateCall
type ProjectsLocationsPluginsDeleteCall
func (c *ProjectsLocationsPluginsDeleteCall) Context(ctx context.Context) *ProjectsLocationsPluginsDeleteCall
func (c *ProjectsLocationsPluginsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsDeleteCall
func (c *ProjectsLocationsPluginsDeleteCall) Header() http.Header
type ProjectsLocationsPluginsDisableCall
func (c *ProjectsLocationsPluginsDisableCall) Context(ctx context.Context) *ProjectsLocationsPluginsDisableCall
func (c *ProjectsLocationsPluginsDisableCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)
func (c *ProjectsLocationsPluginsDisableCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsDisableCall
func (c *ProjectsLocationsPluginsDisableCall) Header() http.Header
type ProjectsLocationsPluginsEnableCall
func (c *ProjectsLocationsPluginsEnableCall) Context(ctx context.Context) *ProjectsLocationsPluginsEnableCall
func (c *ProjectsLocationsPluginsEnableCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)
func (c *ProjectsLocationsPluginsEnableCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsEnableCall
func (c *ProjectsLocationsPluginsEnableCall) Header() http.Header
type ProjectsLocationsPluginsGetCall
func (c *ProjectsLocationsPluginsGetCall) Context(ctx context.Context) *ProjectsLocationsPluginsGetCall
func (c *ProjectsLocationsPluginsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)
func (c *ProjectsLocationsPluginsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsGetCall
func (c *ProjectsLocationsPluginsGetCall) Header() http.Header
func (c *ProjectsLocationsPluginsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsGetCall
type ProjectsLocationsPluginsGetStyleGuideCall
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Context(ctx context.Context) *ProjectsLocationsPluginsGetStyleGuideCall
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuide, error)
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsGetStyleGuideCall
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Header() http.Header
func (c *ProjectsLocationsPluginsGetStyleGuideCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsGetStyleGuideCall
type ProjectsLocationsPluginsInstancesCreateCall
func (c *ProjectsLocationsPluginsInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesCreateCall
func (c *ProjectsLocationsPluginsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesCreateCall
func (c *ProjectsLocationsPluginsInstancesCreateCall) Header() http.Header
func (c *ProjectsLocationsPluginsInstancesCreateCall) PluginInstanceId(pluginInstanceId string) *ProjectsLocationsPluginsInstancesCreateCall
type ProjectsLocationsPluginsInstancesDeleteCall
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesDeleteCall
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesDeleteCall
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Header() http.Header
type ProjectsLocationsPluginsInstancesDisableActionCall
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesDisableActionCall
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesDisableActionCall
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Header() http.Header
type ProjectsLocationsPluginsInstancesEnableActionCall
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesEnableActionCall
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesEnableActionCall
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Header() http.Header
type ProjectsLocationsPluginsInstancesExecuteActionCall
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesExecuteActionCall
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesExecuteActionCall
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Header() http.Header
type ProjectsLocationsPluginsInstancesGetCall
func (c *ProjectsLocationsPluginsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesGetCall
func (c *ProjectsLocationsPluginsInstancesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1PluginInstance, error)
func (c *ProjectsLocationsPluginsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesGetCall
func (c *ProjectsLocationsPluginsInstancesGetCall) Header() http.Header
func (c *ProjectsLocationsPluginsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsInstancesGetCall
type ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListPluginInstancesResponse, error)
func (c *ProjectsLocationsPluginsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) Filter(filter string) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) Header() http.Header
func (c *ProjectsLocationsPluginsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) PageToken(pageToken string) *ProjectsLocationsPluginsInstancesListCall
func (c *ProjectsLocationsPluginsInstancesListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsPluginsInstancesManageSourceDataCall
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesManageSourceDataCall
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse, error)
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesManageSourceDataCall
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Header() http.Header
type ProjectsLocationsPluginsInstancesPatchCall
func (c *ProjectsLocationsPluginsInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesPatchCall
func (c *ProjectsLocationsPluginsInstancesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1PluginInstance, error)
func (c *ProjectsLocationsPluginsInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesPatchCall
func (c *ProjectsLocationsPluginsInstancesPatchCall) Header() http.Header
func (c *ProjectsLocationsPluginsInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsPluginsInstancesPatchCall
type ProjectsLocationsPluginsInstancesService
func NewProjectsLocationsPluginsInstancesService(s *Service) *ProjectsLocationsPluginsInstancesService
func (r *ProjectsLocationsPluginsInstancesService) Create(parent string, ...) *ProjectsLocationsPluginsInstancesCreateCall
func (r *ProjectsLocationsPluginsInstancesService) Delete(name string) *ProjectsLocationsPluginsInstancesDeleteCall
func (r *ProjectsLocationsPluginsInstancesService) DisableAction(name string, ...) *ProjectsLocationsPluginsInstancesDisableActionCall
func (r *ProjectsLocationsPluginsInstancesService) EnableAction(name string, ...) *ProjectsLocationsPluginsInstancesEnableActionCall
func (r *ProjectsLocationsPluginsInstancesService) ExecuteAction(name string, ...) *ProjectsLocationsPluginsInstancesExecuteActionCall
func (r *ProjectsLocationsPluginsInstancesService) Get(name string) *ProjectsLocationsPluginsInstancesGetCall
func (r *ProjectsLocationsPluginsInstancesService) List(parent string) *ProjectsLocationsPluginsInstancesListCall
func (r *ProjectsLocationsPluginsInstancesService) ManageSourceData(name string, ...) *ProjectsLocationsPluginsInstancesManageSourceDataCall
func (r *ProjectsLocationsPluginsInstancesService) Patch(name string, ...) *ProjectsLocationsPluginsInstancesPatchCall
type ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) Context(ctx context.Context) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListPluginsResponse, error)
func (c *ProjectsLocationsPluginsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) Filter(filter string) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) Header() http.Header
func (c *ProjectsLocationsPluginsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) PageSize(pageSize int64) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) PageToken(pageToken string) *ProjectsLocationsPluginsListCall
func (c *ProjectsLocationsPluginsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListPluginsResponse) error) error
type ProjectsLocationsPluginsService
func NewProjectsLocationsPluginsService(s *Service) *ProjectsLocationsPluginsService
func (r *ProjectsLocationsPluginsService) Create(parent string, googlecloudapihubv1plugin *GoogleCloudApihubV1Plugin) *ProjectsLocationsPluginsCreateCall
func (r *ProjectsLocationsPluginsService) Delete(name string) *ProjectsLocationsPluginsDeleteCall
func (r *ProjectsLocationsPluginsService) Disable(name string, ...) *ProjectsLocationsPluginsDisableCall
func (r *ProjectsLocationsPluginsService) Enable(name string, ...) *ProjectsLocationsPluginsEnableCall
func (r *ProjectsLocationsPluginsService) Get(name string) *ProjectsLocationsPluginsGetCall
func (r *ProjectsLocationsPluginsService) GetStyleGuide(name string) *ProjectsLocationsPluginsGetStyleGuideCall
func (r *ProjectsLocationsPluginsService) List(parent string) *ProjectsLocationsPluginsListCall
func (r *ProjectsLocationsPluginsService) UpdateStyleGuide(name string, googlecloudapihubv1styleguide *GoogleCloudApihubV1StyleGuide) *ProjectsLocationsPluginsUpdateStyleGuideCall
type ProjectsLocationsPluginsStyleGuideGetContentsCall
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Context(ctx context.Context) *ProjectsLocationsPluginsStyleGuideGetContentsCall
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuideContents, error)
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsStyleGuideGetContentsCall
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Header() http.Header
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsStyleGuideGetContentsCall
type ProjectsLocationsPluginsStyleGuideService
func NewProjectsLocationsPluginsStyleGuideService(s *Service) *ProjectsLocationsPluginsStyleGuideService
func (r *ProjectsLocationsPluginsStyleGuideService) GetContents(name string) *ProjectsLocationsPluginsStyleGuideGetContentsCall
type ProjectsLocationsPluginsUpdateStyleGuideCall
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Context(ctx context.Context) *ProjectsLocationsPluginsUpdateStyleGuideCall
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuide, error)
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsUpdateStyleGuideCall
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Header() http.Header
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) UpdateMask(updateMask string) *ProjectsLocationsPluginsUpdateStyleGuideCall
type ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) Context(ctx context.Context) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RetrieveApiViewsResponse, error)
func (c *ProjectsLocationsRetrieveApiViewsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) Filter(filter string) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) Header() http.Header
func (c *ProjectsLocationsRetrieveApiViewsCall) IfNoneMatch(entityTag string) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) PageSize(pageSize int64) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) PageToken(pageToken string) *ProjectsLocationsRetrieveApiViewsCall
func (c *ProjectsLocationsRetrieveApiViewsCall) Pages(ctx context.Context, ...) error
func (c *ProjectsLocationsRetrieveApiViewsCall) View(view string) *ProjectsLocationsRetrieveApiViewsCall
type ProjectsLocationsRuntimeProjectAttachmentsCreateCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RuntimeProjectAttachment, error)
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Header() http.Header
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) RuntimeProjectAttachmentId(runtimeProjectAttachmentId string) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall
type ProjectsLocationsRuntimeProjectAttachmentsDeleteCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Header() http.Header
type ProjectsLocationsRuntimeProjectAttachmentsGetCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsGetCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RuntimeProjectAttachment, error)
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsGetCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Header() http.Header
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeProjectAttachmentsGetCall
type ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse, error)
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Filter(filter string) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Header() http.Header
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) OrderBy(orderBy string) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsRuntimeProjectAttachmentsListCall
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsRuntimeProjectAttachmentsService
func NewProjectsLocationsRuntimeProjectAttachmentsService(s *Service) *ProjectsLocationsRuntimeProjectAttachmentsService
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Create(parent string, ...) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Delete(name string) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Get(name string) *ProjectsLocationsRuntimeProjectAttachmentsGetCall
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) List(parent string) *ProjectsLocationsRuntimeProjectAttachmentsListCall
type ProjectsLocationsSearchResourcesCall
func (c *ProjectsLocationsSearchResourcesCall) Context(ctx context.Context) *ProjectsLocationsSearchResourcesCall
func (c *ProjectsLocationsSearchResourcesCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1SearchResourcesResponse, error)
func (c *ProjectsLocationsSearchResourcesCall) Fields(s ...googleapi.Field) *ProjectsLocationsSearchResourcesCall
func (c *ProjectsLocationsSearchResourcesCall) Header() http.Header
func (c *ProjectsLocationsSearchResourcesCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1SearchResourcesResponse) error) error
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) CollectApiData(location string, ...) *ProjectsLocationsCollectApiDataCall
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
func (r *ProjectsLocationsService) LookupRuntimeProjectAttachment(name string) *ProjectsLocationsLookupRuntimeProjectAttachmentCall
func (r *ProjectsLocationsService) RetrieveApiViews(parent string) *ProjectsLocationsRetrieveApiViewsCall
func (r *ProjectsLocationsService) SearchResources(location string, ...) *ProjectsLocationsSearchResourcesCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
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
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type GoogleCloudApihubV1APIMetadata ¶
type GoogleCloudApihubV1APIMetadata struct {
	// Api: Required. The API resource to be pushed to Hub's collect layer. The ID
	// of the API resource will be generated by Hub to ensure uniqueness across all
	// APIs across systems.
	Api *GoogleCloudApihubV1Api `json:"api,omitempty"`
	// OriginalCreateTime: Optional. Timestamp indicating when the API was created
	// at the source.
	OriginalCreateTime string `json:"originalCreateTime,omitempty"`
	// OriginalId: Optional. The unique identifier of the API in the system where
	// it was originally created.
	OriginalId string `json:"originalId,omitempty"`
	// OriginalUpdateTime: Required. Timestamp indicating when the API was last
	// updated at the source.
	OriginalUpdateTime string `json:"originalUpdateTime,omitempty"`
	// Versions: Optional. The list of versions present in an API resource.
	Versions []*GoogleCloudApihubV1VersionMetadata `json:"versions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Api") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Api") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1APIMetadata: The API metadata.

func (GoogleCloudApihubV1APIMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1APIMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ActionExecutionDetail ¶
type GoogleCloudApihubV1ActionExecutionDetail struct {
	// ActionId: Required. The action id of the plugin to execute.
	ActionId string `json:"actionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ActionExecutionDetail: The details for the action to execute.

func (GoogleCloudApihubV1ActionExecutionDetail) MarshalJSON ¶
func (s GoogleCloudApihubV1ActionExecutionDetail) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AdditionalSpecContent ¶
added in v0.258.0
type GoogleCloudApihubV1AdditionalSpecContent struct {
	// CreateTime: Output only. The time at which the spec content was created.
	CreateTime string `json:"createTime,omitempty"`
	// Labels: Optional. The labels of the spec content e.g. specboost addon
	// version.
	Labels map[string]string `json:"labels,omitempty"`
	// SpecContentType: Required. The type of the spec content.
	//
	// Possible values:
	//   "SPEC_CONTENT_TYPE_UNSPECIFIED" - Unspecified spec content type. Defaults
	// to spec content uploaded by the user.
	//   "BOOSTED_SPEC_CONTENT" - The spec content type for boosted spec.
	//   "GATEWAY_OPEN_API_SPEC" - The spec content type for OpenAPI spec. This
	// enum is used for OpenAPI specs ingested via APIGEE X Gateway.
	SpecContentType string `json:"specContentType,omitempty"`
	// SpecContents: Optional. The additional spec contents.
	SpecContents *GoogleCloudApihubV1SpecContents `json:"specContents,omitempty"`
	// UpdateTime: Output only. The time at which the spec content was last
	// updated.
	UpdateTime string `json:"updateTime,omitempty"`
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

GoogleCloudApihubV1AdditionalSpecContent: The additional spec content for the spec. This contains the metadata and the last update time for the additional spec content.

func (GoogleCloudApihubV1AdditionalSpecContent) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1AdditionalSpecContent) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Addon ¶
added in v0.257.0
type GoogleCloudApihubV1Addon struct {
	// Config: Required. The configuration of the addon.
	Config *GoogleCloudApihubV1AddonConfig `json:"config,omitempty"`
	// CreateTime: Output only. The time at which the addon was created.
	CreateTime string `json:"createTime,omitempty"`
	// DataSource: Required. The data source on which the addon operates. This
	// determines which field in the `config` oneof is used.
	//
	// Possible values:
	//   "DATA_SOURCE_UNSPECIFIED" - The data source of the addon is not specified.
	//   "PLUGIN_INSTANCE" - Addon operates on data collected from specific plugin
	// instances.
	//   "ALL_DATA" - Addon operates on all data in the API hub.
	DataSource string `json:"dataSource,omitempty"`
	// Description: Optional. The description of the addon.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the addon.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Identifier. The name of the addon to enable. Format:
	// `projects/{project}/locations/{location}/addons/{addon}`.
	Name string `json:"name,omitempty"`
	// State: Output only. The state of the addon.
	//
	// Possible values:
	//   "ADDON_STATE_UNSPECIFIED" - The addon state is not specified.
	//   "ACTIVE" - The addon is active.
	//   "UPDATING" - The addon is being updated.
	//   "ERROR" - The addon is in error state.
	//   "INACTIVE" - The addon is inactive.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. The time at which the addon was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Config") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Config") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Addon: Addon resource.

func (GoogleCloudApihubV1Addon) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1Addon) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AddonConfig ¶
added in v0.257.0
type GoogleCloudApihubV1AddonConfig struct {
	// AllDataAddonConfig: Configuration for addons which act on all data in the
	// API hub.
	AllDataAddonConfig *GoogleCloudApihubV1AllDataAddonConfig `json:"allDataAddonConfig,omitempty"`
	// GatewayPluginAddonConfig: Configuration for gateway plugin addons.
	GatewayPluginAddonConfig *GoogleCloudApihubV1GatewayPluginAddonConfig `json:"gatewayPluginAddonConfig,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllDataAddonConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllDataAddonConfig") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1AddonConfig: Configuration for the addon.

func (GoogleCloudApihubV1AddonConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1AddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AllDataAddonConfig ¶
added in v0.257.0
type GoogleCloudApihubV1AllDataAddonConfig struct {
	// Enabled: Required. If true, the addon is enabled for all data in the API
	// hub.
	Enabled bool `json:"enabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Enabled") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Enabled") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1AllDataAddonConfig: Configuration for addons which act on all data in the API hub. This is used to specify if the addon is enabled for all data in the API hub.

func (GoogleCloudApihubV1AllDataAddonConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1AllDataAddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AllowedValue ¶
type GoogleCloudApihubV1AllowedValue struct {
	// Description: Optional. The detailed description of the allowed value.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the allowed value.
	DisplayName string `json:"displayName,omitempty"`
	// Id: Required. The ID of the allowed value. * If provided, the same will be
	// used. The service will throw an error if the specified id is already used by
	// another allowed value in the same attribute resource. * If not provided, a
	// system generated id derived from the display name will be used. In this
	// case, the service will handle conflict resolution by adding a system
	// generated suffix in case of duplicates. This value should be 4-63
	// characters, and valid characters are /a-z-/.
	Id string `json:"id,omitempty"`
	// Immutable: Optional. When set to true, the allowed value cannot be updated
	// or deleted by the user. It can only be true for System defined attributes.
	Immutable bool `json:"immutable,omitempty"`
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

GoogleCloudApihubV1AllowedValue: The value that can be assigned to the attribute when the data type is enum.

func (GoogleCloudApihubV1AllowedValue) MarshalJSON ¶
func (s GoogleCloudApihubV1AllowedValue) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Api ¶
type GoogleCloudApihubV1Api struct {
	// ApiFunctionalRequirements: Optional. The api functional requirements
	// associated with the API resource. Carinality is 1 for this attribute. This
	// maps to the following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-api-functional-req
	// uirements` attribute. The value of the attribute should be a proper URI, and
	// in case of Cloud Storage URI, it should point to a Cloud Storage object, not
	// a directory.
	ApiFunctionalRequirements *GoogleCloudApihubV1AttributeValues `json:"apiFunctionalRequirements,omitempty"`
	// ApiRequirements: Optional. The api requirement doc associated with the API
	// resource. Carinality is 1 for this attribute. This maps to the following
	// system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-api-requirements`
	// attribute. The value of the attribute should be a proper URI, and in case of
	// Cloud Storage URI, it should point to a Cloud Storage object, not a
	// directory.
	ApiRequirements *GoogleCloudApihubV1AttributeValues `json:"apiRequirements,omitempty"`
	// ApiStyle: Optional. The style of the API. This maps to the following system
	// defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-api-style`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	ApiStyle *GoogleCloudApihubV1AttributeValues `json:"apiStyle,omitempty"`
	// ApiTechnicalRequirements: Optional. The api technical requirements
	// associated with the API resource. Carinality is 1 for this attribute. This
	// maps to the following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-api-technical-requ
	// irements` attribute. The value of the attribute should be a proper URI, and
	// in case of Cloud Storage URI, it should point to a Cloud Storage object, not
	// a directory.
	ApiTechnicalRequirements *GoogleCloudApihubV1AttributeValues `json:"apiTechnicalRequirements,omitempty"`
	// Attributes: Optional. The list of user defined attributes associated with
	// the API resource. The key is the attribute name. It will be of the format:
	// `projects/{project}/locations/{location}/attributes/{attribute}`. The value
	// is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// BusinessUnit: Optional. The business unit owning the API. This maps to the
	// following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-business-unit`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	BusinessUnit *GoogleCloudApihubV1AttributeValues `json:"businessUnit,omitempty"`
	// CreateTime: Output only. The time at which the API resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. The description of the API resource.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the API resource.
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. The documentation for the API resource.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// Fingerprint: Optional. Fingerprint of the API resource. This must be unique
	// for each API resource. It can neither be unset nor be updated to an existing
	// fingerprint of another API resource.
	Fingerprint string `json:"fingerprint,omitempty"`
	// MaturityLevel: Optional. The maturity level of the API. This maps to the
	// following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-maturity-level`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	MaturityLevel *GoogleCloudApihubV1AttributeValues `json:"maturityLevel,omitempty"`
	// Name: Identifier. The name of the API resource in the API Hub. Format:
	// `projects/{project}/locations/{location}/apis/{api}`
	Name string `json:"name,omitempty"`
	// Owner: Optional. Owner details for the API resource.
	Owner *GoogleCloudApihubV1Owner `json:"owner,omitempty"`
	// SelectedVersion: Optional. The selected version for an API resource. This
	// can be used when special handling is needed on client side for particular
	// version of the API. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}`
	SelectedVersion string `json:"selectedVersion,omitempty"`
	// SourceMetadata: Output only. The list of sources and metadata from the
	// sources of the API resource.
	SourceMetadata []*GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// TargetUser: Optional. The target users for the API. This maps to the
	// following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-target-user`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	TargetUser *GoogleCloudApihubV1AttributeValues `json:"targetUser,omitempty"`
	// Team: Optional. The team owning the API. This maps to the following system
	// defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-team` attribute.
	// The number of values for this attribute will be based on the cardinality of
	// the attribute. The same can be retrieved via GetAttribute API. All values
	// should be from the list of allowed values defined for the attribute.
	Team *GoogleCloudApihubV1AttributeValues `json:"team,omitempty"`
	// UpdateTime: Output only. The time at which the API resource was last
	// updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// Versions: Output only. The list of versions present in an API resource.
	// Note: An API resource can be associated with more than 1 version. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}`
	Versions []string `json:"versions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiFunctionalRequirements")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiFunctionalRequirements") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Api: An API resource in the API Hub.

func (GoogleCloudApihubV1Api) MarshalJSON ¶
func (s GoogleCloudApihubV1Api) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiData ¶
type GoogleCloudApihubV1ApiData struct {
	// ApiMetadataList: Optional. The list of API metadata.
	ApiMetadataList *GoogleCloudApihubV1ApiMetadataList `json:"apiMetadataList,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiMetadataList") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiMetadataList") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiData: The API data to be collected.

func (GoogleCloudApihubV1ApiData) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiData) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiHubInstance ¶
type GoogleCloudApihubV1ApiHubInstance struct {
	// Config: Required. Config of the ApiHub instance.
	Config *GoogleCloudApihubV1Config `json:"config,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. Description of the ApiHub instance.
	Description string `json:"description,omitempty"`
	// Labels: Optional. Instance labels to represent user-provided metadata. Refer
	// to cloud documentation on labels for more details.
	// https://cloud.google.com/compute/docs/labeling-resources
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Identifier. Format:
	// `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.
	Name string `json:"name,omitempty"`
	// State: Output only. The current state of the ApiHub instance.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The default value. This value is used if the state
	// is omitted.
	//   "INACTIVE" - The ApiHub instance has not been initialized or has been
	// deleted.
	//   "CREATING" - The ApiHub instance is being created.
	//   "ACTIVE" - The ApiHub instance has been created and is ready for use.
	//   "UPDATING" - The ApiHub instance is being updated.
	//   "DELETING" - The ApiHub instance is being deleted.
	//   "FAILED" - The ApiHub instance encountered an error during a state change.
	State string `json:"state,omitempty"`
	// StateMessage: Output only. Extra information about ApiHub instance state.
	// Currently the message would be populated when state is `FAILED`.
	StateMessage string `json:"stateMessage,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Config") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Config") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiHubInstance: An ApiHubInstance represents the instance resources of the API Hub. Currently, only one ApiHub instance is allowed for each project.

func (GoogleCloudApihubV1ApiHubInstance) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiHubInstance) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiHubResource ¶
type GoogleCloudApihubV1ApiHubResource struct {
	// Api: This represents Api resource in search results. Only name,
	// display_name, description and owner fields are populated in search results.
	Api *GoogleCloudApihubV1Api `json:"api,omitempty"`
	// Definition: This represents Definition resource in search results. Only name
	// field is populated in search results.
	Definition *GoogleCloudApihubV1Definition `json:"definition,omitempty"`
	// Deployment: This represents Deployment resource in search results. Only
	// name, display_name, description, deployment_type and api_versions fields are
	// populated in search results.
	Deployment *GoogleCloudApihubV1Deployment `json:"deployment,omitempty"`
	// Operation: This represents ApiOperation resource in search results. Only
	// name, description, spec and details fields are populated in search results.
	Operation *GoogleCloudApihubV1ApiOperation `json:"operation,omitempty"`
	// Spec: This represents Spec resource in search results. Only name,
	// display_name, description, spec_type and documentation fields are populated
	// in search results.
	Spec *GoogleCloudApihubV1Spec `json:"spec,omitempty"`
	// Version: This represents Version resource in search results. Only name,
	// display_name, description, lifecycle, compliance and accreditation fields
	// are populated in search results.
	Version *GoogleCloudApihubV1Version `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Api") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Api") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiHubResource: ApiHubResource is one of the resources such as Api, Operation, Deployment, Definition, Spec and Version resources stored in API-Hub.

func (GoogleCloudApihubV1ApiHubResource) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiHubResource) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiKeyConfig ¶
type GoogleCloudApihubV1ApiKeyConfig struct {
	// ApiKey: Required. The name of the SecretManager secret version resource
	// storing the API key. Format:
	// `projects/{project}/secrets/{secrete}/versions/{version}`. The
	// `secretmanager.versions.access` permission should be granted to the service
	// account accessing the secret.
	ApiKey *GoogleCloudApihubV1Secret `json:"apiKey,omitempty"`
	// HttpElementLocation: Required. The location of the API key. The default
	// value is QUERY.
	//
	// Possible values:
	//   "HTTP_ELEMENT_LOCATION_UNSPECIFIED" - HTTP element location not specified.
	//   "QUERY" - Element is in the HTTP request query.
	//   "HEADER" - Element is in the HTTP request header.
	//   "PATH" - Element is in the HTTP request path.
	//   "BODY" - Element is in the HTTP request body.
	//   "COOKIE" - Element is in the HTTP request cookie.
	HttpElementLocation string `json:"httpElementLocation,omitempty"`
	// Name: Required. The parameter name of the API key. E.g. If the API request
	// is "https://example.com/act?api_key=", "api_key" would be the parameter
	// name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiKey") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiKey") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiKeyConfig: Config for authentication with API key.

func (GoogleCloudApihubV1ApiKeyConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiKeyConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiMetadataList ¶
type GoogleCloudApihubV1ApiMetadataList struct {
	// ApiMetadata: Required. The list of API metadata.
	ApiMetadata []*GoogleCloudApihubV1APIMetadata `json:"apiMetadata,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiMetadata") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiMetadataList: The message to hold repeated API metadata.

func (GoogleCloudApihubV1ApiMetadataList) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiMetadataList) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiOperation ¶
type GoogleCloudApihubV1ApiOperation struct {
	// Attributes: Optional. The list of user defined attributes associated with
	// the API operation resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// CreateTime: Output only. The time at which the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// Details: Optional. Operation details. Note: Even though this field is
	// optional, it is required for CreateApiOperation API and we will fail the
	// request if not provided.
	Details *GoogleCloudApihubV1OperationDetails `json:"details,omitempty"`
	// Name: Identifier. The name of the operation. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operat
	// ions/{operation}`
	Name string `json:"name,omitempty"`
	// SourceMetadata: Output only. The list of sources and metadata from the
	// sources of the API operation.
	SourceMetadata []*GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// Spec: Output only. The name of the spec will be of the format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/
	// {spec}` Note:The name of the spec will be empty if the operation is created
	// via CreateApiOperation API.
	Spec string `json:"spec,omitempty"`
	// UpdateTime: Output only. The time at which the operation was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiOperation: Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.

func (GoogleCloudApihubV1ApiOperation) MarshalJSON ¶
func (s GoogleCloudApihubV1ApiOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApiView ¶
added in v0.258.0
type GoogleCloudApihubV1ApiView struct {
	// McpServerView: Output only. MCP server view.
	McpServerView *GoogleCloudApihubV1FlattenedApiVersionDeploymentView `json:"mcpServerView,omitempty"`
	// McpToolView: Output only. MCP tools view.
	McpToolView *GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView `json:"mcpToolView,omitempty"`
	// ForceSendFields is a list of field names (e.g. "McpServerView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "McpServerView") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApiView: The view of an API.

func (GoogleCloudApihubV1ApiView) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1ApiView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeEdgeConfig ¶
added in v0.257.0
type GoogleCloudApihubV1ApigeeEdgeConfig struct {
	// EnvironmentFilter: Optional. The filter to apply on the resources managed by
	// the gateway plugin instance. If provided this filter applies environment
	// specific filtering.
	EnvironmentFilter *GoogleCloudApihubV1EnvironmentFilter `json:"environmentFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnvironmentFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnvironmentFilter") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApigeeEdgeConfig: Configuration for Apigee Edge gateways. Applicability of a filter is determined by the filter being provided. If none of the filters are provided the addon will be enabled for all data brought in by the gateway plugin instance.

func (GoogleCloudApihubV1ApigeeEdgeConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1ApigeeEdgeConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeOPDKConfig ¶
added in v0.257.0
type GoogleCloudApihubV1ApigeeOPDKConfig struct {
	// EnvironmentFilter: Optional. The filter to apply on the resources managed by
	// the gateway plugin instance. If provided this filter applies environment
	// specific filtering.
	EnvironmentFilter *GoogleCloudApihubV1EnvironmentFilter `json:"environmentFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnvironmentFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnvironmentFilter") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApigeeOPDKConfig: Configuration for Apigee OPDK gateways. Applicability of a filter is determined by the filter being provided. If none of the filters are provided the addon will be enabled for all data brought in by the gateway plugin instance.

func (GoogleCloudApihubV1ApigeeOPDKConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1ApigeeOPDKConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApigeeXHybridConfig ¶
added in v0.257.0
type GoogleCloudApihubV1ApigeeXHybridConfig struct {
	// EnvironmentFilter: Optional. The filter to apply on the resources managed by
	// the gateway plugin instance. If provided this filter applies environment
	// specific filtering.
	EnvironmentFilter *GoogleCloudApihubV1EnvironmentFilter `json:"environmentFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnvironmentFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnvironmentFilter") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApigeeXHybridConfig: Configuration for Apigee X and Apigee Hybrid gateways. Applicability of a filter is determined by the filter being provided. If none of the filters are provided the addon will be enabled for all data brought in by the gateway plugin instance.

func (GoogleCloudApihubV1ApigeeXHybridConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1ApigeeXHybridConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ApplicationIntegrationEndpointDetails ¶
type GoogleCloudApihubV1ApplicationIntegrationEndpointDetails struct {
	// TriggerId: Required. The API trigger ID of the Application Integration
	// workflow.
	TriggerId string `json:"triggerId,omitempty"`
	// Uri: Required. The endpoint URI should be a valid REST URI for triggering an
	// Application Integration. Format:
	// `https://integrations.googleapis.com/v1/{name=projects/*/locations/*/integrat
	// ions/*}:execute` or
	// `https://{location}-integrations.googleapis.com/v1/{name=projects/*/locations
	// /*/integrations/*}:execute`
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TriggerId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TriggerId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ApplicationIntegrationEndpointDetails: The details of the Application Integration endpoint to be triggered for curation.

func (GoogleCloudApihubV1ApplicationIntegrationEndpointDetails) MarshalJSON ¶
func (s GoogleCloudApihubV1ApplicationIntegrationEndpointDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Attribute ¶
type GoogleCloudApihubV1Attribute struct {
	// AllowedValues: Optional. The list of allowed values when the attribute value
	// is of type enum. This is required when the data_type of the attribute is
	// ENUM. The maximum number of allowed values of an attribute will be 1000.
	AllowedValues []*GoogleCloudApihubV1AllowedValue `json:"allowedValues,omitempty"`
	// Cardinality: Optional. The maximum number of values that the attribute can
	// have when associated with an API Hub resource. Cardinality 1 would represent
	// a single-valued attribute. It must not be less than 1 or greater than 20. If
	// not specified, the cardinality would be set to 1 by default and represent a
	// single-valued attribute.
	Cardinality int64 `json:"cardinality,omitempty"`
	// CreateTime: Output only. The time at which the attribute was created.
	CreateTime string `json:"createTime,omitempty"`
	// DataType: Required. The type of the data of the attribute.
	//
	// Possible values:
	//   "DATA_TYPE_UNSPECIFIED" - Attribute data type unspecified.
	//   "ENUM" - Attribute's value is of type enum.
	//   "JSON" - Attribute's value is of type json.
	//   "STRING" - Attribute's value is of type string.
	//   "URI" - Attribute's value is of type uri.
	DataType string `json:"dataType,omitempty"`
	// DefinitionType: Output only. The definition type of the attribute.
	//
	// Possible values:
	//   "DEFINITION_TYPE_UNSPECIFIED" - Attribute definition type unspecified.
	//   "SYSTEM_DEFINED" - The attribute is predefined by the API Hub. Note that
	// only the list of allowed values can be updated in this case via
	// UpdateAttribute method.
	//   "USER_DEFINED" - The attribute is defined by the user.
	DefinitionType string `json:"definitionType,omitempty"`
	// Description: Optional. The description of the attribute.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the attribute.
	DisplayName string `json:"displayName,omitempty"`
	// Mandatory: Output only. When mandatory is true, the attribute is mandatory
	// for the resource specified in the scope. Only System defined attributes can
	// be mandatory.
	Mandatory bool `json:"mandatory,omitempty"`
	// Name: Identifier. The name of the attribute in the API Hub. Format:
	// `projects/{project}/locations/{location}/attributes/{attribute}`
	Name string `json:"name,omitempty"`
	// Scope: Required. The scope of the attribute. It represents the resource in
	// the API Hub to which the attribute can be linked.
	//
	// Possible values:
	//   "SCOPE_UNSPECIFIED" - Scope Unspecified.
	//   "API" - Attribute can be linked to an API.
	//   "VERSION" - Attribute can be linked to an API version.
	//   "SPEC" - Attribute can be linked to a Spec.
	//   "API_OPERATION" - Attribute can be linked to an API Operation.
	//   "DEPLOYMENT" - Attribute can be linked to a Deployment.
	//   "DEPENDENCY" - Attribute can be linked to a Dependency.
	//   "DEFINITION" - Attribute can be linked to a definition.
	//   "EXTERNAL_API" - Attribute can be linked to a ExternalAPI.
	//   "PLUGIN" - Attribute can be linked to a Plugin.
	Scope string `json:"scope,omitempty"`
	// UpdateTime: Output only. The time at which the attribute was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AllowedValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedValues") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Attribute: An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.

func (GoogleCloudApihubV1Attribute) MarshalJSON ¶
func (s GoogleCloudApihubV1Attribute) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AttributeValues ¶
type GoogleCloudApihubV1AttributeValues struct {
	// Attribute: Output only. The name of the attribute. Format:
	// projects/{project}/locations/{location}/attributes/{attribute}
	Attribute string `json:"attribute,omitempty"`
	// EnumValues: The attribute values associated with a resource in case
	// attribute data type is enum.
	EnumValues *GoogleCloudApihubV1EnumAttributeValues `json:"enumValues,omitempty"`
	// JsonValues: The attribute values associated with a resource in case
	// attribute data type is JSON.
	JsonValues *GoogleCloudApihubV1StringAttributeValues `json:"jsonValues,omitempty"`
	// StringValues: The attribute values associated with a resource in case
	// attribute data type is string.
	StringValues *GoogleCloudApihubV1StringAttributeValues `json:"stringValues,omitempty"`
	// UriValues: The attribute values associated with a resource in case attribute
	// data type is URL, URI or IP, like gs://bucket-name/object-name.
	UriValues *GoogleCloudApihubV1StringAttributeValues `json:"uriValues,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Attribute") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attribute") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1AttributeValues: The attribute values associated with resource.

func (GoogleCloudApihubV1AttributeValues) MarshalJSON ¶
func (s GoogleCloudApihubV1AttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AuthConfig ¶
type GoogleCloudApihubV1AuthConfig struct {
	// ApiKeyConfig: Api Key Config.
	ApiKeyConfig *GoogleCloudApihubV1ApiKeyConfig `json:"apiKeyConfig,omitempty"`
	// AuthType: Required. The authentication type.
	//
	// Possible values:
	//   "AUTH_TYPE_UNSPECIFIED" - Authentication type not specified.
	//   "NO_AUTH" - No authentication.
	//   "GOOGLE_SERVICE_ACCOUNT" - Google service account authentication.
	//   "USER_PASSWORD" - Username and password authentication.
	//   "API_KEY" - API Key authentication.
	//   "OAUTH2_CLIENT_CREDENTIALS" - Oauth 2.0 client credentials grant
	// authentication.
	AuthType string `json:"authType,omitempty"`
	// GoogleServiceAccountConfig: Google Service Account.
	GoogleServiceAccountConfig *GoogleCloudApihubV1GoogleServiceAccountConfig `json:"googleServiceAccountConfig,omitempty"`
	// Oauth2ClientCredentialsConfig: Oauth2.0 Client Credentials.
	Oauth2ClientCredentialsConfig *GoogleCloudApihubV1Oauth2ClientCredentialsConfig `json:"oauth2ClientCredentialsConfig,omitempty"`
	// UserPasswordConfig: User Password.
	UserPasswordConfig *GoogleCloudApihubV1UserPasswordConfig `json:"userPasswordConfig,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiKeyConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiKeyConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1AuthConfig: AuthConfig represents the authentication information.

func (GoogleCloudApihubV1AuthConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1AuthConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1AuthConfigTemplate ¶
type GoogleCloudApihubV1AuthConfigTemplate struct {
	// ServiceAccount: Optional. The service account of the plugin hosting service.
	// This service account should be granted the required permissions on the Auth
	// Config parameters provided while creating the plugin instances corresponding
	// to this plugin. For example, if the plugin instance auth config requires a
	// secret manager secret, the service account should be granted the
	// secretmanager.versions.access permission on the corresponding secret, if the
	// plugin instance auth config contains a service account, the service account
	// should be granted the iam.serviceAccounts.getAccessToken permission on the
	// corresponding service account.
	ServiceAccount *GoogleCloudApihubV1GoogleServiceAccountConfig `json:"serviceAccount,omitempty"`
	// SupportedAuthTypes: Required. The list of authentication types supported by
	// the plugin.
	//
	// Possible values:
	//   "AUTH_TYPE_UNSPECIFIED" - Authentication type not specified.
	//   "NO_AUTH" - No authentication.
	//   "GOOGLE_SERVICE_ACCOUNT" - Google service account authentication.
	//   "USER_PASSWORD" - Username and password authentication.
	//   "API_KEY" - API Key authentication.
	//   "OAUTH2_CLIENT_CREDENTIALS" - Oauth 2.0 client credentials grant
	// authentication.
	SupportedAuthTypes []string `json:"supportedAuthTypes,omitempty"`
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

GoogleCloudApihubV1AuthConfigTemplate: AuthConfigTemplate represents the authentication template for a plugin.

func (GoogleCloudApihubV1AuthConfigTemplate) MarshalJSON ¶
func (s GoogleCloudApihubV1AuthConfigTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CollectApiDataRequest ¶
type GoogleCloudApihubV1CollectApiDataRequest struct {
	// ActionId: Required. The action ID to be used for collecting the API data.
	// This should map to one of the action IDs specified in action configs in the
	// plugin.
	ActionId string `json:"actionId,omitempty"`
	// ApiData: Required. The API data to be collected.
	ApiData *GoogleCloudApihubV1ApiData `json:"apiData,omitempty"`
	// CollectionType: Required. The type of collection. Applies to all entries in
	// api_data.
	//
	// Possible values:
	//   "COLLECTION_TYPE_UNSPECIFIED" - The default value. This value is used if
	// the collection type is omitted.
	//   "COLLECTION_TYPE_UPSERT" - The collection type is upsert. This should be
	// used when an API is created or updated at the source.
	//   "COLLECTION_TYPE_DELETE" - The collection type is delete. This should be
	// used when an API is deleted at the source.
	CollectionType string `json:"collectionType,omitempty"`
	// PluginInstance: Required. The plugin instance collecting the API data.
	// Format:
	// `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance
	// }`.
	PluginInstance string `json:"pluginInstance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1CollectApiDataRequest: The CollectApiData method's request.

func (GoogleCloudApihubV1CollectApiDataRequest) MarshalJSON ¶
func (s GoogleCloudApihubV1CollectApiDataRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Config ¶
type GoogleCloudApihubV1Config struct {
	// CmekKeyName: Optional. The Customer Managed Encryption Key (CMEK) used for
	// data encryption. The CMEK name should follow the format of
	// `projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)`,
	// where the location must match the instance location. If the CMEK is not
	// provided, a GMEK will be created for the instance.
	CmekKeyName string `json:"cmekKeyName,omitempty"`
	// DisableSearch: Optional. If true, the search will be disabled for the
	// instance. The default value is false.
	DisableSearch bool `json:"disableSearch,omitempty"`
	// EncryptionType: Optional. Encryption type for the region. If the encryption
	// type is CMEK, the cmek_key_name must be provided. If no encryption type is
	// provided, GMEK will be used.
	//
	// Possible values:
	//   "ENCRYPTION_TYPE_UNSPECIFIED" - Encryption type unspecified.
	//   "GMEK" - Default encryption using Google managed encryption key.
	//   "CMEK" - Encryption using customer managed encryption key.
	EncryptionType string `json:"encryptionType,omitempty"`
	// VertexLocation: Optional. The name of the Vertex AI location where the data
	// store is stored.
	VertexLocation string `json:"vertexLocation,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CmekKeyName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CmekKeyName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Config: Available configurations to provision an ApiHub Instance.

func (GoogleCloudApihubV1Config) MarshalJSON ¶
func (s GoogleCloudApihubV1Config) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigTemplate ¶
type GoogleCloudApihubV1ConfigTemplate struct {
	// AdditionalConfigTemplate: Optional. The list of additional configuration
	// variables for the plugin's configuration.
	AdditionalConfigTemplate []*GoogleCloudApihubV1ConfigVariableTemplate `json:"additionalConfigTemplate,omitempty"`
	// AuthConfigTemplate: Optional. The authentication template for the plugin.
	AuthConfigTemplate *GoogleCloudApihubV1AuthConfigTemplate `json:"authConfigTemplate,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdditionalConfigTemplate")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalConfigTemplate") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ConfigTemplate: ConfigTemplate represents the configuration template for a plugin.

func (GoogleCloudApihubV1ConfigTemplate) MarshalJSON ¶
func (s GoogleCloudApihubV1ConfigTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigValueOption ¶
type GoogleCloudApihubV1ConfigValueOption struct {
	// Description: Optional. Description of the option.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. Display name of the option.
	DisplayName string `json:"displayName,omitempty"`
	// Id: Required. Id of the option.
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

GoogleCloudApihubV1ConfigValueOption: ConfigValueOption represents an option for a config variable of type enum or multi select.

func (GoogleCloudApihubV1ConfigValueOption) MarshalJSON ¶
func (s GoogleCloudApihubV1ConfigValueOption) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigVariable ¶
type GoogleCloudApihubV1ConfigVariable struct {
	// BoolValue: Optional. The config variable value in case of config variable of
	// type boolean.
	BoolValue bool `json:"boolValue,omitempty"`
	// EnumValue: Optional. The config variable value in case of config variable of
	// type enum.
	EnumValue *GoogleCloudApihubV1ConfigValueOption `json:"enumValue,omitempty"`
	// IntValue: Optional. The config variable value in case of config variable of
	// type integer.
	IntValue int64 `json:"intValue,omitempty,string"`
	// Key: Output only. Key will be the id to uniquely identify the config
	// variable.
	Key string `json:"key,omitempty"`
	// MultiIntValues: Optional. The config variable value in case of config
	// variable of type multi integer.
	MultiIntValues *GoogleCloudApihubV1MultiIntValues `json:"multiIntValues,omitempty"`
	// MultiSelectValues: Optional. The config variable value in case of config
	// variable of type multi select.
	MultiSelectValues *GoogleCloudApihubV1MultiSelectValues `json:"multiSelectValues,omitempty"`
	// MultiStringValues: Optional. The config variable value in case of config
	// variable of type multi string.
	MultiStringValues *GoogleCloudApihubV1MultiStringValues `json:"multiStringValues,omitempty"`
	// SecretValue: Optional. The config variable value in case of config variable
	// of type secret.
	SecretValue *GoogleCloudApihubV1Secret `json:"secretValue,omitempty"`
	// StringValue: Optional. The config variable value in case of config variable
	// of type string.
	StringValue string `json:"stringValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BoolValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BoolValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ConfigVariable: ConfigVariable represents a additional configuration variable present in a PluginInstance Config or AuthConfig, based on a ConfigVariableTemplate.

func (GoogleCloudApihubV1ConfigVariable) MarshalJSON ¶
func (s GoogleCloudApihubV1ConfigVariable) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ConfigVariableTemplate ¶
type GoogleCloudApihubV1ConfigVariableTemplate struct {
	// Description: Optional. Description.
	Description string `json:"description,omitempty"`
	// EnumOptions: Optional. Enum options. To be populated if `ValueType` is
	// `ENUM`.
	EnumOptions []*GoogleCloudApihubV1ConfigValueOption `json:"enumOptions,omitempty"`
	// Id: Required. ID of the config variable. Must be unique within the
	// configuration.
	Id string `json:"id,omitempty"`
	// MultiSelectOptions: Optional. Multi select options. To be populated if
	// `ValueType` is `MULTI_SELECT`.
	MultiSelectOptions []*GoogleCloudApihubV1ConfigValueOption `json:"multiSelectOptions,omitempty"`
	// Required: Optional. Flag represents that this `ConfigVariable` must be
	// provided for a PluginInstance.
	Required bool `json:"required,omitempty"`
	// ValidationRegex: Optional. Regular expression in RE2 syntax used for
	// validating the `value` of a `ConfigVariable`.
	ValidationRegex string `json:"validationRegex,omitempty"`
	// ValueType: Required. Type of the parameter: string, int, bool etc.
	//
	// Possible values:
	//   "VALUE_TYPE_UNSPECIFIED" - Value type is not specified.
	//   "STRING" - Value type is string.
	//   "INT" - Value type is integer.
	//   "BOOL" - Value type is boolean.
	//   "SECRET" - Value type is secret.
	//   "ENUM" - Value type is enum.
	//   "MULTI_SELECT" - Value type is multi select.
	//   "MULTI_STRING" - Value type is multi string.
	//   "MULTI_INT" - Value type is multi int.
	ValueType string `json:"valueType,omitempty"`
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

GoogleCloudApihubV1ConfigVariableTemplate: ConfigVariableTemplate represents a configuration variable template present in a Plugin Config.

func (GoogleCloudApihubV1ConfigVariableTemplate) MarshalJSON ¶
func (s GoogleCloudApihubV1ConfigVariableTemplate) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Curation ¶
type GoogleCloudApihubV1Curation struct {
	// CreateTime: Output only. The time at which the curation was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. The description of the curation.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the curation.
	DisplayName string `json:"displayName,omitempty"`
	// Endpoint: Required. The endpoint to be triggered for curation.
	Endpoint *GoogleCloudApihubV1Endpoint `json:"endpoint,omitempty"`
	// LastExecutionErrorCode: Output only. The error code of the last execution of
	// the curation. The error code is populated only when the last execution state
	// is failed.
	//
	// Possible values:
	//   "ERROR_CODE_UNSPECIFIED" - Default unspecified error code.
	//   "INTERNAL_ERROR" - The execution failed due to an internal error.
	//   "UNAUTHORIZED" - The curation is not authorized to trigger the endpoint
	// uri.
	LastExecutionErrorCode string `json:"lastExecutionErrorCode,omitempty"`
	// LastExecutionErrorMessage: Output only. Error message describing the
	// failure, if any, during the last execution of the curation.
	LastExecutionErrorMessage string `json:"lastExecutionErrorMessage,omitempty"`
	// LastExecutionState: Output only. The last execution state of the curation.
	//
	// Possible values:
	//   "LAST_EXECUTION_STATE_UNSPECIFIED" - Default unspecified state.
	//   "SUCCEEDED" - The last curation execution was successful.
	//   "FAILED" - The last curation execution failed.
	LastExecutionState string `json:"lastExecutionState,omitempty"`
	// Name: Identifier. The name of the curation. Format:
	// `projects/{project}/locations/{location}/curations/{curation}`
	Name string `json:"name,omitempty"`
	// PluginInstanceActions: Output only. The plugin instances and associated
	// actions that are using the curation. Note: A particular curation could be
	// used by multiple plugin instances or multiple actions in a plugin instance.
	PluginInstanceActions []*GoogleCloudApihubV1PluginInstanceActionID `json:"pluginInstanceActions,omitempty"`
	// UpdateTime: Output only. The time at which the curation was last updated.
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

GoogleCloudApihubV1Curation: A curation resource in the API Hub.

func (GoogleCloudApihubV1Curation) MarshalJSON ¶
func (s GoogleCloudApihubV1Curation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CurationConfig ¶
type GoogleCloudApihubV1CurationConfig struct {
	// CurationType: Required. The curation type for this plugin instance.
	//
	// Possible values:
	//   "CURATION_TYPE_UNSPECIFIED" - Default unspecified curation type.
	//   "DEFAULT_CURATION_FOR_API_METADATA" - Default curation for API metadata
	// will be used.
	//   "CUSTOM_CURATION_FOR_API_METADATA" - Custom curation for API metadata will
	// be used.
	CurationType string `json:"curationType,omitempty"`
	// CustomCuration: Optional. Custom curation information for this plugin
	// instance.
	CustomCuration *GoogleCloudApihubV1CustomCuration `json:"customCuration,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurationType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurationType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1CurationConfig: The curation information for this plugin instance.

func (GoogleCloudApihubV1CurationConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1CurationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1CustomCuration ¶
type GoogleCloudApihubV1CustomCuration struct {
	// Curation: Required. The unique name of the curation resource. This will be
	// the name of the curation resource in the format:
	// `projects/{project}/locations/{location}/curations/{curation}`
	Curation string `json:"curation,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Curation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Curation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1CustomCuration: Custom curation information for this plugin instance.

func (GoogleCloudApihubV1CustomCuration) MarshalJSON ¶
func (s GoogleCloudApihubV1CustomCuration) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Definition ¶
type GoogleCloudApihubV1Definition struct {
	// Attributes: Optional. The list of user defined attributes associated with
	// the definition resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// CreateTime: Output only. The time at which the definition was created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Identifier. The name of the definition. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/defini
	// tions/{definition}`
	Name string `json:"name,omitempty"`
	// Schema: Output only. The value of a schema definition.
	Schema *GoogleCloudApihubV1Schema `json:"schema,omitempty"`
	// Spec: Output only. The name of the spec from where the definition was
	// parsed. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/
	// {spec}`
	Spec string `json:"spec,omitempty"`
	// Type: Output only. The type of the definition.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Definition type unspecified.
	//   "SCHEMA" - Definition type schema.
	Type string `json:"type,omitempty"`
	// UpdateTime: Output only. The time at which the definition was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Definition: Represents a definition for example schema, request, response definitions contained in an API version. A definition is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, definition will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Also, within OpenAPI spec, only `schema` object is supported.

func (GoogleCloudApihubV1Definition) MarshalJSON ¶
func (s GoogleCloudApihubV1Definition) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Dependency ¶
type GoogleCloudApihubV1Dependency struct {
	// Attributes: Optional. The list of user defined attributes associated with
	// the dependency resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// Consumer: Required. Immutable. The entity acting as the consumer in the
	// dependency.
	Consumer *GoogleCloudApihubV1DependencyEntityReference `json:"consumer,omitempty"`
	// CreateTime: Output only. The time at which the dependency was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. Human readable description corresponding of the
	// dependency.
	Description string `json:"description,omitempty"`
	// DiscoveryMode: Output only. Discovery mode of the dependency.
	//
	// Possible values:
	//   "DISCOVERY_MODE_UNSPECIFIED" - Default value. This value is unused.
	//   "MANUAL" - Manual mode of discovery when the dependency is defined by the
	// user.
	DiscoveryMode string `json:"discoveryMode,omitempty"`
	// ErrorDetail: Output only. Error details of a dependency if the system has
	// detected it internally.
	ErrorDetail *GoogleCloudApihubV1DependencyErrorDetail `json:"errorDetail,omitempty"`
	// Name: Identifier. The name of the dependency in the API Hub. Format:
	// `projects/{project}/locations/{location}/dependencies/{dependency}`
	Name string `json:"name,omitempty"`
	// State: Output only. State of the dependency.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "PROPOSED" - Dependency will be in a proposed state when it is newly
	// identified by the API hub on its own.
	//   "VALIDATED" - Dependency will be in a validated state when it is validated
	// by the admin or manually created in the API hub.
	State string `json:"state,omitempty"`
	// Supplier: Required. Immutable. The entity acting as the supplier in the
	// dependency.
	Supplier *GoogleCloudApihubV1DependencyEntityReference `json:"supplier,omitempty"`
	// UpdateTime: Output only. The time at which the dependency was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Dependency: A dependency resource defined in the API hub describes a dependency directed from a consumer to a supplier entity. A dependency can be defined between two Operations or between an Operation and External API.

func (GoogleCloudApihubV1Dependency) MarshalJSON ¶
func (s GoogleCloudApihubV1Dependency) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DependencyEntityReference ¶
type GoogleCloudApihubV1DependencyEntityReference struct {
	// DisplayName: Output only. Display name of the entity.
	DisplayName string `json:"displayName,omitempty"`
	// ExternalApiResourceName: The resource name of an external API in the API
	// Hub. Format:
	// `projects/{project}/locations/{location}/externalApis/{external_api}`
	ExternalApiResourceName string `json:"externalApiResourceName,omitempty"`
	// OperationResourceName: The resource name of an operation in the API Hub.
	// Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operat
	// ions/{operation}`
	OperationResourceName string `json:"operationResourceName,omitempty"`
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

GoogleCloudApihubV1DependencyEntityReference: Reference to an entity participating in a dependency.

func (GoogleCloudApihubV1DependencyEntityReference) MarshalJSON ¶
func (s GoogleCloudApihubV1DependencyEntityReference) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DependencyErrorDetail ¶
type GoogleCloudApihubV1DependencyErrorDetail struct {
	// Error: Optional. Error in the dependency.
	//
	// Possible values:
	//   "ERROR_UNSPECIFIED" - Default value used for no error in the dependency.
	//   "SUPPLIER_NOT_FOUND" - Supplier entity has been deleted.
	//   "SUPPLIER_RECREATED" - Supplier entity has been recreated.
	Error string `json:"error,omitempty"`
	// ErrorTime: Optional. Timestamp at which the error was found.
	ErrorTime string `json:"errorTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Error") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Error") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1DependencyErrorDetail: Details describing error condition of a dependency.

func (GoogleCloudApihubV1DependencyErrorDetail) MarshalJSON ¶
func (s GoogleCloudApihubV1DependencyErrorDetail) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Deployment ¶
type GoogleCloudApihubV1Deployment struct {
	// ApiVersions: Output only. The API versions linked to this deployment. Note:
	// A particular deployment could be linked to multiple different API versions
	// (of same or different APIs).
	ApiVersions []string `json:"apiVersions,omitempty"`
	// Attributes: Optional. The list of user defined attributes associated with
	// the deployment resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// CreateTime: Output only. The time at which the deployment was created.
	CreateTime string `json:"createTime,omitempty"`
	// DeploymentType: Required. The type of deployment. This maps to the following
	// system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-deployment-type`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	DeploymentType *GoogleCloudApihubV1AttributeValues `json:"deploymentType,omitempty"`
	// Description: Optional. The description of the deployment.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the deployment.
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. The documentation of the deployment.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// Endpoints: Required. The endpoints at which this deployment resource is
	// listening for API requests. This could be a list of complete URIs, hostnames
	// or an IP addresses.
	Endpoints []string `json:"endpoints,omitempty"`
	// Environment: Optional. The environment mapping to this deployment. This maps
	// to the following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-environment`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	Environment *GoogleCloudApihubV1AttributeValues `json:"environment,omitempty"`
	// ManagementUrl: Optional. The uri where users can navigate to for the
	// management of the deployment. This maps to the following system defined
	// attribute:
	// `projects/{project}/locations/{location}/attributes/system-management-url`
	// The number of values for this attribute will be based on the cardinality of
	// the attribute. The same can be retrieved via GetAttribute API. The value of
	// the attribute should be a valid URL.
	ManagementUrl *GoogleCloudApihubV1AttributeValues `json:"managementUrl,omitempty"`
	// Name: Identifier. The name of the deployment. Format:
	// `projects/{project}/locations/{location}/deployments/{deployment}`
	Name string `json:"name,omitempty"`
	// ResourceUri: Required. The resource URI identifies the deployment within its
	// gateway. For Apigee gateways, its recommended to use the format:
	// organizations/{org}/environments/{env}/apis/{api}. For ex: if a proxy with
	// name `orders` is deployed in `staging` environment of `cymbal` organization,
	// the resource URI would be:
	// `organizations/cymbal/environments/staging/apis/orders`.
	ResourceUri string `json:"resourceUri,omitempty"`
	// Slo: Optional. The SLO for this deployment. This maps to the following
	// system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-slo` attribute.
	// The number of values for this attribute will be based on the cardinality of
	// the attribute. The same can be retrieved via GetAttribute API. All values
	// should be from the list of allowed values defined for the attribute.
	Slo *GoogleCloudApihubV1AttributeValues `json:"slo,omitempty"`
	// SourceEnvironment: Optional. The environment at source for the deployment.
	// For example: prod, dev, staging, etc.
	SourceEnvironment string `json:"sourceEnvironment,omitempty"`
	// SourceMetadata: Output only. The list of sources and metadata from the
	// sources of the deployment.
	SourceMetadata []*GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// SourceProject: Optional. The project to which the deployment belongs. For
	// Google Cloud gateways, this will refer to the project identifier. For others
	// like Edge/OPDK, this will refer to the org identifier.
	SourceProject string `json:"sourceProject,omitempty"`
	// SourceUri: Optional. The uri where additional source specific information
	// for this deployment can be found. This maps to the following system defined
	// attribute:
	// `projects/{project}/locations/{location}/attributes/system-source-uri` The
	// number of values for this attribute will be based on the cardinality of the
	// attribute. The same can be retrieved via GetAttribute API. The value of the
	// attribute should be a valid URI, and in case of Cloud Storage URI, it should
	// point to a Cloud Storage object, not a directory.
	SourceUri *GoogleCloudApihubV1AttributeValues `json:"sourceUri,omitempty"`
	// UpdateTime: Output only. The time at which the deployment was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiVersions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Deployment: Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.

func (GoogleCloudApihubV1Deployment) MarshalJSON ¶
func (s GoogleCloudApihubV1Deployment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DeploymentMetadata ¶
type GoogleCloudApihubV1DeploymentMetadata struct {
	// Deployment: Required. The deployment resource to be pushed to Hub's collect
	// layer. The ID of the deployment will be generated by Hub.
	Deployment *GoogleCloudApihubV1Deployment `json:"deployment,omitempty"`
	// OriginalCreateTime: Optional. Timestamp indicating when the deployment was
	// created at the source.
	OriginalCreateTime string `json:"originalCreateTime,omitempty"`
	// OriginalId: Optional. The unique identifier of the deployment in the system
	// where it was originally created.
	OriginalId string `json:"originalId,omitempty"`
	// OriginalUpdateTime: Required. Timestamp indicating when the deployment was
	// last updated at the source.
	OriginalUpdateTime string `json:"originalUpdateTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Deployment") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deployment") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1DeploymentMetadata: The metadata associated with a deployment.

func (GoogleCloudApihubV1DeploymentMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1DeploymentMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DisablePluginInstanceActionRequest ¶
type GoogleCloudApihubV1DisablePluginInstanceActionRequest struct {
	// ActionId: Required. The action id to disable.
	ActionId string `json:"actionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1DisablePluginInstanceActionRequest: The DisablePluginInstanceAction method's request.

func (GoogleCloudApihubV1DisablePluginInstanceActionRequest) MarshalJSON ¶
func (s GoogleCloudApihubV1DisablePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DisablePluginRequest ¶
type GoogleCloudApihubV1DisablePluginRequest struct {
}

GoogleCloudApihubV1DisablePluginRequest: The DisablePlugin method's request.

type GoogleCloudApihubV1DiscoveredApiObservation ¶
added in v0.245.0
type GoogleCloudApihubV1DiscoveredApiObservation struct {
	// ApiOperationCount: Optional. The number of observed API Operations.
	ApiOperationCount int64 `json:"apiOperationCount,omitempty,string"`
	// CreateTime: Output only. Create time stamp of the observation in API Hub.
	CreateTime string `json:"createTime,omitempty"`
	// Hostname: Optional. The hostname of requests processed for this Observation.
	Hostname string `json:"hostname,omitempty"`
	// KnownOperationsCount: Output only. The number of known API Operations.
	KnownOperationsCount int64 `json:"knownOperationsCount,omitempty,string"`
	// LastEventDetectedTime: Optional. Last event detected time stamp
	LastEventDetectedTime string `json:"lastEventDetectedTime,omitempty"`
	// Name: Identifier. The name of the discovered API Observation. Format:
	// `projects/{project}/locations/{location}/discoveredApiObservations/{discovere
	// d_api_observation}`
	Name string `json:"name,omitempty"`
	// Origin: Optional. For an observation pushed from a Google Cloud resource,
	// this would be the Google Cloud project id.
	Origin string `json:"origin,omitempty"`
	// ServerIps: Optional. The IP address (IPv4 or IPv6) of the origin server that
	// the request was sent to. This field can include port information. Examples:
	// "192.168.1.1", "10.0.0.1:80", "FE80::0202:B3FF:FE1E:8329".
	ServerIps []string `json:"serverIps,omitempty"`
	// SourceLocations: Optional. The location of the observation source.
	SourceLocations []string `json:"sourceLocations,omitempty"`
	// SourceMetadata: Output only. The metadata of the source from which the
	// observation was collected.
	SourceMetadata *GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// SourceTypes: Optional. The type of the source from which the observation was
	// collected.
	//
	// Possible values:
	//   "SOURCE_TYPE_UNSPECIFIED" - Source type not specified.
	//   "GCP_XLB" - Google Cloud external load balancer.
	//   "GCP_ILB" - Google Cloud internal load balancer.
	SourceTypes []string `json:"sourceTypes,omitempty"`
	// Style: Optional. Style of ApiObservation
	//
	// Possible values:
	//   "STYLE_UNSPECIFIED" - Unknown style
	//   "REST" - Style is Rest API
	//   "GRPC" - Style is Grpc API
	//   "GRAPHQL" - Style is GraphQL API
	Style string `json:"style,omitempty"`
	// UnknownOperationsCount: Output only. The number of unknown API Operations.
	UnknownOperationsCount int64 `json:"unknownOperationsCount,omitempty,string"`
	// UpdateTime: Output only. Update time stamp of the observation in API Hub.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiOperationCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiOperationCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1DiscoveredApiObservation: Respresents an API Observation observed in one of the sources.

func (GoogleCloudApihubV1DiscoveredApiObservation) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1DiscoveredApiObservation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1DiscoveredApiOperation ¶
added in v0.245.0
type GoogleCloudApihubV1DiscoveredApiOperation struct {
	// Classification: Output only. The classification of the discovered API
	// operation.
	//
	// Possible values:
	//   "CLASSIFICATION_UNSPECIFIED" - Operation is not classified as known or
	// unknown.
	//   "KNOWN" - Operation has a matched catalog operation.
	//   "UNKNOWN" - Operation does not have a matched catalog operation.
	Classification string `json:"classification,omitempty"`
	// Count: Optional. The number of occurrences of this API Operation.
	Count int64 `json:"count,omitempty,string"`
	// CreateTime: Output only. Create time stamp of the discovered API operation
	// in API Hub.
	CreateTime string `json:"createTime,omitempty"`
	// FirstSeenTime: Optional. First seen time stamp
	FirstSeenTime string `json:"firstSeenTime,omitempty"`
	// HttpOperation: Optional. An HTTP Operation.
	HttpOperation *GoogleCloudApihubV1HttpOperationDetails `json:"httpOperation,omitempty"`
	// LastSeenTime: Optional. Last seen time stamp
	LastSeenTime string `json:"lastSeenTime,omitempty"`
	// MatchResults: Output only. The list of matched results for the discovered
	// API operation. This will be populated only if the classification is known.
	// The current usecase is for a single match. Keeping it repeated to support
	// multiple matches in future.
	MatchResults []*GoogleCloudApihubV1MatchResult `json:"matchResults,omitempty"`
	// Name: Identifier. The name of the discovered API Operation. Format:
	// `projects/{project}/locations/{location}/discoveredApiObservations/{discovere
	// d_api_observation}/discoveredApiOperations/{discovered_api_operation}`
	Name string `json:"name,omitempty"`
	// SourceMetadata: Output only. The metadata of the source from which the api
	// operation was collected.
	SourceMetadata *GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// UpdateTime: Output only. Update time stamp of the discovered API operation
	// in API Hub.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Classification") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Classification") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1DiscoveredApiOperation: DiscoveredApiOperation represents an API Operation observed in one of the sources.

func (GoogleCloudApihubV1DiscoveredApiOperation) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1DiscoveredApiOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Documentation ¶
type GoogleCloudApihubV1Documentation struct {
	// ExternalUri: Optional. The uri of the externally hosted documentation.
	ExternalUri string `json:"externalUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalUri") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Documentation: Documentation details.

func (GoogleCloudApihubV1Documentation) MarshalJSON ¶
func (s GoogleCloudApihubV1Documentation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnablePluginInstanceActionRequest ¶
type GoogleCloudApihubV1EnablePluginInstanceActionRequest struct {
	// ActionId: Required. The action id to enable.
	ActionId string `json:"actionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1EnablePluginInstanceActionRequest: The EnablePluginInstanceAction method's request.

func (GoogleCloudApihubV1EnablePluginInstanceActionRequest) MarshalJSON ¶
func (s GoogleCloudApihubV1EnablePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnablePluginRequest ¶
type GoogleCloudApihubV1EnablePluginRequest struct {
}

GoogleCloudApihubV1EnablePluginRequest: The EnablePlugin method's request.

type GoogleCloudApihubV1Endpoint ¶
type GoogleCloudApihubV1Endpoint struct {
	// ApplicationIntegrationEndpointDetails: Required. The details of the
	// Application Integration endpoint to be triggered for curation.
	ApplicationIntegrationEndpointDetails *GoogleCloudApihubV1ApplicationIntegrationEndpointDetails `json:"applicationIntegrationEndpointDetails,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ApplicationIntegrationEndpointDetails") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ApplicationIntegrationEndpointDetails") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Endpoint: The endpoint to be triggered for curation. The endpoint will be invoked with a request payload containing ApiMetadata. Response should contain curated data in the form of ApiMetadata.

func (GoogleCloudApihubV1Endpoint) MarshalJSON ¶
func (s GoogleCloudApihubV1Endpoint) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnumAttributeValues ¶
type GoogleCloudApihubV1EnumAttributeValues struct {
	// Values: Required. The attribute values in case attribute data type is enum.
	Values []*GoogleCloudApihubV1AllowedValue `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1EnumAttributeValues: The attribute values of data type enum.

func (GoogleCloudApihubV1EnumAttributeValues) MarshalJSON ¶
func (s GoogleCloudApihubV1EnumAttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1EnvironmentFilter ¶
added in v0.257.0
type GoogleCloudApihubV1EnvironmentFilter struct {
	// AllEnvironments: Optional. Indicates if this filter should match all
	// environments or only a subset of environments. If set to true, all
	// environments are matched.
	AllEnvironments bool `json:"allEnvironments,omitempty"`
	// Environments: Optional. If provided, only environments in this list are
	// matched. This field is ignored if `all_environments` is true.
	Environments []string `json:"environments,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllEnvironments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllEnvironments") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1EnvironmentFilter: Filter for environments.

func (GoogleCloudApihubV1EnvironmentFilter) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1EnvironmentFilter) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExecutePluginInstanceActionRequest ¶
type GoogleCloudApihubV1ExecutePluginInstanceActionRequest struct {
	// ActionExecutionDetail: Required. The execution details for the action to
	// execute.
	ActionExecutionDetail *GoogleCloudApihubV1ActionExecutionDetail `json:"actionExecutionDetail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionExecutionDetail") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionExecutionDetail") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ExecutePluginInstanceActionRequest: The ExecutePluginInstanceAction method's request.

func (GoogleCloudApihubV1ExecutePluginInstanceActionRequest) MarshalJSON ¶
func (s GoogleCloudApihubV1ExecutePluginInstanceActionRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExecutionStatus ¶
type GoogleCloudApihubV1ExecutionStatus struct {
	// CurrentExecutionState: Output only. The current state of the execution.
	//
	// Possible values:
	//   "CURRENT_EXECUTION_STATE_UNSPECIFIED" - Default unspecified execution
	// state.
	//   "RUNNING" - The plugin instance is executing.
	//   "NOT_RUNNING" - The plugin instance is not running an execution.
	CurrentExecutionState string `json:"currentExecutionState,omitempty"`
	// LastExecution: Output only. The last execution of the plugin instance.
	LastExecution *GoogleCloudApihubV1LastExecution `json:"lastExecution,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentExecutionState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentExecutionState") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ExecutionStatus: The execution status for the plugin instance.

func (GoogleCloudApihubV1ExecutionStatus) MarshalJSON ¶
func (s GoogleCloudApihubV1ExecutionStatus) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ExternalApi ¶
type GoogleCloudApihubV1ExternalApi struct {
	// Attributes: Optional. The list of user defined attributes associated with
	// the Version resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// CreateTime: Output only. Creation timestamp.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. Description of the external API. Max length is 2000
	// characters (Unicode Code Points).
	Description string `json:"description,omitempty"`
	// DisplayName: Required. Display name of the external API. Max length is 63
	// characters (Unicode Code Points).
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. Documentation of the external API.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// Endpoints: Optional. List of endpoints on which this API is accessible.
	Endpoints []string `json:"endpoints,omitempty"`
	// Name: Identifier. Format:
	// `projects/{project}/locations/{location}/externalApi/{externalApi}`.
	Name string `json:"name,omitempty"`
	// Paths: Optional. List of paths served by this API.
	Paths []string `json:"paths,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ExternalApi: An external API represents an API being provided by external sources. This can be used to model third-party APIs and can be used to define dependencies.

func (GoogleCloudApihubV1ExternalApi) MarshalJSON ¶
func (s GoogleCloudApihubV1ExternalApi) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FetchAdditionalSpecContentResponse ¶
added in v0.258.0
type GoogleCloudApihubV1FetchAdditionalSpecContentResponse struct {
	// AdditionalSpecContent: The additional spec content.
	AdditionalSpecContent *GoogleCloudApihubV1AdditionalSpecContent `json:"additionalSpecContent,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdditionalSpecContent") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalSpecContent") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1FetchAdditionalSpecContentResponse: The FetchAdditionalSpecContent method's response.

func (GoogleCloudApihubV1FetchAdditionalSpecContentResponse) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1FetchAdditionalSpecContentResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FlattenedApiVersionDeploymentView ¶
added in v0.258.0
type GoogleCloudApihubV1FlattenedApiVersionDeploymentView struct {
	// Api: The API.
	Api *GoogleCloudApihubV1Api `json:"api,omitempty"`
	// Deployment: The deployment.
	Deployment *GoogleCloudApihubV1Deployment `json:"deployment,omitempty"`
	// Version: The version.
	Version *GoogleCloudApihubV1Version `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Api") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Api") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1FlattenedApiVersionDeploymentView: A flattened view of an API, its version and one of the linked deployments.

func (GoogleCloudApihubV1FlattenedApiVersionDeploymentView) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1FlattenedApiVersionDeploymentView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView ¶
added in v0.258.0
type GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView struct {
	// Api: The API.
	Api *GoogleCloudApihubV1Api `json:"api,omitempty"`
	// ApiOperation: The API operation.
	ApiOperation *GoogleCloudApihubV1ApiOperation `json:"apiOperation,omitempty"`
	// Deployment: The deployment.
	Deployment *GoogleCloudApihubV1Deployment `json:"deployment,omitempty"`
	// Version: The version.
	Version *GoogleCloudApihubV1Version `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Api") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Api") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView: A flattened view of an API, its version, one of its operations and one of the linked deployments. If there are no deployments linked to the operation then the result will be empty.

func (GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GatewayPluginAddonConfig ¶
added in v0.257.0
type GoogleCloudApihubV1GatewayPluginAddonConfig struct {
	// GatewayPluginConfigs: Required. The list of gateway plugin configs for which
	// the addon is enabled. Each gateway plugin config should have a unique plugin
	// instance.
	GatewayPluginConfigs []*GoogleCloudApihubV1GatewayPluginConfig `json:"gatewayPluginConfigs,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GatewayPluginConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GatewayPluginConfigs") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1GatewayPluginAddonConfig: Configuration for gateway plugin addons. This is used to specify the list of gateway plugin configs for which the addon is enabled.

func (GoogleCloudApihubV1GatewayPluginAddonConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1GatewayPluginAddonConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GatewayPluginConfig ¶
added in v0.257.0
type GoogleCloudApihubV1GatewayPluginConfig struct {
	// ApigeeEdgeConfig: Configuration for Apigee Edge gateways.
	ApigeeEdgeConfig *GoogleCloudApihubV1ApigeeEdgeConfig `json:"apigeeEdgeConfig,omitempty"`
	// ApigeeOpdkConfig: Configuration for Apigee OPDK gateways.
	ApigeeOpdkConfig *GoogleCloudApihubV1ApigeeOPDKConfig `json:"apigeeOpdkConfig,omitempty"`
	// ApigeeXHybridConfig: Configuration for Apigee X and Apigee Hybrid gateways.
	ApigeeXHybridConfig *GoogleCloudApihubV1ApigeeXHybridConfig `json:"apigeeXHybridConfig,omitempty"`
	// PluginInstance: Required. The name of the gateway plugin instance for which
	// the config is to be specified. Format:
	// projects/{project}/locations/{location}/plugins/{plugin}/pluginInstances/{plu
	// gin_instance}
	PluginInstance string `json:"pluginInstance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApigeeEdgeConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApigeeEdgeConfig") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1GatewayPluginConfig: Configuration for a gateway plugin. This is used to specify configs for different gateways.

func (GoogleCloudApihubV1GatewayPluginConfig) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1GatewayPluginConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1GoogleServiceAccountConfig ¶
type GoogleCloudApihubV1GoogleServiceAccountConfig struct {
	// ServiceAccount: Required. The service account to be used for authenticating
	// request. The `iam.serviceAccounts.getAccessToken` permission should be
	// granted on this service account to the impersonator service account.
	ServiceAccount string `json:"serviceAccount,omitempty"`
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

GoogleCloudApihubV1GoogleServiceAccountConfig: Config for Google service account authentication.

func (GoogleCloudApihubV1GoogleServiceAccountConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1GoogleServiceAccountConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Header ¶
added in v0.245.0
type GoogleCloudApihubV1Header struct {
	// Count: The number of occurrences of this Header across transactions.
	Count int64 `json:"count,omitempty,string"`
	// DataType: Data type of header
	//
	// Possible values:
	//   "DATA_TYPE_UNSPECIFIED" - Unspecified data type
	//   "BOOL" - Boolean data type
	//   "INTEGER" - Integer data type
	//   "FLOAT" - Float data type
	//   "STRING" - String data type
	//   "UUID" - UUID data type
	DataType string `json:"dataType,omitempty"`
	// Name: Header name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Count") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Count") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Header: An aggregation of HTTP header occurrences.

func (GoogleCloudApihubV1Header) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1Header) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HostProjectRegistration ¶
type GoogleCloudApihubV1HostProjectRegistration struct {
	// CreateTime: Output only. The time at which the host project registration was
	// created.
	CreateTime string `json:"createTime,omitempty"`
	// GcpProject: Required. Immutable. Google cloud project name in the format:
	// "projects/abc" or "projects/123". As input, project name with either project
	// id or number are accepted. As output, this field will contain project
	// number.
	GcpProject string `json:"gcpProject,omitempty"`
	// Name: Identifier. The name of the host project registration. Format:
	// "projects/{project}/locations/{location}/hostProjectRegistrations/{host_proje
	// ct_registration}".
	Name string `json:"name,omitempty"`

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

GoogleCloudApihubV1HostProjectRegistration: Host project registration refers to the registration of a Google cloud project with Api Hub as a host project. This is the project where Api Hub is provisioned. It acts as the consumer project for the Api Hub instance provisioned. Multiple runtime projects can be attached to the host project and these attachments define the scope of Api Hub.

func (GoogleCloudApihubV1HostProjectRegistration) MarshalJSON ¶
func (s GoogleCloudApihubV1HostProjectRegistration) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HostingService ¶
type GoogleCloudApihubV1HostingService struct {
	// ServiceUri: Optional. The URI of the service implemented by the plugin
	// developer, used to invoke the plugin's functionality. This information is
	// only required for user defined plugins.
	ServiceUri string `json:"serviceUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ServiceUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServiceUri") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1HostingService: The information related to the service implemented by the plugin developer, used to invoke the plugin's functionality.

func (GoogleCloudApihubV1HostingService) MarshalJSON ¶
func (s GoogleCloudApihubV1HostingService) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpOperation ¶
type GoogleCloudApihubV1HttpOperation struct {
	// Method: Optional. Operation method Note: Even though this field is optional,
	// it is required for CreateApiOperation API and we will fail the request if
	// not provided.
	//
	// Possible values:
	//   "METHOD_UNSPECIFIED" - Method unspecified.
	//   "GET" - Get Operation type.
	//   "PUT" - Put Operation type.
	//   "POST" - Post Operation type.
	//   "DELETE" - Delete Operation type.
	//   "OPTIONS" - Options Operation type.
	//   "HEAD" - Head Operation type.
	//   "PATCH" - Patch Operation type.
	//   "TRACE" - Trace Operation type.
	Method string `json:"method,omitempty"`
	// Path: Optional. The path details for the Operation. Note: Even though this
	// field is optional, it is required for CreateApiOperation API and we will
	// fail the request if not provided.
	Path *GoogleCloudApihubV1Path `json:"path,omitempty"`
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

GoogleCloudApihubV1HttpOperation: The HTTP Operation.

func (GoogleCloudApihubV1HttpOperation) MarshalJSON ¶
func (s GoogleCloudApihubV1HttpOperation) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpOperationDetails ¶
added in v0.245.0
type GoogleCloudApihubV1HttpOperationDetails struct {
	// HttpOperation: Required. An HTTP Operation.
	HttpOperation *GoogleCloudApihubV1HttpOperation `json:"httpOperation,omitempty"`
	// PathParams: Optional. Path params of HttpOperation
	PathParams []*GoogleCloudApihubV1PathParam `json:"pathParams,omitempty"`
	// QueryParams: Optional. Query params of HttpOperation
	QueryParams map[string]GoogleCloudApihubV1QueryParam `json:"queryParams,omitempty"`
	// Request: Optional. Request metadata.
	Request *GoogleCloudApihubV1HttpRequest `json:"request,omitempty"`
	// Response: Optional. Response metadata.
	Response *GoogleCloudApihubV1HttpResponse `json:"response,omitempty"`
	// ForceSendFields is a list of field names (e.g. "HttpOperation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HttpOperation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1HttpOperationDetails: An HTTP-based API Operation, sometimes called a "REST" Operation.

func (GoogleCloudApihubV1HttpOperationDetails) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1HttpOperationDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpRequest ¶
added in v0.245.0
type GoogleCloudApihubV1HttpRequest struct {
	// Headers: Optional. Unordered map from header name to header metadata
	Headers map[string]GoogleCloudApihubV1Header `json:"headers,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Headers") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Headers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1HttpRequest: An aggregation of HTTP requests.

func (GoogleCloudApihubV1HttpRequest) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1HttpRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1HttpResponse ¶
added in v0.245.0
type GoogleCloudApihubV1HttpResponse struct {
	// Headers: Optional. Unordered map from header name to header metadata
	Headers map[string]GoogleCloudApihubV1Header `json:"headers,omitempty"`
	// ResponseCodes: Optional. Map of status code to observed count
	ResponseCodes map[string]string `json:"responseCodes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Headers") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Headers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1HttpResponse: An aggregation of HTTP responses.

func (GoogleCloudApihubV1HttpResponse) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1HttpResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Issue ¶
type GoogleCloudApihubV1Issue struct {
	// Code: Required. Rule code unique to each rule defined in linter.
	Code string `json:"code,omitempty"`
	// Message: Required. Human-readable message describing the issue found by the
	// linter.
	Message string `json:"message,omitempty"`
	// Path: Required. An array of strings indicating the location in the analyzed
	// document where the rule was triggered.
	Path []string `json:"path,omitempty"`
	// Range: Required. Object describing where in the file the issue was found.
	Range *GoogleCloudApihubV1Range `json:"range,omitempty"`
	// Severity: Required. Severity level of the rule violation.
	//
	// Possible values:
	//   "SEVERITY_UNSPECIFIED" - Severity unspecified.
	//   "SEVERITY_ERROR" - Severity error.
	//   "SEVERITY_WARNING" - Severity warning.
	//   "SEVERITY_INFO" - Severity info.
	//   "SEVERITY_HINT" - Severity hint.
	Severity string `json:"severity,omitempty"`
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

GoogleCloudApihubV1Issue: Issue contains the details of a single issue found by the linter.

func (GoogleCloudApihubV1Issue) MarshalJSON ¶
func (s GoogleCloudApihubV1Issue) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LastExecution ¶
type GoogleCloudApihubV1LastExecution struct {
	// EndTime: Output only. The last execution end time of the plugin instance.
	EndTime string `json:"endTime,omitempty"`
	// ErrorMessage: Output only. Error message describing the failure, if any,
	// during the last execution.
	ErrorMessage string `json:"errorMessage,omitempty"`
	// Result: Output only. The result of the last execution of the plugin
	// instance.
	//
	// Possible values:
	//   "RESULT_UNSPECIFIED" - Default unspecified execution result.
	//   "SUCCEEDED" - The plugin instance executed successfully.
	//   "FAILED" - The plugin instance execution failed.
	Result string `json:"result,omitempty"`
	// ResultMetadata: Output only. The result metadata of the last execution of
	// the plugin instance. This will be a string representation of a JSON object
	// and will be available on successful execution.
	ResultMetadata string `json:"resultMetadata,omitempty"`
	// StartTime: Output only. The last execution start time of the plugin
	// instance.
	StartTime string `json:"startTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndTime") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1LastExecution: The result of the last execution of the plugin instance.

func (GoogleCloudApihubV1LastExecution) MarshalJSON ¶
func (s GoogleCloudApihubV1LastExecution) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LintResponse ¶
type GoogleCloudApihubV1LintResponse struct {
	// CreateTime: Required. Timestamp when the linting response was generated.
	CreateTime string `json:"createTime,omitempty"`
	// Issues: Optional. Array of issues found in the analyzed document.
	Issues []*GoogleCloudApihubV1Issue `json:"issues,omitempty"`
	// Linter: Required. Name of the linter used.
	//
	// Possible values:
	//   "LINTER_UNSPECIFIED" - Linter type unspecified.
	//   "SPECTRAL" - Linter type spectral.
	//   "OTHER" - Linter type other.
	Linter string `json:"linter,omitempty"`
	// Source: Required. Name of the linting application.
	Source string `json:"source,omitempty"`
	// State: Required. Lint state represents success or failure for linting.
	//
	// Possible values:
	//   "LINT_STATE_UNSPECIFIED" - Lint state unspecified.
	//   "LINT_STATE_SUCCESS" - Linting was completed successfully.
	//   "LINT_STATE_ERROR" - Linting encountered errors.
	State string `json:"state,omitempty"`
	// Summary: Optional. Summary of all issue types and counts for each severity
	// level.
	Summary []*GoogleCloudApihubV1SummaryEntry `json:"summary,omitempty"`
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

GoogleCloudApihubV1LintResponse: LintResponse contains the response from the linter.

func (GoogleCloudApihubV1LintResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1LintResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LintSpecRequest ¶
type GoogleCloudApihubV1LintSpecRequest struct {
}

GoogleCloudApihubV1LintSpecRequest: The LintSpec method's request.

type GoogleCloudApihubV1ListAddonsResponse ¶
added in v0.257.0
type GoogleCloudApihubV1ListAddonsResponse struct {
	// Addons: The list of addons.
	Addons []*GoogleCloudApihubV1Addon `json:"addons,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Addons") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Addons") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListAddonsResponse: The ListAddons method's response.

func (GoogleCloudApihubV1ListAddonsResponse) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1ListAddonsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListApiOperationsResponse ¶
type GoogleCloudApihubV1ListApiOperationsResponse struct {
	// ApiOperations: The operations corresponding to an API version.
	ApiOperations []*GoogleCloudApihubV1ApiOperation `json:"apiOperations,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiOperations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiOperations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListApiOperationsResponse: The ListApiOperations method's response.

func (GoogleCloudApihubV1ListApiOperationsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListApiOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListApisResponse ¶
type GoogleCloudApihubV1ListApisResponse struct {
	// Apis: The API resources present in the API hub.
	Apis []*GoogleCloudApihubV1Api `json:"apis,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Apis") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Apis") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListApisResponse: The ListApis method's response.

func (GoogleCloudApihubV1ListApisResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListApisResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListAttributesResponse ¶
type GoogleCloudApihubV1ListAttributesResponse struct {
	// Attributes: The list of all attributes.
	Attributes []*GoogleCloudApihubV1Attribute `json:"attributes,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListAttributesResponse: The ListAttributes method's response.

func (GoogleCloudApihubV1ListAttributesResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListAttributesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListCurationsResponse ¶
type GoogleCloudApihubV1ListCurationsResponse struct {
	// Curations: The curation resources present in the API hub.
	Curations []*GoogleCloudApihubV1Curation `json:"curations,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Curations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Curations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListCurationsResponse: The ListCurations method's response.

func (GoogleCloudApihubV1ListCurationsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListCurationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDependenciesResponse ¶
type GoogleCloudApihubV1ListDependenciesResponse struct {
	// Dependencies: The dependency resources present in the API hub.
	Dependencies []*GoogleCloudApihubV1Dependency `json:"dependencies,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Dependencies") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Dependencies") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListDependenciesResponse: The ListDependencies method's response.

func (GoogleCloudApihubV1ListDependenciesResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListDependenciesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDeploymentsResponse ¶
type GoogleCloudApihubV1ListDeploymentsResponse struct {
	// Deployments: The deployment resources present in the API hub.
	Deployments []*GoogleCloudApihubV1Deployment `json:"deployments,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Deployments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deployments") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListDeploymentsResponse: The ListDeployments method's response.

func (GoogleCloudApihubV1ListDeploymentsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListDeploymentsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDiscoveredApiObservationsResponse ¶
added in v0.245.0
type GoogleCloudApihubV1ListDiscoveredApiObservationsResponse struct {
	// DiscoveredApiObservations: The DiscoveredApiObservation from the specified
	// project and location.
	DiscoveredApiObservations []*GoogleCloudApihubV1DiscoveredApiObservation `json:"discoveredApiObservations,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredApiObservations")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredApiObservations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListDiscoveredApiObservationsResponse: Message for response to listing DiscoveredApiObservations

func (GoogleCloudApihubV1ListDiscoveredApiObservationsResponse) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1ListDiscoveredApiObservationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListDiscoveredApiOperationsResponse ¶
added in v0.245.0
type GoogleCloudApihubV1ListDiscoveredApiOperationsResponse struct {
	// DiscoveredApiOperations: The DiscoveredApiOperations from the specified
	// project, location and DiscoveredApiObservation.
	DiscoveredApiOperations []*GoogleCloudApihubV1DiscoveredApiOperation `json:"discoveredApiOperations,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscoveredApiOperations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscoveredApiOperations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListDiscoveredApiOperationsResponse: Message for response to listing DiscoveredApiOperations

func (GoogleCloudApihubV1ListDiscoveredApiOperationsResponse) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1ListDiscoveredApiOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListExternalApisResponse ¶
type GoogleCloudApihubV1ListExternalApisResponse struct {
	// ExternalApis: The External API resources present in the API hub.
	ExternalApis []*GoogleCloudApihubV1ExternalApi `json:"externalApis,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExternalApis") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalApis") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListExternalApisResponse: The ListExternalApis method's response.

func (GoogleCloudApihubV1ListExternalApisResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListExternalApisResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListHostProjectRegistrationsResponse ¶
type GoogleCloudApihubV1ListHostProjectRegistrationsResponse struct {
	// HostProjectRegistrations: The list of host project registrations.
	HostProjectRegistrations []*GoogleCloudApihubV1HostProjectRegistration `json:"hostProjectRegistrations,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "HostProjectRegistrations")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HostProjectRegistrations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ListHostProjectRegistrationsResponse: The ListHostProjectRegistrations method's response.

func (GoogleCloudApihubV1ListHostProjectRegistrationsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListHostProjectRegistrationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListPluginInstancesResponse ¶
type GoogleCloudApihubV1ListPluginInstancesResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// PluginInstances: The plugin instances from the specified parent resource.
	PluginInstances []*GoogleCloudApihubV1PluginInstance `json:"pluginInstances,omitempty"`

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

GoogleCloudApihubV1ListPluginInstancesResponse: The ListPluginInstances method's response.

func (GoogleCloudApihubV1ListPluginInstancesResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListPluginInstancesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListPluginsResponse ¶
type GoogleCloudApihubV1ListPluginsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Plugins: The plugins from the specified parent resource.
	Plugins []*GoogleCloudApihubV1Plugin `json:"plugins,omitempty"`

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

GoogleCloudApihubV1ListPluginsResponse: The ListPlugins method's response.

func (GoogleCloudApihubV1ListPluginsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListPluginsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse ¶
type GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// RuntimeProjectAttachments: List of runtime project attachments.
	RuntimeProjectAttachments []*GoogleCloudApihubV1RuntimeProjectAttachment `json:"runtimeProjectAttachments,omitempty"`

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

GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse: The ListRuntimeProjectAttachments method's response.

func (GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListSpecsResponse ¶
type GoogleCloudApihubV1ListSpecsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Specs: The specs corresponding to an API Version.
	Specs []*GoogleCloudApihubV1Spec `json:"specs,omitempty"`

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

GoogleCloudApihubV1ListSpecsResponse: The ListSpecs method's response.

func (GoogleCloudApihubV1ListSpecsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListSpecsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ListVersionsResponse ¶
type GoogleCloudApihubV1ListVersionsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Versions: The versions corresponding to an API.
	Versions []*GoogleCloudApihubV1Version `json:"versions,omitempty"`

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

GoogleCloudApihubV1ListVersionsResponse: The ListVersions method's response.

func (GoogleCloudApihubV1ListVersionsResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1ListVersionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LookupApiHubInstanceResponse ¶
type GoogleCloudApihubV1LookupApiHubInstanceResponse struct {
	// ApiHubInstance: API Hub instance for a project if it exists, empty
	// otherwise.
	ApiHubInstance *GoogleCloudApihubV1ApiHubInstance `json:"apiHubInstance,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiHubInstance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiHubInstance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1LookupApiHubInstanceResponse: The LookupApiHubInstance method's response.`

func (GoogleCloudApihubV1LookupApiHubInstanceResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1LookupApiHubInstanceResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse ¶
type GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse struct {
	// RuntimeProjectAttachment: Runtime project attachment for a project if
	// exists, empty otherwise.
	RuntimeProjectAttachment *GoogleCloudApihubV1RuntimeProjectAttachment `json:"runtimeProjectAttachment,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "RuntimeProjectAttachment")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RuntimeProjectAttachment") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse: The ListRuntimeProjectAttachments method's response.

func (GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManageAddonConfigRequest ¶
added in v0.257.0
type GoogleCloudApihubV1ManageAddonConfigRequest struct {
	// Config: Required. The config of the addon to be managed. This config will
	// replace the config present in the addon. The type of the config should match
	// the config type already present in the addon.
	Config *GoogleCloudApihubV1AddonConfig `json:"config,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Config") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Config") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ManageAddonConfigRequest: The ManageAddonConfig method's request.

func (GoogleCloudApihubV1ManageAddonConfigRequest) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1ManageAddonConfigRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest ¶
added in v0.250.0
type GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest struct {
	// Action: Required. Action to be performed.
	//
	// Possible values:
	//   "ACTION_UNSPECIFIED" - Default unspecified action.
	//   "UPLOAD" - Upload or upsert data.
	//   "DELETE" - Delete data.
	Action string `json:"action,omitempty"`
	// Data: Required. Data to be managed.
	Data string `json:"data,omitempty"`
	// DataType: Required. Type of data to be managed.
	//
	// Possible values:
	//   "DATA_TYPE_UNSPECIFIED" - Default unspecified type.
	//   "PROXY_DEPLOYMENT_MANIFEST" - Proxy deployment manifest.
	//   "ENVIRONMENT_MANIFEST" - Environment manifest.
	//   "PROXY_BUNDLE" - Proxy bundle.
	//   "SHARED_FLOW_BUNDLE" - Shared flow bundle.
	DataType string `json:"dataType,omitempty"`
	// RelativePath: Required. Relative path of data being managed for a given
	// plugin instance.
	RelativePath string `json:"relativePath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Action") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Action") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest: The ManagePluginInstanceSourceData method's request.

func (GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest) MarshalJSON ¶
added in v0.250.0
func (s GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse ¶
added in v0.250.0
type GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse: The ManagePluginInstanceSourceData method's response.

type GoogleCloudApihubV1MatchResult ¶
added in v0.245.0
type GoogleCloudApihubV1MatchResult struct {
	// Name: Output only. The name of the matched API Operation. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operat
	// ions/{operation}`
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

GoogleCloudApihubV1MatchResult: MatchResult represents the result of matching a discovered API operation with a catalog API operation.

func (GoogleCloudApihubV1MatchResult) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1MatchResult) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1McpTool ¶
added in v0.258.0
type GoogleCloudApihubV1McpTool struct {
	// Annotations: Optional. Optional annotations for the tool.
	Annotations *GoogleCloudApihubV1ToolAnnotations `json:"annotations,omitempty"`
	// Description: Optional. Description of what the tool does.
	Description string `json:"description,omitempty"`
	// InputSchema: Optional. Input schema for the operation. This can be parsed
	// only from MCP schema type.
	InputSchema *GoogleCloudApihubV1OperationSchema `json:"inputSchema,omitempty"`
	// Name: Required. The name of the tool, unique within its parent scope
	// (version).
	Name string `json:"name,omitempty"`
	// OutputSchema: Optional. Output schema for the operation. This can be parsed
	// only from MCP schema type.
	OutputSchema *GoogleCloudApihubV1OperationSchema `json:"outputSchema,omitempty"`
	// Title: Optional. Optional title for the tool.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Annotations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Annotations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1McpTool: Details describing an MCP Tool.

func (GoogleCloudApihubV1McpTool) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1McpTool) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiIntValues ¶
type GoogleCloudApihubV1MultiIntValues struct {
	// Values: Optional. The config variable value of data type multi int.
	Values []int64 `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1MultiIntValues: The config variable value of data type multi int.

func (GoogleCloudApihubV1MultiIntValues) MarshalJSON ¶
func (s GoogleCloudApihubV1MultiIntValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiSelectValues ¶
type GoogleCloudApihubV1MultiSelectValues struct {
	// Values: Optional. The config variable value of data type multi select.
	Values []*GoogleCloudApihubV1ConfigValueOption `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1MultiSelectValues: The config variable value of data type multi select.

func (GoogleCloudApihubV1MultiSelectValues) MarshalJSON ¶
func (s GoogleCloudApihubV1MultiSelectValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1MultiStringValues ¶
type GoogleCloudApihubV1MultiStringValues struct {
	// Values: Optional. The config variable value of data type multi string.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1MultiStringValues: The config variable value of data type multi string.

func (GoogleCloudApihubV1MultiStringValues) MarshalJSON ¶
func (s GoogleCloudApihubV1MultiStringValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Oauth2ClientCredentialsConfig ¶
type GoogleCloudApihubV1Oauth2ClientCredentialsConfig struct {
	// ClientId: Required. The client identifier.
	ClientId string `json:"clientId,omitempty"`
	// ClientSecret: Required. Secret version reference containing the client
	// secret. The `secretmanager.versions.access` permission should be granted to
	// the service account accessing the secret.
	ClientSecret *GoogleCloudApihubV1Secret `json:"clientSecret,omitempty"`
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

GoogleCloudApihubV1Oauth2ClientCredentialsConfig: Parameters to support Oauth 2.0 client credentials grant authentication. See https://tools.ietf.org/html/rfc6749#section-1.3.4 for more details.

func (GoogleCloudApihubV1Oauth2ClientCredentialsConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1Oauth2ClientCredentialsConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OpenApiSpecDetails ¶
type GoogleCloudApihubV1OpenApiSpecDetails struct {
	// Format: Output only. The format of the spec.
	//
	// Possible values:
	//   "FORMAT_UNSPECIFIED" - SpecFile type unspecified.
	//   "OPEN_API_SPEC_2_0" - OpenAPI Spec v2.0.
	//   "OPEN_API_SPEC_3_0" - OpenAPI Spec v3.0.
	//   "OPEN_API_SPEC_3_1" - OpenAPI Spec v3.1.
	Format string `json:"format,omitempty"`
	// Owner: Output only. Owner details for the spec. This maps to `info.contact`
	// in OpenAPI spec.
	Owner *GoogleCloudApihubV1Owner `json:"owner,omitempty"`
	// Version: Output only. The version in the spec. This maps to `info.version`
	// in OpenAPI spec.
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Format") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Format") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1OpenApiSpecDetails: OpenApiSpecDetails contains the details parsed from an OpenAPI spec in addition to the fields mentioned in SpecDetails.

func (GoogleCloudApihubV1OpenApiSpecDetails) MarshalJSON ¶
func (s GoogleCloudApihubV1OpenApiSpecDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationDetails ¶
type GoogleCloudApihubV1OperationDetails struct {
	// Deprecated -- Optional. For OpenAPI spec, this will be set if
	// `operation.deprecated`is marked as `true` in the spec.
	Deprecated bool `json:"deprecated,omitempty"`
	// Description: Optional. Description of the operation behavior. For OpenAPI
	// spec, this will map to `operation.description` in the spec, in case
	// description is empty, `operation.summary` will be used.
	Description string `json:"description,omitempty"`
	// Documentation: Optional. Additional external documentation for this
	// operation. For OpenAPI spec, this will map to `operation.documentation` in
	// the spec.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// HttpOperation: The HTTP Operation.
	HttpOperation *GoogleCloudApihubV1HttpOperation `json:"httpOperation,omitempty"`
	// McpTool: The MCP Tool Operation.
	McpTool *GoogleCloudApihubV1McpTool `json:"mcpTool,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Deprecated") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deprecated") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1OperationDetails: The operation details parsed from the spec.

func (GoogleCloudApihubV1OperationDetails) MarshalJSON ¶
func (s GoogleCloudApihubV1OperationDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationMetadata ¶
type GoogleCloudApihubV1OperationMetadata struct {
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

GoogleCloudApihubV1OperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudApihubV1OperationMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1OperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1OperationSchema ¶
added in v0.258.0
type GoogleCloudApihubV1OperationSchema struct {
	// JsonSchema: The JSON schema. Only valid JSON is accepted but semantic
	// validation of schema is not supported right now.
	JsonSchema googleapi.RawMessage `json:"jsonSchema,omitempty"`
	// ForceSendFields is a list of field names (e.g. "JsonSchema") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "JsonSchema") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1OperationSchema: The operation schema needed for an operation.

func (GoogleCloudApihubV1OperationSchema) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1OperationSchema) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Owner ¶
type GoogleCloudApihubV1Owner struct {
	// DisplayName: Optional. The name of the owner.
	DisplayName string `json:"displayName,omitempty"`
	// Email: Required. The email of the owner.
	Email string `json:"email,omitempty"`
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

GoogleCloudApihubV1Owner: Owner details.

func (GoogleCloudApihubV1Owner) MarshalJSON ¶
func (s GoogleCloudApihubV1Owner) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Path ¶
type GoogleCloudApihubV1Path struct {
	// Description: Optional. A short description for the path applicable to all
	// operations.
	Description string `json:"description,omitempty"`
	// Path: Optional. Complete path relative to server endpoint. Note: Even though
	// this field is optional, it is required for CreateApiOperation API and we
	// will fail the request if not provided.
	Path string `json:"path,omitempty"`
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

GoogleCloudApihubV1Path: The path details derived from the spec.

func (GoogleCloudApihubV1Path) MarshalJSON ¶
func (s GoogleCloudApihubV1Path) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PathParam ¶
added in v0.245.0
type GoogleCloudApihubV1PathParam struct {
	// DataType: Optional. Data type of path param
	//
	// Possible values:
	//   "DATA_TYPE_UNSPECIFIED" - Unspecified data type
	//   "BOOL" - Boolean data type
	//   "INTEGER" - Integer data type
	//   "FLOAT" - Float data type
	//   "STRING" - String data type
	//   "UUID" - UUID data type
	DataType string `json:"dataType,omitempty"`
	// Position: Optional. Segment location in the path, 1-indexed
	Position int64 `json:"position,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DataType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1PathParam: HTTP Path parameter.

func (GoogleCloudApihubV1PathParam) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1PathParam) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Plugin ¶
type GoogleCloudApihubV1Plugin struct {
	// ActionsConfig: Optional. The configuration of actions supported by the
	// plugin. **REQUIRED**: This field must be provided when creating or updating
	// a Plugin. The server will reject requests if this field is missing.
	ActionsConfig []*GoogleCloudApihubV1PluginActionConfig `json:"actionsConfig,omitempty"`
	// ConfigTemplate: Optional. The configuration template for the plugin.
	ConfigTemplate *GoogleCloudApihubV1ConfigTemplate `json:"configTemplate,omitempty"`
	// CreateTime: Output only. Timestamp indicating when the plugin was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. The plugin description. Max length is 2000 characters
	// (Unicode code points).
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the plugin. Max length is 50
	// characters (Unicode code points).
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. The documentation of the plugin, that explains how
	// to set up and use the plugin.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// GatewayType: Optional. The type of the gateway.
	//
	// Possible values:
	//   "GATEWAY_TYPE_UNSPECIFIED" - The gateway type is not specified.
	//   "APIGEE_X_AND_HYBRID" - The gateway type is Apigee X and Hybrid.
	//   "APIGEE_EDGE_PUBLIC_CLOUD" - The gateway type is Apigee Edge Public Cloud.
	//   "APIGEE_EDGE_PRIVATE_CLOUD" - The gateway type is Apigee Edge Private
	// Cloud.
	//   "CLOUD_API_GATEWAY" - The gateway type is Cloud API Gateway.
	//   "CLOUD_ENDPOINTS" - The gateway type is Cloud Endpoints.
	//   "API_DISCOVERY" - The gateway type is API Discovery.
	//   "OTHERS" - The gateway type for any other types of gateways.
	GatewayType string `json:"gatewayType,omitempty"`
	// HostingService: Optional. This field is optional. It is used to notify the
	// plugin hosting service for any lifecycle changes of the plugin instance and
	// trigger execution of plugin instance actions in case of API hub managed
	// actions. This field should be provided if the plugin instance lifecycle of
	// the developed plugin needs to be managed from API hub. Also, in this case
	// the plugin hosting service interface needs to be implemented. This field
	// should not be provided if the plugin wants to manage plugin instance
	// lifecycle events outside of hub interface and use plugin framework for only
	// registering of plugin and plugin instances to capture the source of data
	// into hub. Note, in this case the plugin hosting service interface is not
	// required to be implemented. Also, the plugin instance lifecycle actions will
	// be disabled from API hub's UI.
	HostingService *GoogleCloudApihubV1HostingService `json:"hostingService,omitempty"`
	// Name: Identifier. The name of the plugin. Format:
	// `projects/{project}/locations/{location}/plugins/{plugin}`
	Name string `json:"name,omitempty"`
	// OwnershipType: Output only. The type of the plugin, indicating whether it is
	// 'SYSTEM_OWNED' or 'USER_OWNED'.
	//
	// Possible values:
	//   "OWNERSHIP_TYPE_UNSPECIFIED" - Default unspecified type.
	//   "SYSTEM_OWNED" - System owned plugins are defined by API hub and are
	// available out of the box in API hub.
	//   "USER_OWNED" - User owned plugins are defined by the user and need to be
	// explicitly added to API hub via CreatePlugin method.
	OwnershipType string `json:"ownershipType,omitempty"`
	// PluginCategory: Optional. The category of the plugin, identifying its
	// primary category or purpose. This field is required for all plugins.
	//
	// Possible values:
	//   "PLUGIN_CATEGORY_UNSPECIFIED" - Default unspecified plugin type.
	//   "API_GATEWAY" - API_GATEWAY plugins represent plugins built for API
	// Gateways like Apigee.
	//   "API_PRODUCER" - API_PRODUCER plugins represent plugins built for API
	// Producers like Cloud Run, Application Integration etc.
	PluginCategory string `json:"pluginCategory,omitempty"`
	// State: Output only. Represents the state of the plugin. Note this field will
	// not be set for plugins developed via plugin framework as the state will be
	// managed at plugin instance level.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The default value. This value is used if the state
	// is omitted.
	//   "ENABLED" - The plugin is enabled.
	//   "DISABLED" - The plugin is disabled.
	State string `json:"state,omitempty"`
	// Type: Optional. The type of the API. This maps to the following system
	// defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-plugin-type`
	// attribute. The number of allowed values for this attribute will be based on
	// the cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute. Note this field is not required for plugins developed via plugin
	// framework.
	Type *GoogleCloudApihubV1AttributeValues `json:"type,omitempty"`
	// UpdateTime: Output only. Timestamp indicating when the plugin was last
	// updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ActionsConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionsConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Plugin: A plugin resource in the API Hub.

func (GoogleCloudApihubV1Plugin) MarshalJSON ¶
func (s GoogleCloudApihubV1Plugin) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginActionConfig ¶
type GoogleCloudApihubV1PluginActionConfig struct {
	// Description: Required. The description of the operation performed by the
	// action.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the action.
	DisplayName string `json:"displayName,omitempty"`
	// Id: Required. The id of the action.
	Id string `json:"id,omitempty"`
	// TriggerMode: Required. The trigger mode supported by the action.
	//
	// Possible values:
	//   "TRIGGER_MODE_UNSPECIFIED" - Default unspecified mode.
	//   "API_HUB_ON_DEMAND_TRIGGER" - This action can be executed by invoking
	// ExecutePluginInstanceAction API with the given action id. To support this,
	// the plugin hosting service should handle this action id as part of execute
	// call.
	//   "API_HUB_SCHEDULE_TRIGGER" - This action will be executed on schedule by
	// invoking ExecutePluginInstanceAction API with the given action id. To set
	// the schedule, the user can provide the cron expression in the PluginAction
	// field for a given plugin instance. To support this, the plugin hosting
	// service should handle this action id as part of execute call. Note, on
	// demand execution will be supported by default in this trigger mode.
	//   "NON_API_HUB_MANAGED" - The execution of this plugin is not handled by API
	// hub. In this case, the plugin hosting service need not handle this action id
	// as part of the execute call.
	TriggerMode string `json:"triggerMode,omitempty"`
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

GoogleCloudApihubV1PluginActionConfig: PluginActionConfig represents the configuration of an action supported by a plugin.

func (GoogleCloudApihubV1PluginActionConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1PluginActionConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstance ¶
type GoogleCloudApihubV1PluginInstance struct {
	// Actions: Required. The action status for the plugin instance.
	Actions []*GoogleCloudApihubV1PluginInstanceAction `json:"actions,omitempty"`
	// AdditionalConfig: Optional. The additional information for this plugin
	// instance corresponding to the additional config template of the plugin. This
	// information will be sent to plugin hosting service on each call to plugin
	// hosted service. The key will be the config_variable_template.display_name to
	// uniquely identify the config variable.
	AdditionalConfig map[string]GoogleCloudApihubV1ConfigVariable `json:"additionalConfig,omitempty"`
	// AuthConfig: Optional. The authentication information for this plugin
	// instance.
	AuthConfig *GoogleCloudApihubV1AuthConfig `json:"authConfig,omitempty"`
	// CreateTime: Output only. Timestamp indicating when the plugin instance was
	// created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Required. The display name for this plugin instance. Max length
	// is 255 characters.
	DisplayName string `json:"displayName,omitempty"`
	// ErrorMessage: Output only. Error message describing the failure, if any,
	// during Create, Delete or ApplyConfig operation corresponding to the plugin
	// instance.This field will only be populated if the plugin instance is in the
	// ERROR or FAILED state.
	ErrorMessage string `json:"errorMessage,omitempty"`
	// Name: Identifier. The unique name of the plugin instance resource. Format:
	// `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance
	// }`
	Name string `json:"name,omitempty"`
	// SourceEnvironmentsConfig: Optional. The source environment's config present
	// in the gateway instance linked to the plugin instance. The key is the
	// `source_environment` name from the SourceEnvironment message.
	SourceEnvironmentsConfig map[string]GoogleCloudApihubV1SourceEnvironment `json:"sourceEnvironmentsConfig,omitempty"`
	// SourceProjectId: Optional. The source project id of the plugin instance.
	// This will be the id of runtime project in case of Google Cloud based plugins
	// and org id in case of non-Google Cloud based plugins. This field will be a
	// required field for Google provided on-ramp plugins.
	SourceProjectId string `json:"sourceProjectId,omitempty"`
	// State: Output only. The current state of the plugin instance (e.g., enabled,
	// disabled, provisioning).
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default unspecified state.
	//   "CREATING" - The plugin instance is being created.
	//   "ACTIVE" - The plugin instance is active and ready for executions. This is
	// the only state where executions can run on the plugin instance.
	//   "APPLYING_CONFIG" - The updated config that contains additional_config and
	// auth_config is being applied.
	//   "ERROR" - The ERROR state can come while applying config. Users can
	// retrigger ApplyPluginInstanceConfig to restore the plugin instance back to
	// active state. Note, In case the ERROR state happens while applying config
	// (auth_config, additional_config), the plugin instance will reflect the
	// config which was trying to be applied while error happened. In order to
	// overwrite, trigger ApplyConfig with a new config.
	//   "FAILED" - The plugin instance is in a failed state. This indicates that
	// an unrecoverable error occurred during a previous operation (Create,
	// Delete).
	//   "DELETING" - The plugin instance is being deleted. Delete is only possible
	// if there is no other operation running on the plugin instance and plugin
	// instance action.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. Timestamp indicating when the plugin instance was
	// last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Actions") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Actions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1PluginInstance: Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.

func (GoogleCloudApihubV1PluginInstance) MarshalJSON ¶
func (s GoogleCloudApihubV1PluginInstance) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceAction ¶
type GoogleCloudApihubV1PluginInstanceAction struct {
	// ActionId: Required. This should map to one of the action id specified in
	// actions_config in the plugin.
	ActionId string `json:"actionId,omitempty"`
	// CurationConfig: Optional. This configuration should be provided if the
	// plugin action is publishing data to API hub curate layer.
	CurationConfig *GoogleCloudApihubV1CurationConfig `json:"curationConfig,omitempty"`
	// HubInstanceAction: Optional. The execution information for the plugin
	// instance action done corresponding to an API hub instance.
	HubInstanceAction *GoogleCloudApihubV1ExecutionStatus `json:"hubInstanceAction,omitempty"`
	// ResourceConfig: Output only. The configuration of resources created for a
	// given plugin instance action. Note these will be returned only in case of
	// non-Google Cloud plugins like OPDK.
	ResourceConfig *GoogleCloudApihubV1ResourceConfig `json:"resourceConfig,omitempty"`
	// ScheduleCronExpression: Optional. The schedule for this plugin instance
	// action. This can only be set if the plugin supports API_HUB_SCHEDULE_TRIGGER
	// mode for this action.
	ScheduleCronExpression string `json:"scheduleCronExpression,omitempty"`
	// ScheduleTimeZone: Optional. The time zone for the schedule cron expression.
	// If not provided, UTC will be used.
	ScheduleTimeZone string `json:"scheduleTimeZone,omitempty"`
	// ServiceAccount: Optional. The service account used to publish data. Note,
	// the service account will only be accepted for non-Google Cloud plugins like
	// OPDK.
	ServiceAccount string `json:"serviceAccount,omitempty"`
	// State: Output only. The current state of the plugin action in the plugin
	// instance.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default unspecified state.
	//   "ENABLED" - The action is enabled in the plugin instance i.e., executions
	// can be triggered for this action.
	//   "DISABLED" - The action is disabled in the plugin instance i.e., no
	// executions can be triggered for this action. This state indicates that the
	// user explicitly disabled the instance, and no further action is needed
	// unless the user wants to re-enable it.
	//   "ENABLING" - The action in the plugin instance is being enabled.
	//   "DISABLING" - The action in the plugin instance is being disabled.
	//   "ERROR" - The ERROR state can come while enabling/disabling plugin
	// instance action. Users can retrigger enable, disable via
	// EnablePluginInstanceAction and DisablePluginInstanceAction to restore the
	// action back to enabled/disabled state. Note enable/disable on actions can
	// only be triggered if plugin instance is in Active state.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1PluginInstanceAction: PluginInstanceAction represents an action which can be executed in the plugin instance.

func (GoogleCloudApihubV1PluginInstanceAction) MarshalJSON ¶
func (s GoogleCloudApihubV1PluginInstanceAction) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceActionID ¶
type GoogleCloudApihubV1PluginInstanceActionID struct {
	// ActionId: Output only. The action ID that is using the curation. This should
	// map to one of the action IDs specified in action configs in the plugin.
	ActionId string `json:"actionId,omitempty"`
	// PluginInstance: Output only. Plugin instance that is using the curation.
	// Format is
	// `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance
	// }`
	PluginInstance string `json:"pluginInstance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1PluginInstanceActionID: The plugin instance and associated action that is using the curation.

func (GoogleCloudApihubV1PluginInstanceActionID) MarshalJSON ¶
func (s GoogleCloudApihubV1PluginInstanceActionID) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1PluginInstanceActionSource ¶
type GoogleCloudApihubV1PluginInstanceActionSource struct {
	// ActionId: Output only. The id of the plugin instance action.
	ActionId string `json:"actionId,omitempty"`
	// PluginInstance: Output only. The resource name of the source plugin
	// instance. Format is
	// `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance
	// }`
	PluginInstance string `json:"pluginInstance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1PluginInstanceActionSource: PluginInstanceActionSource represents the plugin instance action source.

func (GoogleCloudApihubV1PluginInstanceActionSource) MarshalJSON ¶
func (s GoogleCloudApihubV1PluginInstanceActionSource) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Point ¶
type GoogleCloudApihubV1Point struct {
	// Character: Required. Character position within the line (zero-indexed).
	Character int64 `json:"character,omitempty"`
	// Line: Required. Line number (zero-indexed).
	Line int64 `json:"line,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Character") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Character") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Point: Point within the file (line and character).

func (GoogleCloudApihubV1Point) MarshalJSON ¶
func (s GoogleCloudApihubV1Point) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1QueryParam ¶
added in v0.245.0
type GoogleCloudApihubV1QueryParam struct {
	// Count: Optional. The number of occurrences of this query parameter across
	// transactions.
	Count int64 `json:"count,omitempty,string"`
	// DataType: Optional. Data type of path param
	//
	// Possible values:
	//   "DATA_TYPE_UNSPECIFIED" - Unspecified data type
	//   "BOOL" - Boolean data type
	//   "INTEGER" - Integer data type
	//   "FLOAT" - Float data type
	//   "STRING" - String data type
	//   "UUID" - UUID data type
	DataType string `json:"dataType,omitempty"`
	// Name: Required. Name of query param
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Count") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Count") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1QueryParam: An aggregation of HTTP query parameter occurrences.

func (GoogleCloudApihubV1QueryParam) MarshalJSON ¶
added in v0.245.0
func (s GoogleCloudApihubV1QueryParam) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Range ¶
type GoogleCloudApihubV1Range struct {
	// End: Required. End of the issue.
	End *GoogleCloudApihubV1Point `json:"end,omitempty"`
	// Start: Required. Start of the issue.
	Start *GoogleCloudApihubV1Point `json:"start,omitempty"`
	// ForceSendFields is a list of field names (e.g. "End") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "End") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Range: Object describing where in the file the issue was found.

func (GoogleCloudApihubV1Range) MarshalJSON ¶
func (s GoogleCloudApihubV1Range) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ResourceConfig ¶
added in v0.241.0
type GoogleCloudApihubV1ResourceConfig struct {
	// ActionType: Output only. The type of the action.
	//
	// Possible values:
	//   "ACTION_TYPE_UNSPECIFIED" - Default unspecified action type.
	//   "SYNC_METADATA" - Action type for sync metadata.
	//   "SYNC_RUNTIME_DATA" - Action type for sync runtime data.
	ActionType string `json:"actionType,omitempty"`
	// PubsubTopic: Output only. The pubsub topic to publish the data to. Format is
	// projects/{project}/topics/{topic}
	PubsubTopic string `json:"pubsubTopic,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActionType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ResourceConfig: The configuration of resources created for a given plugin instance action.

func (GoogleCloudApihubV1ResourceConfig) MarshalJSON ¶
added in v0.241.0
func (s GoogleCloudApihubV1ResourceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1RetrieveApiViewsResponse ¶
added in v0.258.0
type GoogleCloudApihubV1RetrieveApiViewsResponse struct {
	// ApiViews: The list of API views.
	ApiViews []*GoogleCloudApihubV1ApiView `json:"apiViews,omitempty"`
	// NextPageToken: Next page token.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApiViews") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiViews") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1RetrieveApiViewsResponse: The RetrieveApiViews method's response.

func (GoogleCloudApihubV1RetrieveApiViewsResponse) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1RetrieveApiViewsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1RuntimeProjectAttachment ¶
type GoogleCloudApihubV1RuntimeProjectAttachment struct {
	// CreateTime: Output only. Create time.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Identifier. The resource name of a runtime project attachment. Format:
	// "projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_p
	// roject_attachment}".
	Name string `json:"name,omitempty"`
	// RuntimeProject: Required. Immutable. Google cloud project name in the
	// format: "projects/abc" or "projects/123". As input, project name with either
	// project id or number are accepted. As output, this field will contain
	// project number.
	RuntimeProject string `json:"runtimeProject,omitempty"`

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

GoogleCloudApihubV1RuntimeProjectAttachment: Runtime project attachment represents an attachment from the runtime project to the host project. Api Hub looks for deployments in the attached runtime projects and creates corresponding resources in Api Hub for the discovered deployments.

func (GoogleCloudApihubV1RuntimeProjectAttachment) MarshalJSON ¶
func (s GoogleCloudApihubV1RuntimeProjectAttachment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Schema ¶
type GoogleCloudApihubV1Schema struct {
	// DisplayName: Output only. The display name of the schema. This will map to
	// the name of the schema in the spec.
	DisplayName string `json:"displayName,omitempty"`
	// RawValue: Output only. The raw value of the schema definition corresponding
	// to the schema name in the spec.
	RawValue string `json:"rawValue,omitempty"`
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

GoogleCloudApihubV1Schema: The schema details derived from the spec. Currently, this entity is supported for OpenAPI spec only. For OpenAPI spec, this maps to the schema defined in the `definitions` section for OpenAPI 2.0 version and in `components.schemas` section for OpenAPI 3.0 and 3.1 version.

func (GoogleCloudApihubV1Schema) MarshalJSON ¶
func (s GoogleCloudApihubV1Schema) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResourcesRequest ¶
type GoogleCloudApihubV1SearchResourcesRequest struct {
	// Filter: Optional. An expression that filters the list of search results. A
	// filter expression consists of a field name, a comparison operator, and a
	// value for filtering. The value must be a string, a number, or a boolean. The
	// comparison operator must be `=`. Filters are not case sensitive. The
	// following field names are eligible for filtering: * `resource_type` - The
	// type of resource in the search results. Must be one of the following: `Api`,
	// `ApiOperation`, `Deployment`, `Definition`, `Spec` or `Version`. This field
	// can only be specified once in the filter. Here are is an example: *
	// `resource_type = Api` - The resource_type is _Api_.
	Filter string `json:"filter,omitempty"`
	// PageSize: Optional. The maximum number of search results to return. The
	// service may return fewer than this value. If unspecified at most 10 search
	// results will be returned. If value is negative then `INVALID_ARGUMENT` error
	// is returned. The maximum value is 25; values above 25 will be coerced to 25.
	// While paginating, you can specify a new page size parameter for each page of
	// search results to be listed.
	PageSize int64 `json:"pageSize,omitempty"`
	// PageToken: Optional. A page token, received from a previous SearchResources
	// call. Specify this parameter to retrieve the next page of transactions. When
	// paginating, you must specify the `page_token` parameter and all the other
	// parameters except page_size should be specified with the same value which
	// was used in the previous call. If the other fields are set with a different
	// value than the previous call then `INVALID_ARGUMENT` error is returned.
	PageToken string `json:"pageToken,omitempty"`
	// Query: Required. The free text search query. This query can contain keywords
	// which could be related to any detail of the API-Hub resources such display
	// names, descriptions, attributes etc.
	Query string `json:"query,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Filter") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Filter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SearchResourcesRequest: The SearchResources method's request.

func (GoogleCloudApihubV1SearchResourcesRequest) MarshalJSON ¶
func (s GoogleCloudApihubV1SearchResourcesRequest) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResourcesResponse ¶
type GoogleCloudApihubV1SearchResourcesResponse struct {
	// NextPageToken: Pass this token in the SearchResourcesRequest to continue to
	// list results. If all results have been returned, this field is an empty
	// string or not present in the response.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SearchResults: List of search results according to the filter and search
	// query specified. The order of search results represents the ranking.
	SearchResults []*GoogleCloudApihubV1SearchResult `json:"searchResults,omitempty"`

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

GoogleCloudApihubV1SearchResourcesResponse: Response for the SearchResources method.

func (GoogleCloudApihubV1SearchResourcesResponse) MarshalJSON ¶
func (s GoogleCloudApihubV1SearchResourcesResponse) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SearchResult ¶
type GoogleCloudApihubV1SearchResult struct {
	// Resource: This represents the ApiHubResource. Note: Only selected fields of
	// the resources are populated in response.
	Resource *GoogleCloudApihubV1ApiHubResource `json:"resource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Resource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Resource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SearchResult: Represents the search results.

func (GoogleCloudApihubV1SearchResult) MarshalJSON ¶
func (s GoogleCloudApihubV1SearchResult) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Secret ¶
type GoogleCloudApihubV1Secret struct {
	// SecretVersion: Required. The resource name of the secret version in the
	// format, format as: `projects/*/secrets/*/versions/*`.
	SecretVersion string `json:"secretVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SecretVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SecretVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Secret: Secret provides a reference to entries in Secret Manager.

func (GoogleCloudApihubV1Secret) MarshalJSON ¶
func (s GoogleCloudApihubV1Secret) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SourceEnvironment ¶
added in v0.257.0
type GoogleCloudApihubV1SourceEnvironment struct {
	// CreateTime: Optional. The time at which the environment was created at the
	// source.
	CreateTime string `json:"createTime,omitempty"`
	// SourceEnvironment: Required. The name of the environment at the source. This
	// should map to Deployment.
	SourceEnvironment string `json:"sourceEnvironment,omitempty"`
	// SourceEnvironmentUri: The location where additional information about source
	// environments can be found. The location should be relative path of the
	// environment manifest with respect to a plugin instance.
	SourceEnvironmentUri string `json:"sourceEnvironmentUri,omitempty"`
	// UpdateTime: Optional. The time at which the environment was last updated at
	// the source.
	UpdateTime string `json:"updateTime,omitempty"`
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

GoogleCloudApihubV1SourceEnvironment: Message representing the source environment details.

func (GoogleCloudApihubV1SourceEnvironment) MarshalJSON ¶
added in v0.257.0
func (s GoogleCloudApihubV1SourceEnvironment) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SourceMetadata ¶
type GoogleCloudApihubV1SourceMetadata struct {
	// OriginalResourceCreateTime: Output only. The time at which the resource was
	// created at the source.
	OriginalResourceCreateTime string `json:"originalResourceCreateTime,omitempty"`
	// OriginalResourceId: Output only. The unique identifier of the resource at
	// the source.
	OriginalResourceId string `json:"originalResourceId,omitempty"`
	// OriginalResourceUpdateTime: Output only. The time at which the resource was
	// last updated at the source.
	OriginalResourceUpdateTime string `json:"originalResourceUpdateTime,omitempty"`
	// PluginInstanceActionSource: Output only. The source of the resource is a
	// plugin instance action.
	PluginInstanceActionSource *GoogleCloudApihubV1PluginInstanceActionSource `json:"pluginInstanceActionSource,omitempty"`
	// SourceType: Output only. The type of the source.
	//
	// Possible values:
	//   "SOURCE_TYPE_UNSPECIFIED" - Source type not specified.
	//   "PLUGIN" - Source type plugin.
	SourceType string `json:"sourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OriginalResourceCreateTime")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OriginalResourceCreateTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SourceMetadata: SourceMetadata represents the metadata for a resource at the source.

func (GoogleCloudApihubV1SourceMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1SourceMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Spec ¶
type GoogleCloudApihubV1Spec struct {
	// AdditionalSpecContents: Output only. The additional spec contents for the
	// spec.
	AdditionalSpecContents []*GoogleCloudApihubV1AdditionalSpecContent `json:"additionalSpecContents,omitempty"`
	// Attributes: Optional. The list of user defined attributes associated with
	// the spec. The key is the attribute name. It will be of the format:
	// `projects/{project}/locations/{location}/attributes/{attribute}`. The value
	// is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// Contents: Optional. Input only. The contents of the uploaded spec.
	Contents *GoogleCloudApihubV1SpecContents `json:"contents,omitempty"`
	// CreateTime: Output only. The time at which the spec was created.
	CreateTime string `json:"createTime,omitempty"`
	// Details: Output only. Details parsed from the spec.
	Details *GoogleCloudApihubV1SpecDetails `json:"details,omitempty"`
	// DisplayName: Required. The display name of the spec. This can contain the
	// file name of the spec.
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. The documentation of the spec. For OpenAPI spec,
	// this will be populated from `externalDocs` in OpenAPI spec.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// LintResponse: Optional. The lint response for the spec.
	LintResponse *GoogleCloudApihubV1LintResponse `json:"lintResponse,omitempty"`
	// Name: Identifier. The name of the spec. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/
	// {spec}`
	Name string `json:"name,omitempty"`
	// ParsingMode: Optional. Input only. Enum specifying the parsing mode for
	// OpenAPI Specification (OAS) parsing.
	//
	// Possible values:
	//   "PARSING_MODE_UNSPECIFIED" - Defaults to `RELAXED`.
	//   "RELAXED" - Parsing of the Spec on create and update is relaxed, meaning
	// that parsing errors the spec contents will not fail the API call.
	//   "STRICT" - Parsing of the Spec on create and update is strict, meaning
	// that parsing errors in the spec contents will fail the API call.
	ParsingMode string `json:"parsingMode,omitempty"`
	// SourceMetadata: Output only. The list of sources and metadata from the
	// sources of the spec.
	SourceMetadata []*GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// SourceUri: Optional. The URI of the spec source in case file is uploaded
	// from an external version control system.
	SourceUri string `json:"sourceUri,omitempty"`
	// SpecType: Required. The type of spec. The value should be one of the allowed
	// values defined for
	// `projects/{project}/locations/{location}/attributes/system-spec-type`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. Note, this field is mandatory if content is provided.
	SpecType *GoogleCloudApihubV1AttributeValues `json:"specType,omitempty"`
	// UpdateTime: Output only. The time at which the spec was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdditionalSpecContents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalSpecContents") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Spec: Represents a spec associated with an API version in the API Hub. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.

func (GoogleCloudApihubV1Spec) MarshalJSON ¶
func (s GoogleCloudApihubV1Spec) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecContents ¶
type GoogleCloudApihubV1SpecContents struct {
	// Contents: Required. The contents of the spec.
	Contents string `json:"contents,omitempty"`
	// MimeType: Required. The mime type of the content for example
	// application/json, application/yaml, application/wsdl etc.
	MimeType string `json:"mimeType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Contents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Contents") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SpecContents: The spec contents.

func (GoogleCloudApihubV1SpecContents) MarshalJSON ¶
func (s GoogleCloudApihubV1SpecContents) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecDetails ¶
type GoogleCloudApihubV1SpecDetails struct {
	// Description: Output only. The description of the spec.
	Description string `json:"description,omitempty"`
	// OpenApiSpecDetails: Output only. Additional details apart from
	// `OperationDetails` parsed from an OpenAPI spec. The OperationDetails parsed
	// from the spec can be obtained by using ListAPIOperations method.
	OpenApiSpecDetails *GoogleCloudApihubV1OpenApiSpecDetails `json:"openApiSpecDetails,omitempty"`
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

GoogleCloudApihubV1SpecDetails: SpecDetails contains the details parsed from supported spec types.

func (GoogleCloudApihubV1SpecDetails) MarshalJSON ¶
func (s GoogleCloudApihubV1SpecDetails) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SpecMetadata ¶
type GoogleCloudApihubV1SpecMetadata struct {
	// OriginalCreateTime: Optional. Timestamp indicating when the spec was created
	// at the source.
	OriginalCreateTime string `json:"originalCreateTime,omitempty"`
	// OriginalId: Optional. The unique identifier of the spec in the system where
	// it was originally created.
	OriginalId string `json:"originalId,omitempty"`
	// OriginalUpdateTime: Required. Timestamp indicating when the spec was last
	// updated at the source.
	OriginalUpdateTime string `json:"originalUpdateTime,omitempty"`
	// Spec: Required. The spec resource to be pushed to Hub's collect layer. The
	// ID of the spec will be generated by Hub.
	Spec *GoogleCloudApihubV1Spec `json:"spec,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OriginalCreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OriginalCreateTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SpecMetadata: The metadata associated with a spec of the API version.

func (GoogleCloudApihubV1SpecMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1SpecMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StringAttributeValues ¶
type GoogleCloudApihubV1StringAttributeValues struct {
	// Values: Required. The attribute values in case attribute data type is string
	// or JSON.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1StringAttributeValues: The attribute values of data type string or JSON.

func (GoogleCloudApihubV1StringAttributeValues) MarshalJSON ¶
func (s GoogleCloudApihubV1StringAttributeValues) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StyleGuide ¶
type GoogleCloudApihubV1StyleGuide struct {
	// Contents: Required. Input only. The contents of the uploaded style guide.
	Contents *GoogleCloudApihubV1StyleGuideContents `json:"contents,omitempty"`
	// Linter: Required. Target linter for the style guide.
	//
	// Possible values:
	//   "LINTER_UNSPECIFIED" - Linter type unspecified.
	//   "SPECTRAL" - Linter type spectral.
	//   "OTHER" - Linter type other.
	Linter string `json:"linter,omitempty"`
	// Name: Identifier. The name of the style guide. Format:
	// `projects/{project}/locations/{location}/plugins/{plugin}/styleGuide`
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Contents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Contents") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1StyleGuide: Represents a singleton style guide resource to be used for linting Open API specs.

func (GoogleCloudApihubV1StyleGuide) MarshalJSON ¶
func (s GoogleCloudApihubV1StyleGuide) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1StyleGuideContents ¶
type GoogleCloudApihubV1StyleGuideContents struct {
	// Contents: Required. The contents of the style guide.
	Contents string `json:"contents,omitempty"`
	// MimeType: Required. The mime type of the content.
	MimeType string `json:"mimeType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Contents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Contents") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1StyleGuideContents: The style guide contents.

func (GoogleCloudApihubV1StyleGuideContents) MarshalJSON ¶
func (s GoogleCloudApihubV1StyleGuideContents) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1SummaryEntry ¶
type GoogleCloudApihubV1SummaryEntry struct {
	// Count: Required. Count of issues with the given severity.
	Count int64 `json:"count,omitempty"`
	// Severity: Required. Severity of the issue.
	//
	// Possible values:
	//   "SEVERITY_UNSPECIFIED" - Severity unspecified.
	//   "SEVERITY_ERROR" - Severity error.
	//   "SEVERITY_WARNING" - Severity warning.
	//   "SEVERITY_INFO" - Severity info.
	//   "SEVERITY_HINT" - Severity hint.
	Severity string `json:"severity,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Count") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Count") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1SummaryEntry: Count of issues with a given severity.

func (GoogleCloudApihubV1SummaryEntry) MarshalJSON ¶
func (s GoogleCloudApihubV1SummaryEntry) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1ToolAnnotations ¶
added in v0.258.0
type GoogleCloudApihubV1ToolAnnotations struct {
	// AdditionalHints: Optional. Additional hints which may help tools and not
	// covered in defaults.
	AdditionalHints map[string]string `json:"additionalHints,omitempty"`
	// DestructiveHint: Optional. Hint indicating if the tool may have destructive
	// side effects.
	DestructiveHint bool `json:"destructiveHint,omitempty"`
	// IdempotentHint: Optional. Hint indicating if the tool is idempotent.
	IdempotentHint bool `json:"idempotentHint,omitempty"`
	// OpenWorldHint: Optional. Hint indicating if the tool interacts with the open
	// world (e.g., internet).
	OpenWorldHint bool `json:"openWorldHint,omitempty"`
	// ReadOnlyHint: Optional. Hint indicating if the tool is read-only.
	ReadOnlyHint bool `json:"readOnlyHint,omitempty"`
	// Title: Optional. A human-readable title for the tool (if different from
	// Tool.title).
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdditionalHints") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalHints") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1ToolAnnotations: Annotations for a Tool.

func (GoogleCloudApihubV1ToolAnnotations) MarshalJSON ¶
added in v0.258.0
func (s GoogleCloudApihubV1ToolAnnotations) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1UserPasswordConfig ¶
type GoogleCloudApihubV1UserPasswordConfig struct {
	// Password: Required. Secret version reference containing the password. The
	// `secretmanager.versions.access` permission should be granted to the service
	// account accessing the secret.
	Password *GoogleCloudApihubV1Secret `json:"password,omitempty"`
	// Username: Required. Username.
	Username string `json:"username,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Password") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Password") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1UserPasswordConfig: Parameters to support Username and Password Authentication.

func (GoogleCloudApihubV1UserPasswordConfig) MarshalJSON ¶
func (s GoogleCloudApihubV1UserPasswordConfig) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1Version ¶
type GoogleCloudApihubV1Version struct {
	// Accreditation: Optional. The accreditations associated with the API version.
	// This maps to the following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-accreditation`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	Accreditation *GoogleCloudApihubV1AttributeValues `json:"accreditation,omitempty"`
	// ApiOperations: Output only. The operations contained in the API version.
	// These operations will be added to the version when a new spec is added or
	// when an existing spec is updated. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operat
	// ions/{operation}`
	ApiOperations []string `json:"apiOperations,omitempty"`
	// Attributes: Optional. The list of user defined attributes associated with
	// the Version resource. The key is the attribute name. It will be of the
	// format: `projects/{project}/locations/{location}/attributes/{attribute}`.
	// The value is the attribute values associated with the resource.
	Attributes map[string]GoogleCloudApihubV1AttributeValues `json:"attributes,omitempty"`
	// Compliance: Optional. The compliance associated with the API version. This
	// maps to the following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-compliance`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	Compliance *GoogleCloudApihubV1AttributeValues `json:"compliance,omitempty"`
	// CreateTime: Output only. The time at which the version was created.
	CreateTime string `json:"createTime,omitempty"`
	// Definitions: Output only. The definitions contained in the API version.
	// These definitions will be added to the version when a new spec is added or
	// when an existing spec is updated. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/defini
	// tions/{definition}`
	Definitions []string `json:"definitions,omitempty"`
	// Deployments: Optional. The deployments linked to this API version. Note: A
	// particular API version could be deployed to multiple deployments (for dev
	// deployment, UAT deployment, etc) Format is
	// `projects/{project}/locations/{location}/deployments/{deployment}`
	Deployments []string `json:"deployments,omitempty"`
	// Description: Optional. The description of the version.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the version.
	DisplayName string `json:"displayName,omitempty"`
	// Documentation: Optional. The documentation of the version.
	Documentation *GoogleCloudApihubV1Documentation `json:"documentation,omitempty"`
	// Lifecycle: Optional. The lifecycle of the API version. This maps to the
	// following system defined attribute:
	// `projects/{project}/locations/{location}/attributes/system-lifecycle`
	// attribute. The number of values for this attribute will be based on the
	// cardinality of the attribute. The same can be retrieved via GetAttribute
	// API. All values should be from the list of allowed values defined for the
	// attribute.
	Lifecycle *GoogleCloudApihubV1AttributeValues `json:"lifecycle,omitempty"`
	// Name: Identifier. The name of the version. Format:
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}`
	Name string `json:"name,omitempty"`
	// SelectedDeployment: Optional. The selected deployment for a Version
	// resource. This can be used when special handling is needed on client side
	// for a particular deployment linked to the version. Format is
	// `projects/{project}/locations/{location}/deployments/{deployment}`
	SelectedDeployment string `json:"selectedDeployment,omitempty"`
	// SourceMetadata: Output only. The list of sources and metadata from the
	// sources of the version.
	SourceMetadata []*GoogleCloudApihubV1SourceMetadata `json:"sourceMetadata,omitempty"`
	// Specs: Output only. The specs associated with this version. Note that an API
	// version can be associated with multiple specs. Format is
	// `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/
	// {spec}`
	Specs []string `json:"specs,omitempty"`
	// UpdateTime: Output only. The time at which the version was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Accreditation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Accreditation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1Version: Represents a version of the API resource in API hub. This is also referred to as the API version.

func (GoogleCloudApihubV1Version) MarshalJSON ¶
func (s GoogleCloudApihubV1Version) MarshalJSON() ([]byte, error)
type GoogleCloudApihubV1VersionMetadata ¶
type GoogleCloudApihubV1VersionMetadata struct {
	// Deployments: Optional. The deployments linked to this API version. Note: A
	// particular API version could be deployed to multiple deployments (for dev
	// deployment, UAT deployment, etc.)
	Deployments []*GoogleCloudApihubV1DeploymentMetadata `json:"deployments,omitempty"`
	// OriginalCreateTime: Optional. Timestamp indicating when the version was
	// created at the source.
	OriginalCreateTime string `json:"originalCreateTime,omitempty"`
	// OriginalId: Optional. The unique identifier of the version in the system
	// where it was originally created.
	OriginalId string `json:"originalId,omitempty"`
	// OriginalUpdateTime: Required. Timestamp indicating when the version was last
	// updated at the source.
	OriginalUpdateTime string `json:"originalUpdateTime,omitempty"`
	// Specs: Optional. The specs associated with this version. Note that an API
	// version can be associated with multiple specs.
	Specs []*GoogleCloudApihubV1SpecMetadata `json:"specs,omitempty"`
	// Version: Required. Represents a version of the API resource in API hub. The
	// ID of the version will be generated by Hub.
	Version *GoogleCloudApihubV1Version `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Deployments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deployments") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudApihubV1VersionMetadata: The metadata associated with a version of the API resource.

func (GoogleCloudApihubV1VersionMetadata) MarshalJSON ¶
func (s GoogleCloudApihubV1VersionMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudCommonOperationMetadata ¶
type GoogleCloudCommonOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CancelRequested: Output only. Identifies whether the user has requested
	// cancellation of the operation. Operations that have been cancelled
	// successfully have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.
	CancelRequested bool `json:"cancelRequested,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// StatusDetail: Output only. Human-readable status of the operation, if any.
	StatusDetail string `json:"statusDetail,omitempty"`
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

GoogleCloudCommonOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudCommonOperationMetadata) MarshalJSON ¶
func (s GoogleCloudCommonOperationMetadata) MarshalJSON() ([]byte, error)
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
type ProjectsLocationsAddonsGetCall ¶
added in v0.257.0
type ProjectsLocationsAddonsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAddonsGetCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsGetCall) Context(ctx context.Context) *ProjectsLocationsAddonsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAddonsGetCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Addon, error)

Do executes the "apihub.projects.locations.addons.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Addon.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAddonsGetCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAddonsGetCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAddonsGetCall) IfNoneMatch ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAddonsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAddonsListCall ¶
added in v0.257.0
type ProjectsLocationsAddonsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAddonsListCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Context(ctx context.Context) *ProjectsLocationsAddonsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAddonsListCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListAddonsResponse, error)

Do executes the "apihub.projects.locations.addons.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListAddonsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAddonsListCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAddonsListCall) Filter ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Filter(filter string) *ProjectsLocationsAddonsListCall

Filter sets the optional parameter "filter": An expression that filters the list of addons. The only supported filter is `plugin_instance_name`. It can be used to filter addons that are enabled for a given plugin instance. The format of the filter is `plugin_instance_name = "projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance }".

func (*ProjectsLocationsAddonsListCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAddonsListCall) IfNoneMatch ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAddonsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAddonsListCall) PageSize ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) PageSize(pageSize int64) *ProjectsLocationsAddonsListCall

PageSize sets the optional parameter "pageSize": The maximum number of hub addons to return. The service may return fewer than this value. If unspecified, at most 50 hub addons will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsAddonsListCall) PageToken ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) PageToken(pageToken string) *ProjectsLocationsAddonsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAddons` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListAddons` must match the call that provided the page token.

func (*ProjectsLocationsAddonsListCall) Pages ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListAddonsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAddonsManageConfigCall ¶
added in v0.257.0
type ProjectsLocationsAddonsManageConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAddonsManageConfigCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsManageConfigCall) Context(ctx context.Context) *ProjectsLocationsAddonsManageConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAddonsManageConfigCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsManageConfigCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.addons.manageConfig" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAddonsManageConfigCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsManageConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsAddonsManageConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAddonsManageConfigCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsAddonsManageConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAddonsService ¶
added in v0.257.0
type ProjectsLocationsAddonsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAddonsService ¶
added in v0.257.0
func NewProjectsLocationsAddonsService(s *Service) *ProjectsLocationsAddonsService
func (*ProjectsLocationsAddonsService) Get ¶
added in v0.257.0
func (r *ProjectsLocationsAddonsService) Get(name string) *ProjectsLocationsAddonsGetCall

Get: Get an addon.

name: The name of the addon to get. Format: `projects/{project}/locations/{location}/addons/{addon}`.
func (*ProjectsLocationsAddonsService) List ¶
added in v0.257.0
func (r *ProjectsLocationsAddonsService) List(parent string) *ProjectsLocationsAddonsListCall

List: List addons.

parent: The parent resource where this addon will be created. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsAddonsService) ManageConfig ¶
added in v0.257.0
func (r *ProjectsLocationsAddonsService) ManageConfig(name string, googlecloudapihubv1manageaddonconfigrequest *GoogleCloudApihubV1ManageAddonConfigRequest) *ProjectsLocationsAddonsManageConfigCall

ManageConfig: Manage addon config. This RPC is used for managing the config of the addon. Calling this RPC moves the addon into an updating state until the long-running operation succeeds.

name: The name of the addon for which the config is to be managed. Format: `projects/{project}/locations/{location}/addons/{addon}`.
type ProjectsLocationsApiHubInstancesCreateCall ¶
type ProjectsLocationsApiHubInstancesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApiHubInstancesCreateCall) ApiHubInstanceId ¶
func (c *ProjectsLocationsApiHubInstancesCreateCall) ApiHubInstanceId(apiHubInstanceId string) *ProjectsLocationsApiHubInstancesCreateCall

ApiHubInstanceId sets the optional parameter "apiHubInstanceId": Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/a-z[0-9]-_/`.

func (*ProjectsLocationsApiHubInstancesCreateCall) Context ¶
func (c *ProjectsLocationsApiHubInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApiHubInstancesCreateCall) Do ¶
func (c *ProjectsLocationsApiHubInstancesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.apiHubInstances.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApiHubInstancesCreateCall) Fields ¶
func (c *ProjectsLocationsApiHubInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApiHubInstancesCreateCall) Header ¶
func (c *ProjectsLocationsApiHubInstancesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApiHubInstancesDeleteCall ¶
type ProjectsLocationsApiHubInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApiHubInstancesDeleteCall) Context ¶
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApiHubInstancesDeleteCall) Do ¶
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.apiHubInstances.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApiHubInstancesDeleteCall) Fields ¶
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApiHubInstancesDeleteCall) Header ¶
func (c *ProjectsLocationsApiHubInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApiHubInstancesGetCall ¶
type ProjectsLocationsApiHubInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApiHubInstancesGetCall) Context ¶
func (c *ProjectsLocationsApiHubInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApiHubInstancesGetCall) Do ¶
func (c *ProjectsLocationsApiHubInstancesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiHubInstance, error)

Do executes the "apihub.projects.locations.apiHubInstances.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ApiHubInstance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApiHubInstancesGetCall) Fields ¶
func (c *ProjectsLocationsApiHubInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApiHubInstancesGetCall) Header ¶
func (c *ProjectsLocationsApiHubInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApiHubInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApiHubInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApiHubInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApiHubInstancesLookupCall ¶
type ProjectsLocationsApiHubInstancesLookupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApiHubInstancesLookupCall) Context ¶
func (c *ProjectsLocationsApiHubInstancesLookupCall) Context(ctx context.Context) *ProjectsLocationsApiHubInstancesLookupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApiHubInstancesLookupCall) Do ¶
func (c *ProjectsLocationsApiHubInstancesLookupCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1LookupApiHubInstanceResponse, error)

Do executes the "apihub.projects.locations.apiHubInstances.lookup" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1LookupApiHubInstanceResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApiHubInstancesLookupCall) Fields ¶
func (c *ProjectsLocationsApiHubInstancesLookupCall) Fields(s ...googleapi.Field) *ProjectsLocationsApiHubInstancesLookupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApiHubInstancesLookupCall) Header ¶
func (c *ProjectsLocationsApiHubInstancesLookupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApiHubInstancesLookupCall) IfNoneMatch ¶
func (c *ProjectsLocationsApiHubInstancesLookupCall) IfNoneMatch(entityTag string) *ProjectsLocationsApiHubInstancesLookupCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApiHubInstancesService ¶
type ProjectsLocationsApiHubInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApiHubInstancesService ¶
func NewProjectsLocationsApiHubInstancesService(s *Service) *ProjectsLocationsApiHubInstancesService
func (*ProjectsLocationsApiHubInstancesService) Create ¶
func (r *ProjectsLocationsApiHubInstancesService) Create(parent string, googlecloudapihubv1apihubinstance *GoogleCloudApihubV1ApiHubInstance) *ProjectsLocationsApiHubInstancesCreateCall

Create: Provisions instance resources for the API Hub.

parent: The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsApiHubInstancesService) Delete ¶
func (r *ProjectsLocationsApiHubInstancesService) Delete(name string) *ProjectsLocationsApiHubInstancesDeleteCall

Delete: Deletes the API hub instance. Deleting the API hub instance will also result in the removal of all associated runtime project attachments and the host project registration.

name: The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.
func (*ProjectsLocationsApiHubInstancesService) Get ¶
func (r *ProjectsLocationsApiHubInstancesService) Get(name string) *ProjectsLocationsApiHubInstancesGetCall

Get: Gets details of a single API Hub instance.

name: The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.
func (*ProjectsLocationsApiHubInstancesService) Lookup ¶
func (r *ProjectsLocationsApiHubInstancesService) Lookup(parent string) *ProjectsLocationsApiHubInstancesLookupCall

Lookup: Looks up an Api Hub instance in a given Google Cloud project. There will always be only one Api Hub instance for a Google Cloud project across all locations.

parent: There will always be only one Api Hub instance for a Google Cloud project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`.
type ProjectsLocationsApisCreateCall ¶
type ProjectsLocationsApisCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisCreateCall) ApiId ¶
func (c *ProjectsLocationsApisCreateCall) ApiId(apiId string) *ProjectsLocationsApisCreateCall

ApiId sets the optional parameter "apiId": The ID to use for the API resource, which will become the final component of the API's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another API resource in the API hub. * If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsApisCreateCall) Context ¶
func (c *ProjectsLocationsApisCreateCall) Context(ctx context.Context) *ProjectsLocationsApisCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisCreateCall) Do ¶
func (c *ProjectsLocationsApisCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)

Do executes the "apihub.projects.locations.apis.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisCreateCall) Fields ¶
func (c *ProjectsLocationsApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisCreateCall) Header ¶
func (c *ProjectsLocationsApisCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeleteCall ¶
type ProjectsLocationsApisDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisDeleteCall) Context ¶
func (c *ProjectsLocationsApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisDeleteCall) Do ¶
func (c *ProjectsLocationsApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.apis.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisDeleteCall) Fields ¶
func (c *ProjectsLocationsApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisDeleteCall) Force ¶
func (c *ProjectsLocationsApisDeleteCall) Force(force bool) *ProjectsLocationsApisDeleteCall

Force sets the optional parameter "force": If set to true, any versions from this API will also be deleted. Otherwise, the request will only work if the API has no versions.

func (*ProjectsLocationsApisDeleteCall) Header ¶
func (c *ProjectsLocationsApisDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisGetCall ¶
type ProjectsLocationsApisGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisGetCall) Context ¶
func (c *ProjectsLocationsApisGetCall) Context(ctx context.Context) *ProjectsLocationsApisGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisGetCall) Do ¶
func (c *ProjectsLocationsApisGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)

Do executes the "apihub.projects.locations.apis.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisGetCall) Fields ¶
func (c *ProjectsLocationsApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisGetCall) Header ¶
func (c *ProjectsLocationsApisGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisListCall ¶
type ProjectsLocationsApisListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisListCall) Context ¶
func (c *ProjectsLocationsApisListCall) Context(ctx context.Context) *ProjectsLocationsApisListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisListCall) Do ¶
func (c *ProjectsLocationsApisListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListApisResponse, error)

Do executes the "apihub.projects.locations.apis.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListApisResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisListCall) Fields ¶
func (c *ProjectsLocationsApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisListCall) Filter ¶
func (c *ProjectsLocationsApisListCall) Filter(filter string) *ProjectsLocationsApisListCall

Filter sets the optional parameter "filter": An expression that filters the list of ApiResources. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>`, `:` or `=`. Filters are not case sensitive. The following fields in the `ApiResource` are eligible for filtering: * `owner.email` - The email of the team which owns the ApiResource. Allowed comparison operators: `=`. * `create_time` - The time at which the ApiResource was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `display_name` - The display name of the ApiResource. Allowed comparison operators: `=`. * `target_user.enum_values.values.id` - The allowed value id of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`. * `target_user.enum_values.values.display_name` - The allowed value display name of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`. * `team.enum_values.values.id` - The allowed value id of the team attribute associated with the ApiResource. Allowed comparison operator is `:`. * `team.enum_values.values.display_name` - The allowed value display name of the team attribute associated with the ApiResource. Allowed comparison operator is `:`. * `business_unit.enum_values.values.id` - The allowed value id of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`. * `business_unit.enum_values.values.display_name` - The allowed value display name of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`. * `maturity_level.enum_values.values.id` - The allowed value id of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`. * `maturity_level.enum_values.values.display_name` - The allowed value display name of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`. * `api_style.enum_values.values.id` - The allowed value id of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`. * `api_style.enum_values.values.display_name` - The allowed value display name of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` - The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` - The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` - The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` - The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"api-1\" is equivalent to `name = \"projects/test-project-id/locations/test-location-id/apis/api-1\" provided the parent is `projects/test-project-id/locations/test-location-id`. Another supported filter function is `plugins(source_metadata)`. This function filters for resources that are associated with a specific plugin. For example, `plugins(source_metadata) : "projects/test-project-id/locations/test-location-id/plugins/test-plugin-id"

will return resources sourced from the given plugin. Expressions are


combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `owner.email = \"apihub@google.com\" - - The owner team email is _apihub@google.com_. * `owner.email = \"apihub@google.com\" AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The owner team email is _apihub@google.com_ and the api was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `owner.email = \"apihub@google.com\" OR team.enum_values.values.id: apihub-team-id` - The filter string specifies the APIs where the owner team email is _apihub@google.com_ or the id of the allowed value associated with the team attribute is _apihub-team-id_. * `owner.email = \"apihub@google.com\" OR team.enum_values.values.display_name: ApiHub Team` - The filter string specifies the APIs where the owner team email is _apihub@google.com_ or the display name of the allowed value associated with the team attribute is `ApiHub Team`. * `owner.email = \"apihub@google.com\" AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test_enum_id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/1765\0f90-4a29-5431-b3d0-d5532da3764c.string_values.values: test_string_value` - The filter string specifies the APIs where the owner team email is _apihub@google.com_ and the id of the allowed value associated with the user defined attribute of type enum is _test_enum_id_ and the value of the user defined attribute of type string is _test_..

func (*ProjectsLocationsApisListCall) Header ¶
func (c *ProjectsLocationsApisListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisListCall) PageSize ¶
func (c *ProjectsLocationsApisListCall) PageSize(pageSize int64) *ProjectsLocationsApisListCall

PageSize sets the optional parameter "pageSize": The maximum number of API resources to return. The service may return fewer than this value. If unspecified, at most 50 Apis will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisListCall) PageToken ¶
func (c *ProjectsLocationsApisListCall) PageToken(pageToken string) *ProjectsLocationsApisListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListApis` must match the call that provided the page token.

func (*ProjectsLocationsApisListCall) Pages ¶
func (c *ProjectsLocationsApisListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListApisResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisPatchCall ¶
type ProjectsLocationsApisPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisPatchCall) Context ¶
func (c *ProjectsLocationsApisPatchCall) Context(ctx context.Context) *ProjectsLocationsApisPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisPatchCall) Do ¶
func (c *ProjectsLocationsApisPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Api, error)

Do executes the "apihub.projects.locations.apis.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Api.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisPatchCall) Fields ¶
func (c *ProjectsLocationsApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisPatchCall) Header ¶
func (c *ProjectsLocationsApisPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsApisService ¶
type ProjectsLocationsApisService struct {
	Versions *ProjectsLocationsApisVersionsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisService ¶
func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService
func (*ProjectsLocationsApisService) Create ¶
func (r *ProjectsLocationsApisService) Create(parent string, googlecloudapihubv1api *GoogleCloudApihubV1Api) *ProjectsLocationsApisCreateCall

Create: Create an API resource in the API hub. Once an API resource is created, versions can be added to it.

parent: The parent resource for the API resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsApisService) Delete ¶
func (r *ProjectsLocationsApisService) Delete(name string) *ProjectsLocationsApisDeleteCall

Delete: Delete an API resource in the API hub. API can only be deleted if all underlying versions are deleted.

name: The name of the API resource to delete. Format: `projects/{project}/locations/{location}/apis/{api}`.
func (*ProjectsLocationsApisService) Get ¶
func (r *ProjectsLocationsApisService) Get(name string) *ProjectsLocationsApisGetCall

Get: Get API resource details including the API versions contained in it.

name: The name of the API resource to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}`.
func (*ProjectsLocationsApisService) List ¶
func (r *ProjectsLocationsApisService) List(parent string) *ProjectsLocationsApisListCall

List: List API resources in the API hub.

parent: The parent, which owns this collection of API resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsApisService) Patch ¶
func (r *ProjectsLocationsApisService) Patch(name string, googlecloudapihubv1api *GoogleCloudApihubV1Api) *ProjectsLocationsApisPatchCall

Patch: Update an API resource in the API hub. The following fields in the API can be updated: * display_name * description * owner * documentation * target_user * team * business_unit * maturity_level * api_style * attributes * fingerprint The update_mask should be used to specify the fields being updated. Updating the owner field requires complete owner message and updates both owner and email fields.

name: Identifier. The name of the API resource in the API Hub. Format: `projects/{project}/locations/{location}/apis/{api}`.
type ProjectsLocationsApisVersionsCreateCall ¶
type ProjectsLocationsApisVersionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)

Do executes the "apihub.projects.locations.apis.versions.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsCreateCall) VersionId ¶
func (c *ProjectsLocationsApisVersionsCreateCall) VersionId(versionId string) *ProjectsLocationsApisVersionsCreateCall

VersionId sets the optional parameter "versionId": The ID to use for the API version, which will become the final component of the version's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another version in the API resource. * If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}`, its length is limited to 700 characters and valid characters are /a-z[0-9]-_/.

type ProjectsLocationsApisVersionsDefinitionsGetCall ¶
type ProjectsLocationsApisVersionsDefinitionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsDefinitionsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDefinitionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsDefinitionsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Definition, error)

Do executes the "apihub.projects.locations.apis.versions.definitions.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Definition.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsDefinitionsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDefinitionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsDefinitionsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsDefinitionsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsDefinitionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsDefinitionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsDefinitionsService ¶
type ProjectsLocationsApisVersionsDefinitionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsDefinitionsService ¶
func NewProjectsLocationsApisVersionsDefinitionsService(s *Service) *ProjectsLocationsApisVersionsDefinitionsService
func (*ProjectsLocationsApisVersionsDefinitionsService) Get ¶
func (r *ProjectsLocationsApisVersionsDefinitionsService) Get(name string) *ProjectsLocationsApisVersionsDefinitionsGetCall

Get: Get details about a definition in an API version.

name: The name of the definition to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/defi nitions/{definition}`.
type ProjectsLocationsApisVersionsDeleteCall ¶
type ProjectsLocationsApisVersionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.apis.versions.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsDeleteCall) Force ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Force(force bool) *ProjectsLocationsApisVersionsDeleteCall

Force sets the optional parameter "force": If set to true, any specs from this version will also be deleted. Otherwise, the request will only work if the version has no specs.

func (*ProjectsLocationsApisVersionsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsGetCall ¶
type ProjectsLocationsApisVersionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)

Do executes the "apihub.projects.locations.apis.versions.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsListCall ¶
type ProjectsLocationsApisVersionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListVersionsResponse, error)

Do executes the "apihub.projects.locations.apis.versions.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListVersionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsListCall) Filter(filter string) *ProjectsLocationsApisVersionsListCall

Filter sets the optional parameter "filter": An expression that filters the list of Versions. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `Version` are eligible for filtering: * `display_name` - The display name of the Version. Allowed comparison operators: `=`. * `create_time` - The time at which the Version was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `lifecycle.enum_values.values.id` - The allowed value id of the lifecycle attribute associated with the Version. Allowed comparison operators: `:`. * `lifecycle.enum_values.values.display_name` - The allowed value display name of the lifecycle attribute associated with the Version. Allowed comparison operators: `:`. * `compliance.enum_values.values.id` - The allowed value id of the compliances attribute associated with the Version. Allowed comparison operators: `:`. * `compliance.enum_values.values.display_name` - The allowed value display name of the compliances attribute associated with the Version. Allowed comparison operators: `:`. * `accreditation.enum_values.values.id` - The allowed value id of the accreditations attribute associated with the Version. Allowed comparison operators: `:`. * `accreditation.enum_values.values.display_name` - The allowed value display name of the accreditations attribute associated with the Version. Allowed comparison operators: `:`. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` - The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` - The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` - The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` - The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `lifecycle.enum_values.values.id: preview-id` - The filter string specifies that the id of the allowed value associated with the lifecycle attribute of the Version is _preview-id_. * `lifecycle.enum_values.values.display_name: \"Preview Display Name\" - The filter string specifies that the display name of the allowed value associated with the lifecycle attribute of the Version is `Preview Display Name`. * `lifecycle.enum_values.values.id: preview-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The id of the allowed value associated with the lifecycle attribute of the Version is _preview-id_ and it was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `compliance.enum_values.values.id: gdpr-id OR compliance.enum_values.values.id: pci-dss-id` - The id of the allowed value associated with the compliance attribute is _gdpr-id_ or _pci-dss-id_. * `lifecycle.enum_values.values.id: preview-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test` - The filter string specifies that the id of the allowed value associated with the lifecycle attribute of the Version is _preview-id_ and the value of the user defined attribute of type string is _test_.

func (*ProjectsLocationsApisVersionsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 versions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListVersions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListVersions` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListVersionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsOperationsCreateCall ¶
type ProjectsLocationsApisVersionsOperationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsOperationsCreateCall) ApiOperationId ¶
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) ApiOperationId(apiOperationId string) *ProjectsLocationsApisVersionsOperationsCreateCall

ApiOperationId sets the optional parameter "apiOperationId": The ID to use for the operation resource, which will become the final component of the operation's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another operation resource in the API hub. * If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operat ions/{operation}`, its length is limited to 700 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsApisVersionsOperationsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsOperationsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)

Do executes the "apihub.projects.locations.apis.versions.operations.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ApiOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsOperationsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsOperationsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsOperationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsOperationsDeleteCall ¶
type ProjectsLocationsApisVersionsOperationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsOperationsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsOperationsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.apis.versions.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsOperationsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsOperationsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsOperationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsOperationsGetCall ¶
type ProjectsLocationsApisVersionsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsOperationsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsOperationsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)

Do executes the "apihub.projects.locations.apis.versions.operations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ApiOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsOperationsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsOperationsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsOperationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsOperationsListCall ¶
type ProjectsLocationsApisVersionsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsOperationsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsOperationsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListApiOperationsResponse, error)

Do executes the "apihub.projects.locations.apis.versions.operations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListApiOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsOperationsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsOperationsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Filter(filter string) *ProjectsLocationsApisVersionsOperationsListCall

Filter sets the optional parameter "filter": An expression that filters the list of ApiOperations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string or a boolean. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `ApiOperation` are eligible for filtering: * `name` - The ApiOperation resource name. Allowed comparison operators: `=`. * `details.http_operation.path.path` - The http operation's complete path relative to server endpoint. Allowed comparison operators: `=`. * `details.http_operation.method` - The http operation method type. Allowed comparison operators: `=`. * `details.deprecated` - Indicates if the ApiOperation is deprecated. Allowed values are True / False indicating the deprycation status of the ApiOperation. Allowed comparison operators: `=`. * `create_time` - The time at which the ApiOperation was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` - The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` - The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` - The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` - The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `details.deprecated = True` - The ApiOperation is deprecated. * `details.http_operation.method = GET AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The method of the http operation of the ApiOperation is _GET_ and the spec was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `details.http_operation.method = GET OR details.http_operation.method = POST`. - The http operation of the method of ApiOperation is _GET_ or _POST_. * `details.deprecated = True AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test` - The filter string specifies that the ApiOperation is deprecated and the value of the user defined attribute of type string is _test_.

func (*ProjectsLocationsApisVersionsOperationsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsOperationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsOperationsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsOperationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of operations to return. The service may return fewer than this value. If unspecified, at most 50 operations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsOperationsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsOperationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiOperations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListApiOperations` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsOperationsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsOperationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListApiOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsOperationsPatchCall ¶
type ProjectsLocationsApisVersionsOperationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsOperationsPatchCall) Context ¶
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsOperationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsOperationsPatchCall) Do ¶
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ApiOperation, error)

Do executes the "apihub.projects.locations.apis.versions.operations.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ApiOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsOperationsPatchCall) Fields ¶
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsOperationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsOperationsPatchCall) Header ¶
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsOperationsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisVersionsOperationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsOperationsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsApisVersionsOperationsService ¶
type ProjectsLocationsApisVersionsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsOperationsService ¶
func NewProjectsLocationsApisVersionsOperationsService(s *Service) *ProjectsLocationsApisVersionsOperationsService
func (*ProjectsLocationsApisVersionsOperationsService) Create ¶
func (r *ProjectsLocationsApisVersionsOperationsService) Create(parent string, googlecloudapihubv1apioperation *GoogleCloudApihubV1ApiOperation) *ProjectsLocationsApisVersionsOperationsCreateCall

Create: Create an apiOperation in an API version. An apiOperation can be created only if the version has no apiOperations which were created by parsing a spec.

parent: The parent resource for the operation resource. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsOperationsService) Delete ¶
func (r *ProjectsLocationsApisVersionsOperationsService) Delete(name string) *ProjectsLocationsApisVersionsOperationsDeleteCall

Delete: Delete an operation in an API version and we can delete only the operations created via create API. If the operation was created by parsing the spec, then it can be deleted by editing or deleting the spec.

name: The name of the operation resource to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/oper ations/{operation}`.
func (*ProjectsLocationsApisVersionsOperationsService) Get ¶
func (r *ProjectsLocationsApisVersionsOperationsService) Get(name string) *ProjectsLocationsApisVersionsOperationsGetCall

Get: Get details about a particular operation in API version.

name: The name of the operation to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/oper ations/{operation}`.
func (*ProjectsLocationsApisVersionsOperationsService) List ¶
func (r *ProjectsLocationsApisVersionsOperationsService) List(parent string) *ProjectsLocationsApisVersionsOperationsListCall

List: List operations in an API version.

parent: The parent which owns this collection of operations i.e., the API version. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsOperationsService) Patch ¶
func (r *ProjectsLocationsApisVersionsOperationsService) Patch(name string, googlecloudapihubv1apioperation *GoogleCloudApihubV1ApiOperation) *ProjectsLocationsApisVersionsOperationsPatchCall

Patch: Update an operation in an API version. The following fields in the ApiOperation resource can be updated: * details.description * details.documentation * details.http_operation.path * details.http_operation.method * details.deprecated * attributes * details.mcp_tool.title * details.mcp_tool.description * details.mcp_tool.input_schema * details.mcp_tool.output_schema * details.input_schema * details.output_schema * details.mcp_tool.annotations.title * details.mcp_tool.annotations.read_only_hint * details.mcp_tool.annotations.destructive_hint * details.mcp_tool.annotations.idempotent_hint * details.mcp_tool.annotations.open_world_hint * details.mcp_tool.annotations.additional_hints The update_mask should be used to specify the fields being updated. An operation can be updated only if the operation was created via CreateApiOperation API. If the operation was created by parsing the spec, then it can be edited by updating the spec.

name: Identifier. The name of the operation. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/oper ations/{operation}`.
type ProjectsLocationsApisVersionsPatchCall ¶
type ProjectsLocationsApisVersionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsPatchCall) Context ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsPatchCall) Do ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Version, error)

Do executes the "apihub.projects.locations.apis.versions.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Version.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsPatchCall) Fields ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsPatchCall) Header ¶
func (c *ProjectsLocationsApisVersionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisVersionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsApisVersionsService ¶
type ProjectsLocationsApisVersionsService struct {
	Definitions *ProjectsLocationsApisVersionsDefinitionsService

	Operations *ProjectsLocationsApisVersionsOperationsService

	Specs *ProjectsLocationsApisVersionsSpecsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsService ¶
func NewProjectsLocationsApisVersionsService(s *Service) *ProjectsLocationsApisVersionsService
func (*ProjectsLocationsApisVersionsService) Create ¶
func (r *ProjectsLocationsApisVersionsService) Create(parent string, googlecloudapihubv1version *GoogleCloudApihubV1Version) *ProjectsLocationsApisVersionsCreateCall

Create: Create an API version for an API resource in the API hub.

parent: The parent resource for API version. Format: `projects/{project}/locations/{location}/apis/{api}`.
func (*ProjectsLocationsApisVersionsService) Delete ¶
func (r *ProjectsLocationsApisVersionsService) Delete(name string) *ProjectsLocationsApisVersionsDeleteCall

Delete: Delete an API version. Version can only be deleted if all underlying specs, operations, definitions and linked deployments are deleted.

name: The name of the version to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsService) Get ¶
func (r *ProjectsLocationsApisVersionsService) Get(name string) *ProjectsLocationsApisVersionsGetCall

Get: Get details about the API version of an API resource. This will include information about the specs and operations present in the API version as well as the deployments linked to it.

name: The name of the API version to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsService) List ¶
func (r *ProjectsLocationsApisVersionsService) List(parent string) *ProjectsLocationsApisVersionsListCall

List: List API versions of an API resource in the API hub.

parent: The parent which owns this collection of API versions i.e., the API resource Format: `projects/{project}/locations/{location}/apis/{api}`.
func (*ProjectsLocationsApisVersionsService) Patch ¶
func (r *ProjectsLocationsApisVersionsService) Patch(name string, googlecloudapihubv1version *GoogleCloudApihubV1Version) *ProjectsLocationsApisVersionsPatchCall

Patch: Update API version. The following fields in the version can be updated currently: * display_name * description * documentation * deployments * lifecycle * compliance * accreditation * attributes The update_mask should be used to specify the fields being updated.

name: Identifier. The name of the version. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
type ProjectsLocationsApisVersionsSpecsCreateCall ¶
type ProjectsLocationsApisVersionsSpecsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsCreateCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)

Do executes the "apihub.projects.locations.apis.versions.specs.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Spec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsCreateCall) SpecId ¶
func (c *ProjectsLocationsApisVersionsSpecsCreateCall) SpecId(specId string) *ProjectsLocationsApisVersionsSpecsCreateCall

SpecId sets the optional parameter "specId": The ID to use for the spec, which will become the final component of the spec's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another spec in the API resource. * If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/ {spec}`, its length is limited to 1000 characters and valid characters are /a-z[0-9]-_/.

type ProjectsLocationsApisVersionsSpecsDeleteCall ¶
type ProjectsLocationsApisVersionsSpecsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.apis.versions.specs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsDeleteCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall ¶
added in v0.258.0
type ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Context ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Do ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1FetchAdditionalSpecContentResponse, error)

Do executes the "apihub.projects.locations.apis.versions.specs.fetchAdditionalSpecContent" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1FetchAdditionalSpecContentResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Fields ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Header ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) IfNoneMatch ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) SpecContentType ¶
added in v0.258.0
func (c *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall) SpecContentType(specContentType string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall

SpecContentType sets the optional parameter "specContentType": The type of the spec contents to be retrieved.

Possible values:

"SPEC_CONTENT_TYPE_UNSPECIFIED" - Unspecified spec content type. Defaults


to spec content uploaded by the user.

"BOOSTED_SPEC_CONTENT" - The spec content type for boosted spec.
"GATEWAY_OPEN_API_SPEC" - The spec content type for OpenAPI spec. This


enum is used for OpenAPI specs ingested via APIGEE X Gateway.

type ProjectsLocationsApisVersionsSpecsGetCall ¶
type ProjectsLocationsApisVersionsSpecsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsGetCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)

Do executes the "apihub.projects.locations.apis.versions.specs.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Spec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsGetCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsGetContentsCall ¶
type ProjectsLocationsApisVersionsSpecsGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1SpecContents, error)

Do executes the "apihub.projects.locations.apis.versions.specs.getContents" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1SpecContents.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisVersionsSpecsLintCall ¶
type ProjectsLocationsApisVersionsSpecsLintCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsLintCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsLintCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsLintCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.apis.versions.specs.lint" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsLintCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsLintCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsLintCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsLintCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisVersionsSpecsListCall ¶
type ProjectsLocationsApisVersionsSpecsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsListCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsListCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListSpecsResponse, error)

Do executes the "apihub.projects.locations.apis.versions.specs.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListSpecsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsListCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsListCall) Filter ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Filter(filter string) *ProjectsLocationsApisVersionsSpecsListCall

Filter sets the optional parameter "filter": An expression that filters the list of Specs. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>`, `:` or `=`. Filters are not case sensitive. The following fields in the `Spec` are eligible for filtering: * `display_name` - The display name of the Spec. Allowed comparison operators: `=`. * `create_time` - The time at which the Spec was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `spec_type.enum_values.values.id` - The allowed value id of the spec_type attribute associated with the Spec. Allowed comparison operators: `:`. * `spec_type.enum_values.values.display_name` - The allowed value display name of the spec_type attribute associated with the Spec. Allowed comparison operators: `:`. * `lint_response.json_values.values` - The json value of the lint_response attribute associated with the Spec. Allowed comparison operators: `:`. * `mime_type` - The MIME type of the Spec. Allowed comparison operators: `=`. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` - The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` - The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` - The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` - The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `spec_type.enum_values.values.id: rest-id` - The filter string specifies that the id of the allowed value associated with the spec_type attribute is _rest-id_. * `spec_type.enum_values.values.display_name: \"Rest Display Name\" - The filter string specifies that the display name of the allowed value associated with the spec_type attribute is `Rest Display Name`. * `spec_type.enum_values.values.id: grpc-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The id of the allowed value associated with the spec_type attribute is _grpc-id_ and the spec was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `spec_type.enum_values.values.id: rest-id OR spec_type.enum_values.values.id: grpc-id` - The id of the allowed value associated with the spec_type attribute is _rest-id_ or _grpc-id_. * `spec_type.enum_values.values.id: rest-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test` - The filter string specifies that the id of the allowed value associated with the spec_type attribute is _rest-id_ and the id of the allowed value associated with the user defined attribute of type enum is _test_.

func (*ProjectsLocationsApisVersionsSpecsListCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisVersionsSpecsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsApisVersionsSpecsListCall) PageSize ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageSize(pageSize int64) *ProjectsLocationsApisVersionsSpecsListCall

PageSize sets the optional parameter "pageSize": The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 specs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsApisVersionsSpecsListCall) PageToken ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) PageToken(pageToken string) *ProjectsLocationsApisVersionsSpecsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSpecs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSpecs` must match the call that provided the page token.

func (*ProjectsLocationsApisVersionsSpecsListCall) Pages ¶
func (c *ProjectsLocationsApisVersionsSpecsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListSpecsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisVersionsSpecsPatchCall ¶
type ProjectsLocationsApisVersionsSpecsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsApisVersionsSpecsPatchCall) Context ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisVersionsSpecsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Do ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Spec, error)

Do executes the "apihub.projects.locations.apis.versions.specs.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Spec.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Fields ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisVersionsSpecsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) Header ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsApisVersionsSpecsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisVersionsSpecsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsApisVersionsSpecsService ¶
type ProjectsLocationsApisVersionsSpecsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsApisVersionsSpecsService ¶
func NewProjectsLocationsApisVersionsSpecsService(s *Service) *ProjectsLocationsApisVersionsSpecsService
func (*ProjectsLocationsApisVersionsSpecsService) Create ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Create(parent string, googlecloudapihubv1spec *GoogleCloudApihubV1Spec) *ProjectsLocationsApisVersionsSpecsCreateCall

Create: Add a spec to an API version in the API hub. Multiple specs can be added to an API version. Note, while adding a spec, at least one of `contents` or `source_uri` must be provided. If `contents` is provided, then `spec_type` must also be provided. On adding a spec with contents to the version, the operations present in it will be added to the version.Note that the file contents in the spec should be of the same type as defined in the `projects/{project}/locations/{location}/attributes/system-spec-type` attribute associated with spec resource. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently. In order to access the information parsed from the spec, use the GetSpec method. In order to access the raw contents for a particular spec, use the GetSpecContents method. In order to access the operations parsed from the spec, use the ListAPIOperations method.

parent: The parent resource for Spec. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsSpecsService) Delete ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Delete(name string) *ProjectsLocationsApisVersionsSpecsDeleteCall

Delete: Delete a spec. Deleting a spec will also delete the associated operations from the version.

name: The name of the spec to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
func (*ProjectsLocationsApisVersionsSpecsService) FetchAdditionalSpecContent ¶
added in v0.258.0
func (r *ProjectsLocationsApisVersionsSpecsService) FetchAdditionalSpecContent(name string) *ProjectsLocationsApisVersionsSpecsFetchAdditionalSpecContentCall

FetchAdditionalSpecContent: Fetch additional spec content.

name: The name of the spec whose contents need to be retrieved. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
func (*ProjectsLocationsApisVersionsSpecsService) Get ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Get(name string) *ProjectsLocationsApisVersionsSpecsGetCall

Get: Get details about the information parsed from a spec. Note that this method does not return the raw spec contents. Use GetSpecContents method to retrieve the same.

name: The name of the spec to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
func (*ProjectsLocationsApisVersionsSpecsService) GetContents ¶
func (r *ProjectsLocationsApisVersionsSpecsService) GetContents(name string) *ProjectsLocationsApisVersionsSpecsGetContentsCall

GetContents: Get spec contents.

name: The name of the spec whose contents need to be retrieved. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
func (*ProjectsLocationsApisVersionsSpecsService) Lint ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Lint(name string, googlecloudapihubv1lintspecrequest *GoogleCloudApihubV1LintSpecRequest) *ProjectsLocationsApisVersionsSpecsLintCall

Lint: Lints the requested spec and updates the corresponding API Spec with the lint response. This lint response will be available in all subsequent Get and List Spec calls to Core service.

name: The name of the spec to be linted. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
func (*ProjectsLocationsApisVersionsSpecsService) List ¶
func (r *ProjectsLocationsApisVersionsSpecsService) List(parent string) *ProjectsLocationsApisVersionsSpecsListCall

List: List specs corresponding to a particular API resource.

parent: The parent, which owns this collection of specs. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`.
func (*ProjectsLocationsApisVersionsSpecsService) Patch ¶
func (r *ProjectsLocationsApisVersionsSpecsService) Patch(name string, googlecloudapihubv1spec *GoogleCloudApihubV1Spec) *ProjectsLocationsApisVersionsSpecsPatchCall

Patch: Update spec. The following fields in the spec can be updated: * display_name * source_uri * lint_response * attributes * contents * spec_type In case of an OAS spec, updating spec contents can lead to: 1. Creation, deletion and update of operations. 2. Creation, deletion and update of definitions. 3. Update of other info parsed out from the new spec. In case of contents or source_uri being present in update mask, spec_type must also be present. Also, spec_type can not be present in update mask if contents or source_uri is not present. The update_mask should be used to specify the fields being updated.

name: Identifier. The name of the spec. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/spec s/{spec}`.
type ProjectsLocationsAttributesCreateCall ¶
type ProjectsLocationsAttributesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAttributesCreateCall) AttributeId ¶
func (c *ProjectsLocationsAttributesCreateCall) AttributeId(attributeId string) *ProjectsLocationsAttributesCreateCall

AttributeId sets the optional parameter "attributeId": The ID to use for the attribute, which will become the final component of the attribute's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another attribute resource in the API hub. * If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsAttributesCreateCall) Context ¶
func (c *ProjectsLocationsAttributesCreateCall) Context(ctx context.Context) *ProjectsLocationsAttributesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAttributesCreateCall) Do ¶
func (c *ProjectsLocationsAttributesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)

Do executes the "apihub.projects.locations.attributes.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Attribute.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAttributesCreateCall) Fields ¶
func (c *ProjectsLocationsAttributesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAttributesCreateCall) Header ¶
func (c *ProjectsLocationsAttributesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAttributesDeleteCall ¶
type ProjectsLocationsAttributesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAttributesDeleteCall) Context ¶
func (c *ProjectsLocationsAttributesDeleteCall) Context(ctx context.Context) *ProjectsLocationsAttributesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAttributesDeleteCall) Do ¶
func (c *ProjectsLocationsAttributesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.attributes.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAttributesDeleteCall) Fields ¶
func (c *ProjectsLocationsAttributesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAttributesDeleteCall) Header ¶
func (c *ProjectsLocationsAttributesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAttributesGetCall ¶
type ProjectsLocationsAttributesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAttributesGetCall) Context ¶
func (c *ProjectsLocationsAttributesGetCall) Context(ctx context.Context) *ProjectsLocationsAttributesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAttributesGetCall) Do ¶
func (c *ProjectsLocationsAttributesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)

Do executes the "apihub.projects.locations.attributes.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Attribute.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAttributesGetCall) Fields ¶
func (c *ProjectsLocationsAttributesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAttributesGetCall) Header ¶
func (c *ProjectsLocationsAttributesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAttributesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsAttributesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAttributesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAttributesListCall ¶
type ProjectsLocationsAttributesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAttributesListCall) Context ¶
func (c *ProjectsLocationsAttributesListCall) Context(ctx context.Context) *ProjectsLocationsAttributesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAttributesListCall) Do ¶
func (c *ProjectsLocationsAttributesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListAttributesResponse, error)

Do executes the "apihub.projects.locations.attributes.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListAttributesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAttributesListCall) Fields ¶
func (c *ProjectsLocationsAttributesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAttributesListCall) Filter ¶
func (c *ProjectsLocationsAttributesListCall) Filter(filter string) *ProjectsLocationsAttributesListCall

Filter sets the optional parameter "filter": An expression that filters the list of Attributes. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string or a boolean. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `Attribute` are eligible for filtering: * `display_name` - The display name of the Attribute. Allowed comparison operators: `=`. * `definition_type` - The definition type of the attribute. Allowed comparison operators: `=`. * `scope` - The scope of the attribute. Allowed comparison operators: `=`. * `data_type` - The type of the data of the attribute. Allowed comparison operators: `=`. * `mandatory` - Denotes whether the attribute is mandatory or not. Allowed comparison operators: `=`. * `create_time` - The time at which the Attribute was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `display_name = production` - - The display name of the attribute is _production_. * `(display_name = production) AND (create_time < \"2021-08-15T14:50:00Z\") AND (create_time > \"2021-08-10T12:00:00Z\")` - The display name of the attribute is _production_ and the attribute was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `display_name = production OR scope = api` - The attribute where the display name is _production_ or the scope is _api_.

func (*ProjectsLocationsAttributesListCall) Header ¶
func (c *ProjectsLocationsAttributesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAttributesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsAttributesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAttributesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAttributesListCall) PageSize ¶
func (c *ProjectsLocationsAttributesListCall) PageSize(pageSize int64) *ProjectsLocationsAttributesListCall

PageSize sets the optional parameter "pageSize": The maximum number of attribute resources to return. The service may return fewer than this value. If unspecified, at most 50 attributes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsAttributesListCall) PageToken ¶
func (c *ProjectsLocationsAttributesListCall) PageToken(pageToken string) *ProjectsLocationsAttributesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAttributes` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAttributes` must match the call that provided the page token.

func (*ProjectsLocationsAttributesListCall) Pages ¶
func (c *ProjectsLocationsAttributesListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListAttributesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAttributesPatchCall ¶
type ProjectsLocationsAttributesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAttributesPatchCall) Context ¶
func (c *ProjectsLocationsAttributesPatchCall) Context(ctx context.Context) *ProjectsLocationsAttributesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAttributesPatchCall) Do ¶
func (c *ProjectsLocationsAttributesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Attribute, error)

Do executes the "apihub.projects.locations.attributes.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Attribute.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAttributesPatchCall) Fields ¶
func (c *ProjectsLocationsAttributesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAttributesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAttributesPatchCall) Header ¶
func (c *ProjectsLocationsAttributesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAttributesPatchCall) UpdateMask ¶
func (c *ProjectsLocationsAttributesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAttributesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsAttributesService ¶
type ProjectsLocationsAttributesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAttributesService ¶
func NewProjectsLocationsAttributesService(s *Service) *ProjectsLocationsAttributesService
func (*ProjectsLocationsAttributesService) Create ¶
func (r *ProjectsLocationsAttributesService) Create(parent string, googlecloudapihubv1attribute *GoogleCloudApihubV1Attribute) *ProjectsLocationsAttributesCreateCall

Create: Create a user defined attribute. Certain pre defined attributes are already created by the API hub. These attributes will have type as `SYSTEM_DEFINED` and can be listed via ListAttributes method. Allowed values for the same can be updated via UpdateAttribute method.

parent: The parent resource for Attribute. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsAttributesService) Delete ¶
func (r *ProjectsLocationsAttributesService) Delete(name string) *ProjectsLocationsAttributesDeleteCall

Delete: Delete an attribute. Note: System defined attributes cannot be deleted. All associations of the attribute being deleted with any API hub resource will also get deleted.

name: The name of the attribute to delete. Format: `projects/{project}/locations/{location}/attributes/{attribute}`.
func (*ProjectsLocationsAttributesService) Get ¶
func (r *ProjectsLocationsAttributesService) Get(name string) *ProjectsLocationsAttributesGetCall

Get: Get details about the attribute.

name: The name of the attribute to retrieve. Format: `projects/{project}/locations/{location}/attributes/{attribute}`.
func (*ProjectsLocationsAttributesService) List ¶
func (r *ProjectsLocationsAttributesService) List(parent string) *ProjectsLocationsAttributesListCall

List: List all attributes.

parent: The parent resource for Attribute. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsAttributesService) Patch ¶
func (r *ProjectsLocationsAttributesService) Patch(name string, googlecloudapihubv1attribute *GoogleCloudApihubV1Attribute) *ProjectsLocationsAttributesPatchCall

Patch: Update the attribute. The following fields in the Attribute resource can be updated: * display_name The display name can be updated for user defined attributes only. * description The description can be updated for user defined attributes only. * allowed_values To update the list of allowed values, clients need to use the fetched list of allowed values and add or remove values to or from the same list. The mutable allowed values can be updated for both user defined and System defined attributes. The immutable allowed values cannot be updated or deleted. The updated list of allowed values cannot be empty. If an allowed value that is already used by some resource's attribute is deleted, then the association between the resource and the attribute value will also be deleted. * cardinality The cardinality can be updated for user defined attributes only. Cardinality can only be increased during an update. The update_mask should be used to specify the fields being updated.

name: Identifier. The name of the attribute in the API Hub. Format: `projects/{project}/locations/{location}/attributes/{attribute}`.
type ProjectsLocationsCollectApiDataCall ¶
type ProjectsLocationsCollectApiDataCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCollectApiDataCall) Context ¶
func (c *ProjectsLocationsCollectApiDataCall) Context(ctx context.Context) *ProjectsLocationsCollectApiDataCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCollectApiDataCall) Do ¶
func (c *ProjectsLocationsCollectApiDataCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.collectApiData" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCollectApiDataCall) Fields ¶
func (c *ProjectsLocationsCollectApiDataCall) Fields(s ...googleapi.Field) *ProjectsLocationsCollectApiDataCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCollectApiDataCall) Header ¶
func (c *ProjectsLocationsCollectApiDataCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCurationsCreateCall ¶
type ProjectsLocationsCurationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCurationsCreateCall) Context ¶
func (c *ProjectsLocationsCurationsCreateCall) Context(ctx context.Context) *ProjectsLocationsCurationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCurationsCreateCall) CurationId ¶
func (c *ProjectsLocationsCurationsCreateCall) CurationId(curationId string) *ProjectsLocationsCurationsCreateCall

CurationId sets the optional parameter "curationId": The ID to use for the curation resource, which will become the final component of the curations's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified ID is already used by another curation resource in the API hub. * If not provided, a system generated ID will be used. This value should be 4-500 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsCurationsCreateCall) Do ¶
func (c *ProjectsLocationsCurationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)

Do executes the "apihub.projects.locations.curations.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Curation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCurationsCreateCall) Fields ¶
func (c *ProjectsLocationsCurationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCurationsCreateCall) Header ¶
func (c *ProjectsLocationsCurationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCurationsDeleteCall ¶
type ProjectsLocationsCurationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCurationsDeleteCall) Context ¶
func (c *ProjectsLocationsCurationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsCurationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCurationsDeleteCall) Do ¶
func (c *ProjectsLocationsCurationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.curations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCurationsDeleteCall) Fields ¶
func (c *ProjectsLocationsCurationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCurationsDeleteCall) Header ¶
func (c *ProjectsLocationsCurationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCurationsGetCall ¶
type ProjectsLocationsCurationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCurationsGetCall) Context ¶
func (c *ProjectsLocationsCurationsGetCall) Context(ctx context.Context) *ProjectsLocationsCurationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCurationsGetCall) Do ¶
func (c *ProjectsLocationsCurationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)

Do executes the "apihub.projects.locations.curations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Curation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCurationsGetCall) Fields ¶
func (c *ProjectsLocationsCurationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCurationsGetCall) Header ¶
func (c *ProjectsLocationsCurationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsCurationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsCurationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsCurationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsCurationsListCall ¶
type ProjectsLocationsCurationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCurationsListCall) Context ¶
func (c *ProjectsLocationsCurationsListCall) Context(ctx context.Context) *ProjectsLocationsCurationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCurationsListCall) Do ¶
func (c *ProjectsLocationsCurationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListCurationsResponse, error)

Do executes the "apihub.projects.locations.curations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListCurationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCurationsListCall) Fields ¶
func (c *ProjectsLocationsCurationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCurationsListCall) Filter ¶
func (c *ProjectsLocationsCurationsListCall) Filter(filter string) *ProjectsLocationsCurationsListCall

Filter sets the optional parameter "filter": An expression that filters the list of curation resources. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>`, `:` or `=`. Filters are case insensitive. The following fields in the `curation resource` are eligible for filtering: * `create_time` - The time at which the curation was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `display_name` - The display name of the curation. Allowed comparison operators: `=`. * `state` - The state of the curation. Allowed comparison operators: `=`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The curation resource was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_.

func (*ProjectsLocationsCurationsListCall) Header ¶
func (c *ProjectsLocationsCurationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsCurationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsCurationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsCurationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsCurationsListCall) PageSize ¶
func (c *ProjectsLocationsCurationsListCall) PageSize(pageSize int64) *ProjectsLocationsCurationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of curation resources to return. The service may return fewer than this value. If unspecified, at most 50 curations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsCurationsListCall) PageToken ¶
func (c *ProjectsLocationsCurationsListCall) PageToken(pageToken string) *ProjectsLocationsCurationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCurations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListCurations` must match the call that provided the page token.

func (*ProjectsLocationsCurationsListCall) Pages ¶
func (c *ProjectsLocationsCurationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListCurationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsCurationsPatchCall ¶
type ProjectsLocationsCurationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsCurationsPatchCall) Context ¶
func (c *ProjectsLocationsCurationsPatchCall) Context(ctx context.Context) *ProjectsLocationsCurationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsCurationsPatchCall) Do ¶
func (c *ProjectsLocationsCurationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Curation, error)

Do executes the "apihub.projects.locations.curations.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Curation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsCurationsPatchCall) Fields ¶
func (c *ProjectsLocationsCurationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsCurationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsCurationsPatchCall) Header ¶
func (c *ProjectsLocationsCurationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsCurationsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsCurationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsCurationsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsLocationsCurationsService ¶
type ProjectsLocationsCurationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsCurationsService ¶
func NewProjectsLocationsCurationsService(s *Service) *ProjectsLocationsCurationsService
func (*ProjectsLocationsCurationsService) Create ¶
func (r *ProjectsLocationsCurationsService) Create(parent string, googlecloudapihubv1curation *GoogleCloudApihubV1Curation) *ProjectsLocationsCurationsCreateCall

Create: Create a curation resource in the API hub. Once a curation resource is created, plugin instances can start using it.

parent: The parent resource for the curation resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsCurationsService) Delete ¶
func (r *ProjectsLocationsCurationsService) Delete(name string) *ProjectsLocationsCurationsDeleteCall

Delete: Delete a curation resource in the API hub. A curation can only be deleted if it's not being used by any plugin instance.

name: The name of the curation resource to delete. Format: `projects/{project}/locations/{location}/curations/{curation}`.
func (*ProjectsLocationsCurationsService) Get ¶
func (r *ProjectsLocationsCurationsService) Get(name string) *ProjectsLocationsCurationsGetCall

Get: Get curation resource details.

name: The name of the curation resource to retrieve. Format: `projects/{project}/locations/{location}/curations/{curation}`.
func (*ProjectsLocationsCurationsService) List ¶
func (r *ProjectsLocationsCurationsService) List(parent string) *ProjectsLocationsCurationsListCall

List: List curation resources in the API hub.

parent: The parent, which owns this collection of curation resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsCurationsService) Patch ¶
func (r *ProjectsLocationsCurationsService) Patch(name string, googlecloudapihubv1curation *GoogleCloudApihubV1Curation) *ProjectsLocationsCurationsPatchCall

Patch: Update a curation resource in the API hub. The following fields in the curation can be updated: * display_name * description The update_mask should be used to specify the fields being updated.

name: Identifier. The name of the curation. Format: `projects/{project}/locations/{location}/curations/{curation}`.
type ProjectsLocationsDependenciesCreateCall ¶
type ProjectsLocationsDependenciesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDependenciesCreateCall) Context ¶
func (c *ProjectsLocationsDependenciesCreateCall) Context(ctx context.Context) *ProjectsLocationsDependenciesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDependenciesCreateCall) DependencyId ¶
func (c *ProjectsLocationsDependenciesCreateCall) DependencyId(dependencyId string) *ProjectsLocationsDependenciesCreateCall

DependencyId sets the optional parameter "dependencyId": The ID to use for the dependency resource, which will become the final component of the dependency's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if duplicate id is provided by the client. * If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are `a-z[0-9]-_`.

func (*ProjectsLocationsDependenciesCreateCall) Do ¶
func (c *ProjectsLocationsDependenciesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)

Do executes the "apihub.projects.locations.dependencies.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Dependency.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDependenciesCreateCall) Fields ¶
func (c *ProjectsLocationsDependenciesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDependenciesCreateCall) Header ¶
func (c *ProjectsLocationsDependenciesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDependenciesDeleteCall ¶
type ProjectsLocationsDependenciesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDependenciesDeleteCall) Context ¶
func (c *ProjectsLocationsDependenciesDeleteCall) Context(ctx context.Context) *ProjectsLocationsDependenciesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDependenciesDeleteCall) Do ¶
func (c *ProjectsLocationsDependenciesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.dependencies.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDependenciesDeleteCall) Fields ¶
func (c *ProjectsLocationsDependenciesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDependenciesDeleteCall) Header ¶
func (c *ProjectsLocationsDependenciesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDependenciesGetCall ¶
type ProjectsLocationsDependenciesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDependenciesGetCall) Context ¶
func (c *ProjectsLocationsDependenciesGetCall) Context(ctx context.Context) *ProjectsLocationsDependenciesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDependenciesGetCall) Do ¶
func (c *ProjectsLocationsDependenciesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)

Do executes the "apihub.projects.locations.dependencies.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Dependency.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDependenciesGetCall) Fields ¶
func (c *ProjectsLocationsDependenciesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDependenciesGetCall) Header ¶
func (c *ProjectsLocationsDependenciesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDependenciesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsDependenciesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDependenciesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDependenciesListCall ¶
type ProjectsLocationsDependenciesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDependenciesListCall) Context ¶
func (c *ProjectsLocationsDependenciesListCall) Context(ctx context.Context) *ProjectsLocationsDependenciesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDependenciesListCall) Do ¶
func (c *ProjectsLocationsDependenciesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDependenciesResponse, error)

Do executes the "apihub.projects.locations.dependencies.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListDependenciesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDependenciesListCall) Fields ¶
func (c *ProjectsLocationsDependenciesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDependenciesListCall) Filter ¶
func (c *ProjectsLocationsDependenciesListCall) Filter(filter string) *ProjectsLocationsDependenciesListCall

Filter sets the optional parameter "filter": An expression that filters the list of Dependencies. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. Allowed comparison operator is `=`. Filters are not case sensitive. The following fields in the `Dependency` are eligible for filtering: * `consumer.operation_resource_name` - The operation resource name for the consumer entity involved in a dependency. Allowed comparison operators: `=`. * `consumer.external_api_resource_name` - The external api resource name for the consumer entity involved in a dependency. Allowed comparison operators: `=`. * `supplier.operation_resource_name` - The operation resource name for the supplier entity involved in a dependency. Allowed comparison operators: `=`. * `supplier.external_api_resource_name` - The external api resource name for the supplier entity involved in a dependency. Allowed comparison operators: `=`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. For example, `consumer.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\" OR supplier.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\" - The dependencies with either consumer or supplier operation resource name as _projects/p1/locations/global/apis/a1/versions/v1/operations/o1_.

func (*ProjectsLocationsDependenciesListCall) Header ¶
func (c *ProjectsLocationsDependenciesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDependenciesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsDependenciesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDependenciesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDependenciesListCall) PageSize ¶
func (c *ProjectsLocationsDependenciesListCall) PageSize(pageSize int64) *ProjectsLocationsDependenciesListCall

PageSize sets the optional parameter "pageSize": The maximum number of dependency resources to return. The service may return fewer than this value. If unspecified, at most 50 dependencies will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsDependenciesListCall) PageToken ¶
func (c *ProjectsLocationsDependenciesListCall) PageToken(pageToken string) *ProjectsLocationsDependenciesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDependencies` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDependencies` must match the call that provided the page token.

func (*ProjectsLocationsDependenciesListCall) Pages ¶
func (c *ProjectsLocationsDependenciesListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListDependenciesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDependenciesPatchCall ¶
type ProjectsLocationsDependenciesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDependenciesPatchCall) Context ¶
func (c *ProjectsLocationsDependenciesPatchCall) Context(ctx context.Context) *ProjectsLocationsDependenciesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDependenciesPatchCall) Do ¶
func (c *ProjectsLocationsDependenciesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Dependency, error)

Do executes the "apihub.projects.locations.dependencies.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Dependency.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDependenciesPatchCall) Fields ¶
func (c *ProjectsLocationsDependenciesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsDependenciesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDependenciesPatchCall) Header ¶
func (c *ProjectsLocationsDependenciesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDependenciesPatchCall) UpdateMask ¶
func (c *ProjectsLocationsDependenciesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsDependenciesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsDependenciesService ¶
type ProjectsLocationsDependenciesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDependenciesService ¶
func NewProjectsLocationsDependenciesService(s *Service) *ProjectsLocationsDependenciesService
func (*ProjectsLocationsDependenciesService) Create ¶
func (r *ProjectsLocationsDependenciesService) Create(parent string, googlecloudapihubv1dependency *GoogleCloudApihubV1Dependency) *ProjectsLocationsDependenciesCreateCall

Create: Create a dependency between two entities in the API hub.

parent: The parent resource for the dependency resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDependenciesService) Delete ¶
func (r *ProjectsLocationsDependenciesService) Delete(name string) *ProjectsLocationsDependenciesDeleteCall

Delete: Delete the dependency resource.

name: The name of the dependency resource to delete. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`.
func (*ProjectsLocationsDependenciesService) Get ¶
func (r *ProjectsLocationsDependenciesService) Get(name string) *ProjectsLocationsDependenciesGetCall

Get: Get details about a dependency resource in the API hub.

name: The name of the dependency resource to retrieve. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`.
func (*ProjectsLocationsDependenciesService) List ¶
func (r *ProjectsLocationsDependenciesService) List(parent string) *ProjectsLocationsDependenciesListCall

List: List dependencies based on the provided filter and pagination parameters.

parent: The parent which owns this collection of dependency resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDependenciesService) Patch ¶
func (r *ProjectsLocationsDependenciesService) Patch(name string, googlecloudapihubv1dependency *GoogleCloudApihubV1Dependency) *ProjectsLocationsDependenciesPatchCall

Patch: Update a dependency based on the update_mask provided in the request. The following fields in the dependency can be updated: * description

name: Identifier. The name of the dependency in the API Hub. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`.
type ProjectsLocationsDeploymentsCreateCall ¶
type ProjectsLocationsDeploymentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDeploymentsCreateCall) Context ¶
func (c *ProjectsLocationsDeploymentsCreateCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDeploymentsCreateCall) DeploymentId ¶
func (c *ProjectsLocationsDeploymentsCreateCall) DeploymentId(deploymentId string) *ProjectsLocationsDeploymentsCreateCall

DeploymentId sets the optional parameter "deploymentId": The ID to use for the deployment resource, which will become the final component of the deployment's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another deployment resource in the API hub. * If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsDeploymentsCreateCall) Do ¶
func (c *ProjectsLocationsDeploymentsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)

Do executes the "apihub.projects.locations.deployments.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Deployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDeploymentsCreateCall) Fields ¶
func (c *ProjectsLocationsDeploymentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDeploymentsCreateCall) Header ¶
func (c *ProjectsLocationsDeploymentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDeploymentsDeleteCall ¶
type ProjectsLocationsDeploymentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDeploymentsDeleteCall) Context ¶
func (c *ProjectsLocationsDeploymentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDeploymentsDeleteCall) Do ¶
func (c *ProjectsLocationsDeploymentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.deployments.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDeploymentsDeleteCall) Fields ¶
func (c *ProjectsLocationsDeploymentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDeploymentsDeleteCall) Header ¶
func (c *ProjectsLocationsDeploymentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDeploymentsGetCall ¶
type ProjectsLocationsDeploymentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDeploymentsGetCall) Context ¶
func (c *ProjectsLocationsDeploymentsGetCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDeploymentsGetCall) Do ¶
func (c *ProjectsLocationsDeploymentsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)

Do executes the "apihub.projects.locations.deployments.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Deployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDeploymentsGetCall) Fields ¶
func (c *ProjectsLocationsDeploymentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDeploymentsGetCall) Header ¶
func (c *ProjectsLocationsDeploymentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDeploymentsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsDeploymentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDeploymentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDeploymentsListCall ¶
type ProjectsLocationsDeploymentsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDeploymentsListCall) Context ¶
func (c *ProjectsLocationsDeploymentsListCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDeploymentsListCall) Do ¶
func (c *ProjectsLocationsDeploymentsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDeploymentsResponse, error)

Do executes the "apihub.projects.locations.deployments.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListDeploymentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDeploymentsListCall) Fields ¶
func (c *ProjectsLocationsDeploymentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDeploymentsListCall) Filter ¶
func (c *ProjectsLocationsDeploymentsListCall) Filter(filter string) *ProjectsLocationsDeploymentsListCall

Filter sets the optional parameter "filter": An expression that filters the list of Deployments. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `Deployments` are eligible for filtering: * `display_name` - The display name of the Deployment. Allowed comparison operators: `=`. * `create_time` - The time at which the Deployment was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`. * `resource_uri` - A URI to the deployment resource. Allowed comparison operators: `=`. * `api_versions` - The API versions linked to this deployment. Allowed comparison operators: `:`. * `source_project` - The project/organization at source for the deployment. Allowed comparison operators: `=`. * `source_environment` - The environment at source for the deployment. Allowed comparison operators: `=`. * `deployment_type.enum_values.values.id` - The allowed value id of the deployment_type attribute associated with the Deployment. Allowed comparison operators: `:`. * `deployment_type.enum_values.values.display_name` - The allowed value display name of the deployment_type attribute associated with the Deployment. Allowed comparison operators: `:`. * `slo.string_values.values` -The allowed string value of the slo attribute associated with the deployment. Allowed comparison operators: `:`. * `environment.enum_values.values.id` - The allowed value id of the environment attribute associated with the deployment. Allowed comparison operators: `:`. * `environment.enum_values.values.display_name` - The allowed value display name of the environment attribute associated with the deployment. Allowed comparison operators: `:`. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` - The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` - The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` - The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` - The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"deployment-1\" is equivalent to `name = \"projects/test-project-id/locations/test-location-id/deployments/deployment- 1\" provided the parent is `projects/test-project-id/locations/test-location-id`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `environment.enum_values.values.id: staging-id` - The allowed value id of the environment attribute associated with the Deployment is _staging-id_. * `environment.enum_values.values.display_name: \"Staging Deployment\" - The allowed value display name of the environment attribute associated with the Deployment is `Staging Deployment`. * `environment.enum_values.values.id: production-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\" - The allowed value id of the environment attribute associated with the Deployment is _production-id_ and Deployment was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_. * `environment.enum_values.values.id: production-id OR slo.string_values.values: \"99.99%\" - The allowed value id of the environment attribute Deployment is _production-id_ or string value of the slo attribute is _99.99%_. * `environment.enum_values.values.id: staging-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test` - The filter string specifies that the allowed value id of the environment attribute associated with the Deployment is _staging-id_ and the value of the user defined attribute of type string is _test_.

func (*ProjectsLocationsDeploymentsListCall) Header ¶
func (c *ProjectsLocationsDeploymentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDeploymentsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsDeploymentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDeploymentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDeploymentsListCall) PageSize ¶
func (c *ProjectsLocationsDeploymentsListCall) PageSize(pageSize int64) *ProjectsLocationsDeploymentsListCall

PageSize sets the optional parameter "pageSize": The maximum number of deployment resources to return. The service may return fewer than this value. If unspecified, at most 50 deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsDeploymentsListCall) PageToken ¶
func (c *ProjectsLocationsDeploymentsListCall) PageToken(pageToken string) *ProjectsLocationsDeploymentsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDeployments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListDeployments` must match the call that provided the page token.

func (*ProjectsLocationsDeploymentsListCall) Pages ¶
func (c *ProjectsLocationsDeploymentsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListDeploymentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDeploymentsPatchCall ¶
type ProjectsLocationsDeploymentsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDeploymentsPatchCall) Context ¶
func (c *ProjectsLocationsDeploymentsPatchCall) Context(ctx context.Context) *ProjectsLocationsDeploymentsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDeploymentsPatchCall) Do ¶
func (c *ProjectsLocationsDeploymentsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Deployment, error)

Do executes the "apihub.projects.locations.deployments.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Deployment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDeploymentsPatchCall) Fields ¶
func (c *ProjectsLocationsDeploymentsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsDeploymentsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDeploymentsPatchCall) Header ¶
func (c *ProjectsLocationsDeploymentsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDeploymentsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsDeploymentsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsDeploymentsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsDeploymentsService ¶
type ProjectsLocationsDeploymentsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDeploymentsService ¶
func NewProjectsLocationsDeploymentsService(s *Service) *ProjectsLocationsDeploymentsService
func (*ProjectsLocationsDeploymentsService) Create ¶
func (r *ProjectsLocationsDeploymentsService) Create(parent string, googlecloudapihubv1deployment *GoogleCloudApihubV1Deployment) *ProjectsLocationsDeploymentsCreateCall

Create: Create a deployment resource in the API hub. Once a deployment resource is created, it can be associated with API versions.

parent: The parent resource for the deployment resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDeploymentsService) Delete ¶
func (r *ProjectsLocationsDeploymentsService) Delete(name string) *ProjectsLocationsDeploymentsDeleteCall

Delete: Delete a deployment resource in the API hub.

name: The name of the deployment resource to delete. Format: `projects/{project}/locations/{location}/deployments/{deployment}`.
func (*ProjectsLocationsDeploymentsService) Get ¶
func (r *ProjectsLocationsDeploymentsService) Get(name string) *ProjectsLocationsDeploymentsGetCall

Get: Get details about a deployment and the API versions linked to it.

name: The name of the deployment resource to retrieve. Format: `projects/{project}/locations/{location}/deployments/{deployment}`.
func (*ProjectsLocationsDeploymentsService) List ¶
func (r *ProjectsLocationsDeploymentsService) List(parent string) *ProjectsLocationsDeploymentsListCall

List: List deployment resources in the API hub.

parent: The parent, which owns this collection of deployment resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsDeploymentsService) Patch ¶
func (r *ProjectsLocationsDeploymentsService) Patch(name string, googlecloudapihubv1deployment *GoogleCloudApihubV1Deployment) *ProjectsLocationsDeploymentsPatchCall

Patch: Update a deployment resource in the API hub. The following fields in the deployment resource can be updated: * display_name * description * documentation * deployment_type * resource_uri * endpoints * slo * environment * attributes * source_project * source_environment * management_url * source_uri The update_mask should be used to specify the fields being updated.

name: Identifier. The name of the deployment. Format: `projects/{project}/locations/{location}/deployments/{deployment}`.
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Context ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Do ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1DiscoveredApiOperation, error)

Do executes the "apihub.projects.locations.discoveredApiObservations.discoveredApiOperations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1DiscoveredApiOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Fields ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Header ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) IfNoneMatch ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Context ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Do ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDiscoveredApiOperationsResponse, error)

Do executes the "apihub.projects.locations.discoveredApiObservations.discoveredApiOperations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListDiscoveredApiOperationsResponse.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Fields ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Header ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) IfNoneMatch ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageSize ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

PageSize sets the optional parameter "pageSize": DiscoveredApiOperations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageToken ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDiscoveredApiApiOperations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDiscoveredApiApiOperations` must match the call that provided the page token.

func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Pages ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListDiscoveredApiOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService ¶
added in v0.245.0
func NewProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService(s *Service) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService
func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) Get ¶
added in v0.245.0
func (r *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) Get(name string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsGetCall

Get: Gets a DiscoveredAPIOperation in a given project, location, ApiObservation and ApiOperation.

name: The name of the DiscoveredApiOperation to retrieve. Format: projects/{project}/locations/{location}/discoveredApiObservations/{discover ed_api_observation}/discoveredApiOperations/{discovered_api_operation}.
func (*ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) List ¶
added in v0.245.0
func (r *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService) List(parent string) *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsListCall

List: Lists all the DiscoveredAPIOperations in a given project, location and ApiObservation.

parent: The parent, which owns this collection of DiscoveredApiOperations. Format: projects/{project}/locations/{location}/discoveredApiObservations/{discover ed_api_observation}.
type ProjectsLocationsDiscoveredApiObservationsGetCall ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredApiObservationsGetCall) Context ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredApiObservationsGetCall) Do ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1DiscoveredApiObservation, error)

Do executes the "apihub.projects.locations.discoveredApiObservations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1DiscoveredApiObservation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredApiObservationsGetCall) Fields ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredApiObservationsGetCall) Header ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredApiObservationsGetCall) IfNoneMatch ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDiscoveredApiObservationsListCall ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDiscoveredApiObservationsListCall) Context ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Context(ctx context.Context) *ProjectsLocationsDiscoveredApiObservationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) Do ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListDiscoveredApiObservationsResponse, error)

Do executes the "apihub.projects.locations.discoveredApiObservations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListDiscoveredApiObservationsResponse.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) Fields ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDiscoveredApiObservationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) Header ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) IfNoneMatch ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDiscoveredApiObservationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) PageSize ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) PageSize(pageSize int64) *ProjectsLocationsDiscoveredApiObservationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of ApiObservations to return. The service may return fewer than this value. If unspecified, at most 10 ApiObservations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) PageToken ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) PageToken(pageToken string) *ProjectsLocationsDiscoveredApiObservationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiObservations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiObservations` must match the call that provided the page token.

func (*ProjectsLocationsDiscoveredApiObservationsListCall) Pages ¶
added in v0.245.0
func (c *ProjectsLocationsDiscoveredApiObservationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListDiscoveredApiObservationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDiscoveredApiObservationsService ¶
added in v0.245.0
type ProjectsLocationsDiscoveredApiObservationsService struct {
	DiscoveredApiOperations *ProjectsLocationsDiscoveredApiObservationsDiscoveredApiOperationsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsDiscoveredApiObservationsService ¶
added in v0.245.0
func NewProjectsLocationsDiscoveredApiObservationsService(s *Service) *ProjectsLocationsDiscoveredApiObservationsService
func (*ProjectsLocationsDiscoveredApiObservationsService) Get ¶
added in v0.245.0
func (r *ProjectsLocationsDiscoveredApiObservationsService) Get(name string) *ProjectsLocationsDiscoveredApiObservationsGetCall

Get: Gets a DiscoveredAPIObservation in a given project, location and ApiObservation.

name: The name of the DiscoveredApiObservation to retrieve. Format: projects/{project}/locations/{location}/discoveredApiObservations/{discover ed_api_observation}.
func (*ProjectsLocationsDiscoveredApiObservationsService) List ¶
added in v0.245.0
func (r *ProjectsLocationsDiscoveredApiObservationsService) List(parent string) *ProjectsLocationsDiscoveredApiObservationsListCall

List: Lists all the DiscoveredAPIObservations in a given project and location.

parent: The parent, which owns this collection of ApiObservations. Format: projects/{project}/locations/{location}.
type ProjectsLocationsExternalApisCreateCall ¶
type ProjectsLocationsExternalApisCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExternalApisCreateCall) Context ¶
func (c *ProjectsLocationsExternalApisCreateCall) Context(ctx context.Context) *ProjectsLocationsExternalApisCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExternalApisCreateCall) Do ¶
func (c *ProjectsLocationsExternalApisCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)

Do executes the "apihub.projects.locations.externalApis.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ExternalApi.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExternalApisCreateCall) ExternalApiId ¶
func (c *ProjectsLocationsExternalApisCreateCall) ExternalApiId(externalApiId string) *ProjectsLocationsExternalApisCreateCall

ExternalApiId sets the optional parameter "externalApiId": The ID to use for the External API resource, which will become the final component of the External API's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another External API resource in the API hub. * If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /a-z[0-9]-_/.

func (*ProjectsLocationsExternalApisCreateCall) Fields ¶
func (c *ProjectsLocationsExternalApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExternalApisCreateCall) Header ¶
func (c *ProjectsLocationsExternalApisCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsExternalApisDeleteCall ¶
type ProjectsLocationsExternalApisDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExternalApisDeleteCall) Context ¶
func (c *ProjectsLocationsExternalApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsExternalApisDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExternalApisDeleteCall) Do ¶
func (c *ProjectsLocationsExternalApisDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.externalApis.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExternalApisDeleteCall) Fields ¶
func (c *ProjectsLocationsExternalApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExternalApisDeleteCall) Header ¶
func (c *ProjectsLocationsExternalApisDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsExternalApisGetCall ¶
type ProjectsLocationsExternalApisGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExternalApisGetCall) Context ¶
func (c *ProjectsLocationsExternalApisGetCall) Context(ctx context.Context) *ProjectsLocationsExternalApisGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExternalApisGetCall) Do ¶
func (c *ProjectsLocationsExternalApisGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)

Do executes the "apihub.projects.locations.externalApis.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ExternalApi.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExternalApisGetCall) Fields ¶
func (c *ProjectsLocationsExternalApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExternalApisGetCall) Header ¶
func (c *ProjectsLocationsExternalApisGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsExternalApisGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsExternalApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsExternalApisGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsExternalApisListCall ¶
type ProjectsLocationsExternalApisListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExternalApisListCall) Context ¶
func (c *ProjectsLocationsExternalApisListCall) Context(ctx context.Context) *ProjectsLocationsExternalApisListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExternalApisListCall) Do ¶
func (c *ProjectsLocationsExternalApisListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListExternalApisResponse, error)

Do executes the "apihub.projects.locations.externalApis.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListExternalApisResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExternalApisListCall) Fields ¶
func (c *ProjectsLocationsExternalApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExternalApisListCall) Header ¶
func (c *ProjectsLocationsExternalApisListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsExternalApisListCall) IfNoneMatch ¶
func (c *ProjectsLocationsExternalApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsExternalApisListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsExternalApisListCall) PageSize ¶
func (c *ProjectsLocationsExternalApisListCall) PageSize(pageSize int64) *ProjectsLocationsExternalApisListCall

PageSize sets the optional parameter "pageSize": The maximum number of External API resources to return. The service may return fewer than this value. If unspecified, at most 50 ExternalApis will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsExternalApisListCall) PageToken ¶
func (c *ProjectsLocationsExternalApisListCall) PageToken(pageToken string) *ProjectsLocationsExternalApisListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListExternalApis` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListExternalApis` must match the call that provided the page token.

func (*ProjectsLocationsExternalApisListCall) Pages ¶
func (c *ProjectsLocationsExternalApisListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListExternalApisResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsExternalApisPatchCall ¶
type ProjectsLocationsExternalApisPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsExternalApisPatchCall) Context ¶
func (c *ProjectsLocationsExternalApisPatchCall) Context(ctx context.Context) *ProjectsLocationsExternalApisPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsExternalApisPatchCall) Do ¶
func (c *ProjectsLocationsExternalApisPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ExternalApi, error)

Do executes the "apihub.projects.locations.externalApis.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ExternalApi.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsExternalApisPatchCall) Fields ¶
func (c *ProjectsLocationsExternalApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsExternalApisPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsExternalApisPatchCall) Header ¶
func (c *ProjectsLocationsExternalApisPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsExternalApisPatchCall) UpdateMask ¶
func (c *ProjectsLocationsExternalApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsExternalApisPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsExternalApisService ¶
type ProjectsLocationsExternalApisService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsExternalApisService ¶
func NewProjectsLocationsExternalApisService(s *Service) *ProjectsLocationsExternalApisService
func (*ProjectsLocationsExternalApisService) Create ¶
func (r *ProjectsLocationsExternalApisService) Create(parent string, googlecloudapihubv1externalapi *GoogleCloudApihubV1ExternalApi) *ProjectsLocationsExternalApisCreateCall

Create: Create an External API resource in the API hub.

parent: The parent resource for the External API resource. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsExternalApisService) Delete ¶
func (r *ProjectsLocationsExternalApisService) Delete(name string) *ProjectsLocationsExternalApisDeleteCall

Delete: Delete an External API resource in the API hub.

name: The name of the External API resource to delete. Format: `projects/{project}/locations/{location}/externalApis/{externalApi}`.
func (*ProjectsLocationsExternalApisService) Get ¶
func (r *ProjectsLocationsExternalApisService) Get(name string) *ProjectsLocationsExternalApisGetCall

Get: Get details about an External API resource in the API hub.

name: The name of the External API resource to retrieve. Format: `projects/{project}/locations/{location}/externalApis/{externalApi}`.
func (*ProjectsLocationsExternalApisService) List ¶
func (r *ProjectsLocationsExternalApisService) List(parent string) *ProjectsLocationsExternalApisListCall

List: List External API resources in the API hub.

parent: The parent, which owns this collection of External API resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsExternalApisService) Patch ¶
func (r *ProjectsLocationsExternalApisService) Patch(name string, googlecloudapihubv1externalapi *GoogleCloudApihubV1ExternalApi) *ProjectsLocationsExternalApisPatchCall

Patch: Update an External API resource in the API hub. The following fields can be updated: * display_name * description * documentation * endpoints * paths The update_mask should be used to specify the fields being updated.

name: Identifier. Format: `projects/{project}/locations/{location}/externalApi/{externalApi}`.
type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)

Do executes the "apihub.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationLocation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsHostProjectRegistrationsCreateCall ¶
type ProjectsLocationsHostProjectRegistrationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsHostProjectRegistrationsCreateCall) Context ¶
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsHostProjectRegistrationsCreateCall) Do ¶
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1HostProjectRegistration, error)

Do executes the "apihub.projects.locations.hostProjectRegistrations.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1HostProjectRegistration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsHostProjectRegistrationsCreateCall) Fields ¶
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsHostProjectRegistrationsCreateCall) Header ¶
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsHostProjectRegistrationsCreateCall) HostProjectRegistrationId ¶
func (c *ProjectsLocationsHostProjectRegistrationsCreateCall) HostProjectRegistrationId(hostProjectRegistrationId string) *ProjectsLocationsHostProjectRegistrationsCreateCall

HostProjectRegistrationId sets the optional parameter "hostProjectRegistrationId": Required. The ID to use for the Host Project Registration, which will become the final component of the host project registration's resource name. The ID must be the same as the Google cloud project specified in the host_project_registration.gcp_project field.

type ProjectsLocationsHostProjectRegistrationsGetCall ¶
type ProjectsLocationsHostProjectRegistrationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsHostProjectRegistrationsGetCall) Context ¶
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsHostProjectRegistrationsGetCall) Do ¶
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1HostProjectRegistration, error)

Do executes the "apihub.projects.locations.hostProjectRegistrations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1HostProjectRegistration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsHostProjectRegistrationsGetCall) Fields ¶
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsHostProjectRegistrationsGetCall) Header ¶
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsHostProjectRegistrationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsHostProjectRegistrationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsHostProjectRegistrationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsHostProjectRegistrationsListCall ¶
type ProjectsLocationsHostProjectRegistrationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsHostProjectRegistrationsListCall) Context ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Context(ctx context.Context) *ProjectsLocationsHostProjectRegistrationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsHostProjectRegistrationsListCall) Do ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListHostProjectRegistrationsResponse, error)

Do executes the "apihub.projects.locations.hostProjectRegistrations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListHostProjectRegistrationsResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsHostProjectRegistrationsListCall) Fields ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsHostProjectRegistrationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsHostProjectRegistrationsListCall) Filter ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Filter(filter string) *ProjectsLocationsHostProjectRegistrationsListCall

Filter sets the optional parameter "filter": An expression that filters the list of HostProjectRegistrations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. All standard operators as documented at https://google.aip.dev/160 are supported. The following fields in the `HostProjectRegistration` are eligible for filtering: * `name` - The name of the HostProjectRegistration. * `create_time` - The time at which the HostProjectRegistration was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. * `gcp_project` - The Google cloud project associated with the HostProjectRegistration.

func (*ProjectsLocationsHostProjectRegistrationsListCall) Header ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsHostProjectRegistrationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsHostProjectRegistrationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsHostProjectRegistrationsListCall) OrderBy ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) OrderBy(orderBy string) *ProjectsLocationsHostProjectRegistrationsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsHostProjectRegistrationsListCall) PageSize ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) PageSize(pageSize int64) *ProjectsLocationsHostProjectRegistrationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of host project registrations to return. The service may return fewer than this value. If unspecified, at most 50 host project registrations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsHostProjectRegistrationsListCall) PageToken ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) PageToken(pageToken string) *ProjectsLocationsHostProjectRegistrationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListHostProjectRegistrations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListHostProjectRegistrations` must match the call that provided the page token.

func (*ProjectsLocationsHostProjectRegistrationsListCall) Pages ¶
func (c *ProjectsLocationsHostProjectRegistrationsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListHostProjectRegistrationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsHostProjectRegistrationsService ¶
type ProjectsLocationsHostProjectRegistrationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsHostProjectRegistrationsService ¶
func NewProjectsLocationsHostProjectRegistrationsService(s *Service) *ProjectsLocationsHostProjectRegistrationsService
func (*ProjectsLocationsHostProjectRegistrationsService) Create ¶
func (r *ProjectsLocationsHostProjectRegistrationsService) Create(parent string, googlecloudapihubv1hostprojectregistration *GoogleCloudApihubV1HostProjectRegistration) *ProjectsLocationsHostProjectRegistrationsCreateCall

Create: Create a host project registration. A Google cloud project can be registered as a host project if it is not attached as a runtime project to another host project. A project can be registered as a host project only once. Subsequent register calls for the same project will fail.

parent: The parent resource for the host project. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsHostProjectRegistrationsService) Get ¶
func (r *ProjectsLocationsHostProjectRegistrationsService) Get(name string) *ProjectsLocationsHostProjectRegistrationsGetCall

Get: Get a host project registration.

name: Host project registration resource name. projects/{project}/locations/{location}/hostProjectRegistrations/{host_proj ect_registration_id}.
func (*ProjectsLocationsHostProjectRegistrationsService) List ¶
func (r *ProjectsLocationsHostProjectRegistrationsService) List(parent string) *ProjectsLocationsHostProjectRegistrationsListCall

List: Lists host project registrations.

parent: The parent, which owns this collection of host projects. Format: `projects/*/locations/*`.
type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationListLocationsResponse, error)

Do executes the "apihub.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
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

type ProjectsLocationsLookupRuntimeProjectAttachmentCall ¶
type ProjectsLocationsLookupRuntimeProjectAttachmentCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsLookupRuntimeProjectAttachmentCall) Context ¶
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Context(ctx context.Context) *ProjectsLocationsLookupRuntimeProjectAttachmentCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsLookupRuntimeProjectAttachmentCall) Do ¶
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse, error)

Do executes the "apihub.projects.locations.lookupRuntimeProjectAttachment" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse.ServerResponse.Hea der or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsLookupRuntimeProjectAttachmentCall) Fields ¶
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Fields(s ...googleapi.Field) *ProjectsLocationsLookupRuntimeProjectAttachmentCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsLookupRuntimeProjectAttachmentCall) Header ¶
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsLookupRuntimeProjectAttachmentCall) IfNoneMatch ¶
func (c *ProjectsLocationsLookupRuntimeProjectAttachmentCall) IfNoneMatch(entityTag string) *ProjectsLocationsLookupRuntimeProjectAttachmentCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsCancelCall ¶
type ProjectsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsCancelCall) Context ¶
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsCancelCall) Do ¶
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apihub.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apihub.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "apihub.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
added in v0.254.0
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

type ProjectsLocationsPluginsCreateCall ¶
type ProjectsLocationsPluginsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsCreateCall) Context ¶
func (c *ProjectsLocationsPluginsCreateCall) Context(ctx context.Context) *ProjectsLocationsPluginsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsCreateCall) Do ¶
func (c *ProjectsLocationsPluginsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)

Do executes the "apihub.projects.locations.plugins.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Plugin.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsCreateCall) Fields ¶
func (c *ProjectsLocationsPluginsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsCreateCall) Header ¶
func (c *ProjectsLocationsPluginsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsCreateCall) PluginId ¶
func (c *ProjectsLocationsPluginsCreateCall) PluginId(pluginId string) *ProjectsLocationsPluginsCreateCall

PluginId sets the optional parameter "pluginId": The ID to use for the Plugin resource, which will become the final component of the Plugin's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another Plugin resource in the API hub instance. * If not provided, a system generated id will be used. This value should be 4-63 characters, overall resource name which will be of format `projects/{project}/locations/{location}/plugins/{plugin}`, its length is limited to 1000 characters and valid characters are /a-z[0-9]-_/.

type ProjectsLocationsPluginsDeleteCall ¶
type ProjectsLocationsPluginsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsDeleteCall) Context ¶
func (c *ProjectsLocationsPluginsDeleteCall) Context(ctx context.Context) *ProjectsLocationsPluginsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsDeleteCall) Do ¶
func (c *ProjectsLocationsPluginsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsDeleteCall) Fields ¶
func (c *ProjectsLocationsPluginsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsDeleteCall) Header ¶
func (c *ProjectsLocationsPluginsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsDisableCall ¶
type ProjectsLocationsPluginsDisableCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsDisableCall) Context ¶
func (c *ProjectsLocationsPluginsDisableCall) Context(ctx context.Context) *ProjectsLocationsPluginsDisableCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsDisableCall) Do ¶
func (c *ProjectsLocationsPluginsDisableCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)

Do executes the "apihub.projects.locations.plugins.disable" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Plugin.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsDisableCall) Fields ¶
func (c *ProjectsLocationsPluginsDisableCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsDisableCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsDisableCall) Header ¶
func (c *ProjectsLocationsPluginsDisableCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsEnableCall ¶
type ProjectsLocationsPluginsEnableCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsEnableCall) Context ¶
func (c *ProjectsLocationsPluginsEnableCall) Context(ctx context.Context) *ProjectsLocationsPluginsEnableCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsEnableCall) Do ¶
func (c *ProjectsLocationsPluginsEnableCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)

Do executes the "apihub.projects.locations.plugins.enable" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Plugin.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsEnableCall) Fields ¶
func (c *ProjectsLocationsPluginsEnableCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsEnableCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsEnableCall) Header ¶
func (c *ProjectsLocationsPluginsEnableCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsGetCall ¶
type ProjectsLocationsPluginsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsGetCall) Context ¶
func (c *ProjectsLocationsPluginsGetCall) Context(ctx context.Context) *ProjectsLocationsPluginsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsGetCall) Do ¶
func (c *ProjectsLocationsPluginsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1Plugin, error)

Do executes the "apihub.projects.locations.plugins.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1Plugin.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsGetCall) Fields ¶
func (c *ProjectsLocationsPluginsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsGetCall) Header ¶
func (c *ProjectsLocationsPluginsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsPluginsGetStyleGuideCall ¶
type ProjectsLocationsPluginsGetStyleGuideCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsGetStyleGuideCall) Context ¶
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Context(ctx context.Context) *ProjectsLocationsPluginsGetStyleGuideCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsGetStyleGuideCall) Do ¶
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuide, error)

Do executes the "apihub.projects.locations.plugins.getStyleGuide" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1StyleGuide.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsGetStyleGuideCall) Fields ¶
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsGetStyleGuideCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsGetStyleGuideCall) Header ¶
func (c *ProjectsLocationsPluginsGetStyleGuideCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsGetStyleGuideCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsGetStyleGuideCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsGetStyleGuideCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsPluginsInstancesCreateCall ¶
type ProjectsLocationsPluginsInstancesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesCreateCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesCreateCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.instances.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesCreateCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesCreateCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsInstancesCreateCall) PluginInstanceId ¶
func (c *ProjectsLocationsPluginsInstancesCreateCall) PluginInstanceId(pluginInstanceId string) *ProjectsLocationsPluginsInstancesCreateCall

PluginInstanceId sets the optional parameter "pluginInstanceId": The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional. * If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource. * If not provided, a system generated id will be used. This value should be 4-63 characters, and valid characters are /a-z[0-9]-_/.

type ProjectsLocationsPluginsInstancesDeleteCall ¶
type ProjectsLocationsPluginsInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesDeleteCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesDeleteCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesDeleteCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesDeleteCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsInstancesDisableActionCall ¶
type ProjectsLocationsPluginsInstancesDisableActionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesDisableActionCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesDisableActionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesDisableActionCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.instances.disableAction" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesDisableActionCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesDisableActionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesDisableActionCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesDisableActionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsInstancesEnableActionCall ¶
type ProjectsLocationsPluginsInstancesEnableActionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesEnableActionCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesEnableActionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesEnableActionCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.instances.enableAction" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesEnableActionCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesEnableActionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesEnableActionCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesEnableActionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsInstancesExecuteActionCall ¶
type ProjectsLocationsPluginsInstancesExecuteActionCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesExecuteActionCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesExecuteActionCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesExecuteActionCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "apihub.projects.locations.plugins.instances.executeAction" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesExecuteActionCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesExecuteActionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesExecuteActionCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesExecuteActionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsInstancesGetCall ¶
type ProjectsLocationsPluginsInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesGetCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesGetCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1PluginInstance, error)

Do executes the "apihub.projects.locations.plugins.instances.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1PluginInstance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesGetCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesGetCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsPluginsInstancesListCall ¶
type ProjectsLocationsPluginsInstancesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesListCall) Context ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesListCall) Do ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListPluginInstancesResponse, error)

Do executes the "apihub.projects.locations.plugins.instances.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListPluginInstancesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesListCall) Fields ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesListCall) Filter ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Filter(filter string) *ProjectsLocationsPluginsInstancesListCall

Filter sets the optional parameter "filter": An expression that filters the list of plugin instances. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `PluginInstances` are eligible for filtering: * `state` - The state of the Plugin Instance. Allowed comparison operators: `=`. * `source_project_id` - The source project id of the Plugin Instance. Allowed comparison operators: `=`. A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"plugin-instance-1\" is equivalent to `name = \"projects/test-project-id/locations/test-location-id/plugins/plugin-1/instan ces/plugin-instance-1\" provided the parent is `projects/test-project-id/locations/test-location-id/plugins/plugin-1`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `state = ENABLED` - The plugin instance is in enabled state.

func (*ProjectsLocationsPluginsInstancesListCall) Header ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsInstancesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsInstancesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsPluginsInstancesListCall) PageSize ¶
func (c *ProjectsLocationsPluginsInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsPluginsInstancesListCall

PageSize sets the optional parameter "pageSize": The maximum number of hub plugins to return. The service may return fewer than this value. If unspecified, at most 50 hub plugins will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsPluginsInstancesListCall) PageToken ¶
func (c *ProjectsLocationsPluginsInstancesListCall) PageToken(pageToken string) *ProjectsLocationsPluginsInstancesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListPluginInstances` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPluginInstances` must match the call that provided the page token.

func (*ProjectsLocationsPluginsInstancesListCall) Pages ¶
func (c *ProjectsLocationsPluginsInstancesListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListPluginInstancesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsPluginsInstancesManageSourceDataCall ¶
added in v0.250.0
type ProjectsLocationsPluginsInstancesManageSourceDataCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesManageSourceDataCall) Context ¶
added in v0.250.0
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesManageSourceDataCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesManageSourceDataCall) Do ¶
added in v0.250.0
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse, error)

Do executes the "apihub.projects.locations.plugins.instances.manageSourceData" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse.ServerResponse.Hea der or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesManageSourceDataCall) Fields ¶
added in v0.250.0
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesManageSourceDataCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesManageSourceDataCall) Header ¶
added in v0.250.0
func (c *ProjectsLocationsPluginsInstancesManageSourceDataCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsPluginsInstancesPatchCall ¶
added in v0.241.0
type ProjectsLocationsPluginsInstancesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsInstancesPatchCall) Context ¶
added in v0.241.0
func (c *ProjectsLocationsPluginsInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsPluginsInstancesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsInstancesPatchCall) Do ¶
added in v0.241.0
func (c *ProjectsLocationsPluginsInstancesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1PluginInstance, error)

Do executes the "apihub.projects.locations.plugins.instances.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1PluginInstance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsInstancesPatchCall) Fields ¶
added in v0.241.0
func (c *ProjectsLocationsPluginsInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsInstancesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsInstancesPatchCall) Header ¶
added in v0.241.0
func (c *ProjectsLocationsPluginsInstancesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsInstancesPatchCall) UpdateMask ¶
added in v0.241.0
func (c *ProjectsLocationsPluginsInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsPluginsInstancesPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsLocationsPluginsInstancesService ¶
type ProjectsLocationsPluginsInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsPluginsInstancesService ¶
func NewProjectsLocationsPluginsInstancesService(s *Service) *ProjectsLocationsPluginsInstancesService
func (*ProjectsLocationsPluginsInstancesService) Create ¶
func (r *ProjectsLocationsPluginsInstancesService) Create(parent string, googlecloudapihubv1plugininstance *GoogleCloudApihubV1PluginInstance) *ProjectsLocationsPluginsInstancesCreateCall

Create: Creates a Plugin instance in the API hub.

parent: The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.
func (*ProjectsLocationsPluginsInstancesService) Delete ¶
func (r *ProjectsLocationsPluginsInstancesService) Delete(name string) *ProjectsLocationsPluginsInstancesDeleteCall

Delete: Deletes a plugin instance in the API hub.

name: The name of the plugin instance to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) DisableAction ¶
func (r *ProjectsLocationsPluginsInstancesService) DisableAction(name string, googlecloudapihubv1disableplugininstanceactionrequest *GoogleCloudApihubV1DisablePluginInstanceActionRequest) *ProjectsLocationsPluginsInstancesDisableActionCall

DisableAction: Disables a plugin instance in the API hub.

name: The name of the plugin instance to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) EnableAction ¶
func (r *ProjectsLocationsPluginsInstancesService) EnableAction(name string, googlecloudapihubv1enableplugininstanceactionrequest *GoogleCloudApihubV1EnablePluginInstanceActionRequest) *ProjectsLocationsPluginsInstancesEnableActionCall

EnableAction: Enables a plugin instance in the API hub.

name: The name of the plugin instance to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) ExecuteAction ¶
func (r *ProjectsLocationsPluginsInstancesService) ExecuteAction(name string, googlecloudapihubv1executeplugininstanceactionrequest *GoogleCloudApihubV1ExecutePluginInstanceActionRequest) *ProjectsLocationsPluginsInstancesExecuteActionCall

ExecuteAction: Executes a plugin instance in the API hub.

name: The name of the plugin instance to execute. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) Get ¶
func (r *ProjectsLocationsPluginsInstancesService) Get(name string) *ProjectsLocationsPluginsInstancesGetCall

Get: Get an API Hub plugin instance.

name: The name of the plugin instance to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) List ¶
func (r *ProjectsLocationsPluginsInstancesService) List(parent string) *ProjectsLocationsPluginsInstancesListCall

List: List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

parent: The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. To list plugin instances for multiple plugins, use the - character instead of the plugin ID.
func (*ProjectsLocationsPluginsInstancesService) ManageSourceData ¶
added in v0.250.0
func (r *ProjectsLocationsPluginsInstancesService) ManageSourceData(name string, googlecloudapihubv1manageplugininstancesourcedatarequest *GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest) *ProjectsLocationsPluginsInstancesManageSourceDataCall

ManageSourceData: Manages data for a given plugin instance.

name: The name of the plugin instance for which data needs to be managed. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
func (*ProjectsLocationsPluginsInstancesService) Patch ¶
added in v0.241.0
func (r *ProjectsLocationsPluginsInstancesService) Patch(name string, googlecloudapihubv1plugininstance *GoogleCloudApihubV1PluginInstance) *ProjectsLocationsPluginsInstancesPatchCall

Patch: Updates a plugin instance in the API hub. The following fields in the plugin_instance can be updated currently: * display_name * schedule_cron_expression The update_mask should be used to specify the fields being updated. To update the auth_config and additional_config of the plugin instance, use the ApplyPluginInstanceConfig method.

name: Identifier. The unique name of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instan ce}`.
type ProjectsLocationsPluginsListCall ¶
type ProjectsLocationsPluginsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsListCall) Context ¶
func (c *ProjectsLocationsPluginsListCall) Context(ctx context.Context) *ProjectsLocationsPluginsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsListCall) Do ¶
func (c *ProjectsLocationsPluginsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListPluginsResponse, error)

Do executes the "apihub.projects.locations.plugins.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListPluginsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsListCall) Fields ¶
func (c *ProjectsLocationsPluginsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsListCall) Filter ¶
func (c *ProjectsLocationsPluginsListCall) Filter(filter string) *ProjectsLocationsPluginsListCall

Filter sets the optional parameter "filter": An expression that filters the list of plugins. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive. The following fields in the `Plugins` are eligible for filtering: * `plugin_category` - The category of the Plugin. Allowed comparison operators: `=`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: * `plugin_category = ON_RAMP` - The plugin is of category on ramp.

func (*ProjectsLocationsPluginsListCall) Header ¶
func (c *ProjectsLocationsPluginsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsPluginsListCall) PageSize ¶
func (c *ProjectsLocationsPluginsListCall) PageSize(pageSize int64) *ProjectsLocationsPluginsListCall

PageSize sets the optional parameter "pageSize": The maximum number of hub plugins to return. The service may return fewer than this value. If unspecified, at most 50 hub plugins will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsPluginsListCall) PageToken ¶
func (c *ProjectsLocationsPluginsListCall) PageToken(pageToken string) *ProjectsLocationsPluginsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListPlugins` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListPlugins` must match the call that provided the page token.

func (*ProjectsLocationsPluginsListCall) Pages ¶
func (c *ProjectsLocationsPluginsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListPluginsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsPluginsService ¶
type ProjectsLocationsPluginsService struct {
	Instances *ProjectsLocationsPluginsInstancesService

	StyleGuide *ProjectsLocationsPluginsStyleGuideService
	// contains filtered or unexported fields
}
func NewProjectsLocationsPluginsService ¶
func NewProjectsLocationsPluginsService(s *Service) *ProjectsLocationsPluginsService
func (*ProjectsLocationsPluginsService) Create ¶
func (r *ProjectsLocationsPluginsService) Create(parent string, googlecloudapihubv1plugin *GoogleCloudApihubV1Plugin) *ProjectsLocationsPluginsCreateCall

Create: Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

parent: The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsPluginsService) Delete ¶
func (r *ProjectsLocationsPluginsService) Delete(name string) *ProjectsLocationsPluginsDeleteCall

Delete: Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

name: The name of the Plugin resource to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.
func (*ProjectsLocationsPluginsService) Disable ¶
func (r *ProjectsLocationsPluginsService) Disable(name string, googlecloudapihubv1disablepluginrequest *GoogleCloudApihubV1DisablePluginRequest) *ProjectsLocationsPluginsDisableCall

Disable: Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

name: The name of the plugin to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.
func (*ProjectsLocationsPluginsService) Enable ¶
func (r *ProjectsLocationsPluginsService) Enable(name string, googlecloudapihubv1enablepluginrequest *GoogleCloudApihubV1EnablePluginRequest) *ProjectsLocationsPluginsEnableCall

Enable: Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

name: The name of the plugin to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.
func (*ProjectsLocationsPluginsService) Get ¶
func (r *ProjectsLocationsPluginsService) Get(name string) *ProjectsLocationsPluginsGetCall

Get: Get an API Hub plugin.

name: The name of the plugin to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.
func (*ProjectsLocationsPluginsService) GetStyleGuide ¶
func (r *ProjectsLocationsPluginsService) GetStyleGuide(name string) *ProjectsLocationsPluginsGetStyleGuideCall

GetStyleGuide: Get the style guide being used for linting.

name: The name of the spec to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}/styleGuide`.
func (*ProjectsLocationsPluginsService) List ¶
func (r *ProjectsLocationsPluginsService) List(parent string) *ProjectsLocationsPluginsListCall

List: List all the plugins in a given project and location.

parent: The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsPluginsService) UpdateStyleGuide ¶
func (r *ProjectsLocationsPluginsService) UpdateStyleGuide(name string, googlecloudapihubv1styleguide *GoogleCloudApihubV1StyleGuide) *ProjectsLocationsPluginsUpdateStyleGuideCall

UpdateStyleGuide: Update the styleGuide to be used for liniting in by API hub.

name: Identifier. The name of the style guide. Format: `projects/{project}/locations/{location}/plugins/{plugin}/styleGuide`.
type ProjectsLocationsPluginsStyleGuideGetContentsCall ¶
type ProjectsLocationsPluginsStyleGuideGetContentsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsStyleGuideGetContentsCall) Context ¶
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Context(ctx context.Context) *ProjectsLocationsPluginsStyleGuideGetContentsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsStyleGuideGetContentsCall) Do ¶
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuideContents, error)

Do executes the "apihub.projects.locations.plugins.styleGuide.getContents" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1StyleGuideContents.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsStyleGuideGetContentsCall) Fields ¶
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsStyleGuideGetContentsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsStyleGuideGetContentsCall) Header ¶
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsStyleGuideGetContentsCall) IfNoneMatch ¶
func (c *ProjectsLocationsPluginsStyleGuideGetContentsCall) IfNoneMatch(entityTag string) *ProjectsLocationsPluginsStyleGuideGetContentsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsPluginsStyleGuideService ¶
type ProjectsLocationsPluginsStyleGuideService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsPluginsStyleGuideService ¶
func NewProjectsLocationsPluginsStyleGuideService(s *Service) *ProjectsLocationsPluginsStyleGuideService
func (*ProjectsLocationsPluginsStyleGuideService) GetContents ¶
func (r *ProjectsLocationsPluginsStyleGuideService) GetContents(name string) *ProjectsLocationsPluginsStyleGuideGetContentsCall

GetContents: Get the contents of the style guide.

name: The name of the StyleGuide whose contents need to be retrieved. There is exactly one style guide resource per project per location. The expected format is `projects/{project}/locations/{location}/plugins/{plugin}/styleGuide`.
type ProjectsLocationsPluginsUpdateStyleGuideCall ¶
type ProjectsLocationsPluginsUpdateStyleGuideCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsPluginsUpdateStyleGuideCall) Context ¶
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Context(ctx context.Context) *ProjectsLocationsPluginsUpdateStyleGuideCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsPluginsUpdateStyleGuideCall) Do ¶
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1StyleGuide, error)

Do executes the "apihub.projects.locations.plugins.updateStyleGuide" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1StyleGuide.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsPluginsUpdateStyleGuideCall) Fields ¶
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Fields(s ...googleapi.Field) *ProjectsLocationsPluginsUpdateStyleGuideCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsPluginsUpdateStyleGuideCall) Header ¶
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsPluginsUpdateStyleGuideCall) UpdateMask ¶
func (c *ProjectsLocationsPluginsUpdateStyleGuideCall) UpdateMask(updateMask string) *ProjectsLocationsPluginsUpdateStyleGuideCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsLocationsRetrieveApiViewsCall ¶
added in v0.258.0
type ProjectsLocationsRetrieveApiViewsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRetrieveApiViewsCall) Context ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Context(ctx context.Context) *ProjectsLocationsRetrieveApiViewsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRetrieveApiViewsCall) Do ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RetrieveApiViewsResponse, error)

Do executes the "apihub.projects.locations.retrieveApiViews" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1RetrieveApiViewsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRetrieveApiViewsCall) Fields ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Fields(s ...googleapi.Field) *ProjectsLocationsRetrieveApiViewsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRetrieveApiViewsCall) Filter ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Filter(filter string) *ProjectsLocationsRetrieveApiViewsCall

Filter sets the optional parameter "filter": The filter expression.

func (*ProjectsLocationsRetrieveApiViewsCall) Header ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRetrieveApiViewsCall) IfNoneMatch ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) IfNoneMatch(entityTag string) *ProjectsLocationsRetrieveApiViewsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRetrieveApiViewsCall) PageSize ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) PageSize(pageSize int64) *ProjectsLocationsRetrieveApiViewsCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. Default to 100.

func (*ProjectsLocationsRetrieveApiViewsCall) PageToken ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) PageToken(pageToken string) *ProjectsLocationsRetrieveApiViewsCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `RetrieveApiViews` call. Provide this to retrieve the subsequent page.

func (*ProjectsLocationsRetrieveApiViewsCall) Pages ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1RetrieveApiViewsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsRetrieveApiViewsCall) View ¶
added in v0.258.0
func (c *ProjectsLocationsRetrieveApiViewsCall) View(view string) *ProjectsLocationsRetrieveApiViewsCall

View sets the optional parameter "view": Required. The view type to return.

Possible values:

"API_VIEW_TYPE_UNSPECIFIED" - The default view type.
"MCP_SERVER" - The MCP server view in API hub.
"MCP_TOOL" - The MCP tool view in API hub.

type ProjectsLocationsRuntimeProjectAttachmentsCreateCall ¶
type ProjectsLocationsRuntimeProjectAttachmentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Context ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Do ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RuntimeProjectAttachment, error)

Do executes the "apihub.projects.locations.runtimeProjectAttachments.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1RuntimeProjectAttachment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Fields ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Header ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRuntimeProjectAttachmentsCreateCall) RuntimeProjectAttachmentId ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsCreateCall) RuntimeProjectAttachmentId(runtimeProjectAttachmentId string) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall

RuntimeProjectAttachmentId sets the optional parameter "runtimeProjectAttachmentId": Required. The ID to use for the Runtime Project Attachment, which will become the final component of the Runtime Project Attachment's name. The ID must be the same as the project ID of the Google cloud project specified in the runtime_project_attachment.runtime_project field.

type ProjectsLocationsRuntimeProjectAttachmentsDeleteCall ¶
type ProjectsLocationsRuntimeProjectAttachmentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Context ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Do ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "apihub.projects.locations.runtimeProjectAttachments.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Fields ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Header ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsRuntimeProjectAttachmentsGetCall ¶
type ProjectsLocationsRuntimeProjectAttachmentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeProjectAttachmentsGetCall) Context ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeProjectAttachmentsGetCall) Do ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1RuntimeProjectAttachment, error)

Do executes the "apihub.projects.locations.runtimeProjectAttachments.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1RuntimeProjectAttachment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeProjectAttachmentsGetCall) Fields ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeProjectAttachmentsGetCall) Header ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRuntimeProjectAttachmentsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeProjectAttachmentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsRuntimeProjectAttachmentsListCall ¶
type ProjectsLocationsRuntimeProjectAttachmentsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Context ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Context(ctx context.Context) *ProjectsLocationsRuntimeProjectAttachmentsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Do ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse, error)

Do executes the "apihub.projects.locations.runtimeProjectAttachments.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Fields ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsRuntimeProjectAttachmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Filter ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Filter(filter string) *ProjectsLocationsRuntimeProjectAttachmentsListCall

Filter sets the optional parameter "filter": An expression that filters the list of RuntimeProjectAttachments. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. All standard operators as documented at https://google.aip.dev/160 are supported. The following fields in the `RuntimeProjectAttachment` are eligible for filtering: * `name` - The name of the RuntimeProjectAttachment. * `create_time` - The time at which the RuntimeProjectAttachment was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. * `runtime_project` - The Google cloud project associated with the RuntimeProjectAttachment.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Header ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsRuntimeProjectAttachmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) OrderBy ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) OrderBy(orderBy string) *ProjectsLocationsRuntimeProjectAttachmentsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) PageSize ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) PageSize(pageSize int64) *ProjectsLocationsRuntimeProjectAttachmentsListCall

PageSize sets the optional parameter "pageSize": The maximum number of runtime project attachments to return. The service may return fewer than this value. If unspecified, at most 50 runtime project attachments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) PageToken ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) PageToken(pageToken string) *ProjectsLocationsRuntimeProjectAttachmentsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListRuntimeProjectAttachments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListRuntimeProjectAttachments` must match the call that provided the page token.

func (*ProjectsLocationsRuntimeProjectAttachmentsListCall) Pages ¶
func (c *ProjectsLocationsRuntimeProjectAttachmentsListCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsRuntimeProjectAttachmentsService ¶
type ProjectsLocationsRuntimeProjectAttachmentsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsRuntimeProjectAttachmentsService ¶
func NewProjectsLocationsRuntimeProjectAttachmentsService(s *Service) *ProjectsLocationsRuntimeProjectAttachmentsService
func (*ProjectsLocationsRuntimeProjectAttachmentsService) Create ¶
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Create(parent string, googlecloudapihubv1runtimeprojectattachment *GoogleCloudApihubV1RuntimeProjectAttachment) *ProjectsLocationsRuntimeProjectAttachmentsCreateCall

Create: Attaches a runtime project to the host project.

parent: The parent resource for the Runtime Project Attachment. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsRuntimeProjectAttachmentsService) Delete ¶
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Delete(name string) *ProjectsLocationsRuntimeProjectAttachmentsDeleteCall

Delete: Delete a runtime project attachment in the API Hub. This call will detach the runtime project from the host project.

name: The name of the Runtime Project Attachment to delete. Format: `projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime _project_attachment}`.
func (*ProjectsLocationsRuntimeProjectAttachmentsService) Get ¶
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) Get(name string) *ProjectsLocationsRuntimeProjectAttachmentsGetCall

Get: Gets a runtime project attachment.

name: The name of the API resource to retrieve. Format: `projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime _project_attachment}`.
func (*ProjectsLocationsRuntimeProjectAttachmentsService) List ¶
func (r *ProjectsLocationsRuntimeProjectAttachmentsService) List(parent string) *ProjectsLocationsRuntimeProjectAttachmentsListCall

List: List runtime projects attached to the host project.

parent: The parent, which owns this collection of runtime project attachments. Format: `projects/{project}/locations/{location}`.
type ProjectsLocationsSearchResourcesCall ¶
type ProjectsLocationsSearchResourcesCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSearchResourcesCall) Context ¶
func (c *ProjectsLocationsSearchResourcesCall) Context(ctx context.Context) *ProjectsLocationsSearchResourcesCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSearchResourcesCall) Do ¶
func (c *ProjectsLocationsSearchResourcesCall) Do(opts ...googleapi.CallOption) (*GoogleCloudApihubV1SearchResourcesResponse, error)

Do executes the "apihub.projects.locations.searchResources" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudApihubV1SearchResourcesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSearchResourcesCall) Fields ¶
func (c *ProjectsLocationsSearchResourcesCall) Fields(s ...googleapi.Field) *ProjectsLocationsSearchResourcesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSearchResourcesCall) Header ¶
func (c *ProjectsLocationsSearchResourcesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSearchResourcesCall) Pages ¶
func (c *ProjectsLocationsSearchResourcesCall) Pages(ctx context.Context, f func(*GoogleCloudApihubV1SearchResourcesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	Addons *ProjectsLocationsAddonsService

	ApiHubInstances *ProjectsLocationsApiHubInstancesService

	Apis *ProjectsLocationsApisService

	Attributes *ProjectsLocationsAttributesService

	Curations *ProjectsLocationsCurationsService

	Dependencies *ProjectsLocationsDependenciesService

	Deployments *ProjectsLocationsDeploymentsService

	DiscoveredApiObservations *ProjectsLocationsDiscoveredApiObservationsService

	ExternalApis *ProjectsLocationsExternalApisService

	HostProjectRegistrations *ProjectsLocationsHostProjectRegistrationsService

	Operations *ProjectsLocationsOperationsService

	Plugins *ProjectsLocationsPluginsService

	RuntimeProjectAttachments *ProjectsLocationsRuntimeProjectAttachmentsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) CollectApiData ¶
func (r *ProjectsLocationsService) CollectApiData(location string, googlecloudapihubv1collectapidatarequest *GoogleCloudApihubV1CollectApiDataRequest) *ProjectsLocationsCollectApiDataCall

CollectApiData: Collect API data from a source and push it to Hub's collect layer.

location: The regional location of the API hub instance and its resources. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsService) Get ¶
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) List ¶
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

func (*ProjectsLocationsService) LookupRuntimeProjectAttachment ¶
func (r *ProjectsLocationsService) LookupRuntimeProjectAttachment(name string) *ProjectsLocationsLookupRuntimeProjectAttachmentCall

LookupRuntimeProjectAttachment: Look up a runtime project attachment. This API can be called in the context of any project.

name: Runtime project ID to look up runtime project attachment for. Lookup happens across all regions. Expected format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsService) RetrieveApiViews ¶
added in v0.258.0
func (r *ProjectsLocationsService) RetrieveApiViews(parent string) *ProjectsLocationsRetrieveApiViewsCall

RetrieveApiViews: Retrieve API views.

parent: The parent resource name. Format: `projects/{project}/locations/{location}`.
func (*ProjectsLocationsService) SearchResources ¶
func (r *ProjectsLocationsService) SearchResources(location string, googlecloudapihubv1searchresourcesrequest *GoogleCloudApihubV1SearchResourcesRequest) *ProjectsLocationsSearchResourcesCall

SearchResources: Search across API-Hub resources.

location: The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched.
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

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

 Source Files ¶
View all Source files
apihub-gen.go
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
