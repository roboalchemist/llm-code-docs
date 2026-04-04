# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/bigtableadmin/v2

Title: bigtableadmin package - google.golang.org/api/bigtableadmin/v2 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/bigtableadmin/v2

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
bigtableadmin
 
v2
bigtableadmin
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 30
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

Package bigtableadmin provides access to the Cloud Bigtable Admin API.

For product documentation, see: https://cloud.google.com/bigtable/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/bigtableadmin/v2"
...
ctx := context.Background()
bigtableadminService, err := bigtableadmin.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

bigtableadminService, err := bigtableadmin.NewService(ctx, option.WithScopes(bigtableadmin.CloudPlatformReadOnlyScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

bigtableadminService, err := bigtableadmin.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
bigtableadminService, err := bigtableadmin.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AppProfile
func (s AppProfile) MarshalJSON() ([]byte, error)
type AuditConfig
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type AuthorizedView
func (s AuthorizedView) MarshalJSON() ([]byte, error)
type AutomatedBackupPolicy
func (s AutomatedBackupPolicy) MarshalJSON() ([]byte, error)
type AutoscalingLimits
func (s AutoscalingLimits) MarshalJSON() ([]byte, error)
type AutoscalingTargets
func (s AutoscalingTargets) MarshalJSON() ([]byte, error)
type Backup
func (s Backup) MarshalJSON() ([]byte, error)
type BackupInfo
func (s BackupInfo) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type ChangeStreamConfig
func (s ChangeStreamConfig) MarshalJSON() ([]byte, error)
type CheckConsistencyRequest
func (s CheckConsistencyRequest) MarshalJSON() ([]byte, error)
type CheckConsistencyResponse
func (s CheckConsistencyResponse) MarshalJSON() ([]byte, error)
type Cluster
func (s Cluster) MarshalJSON() ([]byte, error)
type ClusterAutoscalingConfig
func (s ClusterAutoscalingConfig) MarshalJSON() ([]byte, error)
type ClusterConfig
func (s ClusterConfig) MarshalJSON() ([]byte, error)
type ClusterState
func (s ClusterState) MarshalJSON() ([]byte, error)
type ColumnFamily
func (s ColumnFamily) MarshalJSON() ([]byte, error)
type ColumnFamilyStats
func (s ColumnFamilyStats) MarshalJSON() ([]byte, error)
func (s *ColumnFamilyStats) UnmarshalJSON(data []byte) error
type CopyBackupMetadata
func (s CopyBackupMetadata) MarshalJSON() ([]byte, error)
type CopyBackupRequest
func (s CopyBackupRequest) MarshalJSON() ([]byte, error)
type CreateAuthorizedViewMetadata
func (s CreateAuthorizedViewMetadata) MarshalJSON() ([]byte, error)
type CreateAuthorizedViewRequest
func (s CreateAuthorizedViewRequest) MarshalJSON() ([]byte, error)
type CreateBackupMetadata
func (s CreateBackupMetadata) MarshalJSON() ([]byte, error)
type CreateClusterMetadata
func (s CreateClusterMetadata) MarshalJSON() ([]byte, error)
type CreateClusterRequest
func (s CreateClusterRequest) MarshalJSON() ([]byte, error)
type CreateInstanceMetadata
func (s CreateInstanceMetadata) MarshalJSON() ([]byte, error)
type CreateInstanceRequest
func (s CreateInstanceRequest) MarshalJSON() ([]byte, error)
type CreateLogicalViewMetadata
func (s CreateLogicalViewMetadata) MarshalJSON() ([]byte, error)
type CreateLogicalViewRequest
func (s CreateLogicalViewRequest) MarshalJSON() ([]byte, error)
type CreateMaterializedViewMetadata
func (s CreateMaterializedViewMetadata) MarshalJSON() ([]byte, error)
type CreateMaterializedViewRequest
func (s CreateMaterializedViewRequest) MarshalJSON() ([]byte, error)
type CreateSchemaBundleMetadata
func (s CreateSchemaBundleMetadata) MarshalJSON() ([]byte, error)
type CreateTableRequest
func (s CreateTableRequest) MarshalJSON() ([]byte, error)
type DataBoostIsolationReadOnly
func (s DataBoostIsolationReadOnly) MarshalJSON() ([]byte, error)
type DataBoostReadLocalWrites
type DropRowRangeRequest
func (s DropRowRangeRequest) MarshalJSON() ([]byte, error)
type Empty
type EncryptionConfig
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EncryptionInfo
func (s EncryptionInfo) MarshalJSON() ([]byte, error)
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type GcRule
func (s GcRule) MarshalJSON() ([]byte, error)
type GenerateConsistencyTokenRequest
type GenerateConsistencyTokenResponse
func (s GenerateConsistencyTokenResponse) MarshalJSON() ([]byte, error)
type GetIamPolicyRequest
func (s GetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GetPolicyOptions
func (s GetPolicyOptions) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2AuthorizedViewFamilySubsets
func (s GoogleBigtableAdminV2AuthorizedViewFamilySubsets) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2AuthorizedViewSubsetView
func (s GoogleBigtableAdminV2AuthorizedViewSubsetView) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2MaterializedViewClusterState
func (s GoogleBigtableAdminV2MaterializedViewClusterState) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeAggregate
func (s GoogleBigtableAdminV2TypeAggregate) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount
type GoogleBigtableAdminV2TypeAggregateMax
type GoogleBigtableAdminV2TypeAggregateMin
type GoogleBigtableAdminV2TypeAggregateSum
type GoogleBigtableAdminV2TypeArray
func (s GoogleBigtableAdminV2TypeArray) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBool
type GoogleBigtableAdminV2TypeBytes
func (s GoogleBigtableAdminV2TypeBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBytesEncoding
func (s GoogleBigtableAdminV2TypeBytesEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBytesEncodingRaw
func (s GoogleBigtableAdminV2TypeBytesEncodingRaw) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeDate
type GoogleBigtableAdminV2TypeEnum
func (s GoogleBigtableAdminV2TypeEnum) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeFloat32
type GoogleBigtableAdminV2TypeFloat64
type GoogleBigtableAdminV2TypeGeography
type GoogleBigtableAdminV2TypeInt64
func (s GoogleBigtableAdminV2TypeInt64) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64Encoding
func (s GoogleBigtableAdminV2TypeInt64Encoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes
func (s GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes
type GoogleBigtableAdminV2TypeMap
func (s GoogleBigtableAdminV2TypeMap) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeProto
func (s GoogleBigtableAdminV2TypeProto) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeString
func (s GoogleBigtableAdminV2TypeString) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncoding
func (s GoogleBigtableAdminV2TypeStringEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes
func (s GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncodingUtf8Raw
type GoogleBigtableAdminV2TypeStruct
func (s GoogleBigtableAdminV2TypeStruct) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncoding
func (s GoogleBigtableAdminV2TypeStructEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes
func (s GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes
type GoogleBigtableAdminV2TypeStructEncodingSingleton
type GoogleBigtableAdminV2TypeStructField
func (s GoogleBigtableAdminV2TypeStructField) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeTimestamp
func (s GoogleBigtableAdminV2TypeTimestamp) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeTimestampEncoding
func (s GoogleBigtableAdminV2TypeTimestampEncoding) MarshalJSON() ([]byte, error)
type HotTablet
func (s HotTablet) MarshalJSON() ([]byte, error)
func (s *HotTablet) UnmarshalJSON(data []byte) error
type Instance
func (s Instance) MarshalJSON() ([]byte, error)
type Intersection
func (s Intersection) MarshalJSON() ([]byte, error)
type ListAppProfilesResponse
func (s ListAppProfilesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedViewsResponse
func (s ListAuthorizedViewsResponse) MarshalJSON() ([]byte, error)
type ListBackupsResponse
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListClustersResponse
func (s ListClustersResponse) MarshalJSON() ([]byte, error)
type ListHotTabletsResponse
func (s ListHotTabletsResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListLogicalViewsResponse
func (s ListLogicalViewsResponse) MarshalJSON() ([]byte, error)
type ListMaterializedViewsResponse
func (s ListMaterializedViewsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListSchemaBundlesResponse
func (s ListSchemaBundlesResponse) MarshalJSON() ([]byte, error)
type ListTablesResponse
func (s ListTablesResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type LogicalView
func (s LogicalView) MarshalJSON() ([]byte, error)
type MaterializedView
func (s MaterializedView) MarshalJSON() ([]byte, error)
type Modification
func (s Modification) MarshalJSON() ([]byte, error)
type ModifyColumnFamiliesRequest
func (s ModifyColumnFamiliesRequest) MarshalJSON() ([]byte, error)
type MultiClusterRoutingUseAny
func (s MultiClusterRoutingUseAny) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationProgress
func (s OperationProgress) MarshalJSON() ([]byte, error)
type OperationsGetCall
func (c *OperationsGetCall) Context(ctx context.Context) *OperationsGetCall
func (c *OperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *OperationsGetCall) Fields(s ...googleapi.Field) *OperationsGetCall
func (c *OperationsGetCall) Header() http.Header
func (c *OperationsGetCall) IfNoneMatch(entityTag string) *OperationsGetCall
type OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) Context(ctx context.Context) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)
func (c *OperationsProjectsOperationsListCall) Fields(s ...googleapi.Field) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) Filter(filter string) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) Header() http.Header
func (c *OperationsProjectsOperationsListCall) IfNoneMatch(entityTag string) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) PageSize(pageSize int64) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) PageToken(pageToken string) *OperationsProjectsOperationsListCall
func (c *OperationsProjectsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error
func (c *OperationsProjectsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OperationsProjectsOperationsListCall
type OperationsProjectsOperationsService
func NewOperationsProjectsOperationsService(s *Service) *OperationsProjectsOperationsService
func (r *OperationsProjectsOperationsService) List(name string) *OperationsProjectsOperationsListCall
type OperationsProjectsService
func NewOperationsProjectsService(s *Service) *OperationsProjectsService
type OperationsService
func NewOperationsService(s *Service) *OperationsService
func (r *OperationsService) Get(name string) *OperationsGetCall
type OptimizeRestoredTableMetadata
func (s OptimizeRestoredTableMetadata) MarshalJSON() ([]byte, error)
type PartialUpdateClusterMetadata
func (s PartialUpdateClusterMetadata) MarshalJSON() ([]byte, error)
type PartialUpdateClusterRequest
func (s PartialUpdateClusterRequest) MarshalJSON() ([]byte, error)
type PartialUpdateInstanceRequest
func (s PartialUpdateInstanceRequest) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsInstancesAppProfilesCreateCall
func (c *ProjectsInstancesAppProfilesCreateCall) AppProfileId(appProfileId string) *ProjectsInstancesAppProfilesCreateCall
func (c *ProjectsInstancesAppProfilesCreateCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesCreateCall
func (c *ProjectsInstancesAppProfilesCreateCall) Do(opts ...googleapi.CallOption) (*AppProfile, error)
func (c *ProjectsInstancesAppProfilesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesCreateCall
func (c *ProjectsInstancesAppProfilesCreateCall) Header() http.Header
func (c *ProjectsInstancesAppProfilesCreateCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesCreateCall
type ProjectsInstancesAppProfilesDeleteCall
func (c *ProjectsInstancesAppProfilesDeleteCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesDeleteCall
func (c *ProjectsInstancesAppProfilesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesAppProfilesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesDeleteCall
func (c *ProjectsInstancesAppProfilesDeleteCall) Header() http.Header
func (c *ProjectsInstancesAppProfilesDeleteCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesDeleteCall
type ProjectsInstancesAppProfilesGetCall
func (c *ProjectsInstancesAppProfilesGetCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesGetCall
func (c *ProjectsInstancesAppProfilesGetCall) Do(opts ...googleapi.CallOption) (*AppProfile, error)
func (c *ProjectsInstancesAppProfilesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesGetCall
func (c *ProjectsInstancesAppProfilesGetCall) Header() http.Header
func (c *ProjectsInstancesAppProfilesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesAppProfilesGetCall
type ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) Do(opts ...googleapi.CallOption) (*ListAppProfilesResponse, error)
func (c *ProjectsInstancesAppProfilesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) Header() http.Header
func (c *ProjectsInstancesAppProfilesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) PageSize(pageSize int64) *ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) PageToken(pageToken string) *ProjectsInstancesAppProfilesListCall
func (c *ProjectsInstancesAppProfilesListCall) Pages(ctx context.Context, f func(*ListAppProfilesResponse) error) error
type ProjectsInstancesAppProfilesPatchCall
func (c *ProjectsInstancesAppProfilesPatchCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesPatchCall
func (c *ProjectsInstancesAppProfilesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesAppProfilesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesPatchCall
func (c *ProjectsInstancesAppProfilesPatchCall) Header() http.Header
func (c *ProjectsInstancesAppProfilesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesPatchCall
func (c *ProjectsInstancesAppProfilesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesAppProfilesPatchCall
type ProjectsInstancesAppProfilesService
func NewProjectsInstancesAppProfilesService(s *Service) *ProjectsInstancesAppProfilesService
func (r *ProjectsInstancesAppProfilesService) Create(parent string, appprofile *AppProfile) *ProjectsInstancesAppProfilesCreateCall
func (r *ProjectsInstancesAppProfilesService) Delete(name string) *ProjectsInstancesAppProfilesDeleteCall
func (r *ProjectsInstancesAppProfilesService) Get(name string) *ProjectsInstancesAppProfilesGetCall
func (r *ProjectsInstancesAppProfilesService) List(parent string) *ProjectsInstancesAppProfilesListCall
func (r *ProjectsInstancesAppProfilesService) Patch(name string, appprofile *AppProfile) *ProjectsInstancesAppProfilesPatchCall
type ProjectsInstancesClustersBackupsCopyCall
func (c *ProjectsInstancesClustersBackupsCopyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsCopyCall
func (c *ProjectsInstancesClustersBackupsCopyCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesClustersBackupsCopyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsCopyCall
func (c *ProjectsInstancesClustersBackupsCopyCall) Header() http.Header
type ProjectsInstancesClustersBackupsCreateCall
func (c *ProjectsInstancesClustersBackupsCreateCall) BackupId(backupId string) *ProjectsInstancesClustersBackupsCreateCall
func (c *ProjectsInstancesClustersBackupsCreateCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsCreateCall
func (c *ProjectsInstancesClustersBackupsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesClustersBackupsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsCreateCall
func (c *ProjectsInstancesClustersBackupsCreateCall) Header() http.Header
type ProjectsInstancesClustersBackupsDeleteCall
func (c *ProjectsInstancesClustersBackupsDeleteCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsDeleteCall
func (c *ProjectsInstancesClustersBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesClustersBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsDeleteCall
func (c *ProjectsInstancesClustersBackupsDeleteCall) Header() http.Header
type ProjectsInstancesClustersBackupsGetCall
func (c *ProjectsInstancesClustersBackupsGetCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsGetCall
func (c *ProjectsInstancesClustersBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)
func (c *ProjectsInstancesClustersBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsGetCall
func (c *ProjectsInstancesClustersBackupsGetCall) Header() http.Header
func (c *ProjectsInstancesClustersBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersBackupsGetCall
type ProjectsInstancesClustersBackupsGetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsGetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsGetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Header() http.Header
type ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)
func (c *ProjectsInstancesClustersBackupsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) Filter(filter string) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) Header() http.Header
func (c *ProjectsInstancesClustersBackupsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) OrderBy(orderBy string) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) PageSize(pageSize int64) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) PageToken(pageToken string) *ProjectsInstancesClustersBackupsListCall
func (c *ProjectsInstancesClustersBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error
type ProjectsInstancesClustersBackupsPatchCall
func (c *ProjectsInstancesClustersBackupsPatchCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsPatchCall
func (c *ProjectsInstancesClustersBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Backup, error)
func (c *ProjectsInstancesClustersBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsPatchCall
func (c *ProjectsInstancesClustersBackupsPatchCall) Header() http.Header
func (c *ProjectsInstancesClustersBackupsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesClustersBackupsPatchCall
type ProjectsInstancesClustersBackupsService
func NewProjectsInstancesClustersBackupsService(s *Service) *ProjectsInstancesClustersBackupsService
func (r *ProjectsInstancesClustersBackupsService) Copy(parent string, copybackuprequest *CopyBackupRequest) *ProjectsInstancesClustersBackupsCopyCall
func (r *ProjectsInstancesClustersBackupsService) Create(parent string, backup *Backup) *ProjectsInstancesClustersBackupsCreateCall
func (r *ProjectsInstancesClustersBackupsService) Delete(name string) *ProjectsInstancesClustersBackupsDeleteCall
func (r *ProjectsInstancesClustersBackupsService) Get(name string) *ProjectsInstancesClustersBackupsGetCall
func (r *ProjectsInstancesClustersBackupsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesClustersBackupsGetIamPolicyCall
func (r *ProjectsInstancesClustersBackupsService) List(parent string) *ProjectsInstancesClustersBackupsListCall
func (r *ProjectsInstancesClustersBackupsService) Patch(nameid string, backup *Backup) *ProjectsInstancesClustersBackupsPatchCall
func (r *ProjectsInstancesClustersBackupsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesClustersBackupsSetIamPolicyCall
func (r *ProjectsInstancesClustersBackupsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesClustersBackupsTestIamPermissionsCall
type ProjectsInstancesClustersBackupsSetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsSetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsSetIamPolicyCall
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Header() http.Header
type ProjectsInstancesClustersBackupsTestIamPermissionsCall
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsTestIamPermissionsCall
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsTestIamPermissionsCall
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesClustersCreateCall
func (c *ProjectsInstancesClustersCreateCall) ClusterId(clusterId string) *ProjectsInstancesClustersCreateCall
func (c *ProjectsInstancesClustersCreateCall) Context(ctx context.Context) *ProjectsInstancesClustersCreateCall
func (c *ProjectsInstancesClustersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesClustersCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersCreateCall
func (c *ProjectsInstancesClustersCreateCall) Header() http.Header
type ProjectsInstancesClustersDeleteCall
func (c *ProjectsInstancesClustersDeleteCall) Context(ctx context.Context) *ProjectsInstancesClustersDeleteCall
func (c *ProjectsInstancesClustersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesClustersDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersDeleteCall
func (c *ProjectsInstancesClustersDeleteCall) Header() http.Header
type ProjectsInstancesClustersGetCall
func (c *ProjectsInstancesClustersGetCall) Context(ctx context.Context) *ProjectsInstancesClustersGetCall
func (c *ProjectsInstancesClustersGetCall) Do(opts ...googleapi.CallOption) (*Cluster, error)
func (c *ProjectsInstancesClustersGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersGetCall
func (c *ProjectsInstancesClustersGetCall) Header() http.Header
func (c *ProjectsInstancesClustersGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersGetCall
type ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) Context(ctx context.Context) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) Do(opts ...googleapi.CallOption) (*ListHotTabletsResponse, error)
func (c *ProjectsInstancesClustersHotTabletsListCall) EndTime(endTime string) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) Header() http.Header
func (c *ProjectsInstancesClustersHotTabletsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) PageSize(pageSize int64) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) PageToken(pageToken string) *ProjectsInstancesClustersHotTabletsListCall
func (c *ProjectsInstancesClustersHotTabletsListCall) Pages(ctx context.Context, f func(*ListHotTabletsResponse) error) error
func (c *ProjectsInstancesClustersHotTabletsListCall) StartTime(startTime string) *ProjectsInstancesClustersHotTabletsListCall
type ProjectsInstancesClustersHotTabletsService
func NewProjectsInstancesClustersHotTabletsService(s *Service) *ProjectsInstancesClustersHotTabletsService
func (r *ProjectsInstancesClustersHotTabletsService) List(parent string) *ProjectsInstancesClustersHotTabletsListCall
type ProjectsInstancesClustersListCall
func (c *ProjectsInstancesClustersListCall) Context(ctx context.Context) *ProjectsInstancesClustersListCall
func (c *ProjectsInstancesClustersListCall) Do(opts ...googleapi.CallOption) (*ListClustersResponse, error)
func (c *ProjectsInstancesClustersListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersListCall
func (c *ProjectsInstancesClustersListCall) Header() http.Header
func (c *ProjectsInstancesClustersListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersListCall
func (c *ProjectsInstancesClustersListCall) PageToken(pageToken string) *ProjectsInstancesClustersListCall
func (c *ProjectsInstancesClustersListCall) Pages(ctx context.Context, f func(*ListClustersResponse) error) error
type ProjectsInstancesClustersPartialUpdateClusterCall
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Context(ctx context.Context) *ProjectsInstancesClustersPartialUpdateClusterCall
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersPartialUpdateClusterCall
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Header() http.Header
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) UpdateMask(updateMask string) *ProjectsInstancesClustersPartialUpdateClusterCall
type ProjectsInstancesClustersService
func NewProjectsInstancesClustersService(s *Service) *ProjectsInstancesClustersService
func (r *ProjectsInstancesClustersService) Create(parent string, cluster *Cluster) *ProjectsInstancesClustersCreateCall
func (r *ProjectsInstancesClustersService) Delete(name string) *ProjectsInstancesClustersDeleteCall
func (r *ProjectsInstancesClustersService) Get(name string) *ProjectsInstancesClustersGetCall
func (r *ProjectsInstancesClustersService) List(parent string) *ProjectsInstancesClustersListCall
func (r *ProjectsInstancesClustersService) PartialUpdateCluster(name string, cluster *Cluster) *ProjectsInstancesClustersPartialUpdateClusterCall
func (r *ProjectsInstancesClustersService) Update(name string, cluster *Cluster) *ProjectsInstancesClustersUpdateCall
type ProjectsInstancesClustersUpdateCall
func (c *ProjectsInstancesClustersUpdateCall) Context(ctx context.Context) *ProjectsInstancesClustersUpdateCall
func (c *ProjectsInstancesClustersUpdateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesClustersUpdateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersUpdateCall
func (c *ProjectsInstancesClustersUpdateCall) Header() http.Header
type ProjectsInstancesCreateCall
func (c *ProjectsInstancesCreateCall) Context(ctx context.Context) *ProjectsInstancesCreateCall
func (c *ProjectsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesCreateCall
func (c *ProjectsInstancesCreateCall) Header() http.Header
type ProjectsInstancesDeleteCall
func (c *ProjectsInstancesDeleteCall) Context(ctx context.Context) *ProjectsInstancesDeleteCall
func (c *ProjectsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesDeleteCall
func (c *ProjectsInstancesDeleteCall) Header() http.Header
type ProjectsInstancesGetCall
func (c *ProjectsInstancesGetCall) Context(ctx context.Context) *ProjectsInstancesGetCall
func (c *ProjectsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesGetCall
func (c *ProjectsInstancesGetCall) Header() http.Header
func (c *ProjectsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesGetCall
type ProjectsInstancesGetIamPolicyCall
func (c *ProjectsInstancesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesGetIamPolicyCall
func (c *ProjectsInstancesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesGetIamPolicyCall
func (c *ProjectsInstancesGetIamPolicyCall) Header() http.Header
type ProjectsInstancesListCall
func (c *ProjectsInstancesListCall) Context(ctx context.Context) *ProjectsInstancesListCall
func (c *ProjectsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)
func (c *ProjectsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesListCall
func (c *ProjectsInstancesListCall) Header() http.Header
func (c *ProjectsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesListCall
func (c *ProjectsInstancesListCall) PageToken(pageToken string) *ProjectsInstancesListCall
func (c *ProjectsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error
type ProjectsInstancesLogicalViewsCreateCall
func (c *ProjectsInstancesLogicalViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsCreateCall
func (c *ProjectsInstancesLogicalViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesLogicalViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsCreateCall
func (c *ProjectsInstancesLogicalViewsCreateCall) Header() http.Header
func (c *ProjectsInstancesLogicalViewsCreateCall) LogicalViewId(logicalViewId string) *ProjectsInstancesLogicalViewsCreateCall
type ProjectsInstancesLogicalViewsDeleteCall
func (c *ProjectsInstancesLogicalViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsDeleteCall
func (c *ProjectsInstancesLogicalViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesLogicalViewsDeleteCall) Etag(etag string) *ProjectsInstancesLogicalViewsDeleteCall
func (c *ProjectsInstancesLogicalViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsDeleteCall
func (c *ProjectsInstancesLogicalViewsDeleteCall) Header() http.Header
type ProjectsInstancesLogicalViewsGetCall
func (c *ProjectsInstancesLogicalViewsGetCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsGetCall
func (c *ProjectsInstancesLogicalViewsGetCall) Do(opts ...googleapi.CallOption) (*LogicalView, error)
func (c *ProjectsInstancesLogicalViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsGetCall
func (c *ProjectsInstancesLogicalViewsGetCall) Header() http.Header
func (c *ProjectsInstancesLogicalViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesLogicalViewsGetCall
type ProjectsInstancesLogicalViewsGetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsGetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsGetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Header() http.Header
type ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) Do(opts ...googleapi.CallOption) (*ListLogicalViewsResponse, error)
func (c *ProjectsInstancesLogicalViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) Header() http.Header
func (c *ProjectsInstancesLogicalViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) PageSize(pageSize int64) *ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) PageToken(pageToken string) *ProjectsInstancesLogicalViewsListCall
func (c *ProjectsInstancesLogicalViewsListCall) Pages(ctx context.Context, f func(*ListLogicalViewsResponse) error) error
type ProjectsInstancesLogicalViewsPatchCall
func (c *ProjectsInstancesLogicalViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsPatchCall
func (c *ProjectsInstancesLogicalViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesLogicalViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsPatchCall
func (c *ProjectsInstancesLogicalViewsPatchCall) Header() http.Header
func (c *ProjectsInstancesLogicalViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesLogicalViewsPatchCall
type ProjectsInstancesLogicalViewsService
func NewProjectsInstancesLogicalViewsService(s *Service) *ProjectsInstancesLogicalViewsService
func (r *ProjectsInstancesLogicalViewsService) Create(parent string, logicalview *LogicalView) *ProjectsInstancesLogicalViewsCreateCall
func (r *ProjectsInstancesLogicalViewsService) Delete(name string) *ProjectsInstancesLogicalViewsDeleteCall
func (r *ProjectsInstancesLogicalViewsService) Get(name string) *ProjectsInstancesLogicalViewsGetCall
func (r *ProjectsInstancesLogicalViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesLogicalViewsGetIamPolicyCall
func (r *ProjectsInstancesLogicalViewsService) List(parent string) *ProjectsInstancesLogicalViewsListCall
func (r *ProjectsInstancesLogicalViewsService) Patch(name string, logicalview *LogicalView) *ProjectsInstancesLogicalViewsPatchCall
func (r *ProjectsInstancesLogicalViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesLogicalViewsSetIamPolicyCall
func (r *ProjectsInstancesLogicalViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesLogicalViewsTestIamPermissionsCall
type ProjectsInstancesLogicalViewsSetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsSetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsSetIamPolicyCall
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Header() http.Header
type ProjectsInstancesLogicalViewsTestIamPermissionsCall
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsTestIamPermissionsCall
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsTestIamPermissionsCall
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesMaterializedViewsCreateCall
func (c *ProjectsInstancesMaterializedViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsCreateCall
func (c *ProjectsInstancesMaterializedViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesMaterializedViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsCreateCall
func (c *ProjectsInstancesMaterializedViewsCreateCall) Header() http.Header
func (c *ProjectsInstancesMaterializedViewsCreateCall) MaterializedViewId(materializedViewId string) *ProjectsInstancesMaterializedViewsCreateCall
type ProjectsInstancesMaterializedViewsDeleteCall
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsDeleteCall
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Etag(etag string) *ProjectsInstancesMaterializedViewsDeleteCall
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsDeleteCall
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Header() http.Header
type ProjectsInstancesMaterializedViewsGetCall
func (c *ProjectsInstancesMaterializedViewsGetCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsGetCall
func (c *ProjectsInstancesMaterializedViewsGetCall) Do(opts ...googleapi.CallOption) (*MaterializedView, error)
func (c *ProjectsInstancesMaterializedViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsGetCall
func (c *ProjectsInstancesMaterializedViewsGetCall) Header() http.Header
func (c *ProjectsInstancesMaterializedViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesMaterializedViewsGetCall
func (c *ProjectsInstancesMaterializedViewsGetCall) View(view string) *ProjectsInstancesMaterializedViewsGetCall
type ProjectsInstancesMaterializedViewsGetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsGetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsGetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Header() http.Header
type ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) Do(opts ...googleapi.CallOption) (*ListMaterializedViewsResponse, error)
func (c *ProjectsInstancesMaterializedViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) Header() http.Header
func (c *ProjectsInstancesMaterializedViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) PageSize(pageSize int64) *ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) PageToken(pageToken string) *ProjectsInstancesMaterializedViewsListCall
func (c *ProjectsInstancesMaterializedViewsListCall) Pages(ctx context.Context, f func(*ListMaterializedViewsResponse) error) error
func (c *ProjectsInstancesMaterializedViewsListCall) View(view string) *ProjectsInstancesMaterializedViewsListCall
type ProjectsInstancesMaterializedViewsPatchCall
func (c *ProjectsInstancesMaterializedViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsPatchCall
func (c *ProjectsInstancesMaterializedViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesMaterializedViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsPatchCall
func (c *ProjectsInstancesMaterializedViewsPatchCall) Header() http.Header
func (c *ProjectsInstancesMaterializedViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesMaterializedViewsPatchCall
type ProjectsInstancesMaterializedViewsService
func NewProjectsInstancesMaterializedViewsService(s *Service) *ProjectsInstancesMaterializedViewsService
func (r *ProjectsInstancesMaterializedViewsService) Create(parent string, materializedview *MaterializedView) *ProjectsInstancesMaterializedViewsCreateCall
func (r *ProjectsInstancesMaterializedViewsService) Delete(name string) *ProjectsInstancesMaterializedViewsDeleteCall
func (r *ProjectsInstancesMaterializedViewsService) Get(name string) *ProjectsInstancesMaterializedViewsGetCall
func (r *ProjectsInstancesMaterializedViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesMaterializedViewsGetIamPolicyCall
func (r *ProjectsInstancesMaterializedViewsService) List(parent string) *ProjectsInstancesMaterializedViewsListCall
func (r *ProjectsInstancesMaterializedViewsService) Patch(name string, materializedview *MaterializedView) *ProjectsInstancesMaterializedViewsPatchCall
func (r *ProjectsInstancesMaterializedViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesMaterializedViewsSetIamPolicyCall
func (r *ProjectsInstancesMaterializedViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall
type ProjectsInstancesMaterializedViewsSetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsSetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsSetIamPolicyCall
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Header() http.Header
type ProjectsInstancesMaterializedViewsTestIamPermissionsCall
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesPartialUpdateInstanceCall
func (c *ProjectsInstancesPartialUpdateInstanceCall) Context(ctx context.Context) *ProjectsInstancesPartialUpdateInstanceCall
func (c *ProjectsInstancesPartialUpdateInstanceCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesPartialUpdateInstanceCall) Fields(s ...googleapi.Field) *ProjectsInstancesPartialUpdateInstanceCall
func (c *ProjectsInstancesPartialUpdateInstanceCall) Header() http.Header
func (c *ProjectsInstancesPartialUpdateInstanceCall) UpdateMask(updateMask string) *ProjectsInstancesPartialUpdateInstanceCall
type ProjectsInstancesService
func NewProjectsInstancesService(s *Service) *ProjectsInstancesService
func (r *ProjectsInstancesService) Create(parent string, createinstancerequest *CreateInstanceRequest) *ProjectsInstancesCreateCall
func (r *ProjectsInstancesService) Delete(name string) *ProjectsInstancesDeleteCall
func (r *ProjectsInstancesService) Get(name string) *ProjectsInstancesGetCall
func (r *ProjectsInstancesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesGetIamPolicyCall
func (r *ProjectsInstancesService) List(parent string) *ProjectsInstancesListCall
func (r *ProjectsInstancesService) PartialUpdateInstance(name string, instance *Instance) *ProjectsInstancesPartialUpdateInstanceCall
func (r *ProjectsInstancesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesSetIamPolicyCall
func (r *ProjectsInstancesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTestIamPermissionsCall
func (r *ProjectsInstancesService) Update(name string, instance *Instance) *ProjectsInstancesUpdateCall
type ProjectsInstancesSetIamPolicyCall
func (c *ProjectsInstancesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesSetIamPolicyCall
func (c *ProjectsInstancesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesSetIamPolicyCall
func (c *ProjectsInstancesSetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesAuthorizedViewsCreateCall
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) AuthorizedViewId(authorizedViewId string) *ProjectsInstancesTablesAuthorizedViewsCreateCall
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsCreateCall
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsCreateCall
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Header() http.Header
type ProjectsInstancesTablesAuthorizedViewsDeleteCall
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsDeleteCall
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Etag(etag string) *ProjectsInstancesTablesAuthorizedViewsDeleteCall
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsDeleteCall
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Header() http.Header
type ProjectsInstancesTablesAuthorizedViewsGetCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsGetCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedView, error)
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsGetCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Header() http.Header
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesAuthorizedViewsGetCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) View(view string) *ProjectsInstancesTablesAuthorizedViewsGetCall
type ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedViewsResponse, error)
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Header() http.Header
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) PageSize(pageSize int64) *ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) PageToken(pageToken string) *ProjectsInstancesTablesAuthorizedViewsListCall
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Pages(ctx context.Context, f func(*ListAuthorizedViewsResponse) error) error
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) View(view string) *ProjectsInstancesTablesAuthorizedViewsListCall
type ProjectsInstancesTablesAuthorizedViewsPatchCall
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsPatchCall
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsPatchCall
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Header() http.Header
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesAuthorizedViewsPatchCall
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesAuthorizedViewsPatchCall
type ProjectsInstancesTablesAuthorizedViewsService
func NewProjectsInstancesTablesAuthorizedViewsService(s *Service) *ProjectsInstancesTablesAuthorizedViewsService
func (r *ProjectsInstancesTablesAuthorizedViewsService) Create(parent string, authorizedview *AuthorizedView) *ProjectsInstancesTablesAuthorizedViewsCreateCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) Delete(name string) *ProjectsInstancesTablesAuthorizedViewsDeleteCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) Get(name string) *ProjectsInstancesTablesAuthorizedViewsGetCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) List(parent string) *ProjectsInstancesTablesAuthorizedViewsListCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) Patch(name string, authorizedview *AuthorizedView) *ProjectsInstancesTablesAuthorizedViewsPatchCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall
func (r *ProjectsInstancesTablesAuthorizedViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall
type ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesTablesCheckConsistencyCall
func (c *ProjectsInstancesTablesCheckConsistencyCall) Context(ctx context.Context) *ProjectsInstancesTablesCheckConsistencyCall
func (c *ProjectsInstancesTablesCheckConsistencyCall) Do(opts ...googleapi.CallOption) (*CheckConsistencyResponse, error)
func (c *ProjectsInstancesTablesCheckConsistencyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesCheckConsistencyCall
func (c *ProjectsInstancesTablesCheckConsistencyCall) Header() http.Header
type ProjectsInstancesTablesCreateCall
func (c *ProjectsInstancesTablesCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesCreateCall
func (c *ProjectsInstancesTablesCreateCall) Do(opts ...googleapi.CallOption) (*Table, error)
func (c *ProjectsInstancesTablesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesCreateCall
func (c *ProjectsInstancesTablesCreateCall) Header() http.Header
type ProjectsInstancesTablesDeleteCall
func (c *ProjectsInstancesTablesDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesDeleteCall
func (c *ProjectsInstancesTablesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesTablesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesDeleteCall
func (c *ProjectsInstancesTablesDeleteCall) Header() http.Header
type ProjectsInstancesTablesDropRowRangeCall
func (c *ProjectsInstancesTablesDropRowRangeCall) Context(ctx context.Context) *ProjectsInstancesTablesDropRowRangeCall
func (c *ProjectsInstancesTablesDropRowRangeCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesTablesDropRowRangeCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesDropRowRangeCall
func (c *ProjectsInstancesTablesDropRowRangeCall) Header() http.Header
type ProjectsInstancesTablesGenerateConsistencyTokenCall
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Context(ctx context.Context) *ProjectsInstancesTablesGenerateConsistencyTokenCall
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Do(opts ...googleapi.CallOption) (*GenerateConsistencyTokenResponse, error)
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGenerateConsistencyTokenCall
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Header() http.Header
type ProjectsInstancesTablesGetCall
func (c *ProjectsInstancesTablesGetCall) Context(ctx context.Context) *ProjectsInstancesTablesGetCall
func (c *ProjectsInstancesTablesGetCall) Do(opts ...googleapi.CallOption) (*Table, error)
func (c *ProjectsInstancesTablesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGetCall
func (c *ProjectsInstancesTablesGetCall) Header() http.Header
func (c *ProjectsInstancesTablesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesGetCall
func (c *ProjectsInstancesTablesGetCall) View(view string) *ProjectsInstancesTablesGetCall
type ProjectsInstancesTablesGetIamPolicyCall
func (c *ProjectsInstancesTablesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesGetIamPolicyCall
func (c *ProjectsInstancesTablesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGetIamPolicyCall
func (c *ProjectsInstancesTablesGetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) Context(ctx context.Context) *ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) Do(opts ...googleapi.CallOption) (*ListTablesResponse, error)
func (c *ProjectsInstancesTablesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) Header() http.Header
func (c *ProjectsInstancesTablesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) PageSize(pageSize int64) *ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) PageToken(pageToken string) *ProjectsInstancesTablesListCall
func (c *ProjectsInstancesTablesListCall) Pages(ctx context.Context, f func(*ListTablesResponse) error) error
func (c *ProjectsInstancesTablesListCall) View(view string) *ProjectsInstancesTablesListCall
type ProjectsInstancesTablesModifyColumnFamiliesCall
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Context(ctx context.Context) *ProjectsInstancesTablesModifyColumnFamiliesCall
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Do(opts ...googleapi.CallOption) (*Table, error)
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesModifyColumnFamiliesCall
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Header() http.Header
type ProjectsInstancesTablesPatchCall
func (c *ProjectsInstancesTablesPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesPatchCall
func (c *ProjectsInstancesTablesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesPatchCall
func (c *ProjectsInstancesTablesPatchCall) Header() http.Header
func (c *ProjectsInstancesTablesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesPatchCall
func (c *ProjectsInstancesTablesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesPatchCall
type ProjectsInstancesTablesRestoreCall
func (c *ProjectsInstancesTablesRestoreCall) Context(ctx context.Context) *ProjectsInstancesTablesRestoreCall
func (c *ProjectsInstancesTablesRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesRestoreCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesRestoreCall
func (c *ProjectsInstancesTablesRestoreCall) Header() http.Header
type ProjectsInstancesTablesSchemaBundlesCreateCall
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesCreateCall
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesCreateCall
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Header() http.Header
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) SchemaBundleId(schemaBundleId string) *ProjectsInstancesTablesSchemaBundlesCreateCall
type ProjectsInstancesTablesSchemaBundlesDeleteCall
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesDeleteCall
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Etag(etag string) *ProjectsInstancesTablesSchemaBundlesDeleteCall
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesDeleteCall
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Header() http.Header
type ProjectsInstancesTablesSchemaBundlesGetCall
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesGetCall
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Do(opts ...googleapi.CallOption) (*SchemaBundle, error)
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesGetCall
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Header() http.Header
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesSchemaBundlesGetCall
type ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Do(opts ...googleapi.CallOption) (*ListSchemaBundlesResponse, error)
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Header() http.Header
func (c *ProjectsInstancesTablesSchemaBundlesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) PageSize(pageSize int64) *ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) PageToken(pageToken string) *ProjectsInstancesTablesSchemaBundlesListCall
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Pages(ctx context.Context, f func(*ListSchemaBundlesResponse) error) error
func (c *ProjectsInstancesTablesSchemaBundlesListCall) View(view string) *ProjectsInstancesTablesSchemaBundlesListCall
type ProjectsInstancesTablesSchemaBundlesPatchCall
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesPatchCall
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesPatchCall
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Header() http.Header
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesSchemaBundlesPatchCall
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesSchemaBundlesPatchCall
type ProjectsInstancesTablesSchemaBundlesService
func NewProjectsInstancesTablesSchemaBundlesService(s *Service) *ProjectsInstancesTablesSchemaBundlesService
func (r *ProjectsInstancesTablesSchemaBundlesService) Create(parent string, schemabundle *SchemaBundle) *ProjectsInstancesTablesSchemaBundlesCreateCall
func (r *ProjectsInstancesTablesSchemaBundlesService) Delete(name string) *ProjectsInstancesTablesSchemaBundlesDeleteCall
func (r *ProjectsInstancesTablesSchemaBundlesService) Get(name string) *ProjectsInstancesTablesSchemaBundlesGetCall
func (r *ProjectsInstancesTablesSchemaBundlesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall
func (r *ProjectsInstancesTablesSchemaBundlesService) List(parent string) *ProjectsInstancesTablesSchemaBundlesListCall
func (r *ProjectsInstancesTablesSchemaBundlesService) Patch(name string, schemabundle *SchemaBundle) *ProjectsInstancesTablesSchemaBundlesPatchCall
func (r *ProjectsInstancesTablesSchemaBundlesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall
func (r *ProjectsInstancesTablesSchemaBundlesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall
type ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesTablesService
func NewProjectsInstancesTablesService(s *Service) *ProjectsInstancesTablesService
func (r *ProjectsInstancesTablesService) CheckConsistency(name string, checkconsistencyrequest *CheckConsistencyRequest) *ProjectsInstancesTablesCheckConsistencyCall
func (r *ProjectsInstancesTablesService) Create(parent string, createtablerequest *CreateTableRequest) *ProjectsInstancesTablesCreateCall
func (r *ProjectsInstancesTablesService) Delete(name string) *ProjectsInstancesTablesDeleteCall
func (r *ProjectsInstancesTablesService) DropRowRange(name string, droprowrangerequest *DropRowRangeRequest) *ProjectsInstancesTablesDropRowRangeCall
func (r *ProjectsInstancesTablesService) GenerateConsistencyToken(name string, generateconsistencytokenrequest *GenerateConsistencyTokenRequest) *ProjectsInstancesTablesGenerateConsistencyTokenCall
func (r *ProjectsInstancesTablesService) Get(name string) *ProjectsInstancesTablesGetCall
func (r *ProjectsInstancesTablesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesGetIamPolicyCall
func (r *ProjectsInstancesTablesService) List(parent string) *ProjectsInstancesTablesListCall
func (r *ProjectsInstancesTablesService) ModifyColumnFamilies(name string, modifycolumnfamiliesrequest *ModifyColumnFamiliesRequest) *ProjectsInstancesTablesModifyColumnFamiliesCall
func (r *ProjectsInstancesTablesService) Patch(name string, table *Table) *ProjectsInstancesTablesPatchCall
func (r *ProjectsInstancesTablesService) Restore(parent string, restoretablerequest *RestoreTableRequest) *ProjectsInstancesTablesRestoreCall
func (r *ProjectsInstancesTablesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesSetIamPolicyCall
func (r *ProjectsInstancesTablesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesTestIamPermissionsCall
func (r *ProjectsInstancesTablesService) Undelete(name string, undeletetablerequest *UndeleteTableRequest) *ProjectsInstancesTablesUndeleteCall
type ProjectsInstancesTablesSetIamPolicyCall
func (c *ProjectsInstancesTablesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSetIamPolicyCall
func (c *ProjectsInstancesTablesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsInstancesTablesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSetIamPolicyCall
func (c *ProjectsInstancesTablesSetIamPolicyCall) Header() http.Header
type ProjectsInstancesTablesTestIamPermissionsCall
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesTestIamPermissionsCall
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesTestIamPermissionsCall
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesTablesUndeleteCall
func (c *ProjectsInstancesTablesUndeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesUndeleteCall
func (c *ProjectsInstancesTablesUndeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsInstancesTablesUndeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesUndeleteCall
func (c *ProjectsInstancesTablesUndeleteCall) Header() http.Header
type ProjectsInstancesTestIamPermissionsCall
func (c *ProjectsInstancesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTestIamPermissionsCall
func (c *ProjectsInstancesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsInstancesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTestIamPermissionsCall
func (c *ProjectsInstancesTestIamPermissionsCall) Header() http.Header
type ProjectsInstancesUpdateCall
func (c *ProjectsInstancesUpdateCall) Context(ctx context.Context) *ProjectsInstancesUpdateCall
func (c *ProjectsInstancesUpdateCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsInstancesUpdateCall) Fields(s ...googleapi.Field) *ProjectsInstancesUpdateCall
func (c *ProjectsInstancesUpdateCall) Header() http.Header
type ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Header() http.Header
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type ProtoSchema
func (s ProtoSchema) MarshalJSON() ([]byte, error)
type RestoreInfo
func (s RestoreInfo) MarshalJSON() ([]byte, error)
type RestoreTableMetadata
func (s RestoreTableMetadata) MarshalJSON() ([]byte, error)
type RestoreTableRequest
func (s RestoreTableRequest) MarshalJSON() ([]byte, error)
type RowAffinity
type SchemaBundle
func (s SchemaBundle) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type SingleClusterRouting
func (s SingleClusterRouting) MarshalJSON() ([]byte, error)
type Split
func (s Split) MarshalJSON() ([]byte, error)
type StandardIsolation
func (s StandardIsolation) MarshalJSON() ([]byte, error)
type StandardReadRemoteWrites
type Status
func (s Status) MarshalJSON() ([]byte, error)
type Table
func (s Table) MarshalJSON() ([]byte, error)
type TableProgress
func (s TableProgress) MarshalJSON() ([]byte, error)
type TableStats
func (s TableStats) MarshalJSON() ([]byte, error)
func (s *TableStats) UnmarshalJSON(data []byte) error
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type TieredStorageConfig
func (s TieredStorageConfig) MarshalJSON() ([]byte, error)
type TieredStorageRule
func (s TieredStorageRule) MarshalJSON() ([]byte, error)
type Type
func (s Type) MarshalJSON() ([]byte, error)
type UndeleteTableMetadata
func (s UndeleteTableMetadata) MarshalJSON() ([]byte, error)
type UndeleteTableRequest
type Union
func (s Union) MarshalJSON() ([]byte, error)
type UpdateAppProfileMetadata
type UpdateAuthorizedViewMetadata
func (s UpdateAuthorizedViewMetadata) MarshalJSON() ([]byte, error)
type UpdateAuthorizedViewRequest
func (s UpdateAuthorizedViewRequest) MarshalJSON() ([]byte, error)
type UpdateClusterMetadata
func (s UpdateClusterMetadata) MarshalJSON() ([]byte, error)
type UpdateInstanceMetadata
func (s UpdateInstanceMetadata) MarshalJSON() ([]byte, error)
type UpdateLogicalViewMetadata
func (s UpdateLogicalViewMetadata) MarshalJSON() ([]byte, error)
type UpdateLogicalViewRequest
func (s UpdateLogicalViewRequest) MarshalJSON() ([]byte, error)
type UpdateSchemaBundleMetadata
func (s UpdateSchemaBundleMetadata) MarshalJSON() ([]byte, error)
type UpdateTableMetadata
func (s UpdateTableMetadata) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// Administer your Cloud Bigtable tables and clusters
	BigtableAdminScope = "https://www.googleapis.com/auth/bigtable.admin"

	// Administer your Cloud Bigtable clusters
	BigtableAdminClusterScope = "https://www.googleapis.com/auth/bigtable.admin.cluster"

	// Administer your Cloud Bigtable clusters
	BigtableAdminInstanceScope = "https://www.googleapis.com/auth/bigtable.admin.instance"

	// Administer your Cloud Bigtable tables
	BigtableAdminTableScope = "https://www.googleapis.com/auth/bigtable.admin.table"

	// Administer your Cloud Bigtable tables and clusters
	CloudBigtableAdminScope = "https://www.googleapis.com/auth/cloud-bigtable.admin"

	// Administer your Cloud Bigtable clusters
	CloudBigtableAdminClusterScope = "https://www.googleapis.com/auth/cloud-bigtable.admin.cluster"

	// Administer your Cloud Bigtable tables
	CloudBigtableAdminTableScope = "https://www.googleapis.com/auth/cloud-bigtable.admin.table"

	// See, edit, configure, and delete your Google Cloud data and see the email
	// address for your Google Account.
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	// View your data across Google Cloud services and see the email address of
	// your Google Account
	CloudPlatformReadOnlyScope = "https://www.googleapis.com/auth/cloud-platform.read-only"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type AppProfile ¶
type AppProfile struct {
	// DataBoostIsolationReadOnly: Specifies that this app profile is intended for
	// read-only usage via the Data Boost feature.
	DataBoostIsolationReadOnly *DataBoostIsolationReadOnly `json:"dataBoostIsolationReadOnly,omitempty"`
	// Description: Long form description of the use case for this AppProfile.
	Description string `json:"description,omitempty"`
	// Etag: Strongly validated etag for optimistic concurrency control. Preserve
	// the value returned from `GetAppProfile` when calling `UpdateAppProfile` to
	// fail the request if there has been a modification in the mean time. The
	// `update_mask` of the request need not include `etag` for this protection to
	// apply. See Wikipedia (https://en.wikipedia.org/wiki/HTTP_ETag) and RFC 7232
	// (https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
	Etag string `json:"etag,omitempty"`
	// MultiClusterRoutingUseAny: Use a multi-cluster routing policy.
	MultiClusterRoutingUseAny *MultiClusterRoutingUseAny `json:"multiClusterRoutingUseAny,omitempty"`
	// Name: The unique name of the app profile, up to 50 characters long. Values
	// are of the form
	// `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
	Name string `json:"name,omitempty"`
	// Priority: This field has been deprecated in favor of
	// `standard_isolation.priority`. If you set this field,
	// `standard_isolation.priority` will be set instead. The priority of requests
	// sent using this app profile.
	//
	// Possible values:
	//   "PRIORITY_UNSPECIFIED" - Default value. Mapped to PRIORITY_HIGH (the
	// legacy behavior) on creation.
	//   "PRIORITY_LOW"
	//   "PRIORITY_MEDIUM"
	//   "PRIORITY_HIGH"
	Priority string `json:"priority,omitempty"`
	// SingleClusterRouting: Use a single-cluster routing policy.
	SingleClusterRouting *SingleClusterRouting `json:"singleClusterRouting,omitempty"`
	// StandardIsolation: The standard options used for isolating this app
	// profile's traffic from other use cases.
	StandardIsolation *StandardIsolation `json:"standardIsolation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataBoostIsolationReadOnly")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataBoostIsolationReadOnly") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppProfile: A configuration object describing how Cloud Bigtable should treat traffic from a particular end user application.

func (AppProfile) MarshalJSON ¶
func (s AppProfile) MarshalJSON() ([]byte, error)
type AuditConfig ¶
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
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig ¶
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
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type AuthorizedView ¶
added in v0.171.0
type AuthorizedView struct {
	// DeletionProtection: Set to true to make the AuthorizedView protected against
	// deletion. The parent Table and containing Instance cannot be deleted if an
	// AuthorizedView has this bit set.
	DeletionProtection bool `json:"deletionProtection,omitempty"`
	// Etag: The etag for this AuthorizedView. If this is provided on update, it
	// must match the server's etag. The server returns ABORTED error on a
	// mismatched etag.
	Etag string `json:"etag,omitempty"`
	// Name: Identifier. The name of this AuthorizedView. Values are of the form
	// `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{auth
	// orized_view}`
	Name string `json:"name,omitempty"`
	// SubsetView: An AuthorizedView permitting access to an explicit subset of a
	// Table.
	SubsetView *GoogleBigtableAdminV2AuthorizedViewSubsetView `json:"subsetView,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeletionProtection") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeletionProtection") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuthorizedView: An Authorized View of a Cloud Bigtable Table.

func (AuthorizedView) MarshalJSON ¶
added in v0.171.0
func (s AuthorizedView) MarshalJSON() ([]byte, error)
type AutomatedBackupPolicy ¶
added in v0.170.0
type AutomatedBackupPolicy struct {
	// Frequency: How frequently automated backups should occur. The only supported
	// value at this time is 24 hours. An undefined frequency is treated as 24
	// hours.
	Frequency string `json:"frequency,omitempty"`
	// RetentionPeriod: Required. How long the automated backups should be
	// retained. Values must be at least 3 days and at most 90 days.
	RetentionPeriod string `json:"retentionPeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Frequency") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Frequency") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutomatedBackupPolicy: Defines an automated backup policy for a table

func (AutomatedBackupPolicy) MarshalJSON ¶
added in v0.170.0
func (s AutomatedBackupPolicy) MarshalJSON() ([]byte, error)
type AutoscalingLimits ¶
added in v0.61.0
type AutoscalingLimits struct {
	// MaxServeNodes: Required. Maximum number of nodes to scale up to.
	MaxServeNodes int64 `json:"maxServeNodes,omitempty"`
	// MinServeNodes: Required. Minimum number of nodes to scale down to.
	MinServeNodes int64 `json:"minServeNodes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaxServeNodes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxServeNodes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutoscalingLimits: Limits for the number of nodes a Cluster can autoscale up/down to.

func (AutoscalingLimits) MarshalJSON ¶
added in v0.61.0
func (s AutoscalingLimits) MarshalJSON() ([]byte, error)
type AutoscalingTargets ¶
added in v0.61.0
type AutoscalingTargets struct {
	// CpuUtilizationPercent: The cpu utilization that the Autoscaler should be
	// trying to achieve. This number is on a scale from 0 (no utilization) to 100
	// (total utilization), and is limited between 10 and 80, otherwise it will
	// return INVALID_ARGUMENT error.
	CpuUtilizationPercent int64 `json:"cpuUtilizationPercent,omitempty"`
	// StorageUtilizationGibPerNode: The storage utilization that the Autoscaler
	// should be trying to achieve. This number is limited between 2560 (2.5TiB)
	// and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16TiB)
	// for an HDD cluster, otherwise it will return INVALID_ARGUMENT error. If this
	// value is set to 0, it will be treated as if it were set to the default
	// value: 2560 for SSD, 8192 for HDD.
	StorageUtilizationGibPerNode int64 `json:"storageUtilizationGibPerNode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CpuUtilizationPercent") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CpuUtilizationPercent") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutoscalingTargets: The Autoscaling targets for a Cluster. These determine the recommended nodes.

func (AutoscalingTargets) MarshalJSON ¶
added in v0.61.0
func (s AutoscalingTargets) MarshalJSON() ([]byte, error)
type Backup ¶
added in v0.30.0
type Backup struct {
	// BackupType: Indicates the backup type of the backup.
	//
	// Possible values:
	//   "BACKUP_TYPE_UNSPECIFIED" - Not specified.
	//   "STANDARD" - The default type for Cloud Bigtable managed backups.
	// Supported for backups created in both HDD and SSD instances. Requires
	// optimization when restored to a table in an SSD instance.
	//   "HOT" - A backup type with faster restore to SSD performance. Only
	// supported for backups created in SSD instances. A new SSD table restored
	// from a hot backup reaches production performance more quickly than a
	// standard backup.
	BackupType string `json:"backupType,omitempty"`
	// EncryptionInfo: Output only. The encryption information for the backup.
	EncryptionInfo *EncryptionInfo `json:"encryptionInfo,omitempty"`
	// EndTime: Output only. `end_time` is the time that the backup was finished.
	// The row data in the backup will be no newer than this timestamp.
	EndTime string `json:"endTime,omitempty"`
	// ExpireTime: Required. The expiration time of the backup. When creating a
	// backup or updating its `expire_time`, the value must be greater than the
	// backup creation time by: - At least 6 hours - At most 90 days Once the
	// `expire_time` has passed, Cloud Bigtable will delete the backup.
	ExpireTime string `json:"expireTime,omitempty"`
	// HotToStandardTime: The time at which the hot backup will be converted to a
	// standard backup. Once the `hot_to_standard_time` has passed, Cloud Bigtable
	// will convert the hot backup to a standard backup. This value must be greater
	// than the backup creation time by: - At least 24 hours This field only
	// applies for hot backups. When creating or updating a standard backup,
	// attempting to set this field will fail the request.
	HotToStandardTime string `json:"hotToStandardTime,omitempty"`
	// Name: A globally unique identifier for the backup which cannot be changed.
	// Values are of the form
	// `projects/{project}/instances/{instance}/clusters/{cluster}/
	// backups/_a-zA-Z0-9*` The final segment of the name must be between 1 and 50
	// characters in length. The backup is stored in the cluster identified by the
	// prefix of the backup name of the form
	// `projects/{project}/instances/{instance}/clusters/{cluster}`.
	Name string `json:"name,omitempty"`
	// SizeBytes: Output only. Size of the backup in bytes.
	SizeBytes int64 `json:"sizeBytes,omitempty,string"`
	// SourceBackup: Output only. Name of the backup from which this backup was
	// copied. If a backup is not created by copying a backup, this field will be
	// empty. Values are of the form: projects//instances//clusters//backups/
	SourceBackup string `json:"sourceBackup,omitempty"`
	// SourceTable: Required. Immutable. Name of the table from which this backup
	// was created. This needs to be in the same instance as the backup. Values are
	// of the form `projects/{project}/instances/{instance}/tables/{source_table}`.
	SourceTable string `json:"sourceTable,omitempty"`
	// StartTime: Output only. `start_time` is the time that the backup was started
	// (i.e. approximately the time the CreateBackup request is received). The row
	// data in this backup will be no older than this timestamp.
	StartTime string `json:"startTime,omitempty"`
	// State: Output only. The current state of the backup.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Not specified.
	//   "CREATING" - The pending backup is still being created. Operations on the
	// backup may fail with `FAILED_PRECONDITION` in this state.
	//   "READY" - The backup is complete and ready for use.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Backup: A backup of a Cloud Bigtable table.

func (Backup) MarshalJSON ¶
added in v0.30.0
func (s Backup) MarshalJSON() ([]byte, error)
type BackupInfo ¶
added in v0.30.0
type BackupInfo struct {
	// Backup: Output only. Name of the backup.
	Backup string `json:"backup,omitempty"`
	// EndTime: Output only. This time that the backup was finished. Row data in
	// the backup will be no newer than this timestamp.
	EndTime string `json:"endTime,omitempty"`
	// SourceBackup: Output only. Name of the backup from which this backup was
	// copied. If a backup is not created by copying a backup, this field will be
	// empty. Values are of the form: projects//instances//clusters//backups/
	SourceBackup string `json:"sourceBackup,omitempty"`
	// SourceTable: Output only. Name of the table the backup was created from.
	SourceTable string `json:"sourceTable,omitempty"`
	// StartTime: Output only. The time that the backup was started. Row data in
	// the backup will be no older than this timestamp.
	StartTime string `json:"startTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Backup") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Backup") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupInfo: Information about a backup.

func (BackupInfo) MarshalJSON ¶
added in v0.30.0
func (s BackupInfo) MarshalJSON() ([]byte, error)
type Binding ¶
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
func (s Binding) MarshalJSON() ([]byte, error)
type ChangeStreamConfig ¶
added in v0.130.0
type ChangeStreamConfig struct {
	// RetentionPeriod: How long the change stream should be retained. Change
	// stream data older than the retention period will not be returned when
	// reading the change stream from the table. Values must be at least 1 day and
	// at most 7 days, and will be truncated to microsecond granularity.
	RetentionPeriod string `json:"retentionPeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RetentionPeriod") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RetentionPeriod") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChangeStreamConfig: Change stream configuration.

func (ChangeStreamConfig) MarshalJSON ¶
added in v0.130.0
func (s ChangeStreamConfig) MarshalJSON() ([]byte, error)
type CheckConsistencyRequest ¶
type CheckConsistencyRequest struct {
	// ConsistencyToken: Required. The token created using GenerateConsistencyToken
	// for the Table.
	ConsistencyToken string `json:"consistencyToken,omitempty"`
	// DataBoostReadLocalWrites: Checks that reads using an app profile with
	// `DataBoostIsolationReadOnly` can see all writes committed before the token
	// was created, but only if the read and write target the same cluster.
	DataBoostReadLocalWrites *DataBoostReadLocalWrites `json:"dataBoostReadLocalWrites,omitempty"`
	// StandardReadRemoteWrites: Checks that reads using an app profile with
	// `StandardIsolation` can see all writes committed before the token was
	// created, even if the read and write target different clusters.
	StandardReadRemoteWrites *StandardReadRemoteWrites `json:"standardReadRemoteWrites,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConsistencyToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsistencyToken") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CheckConsistencyRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency

func (CheckConsistencyRequest) MarshalJSON ¶
func (s CheckConsistencyRequest) MarshalJSON() ([]byte, error)
type CheckConsistencyResponse ¶
type CheckConsistencyResponse struct {
	// Consistent: True only if the token is consistent. A token is consistent if
	// replication has caught up with the restrictions specified in the request.
	Consistent bool `json:"consistent,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Consistent") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Consistent") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CheckConsistencyResponse: Response message for google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency

func (CheckConsistencyResponse) MarshalJSON ¶
func (s CheckConsistencyResponse) MarshalJSON() ([]byte, error)
type Cluster ¶
type Cluster struct {
	// ClusterConfig: Configuration for this cluster.
	ClusterConfig *ClusterConfig `json:"clusterConfig,omitempty"`
	// DefaultStorageType: Immutable. The type of storage used by this cluster to
	// serve its parent instance's tables, unless explicitly overridden.
	//
	// Possible values:
	//   "STORAGE_TYPE_UNSPECIFIED" - The user did not specify a storage type.
	//   "SSD" - Flash (SSD) storage should be used.
	//   "HDD" - Magnetic drive (HDD) storage should be used.
	DefaultStorageType string `json:"defaultStorageType,omitempty"`
	// EncryptionConfig: Immutable. The encryption configuration for CMEK-protected
	// clusters.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// Location: Immutable. The location where this cluster's nodes and storage
	// reside. For best performance, clients should be located as close as possible
	// to this cluster. Currently only zones are supported, so values should be of
	// the form `projects/{project}/locations/{zone}`.
	Location string `json:"location,omitempty"`
	// Name: The unique name of the cluster. Values are of the form
	// `projects/{project}/instances/{instance}/clusters/a-z*`.
	Name string `json:"name,omitempty"`
	// NodeScalingFactor: Immutable. The node scaling factor of this cluster.
	//
	// Possible values:
	//   "NODE_SCALING_FACTOR_UNSPECIFIED" - No node scaling specified. Defaults to
	// NODE_SCALING_FACTOR_1X.
	//   "NODE_SCALING_FACTOR_1X" - The cluster is running with a scaling factor of
	// 1.
	//   "NODE_SCALING_FACTOR_2X" - The cluster is running with a scaling factor of
	// 2. All node count values must be in increments of 2 with this scaling factor
	// enabled, otherwise an INVALID_ARGUMENT error will be returned.
	NodeScalingFactor string `json:"nodeScalingFactor,omitempty"`
	// ServeNodes: The number of nodes in the cluster. If no value is set, Cloud
	// Bigtable automatically allocates nodes based on your data footprint and
	// optimized for 50% storage utilization.
	ServeNodes int64 `json:"serveNodes,omitempty"`
	// State: Output only. The current state of the cluster.
	//
	// Possible values:
	//   "STATE_NOT_KNOWN" - The state of the cluster could not be determined.
	//   "READY" - The cluster has been successfully created and is ready to serve
	// requests.
	//   "CREATING" - The cluster is currently being created, and may be destroyed
	// if the creation process encounters an error. A cluster may not be able to
	// serve requests while being created.
	//   "RESIZING" - The cluster is currently being resized, and may revert to its
	// previous node count if the process encounters an error. A cluster is still
	// capable of serving requests while being resized, but may exhibit performance
	// as if its number of allocated nodes is between the starting and requested
	// states.
	//   "DISABLED" - The cluster has no backing nodes. The data (tables) still
	// exist, but no operations can be performed on the cluster.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClusterConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Cluster: A resizable group of nodes in a particular cloud location, capable of serving all Tables in the parent Instance.

func (Cluster) MarshalJSON ¶
func (s Cluster) MarshalJSON() ([]byte, error)
type ClusterAutoscalingConfig ¶
added in v0.61.0
type ClusterAutoscalingConfig struct {
	// AutoscalingLimits: Required. Autoscaling limits for this cluster.
	AutoscalingLimits *AutoscalingLimits `json:"autoscalingLimits,omitempty"`
	// AutoscalingTargets: Required. Autoscaling targets for this cluster.
	AutoscalingTargets *AutoscalingTargets `json:"autoscalingTargets,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoscalingLimits") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoscalingLimits") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClusterAutoscalingConfig: Autoscaling config for a cluster.

func (ClusterAutoscalingConfig) MarshalJSON ¶
added in v0.61.0
func (s ClusterAutoscalingConfig) MarshalJSON() ([]byte, error)
type ClusterConfig ¶
added in v0.61.0
type ClusterConfig struct {
	// ClusterAutoscalingConfig: Autoscaling configuration for this cluster.
	ClusterAutoscalingConfig *ClusterAutoscalingConfig `json:"clusterAutoscalingConfig,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterAutoscalingConfig")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterAutoscalingConfig") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClusterConfig: Configuration for a cluster.

func (ClusterConfig) MarshalJSON ¶
added in v0.61.0
func (s ClusterConfig) MarshalJSON() ([]byte, error)
type ClusterState ¶
type ClusterState struct {
	// EncryptionInfo: Output only. The encryption information for the table in
	// this cluster. If the encryption key protecting this resource is customer
	// managed, then its version can be rotated in Cloud Key Management Service
	// (Cloud KMS). The primary version of the key and its status will be reflected
	// here when changes propagate from Cloud KMS.
	EncryptionInfo []*EncryptionInfo `json:"encryptionInfo,omitempty"`
	// ReplicationState: Output only. The state of replication for the table in
	// this cluster.
	//
	// Possible values:
	//   "STATE_NOT_KNOWN" - The replication state of the table is unknown in this
	// cluster.
	//   "INITIALIZING" - The cluster was recently created, and the table must
	// finish copying over pre-existing data from other clusters before it can
	// begin receiving live replication updates and serving Data API requests.
	//   "PLANNED_MAINTENANCE" - The table is temporarily unable to serve Data API
	// requests from this cluster due to planned internal maintenance.
	//   "UNPLANNED_MAINTENANCE" - The table is temporarily unable to serve Data
	// API requests from this cluster due to unplanned or emergency maintenance.
	//   "READY" - The table can serve Data API requests from this cluster.
	// Depending on replication delay, reads may not immediately reflect the state
	// of the table in other clusters.
	//   "READY_OPTIMIZING" - The table is fully created and ready for use after a
	// restore, and is being optimized for performance. When optimizations are
	// complete, the table will transition to `READY` state.
	ReplicationState string `json:"replicationState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EncryptionInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EncryptionInfo") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClusterState: The state of a table's data in a particular cluster.

func (ClusterState) MarshalJSON ¶
func (s ClusterState) MarshalJSON() ([]byte, error)
type ColumnFamily ¶
type ColumnFamily struct {
	// GcRule: Garbage collection rule specified as a protobuf. Must serialize to
	// at most 500 bytes. NOTE: Garbage collection executes opportunistically in
	// the background, and so it's possible for reads to return a cell even if it
	// matches the active GC expression for its family.
	GcRule *GcRule `json:"gcRule,omitempty"`
	// Stats: Output only. Only available with STATS_VIEW, this includes summary
	// statistics about column family contents. For statistics over an entire
	// table, see TableStats above.
	Stats *ColumnFamilyStats `json:"stats,omitempty"`
	// ValueType: The type of data stored in each of this family's cell values,
	// including its full encoding. If omitted, the family only serves raw untyped
	// bytes. For now, only the `Aggregate` type is supported. `Aggregate` can only
	// be set at family creation and is immutable afterwards. This field is
	// mutually exclusive with `sql_type`. If `value_type` is `Aggregate`, written
	// data must be compatible with: * `value_type.input_type` for `AddInput`
	// mutations
	ValueType *Type `json:"valueType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcRule") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcRule") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ColumnFamily: A set of columns within a table which share a common configuration.

func (ColumnFamily) MarshalJSON ¶
func (s ColumnFamily) MarshalJSON() ([]byte, error)
type ColumnFamilyStats ¶
added in v0.103.0
type ColumnFamilyStats struct {
	// AverageCellsPerColumn: How many cells are present per column qualifier in
	// this column family, averaged over all rows containing any column in the
	// column family. e.g. For column family "family" in a table with 3 rows: * A
	// row with 3 cells in "family:col" and 1 cell in "other:col" (3 cells / 1
	// column in "family") * A row with 1 cell in "family:col", 7 cells in
	// "family:other_col", and 7 cells in "other:data" (8 cells / 2 columns in
	// "family") * A row with 3 cells in "other:col" (0 columns in "family",
	// "family" not present) would report (3 + 8 + 0)/(1 + 2 + 0) = 3.66 in this
	// field.
	AverageCellsPerColumn float64 `json:"averageCellsPerColumn,omitempty"`
	// AverageColumnsPerRow: How many column qualifiers are present in this column
	// family, averaged over all rows in the table. e.g. For column family "family"
	// in a table with 3 rows: * A row with cells in "family:col" and "other:col"
	// (1 column in "family") * A row with cells in "family:col",
	// "family:other_col", and "other:data" (2 columns in "family") * A row with
	// cells in "other:col" (0 columns in "family", "family" not present) would
	// report (1 + 2 + 0)/3 = 1.5 in this field.
	AverageColumnsPerRow float64 `json:"averageColumnsPerRow,omitempty"`
	// LogicalDataBytes: How much space the data in the column family occupies.
	// This is roughly how many bytes would be needed to read the contents of the
	// entire column family (e.g. by streaming all contents out).
	LogicalDataBytes int64 `json:"logicalDataBytes,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "AverageCellsPerColumn") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AverageCellsPerColumn") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ColumnFamilyStats: Approximate statistics related to a single column family within a table. This information may change rapidly, interpreting these values at a point in time may already preset out-of-date information. Everything below is approximate, unless otherwise specified.

func (ColumnFamilyStats) MarshalJSON ¶
added in v0.103.0
func (s ColumnFamilyStats) MarshalJSON() ([]byte, error)
func (*ColumnFamilyStats) UnmarshalJSON ¶
added in v0.103.0
func (s *ColumnFamilyStats) UnmarshalJSON(data []byte) error
type CopyBackupMetadata ¶
added in v0.101.0
type CopyBackupMetadata struct {
	// Name: The name of the backup being created through the copy operation.
	// Values are of the form `projects//instances//clusters//backups/`.
	Name string `json:"name,omitempty"`
	// Progress: The progress of the CopyBackup operation.
	Progress *OperationProgress `json:"progress,omitempty"`
	// SourceBackupInfo: Information about the source backup that is being copied
	// from.
	SourceBackupInfo *BackupInfo `json:"sourceBackupInfo,omitempty"`
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

CopyBackupMetadata: Metadata type for the google.longrunning.Operation returned by CopyBackup.

func (CopyBackupMetadata) MarshalJSON ¶
added in v0.101.0
func (s CopyBackupMetadata) MarshalJSON() ([]byte, error)
type CopyBackupRequest ¶
added in v0.101.0
type CopyBackupRequest struct {
	// BackupId: Required. The id of the new backup. The `backup_id` along with
	// `parent` are combined as {parent}/backups/{backup_id} to create the full
	// backup name, of the form:
	// `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_i
	// d}`. This string must be between 1 and 50 characters in length and match the
	// regex _a-zA-Z0-9*.
	BackupId string `json:"backupId,omitempty"`
	// ExpireTime: Required. Required. The expiration time of the copied backup
	// with microsecond granularity that must be at least 6 hours and at most 30
	// days from the time the request is received. Once the `expire_time` has
	// passed, Cloud Bigtable will delete the backup and free the resources used by
	// the backup.
	ExpireTime string `json:"expireTime,omitempty"`
	// SourceBackup: Required. The source backup to be copied from. The source
	// backup needs to be in READY state for it to be copied. Copying a copied
	// backup is not allowed. Once CopyBackup is in progress, the source backup
	// cannot be deleted or cleaned up on expiration until CopyBackup is finished.
	// Values are of the form: `projects//instances//clusters//backups/`.
	SourceBackup string `json:"sourceBackup,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CopyBackupRequest: The request for CopyBackup.

func (CopyBackupRequest) MarshalJSON ¶
added in v0.101.0
func (s CopyBackupRequest) MarshalJSON() ([]byte, error)
type CreateAuthorizedViewMetadata ¶
added in v0.171.0
type CreateAuthorizedViewMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// CreateAuthorizedView operation.
	OriginalRequest *CreateAuthorizedViewRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateAuthorizedViewMetadata: The metadata for the Operation returned by CreateAuthorizedView.

func (CreateAuthorizedViewMetadata) MarshalJSON ¶
added in v0.171.0
func (s CreateAuthorizedViewMetadata) MarshalJSON() ([]byte, error)
type CreateAuthorizedViewRequest ¶
added in v0.171.0
type CreateAuthorizedViewRequest struct {
	// AuthorizedView: Required. The AuthorizedView to create.
	AuthorizedView *AuthorizedView `json:"authorizedView,omitempty"`
	// AuthorizedViewId: Required. The id of the AuthorizedView to create. This
	// AuthorizedView must not already exist. The `authorized_view_id` appended to
	// `parent` forms the full AuthorizedView name of the form
	// `projects/{project}/instances/{instance}/tables/{table}/authorizedView/{autho
	// rized_view}`.
	AuthorizedViewId string `json:"authorizedViewId,omitempty"`
	// Parent: Required. This is the name of the table the AuthorizedView belongs
	// to. Values are of the form
	// `projects/{project}/instances/{instance}/tables/{table}`.
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuthorizedView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthorizedView") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateAuthorizedViewRequest: The request for CreateAuthorizedView

func (CreateAuthorizedViewRequest) MarshalJSON ¶
added in v0.171.0
func (s CreateAuthorizedViewRequest) MarshalJSON() ([]byte, error)
type CreateBackupMetadata ¶
added in v0.30.0
type CreateBackupMetadata struct {
	// EndTime: If set, the time at which this operation finished or was cancelled.
	// DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// Name: The name of the backup being created.
	Name string `json:"name,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// SourceTable: The name of the table the backup is created from.
	SourceTable string `json:"sourceTable,omitempty"`
	// StartTime: The time at which this operation started. DEPRECATED: Use
	// request_time instead.
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

CreateBackupMetadata: Metadata type for the operation returned by CreateBackup.

func (CreateBackupMetadata) MarshalJSON ¶
added in v0.30.0
func (s CreateBackupMetadata) MarshalJSON() ([]byte, error)
type CreateClusterMetadata ¶
type CreateClusterMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// CreateCluster operation.
	OriginalRequest *CreateClusterRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// Tables: Keys: the full `name` of each table that existed in the instance
	// when CreateCluster was first called, i.e. `projects//instances//tables/`.
	// Any table added to the instance by a later API call will be created in the
	// new cluster by that API call, not this one. Values: information on how much
	// of a table's data has been copied to the newly-created cluster so far.
	Tables map[string]TableProgress `json:"tables,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateClusterMetadata: The metadata for the Operation returned by CreateCluster.

func (CreateClusterMetadata) MarshalJSON ¶
func (s CreateClusterMetadata) MarshalJSON() ([]byte, error)
type CreateClusterRequest ¶
type CreateClusterRequest struct {
	// Cluster: Required. The cluster to be created. Fields marked `OutputOnly`
	// must be left blank.
	Cluster *Cluster `json:"cluster,omitempty"`
	// ClusterId: Required. The ID to be used when referring to the new cluster
	// within its instance, e.g., just `mycluster` rather than
	// `projects/myproject/instances/myinstance/clusters/mycluster`.
	ClusterId string `json:"clusterId,omitempty"`
	// Parent: Required. The unique name of the instance in which to create the new
	// cluster. Values are of the form `projects/{project}/instances/{instance}`.
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Cluster") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cluster") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateClusterRequest: Request message for BigtableInstanceAdmin.CreateCluster.

func (CreateClusterRequest) MarshalJSON ¶
func (s CreateClusterRequest) MarshalJSON() ([]byte, error)
type CreateInstanceMetadata ¶
type CreateInstanceMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// CreateInstance operation.
	OriginalRequest *CreateInstanceRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateInstanceMetadata: The metadata for the Operation returned by CreateInstance.

func (CreateInstanceMetadata) MarshalJSON ¶
func (s CreateInstanceMetadata) MarshalJSON() ([]byte, error)
type CreateInstanceRequest ¶
type CreateInstanceRequest struct {
	// Clusters: Required. The clusters to be created within the instance, mapped
	// by desired cluster ID, e.g., just `mycluster` rather than
	// `projects/myproject/instances/myinstance/clusters/mycluster`. Fields marked
	// `OutputOnly` must be left blank.
	Clusters map[string]Cluster `json:"clusters,omitempty"`
	// Instance: Required. The instance to create. Fields marked `OutputOnly` must
	// be left blank.
	Instance *Instance `json:"instance,omitempty"`
	// InstanceId: Required. The ID to be used when referring to the new instance
	// within its project, e.g., just `myinstance` rather than
	// `projects/myproject/instances/myinstance`.
	InstanceId string `json:"instanceId,omitempty"`
	// Parent: Required. The unique name of the project in which to create the new
	// instance. Values are of the form `projects/{project}`.
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Clusters") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Clusters") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateInstanceRequest: Request message for BigtableInstanceAdmin.CreateInstance.

func (CreateInstanceRequest) MarshalJSON ¶
func (s CreateInstanceRequest) MarshalJSON() ([]byte, error)
type CreateLogicalViewMetadata ¶
added in v0.227.0
type CreateLogicalViewMetadata struct {
	// EndTime: DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// CreateLogicalView operation.
	OriginalRequest *CreateLogicalViewRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// StartTime: DEPRECATED: Use request_time instead.
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

CreateLogicalViewMetadata: The metadata for the Operation returned by CreateLogicalView.

func (CreateLogicalViewMetadata) MarshalJSON ¶
added in v0.227.0
func (s CreateLogicalViewMetadata) MarshalJSON() ([]byte, error)
type CreateLogicalViewRequest ¶
added in v0.227.0
type CreateLogicalViewRequest struct {
	// LogicalView: Required. The logical view to create.
	LogicalView *LogicalView `json:"logicalView,omitempty"`
	// LogicalViewId: Required. The ID to use for the logical view, which will
	// become the final component of the logical view's resource name.
	LogicalViewId string `json:"logicalViewId,omitempty"`
	// Parent: Required. The parent instance where this logical view will be
	// created. Format: `projects/{project}/instances/{instance}`.
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LogicalView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LogicalView") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateLogicalViewRequest: Request message for BigtableInstanceAdmin.CreateLogicalView.

func (CreateLogicalViewRequest) MarshalJSON ¶
added in v0.227.0
func (s CreateLogicalViewRequest) MarshalJSON() ([]byte, error)
type CreateMaterializedViewMetadata ¶
added in v0.227.0
type CreateMaterializedViewMetadata struct {
	// EndTime: If set, the time at which this operation finished or was canceled.
	// DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// CreateMaterializedView operation.
	OriginalRequest *CreateMaterializedViewRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// StartTime: The time at which this operation started. DEPRECATED: Use
	// request_time instead.
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

CreateMaterializedViewMetadata: The metadata for the Operation returned by CreateMaterializedView.

func (CreateMaterializedViewMetadata) MarshalJSON ¶
added in v0.227.0
func (s CreateMaterializedViewMetadata) MarshalJSON() ([]byte, error)
type CreateMaterializedViewRequest ¶
added in v0.227.0
type CreateMaterializedViewRequest struct {
	// MaterializedView: Required. The materialized view to create.
	MaterializedView *MaterializedView `json:"materializedView,omitempty"`
	// MaterializedViewId: Required. The ID to use for the materialized view, which
	// will become the final component of the materialized view's resource name.
	MaterializedViewId string `json:"materializedViewId,omitempty"`
	// Parent: Required. The parent instance where this materialized view will be
	// created. Format: `projects/{project}/instances/{instance}`.
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaterializedView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaterializedView") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateMaterializedViewRequest: Request message for BigtableInstanceAdmin.CreateMaterializedView.

func (CreateMaterializedViewRequest) MarshalJSON ¶
added in v0.227.0
func (s CreateMaterializedViewRequest) MarshalJSON() ([]byte, error)
type CreateSchemaBundleMetadata ¶
added in v0.240.0
type CreateSchemaBundleMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// Name: The unique name identifying this schema bundle. Values are of the form
	// `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema
	// _bundle}`
	Name string `json:"name,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateSchemaBundleMetadata: The metadata for the Operation returned by CreateSchemaBundle.

func (CreateSchemaBundleMetadata) MarshalJSON ¶
added in v0.240.0
func (s CreateSchemaBundleMetadata) MarshalJSON() ([]byte, error)
type CreateTableRequest ¶
type CreateTableRequest struct {
	// InitialSplits: The optional list of row keys that will be used to initially
	// split the table into several tablets (tablets are similar to HBase regions).
	// Given two split keys, `s1` and `s2`, three tablets will be created, spanning
	// the key ranges: `[, s1), [s1, s2), [s2, )`. Example: * Row keys := `["a",
	// "apple", "custom", "customer_1", "customer_2",` "other", "zz"]` *
	// initial_split_keys := `["apple", "customer_1", "customer_2", "other"]` * Key
	// assignment: - Tablet 1 `[, apple) => {"a"}.` - Tablet 2 `[apple, customer_1)
	// => {"apple", "custom"}.` - Tablet 3 `[customer_1, customer_2) =>
	// {"customer_1"}.` - Tablet 4 `[customer_2, other) => {"customer_2"}.` -
	// Tablet 5 `[other, ) => {"other", "zz"}.`
	InitialSplits []*Split `json:"initialSplits,omitempty"`
	// Table: Required. The Table to create.
	Table *Table `json:"table,omitempty"`
	// TableId: Required. The name by which the new table should be referred to
	// within the parent instance, e.g., `foobar` rather than
	// `{parent}/tables/foobar`. Maximum 50 characters.
	TableId string `json:"tableId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InitialSplits") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InitialSplits") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateTableRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.CreateTable

func (CreateTableRequest) MarshalJSON ¶
func (s CreateTableRequest) MarshalJSON() ([]byte, error)
type DataBoostIsolationReadOnly ¶
added in v0.172.0
type DataBoostIsolationReadOnly struct {
	// ComputeBillingOwner: The Compute Billing Owner for this Data Boost App
	// Profile.
	//
	// Possible values:
	//   "COMPUTE_BILLING_OWNER_UNSPECIFIED" - Unspecified value.
	//   "HOST_PAYS" - The host Cloud Project containing the targeted Bigtable
	// Instance / Table pays for compute.
	ComputeBillingOwner string `json:"computeBillingOwner,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ComputeBillingOwner") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ComputeBillingOwner") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DataBoostIsolationReadOnly: Data Boost is a serverless compute capability that lets you run high-throughput read jobs and queries on your Bigtable data, without impacting the performance of the clusters that handle your application traffic. Data Boost supports read-only use cases with single-cluster routing.

func (DataBoostIsolationReadOnly) MarshalJSON ¶
added in v0.172.0
func (s DataBoostIsolationReadOnly) MarshalJSON() ([]byte, error)
type DataBoostReadLocalWrites ¶
added in v0.172.0
type DataBoostReadLocalWrites struct {
}

DataBoostReadLocalWrites: Checks that all writes before the consistency token was generated in the same cluster are readable by Databoost.

type DropRowRangeRequest ¶
type DropRowRangeRequest struct {
	// DeleteAllDataFromTable: Delete all rows in the table. Setting this to false
	// is a no-op.
	DeleteAllDataFromTable bool `json:"deleteAllDataFromTable,omitempty"`
	// RowKeyPrefix: Delete all rows that start with this row key prefix. Prefix
	// cannot be zero length.
	RowKeyPrefix string `json:"rowKeyPrefix,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeleteAllDataFromTable") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeleteAllDataFromTable") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DropRowRangeRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange

func (DropRowRangeRequest) MarshalJSON ¶
func (s DropRowRangeRequest) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EncryptionConfig ¶
added in v0.44.0
type EncryptionConfig struct {
	// KmsKeyName: Describes the Cloud KMS encryption key that will be used to
	// protect the destination Bigtable cluster. The requirements for this key are:
	// 1) The Cloud Bigtable service account associated with the project that
	// contains this cluster must be granted the
	// `cloudkms.cryptoKeyEncrypterDecrypter` role on the CMEK key. 2) Only
	// regional keys can be used and the region of the CMEK key must match the
	// region of the cluster. Values are of the form
	// `projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}`
	KmsKeyName string `json:"kmsKeyName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "KmsKeyName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KmsKeyName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EncryptionConfig: Cloud Key Management Service (Cloud KMS) settings for a CMEK-protected cluster.

func (EncryptionConfig) MarshalJSON ¶
added in v0.44.0
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EncryptionInfo ¶
added in v0.44.0
type EncryptionInfo struct {
	// EncryptionStatus: Output only. The status of encrypt/decrypt calls on
	// underlying data for this resource. Regardless of status, the existing data
	// is always encrypted at rest.
	EncryptionStatus *Status `json:"encryptionStatus,omitempty"`
	// EncryptionType: Output only. The type of encryption used to protect this
	// resource.
	//
	// Possible values:
	//   "ENCRYPTION_TYPE_UNSPECIFIED" - Encryption type was not specified, though
	// data at rest remains encrypted.
	//   "GOOGLE_DEFAULT_ENCRYPTION" - The data backing this resource is encrypted
	// at rest with a key that is fully managed by Google. No key version or status
	// will be populated. This is the default state.
	//   "CUSTOMER_MANAGED_ENCRYPTION" - The data backing this resource is
	// encrypted at rest with a key that is managed by the customer. The in-use
	// version of the key and its status are populated for CMEK-protected tables.
	// CMEK-protected backups are pinned to the key version that was in use at the
	// time the backup was taken. This key version is populated but its status is
	// not tracked and is reported as `UNKNOWN`.
	EncryptionType string `json:"encryptionType,omitempty"`
	// KmsKeyVersion: Output only. The version of the Cloud KMS key specified in
	// the parent cluster that is in use for the data underlying this table.
	KmsKeyVersion string `json:"kmsKeyVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EncryptionStatus") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EncryptionStatus") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EncryptionInfo: Encryption information for a given resource. If this resource is protected with customer managed encryption, the in-use Cloud Key Management Service (Cloud KMS) key version is specified along with its status.

func (EncryptionInfo) MarshalJSON ¶
added in v0.44.0
func (s EncryptionInfo) MarshalJSON() ([]byte, error)
type Expr ¶
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
func (s Expr) MarshalJSON() ([]byte, error)
type GcRule ¶
type GcRule struct {
	// Intersection: Delete cells that would be deleted by every nested rule.
	Intersection *Intersection `json:"intersection,omitempty"`
	// MaxAge: Delete cells in a column older than the given age. Values must be at
	// least one millisecond, and will be truncated to microsecond granularity.
	MaxAge string `json:"maxAge,omitempty"`
	// MaxNumVersions: Delete all cells in a column except the most recent N.
	MaxNumVersions int64 `json:"maxNumVersions,omitempty"`
	// Union: Delete cells that would be deleted by any nested rule.
	Union *Union `json:"union,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Intersection") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Intersection") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GcRule: Rule for determining which cells to delete during garbage collection.

func (GcRule) MarshalJSON ¶
func (s GcRule) MarshalJSON() ([]byte, error)
type GenerateConsistencyTokenRequest ¶
type GenerateConsistencyTokenRequest struct {
}

GenerateConsistencyTokenRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.GenerateConsistencyToken

type GenerateConsistencyTokenResponse ¶
type GenerateConsistencyTokenResponse struct {
	// ConsistencyToken: The generated consistency token.
	ConsistencyToken string `json:"consistencyToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ConsistencyToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsistencyToken") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GenerateConsistencyTokenResponse: Response message for google.bigtable.admin.v2.BigtableTableAdmin.GenerateConsistencyToken

func (GenerateConsistencyTokenResponse) MarshalJSON ¶
func (s GenerateConsistencyTokenResponse) MarshalJSON() ([]byte, error)
type GetIamPolicyRequest ¶
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
added in v0.10.0
func (s GetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GetPolicyOptions ¶
added in v0.10.0
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
added in v0.10.0
func (s GetPolicyOptions) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2AuthorizedViewFamilySubsets ¶
added in v0.171.0
type GoogleBigtableAdminV2AuthorizedViewFamilySubsets struct {
	// QualifierPrefixes: Prefixes for qualifiers to be included in the
	// AuthorizedView. Every qualifier starting with one of these prefixes is
	// included in the AuthorizedView. To provide access to all qualifiers, include
	// the empty string as a prefix ("").
	QualifierPrefixes []string `json:"qualifierPrefixes,omitempty"`
	// Qualifiers: Individual exact column qualifiers to be included in the
	// AuthorizedView.
	Qualifiers []string `json:"qualifiers,omitempty"`
	// ForceSendFields is a list of field names (e.g. "QualifierPrefixes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "QualifierPrefixes") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2AuthorizedViewFamilySubsets: Subsets of a column family that are included in this AuthorizedView.

func (GoogleBigtableAdminV2AuthorizedViewFamilySubsets) MarshalJSON ¶
added in v0.171.0
func (s GoogleBigtableAdminV2AuthorizedViewFamilySubsets) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2AuthorizedViewSubsetView ¶
added in v0.171.0
type GoogleBigtableAdminV2AuthorizedViewSubsetView struct {
	// FamilySubsets: Map from column family name to the columns in this family to
	// be included in the AuthorizedView.
	FamilySubsets map[string]GoogleBigtableAdminV2AuthorizedViewFamilySubsets `json:"familySubsets,omitempty"`
	// RowPrefixes: Row prefixes to be included in the AuthorizedView. To provide
	// access to all rows, include the empty string as a prefix ("").
	RowPrefixes []string `json:"rowPrefixes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FamilySubsets") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FamilySubsets") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2AuthorizedViewSubsetView: Defines a simple AuthorizedView that is a subset of the underlying Table.

func (GoogleBigtableAdminV2AuthorizedViewSubsetView) MarshalJSON ¶
added in v0.171.0
func (s GoogleBigtableAdminV2AuthorizedViewSubsetView) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2MaterializedViewClusterState ¶
added in v0.253.0
type GoogleBigtableAdminV2MaterializedViewClusterState struct {
	// ReplicationState: Output only. The state of the materialized view in this
	// cluster.
	//
	// Possible values:
	//   "STATE_NOT_KNOWN" - The state of the materialized view is unknown in this
	// cluster.
	//   "INITIALIZING" - The cluster or view was recently created, and the
	// materialized view must finish backfilling before it can begin serving Data
	// API requests.
	//   "READY" - The materialized view can serve Data API requests from this
	// cluster. Depending on materialization and replication delay, reads may not
	// immediately reflect the state of the materialized view in other clusters.
	ReplicationState string `json:"replicationState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReplicationState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReplicationState") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2MaterializedViewClusterState: The state of a materialized view's data in a particular cluster.

func (GoogleBigtableAdminV2MaterializedViewClusterState) MarshalJSON ¶
added in v0.253.0
func (s GoogleBigtableAdminV2MaterializedViewClusterState) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeAggregate ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeAggregate struct {
	// HllppUniqueCount: HyperLogLogPlusPlusUniqueCount aggregator.
	HllppUniqueCount *GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount `json:"hllppUniqueCount,omitempty"`
	// InputType: Type of the inputs that are accumulated by this `Aggregate`. Use
	// `AddInput` mutations to accumulate new inputs.
	InputType *Type `json:"inputType,omitempty"`
	// Max: Max aggregator.
	Max *GoogleBigtableAdminV2TypeAggregateMax `json:"max,omitempty"`
	// Min: Min aggregator.
	Min *GoogleBigtableAdminV2TypeAggregateMin `json:"min,omitempty"`
	// StateType: Output only. Type that holds the internal accumulator state for
	// the `Aggregate`. This is a function of the `input_type` and `aggregator`
	// chosen.
	StateType *Type `json:"stateType,omitempty"`
	// Sum: Sum aggregator.
	Sum *GoogleBigtableAdminV2TypeAggregateSum `json:"sum,omitempty"`
	// ForceSendFields is a list of field names (e.g. "HllppUniqueCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HllppUniqueCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeAggregate: A value that combines incremental updates into a summarized value. Data is never directly written or read using type `Aggregate`. Writes provide either the `input_type` or `state_type`, and reads always return the `state_type` .

func (GoogleBigtableAdminV2TypeAggregate) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeAggregate) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount struct {
}

GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount: Computes an approximate unique count over the input values. When using raw data as input, be careful to use a consistent encoding. Otherwise the same value encoded differently could count more than once, or two distinct values could count as identical. Input: Any, or omit for Raw State: TBD Special state conversions: `Int64` (the unique count estimate)

type GoogleBigtableAdminV2TypeAggregateMax ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeAggregateMax struct {
}

GoogleBigtableAdminV2TypeAggregateMax: Computes the max of the input values. Allowed input: `Int64` State: same as input

type GoogleBigtableAdminV2TypeAggregateMin ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeAggregateMin struct {
}

GoogleBigtableAdminV2TypeAggregateMin: Computes the min of the input values. Allowed input: `Int64` State: same as input

type GoogleBigtableAdminV2TypeAggregateSum ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeAggregateSum struct {
}

GoogleBigtableAdminV2TypeAggregateSum: Computes the sum of the input values. Allowed input: `Int64` State: same as input

type GoogleBigtableAdminV2TypeArray ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeArray struct {
	// ElementType: The type of the elements in the array. This must not be
	// `Array`.
	ElementType *Type `json:"elementType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ElementType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ElementType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeArray: An ordered list of elements of a given type. Values of type `Array` are stored in `Value.array_value`.

func (GoogleBigtableAdminV2TypeArray) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeArray) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBool ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeBool struct {
}

GoogleBigtableAdminV2TypeBool: bool Values of type `Bool` are stored in `Value.bool_value`.

type GoogleBigtableAdminV2TypeBytes ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeBytes struct {
	// Encoding: The encoding to use when converting to or from lower level types.
	Encoding *GoogleBigtableAdminV2TypeBytesEncoding `json:"encoding,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Encoding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Encoding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeBytes: Bytes Values of type `Bytes` are stored in `Value.bytes_value`.

func (GoogleBigtableAdminV2TypeBytes) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBytesEncoding ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeBytesEncoding struct {
	// Raw: Use `Raw` encoding.
	Raw *GoogleBigtableAdminV2TypeBytesEncodingRaw `json:"raw,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Raw") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Raw") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeBytesEncoding: Rules used to convert to or from lower level types.

func (GoogleBigtableAdminV2TypeBytesEncoding) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeBytesEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeBytesEncodingRaw ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeBytesEncodingRaw struct {
	// EscapeNulls: If set, allows NULL values to be encoded as the empty string
	// "". The actual empty string, or any value which only contains the null byte
	// `0x00`, has one more null byte appended.
	EscapeNulls bool `json:"escapeNulls,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EscapeNulls") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EscapeNulls") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeBytesEncodingRaw: Leaves the value as-is. Sorted mode: all values are supported. Distinct mode: all values are supported.

func (GoogleBigtableAdminV2TypeBytesEncodingRaw) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeBytesEncodingRaw) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeDate ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeDate struct {
}

GoogleBigtableAdminV2TypeDate: Date Values of type `Date` are stored in `Value.date_value`.

type GoogleBigtableAdminV2TypeEnum ¶
added in v0.244.0
type GoogleBigtableAdminV2TypeEnum struct {
	// EnumName: The fully qualified name of the protobuf enum message, including
	// package. In the format of "foo.bar.EnumMessage".
	EnumName string `json:"enumName,omitempty"`
	// SchemaBundleId: The ID of the schema bundle that this enum is defined in.
	SchemaBundleId string `json:"schemaBundleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnumName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnumName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeEnum: A protobuf enum type. Values of type `Enum` are stored in `Value.int_value`.

func (GoogleBigtableAdminV2TypeEnum) MarshalJSON ¶
added in v0.244.0
func (s GoogleBigtableAdminV2TypeEnum) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeFloat32 ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeFloat32 struct {
}

GoogleBigtableAdminV2TypeFloat32: Float32 Values of type `Float32` are stored in `Value.float_value`.

type GoogleBigtableAdminV2TypeFloat64 ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeFloat64 struct {
}

GoogleBigtableAdminV2TypeFloat64: Float64 Values of type `Float64` are stored in `Value.float_value`.

type GoogleBigtableAdminV2TypeGeography ¶
added in v0.267.0
type GoogleBigtableAdminV2TypeGeography struct {
}

GoogleBigtableAdminV2TypeGeography: A geography type, representing a point or region on Earth. The value is stored in `Value.bytes_value` as Well-Known Binary (WKB) bytes.

type GoogleBigtableAdminV2TypeInt64 ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeInt64 struct {
	// Encoding: The encoding to use when converting to or from lower level types.
	Encoding *GoogleBigtableAdminV2TypeInt64Encoding `json:"encoding,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Encoding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Encoding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeInt64: Int64 Values of type `Int64` are stored in `Value.int_value`.

func (GoogleBigtableAdminV2TypeInt64) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeInt64) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64Encoding ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeInt64Encoding struct {
	// BigEndianBytes: Use `BigEndianBytes` encoding.
	BigEndianBytes *GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes `json:"bigEndianBytes,omitempty"`
	// OrderedCodeBytes: Use `OrderedCodeBytes` encoding.
	OrderedCodeBytes *GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes `json:"orderedCodeBytes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BigEndianBytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BigEndianBytes") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeInt64Encoding: Rules used to convert to or from lower level types.

func (GoogleBigtableAdminV2TypeInt64Encoding) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeInt64Encoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes ¶
added in v0.172.0
type GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes struct {
	// BytesType: Deprecated: ignored if set.
	BytesType *GoogleBigtableAdminV2TypeBytes `json:"bytesType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BytesType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BytesType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes: Encodes the value as an 8-byte big-endian two's complement value. Sorted mode: non-negative values are supported. Distinct mode: all values are supported. Compatible with: - BigQuery `BINARY` encoding - HBase `Bytes.toBytes` - Java `ByteBuffer.putLong()` with `ByteOrder.BIG_ENDIAN`

func (GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes) MarshalJSON ¶
added in v0.172.0
func (s GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes struct {
}

GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes: Encodes the value in a variable length binary format of up to 10 bytes. Values that are closer to zero use fewer bytes. Sorted mode: all values are supported. Distinct mode: all values are supported.

type GoogleBigtableAdminV2TypeMap ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeMap struct {
	// KeyType: The type of a map key. Only `Bytes`, `String`, and `Int64` are
	// allowed as key types.
	KeyType *Type `json:"keyType,omitempty"`
	// ValueType: The type of the values in a map.
	ValueType *Type `json:"valueType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "KeyType") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KeyType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeMap: A mapping of keys to values of a given type. Values of type `Map` are stored in a `Value.array_value` where each entry is another `Value.array_value` with two elements (the key and the value, in that order). Normally encoded Map values won't have repeated keys, however, clients are expected to handle the case in which they do. If the same key appears multiple times, the _last_ value takes precedence.

func (GoogleBigtableAdminV2TypeMap) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeMap) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeProto ¶
added in v0.244.0
type GoogleBigtableAdminV2TypeProto struct {
	// MessageName: The fully qualified name of the protobuf message, including
	// package. In the format of "foo.bar.Message".
	MessageName string `json:"messageName,omitempty"`
	// SchemaBundleId: The ID of the schema bundle that this proto is defined in.
	SchemaBundleId string `json:"schemaBundleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MessageName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MessageName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeProto: A protobuf message type. Values of type `Proto` are stored in `Value.bytes_value`.

func (GoogleBigtableAdminV2TypeProto) MarshalJSON ¶
added in v0.244.0
func (s GoogleBigtableAdminV2TypeProto) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeString ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeString struct {
	// Encoding: The encoding to use when converting to or from lower level types.
	Encoding *GoogleBigtableAdminV2TypeStringEncoding `json:"encoding,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Encoding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Encoding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeString: String Values of type `String` are stored in `Value.string_value`.

func (GoogleBigtableAdminV2TypeString) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeString) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncoding ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeStringEncoding struct {
	// Utf8Bytes: Use `Utf8Bytes` encoding.
	Utf8Bytes *GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes `json:"utf8Bytes,omitempty"`
	// Utf8Raw: Deprecated: if set, converts to an empty `utf8_bytes`.
	Utf8Raw *GoogleBigtableAdminV2TypeStringEncodingUtf8Raw `json:"utf8Raw,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Utf8Bytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Utf8Bytes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStringEncoding: Rules used to convert to or from lower level types.

func (GoogleBigtableAdminV2TypeStringEncoding) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeStringEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes struct {
	// NullEscapeChar: Single-character escape sequence used to support NULL
	// values. If set, allows NULL values to be encoded as the empty string "". The
	// actual empty string, or any value where every character equals
	// `null_escape_char`, has one more `null_escape_char` appended. If
	// `null_escape_char` is set and does not equal the ASCII null character
	// `0x00`, then the encoding will not support sorted mode. .
	NullEscapeChar string `json:"nullEscapeChar,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NullEscapeChar") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NullEscapeChar") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes: UTF-8 encoding. Sorted mode: - All values are supported. - Code point order is preserved. Distinct mode: all values are supported. Compatible with: - BigQuery `TEXT` encoding - HBase `Bytes.toBytes` - Java `String#getBytes(StandardCharsets.UTF_8)`

func (GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStringEncodingUtf8Raw ¶
added in v0.190.0
type GoogleBigtableAdminV2TypeStringEncodingUtf8Raw struct {
}

GoogleBigtableAdminV2TypeStringEncodingUtf8Raw: Deprecated: prefer the equivalent `Utf8Bytes`.

type GoogleBigtableAdminV2TypeStruct ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeStruct struct {
	// Encoding: The encoding to use when converting to or from lower level types.
	Encoding *GoogleBigtableAdminV2TypeStructEncoding `json:"encoding,omitempty"`
	// Fields: The names and types of the fields in this struct.
	Fields []*GoogleBigtableAdminV2TypeStructField `json:"fields,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Encoding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Encoding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStruct: A structured data value, consisting of fields which map to dynamically typed values. Values of type `Struct` are stored in `Value.array_value` where entries are in the same order and number as `field_types`.

func (GoogleBigtableAdminV2TypeStruct) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeStruct) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncoding ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeStructEncoding struct {
	// DelimitedBytes: Use `DelimitedBytes` encoding.
	DelimitedBytes *GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes `json:"delimitedBytes,omitempty"`
	// OrderedCodeBytes: User `OrderedCodeBytes` encoding.
	OrderedCodeBytes *GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes `json:"orderedCodeBytes,omitempty"`
	// Singleton: Use `Singleton` encoding.
	Singleton *GoogleBigtableAdminV2TypeStructEncodingSingleton `json:"singleton,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DelimitedBytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DelimitedBytes") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStructEncoding: Rules used to convert to or from lower level types.

func (GoogleBigtableAdminV2TypeStructEncoding) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeStructEncoding) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes struct {
	// Delimiter: Byte sequence used to delimit concatenated fields. The delimiter
	// must contain at least 1 character and at most 50 characters.
	Delimiter string `json:"delimiter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Delimiter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Delimiter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes: Fields are encoded independently and concatenated with a configurable `delimiter` in between. A struct with no fields defined is encoded as a single `delimiter`. Sorted mode: - Fields are encoded in sorted mode. - Encoded field values must not contain any bytes <= `delimiter[0]` - Element-wise order is preserved: `A < B` if `A[0] < B[0]`, or if `A[0] == B[0] && A[1] < B[1]`, etc. Strict prefixes sort first. - This encoding does not support `DESC` field ordering. Distinct mode: - Fields are encoded in distinct mode. - Encoded field values must not contain `delimiter[0]`.

func (GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes struct {
}

GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes: Fields are encoded independently, then escaped and delimited by appling the following rules in order: - While the last remaining field is `ASC` or `UNSPECIFIED`, and encodes to the empty string "", remove it. - In each remaining field, replace all null bytes `0x00` with the fixed byte pair `{0x00, 0xFF}`. - If any remaining field encodes to the empty string "", replace it with the fixed byte pair `{0x00, 0x00}`. - Append the fixed byte pair `{0x00, 0x01}` to each remaining field, except for the last remaining field if it is `ASC`. - Bitwise negate all `DESC` fields. - Concatenate the results, or emit the fixed byte pair `{0x00, 0x00}` if there are no remaining fields to concatenate. Examples: ``` - STRUCT() -> "\00\00" - STRUCT("") -> "\00\00" - STRUCT("", "") -> "\00\00" - STRUCT("", "B") -> "\00\00" + "\00\01" + "B" - STRUCT("A", "") -> "A" - STRUCT("", "B", "") -> "\00\00" + "\00\01" + "B" - STRUCT("A", "", "C") -> "A" + "\00\01" + "\00\00" + "\00\01" + "C" ``` Examples for struct with `DESC` fields: ``` - STRUCT("" DESC) -> "\xFF\xFF" + "\xFF\xFE" - STRUCT("" DESC, "") -> "\xFF\xFF" + "\xFF\xFE" - STRUCT("" DESC, "", "") -> "\xFF\xFF" + "\xFF\xFE" - STRUCT("" DESC, "A") -> "\xFF\xFF" + "\xFF\xFE" + "A" - STRUCT("A", "" DESC, "") -> "A" + "\00\01" + "\xFF\xFF" + "\xFF\xFE" - STRUCT("", "A" DESC) -> "\x00\x00" + "\x00\x01" + "\xBE" + "\xFF\xFE" ``` Since null bytes are always escaped, this encoding can cause size blowup for encodings like `Int64.BigEndianBytes` that are likely to produce many such bytes. Sorted mode: - Fields are encoded in sorted mode. - All values supported by the field encodings are allowed. - Fields with unset or `UNSPECIFIED` order are treated as `ASC`. - Element-wise order is preserved: `A < B` if `A[0] < B[0]`, or if `A[0] == B[0] && A[1] < B[1]`, etc. Strict prefixes sort first. Distinct mode: - Fields are encoded in distinct mode. - All values supported by the field encodings are allowed.

type GoogleBigtableAdminV2TypeStructEncodingSingleton ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeStructEncodingSingleton struct {
}

GoogleBigtableAdminV2TypeStructEncodingSingleton: Uses the encoding of `fields[0].type` as-is. Only valid if `fields.size == 1`. This encoding does not support `DESC` field ordering.

type GoogleBigtableAdminV2TypeStructField ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeStructField struct {
	// FieldName: The field name (optional). Fields without a `field_name` are
	// considered anonymous and cannot be referenced by name.
	FieldName string `json:"fieldName,omitempty"`
	// Type: The type of values in this field.
	Type *Type `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeStructField: A struct field and its type.

func (GoogleBigtableAdminV2TypeStructField) MarshalJSON ¶
added in v0.189.0
func (s GoogleBigtableAdminV2TypeStructField) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeTimestamp ¶
added in v0.189.0
type GoogleBigtableAdminV2TypeTimestamp struct {
	// Encoding: The encoding to use when converting to or from lower level types.
	Encoding *GoogleBigtableAdminV2TypeTimestampEncoding `json:"encoding,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Encoding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Encoding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeTimestamp: Timestamp Values of type `Timestamp` are stored in `Value.timestamp_value`.

func (GoogleBigtableAdminV2TypeTimestamp) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeTimestamp) MarshalJSON() ([]byte, error)
type GoogleBigtableAdminV2TypeTimestampEncoding ¶
added in v0.225.0
type GoogleBigtableAdminV2TypeTimestampEncoding struct {
	// UnixMicrosInt64: Encodes the number of microseconds since the Unix epoch
	// using the given `Int64` encoding. Values must be microsecond-aligned.
	// Compatible with: - Java `Instant.truncatedTo()` with `ChronoUnit.MICROS`
	UnixMicrosInt64 *GoogleBigtableAdminV2TypeInt64Encoding `json:"unixMicrosInt64,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UnixMicrosInt64") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UnixMicrosInt64") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleBigtableAdminV2TypeTimestampEncoding: Rules used to convert to or from lower level types.

func (GoogleBigtableAdminV2TypeTimestampEncoding) MarshalJSON ¶
added in v0.225.0
func (s GoogleBigtableAdminV2TypeTimestampEncoding) MarshalJSON() ([]byte, error)
type HotTablet ¶
added in v0.75.0
type HotTablet struct {
	// EndKey: Tablet End Key (inclusive).
	EndKey string `json:"endKey,omitempty"`
	// EndTime: Output only. The end time of the hot tablet.
	EndTime string `json:"endTime,omitempty"`
	// Name: The unique name of the hot tablet. Values are of the form
	// `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-
	// Z0-9_-]*`.
	Name string `json:"name,omitempty"`
	// NodeCpuUsagePercent: Output only. The average CPU usage spent by a node on
	// this tablet over the start_time to end_time time range. The percentage is
	// the amount of CPU used by the node to serve the tablet, from 0% (tablet was
	// not interacted with) to 100% (the node spent all cycles serving the hot
	// tablet).
	NodeCpuUsagePercent float64 `json:"nodeCpuUsagePercent,omitempty"`
	// StartKey: Tablet Start Key (inclusive).
	StartKey string `json:"startKey,omitempty"`
	// StartTime: Output only. The start time of the hot tablet.
	StartTime string `json:"startTime,omitempty"`
	// TableName: Name of the table that contains the tablet. Values are of the
	// form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`.
	TableName string `json:"tableName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndKey") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndKey") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

HotTablet: A tablet is a defined by a start and end key and is explained in https://cloud.google.com/bigtable/docs/overview#architecture and https://cloud.google.com/bigtable/docs/performance#optimization. A Hot tablet is a tablet that exhibits high average cpu usage during the time interval from start time to end time.

func (HotTablet) MarshalJSON ¶
added in v0.75.0
func (s HotTablet) MarshalJSON() ([]byte, error)
func (*HotTablet) UnmarshalJSON ¶
added in v0.75.0
func (s *HotTablet) UnmarshalJSON(data []byte) error
type Instance ¶
type Instance struct {
	// CreateTime: Output only. A commit timestamp representing when this Instance
	// was created. For instances created before this field was added (August
	// 2021), this value is `seconds: 0, nanos: 1`.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Required. The descriptive name for this instance as it appears
	// in UIs. Can be changed at any time, but should be kept globally unique to
	// avoid confusion.
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Labels are a flexible and lightweight mechanism for organizing cloud
	// resources into groups that reflect a customer's organizational needs and
	// deployment strategies. They can be used to filter resources and aggregate
	// metrics. * Label keys must be between 1 and 63 characters long and must
	// conform to the regular expression: `\p{Ll}\p{Lo}{0,62}`. * Label values must
	// be between 0 and 63 characters long and must conform to the regular
	// expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * No more than 64 labels can be
	// associated with a given resource. * Keys and values must both be under 128
	// bytes.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: The unique name of the instance. Values are of the form
	// `projects/{project}/instances/a-z+[a-z0-9]`.
	Name string `json:"name,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// State: Output only. The current state of the instance.
	//
	// Possible values:
	//   "STATE_NOT_KNOWN" - The state of the instance could not be determined.
	//   "READY" - The instance has been successfully created and can serve
	// requests to its tables.
	//   "CREATING" - The instance is currently being created, and may be destroyed
	// if the creation process encounters an error.
	State string `json:"state,omitempty"`
	// Tags: Optional. Input only. Immutable. Tag keys/values directly bound to
	// this resource. For example: - "123/environment": "production", -
	// "123/costCenter": "marketing" Tags and Labels (above) are both used to bind
	// metadata to resources, with different use-cases. See
	// https://cloud.google.com/resource-manager/docs/tags/tags-overview for an
	// in-depth overview on the difference between tags and labels.
	Tags map[string]string `json:"tags,omitempty"`
	// Type: The type of the instance. Defaults to `PRODUCTION`.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - The type of the instance is unspecified. If set when
	// creating an instance, a `PRODUCTION` instance will be created. If set when
	// updating an instance, the type will be left unchanged.
	//   "PRODUCTION" - An instance meant for production use. `serve_nodes` must be
	// set on the cluster.
	//   "DEVELOPMENT" - DEPRECATED: Prefer PRODUCTION for all use cases, as it no
	// longer enforces a higher minimum node count than DEVELOPMENT.
	Type string `json:"type,omitempty"`

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

Instance: A collection of Bigtable Tables and the resources that serve them. All tables in an instance are served from all Clusters in the instance.

func (Instance) MarshalJSON ¶
func (s Instance) MarshalJSON() ([]byte, error)
type Intersection ¶
type Intersection struct {
	// Rules: Only delete cells which would be deleted by every element of `rules`.
	Rules []*GcRule `json:"rules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Rules") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Rules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Intersection: A GcRule which deletes cells matching all of the given rules.

func (Intersection) MarshalJSON ¶
func (s Intersection) MarshalJSON() ([]byte, error)
type ListAppProfilesResponse ¶
type ListAppProfilesResponse struct {
	// AppProfiles: The list of requested app profiles.
	AppProfiles []*AppProfile `json:"appProfiles,omitempty"`
	// FailedLocations: Locations from which AppProfile information could not be
	// retrieved, due to an outage or some other transient condition. AppProfiles
	// from these locations may be missing from `app_profiles`. Values are of the
	// form `projects//locations/`
	FailedLocations []string `json:"failedLocations,omitempty"`
	// NextPageToken: Set if not all app profiles could be returned in a single
	// response. Pass this value to `page_token` in another request to get the next
	// page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppProfiles") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppProfiles") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAppProfilesResponse: Response message for BigtableInstanceAdmin.ListAppProfiles.

func (ListAppProfilesResponse) MarshalJSON ¶
func (s ListAppProfilesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedViewsResponse ¶
added in v0.171.0
type ListAuthorizedViewsResponse struct {
	// AuthorizedViews: The AuthorizedViews present in the requested table.
	AuthorizedViews []*AuthorizedView `json:"authorizedViews,omitempty"`
	// NextPageToken: Set if not all tables could be returned in a single response.
	// Pass this value to `page_token` in another request to get the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuthorizedViews") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthorizedViews") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAuthorizedViewsResponse: Response message for google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews

func (ListAuthorizedViewsResponse) MarshalJSON ¶
added in v0.171.0
func (s ListAuthorizedViewsResponse) MarshalJSON() ([]byte, error)
type ListBackupsResponse ¶
added in v0.30.0
type ListBackupsResponse struct {
	// Backups: The list of matching backups.
	Backups []*Backup `json:"backups,omitempty"`
	// NextPageToken: `next_page_token` can be sent in a subsequent ListBackups
	// call to fetch more of the matching backups.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Backups") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Backups") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBackupsResponse: The response for ListBackups.

func (ListBackupsResponse) MarshalJSON ¶
added in v0.30.0
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListClustersResponse ¶
type ListClustersResponse struct {
	// Clusters: The list of requested clusters.
	Clusters []*Cluster `json:"clusters,omitempty"`
	// FailedLocations: Locations from which Cluster information could not be
	// retrieved, due to an outage or some other transient condition. Clusters from
	// these locations may be missing from `clusters`, or may only have partial
	// information returned. Values are of the form `projects//locations/`
	FailedLocations []string `json:"failedLocations,omitempty"`
	// NextPageToken: DEPRECATED: This field is unused and ignored.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Clusters") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Clusters") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListClustersResponse: Response message for BigtableInstanceAdmin.ListClusters.

func (ListClustersResponse) MarshalJSON ¶
func (s ListClustersResponse) MarshalJSON() ([]byte, error)
type ListHotTabletsResponse ¶
added in v0.75.0
type ListHotTabletsResponse struct {
	// HotTablets: List of hot tablets in the tables of the requested cluster that
	// fall within the requested time range. Hot tablets are ordered by node cpu
	// usage percent. If there are multiple hot tablets that correspond to the same
	// tablet within a 15-minute interval, only the hot tablet with the highest
	// node cpu usage will be included in the response.
	HotTablets []*HotTablet `json:"hotTablets,omitempty"`
	// NextPageToken: Set if not all hot tablets could be returned in a single
	// response. Pass this value to `page_token` in another request to get the next
	// page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "HotTablets") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HotTablets") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListHotTabletsResponse: Response message for BigtableInstanceAdmin.ListHotTablets.

func (ListHotTabletsResponse) MarshalJSON ¶
added in v0.75.0
func (s ListHotTabletsResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse ¶
type ListInstancesResponse struct {
	// FailedLocations: Locations from which Instance information could not be
	// retrieved, due to an outage or some other transient condition. Instances
	// whose Clusters are all in one of the failed locations may be missing from
	// `instances`, and Instances with at least one Cluster in a failed location
	// may only have partial information returned. Values are of the form
	// `projects//locations/`
	FailedLocations []string `json:"failedLocations,omitempty"`
	// Instances: The list of requested instances.
	Instances []*Instance `json:"instances,omitempty"`
	// NextPageToken: DEPRECATED: This field is unused and ignored.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FailedLocations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FailedLocations") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListInstancesResponse: Response message for BigtableInstanceAdmin.ListInstances.

func (ListInstancesResponse) MarshalJSON ¶
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse ¶
added in v0.7.0
type ListLocationsResponse struct {
	// Locations: A list of locations that matches the specified filter in the
	// request.
	Locations []*Location `json:"locations,omitempty"`
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

ListLocationsResponse: The response message for Locations.ListLocations.

func (ListLocationsResponse) MarshalJSON ¶
added in v0.7.0
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListLogicalViewsResponse ¶
added in v0.230.0
type ListLogicalViewsResponse struct {
	// LogicalViews: The list of requested logical views.
	LogicalViews []*LogicalView `json:"logicalViews,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "LogicalViews") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LogicalViews") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListLogicalViewsResponse: Response message for BigtableInstanceAdmin.ListLogicalViews.

func (ListLogicalViewsResponse) MarshalJSON ¶
added in v0.230.0
func (s ListLogicalViewsResponse) MarshalJSON() ([]byte, error)
type ListMaterializedViewsResponse ¶
added in v0.230.0
type ListMaterializedViewsResponse struct {
	// MaterializedViews: The list of requested materialized views.
	MaterializedViews []*MaterializedView `json:"materializedViews,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "MaterializedViews") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaterializedViews") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListMaterializedViewsResponse: Response message for BigtableInstanceAdmin.ListMaterializedViews.

func (ListMaterializedViewsResponse) MarshalJSON ¶
added in v0.230.0
func (s ListMaterializedViewsResponse) MarshalJSON() ([]byte, error)
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
type ListSchemaBundlesResponse ¶
added in v0.240.0
type ListSchemaBundlesResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SchemaBundles: The schema bundles from the specified table.
	SchemaBundles []*SchemaBundle `json:"schemaBundles,omitempty"`

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

ListSchemaBundlesResponse: The response for ListSchemaBundles.

func (ListSchemaBundlesResponse) MarshalJSON ¶
added in v0.240.0
func (s ListSchemaBundlesResponse) MarshalJSON() ([]byte, error)
type ListTablesResponse ¶
type ListTablesResponse struct {
	// NextPageToken: Set if not all tables could be returned in a single response.
	// Pass this value to `page_token` in another request to get the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Tables: The tables present in the requested instance.
	Tables []*Table `json:"tables,omitempty"`

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

ListTablesResponse: Response message for google.bigtable.admin.v2.BigtableTableAdmin.ListTables

func (ListTablesResponse) MarshalJSON ¶
func (s ListTablesResponse) MarshalJSON() ([]byte, error)
type Location ¶
added in v0.7.0
type Location struct {
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

Location: A resource that represents a Google Cloud location.

func (Location) MarshalJSON ¶
added in v0.7.0
func (s Location) MarshalJSON() ([]byte, error)
type LogicalView ¶
added in v0.227.0
type LogicalView struct {
	// DeletionProtection: Optional. Set to true to make the LogicalView protected
	// against deletion.
	DeletionProtection bool `json:"deletionProtection,omitempty"`
	// Etag: Optional. The etag for this logical view. This may be sent on update
	// requests to ensure that the client has an up-to-date value before
	// proceeding. The server returns an ABORTED error on a mismatched etag.
	Etag string `json:"etag,omitempty"`
	// Name: Identifier. The unique name of the logical view. Format:
	// `projects/{project}/instances/{instance}/logicalViews/{logical_view}`
	Name string `json:"name,omitempty"`
	// Query: Required. The logical view's select query.
	Query string `json:"query,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeletionProtection") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeletionProtection") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LogicalView: A SQL logical view object that can be referenced in SQL queries.

func (LogicalView) MarshalJSON ¶
added in v0.227.0
func (s LogicalView) MarshalJSON() ([]byte, error)
type MaterializedView ¶
added in v0.227.0
type MaterializedView struct {
	// ClusterStates: Output only. Map from cluster ID to per-cluster materialized
	// view state. If it could not be determined whether or not the materialized
	// view has data in a particular cluster (for example, if its zone is
	// unavailable), then there will be an entry for the cluster with
	// `STATE_NOT_KNOWN` state. Views: `REPLICATION_VIEW`, `FULL`.
	ClusterStates map[string]GoogleBigtableAdminV2MaterializedViewClusterState `json:"clusterStates,omitempty"`
	// DeletionProtection: Set to true to make the MaterializedView protected
	// against deletion. Views: `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`.
	DeletionProtection bool `json:"deletionProtection,omitempty"`
	// Etag: Optional. The etag for this materialized view. This may be sent on
	// update requests to ensure that the client has an up-to-date value before
	// proceeding. The server returns an ABORTED error on a mismatched etag. Views:
	// `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`.
	Etag string `json:"etag,omitempty"`
	// Name: Identifier. The unique name of the materialized view. Format:
	// `projects/{project}/instances/{instance}/materializedViews/{materialized_view
	// }` Views: `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`.
	Name string `json:"name,omitempty"`
	// Query: Required. Immutable. The materialized view's select query. Views:
	// `SCHEMA_VIEW`, `FULL`.
	Query string `json:"query,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClusterStates") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterStates") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MaterializedView: A materialized view object that can be referenced in SQL queries.

func (MaterializedView) MarshalJSON ¶
added in v0.227.0
func (s MaterializedView) MarshalJSON() ([]byte, error)
type Modification ¶
type Modification struct {
	// Create: Create a new column family with the specified schema, or fail if one
	// already exists with the given ID.
	Create *ColumnFamily `json:"create,omitempty"`
	// Drop: Drop (delete) the column family with the given ID, or fail if no such
	// family exists.
	Drop bool `json:"drop,omitempty"`
	// Id: The ID of the column family to be modified.
	Id string `json:"id,omitempty"`
	// Update: Update an existing column family to the specified schema, or fail if
	// no column family exists with the given ID.
	Update *ColumnFamily `json:"update,omitempty"`
	// UpdateMask: Optional. A mask specifying which fields (e.g. `gc_rule`) in the
	// `update` mod should be updated, ignored for other modification types. If
	// unset or empty, we treat it as updating `gc_rule` to be backward compatible.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Create") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Create") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Modification: A create, update, or delete of a particular column family.

func (Modification) MarshalJSON ¶
func (s Modification) MarshalJSON() ([]byte, error)
type ModifyColumnFamiliesRequest ¶
type ModifyColumnFamiliesRequest struct {
	// IgnoreWarnings: Optional. If true, ignore safety checks when modifying the
	// column families.
	IgnoreWarnings bool `json:"ignoreWarnings,omitempty"`
	// Modifications: Required. Modifications to be atomically applied to the
	// specified table's families. Entries are applied in order, meaning that
	// earlier modifications can be masked by later ones (in the case of repeated
	// updates to the same family, for example).
	Modifications []*Modification `json:"modifications,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IgnoreWarnings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IgnoreWarnings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ModifyColumnFamiliesRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.ModifyColumnFamilies

func (ModifyColumnFamiliesRequest) MarshalJSON ¶
func (s ModifyColumnFamiliesRequest) MarshalJSON() ([]byte, error)
type MultiClusterRoutingUseAny ¶
type MultiClusterRoutingUseAny struct {
	// ClusterIds: The set of clusters to route to. The order is ignored; clusters
	// will be tried in order of distance. If left empty, all clusters are
	// eligible.
	ClusterIds []string `json:"clusterIds,omitempty"`
	// RowAffinity: Row affinity sticky routing based on the row key of the
	// request. Requests that span multiple rows are routed non-deterministically.
	RowAffinity *RowAffinity `json:"rowAffinity,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterIds") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MultiClusterRoutingUseAny: Read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes consistency to improve availability.

func (MultiClusterRoutingUseAny) MarshalJSON ¶
added in v0.59.0
func (s MultiClusterRoutingUseAny) MarshalJSON() ([]byte, error)
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
type OperationProgress ¶
added in v0.30.0
type OperationProgress struct {
	// EndTime: If set, the time at which this operation failed or was completed
	// successfully.
	EndTime string `json:"endTime,omitempty"`
	// ProgressPercent: Percent completion of the operation. Values are between 0
	// and 100 inclusive.
	ProgressPercent int64 `json:"progressPercent,omitempty"`
	// StartTime: Time the request was received.
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

OperationProgress: Encapsulates progress related information for a Cloud Bigtable long running operation.

func (OperationProgress) MarshalJSON ¶
added in v0.30.0
func (s OperationProgress) MarshalJSON() ([]byte, error)
type OperationsGetCall ¶
type OperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*OperationsGetCall) Context ¶
func (c *OperationsGetCall) Context(ctx context.Context) *OperationsGetCall

Context sets the context to be used in this call's Do method.

func (*OperationsGetCall) Do ¶
func (c *OperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsGetCall) Fields ¶
func (c *OperationsGetCall) Fields(s ...googleapi.Field) *OperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsGetCall) Header ¶
func (c *OperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OperationsGetCall) IfNoneMatch ¶
func (c *OperationsGetCall) IfNoneMatch(entityTag string) *OperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OperationsProjectsOperationsListCall ¶
type OperationsProjectsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*OperationsProjectsOperationsListCall) Context ¶
func (c *OperationsProjectsOperationsListCall) Context(ctx context.Context) *OperationsProjectsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*OperationsProjectsOperationsListCall) Do ¶
func (c *OperationsProjectsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "bigtableadmin.operations.projects.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsProjectsOperationsListCall) Fields ¶
func (c *OperationsProjectsOperationsListCall) Fields(s ...googleapi.Field) *OperationsProjectsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsProjectsOperationsListCall) Filter ¶
func (c *OperationsProjectsOperationsListCall) Filter(filter string) *OperationsProjectsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*OperationsProjectsOperationsListCall) Header ¶
func (c *OperationsProjectsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OperationsProjectsOperationsListCall) IfNoneMatch ¶
func (c *OperationsProjectsOperationsListCall) IfNoneMatch(entityTag string) *OperationsProjectsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OperationsProjectsOperationsListCall) PageSize ¶
func (c *OperationsProjectsOperationsListCall) PageSize(pageSize int64) *OperationsProjectsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*OperationsProjectsOperationsListCall) PageToken ¶
func (c *OperationsProjectsOperationsListCall) PageToken(pageToken string) *OperationsProjectsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*OperationsProjectsOperationsListCall) Pages ¶
func (c *OperationsProjectsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*OperationsProjectsOperationsListCall) ReturnPartialSuccess ¶
added in v0.253.0
func (c *OperationsProjectsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OperationsProjectsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type OperationsProjectsOperationsService ¶
type OperationsProjectsOperationsService struct {
	// contains filtered or unexported fields
}
func NewOperationsProjectsOperationsService ¶
func NewOperationsProjectsOperationsService(s *Service) *OperationsProjectsOperationsService
func (*OperationsProjectsOperationsService) List ¶
func (r *OperationsProjectsOperationsService) List(name string) *OperationsProjectsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type OperationsProjectsService ¶
type OperationsProjectsService struct {
	Operations *OperationsProjectsOperationsService
	// contains filtered or unexported fields
}
func NewOperationsProjectsService ¶
func NewOperationsProjectsService(s *Service) *OperationsProjectsService
type OperationsService ¶
type OperationsService struct {
	Projects *OperationsProjectsService
	// contains filtered or unexported fields
}
func NewOperationsService ¶
func NewOperationsService(s *Service) *OperationsService
func (*OperationsService) Get ¶
func (r *OperationsService) Get(name string) *OperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

type OptimizeRestoredTableMetadata ¶
added in v0.30.0
type OptimizeRestoredTableMetadata struct {
	// Name: Name of the restored table being optimized.
	Name string `json:"name,omitempty"`
	// Progress: The progress of the post-restore optimizations.
	Progress *OperationProgress `json:"progress,omitempty"`
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

OptimizeRestoredTableMetadata: Metadata type for the long-running operation used to track the progress of optimizations performed on a newly restored table. This long-running operation is automatically created by the system after the successful completion of a table restore, and cannot be cancelled.

func (OptimizeRestoredTableMetadata) MarshalJSON ¶
added in v0.30.0
func (s OptimizeRestoredTableMetadata) MarshalJSON() ([]byte, error)
type PartialUpdateClusterMetadata ¶
added in v0.61.0
type PartialUpdateClusterMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The original request for PartialUpdateCluster.
	OriginalRequest *PartialUpdateClusterRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PartialUpdateClusterMetadata: The metadata for the Operation returned by PartialUpdateCluster.

func (PartialUpdateClusterMetadata) MarshalJSON ¶
added in v0.61.0
func (s PartialUpdateClusterMetadata) MarshalJSON() ([]byte, error)
type PartialUpdateClusterRequest ¶
added in v0.61.0
type PartialUpdateClusterRequest struct {
	// Cluster: Required. The Cluster which contains the partial updates to be
	// applied, subject to the update_mask.
	Cluster *Cluster `json:"cluster,omitempty"`
	// UpdateMask: Required. The subset of Cluster fields which should be replaced.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Cluster") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cluster") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PartialUpdateClusterRequest: Request message for BigtableInstanceAdmin.PartialUpdateCluster.

func (PartialUpdateClusterRequest) MarshalJSON ¶
added in v0.61.0
func (s PartialUpdateClusterRequest) MarshalJSON() ([]byte, error)
type PartialUpdateInstanceRequest ¶
type PartialUpdateInstanceRequest struct {
	// Instance: Required. The Instance which will (partially) replace the current
	// value.
	Instance *Instance `json:"instance,omitempty"`
	// UpdateMask: Required. The subset of Instance fields which should be
	// replaced. Must be explicitly set.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Instance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Instance") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PartialUpdateInstanceRequest: Request message for BigtableInstanceAdmin.PartialUpdateInstance.

func (PartialUpdateInstanceRequest) MarshalJSON ¶
func (s PartialUpdateInstanceRequest) MarshalJSON() ([]byte, error)
type Policy ¶
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
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsInstancesAppProfilesCreateCall ¶
type ProjectsInstancesAppProfilesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesAppProfilesCreateCall) AppProfileId ¶
func (c *ProjectsInstancesAppProfilesCreateCall) AppProfileId(appProfileId string) *ProjectsInstancesAppProfilesCreateCall

AppProfileId sets the optional parameter "appProfileId": Required. The ID to be used when referring to the new app profile within its instance, e.g., just `myprofile` rather than `projects/myproject/instances/myinstance/appProfiles/myprofile`.

func (*ProjectsInstancesAppProfilesCreateCall) Context ¶
func (c *ProjectsInstancesAppProfilesCreateCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesAppProfilesCreateCall) Do ¶
func (c *ProjectsInstancesAppProfilesCreateCall) Do(opts ...googleapi.CallOption) (*AppProfile, error)

Do executes the "bigtableadmin.projects.instances.appProfiles.create" call. Any non-2xx status code is an error. Response headers are in either *AppProfile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesAppProfilesCreateCall) Fields ¶
func (c *ProjectsInstancesAppProfilesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesAppProfilesCreateCall) Header ¶
func (c *ProjectsInstancesAppProfilesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesAppProfilesCreateCall) IgnoreWarnings ¶
func (c *ProjectsInstancesAppProfilesCreateCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesCreateCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": If true, ignore safety checks when creating the app profile.

type ProjectsInstancesAppProfilesDeleteCall ¶
type ProjectsInstancesAppProfilesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesAppProfilesDeleteCall) Context ¶
func (c *ProjectsInstancesAppProfilesDeleteCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesAppProfilesDeleteCall) Do ¶
func (c *ProjectsInstancesAppProfilesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.appProfiles.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesAppProfilesDeleteCall) Fields ¶
func (c *ProjectsInstancesAppProfilesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesAppProfilesDeleteCall) Header ¶
func (c *ProjectsInstancesAppProfilesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesAppProfilesDeleteCall) IgnoreWarnings ¶
func (c *ProjectsInstancesAppProfilesDeleteCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesDeleteCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": Required. If true, ignore safety checks when deleting the app profile.

type ProjectsInstancesAppProfilesGetCall ¶
type ProjectsInstancesAppProfilesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesAppProfilesGetCall) Context ¶
func (c *ProjectsInstancesAppProfilesGetCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesAppProfilesGetCall) Do ¶
func (c *ProjectsInstancesAppProfilesGetCall) Do(opts ...googleapi.CallOption) (*AppProfile, error)

Do executes the "bigtableadmin.projects.instances.appProfiles.get" call. Any non-2xx status code is an error. Response headers are in either *AppProfile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesAppProfilesGetCall) Fields ¶
func (c *ProjectsInstancesAppProfilesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesAppProfilesGetCall) Header ¶
func (c *ProjectsInstancesAppProfilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesAppProfilesGetCall) IfNoneMatch ¶
func (c *ProjectsInstancesAppProfilesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesAppProfilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesAppProfilesListCall ¶
type ProjectsInstancesAppProfilesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesAppProfilesListCall) Context ¶
func (c *ProjectsInstancesAppProfilesListCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesAppProfilesListCall) Do ¶
func (c *ProjectsInstancesAppProfilesListCall) Do(opts ...googleapi.CallOption) (*ListAppProfilesResponse, error)

Do executes the "bigtableadmin.projects.instances.appProfiles.list" call. Any non-2xx status code is an error. Response headers are in either *ListAppProfilesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesAppProfilesListCall) Fields ¶
func (c *ProjectsInstancesAppProfilesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesAppProfilesListCall) Header ¶
func (c *ProjectsInstancesAppProfilesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesAppProfilesListCall) IfNoneMatch ¶
func (c *ProjectsInstancesAppProfilesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesAppProfilesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesAppProfilesListCall) PageSize ¶
func (c *ProjectsInstancesAppProfilesListCall) PageSize(pageSize int64) *ProjectsInstancesAppProfilesListCall

PageSize sets the optional parameter "pageSize": Maximum number of results per page. A page_size of zero lets the server choose the number of items to return. A page_size which is strictly positive will return at most that many items. A negative page_size will cause an error. Following the first request, subsequent paginated calls are not required to pass a page_size. If a page_size is set in subsequent calls, it must match the page_size given in the first request.

func (*ProjectsInstancesAppProfilesListCall) PageToken ¶
func (c *ProjectsInstancesAppProfilesListCall) PageToken(pageToken string) *ProjectsInstancesAppProfilesListCall

PageToken sets the optional parameter "pageToken": The value of `next_page_token` returned by a previous call.

func (*ProjectsInstancesAppProfilesListCall) Pages ¶
func (c *ProjectsInstancesAppProfilesListCall) Pages(ctx context.Context, f func(*ListAppProfilesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsInstancesAppProfilesPatchCall ¶
type ProjectsInstancesAppProfilesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesAppProfilesPatchCall) Context ¶
func (c *ProjectsInstancesAppProfilesPatchCall) Context(ctx context.Context) *ProjectsInstancesAppProfilesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesAppProfilesPatchCall) Do ¶
func (c *ProjectsInstancesAppProfilesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.appProfiles.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesAppProfilesPatchCall) Fields ¶
func (c *ProjectsInstancesAppProfilesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesAppProfilesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesAppProfilesPatchCall) Header ¶
func (c *ProjectsInstancesAppProfilesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesAppProfilesPatchCall) IgnoreWarnings ¶
func (c *ProjectsInstancesAppProfilesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesAppProfilesPatchCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": If true, ignore safety checks when updating the app profile.

func (*ProjectsInstancesAppProfilesPatchCall) UpdateMask ¶
func (c *ProjectsInstancesAppProfilesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesAppProfilesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The subset of app profile fields which should be replaced. If unset, all fields will be replaced.

type ProjectsInstancesAppProfilesService ¶
type ProjectsInstancesAppProfilesService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesAppProfilesService ¶
func NewProjectsInstancesAppProfilesService(s *Service) *ProjectsInstancesAppProfilesService
func (*ProjectsInstancesAppProfilesService) Create ¶
func (r *ProjectsInstancesAppProfilesService) Create(parent string, appprofile *AppProfile) *ProjectsInstancesAppProfilesCreateCall

Create: Creates an app profile within an instance.

parent: The unique name of the instance in which to create the new app profile. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesAppProfilesService) Delete ¶
func (r *ProjectsInstancesAppProfilesService) Delete(name string) *ProjectsInstancesAppProfilesDeleteCall

Delete: Deletes an app profile from an instance.

name: The unique name of the app profile to be deleted. Values are of the form `projects/{project}/instances/{instance}/appProfiles/{app_profile}`.
func (*ProjectsInstancesAppProfilesService) Get ¶
func (r *ProjectsInstancesAppProfilesService) Get(name string) *ProjectsInstancesAppProfilesGetCall

Get: Gets information about an app profile.

name: The unique name of the requested app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/{app_profile}`.
func (*ProjectsInstancesAppProfilesService) List ¶
func (r *ProjectsInstancesAppProfilesService) List(parent string) *ProjectsInstancesAppProfilesListCall

List: Lists information about app profiles in an instance.

parent: The unique name of the instance for which a list of app profiles is requested. Values are of the form `projects/{project}/instances/{instance}`. Use `{instance} = '-'` to list AppProfiles for all Instances in a project, e.g., `projects/myproject/instances/-`.
func (*ProjectsInstancesAppProfilesService) Patch ¶
func (r *ProjectsInstancesAppProfilesService) Patch(name string, appprofile *AppProfile) *ProjectsInstancesAppProfilesPatchCall

Patch: Updates an app profile within an instance.

name: The unique name of the app profile, up to 50 characters long. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
type ProjectsInstancesClustersBackupsCopyCall ¶
added in v0.101.0
type ProjectsInstancesClustersBackupsCopyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsCopyCall) Context ¶
added in v0.101.0
func (c *ProjectsInstancesClustersBackupsCopyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsCopyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsCopyCall) Do ¶
added in v0.101.0
func (c *ProjectsInstancesClustersBackupsCopyCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.copy" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsCopyCall) Fields ¶
added in v0.101.0
func (c *ProjectsInstancesClustersBackupsCopyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsCopyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsCopyCall) Header ¶
added in v0.101.0
func (c *ProjectsInstancesClustersBackupsCopyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersBackupsCreateCall ¶
added in v0.30.0
type ProjectsInstancesClustersBackupsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsCreateCall) BackupId ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsCreateCall) BackupId(backupId string) *ProjectsInstancesClustersBackupsCreateCall

BackupId sets the optional parameter "backupId": Required. The id of the backup to be created. The `backup_id` along with the parent `parent` are combined as {parent}/backups/{backup_id} to create the full backup name, of the form: `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_i d}`. This string must be between 1 and 50 characters in length and match the regex _a-zA-Z0-9*.

func (*ProjectsInstancesClustersBackupsCreateCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsCreateCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsCreateCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsCreateCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsCreateCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersBackupsDeleteCall ¶
added in v0.30.0
type ProjectsInstancesClustersBackupsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsDeleteCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsDeleteCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsDeleteCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsDeleteCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsDeleteCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersBackupsGetCall ¶
added in v0.30.0
type ProjectsInstancesClustersBackupsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsGetCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsGetCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsGetCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.get" call. Any non-2xx status code is an error. Response headers are in either *Backup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsGetCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsGetCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersBackupsGetCall) IfNoneMatch ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersBackupsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesClustersBackupsGetIamPolicyCall ¶
added in v0.18.0
type ProjectsInstancesClustersBackupsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsGetIamPolicyCall) Context ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsGetIamPolicyCall) Do ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsGetIamPolicyCall) Fields ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsGetIamPolicyCall) Header ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersBackupsListCall ¶
added in v0.30.0
type ProjectsInstancesClustersBackupsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsListCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsListCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsListCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsListCall) Filter ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Filter(filter string) *ProjectsInstancesClustersBackupsListCall

Filter sets the optional parameter "filter": A filter expression that filters backups listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be <, >, <=, >=, !=, =, or :. Colon ':' represents a HAS operator which is roughly synonymous with equality. Filter rules are case insensitive. The fields eligible for filtering are: * `name` * `source_table` * `state` * `start_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * `end_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * `size_bytes` To filter on multiple expressions, provide each separate expression within parentheses. By default, each expression is an AND expression. However, you can include AND, OR, and NOT expressions explicitly. Some examples of using filters are: * `name:"exact" --> The backup's name is the string "exact". * `name:howl` --> The backup's name contains the string "howl". * `source_table:prod` --> The source_table's name contains the string "prod". * `state:CREATING` --> The backup is pending creation. * `state:READY` --> The backup is fully created and ready for use. * `(name:howl) AND (start_time < \"2018-03-28T14:50:00Z\")` --> The backup name contains the string "howl" and start_time of the backup is before 2018-03-28T14:50:00Z. * `size_bytes > 10000000000` --> The backup's size is greater than 10GB

func (*ProjectsInstancesClustersBackupsListCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersBackupsListCall) IfNoneMatch ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersBackupsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesClustersBackupsListCall) OrderBy ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) OrderBy(orderBy string) *ProjectsInstancesClustersBackupsListCall

OrderBy sets the optional parameter "orderBy": An expression for specifying the sort order of the results of the request. The string value should specify one or more fields in Backup. The full syntax is described at https://aip.dev/132#ordering. Fields supported are: * name * source_table * expire_time * start_time * end_time * size_bytes * state For example, "start_time". The default sorting order is ascending. To specify descending order for the field, a suffix " desc" should be appended to the field name. For example, "start_time desc". Redundant space characters in the syntax are insigificant. If order_by is empty, results will be sorted by `start_time` in descending order starting from the most recently created backup.

func (*ProjectsInstancesClustersBackupsListCall) PageSize ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) PageSize(pageSize int64) *ProjectsInstancesClustersBackupsListCall

PageSize sets the optional parameter "pageSize": Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

func (*ProjectsInstancesClustersBackupsListCall) PageToken ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) PageToken(pageToken string) *ProjectsInstancesClustersBackupsListCall

PageToken sets the optional parameter "pageToken": If non-empty, `page_token` should contain a next_page_token from a previous ListBackupsResponse to the same `parent` and with the same `filter`.

func (*ProjectsInstancesClustersBackupsListCall) Pages ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsInstancesClustersBackupsPatchCall ¶
added in v0.30.0
type ProjectsInstancesClustersBackupsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsPatchCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsPatchCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsPatchCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Backup, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.patch" call. Any non-2xx status code is an error. Response headers are in either *Backup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsPatchCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsPatchCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersBackupsPatchCall) UpdateMask ¶
added in v0.30.0
func (c *ProjectsInstancesClustersBackupsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesClustersBackupsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.

type ProjectsInstancesClustersBackupsService ¶
added in v0.18.0
type ProjectsInstancesClustersBackupsService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesClustersBackupsService ¶
added in v0.18.0
func NewProjectsInstancesClustersBackupsService(s *Service) *ProjectsInstancesClustersBackupsService
func (*ProjectsInstancesClustersBackupsService) Copy ¶
added in v0.101.0
func (r *ProjectsInstancesClustersBackupsService) Copy(parent string, copybackuprequest *CopyBackupRequest) *ProjectsInstancesClustersBackupsCopyCall

Copy: Copy a Cloud Bigtable backup to a new backup in the destination cluster located in the destination instance and project.

parent: The name of the destination cluster that will contain the backup copy. The cluster must already exist. Values are of the form: `projects/{project}/instances/{instance}/clusters/{cluster}`.
func (*ProjectsInstancesClustersBackupsService) Create ¶
added in v0.30.0
func (r *ProjectsInstancesClustersBackupsService) Create(parent string, backup *Backup) *ProjectsInstancesClustersBackupsCreateCall

Create: Starts creating a new Cloud Bigtable Backup. The returned backup long-running operation can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup.

parent: This must be one of the clusters in the instance in which this table is located. The backup will be stored in this cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.
func (*ProjectsInstancesClustersBackupsService) Delete ¶
added in v0.30.0
func (r *ProjectsInstancesClustersBackupsService) Delete(name string) *ProjectsInstancesClustersBackupsDeleteCall

Delete: Deletes a pending or completed Cloud Bigtable backup.

name: Name of the backup to delete. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup }`.
func (*ProjectsInstancesClustersBackupsService) Get ¶
added in v0.30.0
func (r *ProjectsInstancesClustersBackupsService) Get(name string) *ProjectsInstancesClustersBackupsGetCall

Get: Gets metadata on a pending or completed Cloud Bigtable Backup.

name: Name of the backup. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup }`.
func (*ProjectsInstancesClustersBackupsService) GetIamPolicy ¶
added in v0.18.0
func (r *ProjectsInstancesClustersBackupsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesClustersBackupsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a Bigtable resource. Returns an empty policy if the resource exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesClustersBackupsService) List ¶
added in v0.30.0
func (r *ProjectsInstancesClustersBackupsService) List(parent string) *ProjectsInstancesClustersBackupsListCall

List: Lists Cloud Bigtable backups. Returns both completed and pending backups.

parent: The cluster to list backups from. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. Use `{cluster} = '-'` to list backups for all clusters in an instance, e.g., `projects/{project}/instances/{instance}/clusters/-`.
func (*ProjectsInstancesClustersBackupsService) Patch ¶
added in v0.30.0
func (r *ProjectsInstancesClustersBackupsService) Patch(nameid string, backup *Backup) *ProjectsInstancesClustersBackupsPatchCall

Patch: Updates a pending or completed Cloud Bigtable Backup.

name: A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/_a-zA-Z0-9*` The final segment of the name must be between 1 and 50 characters in length. The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.
func (*ProjectsInstancesClustersBackupsService) SetIamPolicy ¶
added in v0.18.0
func (r *ProjectsInstancesClustersBackupsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesClustersBackupsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on a Bigtable resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesClustersBackupsService) TestIamPermissions ¶
added in v0.21.0
func (r *ProjectsInstancesClustersBackupsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesClustersBackupsTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified Bigtable resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsInstancesClustersBackupsSetIamPolicyCall ¶
added in v0.18.0
type ProjectsInstancesClustersBackupsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsSetIamPolicyCall) Context ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsSetIamPolicyCall) Do ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsSetIamPolicyCall) Fields ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsSetIamPolicyCall) Header ¶
added in v0.18.0
func (c *ProjectsInstancesClustersBackupsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersBackupsTestIamPermissionsCall ¶
added in v0.21.0
type ProjectsInstancesClustersBackupsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersBackupsTestIamPermissionsCall) Context ¶
added in v0.21.0
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesClustersBackupsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersBackupsTestIamPermissionsCall) Do ¶
added in v0.21.0
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.clusters.backups.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersBackupsTestIamPermissionsCall) Fields ¶
added in v0.21.0
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersBackupsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersBackupsTestIamPermissionsCall) Header ¶
added in v0.21.0
func (c *ProjectsInstancesClustersBackupsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersCreateCall ¶
type ProjectsInstancesClustersCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersCreateCall) ClusterId ¶
func (c *ProjectsInstancesClustersCreateCall) ClusterId(clusterId string) *ProjectsInstancesClustersCreateCall

ClusterId sets the optional parameter "clusterId": Required. The ID to be used when referring to the new cluster within its instance, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.

func (*ProjectsInstancesClustersCreateCall) Context ¶
func (c *ProjectsInstancesClustersCreateCall) Context(ctx context.Context) *ProjectsInstancesClustersCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersCreateCall) Do ¶
func (c *ProjectsInstancesClustersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.clusters.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersCreateCall) Fields ¶
func (c *ProjectsInstancesClustersCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersCreateCall) Header ¶
func (c *ProjectsInstancesClustersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersDeleteCall ¶
type ProjectsInstancesClustersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersDeleteCall) Context ¶
func (c *ProjectsInstancesClustersDeleteCall) Context(ctx context.Context) *ProjectsInstancesClustersDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersDeleteCall) Do ¶
func (c *ProjectsInstancesClustersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.clusters.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersDeleteCall) Fields ¶
func (c *ProjectsInstancesClustersDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersDeleteCall) Header ¶
func (c *ProjectsInstancesClustersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesClustersGetCall ¶
type ProjectsInstancesClustersGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersGetCall) Context ¶
func (c *ProjectsInstancesClustersGetCall) Context(ctx context.Context) *ProjectsInstancesClustersGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersGetCall) Do ¶
func (c *ProjectsInstancesClustersGetCall) Do(opts ...googleapi.CallOption) (*Cluster, error)

Do executes the "bigtableadmin.projects.instances.clusters.get" call. Any non-2xx status code is an error. Response headers are in either *Cluster.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersGetCall) Fields ¶
func (c *ProjectsInstancesClustersGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersGetCall) Header ¶
func (c *ProjectsInstancesClustersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersGetCall) IfNoneMatch ¶
func (c *ProjectsInstancesClustersGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesClustersHotTabletsListCall ¶
added in v0.75.0
type ProjectsInstancesClustersHotTabletsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersHotTabletsListCall) Context ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) Context(ctx context.Context) *ProjectsInstancesClustersHotTabletsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersHotTabletsListCall) Do ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) Do(opts ...googleapi.CallOption) (*ListHotTabletsResponse, error)

Do executes the "bigtableadmin.projects.instances.clusters.hotTablets.list" call. Any non-2xx status code is an error. Response headers are in either *ListHotTabletsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersHotTabletsListCall) EndTime ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) EndTime(endTime string) *ProjectsInstancesClustersHotTabletsListCall

EndTime sets the optional parameter "endTime": The end time to list hot tablets.

func (*ProjectsInstancesClustersHotTabletsListCall) Fields ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersHotTabletsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersHotTabletsListCall) Header ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersHotTabletsListCall) IfNoneMatch ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersHotTabletsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesClustersHotTabletsListCall) PageSize ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) PageSize(pageSize int64) *ProjectsInstancesClustersHotTabletsListCall

PageSize sets the optional parameter "pageSize": Maximum number of results per page. A page_size that is empty or zero lets the server choose the number of items to return. A page_size which is strictly positive will return at most that many items. A negative page_size will cause an error. Following the first request, subsequent paginated calls do not need a page_size field. If a page_size is set in subsequent calls, it must match the page_size given in the first request.

func (*ProjectsInstancesClustersHotTabletsListCall) PageToken ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) PageToken(pageToken string) *ProjectsInstancesClustersHotTabletsListCall

PageToken sets the optional parameter "pageToken": The value of `next_page_token` returned by a previous call.

func (*ProjectsInstancesClustersHotTabletsListCall) Pages ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) Pages(ctx context.Context, f func(*ListHotTabletsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsInstancesClustersHotTabletsListCall) StartTime ¶
added in v0.75.0
func (c *ProjectsInstancesClustersHotTabletsListCall) StartTime(startTime string) *ProjectsInstancesClustersHotTabletsListCall

StartTime sets the optional parameter "startTime": The start time to list hot tablets. The hot tablets in the response will have start times between the requested start time and end time. Start time defaults to Now if it is unset, and end time defaults to Now - 24 hours if it is unset. The start time should be less than the end time, and the maximum allowed time range between start time and end time is 48 hours. Start time and end time should have values between Now and Now - 14 days.

type ProjectsInstancesClustersHotTabletsService ¶
added in v0.75.0
type ProjectsInstancesClustersHotTabletsService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesClustersHotTabletsService ¶
added in v0.75.0
func NewProjectsInstancesClustersHotTabletsService(s *Service) *ProjectsInstancesClustersHotTabletsService
func (*ProjectsInstancesClustersHotTabletsService) List ¶
added in v0.75.0
func (r *ProjectsInstancesClustersHotTabletsService) List(parent string) *ProjectsInstancesClustersHotTabletsListCall

List: Lists hot tablets in a cluster, within the time range provided. Hot tablets are ordered based on CPU usage.

parent: The cluster name to list hot tablets. Value is in the following form: `projects/{project}/instances/{instance}/clusters/{cluster}`.
type ProjectsInstancesClustersListCall ¶
type ProjectsInstancesClustersListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersListCall) Context ¶
func (c *ProjectsInstancesClustersListCall) Context(ctx context.Context) *ProjectsInstancesClustersListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersListCall) Do ¶
func (c *ProjectsInstancesClustersListCall) Do(opts ...googleapi.CallOption) (*ListClustersResponse, error)

Do executes the "bigtableadmin.projects.instances.clusters.list" call. Any non-2xx status code is an error. Response headers are in either *ListClustersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersListCall) Fields ¶
func (c *ProjectsInstancesClustersListCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersListCall) Header ¶
func (c *ProjectsInstancesClustersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersListCall) IfNoneMatch ¶
func (c *ProjectsInstancesClustersListCall) IfNoneMatch(entityTag string) *ProjectsInstancesClustersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesClustersListCall) PageToken ¶
func (c *ProjectsInstancesClustersListCall) PageToken(pageToken string) *ProjectsInstancesClustersListCall

PageToken sets the optional parameter "pageToken": DEPRECATED: This field is unused and ignored.

func (*ProjectsInstancesClustersListCall) Pages ¶
func (c *ProjectsInstancesClustersListCall) Pages(ctx context.Context, f func(*ListClustersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsInstancesClustersPartialUpdateClusterCall ¶
added in v0.46.0
type ProjectsInstancesClustersPartialUpdateClusterCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersPartialUpdateClusterCall) Context ¶
added in v0.46.0
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Context(ctx context.Context) *ProjectsInstancesClustersPartialUpdateClusterCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersPartialUpdateClusterCall) Do ¶
added in v0.46.0
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.clusters.partialUpdateCluster" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersPartialUpdateClusterCall) Fields ¶
added in v0.46.0
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersPartialUpdateClusterCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersPartialUpdateClusterCall) Header ¶
added in v0.46.0
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesClustersPartialUpdateClusterCall) UpdateMask ¶
added in v0.46.0
func (c *ProjectsInstancesClustersPartialUpdateClusterCall) UpdateMask(updateMask string) *ProjectsInstancesClustersPartialUpdateClusterCall

UpdateMask sets the optional parameter "updateMask": Required. The subset of Cluster fields which should be replaced.

type ProjectsInstancesClustersService ¶
type ProjectsInstancesClustersService struct {
	Backups *ProjectsInstancesClustersBackupsService

	HotTablets *ProjectsInstancesClustersHotTabletsService
	// contains filtered or unexported fields
}
func NewProjectsInstancesClustersService ¶
func NewProjectsInstancesClustersService(s *Service) *ProjectsInstancesClustersService
func (*ProjectsInstancesClustersService) Create ¶
func (r *ProjectsInstancesClustersService) Create(parent string, cluster *Cluster) *ProjectsInstancesClustersCreateCall

Create: Creates a cluster within an instance. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled.

parent: The unique name of the instance in which to create the new cluster. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesClustersService) Delete ¶
func (r *ProjectsInstancesClustersService) Delete(name string) *ProjectsInstancesClustersDeleteCall

Delete: Deletes a cluster from an instance.

name: The unique name of the cluster to be deleted. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.
func (*ProjectsInstancesClustersService) Get ¶
func (r *ProjectsInstancesClustersService) Get(name string) *ProjectsInstancesClustersGetCall

Get: Gets information about a cluster.

name: The unique name of the requested cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.
func (*ProjectsInstancesClustersService) List ¶
func (r *ProjectsInstancesClustersService) List(parent string) *ProjectsInstancesClustersListCall

List: Lists information about clusters in an instance.

parent: The unique name of the instance for which a list of clusters is requested. Values are of the form `projects/{project}/instances/{instance}`. Use `{instance} = '-'` to list Clusters for all Instances in a project, e.g., `projects/myproject/instances/-`.
func (*ProjectsInstancesClustersService) PartialUpdateCluster ¶
added in v0.46.0
func (r *ProjectsInstancesClustersService) PartialUpdateCluster(name string, cluster *Cluster) *ProjectsInstancesClustersPartialUpdateClusterCall

PartialUpdateCluster: Partially updates a cluster within a project. This method is the preferred way to update a Cluster. To enable and update autoscaling, set cluster_config.cluster_autoscaling_config. When autoscaling is enabled, serve_nodes is treated as an OUTPUT_ONLY field, meaning that updates to it are ignored. Note that an update cannot simultaneously set serve_nodes to non-zero and cluster_config.cluster_autoscaling_config to non-empty, and also specify both in the update_mask. To disable autoscaling, clear cluster_config.cluster_autoscaling_config, and explicitly set a serve_node count via the update_mask.

name: The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
func (*ProjectsInstancesClustersService) Update ¶
func (r *ProjectsInstancesClustersService) Update(name string, cluster *Cluster) *ProjectsInstancesClustersUpdateCall

Update: Updates a cluster within an instance. Note that UpdateCluster does not support updating cluster_config.cluster_autoscaling_config. In order to update it, you must use PartialUpdateCluster.

name: The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
type ProjectsInstancesClustersUpdateCall ¶
type ProjectsInstancesClustersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesClustersUpdateCall) Context ¶
func (c *ProjectsInstancesClustersUpdateCall) Context(ctx context.Context) *ProjectsInstancesClustersUpdateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesClustersUpdateCall) Do ¶
func (c *ProjectsInstancesClustersUpdateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.clusters.update" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesClustersUpdateCall) Fields ¶
func (c *ProjectsInstancesClustersUpdateCall) Fields(s ...googleapi.Field) *ProjectsInstancesClustersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesClustersUpdateCall) Header ¶
func (c *ProjectsInstancesClustersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesCreateCall ¶
type ProjectsInstancesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesCreateCall) Context ¶
func (c *ProjectsInstancesCreateCall) Context(ctx context.Context) *ProjectsInstancesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesCreateCall) Do ¶
func (c *ProjectsInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesCreateCall) Fields ¶
func (c *ProjectsInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesCreateCall) Header ¶
func (c *ProjectsInstancesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesDeleteCall ¶
type ProjectsInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesDeleteCall) Context ¶
func (c *ProjectsInstancesDeleteCall) Context(ctx context.Context) *ProjectsInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesDeleteCall) Do ¶
func (c *ProjectsInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesDeleteCall) Fields ¶
func (c *ProjectsInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesDeleteCall) Header ¶
func (c *ProjectsInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesGetCall ¶
type ProjectsInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesGetCall) Context ¶
func (c *ProjectsInstancesGetCall) Context(ctx context.Context) *ProjectsInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesGetCall) Do ¶
func (c *ProjectsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "bigtableadmin.projects.instances.get" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesGetCall) Fields ¶
func (c *ProjectsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesGetCall) Header ¶
func (c *ProjectsInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesGetIamPolicyCall ¶
type ProjectsInstancesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesGetIamPolicyCall) Context ¶
func (c *ProjectsInstancesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesGetIamPolicyCall) Do ¶
func (c *ProjectsInstancesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesGetIamPolicyCall) Fields ¶
func (c *ProjectsInstancesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesGetIamPolicyCall) Header ¶
func (c *ProjectsInstancesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesListCall ¶
type ProjectsInstancesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesListCall) Context ¶
func (c *ProjectsInstancesListCall) Context(ctx context.Context) *ProjectsInstancesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesListCall) Do ¶
func (c *ProjectsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)

Do executes the "bigtableadmin.projects.instances.list" call. Any non-2xx status code is an error. Response headers are in either *ListInstancesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesListCall) Fields ¶
func (c *ProjectsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesListCall) Header ¶
func (c *ProjectsInstancesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesListCall) IfNoneMatch ¶
func (c *ProjectsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesListCall) PageToken ¶
func (c *ProjectsInstancesListCall) PageToken(pageToken string) *ProjectsInstancesListCall

PageToken sets the optional parameter "pageToken": DEPRECATED: This field is unused and ignored.

func (*ProjectsInstancesListCall) Pages ¶
func (c *ProjectsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsInstancesLogicalViewsCreateCall ¶
added in v0.230.0
type ProjectsInstancesLogicalViewsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsCreateCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsCreateCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsCreateCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsCreateCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesLogicalViewsCreateCall) LogicalViewId ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsCreateCall) LogicalViewId(logicalViewId string) *ProjectsInstancesLogicalViewsCreateCall

LogicalViewId sets the optional parameter "logicalViewId": Required. The ID to use for the logical view, which will become the final component of the logical view's resource name.

type ProjectsInstancesLogicalViewsDeleteCall ¶
added in v0.230.0
type ProjectsInstancesLogicalViewsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsDeleteCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsDeleteCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsDeleteCall) Etag ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsDeleteCall) Etag(etag string) *ProjectsInstancesLogicalViewsDeleteCall

Etag sets the optional parameter "etag": The current etag of the logical view. If an etag is provided and does not match the current etag of the logical view, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsInstancesLogicalViewsDeleteCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsDeleteCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesLogicalViewsGetCall ¶
added in v0.230.0
type ProjectsInstancesLogicalViewsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsGetCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsGetCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsGetCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsGetCall) Do(opts ...googleapi.CallOption) (*LogicalView, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.get" call. Any non-2xx status code is an error. Response headers are in either *LogicalView.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsGetCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsGetCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesLogicalViewsGetCall) IfNoneMatch ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesLogicalViewsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesLogicalViewsGetIamPolicyCall ¶
added in v0.225.0
type ProjectsInstancesLogicalViewsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsGetIamPolicyCall) Context ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsGetIamPolicyCall) Do ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsGetIamPolicyCall) Fields ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsGetIamPolicyCall) Header ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesLogicalViewsListCall ¶
added in v0.230.0
type ProjectsInstancesLogicalViewsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsListCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsListCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) Do(opts ...googleapi.CallOption) (*ListLogicalViewsResponse, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.list" call. Any non-2xx status code is an error. Response headers are in either *ListLogicalViewsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsListCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsListCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesLogicalViewsListCall) IfNoneMatch ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesLogicalViewsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesLogicalViewsListCall) PageSize ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) PageSize(pageSize int64) *ProjectsInstancesLogicalViewsListCall

PageSize sets the optional parameter "pageSize": The maximum number of logical views to return. The service may return fewer than this value

func (*ProjectsInstancesLogicalViewsListCall) PageToken ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) PageToken(pageToken string) *ProjectsInstancesLogicalViewsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListLogicalViews` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListLogicalViews` must match the call that provided the page token.

func (*ProjectsInstancesLogicalViewsListCall) Pages ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsListCall) Pages(ctx context.Context, f func(*ListLogicalViewsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsInstancesLogicalViewsPatchCall ¶
added in v0.230.0
type ProjectsInstancesLogicalViewsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsPatchCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsPatchCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsPatchCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsPatchCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesLogicalViewsPatchCall) UpdateMask ¶
added in v0.230.0
func (c *ProjectsInstancesLogicalViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesLogicalViewsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsInstancesLogicalViewsService ¶
added in v0.225.0
type ProjectsInstancesLogicalViewsService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesLogicalViewsService ¶
added in v0.225.0
func NewProjectsInstancesLogicalViewsService(s *Service) *ProjectsInstancesLogicalViewsService
func (*ProjectsInstancesLogicalViewsService) Create ¶
added in v0.230.0
func (r *ProjectsInstancesLogicalViewsService) Create(parent string, logicalview *LogicalView) *ProjectsInstancesLogicalViewsCreateCall

Create: Creates a logical view within an instance.

parent: The parent instance where this logical view will be created. Format: `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesLogicalViewsService) Delete ¶
added in v0.230.0
func (r *ProjectsInstancesLogicalViewsService) Delete(name string) *ProjectsInstancesLogicalViewsDeleteCall

Delete: Deletes a logical view from an instance.

name: The unique name of the logical view to be deleted. Format: `projects/{project}/instances/{instance}/logicalViews/{logical_view}`.
func (*ProjectsInstancesLogicalViewsService) Get ¶
added in v0.230.0
func (r *ProjectsInstancesLogicalViewsService) Get(name string) *ProjectsInstancesLogicalViewsGetCall

Get: Gets information about a logical view.

name: The unique name of the requested logical view. Values are of the form `projects/{project}/instances/{instance}/logicalViews/{logical_view}`.
func (*ProjectsInstancesLogicalViewsService) GetIamPolicy ¶
added in v0.225.0
func (r *ProjectsInstancesLogicalViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesLogicalViewsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesLogicalViewsService) List ¶
added in v0.230.0
func (r *ProjectsInstancesLogicalViewsService) List(parent string) *ProjectsInstancesLogicalViewsListCall

List: Lists information about logical views in an instance.

parent: The unique name of the instance for which the list of logical views is requested. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesLogicalViewsService) Patch ¶
added in v0.230.0
func (r *ProjectsInstancesLogicalViewsService) Patch(name string, logicalview *LogicalView) *ProjectsInstancesLogicalViewsPatchCall

Patch: Updates a logical view within an instance.

name: Identifier. The unique name of the logical view. Format: `projects/{project}/instances/{instance}/logicalViews/{logical_view}`.
func (*ProjectsInstancesLogicalViewsService) SetIamPolicy ¶
added in v0.225.0
func (r *ProjectsInstancesLogicalViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesLogicalViewsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on an instance resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesLogicalViewsService) TestIamPermissions ¶
added in v0.225.0
func (r *ProjectsInstancesLogicalViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesLogicalViewsTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified instance resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsInstancesLogicalViewsSetIamPolicyCall ¶
added in v0.225.0
type ProjectsInstancesLogicalViewsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsSetIamPolicyCall) Context ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsSetIamPolicyCall) Do ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsSetIamPolicyCall) Fields ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsSetIamPolicyCall) Header ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesLogicalViewsTestIamPermissionsCall ¶
added in v0.225.0
type ProjectsInstancesLogicalViewsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesLogicalViewsTestIamPermissionsCall) Context ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesLogicalViewsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesLogicalViewsTestIamPermissionsCall) Do ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.logicalViews.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesLogicalViewsTestIamPermissionsCall) Fields ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesLogicalViewsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesLogicalViewsTestIamPermissionsCall) Header ¶
added in v0.225.0
func (c *ProjectsInstancesLogicalViewsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesMaterializedViewsCreateCall ¶
added in v0.230.0
type ProjectsInstancesMaterializedViewsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsCreateCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsCreateCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsCreateCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsCreateCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesMaterializedViewsCreateCall) MaterializedViewId ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsCreateCall) MaterializedViewId(materializedViewId string) *ProjectsInstancesMaterializedViewsCreateCall

MaterializedViewId sets the optional parameter "materializedViewId": Required. The ID to use for the materialized view, which will become the final component of the materialized view's resource name.

type ProjectsInstancesMaterializedViewsDeleteCall ¶
added in v0.230.0
type ProjectsInstancesMaterializedViewsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsDeleteCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsDeleteCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsDeleteCall) Etag ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Etag(etag string) *ProjectsInstancesMaterializedViewsDeleteCall

Etag sets the optional parameter "etag": The current etag of the materialized view. If an etag is provided and does not match the current etag of the materialized view, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsInstancesMaterializedViewsDeleteCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsDeleteCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesMaterializedViewsGetCall ¶
added in v0.230.0
type ProjectsInstancesMaterializedViewsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsGetCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsGetCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsGetCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsGetCall) Do(opts ...googleapi.CallOption) (*MaterializedView, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.get" call. Any non-2xx status code is an error. Response headers are in either *MaterializedView.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsGetCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsGetCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesMaterializedViewsGetCall) IfNoneMatch ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesMaterializedViewsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesMaterializedViewsGetCall) View ¶
added in v0.253.0
func (c *ProjectsInstancesMaterializedViewsGetCall) View(view string) *ProjectsInstancesMaterializedViewsGetCall

View sets the optional parameter "view": Describes which of the materialized view's fields should be populated in the response. Defaults to SCHEMA_VIEW.

Possible values:

"VIEW_UNSPECIFIED" - Uses the default view for each method as documented


in its request.

"SCHEMA_VIEW" - Only populates fields related to the materialized view's


schema.

"REPLICATION_VIEW" - Only populates fields related to the materialized


view's replication state.

"FULL" - Populates all fields.

type ProjectsInstancesMaterializedViewsGetIamPolicyCall ¶
added in v0.224.0
type ProjectsInstancesMaterializedViewsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsGetIamPolicyCall) Context ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsGetIamPolicyCall) Do ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsGetIamPolicyCall) Fields ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsGetIamPolicyCall) Header ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesMaterializedViewsListCall ¶
added in v0.230.0
type ProjectsInstancesMaterializedViewsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsListCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsListCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) Do(opts ...googleapi.CallOption) (*ListMaterializedViewsResponse, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.list" call. Any non-2xx status code is an error. Response headers are in either *ListMaterializedViewsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsListCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsListCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesMaterializedViewsListCall) IfNoneMatch ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesMaterializedViewsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesMaterializedViewsListCall) PageSize ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) PageSize(pageSize int64) *ProjectsInstancesMaterializedViewsListCall

PageSize sets the optional parameter "pageSize": The maximum number of materialized views to return. The service may return fewer than this value

func (*ProjectsInstancesMaterializedViewsListCall) PageToken ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) PageToken(pageToken string) *ProjectsInstancesMaterializedViewsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListMaterializedViews` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListMaterializedViews` must match the call that provided the page token.

func (*ProjectsInstancesMaterializedViewsListCall) Pages ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsListCall) Pages(ctx context.Context, f func(*ListMaterializedViewsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsInstancesMaterializedViewsListCall) View ¶
added in v0.253.0
func (c *ProjectsInstancesMaterializedViewsListCall) View(view string) *ProjectsInstancesMaterializedViewsListCall

View sets the optional parameter "view": Describes which of the materialized view's fields should be populated in the response. For now, only the default value SCHEMA_VIEW is supported.

Possible values:

"VIEW_UNSPECIFIED" - Uses the default view for each method as documented


in its request.

"SCHEMA_VIEW" - Only populates fields related to the materialized view's


schema.

"REPLICATION_VIEW" - Only populates fields related to the materialized


view's replication state.

"FULL" - Populates all fields.

type ProjectsInstancesMaterializedViewsPatchCall ¶
added in v0.230.0
type ProjectsInstancesMaterializedViewsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsPatchCall) Context ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsPatchCall) Do ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsPatchCall) Fields ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsPatchCall) Header ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesMaterializedViewsPatchCall) UpdateMask ¶
added in v0.230.0
func (c *ProjectsInstancesMaterializedViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesMaterializedViewsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsInstancesMaterializedViewsService ¶
added in v0.224.0
type ProjectsInstancesMaterializedViewsService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesMaterializedViewsService ¶
added in v0.224.0
func NewProjectsInstancesMaterializedViewsService(s *Service) *ProjectsInstancesMaterializedViewsService
func (*ProjectsInstancesMaterializedViewsService) Create ¶
added in v0.230.0
func (r *ProjectsInstancesMaterializedViewsService) Create(parent string, materializedview *MaterializedView) *ProjectsInstancesMaterializedViewsCreateCall

Create: Creates a materialized view within an instance.

parent: The parent instance where this materialized view will be created. Format: `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesMaterializedViewsService) Delete ¶
added in v0.230.0
func (r *ProjectsInstancesMaterializedViewsService) Delete(name string) *ProjectsInstancesMaterializedViewsDeleteCall

Delete: Deletes a materialized view from an instance.

name: The unique name of the materialized view to be deleted. Format: `projects/{project}/instances/{instance}/materializedViews/{materialized_vi ew}`.
func (*ProjectsInstancesMaterializedViewsService) Get ¶
added in v0.230.0
func (r *ProjectsInstancesMaterializedViewsService) Get(name string) *ProjectsInstancesMaterializedViewsGetCall

Get: Gets information about a materialized view.

name: The unique name of the requested materialized view. Values are of the form `projects/{project}/instances/{instance}/materializedViews/{materialized_vi ew}`.
func (*ProjectsInstancesMaterializedViewsService) GetIamPolicy ¶
added in v0.224.0
func (r *ProjectsInstancesMaterializedViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesMaterializedViewsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesMaterializedViewsService) List ¶
added in v0.230.0
func (r *ProjectsInstancesMaterializedViewsService) List(parent string) *ProjectsInstancesMaterializedViewsListCall

List: Lists information about materialized views in an instance.

parent: The unique name of the instance for which the list of materialized views is requested. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesMaterializedViewsService) Patch ¶
added in v0.230.0
func (r *ProjectsInstancesMaterializedViewsService) Patch(name string, materializedview *MaterializedView) *ProjectsInstancesMaterializedViewsPatchCall

Patch: Updates a materialized view within an instance.

name: Identifier. The unique name of the materialized view. Format: `projects/{project}/instances/{instance}/materializedViews/{materialized_vi ew}` Views: `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`.
func (*ProjectsInstancesMaterializedViewsService) SetIamPolicy ¶
added in v0.224.0
func (r *ProjectsInstancesMaterializedViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesMaterializedViewsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on an instance resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesMaterializedViewsService) TestIamPermissions ¶
added in v0.224.0
func (r *ProjectsInstancesMaterializedViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified instance resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsInstancesMaterializedViewsSetIamPolicyCall ¶
added in v0.224.0
type ProjectsInstancesMaterializedViewsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsSetIamPolicyCall) Context ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsSetIamPolicyCall) Do ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsSetIamPolicyCall) Fields ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsSetIamPolicyCall) Header ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesMaterializedViewsTestIamPermissionsCall ¶
added in v0.224.0
type ProjectsInstancesMaterializedViewsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Context ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Do ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.materializedViews.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Fields ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesMaterializedViewsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Header ¶
added in v0.224.0
func (c *ProjectsInstancesMaterializedViewsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesPartialUpdateInstanceCall ¶
type ProjectsInstancesPartialUpdateInstanceCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesPartialUpdateInstanceCall) Context ¶
func (c *ProjectsInstancesPartialUpdateInstanceCall) Context(ctx context.Context) *ProjectsInstancesPartialUpdateInstanceCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesPartialUpdateInstanceCall) Do ¶
func (c *ProjectsInstancesPartialUpdateInstanceCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.partialUpdateInstance" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesPartialUpdateInstanceCall) Fields ¶
func (c *ProjectsInstancesPartialUpdateInstanceCall) Fields(s ...googleapi.Field) *ProjectsInstancesPartialUpdateInstanceCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesPartialUpdateInstanceCall) Header ¶
func (c *ProjectsInstancesPartialUpdateInstanceCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesPartialUpdateInstanceCall) UpdateMask ¶
func (c *ProjectsInstancesPartialUpdateInstanceCall) UpdateMask(updateMask string) *ProjectsInstancesPartialUpdateInstanceCall

UpdateMask sets the optional parameter "updateMask": Required. The subset of Instance fields which should be replaced. Must be explicitly set.

type ProjectsInstancesService ¶
type ProjectsInstancesService struct {
	AppProfiles *ProjectsInstancesAppProfilesService

	Clusters *ProjectsInstancesClustersService

	LogicalViews *ProjectsInstancesLogicalViewsService

	MaterializedViews *ProjectsInstancesMaterializedViewsService

	Tables *ProjectsInstancesTablesService
	// contains filtered or unexported fields
}
func NewProjectsInstancesService ¶
func NewProjectsInstancesService(s *Service) *ProjectsInstancesService
func (*ProjectsInstancesService) Create ¶
func (r *ProjectsInstancesService) Create(parent string, createinstancerequest *CreateInstanceRequest) *ProjectsInstancesCreateCall

Create: Create an instance within a project. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled.

parent: The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`.
func (*ProjectsInstancesService) Delete ¶
func (r *ProjectsInstancesService) Delete(name string) *ProjectsInstancesDeleteCall

Delete: Delete an instance from a project.

name: The unique name of the instance to be deleted. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesService) Get ¶
func (r *ProjectsInstancesService) Get(name string) *ProjectsInstancesGetCall

Get: Gets information about an instance.

name: The unique name of the requested instance. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesService) GetIamPolicy ¶
func (r *ProjectsInstancesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesGetIamPolicyCall

GetIamPolicy: Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesService) List ¶
func (r *ProjectsInstancesService) List(parent string) *ProjectsInstancesListCall

List: Lists information about instances in a project.

parent: The unique name of the project for which a list of instances is requested. Values are of the form `projects/{project}`.
func (*ProjectsInstancesService) PartialUpdateInstance ¶
func (r *ProjectsInstancesService) PartialUpdateInstance(name string, instance *Instance) *ProjectsInstancesPartialUpdateInstanceCall

PartialUpdateInstance: Partially updates an instance within a project. This method can modify all fields of an Instance and is the preferred way to update an Instance.

name: The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`.
func (*ProjectsInstancesService) SetIamPolicy ¶
func (r *ProjectsInstancesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesSetIamPolicyCall

SetIamPolicy: Sets the access control policy on an instance resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesService) TestIamPermissions ¶
func (r *ProjectsInstancesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified instance resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesService) Update ¶
func (r *ProjectsInstancesService) Update(name string, instance *Instance) *ProjectsInstancesUpdateCall

Update: Updates an instance within a project. This method updates only the display name and type for an Instance. To update other Instance properties, such as labels, use PartialUpdateInstance.

name: The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`.
type ProjectsInstancesSetIamPolicyCall ¶
type ProjectsInstancesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesSetIamPolicyCall) Context ¶
func (c *ProjectsInstancesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesSetIamPolicyCall) Do ¶
func (c *ProjectsInstancesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesSetIamPolicyCall) Fields ¶
func (c *ProjectsInstancesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesSetIamPolicyCall) Header ¶
func (c *ProjectsInstancesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesAuthorizedViewsCreateCall ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsCreateCall) AuthorizedViewId ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) AuthorizedViewId(authorizedViewId string) *ProjectsInstancesTablesAuthorizedViewsCreateCall

AuthorizedViewId sets the optional parameter "authorizedViewId": Required. The id of the AuthorizedView to create. This AuthorizedView must not already exist. The `authorized_view_id` appended to `parent` forms the full AuthorizedView name of the form `projects/{project}/instances/{instance}/tables/{table}/authorizedView/{autho rized_view}`.

func (*ProjectsInstancesTablesAuthorizedViewsCreateCall) Context ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsCreateCall) Do ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsCreateCall) Fields ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsCreateCall) Header ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesAuthorizedViewsDeleteCall ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsDeleteCall) Context ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsDeleteCall) Do ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsDeleteCall) Etag ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Etag(etag string) *ProjectsInstancesTablesAuthorizedViewsDeleteCall

Etag sets the optional parameter "etag": The current etag of the AuthorizedView. If an etag is provided and does not match the current etag of the AuthorizedView, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsInstancesTablesAuthorizedViewsDeleteCall) Fields ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsDeleteCall) Header ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesAuthorizedViewsGetCall ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsGetCall) Context ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsGetCall) Do ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedView, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedView.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsGetCall) Fields ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsGetCall) Header ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesAuthorizedViewsGetCall) IfNoneMatch ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesAuthorizedViewsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesTablesAuthorizedViewsGetCall) View ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetCall) View(view string) *ProjectsInstancesTablesAuthorizedViewsGetCall

View sets the optional parameter "view": The resource_view to be applied to the returned AuthorizedView's fields. Default to BASIC.

Possible values:

"RESPONSE_VIEW_UNSPECIFIED" - Uses the default view for each method as


documented in the request.

"NAME_ONLY" - Only populates `name`.
"BASIC" - Only populates the AuthorizedView's basic metadata. This


includes: name, deletion_protection, etag.

"FULL" - Populates every fields.

type ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall ¶
added in v0.173.0
type ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Context ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Do ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Fields ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Header ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesAuthorizedViewsListCall ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsListCall) Context ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) Do ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedViewsResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedViewsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) Fields ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) Header ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) IfNoneMatch ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesAuthorizedViewsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) PageSize ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) PageSize(pageSize int64) *ProjectsInstancesTablesAuthorizedViewsListCall

PageSize sets the optional parameter "pageSize": Maximum number of results per page. A page_size of zero lets the server choose the number of items to return. A page_size which is strictly positive will return at most that many items. A negative page_size will cause an error. Following the first request, subsequent paginated calls are not required to pass a page_size. If a page_size is set in subsequent calls, it must match the page_size given in the first request.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) PageToken ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) PageToken(pageToken string) *ProjectsInstancesTablesAuthorizedViewsListCall

PageToken sets the optional parameter "pageToken": The value of `next_page_token` returned by a previous call.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) Pages ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) Pages(ctx context.Context, f func(*ListAuthorizedViewsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsInstancesTablesAuthorizedViewsListCall) View ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsListCall) View(view string) *ProjectsInstancesTablesAuthorizedViewsListCall

View sets the optional parameter "view": The resource_view to be applied to the returned AuthorizedViews' fields. Default to NAME_ONLY.

Possible values:

"RESPONSE_VIEW_UNSPECIFIED" - Uses the default view for each method as


documented in the request.

"NAME_ONLY" - Only populates `name`.
"BASIC" - Only populates the AuthorizedView's basic metadata. This


includes: name, deletion_protection, etag.

"FULL" - Populates every fields.

type ProjectsInstancesTablesAuthorizedViewsPatchCall ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) Context ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) Do ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) Fields ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) Header ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) IgnoreWarnings ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesAuthorizedViewsPatchCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": If true, ignore the safety checks when updating the AuthorizedView.

func (*ProjectsInstancesTablesAuthorizedViewsPatchCall) UpdateMask ¶
added in v0.171.0
func (c *ProjectsInstancesTablesAuthorizedViewsPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesAuthorizedViewsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. A mask specifying which fields in the AuthorizedView resource should be updated. This mask is relative to the AuthorizedView resource, not to the request message. A field will be overwritten if it is in the mask. If empty, all fields set in the request will be overwritten. A special value `*` means to overwrite all fields (including fields not set in the request).

type ProjectsInstancesTablesAuthorizedViewsService ¶
added in v0.171.0
type ProjectsInstancesTablesAuthorizedViewsService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesTablesAuthorizedViewsService ¶
added in v0.171.0
func NewProjectsInstancesTablesAuthorizedViewsService(s *Service) *ProjectsInstancesTablesAuthorizedViewsService
func (*ProjectsInstancesTablesAuthorizedViewsService) Create ¶
added in v0.171.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) Create(parent string, authorizedview *AuthorizedView) *ProjectsInstancesTablesAuthorizedViewsCreateCall

Create: Creates a new AuthorizedView in a table.

parent: This is the name of the table the AuthorizedView belongs to. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesAuthorizedViewsService) Delete ¶
added in v0.171.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) Delete(name string) *ProjectsInstancesTablesAuthorizedViewsDeleteCall

Delete: Permanently deletes a specified AuthorizedView.

name: The unique name of the AuthorizedView to be deleted. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{au thorized_view}`.
func (*ProjectsInstancesTablesAuthorizedViewsService) Get ¶
added in v0.171.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) Get(name string) *ProjectsInstancesTablesAuthorizedViewsGetCall

Get: Gets information from a specified AuthorizedView.

name: The unique name of the requested AuthorizedView. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{au thorized_view}`.
func (*ProjectsInstancesTablesAuthorizedViewsService) GetIamPolicy ¶
added in v0.173.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesAuthorizedViewsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a Bigtable resource. Returns an empty policy if the resource exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesAuthorizedViewsService) List ¶
added in v0.171.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) List(parent string) *ProjectsInstancesTablesAuthorizedViewsListCall

List: Lists all AuthorizedViews from a specific table.

parent: The unique name of the table for which AuthorizedViews should be listed. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesAuthorizedViewsService) Patch ¶
added in v0.171.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) Patch(name string, authorizedview *AuthorizedView) *ProjectsInstancesTablesAuthorizedViewsPatchCall

Patch: Updates an AuthorizedView in a table.

name: Identifier. The name of this AuthorizedView. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{au thorized_view}`.
func (*ProjectsInstancesTablesAuthorizedViewsService) SetIamPolicy ¶
added in v0.173.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on a Bigtable resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesAuthorizedViewsService) TestIamPermissions ¶
added in v0.173.0
func (r *ProjectsInstancesTablesAuthorizedViewsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified Bigtable resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall ¶
added in v0.173.0
type ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Context ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Do ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Fields ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Header ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall ¶
added in v0.173.0
type ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Context ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Do ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.authorizedViews.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Fields ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Header ¶
added in v0.173.0
func (c *ProjectsInstancesTablesAuthorizedViewsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesCheckConsistencyCall ¶
type ProjectsInstancesTablesCheckConsistencyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesCheckConsistencyCall) Context ¶
func (c *ProjectsInstancesTablesCheckConsistencyCall) Context(ctx context.Context) *ProjectsInstancesTablesCheckConsistencyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesCheckConsistencyCall) Do ¶
func (c *ProjectsInstancesTablesCheckConsistencyCall) Do(opts ...googleapi.CallOption) (*CheckConsistencyResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.checkConsistency" call. Any non-2xx status code is an error. Response headers are in either *CheckConsistencyResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesCheckConsistencyCall) Fields ¶
func (c *ProjectsInstancesTablesCheckConsistencyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesCheckConsistencyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesCheckConsistencyCall) Header ¶
func (c *ProjectsInstancesTablesCheckConsistencyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesCreateCall ¶
type ProjectsInstancesTablesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesCreateCall) Context ¶
func (c *ProjectsInstancesTablesCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesCreateCall) Do ¶
func (c *ProjectsInstancesTablesCreateCall) Do(opts ...googleapi.CallOption) (*Table, error)

Do executes the "bigtableadmin.projects.instances.tables.create" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesCreateCall) Fields ¶
func (c *ProjectsInstancesTablesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesCreateCall) Header ¶
func (c *ProjectsInstancesTablesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesDeleteCall ¶
type ProjectsInstancesTablesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesDeleteCall) Context ¶
func (c *ProjectsInstancesTablesDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesDeleteCall) Do ¶
func (c *ProjectsInstancesTablesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.tables.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesDeleteCall) Fields ¶
func (c *ProjectsInstancesTablesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesDeleteCall) Header ¶
func (c *ProjectsInstancesTablesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesDropRowRangeCall ¶
type ProjectsInstancesTablesDropRowRangeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesDropRowRangeCall) Context ¶
func (c *ProjectsInstancesTablesDropRowRangeCall) Context(ctx context.Context) *ProjectsInstancesTablesDropRowRangeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesDropRowRangeCall) Do ¶
func (c *ProjectsInstancesTablesDropRowRangeCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.tables.dropRowRange" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesDropRowRangeCall) Fields ¶
func (c *ProjectsInstancesTablesDropRowRangeCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesDropRowRangeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesDropRowRangeCall) Header ¶
func (c *ProjectsInstancesTablesDropRowRangeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesGenerateConsistencyTokenCall ¶
type ProjectsInstancesTablesGenerateConsistencyTokenCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesGenerateConsistencyTokenCall) Context ¶
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Context(ctx context.Context) *ProjectsInstancesTablesGenerateConsistencyTokenCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesGenerateConsistencyTokenCall) Do ¶
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Do(opts ...googleapi.CallOption) (*GenerateConsistencyTokenResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.generateConsistencyToken" call. Any non-2xx status code is an error. Response headers are in either *GenerateConsistencyTokenResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesGenerateConsistencyTokenCall) Fields ¶
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGenerateConsistencyTokenCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesGenerateConsistencyTokenCall) Header ¶
func (c *ProjectsInstancesTablesGenerateConsistencyTokenCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesGetCall ¶
type ProjectsInstancesTablesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesGetCall) Context ¶
func (c *ProjectsInstancesTablesGetCall) Context(ctx context.Context) *ProjectsInstancesTablesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesGetCall) Do ¶
func (c *ProjectsInstancesTablesGetCall) Do(opts ...googleapi.CallOption) (*Table, error)

Do executes the "bigtableadmin.projects.instances.tables.get" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesGetCall) Fields ¶
func (c *ProjectsInstancesTablesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesGetCall) Header ¶
func (c *ProjectsInstancesTablesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesGetCall) IfNoneMatch ¶
func (c *ProjectsInstancesTablesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesTablesGetCall) View ¶
func (c *ProjectsInstancesTablesGetCall) View(view string) *ProjectsInstancesTablesGetCall

View sets the optional parameter "view": The view to be applied to the returned table's fields. Defaults to `SCHEMA_VIEW` if unspecified.

Possible values:

"VIEW_UNSPECIFIED" - Uses the default view for each method as documented


in its request.

"NAME_ONLY" - Only populates `name`.
"SCHEMA_VIEW" - Only populates `name` and fields related to the table's


schema.

"REPLICATION_VIEW" - Only populates `name` and fields related to the


table's replication state.

"ENCRYPTION_VIEW" - Only populates `name` and fields related to the


table's encryption state.

"STATS_VIEW" - Only populates `name` and fields related to the table's


stats (e.g. TableStats and ColumnFamilyStats).

"FULL" - Populates all fields except for stats. See STATS_VIEW to request


stats.

type ProjectsInstancesTablesGetIamPolicyCall ¶
added in v0.4.0
type ProjectsInstancesTablesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesGetIamPolicyCall) Context ¶
added in v0.4.0
func (c *ProjectsInstancesTablesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesGetIamPolicyCall) Do ¶
added in v0.4.0
func (c *ProjectsInstancesTablesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesGetIamPolicyCall) Fields ¶
added in v0.4.0
func (c *ProjectsInstancesTablesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesGetIamPolicyCall) Header ¶
added in v0.4.0
func (c *ProjectsInstancesTablesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesListCall ¶
type ProjectsInstancesTablesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesListCall) Context ¶
func (c *ProjectsInstancesTablesListCall) Context(ctx context.Context) *ProjectsInstancesTablesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesListCall) Do ¶
func (c *ProjectsInstancesTablesListCall) Do(opts ...googleapi.CallOption) (*ListTablesResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.list" call. Any non-2xx status code is an error. Response headers are in either *ListTablesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesListCall) Fields ¶
func (c *ProjectsInstancesTablesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesListCall) Header ¶
func (c *ProjectsInstancesTablesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesListCall) IfNoneMatch ¶
func (c *ProjectsInstancesTablesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesTablesListCall) PageSize ¶
func (c *ProjectsInstancesTablesListCall) PageSize(pageSize int64) *ProjectsInstancesTablesListCall

PageSize sets the optional parameter "pageSize": Maximum number of results per page. A page_size of zero lets the server choose the number of items to return. A page_size which is strictly positive will return at most that many items. A negative page_size will cause an error. Following the first request, subsequent paginated calls are not required to pass a page_size. If a page_size is set in subsequent calls, it must match the page_size given in the first request.

func (*ProjectsInstancesTablesListCall) PageToken ¶
func (c *ProjectsInstancesTablesListCall) PageToken(pageToken string) *ProjectsInstancesTablesListCall

PageToken sets the optional parameter "pageToken": The value of `next_page_token` returned by a previous call.

func (*ProjectsInstancesTablesListCall) Pages ¶
func (c *ProjectsInstancesTablesListCall) Pages(ctx context.Context, f func(*ListTablesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsInstancesTablesListCall) View ¶
func (c *ProjectsInstancesTablesListCall) View(view string) *ProjectsInstancesTablesListCall

View sets the optional parameter "view": The view to be applied to the returned tables' fields. Only NAME_ONLY view (default), REPLICATION_VIEW and ENCRYPTION_VIEW are supported.

Possible values:

"VIEW_UNSPECIFIED" - Uses the default view for each method as documented


in its request.

"NAME_ONLY" - Only populates `name`.
"SCHEMA_VIEW" - Only populates `name` and fields related to the table's


schema.

"REPLICATION_VIEW" - Only populates `name` and fields related to the


table's replication state.

"ENCRYPTION_VIEW" - Only populates `name` and fields related to the


table's encryption state.

"STATS_VIEW" - Only populates `name` and fields related to the table's


stats (e.g. TableStats and ColumnFamilyStats).

"FULL" - Populates all fields except for stats. See STATS_VIEW to request


stats.

type ProjectsInstancesTablesModifyColumnFamiliesCall ¶
type ProjectsInstancesTablesModifyColumnFamiliesCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesModifyColumnFamiliesCall) Context ¶
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Context(ctx context.Context) *ProjectsInstancesTablesModifyColumnFamiliesCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesModifyColumnFamiliesCall) Do ¶
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Do(opts ...googleapi.CallOption) (*Table, error)

Do executes the "bigtableadmin.projects.instances.tables.modifyColumnFamilies" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesModifyColumnFamiliesCall) Fields ¶
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesModifyColumnFamiliesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesModifyColumnFamiliesCall) Header ¶
func (c *ProjectsInstancesTablesModifyColumnFamiliesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesPatchCall ¶
added in v0.103.0
type ProjectsInstancesTablesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesPatchCall) Context ¶
added in v0.103.0
func (c *ProjectsInstancesTablesPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesPatchCall) Do ¶
added in v0.103.0
func (c *ProjectsInstancesTablesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesPatchCall) Fields ¶
added in v0.103.0
func (c *ProjectsInstancesTablesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesPatchCall) Header ¶
added in v0.103.0
func (c *ProjectsInstancesTablesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesPatchCall) IgnoreWarnings ¶
added in v0.230.0
func (c *ProjectsInstancesTablesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesPatchCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": If true, ignore safety checks when updating the table.

func (*ProjectsInstancesTablesPatchCall) UpdateMask ¶
added in v0.103.0
func (c *ProjectsInstancesTablesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update. A mask specifying which fields (e.g. `change_stream_config`) in the `table` field should be updated. This mask is relative to the `table` field, not to the request message. The wildcard (*) path is currently not supported. Currently UpdateTable is only supported for the following fields: * `change_stream_config` * `change_stream_config.retention_period` * `deletion_protection` * `automated_backup_policy` * `automated_backup_policy.retention_period` * `automated_backup_policy.frequency` * `row_key_schema` If `column_families` is set in `update_mask`, it will return an UNIMPLEMENTED error.

type ProjectsInstancesTablesRestoreCall ¶
added in v0.30.0
type ProjectsInstancesTablesRestoreCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesRestoreCall) Context ¶
added in v0.30.0
func (c *ProjectsInstancesTablesRestoreCall) Context(ctx context.Context) *ProjectsInstancesTablesRestoreCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesRestoreCall) Do ¶
added in v0.30.0
func (c *ProjectsInstancesTablesRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.restore" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesRestoreCall) Fields ¶
added in v0.30.0
func (c *ProjectsInstancesTablesRestoreCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesRestoreCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesRestoreCall) Header ¶
added in v0.30.0
func (c *ProjectsInstancesTablesRestoreCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesSchemaBundlesCreateCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesCreateCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesCreateCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesCreateCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesCreateCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesSchemaBundlesCreateCall) SchemaBundleId ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesCreateCall) SchemaBundleId(schemaBundleId string) *ProjectsInstancesTablesSchemaBundlesCreateCall

SchemaBundleId sets the optional parameter "schemaBundleId": Required. The unique ID to use for the schema bundle, which will become the final component of the schema bundle's resource name.

type ProjectsInstancesTablesSchemaBundlesDeleteCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesDeleteCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesDeleteCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesDeleteCall) Etag ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Etag(etag string) *ProjectsInstancesTablesSchemaBundlesDeleteCall

Etag sets the optional parameter "etag": The etag of the schema bundle. If this is provided, it must match the server's etag. The server returns an ABORTED error on a mismatched etag.

func (*ProjectsInstancesTablesSchemaBundlesDeleteCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesDeleteCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesSchemaBundlesGetCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesGetCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesGetCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Do(opts ...googleapi.CallOption) (*SchemaBundle, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.get" call. Any non-2xx status code is an error. Response headers are in either *SchemaBundle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesGetCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesGetCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesSchemaBundlesGetCall) IfNoneMatch ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesSchemaBundlesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesSchemaBundlesListCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesListCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesListCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Do(opts ...googleapi.CallOption) (*ListSchemaBundlesResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.list" call. Any non-2xx status code is an error. Response headers are in either *ListSchemaBundlesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesListCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesListCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesSchemaBundlesListCall) IfNoneMatch ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) IfNoneMatch(entityTag string) *ProjectsInstancesTablesSchemaBundlesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsInstancesTablesSchemaBundlesListCall) PageSize ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) PageSize(pageSize int64) *ProjectsInstancesTablesSchemaBundlesListCall

PageSize sets the optional parameter "pageSize": The maximum number of schema bundles to return. If the value is positive, the server may return at most this value. If unspecified, the server will return the maximum allowed page size.

func (*ProjectsInstancesTablesSchemaBundlesListCall) PageToken ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) PageToken(pageToken string) *ProjectsInstancesTablesSchemaBundlesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSchemaBundles` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSchemaBundles` must match the call that provided the page token.

func (*ProjectsInstancesTablesSchemaBundlesListCall) Pages ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) Pages(ctx context.Context, f func(*ListSchemaBundlesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsInstancesTablesSchemaBundlesListCall) View ¶
added in v0.244.0
func (c *ProjectsInstancesTablesSchemaBundlesListCall) View(view string) *ProjectsInstancesTablesSchemaBundlesListCall

View sets the optional parameter "view": The resource_view to be applied to the returned SchemaBundles' fields. Defaults to NAME_ONLY.

Possible values:

"SCHEMA_BUNDLE_VIEW_UNSPECIFIED" - Uses the default view for each method


as documented in the request.

"NAME_ONLY" - Only populates `name`.
"BASIC" - Only populates the SchemaBundle's basic metadata. This includes:


name, etag, create_time, update_time.

"FULL" - Populates every field.

type ProjectsInstancesTablesSchemaBundlesPatchCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesPatchCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesPatchCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesPatchCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesPatchCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsInstancesTablesSchemaBundlesPatchCall) IgnoreWarnings ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) IgnoreWarnings(ignoreWarnings bool) *ProjectsInstancesTablesSchemaBundlesPatchCall

IgnoreWarnings sets the optional parameter "ignoreWarnings": If set, ignore the safety checks when updating the Schema Bundle. The safety checks are: - The new Schema Bundle is backwards compatible with the existing Schema Bundle.

func (*ProjectsInstancesTablesSchemaBundlesPatchCall) UpdateMask ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesPatchCall) UpdateMask(updateMask string) *ProjectsInstancesTablesSchemaBundlesPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update.

type ProjectsInstancesTablesSchemaBundlesService ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesService struct {
	// contains filtered or unexported fields
}
func NewProjectsInstancesTablesSchemaBundlesService ¶
added in v0.240.0
func NewProjectsInstancesTablesSchemaBundlesService(s *Service) *ProjectsInstancesTablesSchemaBundlesService
func (*ProjectsInstancesTablesSchemaBundlesService) Create ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) Create(parent string, schemabundle *SchemaBundle) *ProjectsInstancesTablesSchemaBundlesCreateCall

Create: Creates a new schema bundle in the specified table.

parent: The parent resource where this schema bundle will be created. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesSchemaBundlesService) Delete ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) Delete(name string) *ProjectsInstancesTablesSchemaBundlesDeleteCall

Delete: Deletes a schema bundle in the specified table.

name: The unique name of the schema bundle to delete. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{sche ma_bundle}`.
func (*ProjectsInstancesTablesSchemaBundlesService) Get ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) Get(name string) *ProjectsInstancesTablesSchemaBundlesGetCall

Get: Gets metadata information about the specified schema bundle.

name: The unique name of the schema bundle to retrieve. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{sche ma_bundle}`.
func (*ProjectsInstancesTablesSchemaBundlesService) GetIamPolicy ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesSchemaBundlesGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a Bigtable resource. Returns an empty policy if the resource exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesSchemaBundlesService) List ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) List(parent string) *ProjectsInstancesTablesSchemaBundlesListCall

List: Lists all schema bundles associated with the specified table.

parent: The parent, which owns this collection of schema bundles. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesSchemaBundlesService) Patch ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) Patch(name string, schemabundle *SchemaBundle) *ProjectsInstancesTablesSchemaBundlesPatchCall

Patch: Updates a schema bundle in the specified table.

name: Identifier. The unique name identifying this schema bundle. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{sche ma_bundle}`.
func (*ProjectsInstancesTablesSchemaBundlesService) SetIamPolicy ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall

SetIamPolicy: Sets the access control policy on a Bigtable resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesSchemaBundlesService) TestIamPermissions ¶
added in v0.240.0
func (r *ProjectsInstancesTablesSchemaBundlesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified Bigtable resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall ¶
added in v0.240.0
type ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Context ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Do ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.schemaBundles.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Fields ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Header ¶
added in v0.240.0
func (c *ProjectsInstancesTablesSchemaBundlesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesService ¶
type ProjectsInstancesTablesService struct {
	AuthorizedViews *ProjectsInstancesTablesAuthorizedViewsService

	SchemaBundles *ProjectsInstancesTablesSchemaBundlesService
	// contains filtered or unexported fields
}
func NewProjectsInstancesTablesService ¶
func NewProjectsInstancesTablesService(s *Service) *ProjectsInstancesTablesService
func (*ProjectsInstancesTablesService) CheckConsistency ¶
func (r *ProjectsInstancesTablesService) CheckConsistency(name string, checkconsistencyrequest *CheckConsistencyRequest) *ProjectsInstancesTablesCheckConsistencyCall

CheckConsistency: Checks replication consistency based on a consistency token, that is, if replication has caught up based on the conditions specified in the token and the check request.

name: The unique name of the Table for which to check replication consistency. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) Create ¶
func (r *ProjectsInstancesTablesService) Create(parent string, createtablerequest *CreateTableRequest) *ProjectsInstancesTablesCreateCall

Create: Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request.

parent: The unique name of the instance in which to create the table. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesTablesService) Delete ¶
func (r *ProjectsInstancesTablesService) Delete(name string) *ProjectsInstancesTablesDeleteCall

Delete: Permanently deletes a specified table and all of its data.

name: The unique name of the table to be deleted. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) DropRowRange ¶
func (r *ProjectsInstancesTablesService) DropRowRange(name string, droprowrangerequest *DropRowRangeRequest) *ProjectsInstancesTablesDropRowRangeCall

DropRowRange: Permanently drop/delete a row range from a specified table. The request can specify whether to delete all rows in a table, or only those that match a particular prefix. Note that row key prefixes used here are treated as service data. For more information about how service data is handled, see the Google Cloud Privacy Notice (https://cloud.google.com/terms/cloud-privacy-notice).

name: The unique name of the table on which to drop a range of rows. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) GenerateConsistencyToken ¶
func (r *ProjectsInstancesTablesService) GenerateConsistencyToken(name string, generateconsistencytokenrequest *GenerateConsistencyTokenRequest) *ProjectsInstancesTablesGenerateConsistencyTokenCall

GenerateConsistencyToken: Generates a consistency token for a Table, which can be used in CheckConsistency to check whether mutations to the table that finished before this call started have been replicated. The tokens will be available for 90 days.

name: The unique name of the Table for which to create a consistency token. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) Get ¶
func (r *ProjectsInstancesTablesService) Get(name string) *ProjectsInstancesTablesGetCall

Get: Gets metadata information about the specified table.

name: The unique name of the requested table. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) GetIamPolicy ¶
added in v0.4.0
func (r *ProjectsInstancesTablesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *ProjectsInstancesTablesGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a Bigtable resource. Returns an empty policy if the resource exists but does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesService) List ¶
func (r *ProjectsInstancesTablesService) List(parent string) *ProjectsInstancesTablesListCall

List: Lists all tables served from a specified instance.

parent: The unique name of the instance for which tables should be listed. Values are of the form `projects/{project}/instances/{instance}`.
func (*ProjectsInstancesTablesService) ModifyColumnFamilies ¶
func (r *ProjectsInstancesTablesService) ModifyColumnFamilies(name string, modifycolumnfamiliesrequest *ModifyColumnFamiliesRequest) *ProjectsInstancesTablesModifyColumnFamiliesCall

ModifyColumnFamilies: Performs a series of column family modifications on the specified table. Either all or none of the modifications will occur before this method returns, but data requests received prior to that point may see a table where only some modifications have taken effect.

name: The unique name of the table whose families should be modified. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
func (*ProjectsInstancesTablesService) Patch ¶
added in v0.103.0
func (r *ProjectsInstancesTablesService) Patch(name string, table *Table) *ProjectsInstancesTablesPatchCall

Patch: Updates a specified table.

name: The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `STATS_VIEW`, `FULL`.
func (*ProjectsInstancesTablesService) Restore ¶
added in v0.30.0
func (r *ProjectsInstancesTablesService) Restore(parent string, restoretablerequest *RestoreTableRequest) *ProjectsInstancesTablesRestoreCall

Restore: Create a new table by restoring from a completed backup. The returned table long-running operation can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreTableMetadata. The response type is Table, if successful.

parent: The name of the instance in which to create the restored table. Values are of the form `projects//instances/`.
func (*ProjectsInstancesTablesService) SetIamPolicy ¶
added in v0.4.0
func (r *ProjectsInstancesTablesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsInstancesTablesSetIamPolicyCall

SetIamPolicy: Sets the access control policy on a Bigtable resource. Replaces any existing policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesService) TestIamPermissions ¶
added in v0.4.0
func (r *ProjectsInstancesTablesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsInstancesTablesTestIamPermissionsCall

TestIamPermissions: Returns permissions that the caller has on the specified Bigtable resource.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsInstancesTablesService) Undelete ¶
added in v0.86.0
func (r *ProjectsInstancesTablesService) Undelete(name string, undeletetablerequest *UndeleteTableRequest) *ProjectsInstancesTablesUndeleteCall

Undelete: Restores a specified table which was accidentally deleted.

name: The unique name of the table to be restored. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.
type ProjectsInstancesTablesSetIamPolicyCall ¶
added in v0.4.0
type ProjectsInstancesTablesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesSetIamPolicyCall) Context ¶
added in v0.4.0
func (c *ProjectsInstancesTablesSetIamPolicyCall) Context(ctx context.Context) *ProjectsInstancesTablesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesSetIamPolicyCall) Do ¶
added in v0.4.0
func (c *ProjectsInstancesTablesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "bigtableadmin.projects.instances.tables.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesSetIamPolicyCall) Fields ¶
added in v0.4.0
func (c *ProjectsInstancesTablesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesSetIamPolicyCall) Header ¶
added in v0.4.0
func (c *ProjectsInstancesTablesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesTestIamPermissionsCall ¶
added in v0.4.0
type ProjectsInstancesTablesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesTestIamPermissionsCall) Context ¶
added in v0.4.0
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTablesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesTestIamPermissionsCall) Do ¶
added in v0.4.0
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.tables.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesTestIamPermissionsCall) Fields ¶
added in v0.4.0
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesTestIamPermissionsCall) Header ¶
added in v0.4.0
func (c *ProjectsInstancesTablesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTablesUndeleteCall ¶
added in v0.86.0
type ProjectsInstancesTablesUndeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTablesUndeleteCall) Context ¶
added in v0.86.0
func (c *ProjectsInstancesTablesUndeleteCall) Context(ctx context.Context) *ProjectsInstancesTablesUndeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTablesUndeleteCall) Do ¶
added in v0.86.0
func (c *ProjectsInstancesTablesUndeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "bigtableadmin.projects.instances.tables.undelete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTablesUndeleteCall) Fields ¶
added in v0.86.0
func (c *ProjectsInstancesTablesUndeleteCall) Fields(s ...googleapi.Field) *ProjectsInstancesTablesUndeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTablesUndeleteCall) Header ¶
added in v0.86.0
func (c *ProjectsInstancesTablesUndeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesTestIamPermissionsCall ¶
type ProjectsInstancesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesTestIamPermissionsCall) Context ¶
func (c *ProjectsInstancesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsInstancesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesTestIamPermissionsCall) Do ¶
func (c *ProjectsInstancesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "bigtableadmin.projects.instances.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesTestIamPermissionsCall) Fields ¶
func (c *ProjectsInstancesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsInstancesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesTestIamPermissionsCall) Header ¶
func (c *ProjectsInstancesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsInstancesUpdateCall ¶
type ProjectsInstancesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsInstancesUpdateCall) Context ¶
func (c *ProjectsInstancesUpdateCall) Context(ctx context.Context) *ProjectsInstancesUpdateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsInstancesUpdateCall) Do ¶
func (c *ProjectsInstancesUpdateCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "bigtableadmin.projects.instances.update" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsInstancesUpdateCall) Fields ¶
func (c *ProjectsInstancesUpdateCall) Fields(s ...googleapi.Field) *ProjectsInstancesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsInstancesUpdateCall) Header ¶
func (c *ProjectsInstancesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsListCall ¶
added in v0.7.0
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "bigtableadmin.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.230.0
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

func (*ProjectsLocationsListCall) Fields ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsListCall) Filter ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*ProjectsLocationsListCall) Header ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsListCall) IfNoneMatch ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsListCall) PageSize ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*ProjectsLocationsListCall) PageToken ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

func (*ProjectsLocationsListCall) Pages ¶
added in v0.7.0
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsService ¶
added in v0.7.0
type ProjectsLocationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
added in v0.7.0
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) List ¶
added in v0.7.0
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

type ProjectsService ¶
type ProjectsService struct {
	Instances *ProjectsInstancesService

	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type ProtoSchema ¶
added in v0.240.0
type ProtoSchema struct {
	// ProtoDescriptors: Required. Contains a protobuf-serialized
	// google.protobuf.FileDescriptorSet
	// (https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto),
	// which could include multiple proto files. To generate it, install
	// (https://grpc.io/docs/protoc-installation/) and run `protoc` with
	// `--include_imports` and `--descriptor_set_out`. For example, to generate for
	// moon/shot/app.proto, run “` $protoc --proto_path=/app_path
	// --proto_path=/lib_path \ --include_imports \
	// --descriptor_set_out=descriptors.pb \ moon/shot/app.proto “` For more
	// details, see protobuffer self description
	// (https://developers.google.com/protocol-buffers/docs/techniques#self-description).
	ProtoDescriptors string `json:"protoDescriptors,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProtoDescriptors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProtoDescriptors") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProtoSchema: Represents a protobuf schema.

func (ProtoSchema) MarshalJSON ¶
added in v0.240.0
func (s ProtoSchema) MarshalJSON() ([]byte, error)
type RestoreInfo ¶
added in v0.30.0
type RestoreInfo struct {
	// BackupInfo: Information about the backup used to restore the table. The
	// backup may no longer exist.
	BackupInfo *BackupInfo `json:"backupInfo,omitempty"`
	// SourceType: The type of the restore source.
	//
	// Possible values:
	//   "RESTORE_SOURCE_TYPE_UNSPECIFIED" - No restore associated.
	//   "BACKUP" - A backup was used as the source of the restore.
	SourceType string `json:"sourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreInfo: Information about a table restore.

func (RestoreInfo) MarshalJSON ¶
added in v0.30.0
func (s RestoreInfo) MarshalJSON() ([]byte, error)
type RestoreTableMetadata ¶
added in v0.30.0
type RestoreTableMetadata struct {
	BackupInfo *BackupInfo `json:"backupInfo,omitempty"`
	// Name: Name of the table being created and restored to.
	Name string `json:"name,omitempty"`
	// OptimizeTableOperationName: If exists, the name of the long-running
	// operation that will be used to track the post-restore optimization process
	// to optimize the performance of the restored table. The metadata type of the
	// long-running operation is OptimizeRestoredTableMetadata. The response type
	// is Empty. This long-running operation may be automatically created by the
	// system if applicable after the RestoreTable long-running operation completes
	// successfully. This operation may not be created if the table is already
	// optimized or the restore was not successful.
	OptimizeTableOperationName string `json:"optimizeTableOperationName,omitempty"`
	// Progress: The progress of the RestoreTable operation.
	Progress *OperationProgress `json:"progress,omitempty"`
	// SourceType: The type of the restore source.
	//
	// Possible values:
	//   "RESTORE_SOURCE_TYPE_UNSPECIFIED" - No restore associated.
	//   "BACKUP" - A backup was used as the source of the restore.
	SourceType string `json:"sourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreTableMetadata: Metadata type for the long-running operation returned by RestoreTable.

func (RestoreTableMetadata) MarshalJSON ¶
added in v0.30.0
func (s RestoreTableMetadata) MarshalJSON() ([]byte, error)
type RestoreTableRequest ¶
added in v0.30.0
type RestoreTableRequest struct {
	// Backup: Name of the backup from which to restore. Values are of the form
	// `projects//instances//clusters//backups/`.
	Backup string `json:"backup,omitempty"`
	// TableId: Required. The id of the table to create and restore to. This table
	// must not already exist. The `table_id` appended to `parent` forms the full
	// table name of the form `projects//instances//tables/`.
	TableId string `json:"tableId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Backup") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Backup") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreTableRequest: The request for RestoreTable.

func (RestoreTableRequest) MarshalJSON ¶
added in v0.30.0
func (s RestoreTableRequest) MarshalJSON() ([]byte, error)
type RowAffinity ¶
added in v0.198.0
type RowAffinity struct {
}

RowAffinity: If enabled, Bigtable will route the request based on the row key of the request, rather than randomly. Instead, each row key will be assigned to a cluster, and will stick to that cluster. If clusters are added or removed, then this may affect which row keys stick to which clusters. To avoid this, users can use a cluster group to specify which clusters are to be used. In this case, new clusters that are not a part of the cluster group will not be routed to, and routing will be unaffected by the new cluster. Moreover, clusters specified in the cluster group cannot be deleted unless removed from the cluster group.

type SchemaBundle ¶
added in v0.240.0
type SchemaBundle struct {
	// Etag: Optional. The etag for this schema bundle. This may be sent on update
	// and delete requests to ensure the client has an up-to-date value before
	// proceeding. The server returns an ABORTED error on a mismatched etag.
	Etag string `json:"etag,omitempty"`
	// Name: Identifier. The unique name identifying this schema bundle. Values are
	// of the form
	// `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema
	// _bundle}`
	Name string `json:"name,omitempty"`
	// ProtoSchema: Schema for Protobufs.
	ProtoSchema *ProtoSchema `json:"protoSchema,omitempty"`

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

SchemaBundle: A named collection of related schemas.

func (SchemaBundle) MarshalJSON ¶
added in v0.240.0
func (s SchemaBundle) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Operations *OperationsService

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type SetIamPolicyRequest ¶
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
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type SingleClusterRouting ¶
type SingleClusterRouting struct {
	// AllowTransactionalWrites: Whether or not `CheckAndMutateRow` and
	// `ReadModifyWriteRow` requests are allowed by this app profile. It is unsafe
	// to send these requests to the same table/row/column in multiple clusters.
	AllowTransactionalWrites bool `json:"allowTransactionalWrites,omitempty"`
	// ClusterId: The cluster to which read/write requests should be routed.
	ClusterId string `json:"clusterId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowTransactionalWrites")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowTransactionalWrites") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SingleClusterRouting: Unconditionally routes all read/write requests to a specific cluster. This option preserves read-your-writes consistency but does not improve availability.

func (SingleClusterRouting) MarshalJSON ¶
func (s SingleClusterRouting) MarshalJSON() ([]byte, error)
type Split ¶
type Split struct {
	// Key: Row key to use as an initial tablet boundary.
	Key string `json:"key,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Key") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Key") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Split: An initial split point for a newly created table.

func (Split) MarshalJSON ¶
func (s Split) MarshalJSON() ([]byte, error)
type StandardIsolation ¶
added in v0.149.0
type StandardIsolation struct {
	// Priority: The priority of requests sent using this app profile.
	//
	// Possible values:
	//   "PRIORITY_UNSPECIFIED" - Default value. Mapped to PRIORITY_HIGH (the
	// legacy behavior) on creation.
	//   "PRIORITY_LOW"
	//   "PRIORITY_MEDIUM"
	//   "PRIORITY_HIGH"
	Priority string `json:"priority,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Priority") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Priority") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StandardIsolation: Standard options for isolating this app profile's traffic from other use cases.

func (StandardIsolation) MarshalJSON ¶
added in v0.149.0
func (s StandardIsolation) MarshalJSON() ([]byte, error)
type StandardReadRemoteWrites ¶
added in v0.150.0
type StandardReadRemoteWrites struct {
}

StandardReadRemoteWrites: Checks that all writes before the consistency token was generated are replicated in every cluster and readable.

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
type Table ¶
type Table struct {
	// AutomatedBackupPolicy: If specified, automated backups are enabled for this
	// table. Otherwise, automated backups are disabled.
	AutomatedBackupPolicy *AutomatedBackupPolicy `json:"automatedBackupPolicy,omitempty"`
	// ChangeStreamConfig: If specified, enable the change stream on this table.
	// Otherwise, the change stream is disabled and the change stream is not
	// retained.
	ChangeStreamConfig *ChangeStreamConfig `json:"changeStreamConfig,omitempty"`
	// ClusterStates: Output only. Map from cluster ID to per-cluster table state.
	// If it could not be determined whether or not the table has data in a
	// particular cluster (for example, if its zone is unavailable), then there
	// will be an entry for the cluster with UNKNOWN `replication_status`. Views:
	// `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL`
	ClusterStates map[string]ClusterState `json:"clusterStates,omitempty"`
	// ColumnFamilies: The column families configured for this table, mapped by
	// column family ID. Views: `SCHEMA_VIEW`, `STATS_VIEW`, `FULL`
	ColumnFamilies map[string]ColumnFamily `json:"columnFamilies,omitempty"`
	// DeletionProtection: Set to true to make the table protected against data
	// loss. i.e. deleting the following resources through Admin APIs are
	// prohibited: * The table. * The column families in the table. * The instance
	// containing the table. Note one can still delete the data stored in the table
	// through Data APIs.
	DeletionProtection bool `json:"deletionProtection,omitempty"`
	// Granularity: Immutable. The granularity (i.e. `MILLIS`) at which timestamps
	// are stored in this table. Timestamps not matching the granularity will be
	// rejected. If unspecified at creation time, the value will be set to
	// `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.
	//
	// Possible values:
	//   "TIMESTAMP_GRANULARITY_UNSPECIFIED" - The user did not specify a
	// granularity. Should not be returned. When specified during table creation,
	// MILLIS will be used.
	//   "MILLIS" - The table keeps data versioned at a granularity of 1ms.
	Granularity string `json:"granularity,omitempty"`
	// Name: The unique name of the table. Values are of the form
	// `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views:
	// `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `STATS_VIEW`, `FULL`
	Name string `json:"name,omitempty"`
	// RestoreInfo: Output only. If this table was restored from another data
	// source (e.g. a backup), this field will be populated with information about
	// the restore.
	RestoreInfo *RestoreInfo `json:"restoreInfo,omitempty"`
	// RowKeySchema: The row key schema for this table. The schema is used to
	// decode the raw row key bytes into a structured format. The order of field
	// declarations in this schema is important, as it reflects how the raw row key
	// bytes are structured. Currently, this only affects how the key is read via a
	// GoogleSQL query from the ExecuteQuery API. For a SQL query, the _key column
	// is still read as raw bytes. But queries can reference the key fields by
	// name, which will be decoded from _key using provided type and encoding.
	// Queries that reference key fields will fail if they encounter an invalid row
	// key. For example, if _key = "some_id#2024-04-30#\x00\x13\x00\xf3" with the
	// following schema: { fields { field_name: "id" type { string { encoding:
	// utf8_bytes {} } } } fields { field_name: "date" type { string { encoding:
	// utf8_bytes {} } } } fields { field_name: "product_code" type { int64 {
	// encoding: big_endian_bytes {} } } } encoding { delimited_bytes { delimiter:
	// "#" } } } The decoded key parts would be: id = "some_id", date =
	// "2024-04-30", product_code = 1245427 The query "SELECT _key, product_code
	// FROM table" will return two columns:
	// /------------------------------------------------------\ | _key |
	// product_code | | --------------------------------------|--------------| |
	// "some_id#2024-04-30#\x00\x13\x00\xf3" | 1245427 |
	// \------------------------------------------------------/ The schema has the
	// following invariants: (1) The decoded field values are order-preserved. For
	// read, the field values will be decoded in sorted mode from the raw bytes.
	// (2) Every field in the schema must specify a non-empty name. (3) Every field
	// must specify a type with an associated encoding. The type is limited to
	// scalar types only: Array, Map, Aggregate, and Struct are not allowed. (4)
	// The field names must not collide with existing column family names and
	// reserved keywords "_key" and "_timestamp". The following update operations
	// are allowed for row_key_schema: - Update from an empty schema to a new
	// schema. - Remove the existing schema. This operation requires setting the
	// `ignore_warnings` flag to `true`, since it might be a backward incompatible
	// change. Without the flag, the update request will fail with an
	// INVALID_ARGUMENT error. Any other row key schema update operation (e.g.
	// update existing schema columns names or types) is currently unsupported.
	RowKeySchema *GoogleBigtableAdminV2TypeStruct `json:"rowKeySchema,omitempty"`
	// Stats: Output only. Only available with STATS_VIEW, this includes summary
	// statistics about the entire table contents. For statistics about a specific
	// column family, see ColumnFamilyStats in the mapped ColumnFamily collection
	// above.
	Stats *TableStats `json:"stats,omitempty"`
	// TieredStorageConfig: Rules to specify what data is stored in each storage
	// tier. Different tiers store data differently, providing different trade-offs
	// between cost and performance. Different parts of a table can be stored
	// separately on different tiers. If a config is specified, tiered storage is
	// enabled for this table. Otherwise, tiered storage is disabled. Only SSD
	// instances can configure tiered storage.
	TieredStorageConfig *TieredStorageConfig `json:"tieredStorageConfig,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AutomatedBackupPolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutomatedBackupPolicy") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Table: A collection of user data indexed by row, column, and timestamp. Each table is served using the resources of its parent cluster.

func (Table) MarshalJSON ¶
func (s Table) MarshalJSON() ([]byte, error)
type TableProgress ¶
added in v0.2.0
type TableProgress struct {
	// EstimatedCopiedBytes: Estimate of the number of bytes copied so far for this
	// table. This will eventually reach 'estimated_size_bytes' unless the table
	// copy is CANCELLED.
	EstimatedCopiedBytes int64 `json:"estimatedCopiedBytes,omitempty,string"`
	// EstimatedSizeBytes: Estimate of the size of the table to be copied.
	EstimatedSizeBytes int64 `json:"estimatedSizeBytes,omitempty,string"`
	// Possible values:
	//   "STATE_UNSPECIFIED"
	//   "PENDING" - The table has not yet begun copying to the new cluster.
	//   "COPYING" - The table is actively being copied to the new cluster.
	//   "COMPLETED" - The table has been fully copied to the new cluster.
	//   "CANCELLED" - The table was deleted before it finished copying to the new
	// cluster. Note that tables deleted after completion will stay marked as
	// COMPLETED, not CANCELLED.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EstimatedCopiedBytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EstimatedCopiedBytes") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TableProgress: Progress info for copying a table's data to the new cluster.

func (TableProgress) MarshalJSON ¶
added in v0.2.0
func (s TableProgress) MarshalJSON() ([]byte, error)
type TableStats ¶
added in v0.103.0
type TableStats struct {
	// AverageCellsPerColumn: How many cells are present per column (column family,
	// column qualifier) combinations, averaged over all columns in all rows in the
	// table. e.g. A table with 2 rows: * A row with 3 cells in "family:col" and 1
	// cell in "other:col" (4 cells / 2 columns) * A row with 1 cell in
	// "family:col", 7 cells in "family:other_col", and 7 cells in "other:data" (15
	// cells / 3 columns) would report (4 + 15)/(2 + 3) = 3.8 in this field.
	AverageCellsPerColumn float64 `json:"averageCellsPerColumn,omitempty"`
	// AverageColumnsPerRow: How many (column family, column qualifier)
	// combinations are present per row in the table, averaged over all rows in the
	// table. e.g. A table with 2 rows: * A row with cells in "family:col" and
	// "other:col" (2 distinct columns) * A row with cells in "family:col",
	// "family:other_col", and "other:data" (3 distinct columns) would report (2 +
	// 3)/2 = 2.5 in this field.
	AverageColumnsPerRow float64 `json:"averageColumnsPerRow,omitempty"`
	// LogicalDataBytes: This is roughly how many bytes would be needed to read the
	// entire table (e.g. by streaming all contents out).
	LogicalDataBytes int64 `json:"logicalDataBytes,omitempty,string"`
	// RowCount: How many rows are in the table.
	RowCount int64 `json:"rowCount,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "AverageCellsPerColumn") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AverageCellsPerColumn") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TableStats: Approximate statistics related to a table. These statistics are calculated infrequently, while simultaneously, data in the table can change rapidly. Thus the values reported here (e.g. row count) are very likely out-of date, even the instant they are received in this API. Thus, only treat these values as approximate. IMPORTANT: Everything below is approximate, unless otherwise specified.

func (TableStats) MarshalJSON ¶
added in v0.103.0
func (s TableStats) MarshalJSON() ([]byte, error)
func (*TableStats) UnmarshalJSON ¶
added in v0.103.0
func (s *TableStats) UnmarshalJSON(data []byte) error
type TestIamPermissionsRequest ¶
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
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse ¶
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
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type TieredStorageConfig ¶
added in v0.239.0
type TieredStorageConfig struct {
	// InfrequentAccess: Rule to specify what data is stored in the infrequent
	// access(IA) tier. The IA tier allows storing more data per node with reduced
	// performance.
	InfrequentAccess *TieredStorageRule `json:"infrequentAccess,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InfrequentAccess") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InfrequentAccess") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TieredStorageConfig: Config for tiered storage. A valid config must have a valid TieredStorageRule. Otherwise the whole TieredStorageConfig must be unset. By default all data is stored in the SSD tier (only SSD instances can configure tiered storage).

func (TieredStorageConfig) MarshalJSON ¶
added in v0.239.0
func (s TieredStorageConfig) MarshalJSON() ([]byte, error)
type TieredStorageRule ¶
added in v0.239.0
type TieredStorageRule struct {
	// IncludeIfOlderThan: Include cells older than the given age. For the
	// infrequent access tier, this value must be at least 30 days.
	IncludeIfOlderThan string `json:"includeIfOlderThan,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IncludeIfOlderThan") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IncludeIfOlderThan") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TieredStorageRule: Rule to specify what data is stored in a storage tier.

func (TieredStorageRule) MarshalJSON ¶
added in v0.239.0
func (s TieredStorageRule) MarshalJSON() ([]byte, error)
type Type ¶
added in v0.172.0
type Type struct {
	// AggregateType: Aggregate
	AggregateType *GoogleBigtableAdminV2TypeAggregate `json:"aggregateType,omitempty"`
	// ArrayType: Array
	ArrayType *GoogleBigtableAdminV2TypeArray `json:"arrayType,omitempty"`
	// BoolType: Bool
	BoolType *GoogleBigtableAdminV2TypeBool `json:"boolType,omitempty"`
	// BytesType: Bytes
	BytesType *GoogleBigtableAdminV2TypeBytes `json:"bytesType,omitempty"`
	// DateType: Date
	DateType *GoogleBigtableAdminV2TypeDate `json:"dateType,omitempty"`
	// EnumType: Enum
	EnumType *GoogleBigtableAdminV2TypeEnum `json:"enumType,omitempty"`
	// Float32Type: Float32
	Float32Type *GoogleBigtableAdminV2TypeFloat32 `json:"float32Type,omitempty"`
	// Float64Type: Float64
	Float64Type *GoogleBigtableAdminV2TypeFloat64 `json:"float64Type,omitempty"`
	// GeographyType: Geography
	GeographyType *GoogleBigtableAdminV2TypeGeography `json:"geographyType,omitempty"`
	// Int64Type: Int64
	Int64Type *GoogleBigtableAdminV2TypeInt64 `json:"int64Type,omitempty"`
	// MapType: Map
	MapType *GoogleBigtableAdminV2TypeMap `json:"mapType,omitempty"`
	// ProtoType: Proto
	ProtoType *GoogleBigtableAdminV2TypeProto `json:"protoType,omitempty"`
	// StringType: String
	StringType *GoogleBigtableAdminV2TypeString `json:"stringType,omitempty"`
	// StructType: Struct
	StructType *GoogleBigtableAdminV2TypeStruct `json:"structType,omitempty"`
	// TimestampType: Timestamp
	TimestampType *GoogleBigtableAdminV2TypeTimestamp `json:"timestampType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AggregateType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AggregateType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Type: `Type` represents the type of data that is written to, read from, or stored in Bigtable. It is heavily based on the GoogleSQL standard to help maintain familiarity and consistency across products and features. For compatibility with Bigtable's existing untyped APIs, each `Type` includes an `Encoding` which describes how to convert to or from the underlying data. Each encoding can operate in one of two modes: - Sorted: In this mode, Bigtable guarantees that `Encode(X) <= Encode(Y)` if and only if `X <= Y`. This is useful anywhere sort order is important, for example when encoding keys. - Distinct: In this mode, Bigtable guarantees that if `X != Y` then `Encode(X) != Encode(Y)`. However, the converse is not guaranteed. For example, both `{'foo': '1', 'bar': '2'}` and `{'bar': '2', 'foo': '1'}` are valid encodings of the same JSON value. The API clearly documents which mode is used wherever an encoding can be configured. Each encoding also documents which values are supported in which modes. For example, when encoding INT64 as a numeric STRING, negative numbers cannot be encoded in sorted mode. This is because `INT64(1) > INT64(-1)`, but `STRING("-00001") > STRING("00001")`.

func (Type) MarshalJSON ¶
added in v0.172.0
func (s Type) MarshalJSON() ([]byte, error)
type UndeleteTableMetadata ¶
added in v0.63.0
type UndeleteTableMetadata struct {
	// EndTime: If set, the time at which this operation finished or was cancelled.
	// DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// Name: The name of the table being restored.
	Name string `json:"name,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// StartTime: The time at which this operation started. DEPRECATED: Use
	// request_time instead.
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

UndeleteTableMetadata: Metadata type for the operation returned by google.bigtable.admin.v2.BigtableTableAdmin.UndeleteTable.

func (UndeleteTableMetadata) MarshalJSON ¶
added in v0.63.0
func (s UndeleteTableMetadata) MarshalJSON() ([]byte, error)
type UndeleteTableRequest ¶
added in v0.86.0
type UndeleteTableRequest struct {
}

UndeleteTableRequest: Request message for google.bigtable.admin.v2.BigtableTableAdmin.UndeleteTable

type Union ¶
type Union struct {
	// Rules: Delete cells which would be deleted by any element of `rules`.
	Rules []*GcRule `json:"rules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Rules") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Rules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Union: A GcRule which deletes cells matching any of the given rules.

func (Union) MarshalJSON ¶
func (s Union) MarshalJSON() ([]byte, error)
type UpdateAppProfileMetadata ¶
type UpdateAppProfileMetadata struct {
}

UpdateAppProfileMetadata: The metadata for the Operation returned by UpdateAppProfile.

type UpdateAuthorizedViewMetadata ¶
added in v0.171.0
type UpdateAuthorizedViewMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// UpdateAuthorizedView operation.
	OriginalRequest *UpdateAuthorizedViewRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateAuthorizedViewMetadata: Metadata for the google.longrunning.Operation returned by UpdateAuthorizedView.

func (UpdateAuthorizedViewMetadata) MarshalJSON ¶
added in v0.171.0
func (s UpdateAuthorizedViewMetadata) MarshalJSON() ([]byte, error)
type UpdateAuthorizedViewRequest ¶
added in v0.171.0
type UpdateAuthorizedViewRequest struct {
	// AuthorizedView: Required. The AuthorizedView to update. The `name` in
	// `authorized_view` is used to identify the AuthorizedView. AuthorizedView
	// name must in this format:
	// `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{auth
	// orized_view}`.
	AuthorizedView *AuthorizedView `json:"authorizedView,omitempty"`
	// IgnoreWarnings: Optional. If true, ignore the safety checks when updating
	// the AuthorizedView.
	IgnoreWarnings bool `json:"ignoreWarnings,omitempty"`
	// UpdateMask: Optional. The list of fields to update. A mask specifying which
	// fields in the AuthorizedView resource should be updated. This mask is
	// relative to the AuthorizedView resource, not to the request message. A field
	// will be overwritten if it is in the mask. If empty, all fields set in the
	// request will be overwritten. A special value `*` means to overwrite all
	// fields (including fields not set in the request).
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuthorizedView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthorizedView") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateAuthorizedViewRequest: The request for UpdateAuthorizedView.

func (UpdateAuthorizedViewRequest) MarshalJSON ¶
added in v0.171.0
func (s UpdateAuthorizedViewRequest) MarshalJSON() ([]byte, error)
type UpdateClusterMetadata ¶
type UpdateClusterMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// UpdateCluster operation.
	OriginalRequest *Cluster `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateClusterMetadata: The metadata for the Operation returned by UpdateCluster.

func (UpdateClusterMetadata) MarshalJSON ¶
func (s UpdateClusterMetadata) MarshalJSON() ([]byte, error)
type UpdateInstanceMetadata ¶
type UpdateInstanceMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// UpdateInstance operation.
	OriginalRequest *PartialUpdateInstanceRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateInstanceMetadata: The metadata for the Operation returned by UpdateInstance.

func (UpdateInstanceMetadata) MarshalJSON ¶
func (s UpdateInstanceMetadata) MarshalJSON() ([]byte, error)
type UpdateLogicalViewMetadata ¶
added in v0.227.0
type UpdateLogicalViewMetadata struct {
	// EndTime: DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// OriginalRequest: The request that prompted the initiation of this
	// UpdateLogicalView operation.
	OriginalRequest *UpdateLogicalViewRequest `json:"originalRequest,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// StartTime: DEPRECATED: Use request_time instead.
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

UpdateLogicalViewMetadata: The metadata for the Operation returned by UpdateLogicalView.

func (UpdateLogicalViewMetadata) MarshalJSON ¶
added in v0.227.0
func (s UpdateLogicalViewMetadata) MarshalJSON() ([]byte, error)
type UpdateLogicalViewRequest ¶
added in v0.227.0
type UpdateLogicalViewRequest struct {
	// LogicalView: Required. The logical view to update. The logical view's `name`
	// field is used to identify the view to update. Format:
	// `projects/{project}/instances/{instance}/logicalViews/{logical_view}`.
	LogicalView *LogicalView `json:"logicalView,omitempty"`
	// UpdateMask: Optional. The list of fields to update.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LogicalView") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LogicalView") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateLogicalViewRequest: Request message for BigtableInstanceAdmin.UpdateLogicalView.

func (UpdateLogicalViewRequest) MarshalJSON ¶
added in v0.227.0
func (s UpdateLogicalViewRequest) MarshalJSON() ([]byte, error)
type UpdateSchemaBundleMetadata ¶
added in v0.240.0
type UpdateSchemaBundleMetadata struct {
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// Name: The unique name identifying this schema bundle. Values are of the form
	// `projects/{project}/instances/{instance}/tables/{table}/schemaBundles/{schema
	// _bundle}`
	Name string `json:"name,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinishTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinishTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateSchemaBundleMetadata: The metadata for the Operation returned by UpdateSchemaBundle.

func (UpdateSchemaBundleMetadata) MarshalJSON ¶
added in v0.240.0
func (s UpdateSchemaBundleMetadata) MarshalJSON() ([]byte, error)
type UpdateTableMetadata ¶
added in v0.103.0
type UpdateTableMetadata struct {
	// EndTime: If set, the time at which this operation finished or was canceled.
	// DEPRECATED: Use finish_time instead.
	EndTime string `json:"endTime,omitempty"`
	// FinishTime: The time at which the operation failed or was completed
	// successfully.
	FinishTime string `json:"finishTime,omitempty"`
	// Name: The name of the table being updated.
	Name string `json:"name,omitempty"`
	// RequestTime: The time at which the original request was received.
	RequestTime string `json:"requestTime,omitempty"`
	// StartTime: The time at which this operation started. DEPRECATED: Use
	// request_time instead.
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

UpdateTableMetadata: Metadata type for the operation returned by UpdateTable.

func (UpdateTableMetadata) MarshalJSON ¶
added in v0.103.0
func (s UpdateTableMetadata) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
bigtableadmin-gen.go
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
