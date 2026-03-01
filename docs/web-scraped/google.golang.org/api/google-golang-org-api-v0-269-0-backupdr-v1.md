# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/backupdr/v1

Title: backupdr package - google.golang.org/api/backupdr/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/backupdr/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
backupdr
 
v1
backupdr
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 1
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

Package backupdr provides access to the Backup and DR Service API.

For product documentation, see: https://cloud.google.com/backup-disaster-recovery

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/backupdr/v1"
...
ctx := context.Background()
backupdrService, err := backupdr.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

backupdrService, err := backupdr.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
backupdrService, err := backupdr.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AbandonBackupRequest
func (s AbandonBackupRequest) MarshalJSON() ([]byte, error)
type AcceleratorConfig
func (s AcceleratorConfig) MarshalJSON() ([]byte, error)
type AccessConfig
func (s AccessConfig) MarshalJSON() ([]byte, error)
type AdvancedMachineFeatures
func (s AdvancedMachineFeatures) MarshalJSON() ([]byte, error)
type AliasIpRange
func (s AliasIpRange) MarshalJSON() ([]byte, error)
type AllocationAffinity
func (s AllocationAffinity) MarshalJSON() ([]byte, error)
type AlloyDBClusterBackupPlanAssociationProperties
func (s AlloyDBClusterBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type AlloyDBClusterDataSourceProperties
func (s AlloyDBClusterDataSourceProperties) MarshalJSON() ([]byte, error)
type AlloyDBClusterDataSourceReferenceProperties
func (s AlloyDBClusterDataSourceReferenceProperties) MarshalJSON() ([]byte, error)
type AlloyDbClusterBackupProperties
func (s AlloyDbClusterBackupProperties) MarshalJSON() ([]byte, error)
type AlloyDbPitrWindow
func (s AlloyDbPitrWindow) MarshalJSON() ([]byte, error)
type AttachedDisk
func (s AttachedDisk) MarshalJSON() ([]byte, error)
type AuditConfig
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type Backup
func (s Backup) MarshalJSON() ([]byte, error)
type BackupApplianceBackupConfig
func (s BackupApplianceBackupConfig) MarshalJSON() ([]byte, error)
type BackupApplianceBackupProperties
func (s BackupApplianceBackupProperties) MarshalJSON() ([]byte, error)
type BackupApplianceLockInfo
func (s BackupApplianceLockInfo) MarshalJSON() ([]byte, error)
type BackupConfigDetails
func (s BackupConfigDetails) MarshalJSON() ([]byte, error)
type BackupConfigInfo
func (s BackupConfigInfo) MarshalJSON() ([]byte, error)
type BackupDrPlanConfig
func (s BackupDrPlanConfig) MarshalJSON() ([]byte, error)
type BackupDrPlanRule
func (s BackupDrPlanRule) MarshalJSON() ([]byte, error)
type BackupDrTemplateConfig
func (s BackupDrTemplateConfig) MarshalJSON() ([]byte, error)
type BackupGcpResource
func (s BackupGcpResource) MarshalJSON() ([]byte, error)
type BackupLocation
func (s BackupLocation) MarshalJSON() ([]byte, error)
type BackupLock
func (s BackupLock) MarshalJSON() ([]byte, error)
type BackupPlan
func (s BackupPlan) MarshalJSON() ([]byte, error)
type BackupPlanAssociation
func (s BackupPlanAssociation) MarshalJSON() ([]byte, error)
type BackupPlanRevision
func (s BackupPlanRevision) MarshalJSON() ([]byte, error)
type BackupRule
func (s BackupRule) MarshalJSON() ([]byte, error)
type BackupVault
func (s BackupVault) MarshalJSON() ([]byte, error)
type BackupWindow
func (s BackupWindow) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type CancelOperationRequest
type CloudSqlInstanceBackupPlanAssociationProperties
func (s CloudSqlInstanceBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceBackupProperties
func (s CloudSqlInstanceBackupProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceDataSourceProperties
func (s CloudSqlInstanceDataSourceProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceDataSourceReferenceProperties
func (s CloudSqlInstanceDataSourceReferenceProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceInitializationConfig
func (s CloudSqlInstanceInitializationConfig) MarshalJSON() ([]byte, error)
type ComputeInstanceBackupProperties
func (s ComputeInstanceBackupProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceDataSourceProperties
func (s ComputeInstanceDataSourceProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceRestoreProperties
func (s ComputeInstanceRestoreProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceTargetEnvironment
func (s ComputeInstanceTargetEnvironment) MarshalJSON() ([]byte, error)
type ConfidentialInstanceConfig
func (s ConfidentialInstanceConfig) MarshalJSON() ([]byte, error)
type CustomerEncryptionKey
func (s CustomerEncryptionKey) MarshalJSON() ([]byte, error)
type DataSource
func (s DataSource) MarshalJSON() ([]byte, error)
type DataSourceBackupApplianceApplication
func (s DataSourceBackupApplianceApplication) MarshalJSON() ([]byte, error)
type DataSourceBackupConfigInfo
func (s DataSourceBackupConfigInfo) MarshalJSON() ([]byte, error)
type DataSourceGcpResource
func (s DataSourceGcpResource) MarshalJSON() ([]byte, error)
type DataSourceGcpResourceInfo
func (s DataSourceGcpResourceInfo) MarshalJSON() ([]byte, error)
type DataSourceReference
func (s DataSourceReference) MarshalJSON() ([]byte, error)
type DiskBackupProperties
func (s DiskBackupProperties) MarshalJSON() ([]byte, error)
type DiskDataSourceProperties
func (s DiskDataSourceProperties) MarshalJSON() ([]byte, error)
type DiskRestoreProperties
func (s DiskRestoreProperties) MarshalJSON() ([]byte, error)
type DiskTargetEnvironment
func (s DiskTargetEnvironment) MarshalJSON() ([]byte, error)
type DisplayDevice
func (s DisplayDevice) MarshalJSON() ([]byte, error)
type Empty
type EncryptionConfig
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EndTrialRequest
func (s EndTrialRequest) MarshalJSON() ([]byte, error)
type Entry
func (s Entry) MarshalJSON() ([]byte, error)
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type FetchAccessTokenRequest
func (s FetchAccessTokenRequest) MarshalJSON() ([]byte, error)
type FetchAccessTokenResponse
func (s FetchAccessTokenResponse) MarshalJSON() ([]byte, error)
type FetchBackupPlanAssociationsForResourceTypeResponse
func (s FetchBackupPlanAssociationsForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchBackupsForResourceTypeResponse
func (s FetchBackupsForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchDataSourceReferencesForResourceTypeResponse
func (s FetchDataSourceReferencesForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchMsComplianceMetadataRequest
func (s FetchMsComplianceMetadataRequest) MarshalJSON() ([]byte, error)
type FetchMsComplianceMetadataResponse
func (s FetchMsComplianceMetadataResponse) MarshalJSON() ([]byte, error)
type FetchUsableBackupVaultsResponse
func (s FetchUsableBackupVaultsResponse) MarshalJSON() ([]byte, error)
type FilestoreInstanceBackupPlanAssociationProperties
func (s FilestoreInstanceBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type FinalizeBackupRequest
func (s FinalizeBackupRequest) MarshalJSON() ([]byte, error)
type GCPBackupPlanInfo
func (s GCPBackupPlanInfo) MarshalJSON() ([]byte, error)
type GcpBackupConfig
func (s GcpBackupConfig) MarshalJSON() ([]byte, error)
type GcpResource
func (s GcpResource) MarshalJSON() ([]byte, error)
type GuestOsFeature
func (s GuestOsFeature) MarshalJSON() ([]byte, error)
type InitializeParams
func (s InitializeParams) MarshalJSON() ([]byte, error)
type InitializeServiceRequest
func (s InitializeServiceRequest) MarshalJSON() ([]byte, error)
type InitiateBackupRequest
func (s InitiateBackupRequest) MarshalJSON() ([]byte, error)
type InitiateBackupResponse
func (s InitiateBackupResponse) MarshalJSON() ([]byte, error)
type InstanceParams
func (s InstanceParams) MarshalJSON() ([]byte, error)
type ListBackupPlanAssociationsResponse
func (s ListBackupPlanAssociationsResponse) MarshalJSON() ([]byte, error)
type ListBackupPlanRevisionsResponse
func (s ListBackupPlanRevisionsResponse) MarshalJSON() ([]byte, error)
type ListBackupPlansResponse
func (s ListBackupPlansResponse) MarshalJSON() ([]byte, error)
type ListBackupVaultsResponse
func (s ListBackupVaultsResponse) MarshalJSON() ([]byte, error)
type ListBackupsResponse
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListDataSourceReferencesResponse
func (s ListDataSourceReferencesResponse) MarshalJSON() ([]byte, error)
type ListDataSourcesResponse
func (s ListDataSourcesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListManagementServersResponse
func (s ListManagementServersResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListResourceBackupConfigsResponse
func (s ListResourceBackupConfigsResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type LocationMetadata
func (s LocationMetadata) MarshalJSON() ([]byte, error)
type ManagementServer
func (s ManagementServer) MarshalJSON() ([]byte, error)
type ManagementURI
func (s ManagementURI) MarshalJSON() ([]byte, error)
type Metadata
func (s Metadata) MarshalJSON() ([]byte, error)
type NetworkConfig
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type NetworkInterface
func (s NetworkInterface) MarshalJSON() ([]byte, error)
type NetworkPerformanceConfig
func (s NetworkPerformanceConfig) MarshalJSON() ([]byte, error)
type NodeAffinity
func (s NodeAffinity) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type PitrSettings
func (s PitrSettings) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ProjectsLocationsBackupPlanAssociationsCreateCall
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) BackupPlanAssociationId(backupPlanAssociationId string) *ProjectsLocationsBackupPlanAssociationsCreateCall
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsCreateCall
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsCreateCall
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsCreateCall
type ProjectsLocationsBackupPlanAssociationsDeleteCall
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsDeleteCall
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsDeleteCall
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsDeleteCall
type ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchBackupPlanAssociationsForResourceTypeResponse, error)
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Pages(ctx context.Context, ...) error
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
type ProjectsLocationsBackupPlanAssociationsGetCall
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsGetCall
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Do(opts ...googleapi.CallOption) (*BackupPlanAssociation, error)
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsGetCall
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsGetCall
type ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlanAssociationsResponse, error)
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Filter(filter string) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlanAssociationsListCall
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Pages(ctx context.Context, f func(*ListBackupPlanAssociationsResponse) error) error
type ProjectsLocationsBackupPlanAssociationsPatchCall
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsPatchCall
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsPatchCall
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsPatchCall
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupPlanAssociationsPatchCall
type ProjectsLocationsBackupPlanAssociationsService
func NewProjectsLocationsBackupPlanAssociationsService(s *Service) *ProjectsLocationsBackupPlanAssociationsService
func (r *ProjectsLocationsBackupPlanAssociationsService) Create(parent string, backupplanassociation *BackupPlanAssociation) *ProjectsLocationsBackupPlanAssociationsCreateCall
func (r *ProjectsLocationsBackupPlanAssociationsService) Delete(name string) *ProjectsLocationsBackupPlanAssociationsDeleteCall
func (r *ProjectsLocationsBackupPlanAssociationsService) FetchForResourceType(parent string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall
func (r *ProjectsLocationsBackupPlanAssociationsService) Get(name string) *ProjectsLocationsBackupPlanAssociationsGetCall
func (r *ProjectsLocationsBackupPlanAssociationsService) List(parent string) *ProjectsLocationsBackupPlanAssociationsListCall
func (r *ProjectsLocationsBackupPlanAssociationsService) Patch(name string, backupplanassociation *BackupPlanAssociation) *ProjectsLocationsBackupPlanAssociationsPatchCall
func (r *ProjectsLocationsBackupPlanAssociationsService) TriggerBackup(name string, triggerbackuprequest *TriggerBackupRequest) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall
type ProjectsLocationsBackupPlanAssociationsTriggerBackupCall
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Header() http.Header
type ProjectsLocationsBackupPlansCreateCall
func (c *ProjectsLocationsBackupPlansCreateCall) BackupPlanId(backupPlanId string) *ProjectsLocationsBackupPlansCreateCall
func (c *ProjectsLocationsBackupPlansCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansCreateCall
func (c *ProjectsLocationsBackupPlansCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlansCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansCreateCall
func (c *ProjectsLocationsBackupPlansCreateCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansCreateCall) RequestId(requestId string) *ProjectsLocationsBackupPlansCreateCall
type ProjectsLocationsBackupPlansDeleteCall
func (c *ProjectsLocationsBackupPlansDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansDeleteCall
func (c *ProjectsLocationsBackupPlansDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlansDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansDeleteCall
func (c *ProjectsLocationsBackupPlansDeleteCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupPlansDeleteCall
type ProjectsLocationsBackupPlansGetCall
func (c *ProjectsLocationsBackupPlansGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansGetCall
func (c *ProjectsLocationsBackupPlansGetCall) Do(opts ...googleapi.CallOption) (*BackupPlan, error)
func (c *ProjectsLocationsBackupPlansGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansGetCall
func (c *ProjectsLocationsBackupPlansGetCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansGetCall
type ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlansResponse, error)
func (c *ProjectsLocationsBackupPlansListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) Filter(filter string) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) OrderBy(orderBy string) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlansListCall
func (c *ProjectsLocationsBackupPlansListCall) Pages(ctx context.Context, f func(*ListBackupPlansResponse) error) error
type ProjectsLocationsBackupPlansPatchCall
func (c *ProjectsLocationsBackupPlansPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansPatchCall
func (c *ProjectsLocationsBackupPlansPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupPlansPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansPatchCall
func (c *ProjectsLocationsBackupPlansPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansPatchCall) RequestId(requestId string) *ProjectsLocationsBackupPlansPatchCall
func (c *ProjectsLocationsBackupPlansPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupPlansPatchCall
type ProjectsLocationsBackupPlansRevisionsGetCall
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansRevisionsGetCall
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Do(opts ...googleapi.CallOption) (*BackupPlanRevision, error)
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansRevisionsGetCall
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansRevisionsGetCall
type ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlanRevisionsResponse, error)
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Header() http.Header
func (c *ProjectsLocationsBackupPlansRevisionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlansRevisionsListCall
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Pages(ctx context.Context, f func(*ListBackupPlanRevisionsResponse) error) error
type ProjectsLocationsBackupPlansRevisionsService
func NewProjectsLocationsBackupPlansRevisionsService(s *Service) *ProjectsLocationsBackupPlansRevisionsService
func (r *ProjectsLocationsBackupPlansRevisionsService) Get(name string) *ProjectsLocationsBackupPlansRevisionsGetCall
func (r *ProjectsLocationsBackupPlansRevisionsService) List(parent string) *ProjectsLocationsBackupPlansRevisionsListCall
type ProjectsLocationsBackupPlansService
func NewProjectsLocationsBackupPlansService(s *Service) *ProjectsLocationsBackupPlansService
func (r *ProjectsLocationsBackupPlansService) Create(parent string, backupplan *BackupPlan) *ProjectsLocationsBackupPlansCreateCall
func (r *ProjectsLocationsBackupPlansService) Delete(name string) *ProjectsLocationsBackupPlansDeleteCall
func (r *ProjectsLocationsBackupPlansService) Get(name string) *ProjectsLocationsBackupPlansGetCall
func (r *ProjectsLocationsBackupPlansService) List(parent string) *ProjectsLocationsBackupPlansListCall
func (r *ProjectsLocationsBackupPlansService) Patch(name string, backupplan *BackupPlan) *ProjectsLocationsBackupPlansPatchCall
type ProjectsLocationsBackupVaultsCreateCall
func (c *ProjectsLocationsBackupVaultsCreateCall) BackupVaultId(backupVaultId string) *ProjectsLocationsBackupVaultsCreateCall
func (c *ProjectsLocationsBackupVaultsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsCreateCall
func (c *ProjectsLocationsBackupVaultsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsCreateCall
func (c *ProjectsLocationsBackupVaultsCreateCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsCreateCall
func (c *ProjectsLocationsBackupVaultsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsCreateCall
type ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall
type ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchBackupsForResourceTypeResponse, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Pages(ctx context.Context, f func(*FetchBackupsForResourceTypeResponse) error) error
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
type ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
type ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
type ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
type ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesBackupsService
func NewProjectsLocationsBackupVaultsDataSourcesBackupsService(s *Service) *ProjectsLocationsBackupVaultsDataSourcesBackupsService
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Delete(name string) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) FetchForResourceType(parent string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Get(name string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) List(parent string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Patch(name string, backup *Backup) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Restore(name string, restorebackuprequest *RestoreBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall
type ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Do(opts ...googleapi.CallOption) (*FetchAccessTokenResponse, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Do(opts ...googleapi.CallOption) (*DataSource, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesGetCall
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesGetCall
type ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Do(opts ...googleapi.CallOption) (*InitiateBackupResponse, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourcesResponse, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Pages(ctx context.Context, f func(*ListDataSourcesResponse) error) error
type ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
type ProjectsLocationsBackupVaultsDataSourcesRemoveCall
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Header() http.Header
type ProjectsLocationsBackupVaultsDataSourcesService
func NewProjectsLocationsBackupVaultsDataSourcesService(s *Service) *ProjectsLocationsBackupVaultsDataSourcesService
func (r *ProjectsLocationsBackupVaultsDataSourcesService) AbandonBackup(dataSource string, abandonbackuprequest *AbandonBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) FetchAccessToken(name string, fetchaccesstokenrequest *FetchAccessTokenRequest) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) FinalizeBackup(dataSource string, finalizebackuprequest *FinalizeBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Get(name string) *ProjectsLocationsBackupVaultsDataSourcesGetCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) InitiateBackup(dataSource string, initiatebackuprequest *InitiateBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) List(parent string) *ProjectsLocationsBackupVaultsDataSourcesListCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Patch(name string, datasource *DataSource) *ProjectsLocationsBackupVaultsDataSourcesPatchCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Remove(name string, removedatasourcerequest *RemoveDataSourceRequest) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall
func (r *ProjectsLocationsBackupVaultsDataSourcesService) SetInternalStatus(dataSource string, setinternalstatusrequest *SetInternalStatusRequest) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall
type ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Header() http.Header
type ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsDeleteCall) Etag(etag string) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) Force(force bool) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsDeleteCall) IgnoreBackupPlanReferences(ignoreBackupPlanReferences bool) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDeleteCall
func (c *ProjectsLocationsBackupVaultsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsDeleteCall
type ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Do(opts ...googleapi.CallOption) (*FetchUsableBackupVaultsResponse, error)
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Filter(filter string) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsFetchUsableCall
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Pages(ctx context.Context, f func(*FetchUsableBackupVaultsResponse) error) error
type ProjectsLocationsBackupVaultsGetCall
func (c *ProjectsLocationsBackupVaultsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsGetCall
func (c *ProjectsLocationsBackupVaultsGetCall) Do(opts ...googleapi.CallOption) (*BackupVault, error)
func (c *ProjectsLocationsBackupVaultsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsGetCall
func (c *ProjectsLocationsBackupVaultsGetCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsGetCall
func (c *ProjectsLocationsBackupVaultsGetCall) View(view string) *ProjectsLocationsBackupVaultsGetCall
type ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) Do(opts ...googleapi.CallOption) (*ListBackupVaultsResponse, error)
func (c *ProjectsLocationsBackupVaultsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) Filter(filter string) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsListCall
func (c *ProjectsLocationsBackupVaultsListCall) Pages(ctx context.Context, f func(*ListBackupVaultsResponse) error) error
func (c *ProjectsLocationsBackupVaultsListCall) View(view string) *ProjectsLocationsBackupVaultsListCall
type ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupVaultsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) Force(force bool) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) ForceUpdateAccessRestriction(forceUpdateAccessRestriction bool) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupVaultsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsPatchCall
func (c *ProjectsLocationsBackupVaultsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsPatchCall
type ProjectsLocationsBackupVaultsService
func NewProjectsLocationsBackupVaultsService(s *Service) *ProjectsLocationsBackupVaultsService
func (r *ProjectsLocationsBackupVaultsService) Create(parent string, backupvault *BackupVault) *ProjectsLocationsBackupVaultsCreateCall
func (r *ProjectsLocationsBackupVaultsService) Delete(name string) *ProjectsLocationsBackupVaultsDeleteCall
func (r *ProjectsLocationsBackupVaultsService) FetchUsable(parent string) *ProjectsLocationsBackupVaultsFetchUsableCall
func (r *ProjectsLocationsBackupVaultsService) Get(name string) *ProjectsLocationsBackupVaultsGetCall
func (r *ProjectsLocationsBackupVaultsService) List(parent string) *ProjectsLocationsBackupVaultsListCall
func (r *ProjectsLocationsBackupVaultsService) Patch(name string, backupvault *BackupVault) *ProjectsLocationsBackupVaultsPatchCall
func (r *ProjectsLocationsBackupVaultsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsBackupVaultsTestIamPermissionsCall
type ProjectsLocationsBackupVaultsTestIamPermissionsCall
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsTestIamPermissionsCall
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsTestIamPermissionsCall
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchDataSourceReferencesForResourceTypeResponse, error)
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Header() http.Header
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Pages(ctx context.Context, ...) error
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
type ProjectsLocationsDataSourceReferencesGetCall
func (c *ProjectsLocationsDataSourceReferencesGetCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesGetCall
func (c *ProjectsLocationsDataSourceReferencesGetCall) Do(opts ...googleapi.CallOption) (*DataSourceReference, error)
func (c *ProjectsLocationsDataSourceReferencesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesGetCall
func (c *ProjectsLocationsDataSourceReferencesGetCall) Header() http.Header
func (c *ProjectsLocationsDataSourceReferencesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesGetCall
type ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourceReferencesResponse, error)
func (c *ProjectsLocationsDataSourceReferencesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) Filter(filter string) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) Header() http.Header
func (c *ProjectsLocationsDataSourceReferencesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) OrderBy(orderBy string) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) PageSize(pageSize int64) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) PageToken(pageToken string) *ProjectsLocationsDataSourceReferencesListCall
func (c *ProjectsLocationsDataSourceReferencesListCall) Pages(ctx context.Context, f func(*ListDataSourceReferencesResponse) error) error
type ProjectsLocationsDataSourceReferencesService
func NewProjectsLocationsDataSourceReferencesService(s *Service) *ProjectsLocationsDataSourceReferencesService
func (r *ProjectsLocationsDataSourceReferencesService) FetchForResourceType(parent string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall
func (r *ProjectsLocationsDataSourceReferencesService) Get(name string) *ProjectsLocationsDataSourceReferencesGetCall
func (r *ProjectsLocationsDataSourceReferencesService) List(parent string) *ProjectsLocationsDataSourceReferencesListCall
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsGetTrialCall
func (c *ProjectsLocationsGetTrialCall) Context(ctx context.Context) *ProjectsLocationsGetTrialCall
func (c *ProjectsLocationsGetTrialCall) Do(opts ...googleapi.CallOption) (*Trial, error)
func (c *ProjectsLocationsGetTrialCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetTrialCall
func (c *ProjectsLocationsGetTrialCall) Header() http.Header
func (c *ProjectsLocationsGetTrialCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetTrialCall
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
type ProjectsLocationsManagementServersCreateCall
func (c *ProjectsLocationsManagementServersCreateCall) Context(ctx context.Context) *ProjectsLocationsManagementServersCreateCall
func (c *ProjectsLocationsManagementServersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsManagementServersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersCreateCall
func (c *ProjectsLocationsManagementServersCreateCall) Header() http.Header
func (c *ProjectsLocationsManagementServersCreateCall) ManagementServerId(managementServerId string) *ProjectsLocationsManagementServersCreateCall
func (c *ProjectsLocationsManagementServersCreateCall) RequestId(requestId string) *ProjectsLocationsManagementServersCreateCall
type ProjectsLocationsManagementServersDeleteCall
func (c *ProjectsLocationsManagementServersDeleteCall) Context(ctx context.Context) *ProjectsLocationsManagementServersDeleteCall
func (c *ProjectsLocationsManagementServersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsManagementServersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersDeleteCall
func (c *ProjectsLocationsManagementServersDeleteCall) Header() http.Header
func (c *ProjectsLocationsManagementServersDeleteCall) RequestId(requestId string) *ProjectsLocationsManagementServersDeleteCall
type ProjectsLocationsManagementServersGetCall
func (c *ProjectsLocationsManagementServersGetCall) Context(ctx context.Context) *ProjectsLocationsManagementServersGetCall
func (c *ProjectsLocationsManagementServersGetCall) Do(opts ...googleapi.CallOption) (*ManagementServer, error)
func (c *ProjectsLocationsManagementServersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersGetCall
func (c *ProjectsLocationsManagementServersGetCall) Header() http.Header
func (c *ProjectsLocationsManagementServersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersGetCall
type ProjectsLocationsManagementServersGetIamPolicyCall
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsManagementServersGetIamPolicyCall
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersGetIamPolicyCall
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersGetIamPolicyCall
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsManagementServersGetIamPolicyCall
type ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) Context(ctx context.Context) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) Do(opts ...googleapi.CallOption) (*ListManagementServersResponse, error)
func (c *ProjectsLocationsManagementServersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) Filter(filter string) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) Header() http.Header
func (c *ProjectsLocationsManagementServersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) OrderBy(orderBy string) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) PageSize(pageSize int64) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) PageToken(pageToken string) *ProjectsLocationsManagementServersListCall
func (c *ProjectsLocationsManagementServersListCall) Pages(ctx context.Context, f func(*ListManagementServersResponse) error) error
type ProjectsLocationsManagementServersMsComplianceMetadataCall
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Context(ctx context.Context) *ProjectsLocationsManagementServersMsComplianceMetadataCall
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Do(opts ...googleapi.CallOption) (*FetchMsComplianceMetadataResponse, error)
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersMsComplianceMetadataCall
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Header() http.Header
type ProjectsLocationsManagementServersService
func NewProjectsLocationsManagementServersService(s *Service) *ProjectsLocationsManagementServersService
func (r *ProjectsLocationsManagementServersService) Create(parent string, managementserver *ManagementServer) *ProjectsLocationsManagementServersCreateCall
func (r *ProjectsLocationsManagementServersService) Delete(name string) *ProjectsLocationsManagementServersDeleteCall
func (r *ProjectsLocationsManagementServersService) Get(name string) *ProjectsLocationsManagementServersGetCall
func (r *ProjectsLocationsManagementServersService) GetIamPolicy(resource string) *ProjectsLocationsManagementServersGetIamPolicyCall
func (r *ProjectsLocationsManagementServersService) List(parent string) *ProjectsLocationsManagementServersListCall
func (r *ProjectsLocationsManagementServersService) MsComplianceMetadata(parent string, ...) *ProjectsLocationsManagementServersMsComplianceMetadataCall
func (r *ProjectsLocationsManagementServersService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsManagementServersSetIamPolicyCall
func (r *ProjectsLocationsManagementServersService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsManagementServersTestIamPermissionsCall
type ProjectsLocationsManagementServersSetIamPolicyCall
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsManagementServersSetIamPolicyCall
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersSetIamPolicyCall
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Header() http.Header
type ProjectsLocationsManagementServersTestIamPermissionsCall
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsManagementServersTestIamPermissionsCall
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersTestIamPermissionsCall
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Header() http.Header
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
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Header() http.Header
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall
type ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) Context(ctx context.Context) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) Do(opts ...googleapi.CallOption) (*ListResourceBackupConfigsResponse, error)
func (c *ProjectsLocationsResourceBackupConfigsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) Filter(filter string) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) Header() http.Header
func (c *ProjectsLocationsResourceBackupConfigsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) OrderBy(orderBy string) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) PageSize(pageSize int64) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) PageToken(pageToken string) *ProjectsLocationsResourceBackupConfigsListCall
func (c *ProjectsLocationsResourceBackupConfigsListCall) Pages(ctx context.Context, f func(*ListResourceBackupConfigsResponse) error) error
type ProjectsLocationsResourceBackupConfigsService
func NewProjectsLocationsResourceBackupConfigsService(s *Service) *ProjectsLocationsResourceBackupConfigsService
func (r *ProjectsLocationsResourceBackupConfigsService) List(parent string) *ProjectsLocationsResourceBackupConfigsListCall
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) GetTrial(name string) *ProjectsLocationsGetTrialCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsLocationsServiceConfigInitializeCall
func (c *ProjectsLocationsServiceConfigInitializeCall) Context(ctx context.Context) *ProjectsLocationsServiceConfigInitializeCall
func (c *ProjectsLocationsServiceConfigInitializeCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsServiceConfigInitializeCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceConfigInitializeCall
func (c *ProjectsLocationsServiceConfigInitializeCall) Header() http.Header
type ProjectsLocationsServiceConfigService
func NewProjectsLocationsServiceConfigService(s *Service) *ProjectsLocationsServiceConfigService
func (r *ProjectsLocationsServiceConfigService) Initialize(name string, initializeservicerequest *InitializeServiceRequest) *ProjectsLocationsServiceConfigInitializeCall
type ProjectsLocationsTrialEndCall
func (c *ProjectsLocationsTrialEndCall) Context(ctx context.Context) *ProjectsLocationsTrialEndCall
func (c *ProjectsLocationsTrialEndCall) Do(opts ...googleapi.CallOption) (*Trial, error)
func (c *ProjectsLocationsTrialEndCall) Fields(s ...googleapi.Field) *ProjectsLocationsTrialEndCall
func (c *ProjectsLocationsTrialEndCall) Header() http.Header
type ProjectsLocationsTrialService
func NewProjectsLocationsTrialService(s *Service) *ProjectsLocationsTrialService
func (r *ProjectsLocationsTrialService) End(parent string, endtrialrequest *EndTrialRequest) *ProjectsLocationsTrialEndCall
func (r *ProjectsLocationsTrialService) Subscribe(parent string, subscribetrialrequest *SubscribeTrialRequest) *ProjectsLocationsTrialSubscribeCall
type ProjectsLocationsTrialSubscribeCall
func (c *ProjectsLocationsTrialSubscribeCall) Context(ctx context.Context) *ProjectsLocationsTrialSubscribeCall
func (c *ProjectsLocationsTrialSubscribeCall) Do(opts ...googleapi.CallOption) (*Trial, error)
func (c *ProjectsLocationsTrialSubscribeCall) Fields(s ...googleapi.Field) *ProjectsLocationsTrialSubscribeCall
func (c *ProjectsLocationsTrialSubscribeCall) Header() http.Header
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type RegionDiskTargetEnvironment
func (s RegionDiskTargetEnvironment) MarshalJSON() ([]byte, error)
type RemoveDataSourceRequest
func (s RemoveDataSourceRequest) MarshalJSON() ([]byte, error)
type ResourceBackupConfig
func (s ResourceBackupConfig) MarshalJSON() ([]byte, error)
type RestoreBackupRequest
func (s RestoreBackupRequest) MarshalJSON() ([]byte, error)
type RestoreBackupResponse
func (s RestoreBackupResponse) MarshalJSON() ([]byte, error)
type RuleConfigInfo
func (s RuleConfigInfo) MarshalJSON() ([]byte, error)
type Scheduling
func (s Scheduling) MarshalJSON() ([]byte, error)
type SchedulingDuration
func (s SchedulingDuration) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type ServiceAccount
func (s ServiceAccount) MarshalJSON() ([]byte, error)
type ServiceLockInfo
func (s ServiceLockInfo) MarshalJSON() ([]byte, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type SetInternalStatusRequest
func (s SetInternalStatusRequest) MarshalJSON() ([]byte, error)
type SetInternalStatusResponse
type StandardSchedule
func (s StandardSchedule) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type SubscribeTrialRequest
type Tags
func (s Tags) MarshalJSON() ([]byte, error)
type TargetResource
func (s TargetResource) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type Trial
func (s Trial) MarshalJSON() ([]byte, error)
type TriggerBackupRequest
func (s TriggerBackupRequest) MarshalJSON() ([]byte, error)
type WeekDayOfMonth
func (s WeekDayOfMonth) MarshalJSON() ([]byte, error)
type WorkforceIdentityBasedManagementURI
func (s WorkforceIdentityBasedManagementURI) MarshalJSON() ([]byte, error)
type WorkforceIdentityBasedOAuth2ClientID
func (s WorkforceIdentityBasedOAuth2ClientID) MarshalJSON() ([]byte, error)
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
type AbandonBackupRequest ¶
added in v0.188.0
type AbandonBackupRequest struct {
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

AbandonBackupRequest: request message for AbandonBackup.

func (AbandonBackupRequest) MarshalJSON ¶
added in v0.188.0
func (s AbandonBackupRequest) MarshalJSON() ([]byte, error)
type AcceleratorConfig ¶
added in v0.188.0
type AcceleratorConfig struct {
	// AcceleratorCount: Optional. The number of the guest accelerator cards
	// exposed to this instance.
	AcceleratorCount int64 `json:"acceleratorCount,omitempty"`
	// AcceleratorType: Optional. Full or partial URL of the accelerator type
	// resource to attach to this instance.
	AcceleratorType string `json:"acceleratorType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AcceleratorCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcceleratorCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AcceleratorConfig: A specification of the type and number of accelerator cards attached to the instance.

func (AcceleratorConfig) MarshalJSON ¶
added in v0.188.0
func (s AcceleratorConfig) MarshalJSON() ([]byte, error)
type AccessConfig ¶
added in v0.188.0
type AccessConfig struct {
	// ExternalIpv6: Optional. The external IPv6 address of this access
	// configuration.
	ExternalIpv6 string `json:"externalIpv6,omitempty"`
	// ExternalIpv6PrefixLength: Optional. The prefix length of the external IPv6
	// range.
	ExternalIpv6PrefixLength int64 `json:"externalIpv6PrefixLength,omitempty"`
	// Name: Optional. The name of this access configuration.
	Name string `json:"name,omitempty"`
	// NatIP: Optional. The external IP address of this access configuration.
	NatIP string `json:"natIP,omitempty"`
	// NetworkTier: Optional. This signifies the networking tier used for
	// configuring this access
	//
	// Possible values:
	//   "NETWORK_TIER_UNSPECIFIED" - Default value. This value is unused.
	//   "PREMIUM" - High quality, Google-grade network tier, support for all
	// networking products.
	//   "STANDARD" - Public internet quality, only limited support for other
	// networking products.
	NetworkTier string `json:"networkTier,omitempty"`
	// PublicPtrDomainName: Optional. The DNS domain name for the public PTR
	// record.
	PublicPtrDomainName string `json:"publicPtrDomainName,omitempty"`
	// SetPublicPtr: Optional. Specifies whether a public DNS 'PTR' record should
	// be created to map the external IP address of the instance to a DNS domain
	// name.
	SetPublicPtr bool `json:"setPublicPtr,omitempty"`
	// Type: Optional. In accessConfigs (IPv4), the default and only option is
	// ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is
	// DIRECT_IPV6.
	//
	// Possible values:
	//   "ACCESS_TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "ONE_TO_ONE_NAT" - ONE_TO_ONE_NAT
	//   "DIRECT_IPV6" - Direct IPv6 access.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalIpv6") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalIpv6") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessConfig: An access configuration attached to an instance's network interface. Only one access config per instance is supported.

func (AccessConfig) MarshalJSON ¶
added in v0.188.0
func (s AccessConfig) MarshalJSON() ([]byte, error)
type AdvancedMachineFeatures ¶
added in v0.192.0
type AdvancedMachineFeatures struct {
	// EnableNestedVirtualization: Optional. Whether to enable nested
	// virtualization or not (default is false).
	EnableNestedVirtualization bool `json:"enableNestedVirtualization,omitempty"`
	// EnableUefiNetworking: Optional. Whether to enable UEFI networking for
	// instance creation.
	EnableUefiNetworking bool `json:"enableUefiNetworking,omitempty"`
	// ThreadsPerCore: Optional. The number of threads per physical core. To
	// disable simultaneous multithreading (SMT) set this to 1. If unset, the
	// maximum number of threads supported per core by the underlying processor is
	// assumed.
	ThreadsPerCore int64 `json:"threadsPerCore,omitempty"`
	// VisibleCoreCount: Optional. The number of physical cores to expose to an
	// instance. Multiply by the number of threads per core to compute the total
	// number of virtual CPUs to expose to the instance. If unset, the number of
	// cores is inferred from the instance's nominal CPU count and the underlying
	// platform's SMT width.
	VisibleCoreCount int64 `json:"visibleCoreCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnableNestedVirtualization")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnableNestedVirtualization") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdvancedMachineFeatures: Specifies options for controlling advanced machine features.

func (AdvancedMachineFeatures) MarshalJSON ¶
added in v0.192.0
func (s AdvancedMachineFeatures) MarshalJSON() ([]byte, error)
type AliasIpRange ¶
added in v0.188.0
type AliasIpRange struct {
	// IpCidrRange: Optional. The IP alias ranges to allocate for this interface.
	IpCidrRange string `json:"ipCidrRange,omitempty"`
	// SubnetworkRangeName: Optional. The name of a subnetwork secondary IP range
	// from which to allocate an IP alias range. If not specified, the primary
	// range of the subnetwork is used.
	SubnetworkRangeName string `json:"subnetworkRangeName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IpCidrRange") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IpCidrRange") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AliasIpRange: An alias IP range attached to an instance's network interface.

func (AliasIpRange) MarshalJSON ¶
added in v0.188.0
func (s AliasIpRange) MarshalJSON() ([]byte, error)
type AllocationAffinity ¶
added in v0.192.0
type AllocationAffinity struct {
	// ConsumeReservationType: Optional. Specifies the type of reservation from
	// which this instance can consume
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "NO_RESERVATION" - Do not consume from any allocated capacity.
	//   "ANY_RESERVATION" - Consume any allocation available.
	//   "SPECIFIC_RESERVATION" - Must consume from a specific reservation. Must
	// specify key value fields for specifying the reservations.
	ConsumeReservationType string `json:"consumeReservationType,omitempty"`
	// Key: Optional. Corresponds to the label key of a reservation resource.
	Key string `json:"key,omitempty"`
	// Values: Optional. Corresponds to the label values of a reservation resource.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConsumeReservationType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsumeReservationType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AllocationAffinity: Specifies the reservations that this instance can consume from.

func (AllocationAffinity) MarshalJSON ¶
added in v0.192.0
func (s AllocationAffinity) MarshalJSON() ([]byte, error)
type AlloyDBClusterBackupPlanAssociationProperties ¶
added in v0.260.0
type AlloyDBClusterBackupPlanAssociationProperties struct {
	// ClusterUid: Output only. The cluster UID of the AlloyDB cluster.
	ClusterUid string `json:"clusterUid,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterUid") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterUid") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AlloyDBClusterBackupPlanAssociationProperties: Properties for an AlloyDB cluster backup plan association.

func (AlloyDBClusterBackupPlanAssociationProperties) MarshalJSON ¶
added in v0.262.0
func (s AlloyDBClusterBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type AlloyDBClusterDataSourceProperties ¶
added in v0.251.0
type AlloyDBClusterDataSourceProperties struct {
	// ClusterUid: Output only. The cluster UID of the AlloyDB cluster backed up by
	// the datasource.
	ClusterUid string `json:"clusterUid,omitempty"`
	// Name: Output only. Name of the AlloyDB cluster backed up by the datasource.
	Name string `json:"name,omitempty"`
	// PitrWindows: Output only. Point in time recovery windows. The order is
	// guaranteed to be ascending by start time.
	PitrWindows []*AlloyDbPitrWindow `json:"pitrWindows,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterUid") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterUid") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AlloyDBClusterDataSourceProperties: AlloyDBClusterDataSourceProperties represents the properties of a AlloyDB cluster resource that are stored in the DataSource. .

func (AlloyDBClusterDataSourceProperties) MarshalJSON ¶
added in v0.251.0
func (s AlloyDBClusterDataSourceProperties) MarshalJSON() ([]byte, error)
type AlloyDBClusterDataSourceReferenceProperties ¶
added in v0.262.0
type AlloyDBClusterDataSourceReferenceProperties struct {
	// Name: Output only. Name of the AlloyDB cluster backed up by the datasource.
	// Format: projects/{project}/locations/{location}/clusters/{cluster}
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

AlloyDBClusterDataSourceReferenceProperties: AlloyDBClusterDataSourceReferenceProperties represents the properties of an AlloyDB cluster that are stored in the DataSourceReference.

func (AlloyDBClusterDataSourceReferenceProperties) MarshalJSON ¶
added in v0.262.0
func (s AlloyDBClusterDataSourceReferenceProperties) MarshalJSON() ([]byte, error)
type AlloyDbClusterBackupProperties ¶
added in v0.251.0
type AlloyDbClusterBackupProperties struct {
	// ChainId: Output only. The chain id of this backup. Backups belonging to the
	// same chain are sharing the same chain id. This property is calculated and
	// maintained by BackupDR.
	ChainId string `json:"chainId,omitempty"`
	// DatabaseVersion: Output only. The PostgreSQL major version of the AlloyDB
	// cluster when the backup was taken.
	DatabaseVersion string `json:"databaseVersion,omitempty"`
	// Description: An optional text description for the backup.
	Description string `json:"description,omitempty"`
	// StoredBytes: Output only. Storage usage of this particular backup
	StoredBytes int64 `json:"storedBytes,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "ChainId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChainId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AlloyDbClusterBackupProperties: AlloyDbClusterBackupProperties represents AlloyDB cluster backup properties. .

func (AlloyDbClusterBackupProperties) MarshalJSON ¶
added in v0.251.0
func (s AlloyDbClusterBackupProperties) MarshalJSON() ([]byte, error)
type AlloyDbPitrWindow ¶
added in v0.262.0
type AlloyDbPitrWindow struct {
	// EndTime: Output only. The end time of the PITR window. It is not set if the
	// corresponding Backup Plan Association is active.
	EndTime string `json:"endTime,omitempty"`
	// LogRetentionDays: Output only. Log retention days for the PITR window.
	LogRetentionDays int64 `json:"logRetentionDays,omitempty,string"`
	// StartTime: Output only. The start time of the PITR window.
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

AlloyDbPitrWindow: Point in time recovery window for an AlloyDB cluster.

func (AlloyDbPitrWindow) MarshalJSON ¶
added in v0.262.0
func (s AlloyDbPitrWindow) MarshalJSON() ([]byte, error)
type AttachedDisk ¶
added in v0.188.0
type AttachedDisk struct {
	// AutoDelete: Optional. Specifies whether the disk will be auto-deleted when
	// the instance is deleted (but not when the disk is detached from the
	// instance).
	AutoDelete bool `json:"autoDelete,omitempty"`
	// Boot: Optional. Indicates that this is a boot disk. The virtual machine will
	// use the first partition of the disk for its root filesystem.
	Boot bool `json:"boot,omitempty"`
	// DeviceName: Optional. This is used as an identifier for the disks. This is
	// the unique name has to provided to modify disk parameters like disk_name and
	// replica_zones (in case of RePDs)
	DeviceName string `json:"deviceName,omitempty"`
	// DiskEncryptionKey: Optional. Encrypts or decrypts a disk using a
	// customer-supplied encryption key.
	DiskEncryptionKey *CustomerEncryptionKey `json:"diskEncryptionKey,omitempty"`
	// DiskInterface: Optional. Specifies the disk interface to use for attaching
	// this disk.
	//
	// Possible values:
	//   "DISK_INTERFACE_UNSPECIFIED" - Default value, which is unused.
	//   "SCSI" - SCSI Disk Interface.
	//   "NVME" - NVME Disk Interface.
	//   "NVDIMM" - NVDIMM Disk Interface.
	//   "ISCSI" - ISCSI Disk Interface.
	DiskInterface string `json:"diskInterface,omitempty"`
	// DiskSizeGb: Optional. The size of the disk in GB.
	DiskSizeGb int64 `json:"diskSizeGb,omitempty,string"`
	// DiskType: Optional. Output only. The URI of the disk type resource. For
	// example: projects/project/zones/zone/diskTypes/pd-standard or pd-ssd
	DiskType string `json:"diskType,omitempty"`
	// DiskTypeDeprecated: Specifies the type of the disk.
	//
	// Possible values:
	//   "DISK_TYPE_UNSPECIFIED" - Default value, which is unused.
	//   "SCRATCH" - A scratch disk type.
	//   "PERSISTENT" - A persistent disk type.
	DiskTypeDeprecated string `json:"diskTypeDeprecated,omitempty"`
	// GuestOsFeature: Optional. A list of features to enable on the guest
	// operating system. Applicable only for bootable images.
	GuestOsFeature []*GuestOsFeature `json:"guestOsFeature,omitempty"`
	// Index: Optional. A zero-based index to this disk, where 0 is reserved for
	// the boot disk.
	Index int64 `json:"index,omitempty,string"`
	// InitializeParams: Optional. Specifies the parameters to initialize this
	// disk.
	InitializeParams *InitializeParams `json:"initializeParams,omitempty"`
	// Kind: Optional. Type of the resource.
	Kind string `json:"kind,omitempty"`
	// License: Optional. Any valid publicly visible licenses.
	License []string `json:"license,omitempty"`
	// Mode: Optional. The mode in which to attach this disk.
	//
	// Possible values:
	//   "DISK_MODE_UNSPECIFIED" - Default value, which is unused.
	//   "READ_WRITE" - Attaches this disk in read-write mode. Only one virtual
	// machine at a time can be attached to a disk in read-write mode.
	//   "READ_ONLY" - Attaches this disk in read-only mode. Multiple virtual
	// machines can use a disk in read-only mode at a time.
	//   "LOCKED" - The disk is locked for administrative reasons. Nobody else can
	// use the disk. This mode is used (for example) when taking a snapshot of a
	// disk to prevent mounting the disk while it is being snapshotted.
	Mode string `json:"mode,omitempty"`
	// SavedState: Optional. Output only. The state of the disk.
	//
	// Possible values:
	//   "DISK_SAVED_STATE_UNSPECIFIED" - Default Disk state has not been
	// preserved.
	//   "PRESERVED" - Disk state has been preserved.
	SavedState string `json:"savedState,omitempty"`
	// Source: Optional. Specifies a valid partial or full URL to an existing
	// Persistent Disk resource.
	Source string `json:"source,omitempty"`
	// Type: Optional. Specifies the type of the disk.
	//
	// Possible values:
	//   "DISK_TYPE_UNSPECIFIED" - Default value, which is unused.
	//   "SCRATCH" - A scratch disk type.
	//   "PERSISTENT" - A persistent disk type.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoDelete") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoDelete") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AttachedDisk: An instance-attached disk resource.

func (AttachedDisk) MarshalJSON ¶
added in v0.188.0
func (s AttachedDisk) MarshalJSON() ([]byte, error)
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
type Backup ¶
added in v0.188.0
type Backup struct {
	// AlloyDbBackupProperties: Output only. AlloyDB specific backup properties.
	AlloyDbBackupProperties *AlloyDbClusterBackupProperties `json:"alloyDbBackupProperties,omitempty"`
	// BackupApplianceBackupProperties: Output only. Backup Appliance specific
	// backup properties.
	BackupApplianceBackupProperties *BackupApplianceBackupProperties `json:"backupApplianceBackupProperties,omitempty"`
	// BackupApplianceLocks: Optional. The list of BackupLocks taken by the
	// accessor Backup Appliance.
	BackupApplianceLocks []*BackupLock `json:"backupApplianceLocks,omitempty"`
	// BackupRetentionInheritance: Output only. Setting for how the enforced
	// retention end time is inherited. This value is copied from this backup's
	// BackupVault.
	//
	// Possible values:
	//   "BACKUP_RETENTION_INHERITANCE_UNSPECIFIED" - Inheritance behavior not set.
	// This will default to `INHERIT_VAULT_RETENTION`.
	//   "INHERIT_VAULT_RETENTION" - The enforced retention end time of a backup
	// will be inherited from the backup vault's
	// `backup_minimum_enforced_retention_duration` field. This is the default
	// behavior.
	//   "MATCH_BACKUP_EXPIRE_TIME" - The enforced retention end time of a backup
	// will always match the expire time of the backup. If this is set, the
	// backup's enforced retention end time will be set to match the expire time
	// during creation of the backup. When updating, the ERET and expire time must
	// be updated together and have the same value. Invalid update requests will be
	// rejected by the server.
	BackupRetentionInheritance string `json:"backupRetentionInheritance,omitempty"`
	// BackupType: Output only. Type of the backup, unspecified, scheduled or
	// ondemand.
	//
	// Possible values:
	//   "BACKUP_TYPE_UNSPECIFIED" - Backup type is unspecified.
	//   "SCHEDULED" - Scheduled backup.
	//   "ON_DEMAND" - On demand backup.
	//   "ON_DEMAND_OPERATIONAL" - Operational backup.
	BackupType string `json:"backupType,omitempty"`
	// CloudSqlInstanceBackupProperties: Output only. Cloud SQL specific backup
	// properties.
	CloudSqlInstanceBackupProperties *CloudSqlInstanceBackupProperties `json:"cloudSqlInstanceBackupProperties,omitempty"`
	// ComputeInstanceBackupProperties: Output only. Compute Engine specific backup
	// properties.
	ComputeInstanceBackupProperties *ComputeInstanceBackupProperties `json:"computeInstanceBackupProperties,omitempty"`
	// ConsistencyTime: Output only. The point in time when this backup was
	// captured from the source.
	ConsistencyTime string `json:"consistencyTime,omitempty"`
	// CreateTime: Output only. The time when the instance was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Output only. The description of the Backup instance (2048
	// characters or less).
	Description string `json:"description,omitempty"`
	// DiskBackupProperties: Output only. Disk specific backup properties.
	DiskBackupProperties *DiskBackupProperties `json:"diskBackupProperties,omitempty"`
	// EnforcedRetentionEndTime: Optional. The backup can not be deleted before
	// this time.
	EnforcedRetentionEndTime string `json:"enforcedRetentionEndTime,omitempty"`
	// Etag: Optional. Server specified ETag to prevent updates from overwriting
	// each other.
	Etag string `json:"etag,omitempty"`
	// ExpireTime: Optional. When this backup is automatically expired.
	ExpireTime string `json:"expireTime,omitempty"`
	// GcpBackupPlanInfo: Output only. Configuration for a Google Cloud resource.
	GcpBackupPlanInfo *GCPBackupPlanInfo `json:"gcpBackupPlanInfo,omitempty"`
	// GcpResource: Output only. Unique identifier of the GCP resource that is
	// being backed up.
	GcpResource *BackupGcpResource `json:"gcpResource,omitempty"`
	// KmsKeyVersions: Optional. Output only. The list of KMS key versions used to
	// encrypt the backup.
	KmsKeyVersions []string `json:"kmsKeyVersions,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata. No
	// labels currently defined.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Output only. Identifier. Name of the backup to create. It must have
	// the
	// format"projects//locations//backupVaults//dataSources/{datasource}/backups/{
	// backup}". `{backup}` cannot be changed after creation. It must be between
	// 3-63 characters long and must be unique within the datasource.
	Name string `json:"name,omitempty"`
	// ResourceSizeBytes: Output only. source resource size in bytes at the time of
	// the backup.
	ResourceSizeBytes int64 `json:"resourceSizeBytes,omitempty,string"`
	// SatisfiesPzi: Optional. Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Optional. Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// ServiceLocks: Output only. The list of BackupLocks taken by the service to
	// prevent the deletion of the backup.
	ServiceLocks []*BackupLock `json:"serviceLocks,omitempty"`
	// State: Output only. The Backup resource instance state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The backup is being created.
	//   "ACTIVE" - The backup has been created and is fully usable.
	//   "DELETING" - The backup is being deleted.
	//   "ERROR" - The backup is experiencing an issue and might be unusable.
	//   "UPLOADING" - The backup is being uploaded.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. The time when the instance was updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AlloyDbBackupProperties") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AlloyDbBackupProperties") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Backup: Message describing a Backup object.

func (Backup) MarshalJSON ¶
added in v0.188.0
func (s Backup) MarshalJSON() ([]byte, error)
type BackupApplianceBackupConfig ¶
added in v0.188.0
type BackupApplianceBackupConfig struct {
	// ApplicationName: The name of the application.
	ApplicationName string `json:"applicationName,omitempty"`
	// BackupApplianceId: The ID of the backup appliance.
	BackupApplianceId int64 `json:"backupApplianceId,omitempty,string"`
	// BackupApplianceName: The name of the backup appliance.
	BackupApplianceName string `json:"backupApplianceName,omitempty"`
	// HostName: The name of the host where the application is running.
	HostName string `json:"hostName,omitempty"`
	// SlaId: The ID of the SLA of this application.
	SlaId int64 `json:"slaId,omitempty,string"`
	// SlpName: The name of the SLP associated with the application.
	SlpName string `json:"slpName,omitempty"`
	// SltName: The name of the SLT associated with the application.
	SltName string `json:"sltName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicationName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicationName") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupApplianceBackupConfig: BackupApplianceBackupConfig captures the backup configuration for applications that are protected by Backup Appliances.

func (BackupApplianceBackupConfig) MarshalJSON ¶
added in v0.188.0
func (s BackupApplianceBackupConfig) MarshalJSON() ([]byte, error)
type BackupApplianceBackupProperties ¶
added in v0.188.0
type BackupApplianceBackupProperties struct {
	// FinalizeTime: Output only. The time when this backup object was finalized
	// (if none, backup is not finalized).
	FinalizeTime string `json:"finalizeTime,omitempty"`
	// GenerationId: Output only. The numeric generation ID of the backup
	// (monotonically increasing).
	GenerationId int64 `json:"generationId,omitempty"`
	// RecoveryRangeEndTime: Optional. The latest timestamp of data available in
	// this Backup.
	RecoveryRangeEndTime string `json:"recoveryRangeEndTime,omitempty"`
	// RecoveryRangeStartTime: Optional. The earliest timestamp of data available
	// in this Backup.
	RecoveryRangeStartTime string `json:"recoveryRangeStartTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FinalizeTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinalizeTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupApplianceBackupProperties: BackupApplianceBackupProperties represents BackupDR backup appliance's properties.

func (BackupApplianceBackupProperties) MarshalJSON ¶
added in v0.188.0
func (s BackupApplianceBackupProperties) MarshalJSON() ([]byte, error)
type BackupApplianceLockInfo ¶
added in v0.188.0
type BackupApplianceLockInfo struct {
	// BackupApplianceId: Required. The ID of the backup/recovery appliance that
	// created this lock.
	BackupApplianceId int64 `json:"backupApplianceId,omitempty,string"`
	// BackupApplianceName: Required. The name of the backup/recovery appliance
	// that created this lock.
	BackupApplianceName string `json:"backupApplianceName,omitempty"`
	// BackupImage: The image name that depends on this Backup.
	BackupImage string `json:"backupImage,omitempty"`
	// JobName: The job name on the backup/recovery appliance that created this
	// lock.
	JobName string `json:"jobName,omitempty"`
	// LockReason: Required. The reason for the lock: e.g.
	// MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the
	// client and it is not interpreted by the BackupVault service.
	LockReason string `json:"lockReason,omitempty"`
	// SlaId: The SLA on the backup/recovery appliance that owns the lock.
	SlaId int64 `json:"slaId,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "BackupApplianceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupApplianceId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupApplianceLockInfo: BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

func (BackupApplianceLockInfo) MarshalJSON ¶
added in v0.188.0
func (s BackupApplianceLockInfo) MarshalJSON() ([]byte, error)
type BackupConfigDetails ¶
added in v0.220.0
type BackupConfigDetails struct {
	// ApplicableResource: Output only. The full resource name
	// (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the
	// resource that is applicable for the backup configuration. Example:
	// "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance
	// }"
	ApplicableResource string `json:"applicableResource,omitempty"`
	// BackupConfigSource: Output only. The full resource name of the backup config
	// source resource. For example,
	// "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPla
	// ns/{backupplanId}" or
	// "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolic
	// ies/{resourcePolicyId}".
	BackupConfigSource string `json:"backupConfigSource,omitempty"`
	// BackupConfigSourceDisplayName: Output only. The display name of the backup
	// config source resource.
	BackupConfigSourceDisplayName string `json:"backupConfigSourceDisplayName,omitempty"`
	// BackupDrPlanConfig: Google Cloud Backup and DR's Backup Plan specific data.
	BackupDrPlanConfig *BackupDrPlanConfig `json:"backupDrPlanConfig,omitempty"`
	// BackupDrTemplateConfig: Google Cloud Backup and DR's Template specific data.
	BackupDrTemplateConfig *BackupDrTemplateConfig `json:"backupDrTemplateConfig,omitempty"`
	// BackupLocations: The locations where the backups are to be stored.
	BackupLocations []*BackupLocation `json:"backupLocations,omitempty"`
	// BackupVault: Output only. The full resource name
	// (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the
	// backup vault that will store the backups generated through this backup
	// configuration. Example:
	// "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVau
	// lts/{backupvaultId}"
	BackupVault string `json:"backupVault,omitempty"`
	// LatestSuccessfulBackupTime: Output only. Timestamp of the latest successful
	// backup created via this backup configuration.
	LatestSuccessfulBackupTime string `json:"latestSuccessfulBackupTime,omitempty"`
	// PitrSettings: Output only. Point in time recovery settings of the backup
	// configuration resource.
	PitrSettings *PitrSettings `json:"pitrSettings,omitempty"`
	// State: Output only. The state of the backup config resource.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Backup config state not set.
	//   "ACTIVE" - The config is in an active state protecting the resource
	//   "INACTIVE" - The config is currently not protecting the resource. Either
	// because it is disabled or the owning project has been deleted without
	// cleanup of the actual resource.
	//   "ERROR" - The config still exists but because of some error state it is
	// not protecting the resource. Like the source project is deleted. For eg.
	// PlanAssociation, BackupPlan is deleted.
	State string `json:"state,omitempty"`
	// Type: Output only. The type of the backup config resource.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Backup config type is unspecified.
	//   "CLOUD_SQL_INSTANCE_BACKUP_CONFIG" - Backup config is Cloud SQL instance's
	// automated backup config.
	//   "COMPUTE_ENGINE_RESOURCE_POLICY" - Backup config is Compute Engine
	// Resource Policy.
	//   "BACKUPDR_BACKUP_PLAN" - Backup config is Google Cloud Backup and DR's
	// Backup Plan.
	//   "BACKUPDR_TEMPLATE" - Backup config is Google Cloud Backup and DR's
	// Template.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicableResource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicableResource") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupConfigDetails: BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

func (BackupConfigDetails) MarshalJSON ¶
added in v0.220.0
func (s BackupConfigDetails) MarshalJSON() ([]byte, error)
type BackupConfigInfo ¶
added in v0.188.0
type BackupConfigInfo struct {
	// BackupApplianceBackupConfig: Configuration for an application backed up by a
	// Backup Appliance.
	BackupApplianceBackupConfig *BackupApplianceBackupConfig `json:"backupApplianceBackupConfig,omitempty"`
	// GcpBackupConfig: Configuration for a Google Cloud resource.
	GcpBackupConfig *GcpBackupConfig `json:"gcpBackupConfig,omitempty"`
	// LastBackupError: Output only. If the last backup failed, this field has the
	// error message.
	LastBackupError *Status `json:"lastBackupError,omitempty"`
	// LastBackupState: Output only. The status of the last backup to this
	// BackupVault
	//
	// Possible values:
	//   "LAST_BACKUP_STATE_UNSPECIFIED" - Status not set.
	//   "FIRST_BACKUP_PENDING" - The first backup has not yet completed
	//   "SUCCEEDED" - The most recent backup was successful
	//   "FAILED" - The most recent backup failed
	//   "PERMISSION_DENIED" - The most recent backup could not be run/failed
	// because of the lack of permissions
	LastBackupState string `json:"lastBackupState,omitempty"`
	// LastSuccessfulBackupConsistencyTime: Output only. If the last backup were
	// successful, this field has the consistency date.
	LastSuccessfulBackupConsistencyTime string `json:"lastSuccessfulBackupConsistencyTime,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "BackupApplianceBackupConfig") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupApplianceBackupConfig") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupConfigInfo: BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

func (BackupConfigInfo) MarshalJSON ¶
added in v0.188.0
func (s BackupConfigInfo) MarshalJSON() ([]byte, error)
type BackupDrPlanConfig ¶
added in v0.220.0
type BackupDrPlanConfig struct {
	// BackupDrPlanRules: Backup rules of the backup plan resource.
	BackupDrPlanRules []*BackupDrPlanRule `json:"backupDrPlanRules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupDrPlanRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupDrPlanRules") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupDrPlanConfig: BackupDrPlanConfig has additional information about Google Cloud Backup and DR's Plan backup configuration.

func (BackupDrPlanConfig) MarshalJSON ¶
added in v0.220.0
func (s BackupDrPlanConfig) MarshalJSON() ([]byte, error)
type BackupDrPlanRule ¶
added in v0.220.0
type BackupDrPlanRule struct {
	// LastSuccessfulBackupTime: Output only. Timestamp of the latest successful
	// backup created via this backup rule.
	LastSuccessfulBackupTime string `json:"lastSuccessfulBackupTime,omitempty"`
	// RuleId: Output only. Unique Id of the backup rule.
	RuleId string `json:"ruleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastSuccessfulBackupTime")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastSuccessfulBackupTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupDrPlanRule: BackupDrPlanRule has rule specific information of the backup plan resource.

func (BackupDrPlanRule) MarshalJSON ¶
added in v0.220.0
func (s BackupDrPlanRule) MarshalJSON() ([]byte, error)
type BackupDrTemplateConfig ¶
added in v0.220.0
type BackupDrTemplateConfig struct {
	// FirstPartyManagementUri: Output only. The URI of the BackupDr template
	// resource for the first party identity users.
	FirstPartyManagementUri string `json:"firstPartyManagementUri,omitempty"`
	// ThirdPartyManagementUri: Output only. The URI of the BackupDr template
	// resource for the third party identity users.
	ThirdPartyManagementUri string `json:"thirdPartyManagementUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FirstPartyManagementUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirstPartyManagementUri") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupDrTemplateConfig: Provides additional information about Google Cloud Backup and DR's Template backup configuration.

func (BackupDrTemplateConfig) MarshalJSON ¶
added in v0.220.0
func (s BackupDrTemplateConfig) MarshalJSON() ([]byte, error)
type BackupGcpResource ¶
added in v0.254.0
type BackupGcpResource struct {
	// GcpResourcename: Name of the Google Cloud resource.
	GcpResourcename string `json:"gcpResourcename,omitempty"`
	// Location: Location of the resource: //"global"/"unspecified".
	Location string `json:"location,omitempty"`
	// Type: Type of the resource. Use the Unified Resource Type, eg.
	// compute.googleapis.com/Instance.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcpResourcename") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcpResourcename") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupGcpResource: Minimum details to identify a Google Cloud resource for a backup.

func (BackupGcpResource) MarshalJSON ¶
added in v0.254.0
func (s BackupGcpResource) MarshalJSON() ([]byte, error)
type BackupLocation ¶
added in v0.220.0
type BackupLocation struct {
	// LocationId: Output only. The id of the cloud location. Example:
	// "us-central1"
	LocationId string `json:"locationId,omitempty"`
	// Type: Output only. The type of the location.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Location type is unspecified.
	//   "ZONAL" - Location type is zonal.
	//   "REGIONAL" - Location type is regional.
	//   "MULTI_REGIONAL" - Location type is multi regional.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LocationId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LocationId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupLocation: BackupLocation represents a cloud location where a backup can be stored.

func (BackupLocation) MarshalJSON ¶
added in v0.220.0
func (s BackupLocation) MarshalJSON() ([]byte, error)
type BackupLock ¶
added in v0.188.0
type BackupLock struct {
	// BackupApplianceLockInfo: If the client is a backup and recovery appliance,
	// this contains metadata about why the lock exists.
	BackupApplianceLockInfo *BackupApplianceLockInfo `json:"backupApplianceLockInfo,omitempty"`
	// LockUntilTime: Required. The time after which this lock is not considered
	// valid and will no longer protect the Backup from deletion.
	LockUntilTime string `json:"lockUntilTime,omitempty"`
	// ServiceLockInfo: Output only. Contains metadata about the lock exist for
	// Google Cloud native backups.
	ServiceLockInfo *ServiceLockInfo `json:"serviceLockInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupApplianceLockInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupApplianceLockInfo") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupLock: BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

func (BackupLock) MarshalJSON ¶
added in v0.188.0
func (s BackupLock) MarshalJSON() ([]byte, error)
type BackupPlan ¶
added in v0.192.0
type BackupPlan struct {
	// BackupRules: Optional. The backup rules for this `BackupPlan`.
	BackupRules []*BackupRule `json:"backupRules,omitempty"`
	// BackupVault: Required. Resource name of backup vault which will be used as
	// storage location for backups. Format:
	// projects/{project}/locations/{location}/backupVaults/{backupvault}
	BackupVault string `json:"backupVault,omitempty"`
	// BackupVaultServiceAccount: Output only. The Google Cloud service account to
	// be used by the BackupVault for taking backups. Specify the email address of
	// the Backup Vault Service Account.
	BackupVaultServiceAccount string `json:"backupVaultServiceAccount,omitempty"`
	// CreateTime: Output only. When the `BackupPlan` was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. The description of the `BackupPlan` resource. The
	// description allows for additional details about `BackupPlan` and its use
	// cases to be provided. An example description is the following: "This is a
	// backup plan that performs a daily backup at 6pm and retains data for 3
	// months". The description must be at most 2048 characters.
	Description string `json:"description,omitempty"`
	// Etag: Optional. `etag` is returned from the service in the response. As a
	// user of the service, you may provide an etag value in this field to prevent
	// stale resources.
	Etag string `json:"etag,omitempty"`
	// Labels: Optional. This collection of key/value pairs allows for custom
	// labels to be supplied by the user. Example, {"tag": "Weekly"}.
	Labels map[string]string `json:"labels,omitempty"`
	// LogRetentionDays: Optional. Applicable only for Cloud SQL resource_type.
	// Configures how long logs will be stored. It is defined in “days”. This
	// value should be greater than or equal to minimum enforced log retention
	// duration of the backup vault.
	LogRetentionDays int64 `json:"logRetentionDays,omitempty,string"`
	// MaxCustomOnDemandRetentionDays: Optional. Optional field to configure the
	// maximum number of days for which a backup can be retained. This field is
	// only applicable for on-demand backups taken with custom retention value.
	MaxCustomOnDemandRetentionDays int64 `json:"maxCustomOnDemandRetentionDays,omitempty"`
	// Name: Output only. Identifier. The resource name of the `BackupPlan`.
	// Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
	Name string `json:"name,omitempty"`
	// ResourceType: Required. The resource type to which the `BackupPlan` will be
	// applied. Examples include, "compute.googleapis.com/Instance",
	// "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster",
	// "compute.googleapis.com/Disk".
	ResourceType string `json:"resourceType,omitempty"`
	// RevisionId: Output only. The user friendly revision ID of the
	// `BackupPlanRevision`. Example: v0, v1, v2, etc.
	RevisionId string `json:"revisionId,omitempty"`
	// RevisionName: Output only. The resource id of the `BackupPlanRevision`.
	// Format:
	// `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/
	// {revision_id}`
	RevisionName string `json:"revisionName,omitempty"`
	// State: Output only. The `State` for the `BackupPlan`.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The resource is being created.
	//   "ACTIVE" - The resource has been created and is fully usable.
	//   "DELETING" - The resource is being deleted.
	//   "INACTIVE" - The resource has been created but is not usable.
	//   "UPDATING" - The resource is being updated.
	State string `json:"state,omitempty"`
	// SupportedResourceTypes: Output only. All resource types to which backupPlan
	// can be applied.
	SupportedResourceTypes []string `json:"supportedResourceTypes,omitempty"`
	// UpdateTime: Output only. When the `BackupPlan` was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupRules") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupPlan: A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

func (BackupPlan) MarshalJSON ¶
added in v0.192.0
func (s BackupPlan) MarshalJSON() ([]byte, error)
type BackupPlanAssociation ¶
added in v0.192.0
type BackupPlanAssociation struct {
	// AlloydbClusterBackupPlanAssociationProperties: Output only. AlloyDB
	// cluster's backup plan association properties.
	AlloydbClusterBackupPlanAssociationProperties *AlloyDBClusterBackupPlanAssociationProperties `json:"alloydbClusterBackupPlanAssociationProperties,omitempty"`
	// BackupPlan: Required. Resource name of backup plan which needs to be applied
	// on workload. Format:
	// projects/{project}/locations/{location}/backupPlans/{backupPlanId}
	BackupPlan string `json:"backupPlan,omitempty"`
	// BackupPlanRevisionId: Output only. The user friendly revision ID of the
	// `BackupPlanRevision`. Example: v0, v1, v2, etc.
	BackupPlanRevisionId string `json:"backupPlanRevisionId,omitempty"`
	// BackupPlanRevisionName: Output only. The resource id of the
	// `BackupPlanRevision`. Format:
	// `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/
	// {revision_id}`
	BackupPlanRevisionName string `json:"backupPlanRevisionName,omitempty"`
	// CloudSqlInstanceBackupPlanAssociationProperties: Output only. Cloud SQL
	// instance's backup plan association properties.
	CloudSqlInstanceBackupPlanAssociationProperties *CloudSqlInstanceBackupPlanAssociationProperties `json:"cloudSqlInstanceBackupPlanAssociationProperties,omitempty"`
	// CreateTime: Output only. The time when the instance was created.
	CreateTime string `json:"createTime,omitempty"`
	// DataSource: Output only. Resource name of data source which will be used as
	// storage location for backups taken. Format :
	// projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSource
	// s/{datasource}
	DataSource string `json:"dataSource,omitempty"`
	// FilestoreInstanceBackupPlanAssociationProperties: Output only. Filestore
	// instance's backup plan association properties.
	FilestoreInstanceBackupPlanAssociationProperties *FilestoreInstanceBackupPlanAssociationProperties `json:"filestoreInstanceBackupPlanAssociationProperties,omitempty"`
	// Name: Output only. Identifier. The resource name of BackupPlanAssociation in
	// below format Format :
	// projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAss
	// ociationId}
	Name string `json:"name,omitempty"`
	// Resource: Required. Immutable. Resource name of workload on which the backup
	// plan is applied. The format can either be the resource name (e.g.,
	// "projects/my-project/zones/us-central1-a/instances/my-instance") or the full
	// resource URI (e.g.,
	// "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-
	// a/instances/my-instance").
	Resource string `json:"resource,omitempty"`
	// ResourceType: Required. Immutable. Resource type of workload on which
	// backupplan is applied
	ResourceType string `json:"resourceType,omitempty"`
	// RulesConfigInfo: Output only. The config info related to backup rules.
	RulesConfigInfo []*RuleConfigInfo `json:"rulesConfigInfo,omitempty"`
	// State: Output only. The BackupPlanAssociation resource state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The resource is being created.
	//   "ACTIVE" - The resource has been created and is fully usable.
	//   "DELETING" - The resource is being deleted.
	//   "INACTIVE" - The resource has been created but is not usable.
	//   "UPDATING" - The resource is being updated.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. The time when the instance was updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "AlloydbClusterBackupPlanAssociationProperties") to unconditionally include
	// in API requests. By default, fields with empty or default values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AlloydbClusterBackupPlanAssociationProperties") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupPlanAssociation: A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

func (BackupPlanAssociation) MarshalJSON ¶
added in v0.192.0
func (s BackupPlanAssociation) MarshalJSON() ([]byte, error)
type BackupPlanRevision ¶
added in v0.237.0
type BackupPlanRevision struct {
	// BackupPlanSnapshot: The Backup Plan being encompassed by this revision.
	BackupPlanSnapshot *BackupPlan `json:"backupPlanSnapshot,omitempty"`
	// CreateTime: Output only. The timestamp that the revision was created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Output only. Identifier. The resource name of the
	// `BackupPlanRevision`. Format:
	// `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/
	// {revision}`
	Name string `json:"name,omitempty"`
	// RevisionId: Output only. The user friendly revision ID of the
	// `BackupPlanRevision`. Example: v0, v1, v2, etc.
	RevisionId string `json:"revisionId,omitempty"`
	// State: Output only. Resource State
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The resource is being created.
	//   "ACTIVE" - The resource has been created and is fully usable.
	//   "DELETING" - The resource is being deleted.
	//   "INACTIVE" - The resource has been created but is not usable.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupPlanSnapshot") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlanSnapshot") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupPlanRevision: `BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

func (BackupPlanRevision) MarshalJSON ¶
added in v0.237.0
func (s BackupPlanRevision) MarshalJSON() ([]byte, error)
type BackupRule ¶
added in v0.192.0
type BackupRule struct {
	// BackupRetentionDays: Required. Configures the duration for which backup data
	// will be kept. It is defined in “days”. The value should be greater than
	// or equal to minimum enforced retention of the backup vault. Minimum value is
	// 1 and maximum value is 36159 for custom retention on-demand backup. Minimum
	// and maximum values are workload specific for all other rules. Note: Longer
	// retention can lead to higher storage costs post introductory trial. We
	// recommend starting with a short duration of 3 days or less.
	BackupRetentionDays int64 `json:"backupRetentionDays,omitempty"`
	// RuleId: Required. Immutable. The unique id of this `BackupRule`. The
	// `rule_id` is unique per `BackupPlan`.The `rule_id` must start with a
	// lowercase letter followed by up to 62 lowercase letters, numbers, or
	// hyphens. Pattern, /a-z{,62}/.
	RuleId string `json:"ruleId,omitempty"`
	// StandardSchedule: Optional. Defines a schedule that runs within the confines
	// of a defined window of time.
	StandardSchedule *StandardSchedule `json:"standardSchedule,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupRetentionDays") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupRetentionDays") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupRule: `BackupRule` binds the backup schedule to a retention policy.

func (BackupRule) MarshalJSON ¶
added in v0.192.0
func (s BackupRule) MarshalJSON() ([]byte, error)
type BackupVault ¶
added in v0.188.0
type BackupVault struct {
	// AccessRestriction: Optional. Note: This field is added for future use case
	// and will not be supported in the current release. Access restriction for the
	// backup vault. Default value is WITHIN_ORGANIZATION if not provided during
	// creation.
	//
	// Possible values:
	//   "ACCESS_RESTRICTION_UNSPECIFIED" - Access restriction not set. If user
	// does not provide any value or pass this value, it will be changed to
	// WITHIN_ORGANIZATION.
	//   "WITHIN_PROJECT" - Access to or from resources outside your current
	// project will be denied.
	//   "WITHIN_ORGANIZATION" - Access to or from resources outside your current
	// organization will be denied.
	//   "UNRESTRICTED" - No access restriction.
	//   "WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA" - Access to or from resources outside
	// your current organization will be denied except for backup appliance.
	AccessRestriction string `json:"accessRestriction,omitempty"`
	// Annotations: Optional. User annotations. See
	// https://google.aip.dev/128#annotations Stores small amounts of arbitrary
	// data.
	Annotations map[string]string `json:"annotations,omitempty"`
	// BackupCount: Output only. The number of backups in this backup vault.
	BackupCount int64 `json:"backupCount,omitempty,string"`
	// BackupMinimumEnforcedRetentionDuration: Required. The default and minimum
	// enforced retention for each backup within the backup vault. The enforced
	// retention for each backup can be extended. Note: Longer minimum enforced
	// retention period impacts potential storage costs post introductory trial. We
	// recommend starting with a short duration of 3 days or less.
	BackupMinimumEnforcedRetentionDuration string `json:"backupMinimumEnforcedRetentionDuration,omitempty"`
	// BackupRetentionInheritance: Optional. Setting for how a backup's enforced
	// retention end time is inherited.
	//
	// Possible values:
	//   "BACKUP_RETENTION_INHERITANCE_UNSPECIFIED" - Inheritance behavior not set.
	// This will default to `INHERIT_VAULT_RETENTION`.
	//   "INHERIT_VAULT_RETENTION" - The enforced retention end time of a backup
	// will be inherited from the backup vault's
	// `backup_minimum_enforced_retention_duration` field. This is the default
	// behavior.
	//   "MATCH_BACKUP_EXPIRE_TIME" - The enforced retention end time of a backup
	// will always match the expire time of the backup. If this is set, the
	// backup's enforced retention end time will be set to match the expire time
	// during creation of the backup. When updating, the ERET and expire time must
	// be updated together and have the same value. Invalid update requests will be
	// rejected by the server.
	BackupRetentionInheritance string `json:"backupRetentionInheritance,omitempty"`
	// CreateTime: Output only. The time when the instance was created.
	CreateTime string `json:"createTime,omitempty"`
	// Deletable: Output only. Set to true when there are no backups nested under
	// this resource.
	Deletable bool `json:"deletable,omitempty"`
	// Description: Optional. The description of the BackupVault instance (2048
	// characters or less).
	Description string `json:"description,omitempty"`
	// EffectiveTime: Optional. Time after which the BackupVault resource is
	// locked.
	EffectiveTime string `json:"effectiveTime,omitempty"`
	// EncryptionConfig: Optional. The encryption config of the backup vault.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// Etag: Optional. Server specified ETag for the backup vault resource to
	// prevent simultaneous updates from overwiting each other.
	Etag string `json:"etag,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata. No
	// labels currently defined:
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Output only. Identifier. Name of the backup vault to create. It must
	// have the
	// format"projects/{project}/locations/{location}/backupVaults/{backupvault}".
	//  `{backupvault}` cannot be changed after creation. It must be between 3-63
	// characters long and must be unique within the project and location.
	Name string `json:"name,omitempty"`
	// ServiceAccount: Output only. Service account used by the BackupVault Service
	// for this BackupVault. The user should grant this account permissions in
	// their workload project to enable the service to run backups and restores
	// there.
	ServiceAccount string `json:"serviceAccount,omitempty"`
	// State: Output only. The BackupVault resource instance state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The backup vault is being created.
	//   "ACTIVE" - The backup vault has been created and is fully usable.
	//   "DELETING" - The backup vault is being deleted.
	//   "ERROR" - The backup vault is experiencing an issue and might be unusable.
	//   "UPDATING" - The backup vault is being updated.
	State string `json:"state,omitempty"`
	// TotalStoredBytes: Output only. Total size of the storage used by all backup
	// resources.
	TotalStoredBytes int64 `json:"totalStoredBytes,omitempty,string"`
	// Uid: Output only. Immutable after resource creation until resource deletion.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. The time when the instance was updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessRestriction") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessRestriction") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupVault: Message describing a BackupVault object.

func (BackupVault) MarshalJSON ¶
added in v0.188.0
func (s BackupVault) MarshalJSON() ([]byte, error)
type BackupWindow ¶
added in v0.192.0
type BackupWindow struct {
	// EndHourOfDay: Required. The hour of day (1-24) when the window end for
	// example if value of end hour of day is 10 that mean backup window end time
	// is 10:00. End hour of day should be greater than start hour of day. 0 <=
	// start_hour_of_day < end_hour_of_day <= 24 End hour of day is not include in
	// backup window that mean if end_hour_of_day= 10 jobs should start before
	// 10:00.
	EndHourOfDay int64 `json:"endHourOfDay,omitempty"`
	// StartHourOfDay: Required. The hour of day (0-23) when the window starts for
	// example if value of start hour of day is 6 that mean backup window start at
	// 6:00.
	StartHourOfDay int64 `json:"startHourOfDay,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndHourOfDay") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndHourOfDay") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupWindow: `BackupWindow` defines a window of the day during which backup jobs will run.

func (BackupWindow) MarshalJSON ¶
added in v0.192.0
func (s BackupWindow) MarshalJSON() ([]byte, error)
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
type CancelOperationRequest ¶
type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type CloudSqlInstanceBackupPlanAssociationProperties ¶
added in v0.241.0
type CloudSqlInstanceBackupPlanAssociationProperties struct {
	// InstanceCreateTime: Output only. The time when the instance was created.
	InstanceCreateTime string `json:"instanceCreateTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InstanceCreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstanceCreateTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSqlInstanceBackupPlanAssociationProperties: Cloud SQL instance's BPA properties.

func (CloudSqlInstanceBackupPlanAssociationProperties) MarshalJSON ¶
added in v0.241.0
func (s CloudSqlInstanceBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceBackupProperties ¶
added in v0.241.0
type CloudSqlInstanceBackupProperties struct {
	// DatabaseInstalledVersion: Output only. The installed database version of the
	// Cloud SQL instance when the backup was taken.
	DatabaseInstalledVersion string `json:"databaseInstalledVersion,omitempty"`
	// FinalBackup: Output only. Whether the backup is a final backup.
	FinalBackup bool `json:"finalBackup,omitempty"`
	// InstanceCreateTime: Output only. The instance creation timestamp.
	InstanceCreateTime string `json:"instanceCreateTime,omitempty"`
	// InstanceDeleteTime: Output only. The instance delete timestamp.
	InstanceDeleteTime string `json:"instanceDeleteTime,omitempty"`
	// InstanceTier: Output only. The tier (or machine type) for this instance.
	// Example: `db-custom-1-3840`
	InstanceTier string `json:"instanceTier,omitempty"`
	// SourceInstance: Output only. The source instance of the backup. Format:
	// projects/{project}/instances/{instance}
	SourceInstance string `json:"sourceInstance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DatabaseInstalledVersion")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DatabaseInstalledVersion") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSqlInstanceBackupProperties: CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

func (CloudSqlInstanceBackupProperties) MarshalJSON ¶
added in v0.241.0
func (s CloudSqlInstanceBackupProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceDataSourceProperties ¶
added in v0.241.0
type CloudSqlInstanceDataSourceProperties struct {
	// DatabaseInstalledVersion: Output only. The installed database version of the
	// Cloud SQL instance.
	DatabaseInstalledVersion string `json:"databaseInstalledVersion,omitempty"`
	// InstanceCreateTime: Output only. The instance creation timestamp.
	InstanceCreateTime string `json:"instanceCreateTime,omitempty"`
	// InstanceTier: Output only. The tier (or machine type) for this instance.
	// Example: `db-custom-1-3840`
	InstanceTier string `json:"instanceTier,omitempty"`
	// Name: Output only. Name of the Cloud SQL instance backed up by the
	// datasource. Format: projects/{project}/instances/{instance}
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DatabaseInstalledVersion")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DatabaseInstalledVersion") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSqlInstanceDataSourceProperties: CloudSqlInstanceDataSourceProperties represents the properties of a Cloud SQL resource that are stored in the DataSource.

func (CloudSqlInstanceDataSourceProperties) MarshalJSON ¶
added in v0.241.0
func (s CloudSqlInstanceDataSourceProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceDataSourceReferenceProperties ¶
added in v0.241.0
type CloudSqlInstanceDataSourceReferenceProperties struct {
	// DatabaseInstalledVersion: Output only. The installed database version of the
	// Cloud SQL instance.
	DatabaseInstalledVersion string `json:"databaseInstalledVersion,omitempty"`
	// InstanceCreateTime: Output only. The instance creation timestamp.
	InstanceCreateTime string `json:"instanceCreateTime,omitempty"`
	// InstanceTier: Output only. The tier (or machine type) for this instance.
	// Example: `db-custom-1-3840`
	InstanceTier string `json:"instanceTier,omitempty"`
	// Name: Output only. Name of the Cloud SQL instance backed up by the
	// datasource. Format: projects/{project}/instances/{instance}
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DatabaseInstalledVersion")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DatabaseInstalledVersion") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSqlInstanceDataSourceReferenceProperties: CloudSqlInstanceDataSourceReferenceProperties represents the properties of a Cloud SQL resource that are stored in the DataSourceReference.

func (CloudSqlInstanceDataSourceReferenceProperties) MarshalJSON ¶
added in v0.241.0
func (s CloudSqlInstanceDataSourceReferenceProperties) MarshalJSON() ([]byte, error)
type CloudSqlInstanceInitializationConfig ¶
added in v0.241.0
type CloudSqlInstanceInitializationConfig struct {
	// Edition: Required. The edition of the Cloud SQL instance.
	//
	// Possible values:
	//   "EDITION_UNSPECIFIED" - Unspecified edition.
	//   "ENTERPRISE" - Enterprise edition.
	//   "ENTERPRISE_PLUS" - Enterprise Plus edition.
	Edition string `json:"edition,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Edition") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Edition") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSqlInstanceInitializationConfig: CloudSqlInstanceInitializationConfig contains the configuration for initializing a Cloud SQL instance.

func (CloudSqlInstanceInitializationConfig) MarshalJSON ¶
added in v0.241.0
func (s CloudSqlInstanceInitializationConfig) MarshalJSON() ([]byte, error)
type ComputeInstanceBackupProperties ¶
added in v0.188.0
type ComputeInstanceBackupProperties struct {
	// CanIpForward: Enables instances created based on these properties to send
	// packets with source IP addresses other than their own and receive packets
	// with destination IP addresses other than their own. If these instances will
	// be used as an IP gateway or it will be set as the next-hop in a Route
	// resource, specify `true`. If unsure, leave this set to `false`. See the
	// https://cloud.google.com/vpc/docs/using-routes#canipforward documentation
	// for more information.
	CanIpForward bool `json:"canIpForward,omitempty"`
	// Description: An optional text description for the instances that are created
	// from these properties.
	Description string `json:"description,omitempty"`
	// Disk: An array of disks that are associated with the instances that are
	// created from these properties.
	Disk []*AttachedDisk `json:"disk,omitempty"`
	// GuestAccelerator: A list of guest accelerator cards' type and count to use
	// for instances created from these properties.
	GuestAccelerator []*AcceleratorConfig `json:"guestAccelerator,omitempty"`
	// KeyRevocationActionType: KeyRevocationActionType of the instance. Supported
	// options are "STOP" and "NONE". The default value is "NONE" if it is not
	// specified.
	//
	// Possible values:
	//   "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED" - Default value. This value is
	// unused.
	//   "NONE" - Indicates user chose no operation.
	//   "STOP" - Indicates user chose to opt for VM shutdown on key revocation.
	KeyRevocationActionType string `json:"keyRevocationActionType,omitempty"`
	// Labels: Labels to apply to instances that are created from these properties.
	Labels map[string]string `json:"labels,omitempty"`
	// MachineType: The machine type to use for instances that are created from
	// these properties.
	MachineType string `json:"machineType,omitempty"`
	// Metadata: The metadata key/value pairs to assign to instances that are
	// created from these properties. These pairs can consist of custom metadata or
	// predefined keys. See https://cloud.google.com/compute/docs/metadata/overview
	// for more information.
	Metadata *Metadata `json:"metadata,omitempty"`
	// MinCpuPlatform: Minimum cpu/platform to be used by instances. The instance
	// may be scheduled on the specified or newer cpu/platform. Applicable values
	// are the friendly names of CPU platforms, such as `minCpuPlatform: Intel
	// Haswell` or `minCpuPlatform: Intel Sandy Bridge`. For more information, read
	// https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform.
	MinCpuPlatform string `json:"minCpuPlatform,omitempty"`
	// NetworkInterface: An array of network access configurations for this
	// interface.
	NetworkInterface []*NetworkInterface `json:"networkInterface,omitempty"`
	// Scheduling: Specifies the scheduling options for the instances that are
	// created from these properties.
	Scheduling *Scheduling `json:"scheduling,omitempty"`
	// ServiceAccount: A list of service accounts with specified scopes. Access
	// tokens for these service accounts are available to the instances that are
	// created from these properties. Use metadata queries to obtain the access
	// tokens for these instances.
	ServiceAccount []*ServiceAccount `json:"serviceAccount,omitempty"`
	// SourceInstance: The source instance used to create this backup. This can be
	// a partial or full URL to the resource. For example, the following are valid
	// values:
	// -https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
	// instance -projects/project/zones/zone/instances/instance
	SourceInstance string `json:"sourceInstance,omitempty"`
	// Tags: A list of tags to apply to the instances that are created from these
	// properties. The tags identify valid sources or targets for network
	// firewalls. The setTags method can modify this list of tags. Each tag within
	// the list must comply with RFC1035 (https://www.ietf.org/rfc/rfc1035.txt).
	Tags *Tags `json:"tags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CanIpForward") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CanIpForward") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ComputeInstanceBackupProperties: ComputeInstanceBackupProperties represents Compute Engine instance backup properties.

func (ComputeInstanceBackupProperties) MarshalJSON ¶
added in v0.188.0
func (s ComputeInstanceBackupProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceDataSourceProperties ¶
added in v0.188.0
type ComputeInstanceDataSourceProperties struct {
	// Description: The description of the Compute Engine instance.
	Description string `json:"description,omitempty"`
	// MachineType: The machine type of the instance.
	MachineType string `json:"machineType,omitempty"`
	// Name: Name of the compute instance backed up by the datasource.
	Name string `json:"name,omitempty"`
	// TotalDiskCount: The total number of disks attached to the Instance.
	TotalDiskCount int64 `json:"totalDiskCount,omitempty,string"`
	// TotalDiskSizeGb: The sum of all the disk sizes.
	TotalDiskSizeGb int64 `json:"totalDiskSizeGb,omitempty,string"`
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

ComputeInstanceDataSourceProperties: ComputeInstanceDataSourceProperties represents the properties of a ComputeEngine resource that are stored in the DataSource.

func (ComputeInstanceDataSourceProperties) MarshalJSON ¶
added in v0.188.0
func (s ComputeInstanceDataSourceProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceRestoreProperties ¶
added in v0.192.0
type ComputeInstanceRestoreProperties struct {
	// AdvancedMachineFeatures: Optional. Controls for advanced machine-related
	// behavior features.
	AdvancedMachineFeatures *AdvancedMachineFeatures `json:"advancedMachineFeatures,omitempty"`
	// CanIpForward: Optional. Allows this instance to send and receive packets
	// with non-matching destination or source IPs.
	CanIpForward bool `json:"canIpForward,omitempty"`
	// ConfidentialInstanceConfig: Optional. Controls Confidential compute options
	// on the instance
	ConfidentialInstanceConfig *ConfidentialInstanceConfig `json:"confidentialInstanceConfig,omitempty"`
	// DeletionProtection: Optional. Whether the resource should be protected
	// against deletion.
	DeletionProtection bool `json:"deletionProtection,omitempty"`
	// Description: Optional. An optional description of this resource. Provide
	// this property when you create the resource.
	Description string `json:"description,omitempty"`
	// Disks: Optional. Array of disks associated with this instance. Persistent
	// disks must be created before you can assign them. Source regional persistent
	// disks will be restored with default replica zones if not specified.
	Disks []*AttachedDisk `json:"disks,omitempty"`
	// DisplayDevice: Optional. Enables display device for the instance.
	DisplayDevice *DisplayDevice `json:"displayDevice,omitempty"`
	// GuestAccelerators: Optional. A list of the type and count of accelerator
	// cards attached to the instance.
	GuestAccelerators []*AcceleratorConfig `json:"guestAccelerators,omitempty"`
	// Hostname: Optional. Specifies the hostname of the instance. The specified
	// hostname must be RFC1035 compliant. If hostname is not specified, the
	// default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the
	// global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using
	// zonal DNS.
	Hostname string `json:"hostname,omitempty"`
	// InstanceEncryptionKey: Optional. Encrypts suspended data for an instance
	// with a customer-managed encryption key.
	InstanceEncryptionKey *CustomerEncryptionKey `json:"instanceEncryptionKey,omitempty"`
	// KeyRevocationActionType: Optional. KeyRevocationActionType of the instance.
	//
	// Possible values:
	//   "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED" - Default value. This value is
	// unused.
	//   "NONE" - Indicates user chose no operation.
	//   "STOP" - Indicates user chose to opt for VM shutdown on key revocation.
	KeyRevocationActionType string `json:"keyRevocationActionType,omitempty"`
	// Labels: Optional. Labels to apply to this instance.
	Labels map[string]string `json:"labels,omitempty"`
	// MachineType: Optional. Full or partial URL of the machine type resource to
	// use for this instance.
	MachineType string `json:"machineType,omitempty"`
	// Metadata: Optional. This includes custom metadata and predefined keys.
	Metadata *Metadata `json:"metadata,omitempty"`
	// MinCpuPlatform: Optional. Minimum CPU platform to use for this instance.
	MinCpuPlatform string `json:"minCpuPlatform,omitempty"`
	// Name: Required. Name of the compute instance.
	Name string `json:"name,omitempty"`
	// NetworkInterfaces: Optional. An array of network configurations for this
	// instance. These specify how interfaces are configured to interact with other
	// network services, such as connecting to the internet. Multiple interfaces
	// are supported per instance. Required to restore in different project or
	// region.
	NetworkInterfaces []*NetworkInterface `json:"networkInterfaces,omitempty"`
	// NetworkPerformanceConfig: Optional. Configure network performance such as
	// egress bandwidth tier.
	NetworkPerformanceConfig *NetworkPerformanceConfig `json:"networkPerformanceConfig,omitempty"`
	// Params: Input only. Additional params passed with the request, but not
	// persisted as part of resource payload.
	Params *InstanceParams `json:"params,omitempty"`
	// PrivateIpv6GoogleAccess: Optional. The private IPv6 google access type for
	// the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default.
	//
	// Possible values:
	//   "INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED" - Default value. This
	// value is unused.
	//   "INHERIT_FROM_SUBNETWORK" - Each network interface inherits
	// PrivateIpv6GoogleAccess from its subnetwork.
	//   "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE" - Outbound private IPv6 access from
	// VMs in this subnet to Google services. If specified, the subnetwork who is
	// attached to the instance's default network interface will be assigned an
	// internal IPv6 prefix if it doesn't have before.
	//   "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE" - Bidirectional private IPv6
	// access to/from Google services. If specified, the subnetwork who is attached
	// to the instance's default network interface will be assigned an internal
	// IPv6 prefix if it doesn't have before.
	PrivateIpv6GoogleAccess string `json:"privateIpv6GoogleAccess,omitempty"`
	// ReservationAffinity: Optional. Specifies the reservations that this instance
	// can consume from.
	ReservationAffinity *AllocationAffinity `json:"reservationAffinity,omitempty"`
	// ResourcePolicies: Optional. Resource policies applied to this instance. By
	// default, no resource policies will be applied.
	ResourcePolicies []string `json:"resourcePolicies,omitempty"`
	// Scheduling: Optional. Sets the scheduling options for this instance.
	Scheduling *Scheduling `json:"scheduling,omitempty"`
	// ServiceAccounts: Optional. A list of service accounts, with their specified
	// scopes, authorized for this instance. Only one service account per VM
	// instance is supported.
	ServiceAccounts []*ServiceAccount `json:"serviceAccounts,omitempty"`
	// Tags: Optional. Tags to apply to this instance. Tags are used to identify
	// valid sources or targets for network firewalls and are specified by the
	// client during instance creation.
	Tags *Tags `json:"tags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdvancedMachineFeatures") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdvancedMachineFeatures") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ComputeInstanceRestoreProperties: ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

func (ComputeInstanceRestoreProperties) MarshalJSON ¶
added in v0.192.0
func (s ComputeInstanceRestoreProperties) MarshalJSON() ([]byte, error)
type ComputeInstanceTargetEnvironment ¶
added in v0.192.0
type ComputeInstanceTargetEnvironment struct {
	// Project: Required. Target project for the Compute Engine instance.
	Project string `json:"project,omitempty"`
	// Zone: Required. The zone of the Compute Engine instance.
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Project") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Project") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ComputeInstanceTargetEnvironment: ComputeInstanceTargetEnvironment represents Compute Engine target environment to be used during restore.

func (ComputeInstanceTargetEnvironment) MarshalJSON ¶
added in v0.192.0
func (s ComputeInstanceTargetEnvironment) MarshalJSON() ([]byte, error)
type ConfidentialInstanceConfig ¶
added in v0.192.0
type ConfidentialInstanceConfig struct {
	// EnableConfidentialCompute: Optional. Defines whether the instance should
	// have confidential compute enabled.
	EnableConfidentialCompute bool `json:"enableConfidentialCompute,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnableConfidentialCompute")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnableConfidentialCompute") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConfidentialInstanceConfig: A set of Confidential Instance options.

func (ConfidentialInstanceConfig) MarshalJSON ¶
added in v0.192.0
func (s ConfidentialInstanceConfig) MarshalJSON() ([]byte, error)
type CustomerEncryptionKey ¶
added in v0.188.0
type CustomerEncryptionKey struct {
	// KmsKeyName: Optional. The name of the encryption key that is stored in
	// Google Cloud KMS.
	KmsKeyName string `json:"kmsKeyName,omitempty"`
	// KmsKeyServiceAccount: Optional. The service account being used for the
	// encryption request for the given KMS key. If absent, the Compute Engine
	// default service account is used.
	KmsKeyServiceAccount string `json:"kmsKeyServiceAccount,omitempty"`
	// RawKey: Optional. Specifies a 256-bit customer-supplied encryption key.
	RawKey string `json:"rawKey,omitempty"`
	// RsaEncryptedKey: Optional. RSA-wrapped 2048-bit customer-supplied encryption
	// key to either encrypt or decrypt this resource.
	RsaEncryptedKey string `json:"rsaEncryptedKey,omitempty"`
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

CustomerEncryptionKey: A customer-supplied encryption key.

func (CustomerEncryptionKey) MarshalJSON ¶
added in v0.188.0
func (s CustomerEncryptionKey) MarshalJSON() ([]byte, error)
type DataSource ¶
added in v0.188.0
type DataSource struct {
	// BackupBlockedByVaultAccessRestriction: Output only. This field is set to
	// true if the backup is blocked by vault access restriction.
	BackupBlockedByVaultAccessRestriction bool `json:"backupBlockedByVaultAccessRestriction,omitempty"`
	// BackupConfigInfo: Output only. Details of how the resource is configured for
	// backup.
	BackupConfigInfo *BackupConfigInfo `json:"backupConfigInfo,omitempty"`
	// BackupCount: Number of backups in the data source.
	BackupCount int64 `json:"backupCount,omitempty,string"`
	// ConfigState: Output only. The backup configuration state.
	//
	// Possible values:
	//   "BACKUP_CONFIG_STATE_UNSPECIFIED" - The possible states of backup
	// configuration. Status not set.
	//   "ACTIVE" - The data source is actively protected (i.e. there is a
	// BackupPlanAssociation or Appliance SLA pointing to it)
	//   "PASSIVE" - The data source is no longer protected (but may have backups
	// under it)
	ConfigState string `json:"configState,omitempty"`
	// CreateTime: Output only. The time when the instance was created.
	CreateTime string `json:"createTime,omitempty"`
	// DataSourceBackupApplianceApplication: The backed up resource is a backup
	// appliance application.
	DataSourceBackupApplianceApplication *DataSourceBackupApplianceApplication `json:"dataSourceBackupApplianceApplication,omitempty"`
	// DataSourceGcpResource: The backed up resource is a Google Cloud resource.
	// The word 'DataSource' was included in the names to indicate that this is the
	// representation of the Google Cloud resource used within the DataSource
	// object.
	DataSourceGcpResource *DataSourceGcpResource `json:"dataSourceGcpResource,omitempty"`
	// Etag: Server specified ETag for the ManagementServer resource to prevent
	// simultaneous updates from overwiting each other.
	Etag string `json:"etag,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata. No
	// labels currently defined:
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Output only. Identifier. Name of the datasource to create. It must
	// have the
	// format"projects/{project}/locations/{location}/backupVaults/{backupvault}/da
	// taSources/{datasource}". `{datasource}` cannot be changed after creation.
	// It must be between 3-63 characters long and must be unique within the backup
	// vault.
	Name string `json:"name,omitempty"`
	// State: Output only. The DataSource resource instance state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The data source is being created.
	//   "ACTIVE" - The data source has been created and is fully usable.
	//   "DELETING" - The data source is being deleted.
	//   "ERROR" - The data source is experiencing an issue and might be unusable.
	State string `json:"state,omitempty"`
	// TotalStoredBytes: The number of bytes (metadata and data) stored in this
	// datasource.
	TotalStoredBytes int64 `json:"totalStoredBytes,omitempty,string"`
	// UpdateTime: Output only. The time when the instance was updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "BackupBlockedByVaultAccessRestriction") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "BackupBlockedByVaultAccessRestriction") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

DataSource: Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

func (DataSource) MarshalJSON ¶
added in v0.188.0
func (s DataSource) MarshalJSON() ([]byte, error)
type DataSourceBackupApplianceApplication ¶
added in v0.188.0
type DataSourceBackupApplianceApplication struct {
	// ApplianceId: Appliance Id of the Backup Appliance.
	ApplianceId int64 `json:"applianceId,omitempty,string"`
	// ApplicationId: The appid field of the application within the Backup
	// Appliance.
	ApplicationId int64 `json:"applicationId,omitempty,string"`
	// ApplicationName: The name of the Application as known to the Backup
	// Appliance.
	ApplicationName string `json:"applicationName,omitempty"`
	// BackupAppliance: Appliance name.
	BackupAppliance string `json:"backupAppliance,omitempty"`
	// HostId: Hostid of the application host.
	HostId int64 `json:"hostId,omitempty,string"`
	// Hostname: Hostname of the host where the application is running.
	Hostname string `json:"hostname,omitempty"`
	// Type: The type of the application. e.g. VMBackup
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplianceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplianceId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DataSourceBackupApplianceApplication: BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance.

func (DataSourceBackupApplianceApplication) MarshalJSON ¶
added in v0.188.0
func (s DataSourceBackupApplianceApplication) MarshalJSON() ([]byte, error)
type DataSourceBackupConfigInfo ¶
added in v0.241.0
type DataSourceBackupConfigInfo struct {
	// LastBackupState: Output only. The status of the last backup in this
	// DataSource
	//
	// Possible values:
	//   "LAST_BACKUP_STATE_UNSPECIFIED" - Status not set.
	//   "FIRST_BACKUP_PENDING" - The first backup has not yet completed
	//   "SUCCEEDED" - The most recent backup was successful
	//   "FAILED" - The most recent backup failed
	//   "PERMISSION_DENIED" - The most recent backup could not be run/failed
	// because of the lack of permissions
	LastBackupState string `json:"lastBackupState,omitempty"`
	// LastSuccessfulBackupConsistencyTime: Output only. Timestamp of the last
	// successful backup to this DataSource.
	LastSuccessfulBackupConsistencyTime string `json:"lastSuccessfulBackupConsistencyTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastBackupState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastBackupState") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DataSourceBackupConfigInfo: Information of backup configuration on the DataSource.

func (DataSourceBackupConfigInfo) MarshalJSON ¶
added in v0.241.0
func (s DataSourceBackupConfigInfo) MarshalJSON() ([]byte, error)
type DataSourceGcpResource ¶
added in v0.188.0
type DataSourceGcpResource struct {
	// AlloyDbClusterDatasourceProperties: Output only.
	// AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster
	// properties that are useful at the Datasource level. Currently none of its
	// child properties are auditable. If new auditable properties are added, the
	// AUDIT annotation should be added.
	AlloyDbClusterDatasourceProperties *AlloyDBClusterDataSourceProperties `json:"alloyDbClusterDatasourceProperties,omitempty"`
	// CloudSqlInstanceDatasourceProperties: Output only.
	// CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance
	// properties that are useful at the Datasource level.
	CloudSqlInstanceDatasourceProperties *CloudSqlInstanceDataSourceProperties `json:"cloudSqlInstanceDatasourceProperties,omitempty"`
	// ComputeInstanceDatasourceProperties: ComputeInstanceDataSourceProperties has
	// a subset of Compute Instance properties that are useful at the Datasource
	// level.
	ComputeInstanceDatasourceProperties *ComputeInstanceDataSourceProperties `json:"computeInstanceDatasourceProperties,omitempty"`
	// DiskDatasourceProperties: DiskDataSourceProperties has a subset of Disk
	// properties that are useful at the Datasource level.
	DiskDatasourceProperties *DiskDataSourceProperties `json:"diskDatasourceProperties,omitempty"`
	// GcpResourcename: Output only. Full resource pathname URL of the source
	// Google Cloud resource.
	GcpResourcename string `json:"gcpResourcename,omitempty"`
	// Location: Location of the resource: //"global"/"unspecified".
	Location string `json:"location,omitempty"`
	// Type: The type of the Google Cloud resource. Use the Unified Resource Type,
	// eg. compute.googleapis.com/Instance.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AlloyDbClusterDatasourceProperties") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AlloyDbClusterDatasourceProperties") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

DataSourceGcpResource: DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

func (DataSourceGcpResource) MarshalJSON ¶
added in v0.188.0
func (s DataSourceGcpResource) MarshalJSON() ([]byte, error)
type DataSourceGcpResourceInfo ¶
added in v0.241.0
type DataSourceGcpResourceInfo struct {
	// AlloyDbClusterProperties: Output only. The properties of the AlloyDB
	// cluster.
	AlloyDbClusterProperties *AlloyDBClusterDataSourceReferenceProperties `json:"alloyDbClusterProperties,omitempty"`
	// CloudSqlInstanceProperties: Output only. The properties of the Cloud SQL
	// instance.
	CloudSqlInstanceProperties *CloudSqlInstanceDataSourceReferenceProperties `json:"cloudSqlInstanceProperties,omitempty"`
	// GcpResourcename: Output only. The resource name of the Google Cloud
	// resource. Ex: projects/{project}/zones/{zone}/instances/{instance}
	GcpResourcename string `json:"gcpResourcename,omitempty"`
	// Location: Output only. The location of the Google Cloud resource. Ex:
	// //"global"/"unspecified"
	Location string `json:"location,omitempty"`
	// Type: Output only. The type of the Google Cloud resource. Ex:
	// compute.googleapis.com/Instance
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AlloyDbClusterProperties")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AlloyDbClusterProperties") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DataSourceGcpResourceInfo: The Google Cloud resource that the DataSource is associated with.

func (DataSourceGcpResourceInfo) MarshalJSON ¶
added in v0.241.0
func (s DataSourceGcpResourceInfo) MarshalJSON() ([]byte, error)
type DataSourceReference ¶
added in v0.241.0
type DataSourceReference struct {
	// CreateTime: Output only. The time when the DataSourceReference was created.
	CreateTime string `json:"createTime,omitempty"`
	// DataSource: Output only. The resource name of the DataSource. Format:
	// projects/{project}/locations/{location}/backupVaults/{backupVault}/dataSource
	// s/{dataSource}
	DataSource string `json:"dataSource,omitempty"`
	// DataSourceBackupConfigInfo: Output only. Information of backup configuration
	// on the DataSource.
	DataSourceBackupConfigInfo *DataSourceBackupConfigInfo `json:"dataSourceBackupConfigInfo,omitempty"`
	// DataSourceBackupConfigState: Output only. The backup configuration state of
	// the DataSource.
	//
	// Possible values:
	//   "BACKUP_CONFIG_STATE_UNSPECIFIED" - The possible states of backup
	// configuration. Status not set.
	//   "ACTIVE" - The data source is actively protected (i.e. there is a
	// BackupPlanAssociation or Appliance SLA pointing to it)
	//   "PASSIVE" - The data source is no longer protected (but may have backups
	// under it)
	DataSourceBackupConfigState string `json:"dataSourceBackupConfigState,omitempty"`
	// DataSourceBackupCount: Output only. Number of backups in the DataSource.
	DataSourceBackupCount int64 `json:"dataSourceBackupCount,omitempty,string"`
	// DataSourceGcpResourceInfo: Output only. The Google Cloud resource that the
	// DataSource is associated with.
	DataSourceGcpResourceInfo *DataSourceGcpResourceInfo `json:"dataSourceGcpResourceInfo,omitempty"`
	// Name: Identifier. The resource name of the DataSourceReference. Format:
	// projects/{project}/locations/{location}/dataSourceReferences/{data_source_ref
	// erence}
	Name string `json:"name,omitempty"`
	// TotalStoredBytes: Output only. Total size of the storage used by all backup
	// resources for the referenced datasource.
	TotalStoredBytes int64 `json:"totalStoredBytes,omitempty,string"`

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

DataSourceReference: DataSourceReference is a reference to a DataSource resource.

func (DataSourceReference) MarshalJSON ¶
added in v0.241.0
func (s DataSourceReference) MarshalJSON() ([]byte, error)
type DiskBackupProperties ¶
added in v0.234.0
type DiskBackupProperties struct {
	// AccessMode: The access mode of the source disk.
	AccessMode string `json:"accessMode,omitempty"`
	// Architecture: The architecture of the source disk. Valid values are ARM64 or
	// X86_64.
	//
	// Possible values:
	//   "ARCHITECTURE_UNSPECIFIED" - Default value. This value is unused.
	//   "X86_64" - Disks with architecture X86_64
	//   "ARM64" - Disks with architecture ARM64
	Architecture string `json:"architecture,omitempty"`
	// Description: A description of the source disk.
	Description string `json:"description,omitempty"`
	// EnableConfidentialCompute: Indicates whether the source disk is using
	// confidential compute mode.
	EnableConfidentialCompute bool `json:"enableConfidentialCompute,omitempty"`
	// GuestOsFeature: A list of guest OS features that are applicable to this
	// backup.
	GuestOsFeature []*GuestOsFeature `json:"guestOsFeature,omitempty"`
	// Labels: The labels of the source disk.
	Labels map[string]string `json:"labels,omitempty"`
	// Licenses: A list of publicly available licenses that are applicable to this
	// backup. This is applicable if the original image had licenses attached, e.g.
	// Windows image.
	Licenses []string `json:"licenses,omitempty"`
	// PhysicalBlockSizeBytes: The physical block size of the source disk.
	PhysicalBlockSizeBytes int64 `json:"physicalBlockSizeBytes,omitempty,string"`
	// ProvisionedIops: The number of IOPS provisioned for the source disk.
	ProvisionedIops int64 `json:"provisionedIops,omitempty,string"`
	// ProvisionedThroughput: The number of throughput provisioned for the source
	// disk.
	ProvisionedThroughput int64 `json:"provisionedThroughput,omitempty,string"`
	// Region: Region and zone are mutually exclusive fields. The URL of the region
	// of the source disk.
	Region string `json:"region,omitempty"`
	// ReplicaZones: The URL of the Zones where the source disk should be
	// replicated.
	ReplicaZones []string `json:"replicaZones,omitempty"`
	// SizeGb: Size(in GB) of the source disk.
	SizeGb int64 `json:"sizeGb,omitempty,string"`
	// SourceDisk: The source disk used to create this backup.
	SourceDisk string `json:"sourceDisk,omitempty"`
	// StoragePool: The storage pool of the source disk.
	StoragePool string `json:"storagePool,omitempty"`
	// Type: The URL of the type of the disk.
	Type string `json:"type,omitempty"`
	// Zone: The URL of the Zone where the source disk.
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessMode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessMode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DiskBackupProperties: DiskBackupProperties represents the properties of a Disk backup.

func (DiskBackupProperties) MarshalJSON ¶
added in v0.234.0
func (s DiskBackupProperties) MarshalJSON() ([]byte, error)
type DiskDataSourceProperties ¶
added in v0.234.0
type DiskDataSourceProperties struct {
	// Description: The description of the disk.
	Description string `json:"description,omitempty"`
	// Name: Name of the disk backed up by the datasource.
	Name string `json:"name,omitempty"`
	// SizeGb: The size of the disk in GB.
	SizeGb int64 `json:"sizeGb,omitempty,string"`
	// Type: The type of the disk.
	Type string `json:"type,omitempty"`
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

DiskDataSourceProperties: DiskDataSourceProperties represents the properties of a Disk resource that are stored in the DataSource. .

func (DiskDataSourceProperties) MarshalJSON ¶
added in v0.234.0
func (s DiskDataSourceProperties) MarshalJSON() ([]byte, error)
type DiskRestoreProperties ¶
added in v0.234.0
type DiskRestoreProperties struct {
	// AccessMode: Optional. The access mode of the disk.
	//
	// Possible values:
	//   "READ_WRITE_SINGLE" - The default AccessMode, means the disk can be
	// attached to single instance in RW mode.
	//   "READ_WRITE_MANY" - The AccessMode means the disk can be attached to
	// multiple instances in RW mode.
	//   "READ_ONLY_MANY" - The AccessMode means the disk can be attached to
	// multiple instances in RO mode.
	AccessMode string `json:"accessMode,omitempty"`
	// Architecture: Optional. The architecture of the source disk. Valid values
	// are ARM64 or X86_64.
	//
	// Possible values:
	//   "ARCHITECTURE_UNSPECIFIED" - Default value. This value is unused.
	//   "X86_64" - Disks with architecture X86_64
	//   "ARM64" - Disks with architecture ARM64
	Architecture string `json:"architecture,omitempty"`
	// Description: Optional. An optional description of this resource. Provide
	// this property when you create the resource.
	Description string `json:"description,omitempty"`
	// DiskEncryptionKey: Optional. Encrypts the disk using a customer-supplied
	// encryption key or a customer-managed encryption key.
	DiskEncryptionKey *CustomerEncryptionKey `json:"diskEncryptionKey,omitempty"`
	// EnableConfidentialCompute: Optional. Indicates whether this disk is using
	// confidential compute mode. Encryption with a Cloud KMS key is required to
	// enable this option.
	EnableConfidentialCompute bool `json:"enableConfidentialCompute,omitempty"`
	// GuestOsFeature: Optional. A list of features to enable in the guest
	// operating system. This is applicable only for bootable images.
	GuestOsFeature []*GuestOsFeature `json:"guestOsFeature,omitempty"`
	// Labels: Optional. Labels to apply to this disk. These can be modified later
	// using setLabels method. Label values can be empty.
	Labels map[string]string `json:"labels,omitempty"`
	// Licenses: Optional. A list of publicly available licenses that are
	// applicable to this backup. This is applicable if the original image had
	// licenses attached, e.g. Windows image
	Licenses []string `json:"licenses,omitempty"`
	// Name: Required. Name of the disk.
	Name string `json:"name,omitempty"`
	// PhysicalBlockSizeBytes: Optional. Physical block size of the persistent
	// disk, in bytes. If not present in a request, a default value is used.
	// Currently, the supported size is 4096.
	PhysicalBlockSizeBytes int64 `json:"physicalBlockSizeBytes,omitempty,string"`
	// ProvisionedIops: Optional. Indicates how many IOPS to provision for the
	// disk. This sets the number of I/O operations per second that the disk can
	// handle.
	ProvisionedIops int64 `json:"provisionedIops,omitempty,string"`
	// ProvisionedThroughput: Optional. Indicates how much throughput to provision
	// for the disk. This sets the number of throughput MB per second that the disk
	// can handle.
	ProvisionedThroughput int64 `json:"provisionedThroughput,omitempty,string"`
	// ResourceManagerTags: Optional. Resource manager tags to be bound to the
	// disk.
	ResourceManagerTags map[string]string `json:"resourceManagerTags,omitempty"`
	// ResourcePolicy: Optional. Resource policies applied to this disk.
	ResourcePolicy []string `json:"resourcePolicy,omitempty"`
	// SizeGb: Required. The size of the disk in GB.
	SizeGb int64 `json:"sizeGb,omitempty,string"`
	// StoragePool: Optional. The storage pool in which the new disk is created.
	// You can provide this as a partial or full URL to the resource.
	StoragePool string `json:"storagePool,omitempty"`
	// Type: Required. URL of the disk type resource describing which disk type to
	// use to create the disk.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessMode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessMode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DiskRestoreProperties: DiskRestoreProperties represents the properties of a Disk restore.

func (DiskRestoreProperties) MarshalJSON ¶
added in v0.234.0
func (s DiskRestoreProperties) MarshalJSON() ([]byte, error)
type DiskTargetEnvironment ¶
added in v0.234.0
type DiskTargetEnvironment struct {
	// Project: Required. Target project for the disk.
	Project string `json:"project,omitempty"`
	// Zone: Required. Target zone for the disk.
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Project") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Project") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DiskTargetEnvironment: DiskTargetEnvironment represents the target environment for the disk.

func (DiskTargetEnvironment) MarshalJSON ¶
added in v0.234.0
func (s DiskTargetEnvironment) MarshalJSON() ([]byte, error)
type DisplayDevice ¶
added in v0.192.0
type DisplayDevice struct {
	// EnableDisplay: Optional. Enables display for the Compute Engine VM
	EnableDisplay bool `json:"enableDisplay,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EnableDisplay") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EnableDisplay") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DisplayDevice: A set of Display Device options

func (DisplayDevice) MarshalJSON ¶
added in v0.192.0
func (s DisplayDevice) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EncryptionConfig ¶
added in v0.257.0
type EncryptionConfig struct {
	// KmsKeyName: Optional. The Cloud KMS key name to encrypt backups in this
	// backup vault. Must be in the same region as the vault. Some workload backups
	// like compute disk backups may use their inherited source key instead.
	// Format:
	// projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}
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

EncryptionConfig: Message describing the EncryptionConfig of backup vault. This determines how data within the vault is encrypted at rest.

func (EncryptionConfig) MarshalJSON ¶
added in v0.257.0
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EndTrialRequest ¶
added in v0.257.0
type EndTrialRequest struct {
	// EndReason: Required. The reason for ending the trial.
	//
	// Possible values:
	//   "END_REASON_UNSPECIFIED" - End reason not set.
	//   "MOVE_TO_PAID" - Trial is deliberately ended by the user to transition to
	// paid usage.
	//   "DISCONTINUED" - Trial is discontinued before expiration.
	EndReason string `json:"endReason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndReason") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndReason") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EndTrialRequest: Request message for ending a trial.

func (EndTrialRequest) MarshalJSON ¶
added in v0.257.0
func (s EndTrialRequest) MarshalJSON() ([]byte, error)
type Entry ¶
added in v0.188.0
type Entry struct {
	// Key: Optional. Key for the metadata entry.
	Key string `json:"key,omitempty"`
	// Value: Optional. Value for the metadata entry. These are free-form strings,
	// and only have meaning as interpreted by the image running in the instance.
	// The only restriction placed on values is that their size must be less than
	// or equal to 262144 bytes (256 KiB).
	Value string `json:"value,omitempty"`
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

Entry: A key/value pair to be used for storing metadata.

func (Entry) MarshalJSON ¶
added in v0.188.0
func (s Entry) MarshalJSON() ([]byte, error)
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
type FetchAccessTokenRequest ¶
added in v0.188.0
type FetchAccessTokenRequest struct {
	// GenerationId: Required. The generation of the backup to update.
	GenerationId int64 `json:"generationId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GenerationId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GenerationId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchAccessTokenRequest: Request message for FetchAccessToken.

func (FetchAccessTokenRequest) MarshalJSON ¶
added in v0.188.0
func (s FetchAccessTokenRequest) MarshalJSON() ([]byte, error)
type FetchAccessTokenResponse ¶
added in v0.188.0
type FetchAccessTokenResponse struct {
	// ExpireTime: The token is valid until this time.
	ExpireTime string `json:"expireTime,omitempty"`
	// ReadLocation: The location in bucket that can be used for reading.
	ReadLocation string `json:"readLocation,omitempty"`
	// Token: The downscoped token that was created.
	Token string `json:"token,omitempty"`
	// WriteLocation: The location in bucket that can be used for writing.
	WriteLocation string `json:"writeLocation,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExpireTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpireTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchAccessTokenResponse: Response message for FetchAccessToken.

func (FetchAccessTokenResponse) MarshalJSON ¶
added in v0.188.0
func (s FetchAccessTokenResponse) MarshalJSON() ([]byte, error)
type FetchBackupPlanAssociationsForResourceTypeResponse ¶
added in v0.241.0
type FetchBackupPlanAssociationsForResourceTypeResponse struct {
	// BackupPlanAssociations: Output only. The BackupPlanAssociations from the
	// specified parent.
	BackupPlanAssociations []*BackupPlanAssociation `json:"backupPlanAssociations,omitempty"`
	// NextPageToken: Output only. A token, which can be sent as `page_token` to
	// retrieve the next page. If this field is omitted, there are no subsequent
	// pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupPlanAssociations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlanAssociations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchBackupPlanAssociationsForResourceTypeResponse: Response for the FetchBackupPlanAssociationsForResourceType method.

func (FetchBackupPlanAssociationsForResourceTypeResponse) MarshalJSON ¶
added in v0.241.0
func (s FetchBackupPlanAssociationsForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchBackupsForResourceTypeResponse ¶
added in v0.254.0
type FetchBackupsForResourceTypeResponse struct {
	// Backups: The Backups from the specified parent.
	Backups []*Backup `json:"backups,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
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

FetchBackupsForResourceTypeResponse: Response for the FetchBackupsForResourceType method.

func (FetchBackupsForResourceTypeResponse) MarshalJSON ¶
added in v0.254.0
func (s FetchBackupsForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchDataSourceReferencesForResourceTypeResponse ¶
added in v0.241.0
type FetchDataSourceReferencesForResourceTypeResponse struct {
	// DataSourceReferences: The DataSourceReferences from the specified parent.
	DataSourceReferences []*DataSourceReference `json:"dataSourceReferences,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataSourceReferences") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataSourceReferences") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchDataSourceReferencesForResourceTypeResponse: Response for the FetchDataSourceReferencesForResourceType method.

func (FetchDataSourceReferencesForResourceTypeResponse) MarshalJSON ¶
added in v0.241.0
func (s FetchDataSourceReferencesForResourceTypeResponse) MarshalJSON() ([]byte, error)
type FetchMsComplianceMetadataRequest ¶
added in v0.243.0
type FetchMsComplianceMetadataRequest struct {
	// ProjectId: Required. The project id of the target project
	ProjectId string `json:"projectId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProjectId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProjectId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchMsComplianceMetadataRequest: Request message for GetMsComplianceMetadata

func (FetchMsComplianceMetadataRequest) MarshalJSON ¶
added in v0.243.0
func (s FetchMsComplianceMetadataRequest) MarshalJSON() ([]byte, error)
type FetchMsComplianceMetadataResponse ¶
added in v0.243.0
type FetchMsComplianceMetadataResponse struct {
	// IsAssuredWorkload: The ms compliance metadata of the target project, if the
	// project is an Assured Workloads project, values will be true, otherwise
	// false.
	IsAssuredWorkload bool `json:"isAssuredWorkload,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "IsAssuredWorkload") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsAssuredWorkload") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchMsComplianceMetadataResponse: Response message for GetMsComplianceMetadata

func (FetchMsComplianceMetadataResponse) MarshalJSON ¶
added in v0.243.0
func (s FetchMsComplianceMetadataResponse) MarshalJSON() ([]byte, error)
type FetchUsableBackupVaultsResponse ¶
added in v0.188.0
type FetchUsableBackupVaultsResponse struct {
	// BackupVaults: The list of BackupVault instances in the project for the
	// specified location. If the '{location}' value in the request is "-", the
	// response contains a list of instances from all locations. In case any
	// location is unreachable, the response will only return backup vaults in
	// reachable locations and the 'unreachable' field will be populated with a
	// list of unreachable locations.
	BackupVaults []*BackupVault `json:"backupVaults,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupVaults") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupVaults") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FetchUsableBackupVaultsResponse: Response message for fetching usable BackupVaults.

func (FetchUsableBackupVaultsResponse) MarshalJSON ¶
added in v0.188.0
func (s FetchUsableBackupVaultsResponse) MarshalJSON() ([]byte, error)
type FilestoreInstanceBackupPlanAssociationProperties ¶
added in v0.260.0
type FilestoreInstanceBackupPlanAssociationProperties struct {
	// InstanceCreateTime: Output only. The time when the instance was created.
	InstanceCreateTime string `json:"instanceCreateTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InstanceCreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstanceCreateTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilestoreInstanceBackupPlanAssociationProperties: Filestore instance's BPA properties.

func (FilestoreInstanceBackupPlanAssociationProperties) MarshalJSON ¶
added in v0.260.0
func (s FilestoreInstanceBackupPlanAssociationProperties) MarshalJSON() ([]byte, error)
type FinalizeBackupRequest ¶
added in v0.188.0
type FinalizeBackupRequest struct {
	// BackupId: Required. Resource ID of the Backup resource to be finalized. This
	// must be the same backup_id that was used in the InitiateBackupRequest.
	BackupId string `json:"backupId,omitempty"`
	// ConsistencyTime: The point in time when this backup was captured from the
	// source. This will be assigned to the consistency_time field of the newly
	// created Backup.
	ConsistencyTime string `json:"consistencyTime,omitempty"`
	// Description: This will be assigned to the description field of the newly
	// created Backup.
	Description string `json:"description,omitempty"`
	// RecoveryRangeEndTime: The latest timestamp of data available in this Backup.
	// This will be set on the newly created Backup.
	RecoveryRangeEndTime string `json:"recoveryRangeEndTime,omitempty"`
	// RecoveryRangeStartTime: The earliest timestamp of data available in this
	// Backup. This will set on the newly created Backup.
	RecoveryRangeStartTime string `json:"recoveryRangeStartTime,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes after the first request. For example,
	// consider a situation where you make an initial request and the request times
	// out. If you make the request again with the same request ID, the server can
	// check if original operation with the same request ID was received, and if
	// so, will ignore the second request. This prevents clients from accidentally
	// creating duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// RetentionDuration: The ExpireTime on the backup will be set to FinalizeTime
	// plus this duration. If the resulting ExpireTime is less than
	// EnforcedRetentionEndTime, then ExpireTime is set to
	// EnforcedRetentionEndTime.
	RetentionDuration string `json:"retentionDuration,omitempty"`
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

FinalizeBackupRequest: Message for finalizing a Backup.

func (FinalizeBackupRequest) MarshalJSON ¶
added in v0.188.0
func (s FinalizeBackupRequest) MarshalJSON() ([]byte, error)
type GCPBackupPlanInfo ¶
added in v0.188.0
type GCPBackupPlanInfo struct {
	// BackupPlan: Resource name of backup plan by which workload is protected at
	// the time of the backup. Format:
	// projects/{project}/locations/{location}/backupPlans/{backupPlanId}
	BackupPlan string `json:"backupPlan,omitempty"`
	// BackupPlanRevisionId: The user friendly id of the backup plan revision which
	// triggered this backup in case of scheduled backup or used for on demand
	// backup.
	BackupPlanRevisionId string `json:"backupPlanRevisionId,omitempty"`
	// BackupPlanRevisionName: Resource name of the backup plan revision which
	// triggered this backup in case of scheduled backup or used for on demand
	// backup. Format:
	// projects/{project}/locations/{location}/backupPlans/{backupPlanId}/revisions/
	// {revisionId}
	BackupPlanRevisionName string `json:"backupPlanRevisionName,omitempty"`
	// BackupPlanRuleId: The rule id of the backup plan which triggered this backup
	// in case of scheduled backup or used for
	BackupPlanRuleId string `json:"backupPlanRuleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupPlan") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlan") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GCPBackupPlanInfo: GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup.

func (GCPBackupPlanInfo) MarshalJSON ¶
added in v0.188.0
func (s GCPBackupPlanInfo) MarshalJSON() ([]byte, error)
type GcpBackupConfig ¶
added in v0.188.0
type GcpBackupConfig struct {
	// BackupPlan: The name of the backup plan.
	BackupPlan string `json:"backupPlan,omitempty"`
	// BackupPlanAssociation: The name of the backup plan association.
	BackupPlanAssociation string `json:"backupPlanAssociation,omitempty"`
	// BackupPlanDescription: The description of the backup plan.
	BackupPlanDescription string `json:"backupPlanDescription,omitempty"`
	// BackupPlanRevisionId: The user friendly id of the backup plan revision. E.g.
	// v0, v1 etc.
	BackupPlanRevisionId string `json:"backupPlanRevisionId,omitempty"`
	// BackupPlanRevisionName: The name of the backup plan revision.
	BackupPlanRevisionName string `json:"backupPlanRevisionName,omitempty"`
	// BackupPlanRules: The names of the backup plan rules which point to this
	// backupvault
	BackupPlanRules []string `json:"backupPlanRules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupPlan") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlan") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GcpBackupConfig: GcpBackupConfig captures the Backup configuration details for Google Cloud resources. All Google Cloud resources regardless of type are protected with backup plan associations.

func (GcpBackupConfig) MarshalJSON ¶
added in v0.188.0
func (s GcpBackupConfig) MarshalJSON() ([]byte, error)
type GcpResource ¶
added in v0.200.0
type GcpResource struct {
	// GcpResourcename: Name of the Google Cloud resource.
	GcpResourcename string `json:"gcpResourcename,omitempty"`
	// Location: Location of the resource: //"global"/"unspecified".
	Location string `json:"location,omitempty"`
	// Type: Type of the resource. Use the Unified Resource Type, eg.
	// compute.googleapis.com/Instance.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcpResourcename") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcpResourcename") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GcpResource: Minimum details to identify a Google Cloud resource

func (GcpResource) MarshalJSON ¶
added in v0.200.0
func (s GcpResource) MarshalJSON() ([]byte, error)
type GuestOsFeature ¶
added in v0.188.0
type GuestOsFeature struct {
	// Type: The ID of a supported feature.
	//
	// Possible values:
	//   "FEATURE_TYPE_UNSPECIFIED" - Default value, which is unused.
	//   "VIRTIO_SCSI_MULTIQUEUE" - VIRTIO_SCSI_MULTIQUEUE feature type.
	//   "WINDOWS" - WINDOWS feature type.
	//   "MULTI_IP_SUBNET" - MULTI_IP_SUBNET feature type.
	//   "UEFI_COMPATIBLE" - UEFI_COMPATIBLE feature type.
	//   "SECURE_BOOT" - SECURE_BOOT feature type.
	//   "GVNIC" - GVNIC feature type.
	//   "SEV_CAPABLE" - SEV_CAPABLE feature type.
	//   "BARE_METAL_LINUX_COMPATIBLE" - BARE_METAL_LINUX_COMPATIBLE feature type.
	//   "SUSPEND_RESUME_COMPATIBLE" - SUSPEND_RESUME_COMPATIBLE feature type.
	//   "SEV_LIVE_MIGRATABLE" - SEV_LIVE_MIGRATABLE feature type.
	//   "SEV_SNP_CAPABLE" - SEV_SNP_CAPABLE feature type.
	//   "TDX_CAPABLE" - TDX_CAPABLE feature type.
	//   "IDPF" - IDPF feature type.
	//   "SEV_LIVE_MIGRATABLE_V2" - SEV_LIVE_MIGRATABLE_V2 feature type.
	Type string `json:"type,omitempty"`
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

GuestOsFeature: Feature type of the Guest OS.

func (GuestOsFeature) MarshalJSON ¶
added in v0.188.0
func (s GuestOsFeature) MarshalJSON() ([]byte, error)
type InitializeParams ¶
added in v0.188.0
type InitializeParams struct {
	// DiskName: Optional. Specifies the disk name. If not specified, the default
	// is to use the name of the instance.
	DiskName string `json:"diskName,omitempty"`
	// ReplicaZones: Optional. URL of the zone where the disk should be created.
	// Required for each regional disk associated with the instance.
	ReplicaZones []string `json:"replicaZones,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DiskName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiskName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InitializeParams: Specifies the parameters to initialize this disk.

func (InitializeParams) MarshalJSON ¶
added in v0.188.0
func (s InitializeParams) MarshalJSON() ([]byte, error)
type InitializeServiceRequest ¶
added in v0.212.0
type InitializeServiceRequest struct {
	// CloudSqlInstanceInitializationConfig: Optional. The configuration for
	// initializing a Cloud SQL instance.
	CloudSqlInstanceInitializationConfig *CloudSqlInstanceInitializationConfig `json:"cloudSqlInstanceInitializationConfig,omitempty"`
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
	// ResourceType: Required. The resource type to which the default service
	// config will be applied. Examples include, "compute.googleapis.com/Instance"
	// and "storage.googleapis.com/Bucket".
	ResourceType string `json:"resourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "CloudSqlInstanceInitializationConfig") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "CloudSqlInstanceInitializationConfig") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

InitializeServiceRequest: Request message for initializing the service.

func (InitializeServiceRequest) MarshalJSON ¶
added in v0.212.0
func (s InitializeServiceRequest) MarshalJSON() ([]byte, error)
type InitiateBackupRequest ¶
added in v0.188.0
type InitiateBackupRequest struct {
	// BackupId: Required. Resource ID of the Backup resource.
	BackupId string `json:"backupId,omitempty"`
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

InitiateBackupRequest: request message for InitiateBackup.

func (InitiateBackupRequest) MarshalJSON ¶
added in v0.188.0
func (s InitiateBackupRequest) MarshalJSON() ([]byte, error)
type InitiateBackupResponse ¶
added in v0.188.0
type InitiateBackupResponse struct {
	// Backup: The name of the backup that was created.
	Backup string `json:"backup,omitempty"`
	// BaseBackupGenerationId: The generation id of the base backup. It is needed
	// for the incremental backups.
	BaseBackupGenerationId int64 `json:"baseBackupGenerationId,omitempty"`
	// NewBackupGenerationId: The generation id of the new backup.
	NewBackupGenerationId int64 `json:"newBackupGenerationId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

InitiateBackupResponse: Response message for InitiateBackup.

func (InitiateBackupResponse) MarshalJSON ¶
added in v0.188.0
func (s InitiateBackupResponse) MarshalJSON() ([]byte, error)
type InstanceParams ¶
added in v0.192.0
type InstanceParams struct {
	// ResourceManagerTags: Optional. Resource manager tags to be bound to the
	// instance.
	ResourceManagerTags map[string]string `json:"resourceManagerTags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ResourceManagerTags") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ResourceManagerTags") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstanceParams: Additional instance params.

func (InstanceParams) MarshalJSON ¶
added in v0.192.0
func (s InstanceParams) MarshalJSON() ([]byte, error)
type ListBackupPlanAssociationsResponse ¶
added in v0.192.0
type ListBackupPlanAssociationsResponse struct {
	// BackupPlanAssociations: The list of Backup Plan Associations in the project
	// for the specified location. If the `{location}` value in the request is "-",
	// the response contains a list of instances from all locations. In case any
	// location is unreachable, the response will only return backup plan
	// associations in reachable locations and the 'unreachable' field will be
	// populated with a list of unreachable locations.
	BackupPlanAssociations []*BackupPlanAssociation `json:"backupPlanAssociations,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupPlanAssociations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlanAssociations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBackupPlanAssociationsResponse: Response message for List BackupPlanAssociation

func (ListBackupPlanAssociationsResponse) MarshalJSON ¶
added in v0.192.0
func (s ListBackupPlanAssociationsResponse) MarshalJSON() ([]byte, error)
type ListBackupPlanRevisionsResponse ¶
added in v0.237.0
type ListBackupPlanRevisionsResponse struct {
	// BackupPlanRevisions: The list of `BackupPlanRevisions` in the project for
	// the specified location. If the `{location}` value in the request is "-", the
	// response contains a list of resources from all locations. In case any
	// location is unreachable, the response will only return backup plans in
	// reachable locations and the 'unreachable' field will be populated with a
	// list of unreachable locations.
	BackupPlanRevisions []*BackupPlanRevision `json:"backupPlanRevisions,omitempty"`
	// NextPageToken: A token which may be sent as page_token in a subsequent
	// `ListBackupPlanRevisions` call to retrieve the next page of results. If this
	// field is omitted or empty, then there are no more results to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupPlanRevisions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlanRevisions") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBackupPlanRevisionsResponse: The response message for getting a list of `BackupPlanRevision`.

func (ListBackupPlanRevisionsResponse) MarshalJSON ¶
added in v0.237.0
func (s ListBackupPlanRevisionsResponse) MarshalJSON() ([]byte, error)
type ListBackupPlansResponse ¶
added in v0.192.0
type ListBackupPlansResponse struct {
	// BackupPlans: The list of `BackupPlans` in the project for the specified
	// location. If the `{location}` value in the request is "-", the response
	// contains a list of resources from all locations. In case any location is
	// unreachable, the response will only return backup plans in reachable
	// locations and the 'unreachable' field will be populated with a list of
	// unreachable locations. BackupPlan
	BackupPlans []*BackupPlan `json:"backupPlans,omitempty"`
	// NextPageToken: A token which may be sent as page_token in a subsequent
	// `ListBackupPlans` call to retrieve the next page of results. If this field
	// is omitted or empty, then there are no more results to return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupPlans") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupPlans") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBackupPlansResponse: The response message for getting a list of `BackupPlan`.

func (ListBackupPlansResponse) MarshalJSON ¶
added in v0.192.0
func (s ListBackupPlansResponse) MarshalJSON() ([]byte, error)
type ListBackupVaultsResponse ¶
added in v0.188.0
type ListBackupVaultsResponse struct {
	// BackupVaults: The list of BackupVault instances in the project for the
	// specified location. If the '{location}' value in the request is "-", the
	// response contains a list of instances from all locations. In case any
	// location is unreachable, the response will only return backup vaults in
	// reachable locations and the 'unreachable' field will be populated with a
	// list of unreachable locations.
	BackupVaults []*BackupVault `json:"backupVaults,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BackupVaults") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupVaults") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBackupVaultsResponse: Response message for listing BackupVaults.

func (ListBackupVaultsResponse) MarshalJSON ¶
added in v0.188.0
func (s ListBackupVaultsResponse) MarshalJSON() ([]byte, error)
type ListBackupsResponse ¶
added in v0.188.0
type ListBackupsResponse struct {
	// Backups: The list of Backup instances in the project for the specified
	// location. If the '{location}' value in the request is "-", the response
	// contains a list of instances from all locations. In case any location is
	// unreachable, the response will only return data sources in reachable
	// locations and the 'unreachable' field will be populated with a list of
	// unreachable locations.
	Backups []*Backup `json:"backups,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

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

ListBackupsResponse: Response message for listing Backups.

func (ListBackupsResponse) MarshalJSON ¶
added in v0.188.0
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListDataSourceReferencesResponse ¶
added in v0.254.0
type ListDataSourceReferencesResponse struct {
	// DataSourceReferences: The DataSourceReferences from the specified parent.
	DataSourceReferences []*DataSourceReference `json:"dataSourceReferences,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataSourceReferences") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataSourceReferences") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDataSourceReferencesResponse: Response for the ListDataSourceReferences method.

func (ListDataSourceReferencesResponse) MarshalJSON ¶
added in v0.254.0
func (s ListDataSourceReferencesResponse) MarshalJSON() ([]byte, error)
type ListDataSourcesResponse ¶
added in v0.188.0
type ListDataSourcesResponse struct {
	// DataSources: The list of DataSource instances in the project for the
	// specified location. If the '{location}' value in the request is "-", the
	// response contains a list of instances from all locations. In case any
	// location is unreachable, the response will only return data sources in
	// reachable locations and the 'unreachable' field will be populated with a
	// list of unreachable locations.
	DataSources []*DataSource `json:"dataSources,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataSources") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataSources") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDataSourcesResponse: Response message for listing DataSources.

func (ListDataSourcesResponse) MarshalJSON ¶
added in v0.188.0
func (s ListDataSourcesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse ¶
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
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListManagementServersResponse ¶
type ListManagementServersResponse struct {
	// ManagementServers: The list of ManagementServer instances in the project for
	// the specified location. If the '{location}' value in the request is "-", the
	// response contains a list of instances from all locations. In case any
	// location is unreachable, the response will only return management servers in
	// reachable locations and the 'unreachable' field will be populated with a
	// list of unreachable locations.
	ManagementServers []*ManagementServer `json:"managementServers,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ManagementServers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagementServers") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListManagementServersResponse: Response message for listing management servers.

func (ListManagementServersResponse) MarshalJSON ¶
func (s ListManagementServersResponse) MarshalJSON() ([]byte, error)
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
type ListResourceBackupConfigsResponse ¶
added in v0.220.0
type ListResourceBackupConfigsResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// ResourceBackupConfigs: The list of ResourceBackupConfigs for the specified
	// scope.
	ResourceBackupConfigs []*ResourceBackupConfig `json:"resourceBackupConfigs,omitempty"`

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

ListResourceBackupConfigsResponse: Response for ListResourceBackupConfigs.

func (ListResourceBackupConfigsResponse) MarshalJSON ¶
added in v0.220.0
func (s ListResourceBackupConfigsResponse) MarshalJSON() ([]byte, error)
type Location ¶
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

Location: A resource that represents a Google Cloud location.

func (Location) MarshalJSON ¶
func (s Location) MarshalJSON() ([]byte, error)
type LocationMetadata ¶
added in v0.247.0
type LocationMetadata struct {
	// Possible values:
	//   "FEATURE_UNSPECIFIED"
	//   "MANAGEMENT_SERVER"
	//   "COMPUTE_INSTANCE"
	//   "PROTECTION_SUMMARY"
	UnsupportedFeatures []string `json:"unsupportedFeatures,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UnsupportedFeatures") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UnsupportedFeatures") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (LocationMetadata) MarshalJSON ¶
added in v0.247.0
func (s LocationMetadata) MarshalJSON() ([]byte, error)
type ManagementServer ¶
type ManagementServer struct {
	// BaProxyUri: Output only. The hostname or ip address of the exposed AGM
	// endpoints, used by BAs to connect to BA proxy.
	BaProxyUri []string `json:"baProxyUri,omitempty"`
	// CreateTime: Output only. The time when the instance was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. The description of the ManagementServer instance
	// (2048 characters or less).
	Description string `json:"description,omitempty"`
	// Etag: Optional. Server specified ETag for the ManagementServer resource to
	// prevent simultaneous updates from overwiting each other.
	Etag string `json:"etag,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	// Labels currently defined: 1. migrate_from_go= If set to true, the MS is
	// created in migration ready mode.
	Labels map[string]string `json:"labels,omitempty"`
	// ManagementUri: Output only. The hostname or ip address of the exposed AGM
	// endpoints, used by clients to connect to AGM/RD graphical user interface and
	// APIs.
	ManagementUri *ManagementURI `json:"managementUri,omitempty"`
	// Name: Output only. Identifier. The resource name.
	Name string `json:"name,omitempty"`
	// Networks: Optional. VPC networks to which the ManagementServer instance is
	// connected. For this version, only a single network is supported. This field
	// is optional if MS is created without PSA
	Networks []*NetworkConfig `json:"networks,omitempty"`
	// Oauth2ClientId: Output only. The OAuth 2.0 client id is required to make API
	// calls to the Backup and DR instance API of this ManagementServer. This is
	// the value that should be provided in the 'aud' field of the OIDC ID Token
	// (see openid specification
	// https://openid.net/specs/openid-connect-core-1_0.html#IDToken).
	Oauth2ClientId string `json:"oauth2ClientId,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// State: Output only. The ManagementServer state.
	//
	// Possible values:
	//   "INSTANCE_STATE_UNSPECIFIED" - State not set.
	//   "CREATING" - The instance is being created.
	//   "READY" - The instance has been created and is fully usable.
	//   "UPDATING" - The instance configuration is being updated. Certain kinds of
	// updates may cause the instance to become unusable while the update is in
	// progress.
	//   "DELETING" - The instance is being deleted.
	//   "REPAIRING" - The instance is being repaired and may be unstable.
	//   "MAINTENANCE" - Maintenance is being performed on this instance.
	//   "ERROR" - The instance is experiencing an issue and might be unusable. You
	// can get further details from the statusMessage field of Instance resource.
	State string `json:"state,omitempty"`
	// Type: Optional. The type of the ManagementServer resource.
	//
	// Possible values:
	//   "INSTANCE_TYPE_UNSPECIFIED" - Instance type is not mentioned.
	//   "BACKUP_RESTORE" - Instance for backup and restore management (i.e., AGM).
	Type string `json:"type,omitempty"`
	// UpdateTime: Output only. The time when the instance was updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// WorkforceIdentityBasedManagementUri: Output only. The hostnames of the
	// exposed AGM endpoints for both types of user i.e. 1p and 3p, used to connect
	// AGM/RM UI.
	WorkforceIdentityBasedManagementUri *WorkforceIdentityBasedManagementURI `json:"workforceIdentityBasedManagementUri,omitempty"`
	// WorkforceIdentityBasedOauth2ClientId: Output only. The OAuth client IDs for
	// both types of user i.e. 1p and 3p.
	WorkforceIdentityBasedOauth2ClientId *WorkforceIdentityBasedOAuth2ClientID `json:"workforceIdentityBasedOauth2ClientId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BaProxyUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BaProxyUri") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagementServer: ManagementServer describes a single BackupDR ManagementServer instance.

func (ManagementServer) MarshalJSON ¶
func (s ManagementServer) MarshalJSON() ([]byte, error)
type ManagementURI ¶
type ManagementURI struct {
	// Api: Output only. The ManagementServer AGM/RD API URL.
	Api string `json:"api,omitempty"`
	// WebUi: Output only. The ManagementServer AGM/RD WebUI URL.
	WebUi string `json:"webUi,omitempty"`
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

ManagementURI: ManagementURI for the Management Server resource.

func (ManagementURI) MarshalJSON ¶
func (s ManagementURI) MarshalJSON() ([]byte, error)
type Metadata ¶
added in v0.188.0
type Metadata struct {
	// Items: Optional. Array of key/value pairs. The total size of all keys and
	// values must be less than 512 KB.
	Items []*Entry `json:"items,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Metadata: A metadata key/value entry.

func (Metadata) MarshalJSON ¶
added in v0.188.0
func (s Metadata) MarshalJSON() ([]byte, error)
type NetworkConfig ¶
type NetworkConfig struct {
	// Network: Optional. The resource name of the Google Compute Engine VPC
	// network to which the ManagementServer instance is connected.
	Network string `json:"network,omitempty"`
	// PeeringMode: Optional. The network connect mode of the ManagementServer
	// instance. For this version, only PRIVATE_SERVICE_ACCESS is supported.
	//
	// Possible values:
	//   "PEERING_MODE_UNSPECIFIED" - Peering mode not set.
	//   "PRIVATE_SERVICE_ACCESS" - Connect using Private Service Access to the
	// Management Server. Private services access provides an IP address range for
	// multiple Google Cloud services, including Google Cloud Backup and DR.
	PeeringMode string `json:"peeringMode,omitempty"`
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

NetworkConfig: Network configuration for ManagementServer instance.

func (NetworkConfig) MarshalJSON ¶
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type NetworkInterface ¶
added in v0.188.0
type NetworkInterface struct {
	// AccessConfigs: Optional. An array of configurations for this interface.
	// Currently, only one access config,ONE_TO_ONE_NAT is supported. If there are
	// no accessConfigs specified, then this instance will have no external
	// internet access.
	AccessConfigs []*AccessConfig `json:"accessConfigs,omitempty"`
	// AliasIpRanges: Optional. An array of alias IP ranges for this network
	// interface. You can only specify this field for network interfaces in VPC
	// networks.
	AliasIpRanges []*AliasIpRange `json:"aliasIpRanges,omitempty"`
	// InternalIpv6PrefixLength: Optional. The prefix length of the primary
	// internal IPv6 range.
	InternalIpv6PrefixLength int64 `json:"internalIpv6PrefixLength,omitempty"`
	// Ipv6AccessConfigs: Optional. An array of IPv6 access configurations for this
	// interface. Currently, only one IPv6 access config, DIRECT_IPV6, is
	// supported. If there is no ipv6AccessConfig specified, then this instance
	// will have no external IPv6 Internet access.
	Ipv6AccessConfigs []*AccessConfig `json:"ipv6AccessConfigs,omitempty"`
	// Ipv6AccessType: Optional. [Output Only] One of EXTERNAL, INTERNAL to
	// indicate whether the IP can be accessed from the Internet. This field is
	// always inherited from its subnetwork.
	//
	// Possible values:
	//   "UNSPECIFIED_IPV6_ACCESS_TYPE" - IPv6 access type not set. Means this
	// network interface hasn't been turned on IPv6 yet.
	//   "INTERNAL" - This network interface can have internal IPv6.
	//   "EXTERNAL" - This network interface can have external IPv6.
	Ipv6AccessType string `json:"ipv6AccessType,omitempty"`
	// Ipv6Address: Optional. An IPv6 internal network address for this network
	// interface. To use a static internal IP address, it must be unused and in the
	// same region as the instance's zone. If not specified, Google Cloud will
	// automatically assign an internal IPv6 address from the instance's
	// subnetwork.
	Ipv6Address string `json:"ipv6Address,omitempty"`
	// Name: Output only. [Output Only] The name of the network interface, which is
	// generated by the server.
	Name string `json:"name,omitempty"`
	// Network: Optional. URL of the VPC network resource for this instance.
	Network string `json:"network,omitempty"`
	// NetworkAttachment: Optional. The URL of the network attachment that this
	// interface should connect to in the following format:
	// projects/{project_number}/regions/{region_name}/networkAttachments/{network_a
	// ttachment_name}.
	NetworkAttachment string `json:"networkAttachment,omitempty"`
	// NetworkIP: Optional. An IPv4 internal IP address to assign to the instance
	// for this network interface. If not specified by the user, an unused internal
	// IP is assigned by the system.
	NetworkIP string `json:"networkIP,omitempty"`
	// NicType: Optional. The type of vNIC to be used on this interface. This may
	// be gVNIC or VirtioNet.
	//
	// Possible values:
	//   "NIC_TYPE_UNSPECIFIED" - Default should be NIC_TYPE_UNSPECIFIED.
	//   "VIRTIO_NET" - VIRTIO
	//   "GVNIC" - GVNIC
	NicType string `json:"nicType,omitempty"`
	// QueueCount: Optional. The networking queue count that's specified by users
	// for the network interface. Both Rx and Tx queues will be set to this number.
	// It'll be empty if not specified by the users.
	QueueCount int64 `json:"queueCount,omitempty"`
	// StackType: The stack type for this network interface.
	//
	// Possible values:
	//   "STACK_TYPE_UNSPECIFIED" - Default should be STACK_TYPE_UNSPECIFIED.
	//   "IPV4_ONLY" - The network interface will be assigned IPv4 address.
	//   "IPV4_IPV6" - The network interface can have both IPv4 and IPv6 addresses.
	StackType string `json:"stackType,omitempty"`
	// Subnetwork: Optional. The URL of the Subnetwork resource for this instance.
	Subnetwork string `json:"subnetwork,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessConfigs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkInterface: A network interface resource attached to an instance. s

func (NetworkInterface) MarshalJSON ¶
added in v0.188.0
func (s NetworkInterface) MarshalJSON() ([]byte, error)
type NetworkPerformanceConfig ¶
added in v0.192.0
type NetworkPerformanceConfig struct {
	// TotalEgressBandwidthTier: Optional. The tier of the total egress bandwidth.
	//
	// Possible values:
	//   "TIER_UNSPECIFIED" - This value is unused.
	//   "DEFAULT" - Default network performance config.
	//   "TIER_1" - Tier 1 network performance config.
	TotalEgressBandwidthTier string `json:"totalEgressBandwidthTier,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TotalEgressBandwidthTier")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TotalEgressBandwidthTier") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkPerformanceConfig: Network performance configuration.

func (NetworkPerformanceConfig) MarshalJSON ¶
added in v0.192.0
func (s NetworkPerformanceConfig) MarshalJSON() ([]byte, error)
type NodeAffinity ¶
added in v0.188.0
type NodeAffinity struct {
	// Key: Optional. Corresponds to the label key of Node resource.
	Key string `json:"key,omitempty"`
	// Operator: Optional. Defines the operation of node selection.
	//
	// Possible values:
	//   "OPERATOR_UNSPECIFIED" - Default value. This value is unused.
	//   "IN" - Requires Compute Engine to seek for matched nodes.
	//   "NOT_IN" - Requires Compute Engine to avoid certain nodes.
	Operator string `json:"operator,omitempty"`
	// Values: Optional. Corresponds to the label values of Node resource.
	Values []string `json:"values,omitempty"`
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

NodeAffinity: Node Affinity: the configuration of desired nodes onto which this Instance could be scheduled.

func (NodeAffinity) MarshalJSON ¶
added in v0.188.0
func (s NodeAffinity) MarshalJSON() ([]byte, error)
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
type OperationMetadata ¶
type OperationMetadata struct {
	// AdditionalInfo: Output only. AdditionalInfo contains additional Info related
	// to backup plan association resource.
	AdditionalInfo map[string]string `json:"additionalInfo,omitempty"`
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of 1, corresponding to 'Code.CANCELLED'.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdditionalInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalInfo") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperationMetadata: Represents the metadata of the long-running operation.

func (OperationMetadata) MarshalJSON ¶
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type PitrSettings ¶
added in v0.220.0
type PitrSettings struct {
	// RetentionDays: Output only. Number of days to retain the backup.
	RetentionDays int64 `json:"retentionDays,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RetentionDays") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RetentionDays") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PitrSettings: Point in time recovery settings of the backup configuration resource.

func (PitrSettings) MarshalJSON ¶
added in v0.220.0
func (s PitrSettings) MarshalJSON() ([]byte, error)
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
type ProjectsLocationsBackupPlanAssociationsCreateCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsCreateCall) BackupPlanAssociationId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) BackupPlanAssociationId(backupPlanAssociationId string) *ProjectsLocationsBackupPlanAssociationsCreateCall

BackupPlanAssociationId sets the optional parameter "backupPlanAssociationId": Required. The name of the backup plan association to create. The name must be unique for the specified project and location.

func (*ProjectsLocationsBackupPlanAssociationsCreateCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsCreateCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsCreateCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsCreateCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsCreateCall) RequestId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsBackupPlanAssociationsDeleteCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsDeleteCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsDeleteCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsDeleteCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsDeleteCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsDeleteCall) RequestId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall ¶
added in v0.241.0
type ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Context ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Do ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchBackupPlanAssociationsForResourceTypeResponse, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.fetchForResourceType" call. Any non-2xx status code is an error. Response headers are in either *FetchBackupPlanAssociationsForResourceTypeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Fields ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Filter ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

Filter sets the optional parameter "filter": A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: * resource * backup_plan * state * data_source * cloud_sql_instance_backup_plan_association_properties.instance_create_time

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Header ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) IfNoneMatch ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) OrderBy ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * name

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageSize ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

PageSize sets the optional parameter "pageSize": The maximum number of BackupPlanAssociations to return. The service may return fewer than this value. If unspecified, at most 50 BackupPlanAssociations will be returned. The maximum value is 100; values above 100 will be coerced to 100.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageToken ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous call of `FetchBackupPlanAssociationsForResourceType`. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `FetchBackupPlanAssociationsForResourceType` must match the call that provided the page token.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Pages ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) Pages(ctx context.Context, f func(*FetchBackupPlanAssociationsForResourceTypeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) ResourceType ¶
added in v0.241.0
func (c *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

ResourceType sets the optional parameter "resourceType": Required. The type of the Google Cloud resource. Ex: sql.googleapis.com/Instance

type ProjectsLocationsBackupPlanAssociationsGetCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsGetCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsGetCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Do(opts ...googleapi.CallOption) (*BackupPlanAssociation, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.get" call. Any non-2xx status code is an error. Response headers are in either *BackupPlanAssociation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsGetCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsGetCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsGetCall) IfNoneMatch ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsBackupPlanAssociationsListCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsListCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsListCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlanAssociationsResponse, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupPlanAssociationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsListCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsListCall) Filter ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Filter(filter string) *ProjectsLocationsBackupPlanAssociationsListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsBackupPlanAssociationsListCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsListCall) IfNoneMatch ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlanAssociationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupPlanAssociationsListCall) PageSize ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlanAssociationsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupPlanAssociationsListCall) PageToken ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlanAssociationsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupPlanAssociationsListCall) Pages ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsListCall) Pages(ctx context.Context, f func(*ListBackupPlanAssociationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsBackupPlanAssociationsPatchCall ¶
added in v0.234.0
type ProjectsLocationsBackupPlanAssociationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsPatchCall) Context ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsPatchCall) Do ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsPatchCall) Fields ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsPatchCall) Header ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlanAssociationsPatchCall) RequestId ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupPlanAssociationsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupPlanAssociationsPatchCall) UpdateMask ¶
added in v0.234.0
func (c *ProjectsLocationsBackupPlanAssociationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupPlanAssociationsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlanAssociation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently backup_plan_association.backup_plan is the only supported field.

type ProjectsLocationsBackupPlanAssociationsService ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupPlanAssociationsService ¶
added in v0.192.0
func NewProjectsLocationsBackupPlanAssociationsService(s *Service) *ProjectsLocationsBackupPlanAssociationsService
func (*ProjectsLocationsBackupPlanAssociationsService) Create ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlanAssociationsService) Create(parent string, backupplanassociation *BackupPlanAssociation) *ProjectsLocationsBackupPlanAssociationsCreateCall

Create: Create a BackupPlanAssociation

parent: The backup plan association project and location in the format `projects/{project_id}/locations/{location}`. In Backup and DR locations map to Google Cloud regions, for example **us-central1**.
func (*ProjectsLocationsBackupPlanAssociationsService) Delete ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlanAssociationsService) Delete(name string) *ProjectsLocationsBackupPlanAssociationsDeleteCall

Delete: Deletes a single BackupPlanAssociation.

name: Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlan AssociationId}`.
func (*ProjectsLocationsBackupPlanAssociationsService) FetchForResourceType ¶
added in v0.241.0
func (r *ProjectsLocationsBackupPlanAssociationsService) FetchForResourceType(parent string) *ProjectsLocationsBackupPlanAssociationsFetchForResourceTypeCall

FetchForResourceType: List BackupPlanAssociations for a given resource type.

parent: The parent resource name. Format: projects/{project}/locations/{location}.
func (*ProjectsLocationsBackupPlanAssociationsService) Get ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlanAssociationsService) Get(name string) *ProjectsLocationsBackupPlanAssociationsGetCall

Get: Gets details of a single BackupPlanAssociation.

name: Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlan AssociationId}`.
func (*ProjectsLocationsBackupPlanAssociationsService) List ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlanAssociationsService) List(parent string) *ProjectsLocationsBackupPlanAssociationsListCall

List: Lists BackupPlanAssociations in a given project and location.

parent: The project and location for which to retrieve backup Plan Associations information, in the format `projects/{project_id}/locations/{location}`. In Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backup plan associations for all locations, use "-" for the `{location}` value.
func (*ProjectsLocationsBackupPlanAssociationsService) Patch ¶
added in v0.234.0
func (r *ProjectsLocationsBackupPlanAssociationsService) Patch(name string, backupplanassociation *BackupPlanAssociation) *ProjectsLocationsBackupPlanAssociationsPatchCall

Patch: Update a BackupPlanAssociation.

name: Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanA ssociationId}.
func (*ProjectsLocationsBackupPlanAssociationsService) TriggerBackup ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlanAssociationsService) TriggerBackup(name string, triggerbackuprequest *TriggerBackupRequest) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall

TriggerBackup: Triggers a new Backup.

name: Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlan AssociationId}`.
type ProjectsLocationsBackupPlanAssociationsTriggerBackupCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlanAssociationsTriggerBackupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlanAssociations.triggerBackup" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlanAssociationsTriggerBackupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupPlansCreateCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlansCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansCreateCall) BackupPlanId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) BackupPlanId(backupPlanId string) *ProjectsLocationsBackupPlansCreateCall

BackupPlanId sets the optional parameter "backupPlanId": Required. The name of the `BackupPlan` to create. The name must be unique for the specified project and location.The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /a-z{,62}/.

func (*ProjectsLocationsBackupPlansCreateCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansCreateCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlans.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansCreateCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansCreateCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansCreateCall) RequestId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansCreateCall) RequestId(requestId string) *ProjectsLocationsBackupPlansCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsBackupPlansDeleteCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlansDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansDeleteCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansDeleteCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlans.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansDeleteCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansDeleteCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansDeleteCall) RequestId ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupPlansDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsBackupPlansGetCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlansGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansGetCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansGetCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansGetCall) Do(opts ...googleapi.CallOption) (*BackupPlan, error)

Do executes the "backupdr.projects.locations.backupPlans.get" call. Any non-2xx status code is an error. Response headers are in either *BackupPlan.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansGetCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansGetCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansGetCall) IfNoneMatch ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsBackupPlansListCall ¶
added in v0.192.0
type ProjectsLocationsBackupPlansListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansListCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansListCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlansResponse, error)

Do executes the "backupdr.projects.locations.backupPlans.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupPlansResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansListCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansListCall) Filter ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Filter(filter string) *ProjectsLocationsBackupPlansListCall

Filter sets the optional parameter "filter": Field match expression used to filter the results.

func (*ProjectsLocationsBackupPlansListCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansListCall) IfNoneMatch ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupPlansListCall) OrderBy ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) OrderBy(orderBy string) *ProjectsLocationsBackupPlansListCall

OrderBy sets the optional parameter "orderBy": Field by which to sort the results.

func (*ProjectsLocationsBackupPlansListCall) PageSize ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlansListCall

PageSize sets the optional parameter "pageSize": The maximum number of `BackupPlans` to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsBackupPlansListCall) PageToken ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlansListCall

PageToken sets the optional parameter "pageToken": The value of next_page_token received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token.

func (*ProjectsLocationsBackupPlansListCall) Pages ¶
added in v0.192.0
func (c *ProjectsLocationsBackupPlansListCall) Pages(ctx context.Context, f func(*ListBackupPlansResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsBackupPlansPatchCall ¶
added in v0.237.0
type ProjectsLocationsBackupPlansPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansPatchCall) Context ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansPatchCall) Do ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupPlans.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansPatchCall) Fields ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansPatchCall) Header ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansPatchCall) RequestId ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) RequestId(requestId string) *ProjectsLocationsBackupPlansPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupPlansPatchCall) UpdateMask ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupPlansPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlan resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently, these fields are supported in update: description, schedules, retention period, adding and removing Backup Rules.

type ProjectsLocationsBackupPlansRevisionsGetCall ¶
added in v0.237.0
type ProjectsLocationsBackupPlansRevisionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansRevisionsGetCall) Context ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansRevisionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansRevisionsGetCall) Do ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Do(opts ...googleapi.CallOption) (*BackupPlanRevision, error)

Do executes the "backupdr.projects.locations.backupPlans.revisions.get" call. Any non-2xx status code is an error. Response headers are in either *BackupPlanRevision.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansRevisionsGetCall) Fields ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansRevisionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansRevisionsGetCall) Header ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansRevisionsGetCall) IfNoneMatch ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansRevisionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsBackupPlansRevisionsListCall ¶
added in v0.237.0
type ProjectsLocationsBackupPlansRevisionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupPlansRevisionsListCall) Context ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Context(ctx context.Context) *ProjectsLocationsBackupPlansRevisionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupPlansRevisionsListCall) Do ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Do(opts ...googleapi.CallOption) (*ListBackupPlanRevisionsResponse, error)

Do executes the "backupdr.projects.locations.backupPlans.revisions.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupPlanRevisionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupPlansRevisionsListCall) Fields ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupPlansRevisionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupPlansRevisionsListCall) Header ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupPlansRevisionsListCall) IfNoneMatch ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupPlansRevisionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupPlansRevisionsListCall) PageSize ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupPlansRevisionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of `BackupPlans` to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsBackupPlansRevisionsListCall) PageToken ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) PageToken(pageToken string) *ProjectsLocationsBackupPlansRevisionsListCall

PageToken sets the optional parameter "pageToken": The value of next_page_token received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token.

func (*ProjectsLocationsBackupPlansRevisionsListCall) Pages ¶
added in v0.237.0
func (c *ProjectsLocationsBackupPlansRevisionsListCall) Pages(ctx context.Context, f func(*ListBackupPlanRevisionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsBackupPlansRevisionsService ¶
added in v0.237.0
type ProjectsLocationsBackupPlansRevisionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupPlansRevisionsService ¶
added in v0.237.0
func NewProjectsLocationsBackupPlansRevisionsService(s *Service) *ProjectsLocationsBackupPlansRevisionsService
func (*ProjectsLocationsBackupPlansRevisionsService) Get ¶
added in v0.237.0
func (r *ProjectsLocationsBackupPlansRevisionsService) Get(name string) *ProjectsLocationsBackupPlansRevisionsGetCall

Get: Gets details of a single BackupPlanRevision.

name: The resource name of the `BackupPlanRevision` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revision s/{revision}`.
func (*ProjectsLocationsBackupPlansRevisionsService) List ¶
added in v0.237.0
func (r *ProjectsLocationsBackupPlansRevisionsService) List(parent string) *ProjectsLocationsBackupPlansRevisionsListCall

List: Lists BackupPlanRevisions in a given project and location.

parent: The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**.
type ProjectsLocationsBackupPlansService ¶
added in v0.192.0
type ProjectsLocationsBackupPlansService struct {
	Revisions *ProjectsLocationsBackupPlansRevisionsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupPlansService ¶
added in v0.192.0
func NewProjectsLocationsBackupPlansService(s *Service) *ProjectsLocationsBackupPlansService
func (*ProjectsLocationsBackupPlansService) Create ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlansService) Create(parent string, backupplan *BackupPlan) *ProjectsLocationsBackupPlansCreateCall

Create: Create a BackupPlan

parent: The `BackupPlan` project and location in the format `projects/{project}/locations/{location}`. In Google Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**.
func (*ProjectsLocationsBackupPlansService) Delete ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlansService) Delete(name string) *ProjectsLocationsBackupPlansDeleteCall

Delete: Deletes a single BackupPlan.

name: The resource name of the `BackupPlan` to delete. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`.
func (*ProjectsLocationsBackupPlansService) Get ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlansService) Get(name string) *ProjectsLocationsBackupPlansGetCall

Get: Gets details of a single BackupPlan.

name: The resource name of the `BackupPlan` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`.
func (*ProjectsLocationsBackupPlansService) List ¶
added in v0.192.0
func (r *ProjectsLocationsBackupPlansService) List(parent string) *ProjectsLocationsBackupPlansListCall

List: Lists BackupPlans in a given project and location.

parent: The project and location for which to retrieve `BackupPlans` information. Format: `projects/{project}/locations/{location}`. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backup plans for all locations, use "-" for the `{location}` value.
func (*ProjectsLocationsBackupPlansService) Patch ¶
added in v0.237.0
func (r *ProjectsLocationsBackupPlansService) Patch(name string, backupplan *BackupPlan) *ProjectsLocationsBackupPlansPatchCall

Patch: Update a BackupPlan.

name: Output only. Identifier. The resource name of the `BackupPlan`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`.
type ProjectsLocationsBackupVaultsCreateCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsCreateCall) BackupVaultId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) BackupVaultId(backupVaultId string) *ProjectsLocationsBackupVaultsCreateCall

BackupVaultId sets the optional parameter "backupVaultId": Required. ID of the requesting object If auto-generating ID server-side, remove this field and backup_vault_id from the method_signature of Create RPC

func (*ProjectsLocationsBackupVaultsCreateCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsCreateCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsCreateCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsCreateCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsCreateCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupVaultsCreateCall) ValidateOnly ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsCreateCall

ValidateOnly sets the optional parameter "validateOnly": Only validate the request, but do not perform mutations. The default is 'false'.

type ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.abandonBackup" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall ¶
added in v0.254.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Context ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Do ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchBackupsForResourceTypeResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.fetchForResourceType" call. Any non-2xx status code is an error. Response headers are in either *FetchBackupsForResourceTypeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Fields ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Filter ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

Filter sets the optional parameter "filter": A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: * name * state * backup_type * create_time * expire_time * enforced_retention_end_time * gcp_backup_plan_info.backup_plan * cloud_sql_instance_backup_properties.instance_tier * cloud_sql_instance_backup_properties.database_installed_version

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Header ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) IfNoneMatch ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) OrderBy ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * name

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageSize ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

PageSize sets the optional parameter "pageSize": The maximum number of Backups to return. The service may return fewer than this value. If unspecified, at most 50 Backups will be returned. The maximum value is 100; values above 100 will be coerced to 100.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageToken ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous call of `FetchBackupsForResourceType`. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `FetchBackupsForResourceType` must match the call that provided the page token.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Pages ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) Pages(ctx context.Context, f func(*FetchBackupsForResourceTypeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) ResourceType ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

ResourceType sets the optional parameter "resourceType": Required. The type of the Google Cloud resource. Ex: sqladmin.googleapis.com/Instance

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) View ¶
added in v0.254.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

View sets the optional parameter "view": This parameter is used to specify the view of the backup. If not specified, the default view is BASIC.

Possible values:

"BACKUP_VIEW_UNSPECIFIED" - If the value is not set, the default 'FULL'


view is used.

"BACKUP_VIEW_BASIC" - Includes basic data about the Backup, but not the


full contents.

"BACKUP_VIEW_FULL" - Includes all data about the Backup. This is the


default value (for both ListBackups and GetBackup).

type ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.get" call. Any non-2xx status code is an error. Response headers are in either *Backup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) View ¶
added in v0.198.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall

View sets the optional parameter "view": Reserved for future use to provide a BASIC & FULL view of Backup resource.

Possible values:

"BACKUP_VIEW_UNSPECIFIED" - If the value is not set, the default 'FULL'


view is used.

"BACKUP_VIEW_BASIC" - Includes basic data about the Backup, but not the


full contents.

"BACKUP_VIEW_FULL" - Includes all data about the Backup. This is the


default value (for both ListBackups and GetBackup).

type ProjectsLocationsBackupVaultsDataSourcesBackupsListCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Filter ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) OrderBy ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageSize ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageToken ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Pages ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) View ¶
added in v0.198.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall) View(view string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

View sets the optional parameter "view": Reserved for future use to provide a BASIC & FULL view of Backup resource.

Possible values:

"BACKUP_VIEW_UNSPECIFIED" - If the value is not set, the default 'FULL'


view is used.

"BACKUP_VIEW_BASIC" - Includes basic data about the Backup, but not the


full contents.

"BACKUP_VIEW_FULL" - Includes all data about the Backup. This is the


default value (for both ListBackups and GetBackup).

type ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) UpdateMask ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.

type ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall ¶
added in v0.192.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Context ¶
added in v0.192.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Do ¶
added in v0.192.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.backups.restore" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Fields ¶
added in v0.192.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Header ¶
added in v0.192.0
func (c *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesBackupsService ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesBackupsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupVaultsDataSourcesBackupsService ¶
added in v0.188.0
func NewProjectsLocationsBackupVaultsDataSourcesBackupsService(s *Service) *ProjectsLocationsBackupVaultsDataSourcesBackupsService
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) Delete ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Delete(name string) *ProjectsLocationsBackupVaultsDataSourcesBackupsDeleteCall

Delete: Deletes a Backup.

- name: Name of the resource.

func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) FetchForResourceType ¶
added in v0.254.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) FetchForResourceType(parent string) *ProjectsLocationsBackupVaultsDataSourcesBackupsFetchForResourceTypeCall

FetchForResourceType: Fetch Backups for a given resource type.

parent: Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSo urces/{datasourceId}.
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) Get ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Get(name string) *ProjectsLocationsBackupVaultsDataSourcesBackupsGetCall

Get: Gets details of a Backup.

name: Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/data Sources/{datasource}/backups/{backup}'.
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) List ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) List(parent string) *ProjectsLocationsBackupVaultsDataSourcesBackupsListCall

List: Lists Backups in a given project and location.

parent: The project and location for which to retrieve backup information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) Patch ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Patch(name string, backup *Backup) *ProjectsLocationsBackupVaultsDataSourcesBackupsPatchCall

Patch: Updates the settings of a Backup.

name: Output only. Identifier. Name of the backup to create. It must have the format"projects//locations//backupVaults//dataSources/{datasource}/backups /{backup}". `{backup}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the datasource.
func (*ProjectsLocationsBackupVaultsDataSourcesBackupsService) Restore ¶
added in v0.192.0
func (r *ProjectsLocationsBackupVaultsDataSourcesBackupsService) Restore(name string, restorebackuprequest *RestoreBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesBackupsRestoreCall

Restore: Restore from a Backup

name: The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.
type ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Do(opts ...googleapi.CallOption) (*FetchAccessTokenResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.fetchAccessToken" call. Any non-2xx status code is an error. Response headers are in either *FetchAccessTokenResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.finalizeBackup" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesGetCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesGetCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesGetCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Do(opts ...googleapi.CallOption) (*DataSource, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.get" call. Any non-2xx status code is an error. Response headers are in either *DataSource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesGetCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesGetCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesGetCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Do(opts ...googleapi.CallOption) (*InitiateBackupResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.initiateBackup" call. Any non-2xx status code is an error. Response headers are in either *InitiateBackupResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesListCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourcesResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.list" call. Any non-2xx status code is an error. Response headers are in either *ListDataSourcesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Filter ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Filter(filter string) *ProjectsLocationsBackupVaultsDataSourcesListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsDataSourcesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) OrderBy ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsDataSourcesListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) PageSize ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsDataSourcesListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) PageToken ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsDataSourcesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupVaultsDataSourcesListCall) Pages ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesListCall) Pages(ctx context.Context, f func(*ListDataSourcesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsBackupVaultsDataSourcesPatchCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) AllowMissing ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

AllowMissing sets the optional parameter "allowMissing": Enable upsert.

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupVaultsDataSourcesPatchCall) UpdateMask ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the DataSource resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.

type ProjectsLocationsBackupVaultsDataSourcesRemoveCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesRemoveCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.remove" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesRemoveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDataSourcesService ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesService struct {
	Backups *ProjectsLocationsBackupVaultsDataSourcesBackupsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupVaultsDataSourcesService ¶
added in v0.188.0
func NewProjectsLocationsBackupVaultsDataSourcesService(s *Service) *ProjectsLocationsBackupVaultsDataSourcesService
func (*ProjectsLocationsBackupVaultsDataSourcesService) AbandonBackup ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) AbandonBackup(dataSource string, abandonbackuprequest *AbandonBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesAbandonBackupCall

AbandonBackup: Internal only. Abandons a backup.

dataSource: The resource name of the instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/'.
func (*ProjectsLocationsBackupVaultsDataSourcesService) FetchAccessToken ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) FetchAccessToken(name string, fetchaccesstokenrequest *FetchAccessTokenRequest) *ProjectsLocationsBackupVaultsDataSourcesFetchAccessTokenCall

FetchAccessToken: Internal only. Fetch access token for a given data source.

name: The resource name for the location for which static IPs should be returned. Must be in the format 'projects/*/locations/*/backupVaults/*/dataSources'.
func (*ProjectsLocationsBackupVaultsDataSourcesService) FinalizeBackup ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) FinalizeBackup(dataSource string, finalizebackuprequest *FinalizeBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesFinalizeBackupCall

FinalizeBackup: Internal only. Finalize a backup that was started by a call to InitiateBackup.

dataSource: The resource name of the instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/'.
func (*ProjectsLocationsBackupVaultsDataSourcesService) Get ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Get(name string) *ProjectsLocationsBackupVaultsDataSourcesGetCall

Get: Gets details of a DataSource.

name: Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/da taSource/{resource_name}'.
func (*ProjectsLocationsBackupVaultsDataSourcesService) InitiateBackup ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) InitiateBackup(dataSource string, initiatebackuprequest *InitiateBackupRequest) *ProjectsLocationsBackupVaultsDataSourcesInitiateBackupCall

InitiateBackup: Internal only. Initiates a backup.

dataSource: The resource name of the instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/'.
func (*ProjectsLocationsBackupVaultsDataSourcesService) List ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) List(parent string) *ProjectsLocationsBackupVaultsDataSourcesListCall

List: Lists DataSources in a given project and location.

parent: The project and location for which to retrieve data sources information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value.
func (*ProjectsLocationsBackupVaultsDataSourcesService) Patch ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Patch(name string, datasource *DataSource) *ProjectsLocationsBackupVaultsDataSourcesPatchCall

Patch: Updates the settings of a DataSource.

name: Output only. Identifier. Name of the datasource to create. It must have the format"projects/{project}/locations/{location}/backupVaults/{backupvault}/ dataSources/{datasource}". `{datasource}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the backup vault.
func (*ProjectsLocationsBackupVaultsDataSourcesService) Remove ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) Remove(name string, removedatasourcerequest *RemoveDataSourceRequest) *ProjectsLocationsBackupVaultsDataSourcesRemoveCall

Remove: Deletes a DataSource. This is a custom method instead of a standard delete method because external clients will not delete DataSources except for BackupDR backup appliances.

- name: Name of the resource.

func (*ProjectsLocationsBackupVaultsDataSourcesService) SetInternalStatus ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsDataSourcesService) SetInternalStatus(dataSource string, setinternalstatusrequest *SetInternalStatusRequest) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall

SetInternalStatus: Sets the internal status of a DataSource.

dataSource: The resource name of the instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/'.
type ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.dataSources.setInternalStatus" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDataSourcesSetInternalStatusCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsBackupVaultsDeleteCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsDeleteCall) AllowMissing ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupVaultsDeleteCall

AllowMissing sets the optional parameter "allowMissing": If true and the BackupVault is not found, the request will succeed but no action will be taken.

func (*ProjectsLocationsBackupVaultsDeleteCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsDeleteCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsDeleteCall) Etag ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Etag(etag string) *ProjectsLocationsBackupVaultsDeleteCall

Etag sets the optional parameter "etag": The current etag of the backup vault. If an etag is provided and does not match the current etag of the connection, deletion will be blocked.

func (*ProjectsLocationsBackupVaultsDeleteCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsDeleteCall) Force ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Force(force bool) *ProjectsLocationsBackupVaultsDeleteCall

Force sets the optional parameter "force": If set to true, any data source from this backup vault will also be deleted.

func (*ProjectsLocationsBackupVaultsDeleteCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsDeleteCall) IgnoreBackupPlanReferences ¶
added in v0.202.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) IgnoreBackupPlanReferences(ignoreBackupPlanReferences bool) *ProjectsLocationsBackupVaultsDeleteCall

IgnoreBackupPlanReferences sets the optional parameter "ignoreBackupPlanReferences": If set to true, backupvault deletion will proceed even if there are backup plans referencing the backupvault. The default is 'false'.

func (*ProjectsLocationsBackupVaultsDeleteCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupVaultsDeleteCall) ValidateOnly ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": Only validate the request, but do not perform mutations. The default is 'false'.

type ProjectsLocationsBackupVaultsFetchUsableCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsFetchUsableCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsFetchUsableCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsFetchUsableCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Do(opts ...googleapi.CallOption) (*FetchUsableBackupVaultsResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.fetchUsable" call. Any non-2xx status code is an error. Response headers are in either *FetchUsableBackupVaultsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsFetchUsableCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) Filter ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Filter(filter string) *ProjectsLocationsBackupVaultsFetchUsableCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsFetchUsableCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) OrderBy ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsFetchUsableCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) PageSize ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsFetchUsableCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) PageToken ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsFetchUsableCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupVaultsFetchUsableCall) Pages ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsFetchUsableCall) Pages(ctx context.Context, f func(*FetchUsableBackupVaultsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsBackupVaultsGetCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsGetCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsGetCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsGetCall) Do(opts ...googleapi.CallOption) (*BackupVault, error)

Do executes the "backupdr.projects.locations.backupVaults.get" call. Any non-2xx status code is an error. Response headers are in either *BackupVault.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsGetCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsGetCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsGetCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsGetCall) View ¶
added in v0.198.0
func (c *ProjectsLocationsBackupVaultsGetCall) View(view string) *ProjectsLocationsBackupVaultsGetCall

View sets the optional parameter "view": Reserved for future use to provide a BASIC & FULL view of Backup Vault

Possible values:

"BACKUP_VAULT_VIEW_UNSPECIFIED" - If the value is not set, the default


'FULL' view is used.

"BACKUP_VAULT_VIEW_BASIC" - Includes basic data about the Backup Vault,


but not the full contents.

"BACKUP_VAULT_VIEW_FULL" - Includes all data about the Backup Vault. This


is the default value (for both ListBackupVaults and GetBackupVault).

type ProjectsLocationsBackupVaultsListCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsListCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsListCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Do(opts ...googleapi.CallOption) (*ListBackupVaultsResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupVaultsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsListCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsListCall) Filter ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Filter(filter string) *ProjectsLocationsBackupVaultsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsBackupVaultsListCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsListCall) IfNoneMatch ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupVaultsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupVaultsListCall) OrderBy ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupVaultsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsBackupVaultsListCall) PageSize ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupVaultsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupVaultsListCall) PageToken ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) PageToken(pageToken string) *ProjectsLocationsBackupVaultsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupVaultsListCall) Pages ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsListCall) Pages(ctx context.Context, f func(*ListBackupVaultsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsBackupVaultsListCall) View ¶
added in v0.198.0
func (c *ProjectsLocationsBackupVaultsListCall) View(view string) *ProjectsLocationsBackupVaultsListCall

View sets the optional parameter "view": Reserved for future use to provide a BASIC & FULL view of Backup Vault.

Possible values:

"BACKUP_VAULT_VIEW_UNSPECIFIED" - If the value is not set, the default


'FULL' view is used.

"BACKUP_VAULT_VIEW_BASIC" - Includes basic data about the Backup Vault,


but not the full contents.

"BACKUP_VAULT_VIEW_FULL" - Includes all data about the Backup Vault. This


is the default value (for both ListBackupVaults and GetBackupVault).

type ProjectsLocationsBackupVaultsPatchCall ¶
added in v0.188.0
type ProjectsLocationsBackupVaultsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsPatchCall) Context ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsPatchCall) Do ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.backupVaults.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsPatchCall) Fields ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsPatchCall) Force ¶
added in v0.190.0
func (c *ProjectsLocationsBackupVaultsPatchCall) Force(force bool) *ProjectsLocationsBackupVaultsPatchCall

Force sets the optional parameter "force": If set to true, will not check plan duration against backup vault enforcement duration.

func (*ProjectsLocationsBackupVaultsPatchCall) ForceUpdateAccessRestriction ¶
added in v0.234.0
func (c *ProjectsLocationsBackupVaultsPatchCall) ForceUpdateAccessRestriction(forceUpdateAccessRestriction bool) *ProjectsLocationsBackupVaultsPatchCall

ForceUpdateAccessRestriction sets the optional parameter "forceUpdateAccessRestriction": If set to true, we will force update access restriction even if some non compliant data sources are present. The default is 'false'.

func (*ProjectsLocationsBackupVaultsPatchCall) Header ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupVaultsPatchCall) RequestId ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupVaultsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupVaultsPatchCall) UpdateMask ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupVaultsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Field mask is used to specify the fields to be overwritten in the BackupVault resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail.

func (*ProjectsLocationsBackupVaultsPatchCall) ValidateOnly ¶
added in v0.188.0
func (c *ProjectsLocationsBackupVaultsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupVaultsPatchCall

ValidateOnly sets the optional parameter "validateOnly": Only validate the request, but do not perform mutations. The default is 'false'.

type ProjectsLocationsBackupVaultsService ¶
added in v0.155.0
type ProjectsLocationsBackupVaultsService struct {
	DataSources *ProjectsLocationsBackupVaultsDataSourcesService
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupVaultsService ¶
added in v0.155.0
func NewProjectsLocationsBackupVaultsService(s *Service) *ProjectsLocationsBackupVaultsService
func (*ProjectsLocationsBackupVaultsService) Create ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) Create(parent string, backupvault *BackupVault) *ProjectsLocationsBackupVaultsCreateCall

Create: Creates a new BackupVault in a given project and location.

- parent: Value for parent.

func (*ProjectsLocationsBackupVaultsService) Delete ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) Delete(name string) *ProjectsLocationsBackupVaultsDeleteCall

Delete: Deletes a BackupVault.

- name: Name of the resource.

func (*ProjectsLocationsBackupVaultsService) FetchUsable ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) FetchUsable(parent string) *ProjectsLocationsBackupVaultsFetchUsableCall

FetchUsable: FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

parent: The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value.
func (*ProjectsLocationsBackupVaultsService) Get ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) Get(name string) *ProjectsLocationsBackupVaultsGetCall

Get: Gets details of a BackupVault.

name: Name of the backupvault store resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'.
func (*ProjectsLocationsBackupVaultsService) List ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) List(parent string) *ProjectsLocationsBackupVaultsListCall

List: Lists BackupVaults in a given project and location.

parent: The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value.
func (*ProjectsLocationsBackupVaultsService) Patch ¶
added in v0.188.0
func (r *ProjectsLocationsBackupVaultsService) Patch(name string, backupvault *BackupVault) *ProjectsLocationsBackupVaultsPatchCall

Patch: Updates the settings of a BackupVault.

name: Output only. Identifier. Name of the backup vault to create. It must have the format"projects/{project}/locations/{location}/backupVaults/{backupvault}" `. `{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.
func (*ProjectsLocationsBackupVaultsService) TestIamPermissions ¶
added in v0.155.0
func (r *ProjectsLocationsBackupVaultsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsBackupVaultsTestIamPermissionsCall

TestIamPermissions: Returns the caller's permissions on a BackupVault resource. A caller is not required to have Google IAM permission to make this request.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsBackupVaultsTestIamPermissionsCall ¶
added in v0.155.0
type ProjectsLocationsBackupVaultsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupVaultsTestIamPermissionsCall) Context ¶
added in v0.155.0
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsBackupVaultsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupVaultsTestIamPermissionsCall) Do ¶
added in v0.155.0
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "backupdr.projects.locations.backupVaults.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupVaultsTestIamPermissionsCall) Fields ¶
added in v0.155.0
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupVaultsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupVaultsTestIamPermissionsCall) Header ¶
added in v0.155.0
func (c *ProjectsLocationsBackupVaultsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall ¶
added in v0.241.0
type ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Context ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Do ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Do(opts ...googleapi.CallOption) (*FetchDataSourceReferencesForResourceTypeResponse, error)

Do executes the "backupdr.projects.locations.dataSourceReferences.fetchForResourceType" call. Any non-2xx status code is an error. Response headers are in either *FetchDataSourceReferencesForResourceTypeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Fields ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Filter ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Filter(filter string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

Filter sets the optional parameter "filter": A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: * data_source * data_source_gcp_resource_info.gcp_resourcename * data_source_backup_config_state * data_source_backup_count * data_source_backup_config_info.last_backup_state * data_source_gcp_resource_info.gcp_resourcename * data_source_gcp_resource_info.type * data_source_gcp_resource_info.location * data_source_gcp_resource_info.cloud_sql_instance_properties.instance_create_t ime

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Header ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) IfNoneMatch ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) OrderBy ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) OrderBy(orderBy string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * name

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageSize ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageSize(pageSize int64) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

PageSize sets the optional parameter "pageSize": The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageToken ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) PageToken(pageToken string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous call of `FetchDataSourceReferencesForResourceType`. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `FetchDataSourceReferencesForResourceType` must match the call that provided the page token.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Pages ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) Pages(ctx context.Context, f func(*FetchDataSourceReferencesForResourceTypeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) ResourceType ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall) ResourceType(resourceType string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

ResourceType sets the optional parameter "resourceType": Required. The type of the Google Cloud resource. Ex: sql.googleapis.com/Instance

type ProjectsLocationsDataSourceReferencesGetCall ¶
added in v0.241.0
type ProjectsLocationsDataSourceReferencesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDataSourceReferencesGetCall) Context ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesGetCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDataSourceReferencesGetCall) Do ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesGetCall) Do(opts ...googleapi.CallOption) (*DataSourceReference, error)

Do executes the "backupdr.projects.locations.dataSourceReferences.get" call. Any non-2xx status code is an error. Response headers are in either *DataSourceReference.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDataSourceReferencesGetCall) Fields ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDataSourceReferencesGetCall) Header ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDataSourceReferencesGetCall) IfNoneMatch ¶
added in v0.241.0
func (c *ProjectsLocationsDataSourceReferencesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDataSourceReferencesListCall ¶
added in v0.254.0
type ProjectsLocationsDataSourceReferencesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsDataSourceReferencesListCall) Context ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Context(ctx context.Context) *ProjectsLocationsDataSourceReferencesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsDataSourceReferencesListCall) Do ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourceReferencesResponse, error)

Do executes the "backupdr.projects.locations.dataSourceReferences.list" call. Any non-2xx status code is an error. Response headers are in either *ListDataSourceReferencesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsDataSourceReferencesListCall) Fields ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourceReferencesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsDataSourceReferencesListCall) Filter ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Filter(filter string) *ProjectsLocationsDataSourceReferencesListCall

Filter sets the optional parameter "filter": A filter expression that filters the results listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The following field and operator combinations are supported: * data_source_gcp_resource_info.gcp_resourcename with `=`, `!=` * data_source_gcp_resource_info.type with `=`, `!=`

func (*ProjectsLocationsDataSourceReferencesListCall) Header ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsDataSourceReferencesListCall) IfNoneMatch ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourceReferencesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsDataSourceReferencesListCall) OrderBy ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) OrderBy(orderBy string) *ProjectsLocationsDataSourceReferencesListCall

OrderBy sets the optional parameter "orderBy": A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * data_source * data_source_gcp_resource_info.gcp_resourcename

func (*ProjectsLocationsDataSourceReferencesListCall) PageSize ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) PageSize(pageSize int64) *ProjectsLocationsDataSourceReferencesListCall

PageSize sets the optional parameter "pageSize": The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100.

func (*ProjectsLocationsDataSourceReferencesListCall) PageToken ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) PageToken(pageToken string) *ProjectsLocationsDataSourceReferencesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDataSourceReferences` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSourceReferences` must match the call that provided the page token.

func (*ProjectsLocationsDataSourceReferencesListCall) Pages ¶
added in v0.254.0
func (c *ProjectsLocationsDataSourceReferencesListCall) Pages(ctx context.Context, f func(*ListDataSourceReferencesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDataSourceReferencesService ¶
added in v0.241.0
type ProjectsLocationsDataSourceReferencesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsDataSourceReferencesService ¶
added in v0.241.0
func NewProjectsLocationsDataSourceReferencesService(s *Service) *ProjectsLocationsDataSourceReferencesService
func (*ProjectsLocationsDataSourceReferencesService) FetchForResourceType ¶
added in v0.241.0
func (r *ProjectsLocationsDataSourceReferencesService) FetchForResourceType(parent string) *ProjectsLocationsDataSourceReferencesFetchForResourceTypeCall

FetchForResourceType: Fetch DataSourceReferences for a given project, location and resource type.

parent: The parent resource name. Format: projects/{project}/locations/{location}.
func (*ProjectsLocationsDataSourceReferencesService) Get ¶
added in v0.241.0
func (r *ProjectsLocationsDataSourceReferencesService) Get(name string) *ProjectsLocationsDataSourceReferencesGetCall

Get: Gets details of a single DataSourceReference.

name: The name of the DataSourceReference to retrieve. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_r eference}.
func (*ProjectsLocationsDataSourceReferencesService) List ¶
added in v0.254.0
func (r *ProjectsLocationsDataSourceReferencesService) List(parent string) *ProjectsLocationsDataSourceReferencesListCall

List: Lists DataSourceReferences for a given project and location.

parent: The parent resource name. Format: projects/{project}/locations/{location}.
type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "backupdr.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGetTrialCall ¶
added in v0.249.0
type ProjectsLocationsGetTrialCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetTrialCall) Context ¶
added in v0.249.0
func (c *ProjectsLocationsGetTrialCall) Context(ctx context.Context) *ProjectsLocationsGetTrialCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetTrialCall) Do ¶
added in v0.249.0
func (c *ProjectsLocationsGetTrialCall) Do(opts ...googleapi.CallOption) (*Trial, error)

Do executes the "backupdr.projects.locations.getTrial" call. Any non-2xx status code is an error. Response headers are in either *Trial.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetTrialCall) Fields ¶
added in v0.249.0
func (c *ProjectsLocationsGetTrialCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetTrialCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetTrialCall) Header ¶
added in v0.249.0
func (c *ProjectsLocationsGetTrialCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetTrialCall) IfNoneMatch ¶
added in v0.249.0
func (c *ProjectsLocationsGetTrialCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetTrialCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "backupdr.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.229.0
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
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsManagementServersCreateCall ¶
type ProjectsLocationsManagementServersCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersCreateCall) Context ¶
func (c *ProjectsLocationsManagementServersCreateCall) Context(ctx context.Context) *ProjectsLocationsManagementServersCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersCreateCall) Do ¶
func (c *ProjectsLocationsManagementServersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.managementServers.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersCreateCall) Fields ¶
func (c *ProjectsLocationsManagementServersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersCreateCall) Header ¶
func (c *ProjectsLocationsManagementServersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsManagementServersCreateCall) ManagementServerId ¶
func (c *ProjectsLocationsManagementServersCreateCall) ManagementServerId(managementServerId string) *ProjectsLocationsManagementServersCreateCall

ManagementServerId sets the optional parameter "managementServerId": Required. The name of the management server to create. The name must be unique for the specified project and location.

func (*ProjectsLocationsManagementServersCreateCall) RequestId ¶
func (c *ProjectsLocationsManagementServersCreateCall) RequestId(requestId string) *ProjectsLocationsManagementServersCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsManagementServersDeleteCall ¶
type ProjectsLocationsManagementServersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersDeleteCall) Context ¶
func (c *ProjectsLocationsManagementServersDeleteCall) Context(ctx context.Context) *ProjectsLocationsManagementServersDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersDeleteCall) Do ¶
func (c *ProjectsLocationsManagementServersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.managementServers.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersDeleteCall) Fields ¶
func (c *ProjectsLocationsManagementServersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersDeleteCall) Header ¶
func (c *ProjectsLocationsManagementServersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsManagementServersDeleteCall) RequestId ¶
func (c *ProjectsLocationsManagementServersDeleteCall) RequestId(requestId string) *ProjectsLocationsManagementServersDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsManagementServersGetCall ¶
type ProjectsLocationsManagementServersGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersGetCall) Context ¶
func (c *ProjectsLocationsManagementServersGetCall) Context(ctx context.Context) *ProjectsLocationsManagementServersGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersGetCall) Do ¶
func (c *ProjectsLocationsManagementServersGetCall) Do(opts ...googleapi.CallOption) (*ManagementServer, error)

Do executes the "backupdr.projects.locations.managementServers.get" call. Any non-2xx status code is an error. Response headers are in either *ManagementServer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersGetCall) Fields ¶
func (c *ProjectsLocationsManagementServersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersGetCall) Header ¶
func (c *ProjectsLocationsManagementServersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsManagementServersGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsManagementServersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsManagementServersGetIamPolicyCall ¶
type ProjectsLocationsManagementServersGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsManagementServersGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "backupdr.projects.locations.managementServers.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsManagementServersGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsManagementServersGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsManagementServersGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsManagementServersGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsManagementServersListCall ¶
type ProjectsLocationsManagementServersListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersListCall) Context ¶
func (c *ProjectsLocationsManagementServersListCall) Context(ctx context.Context) *ProjectsLocationsManagementServersListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersListCall) Do ¶
func (c *ProjectsLocationsManagementServersListCall) Do(opts ...googleapi.CallOption) (*ListManagementServersResponse, error)

Do executes the "backupdr.projects.locations.managementServers.list" call. Any non-2xx status code is an error. Response headers are in either *ListManagementServersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersListCall) Fields ¶
func (c *ProjectsLocationsManagementServersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersListCall) Filter ¶
func (c *ProjectsLocationsManagementServersListCall) Filter(filter string) *ProjectsLocationsManagementServersListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsManagementServersListCall) Header ¶
func (c *ProjectsLocationsManagementServersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsManagementServersListCall) IfNoneMatch ¶
func (c *ProjectsLocationsManagementServersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsManagementServersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsManagementServersListCall) OrderBy ¶
func (c *ProjectsLocationsManagementServersListCall) OrderBy(orderBy string) *ProjectsLocationsManagementServersListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsManagementServersListCall) PageSize ¶
func (c *ProjectsLocationsManagementServersListCall) PageSize(pageSize int64) *ProjectsLocationsManagementServersListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsManagementServersListCall) PageToken ¶
func (c *ProjectsLocationsManagementServersListCall) PageToken(pageToken string) *ProjectsLocationsManagementServersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsManagementServersListCall) Pages ¶
func (c *ProjectsLocationsManagementServersListCall) Pages(ctx context.Context, f func(*ListManagementServersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsManagementServersMsComplianceMetadataCall ¶
added in v0.243.0
type ProjectsLocationsManagementServersMsComplianceMetadataCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersMsComplianceMetadataCall) Context ¶
added in v0.243.0
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Context(ctx context.Context) *ProjectsLocationsManagementServersMsComplianceMetadataCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersMsComplianceMetadataCall) Do ¶
added in v0.243.0
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Do(opts ...googleapi.CallOption) (*FetchMsComplianceMetadataResponse, error)

Do executes the "backupdr.projects.locations.managementServers.msComplianceMetadata" call. Any non-2xx status code is an error. Response headers are in either *FetchMsComplianceMetadataResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersMsComplianceMetadataCall) Fields ¶
added in v0.243.0
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersMsComplianceMetadataCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersMsComplianceMetadataCall) Header ¶
added in v0.243.0
func (c *ProjectsLocationsManagementServersMsComplianceMetadataCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsManagementServersService ¶
type ProjectsLocationsManagementServersService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsManagementServersService ¶
func NewProjectsLocationsManagementServersService(s *Service) *ProjectsLocationsManagementServersService
func (*ProjectsLocationsManagementServersService) Create ¶
func (r *ProjectsLocationsManagementServersService) Create(parent string, managementserver *ManagementServer) *ProjectsLocationsManagementServersCreateCall

Create: Creates a new ManagementServer in a given project and location.

parent: The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**.
func (*ProjectsLocationsManagementServersService) Delete ¶
func (r *ProjectsLocationsManagementServersService) Delete(name string) *ProjectsLocationsManagementServersDeleteCall

Delete: Deletes a single ManagementServer.

- name: Name of the resource.

func (*ProjectsLocationsManagementServersService) Get ¶
func (r *ProjectsLocationsManagementServersService) Get(name string) *ProjectsLocationsManagementServersGetCall

Get: Gets details of a single ManagementServer.

name: Name of the management server resource name, in the format 'projects/{project_id}/locations/{location}/managementServers/{resource_nam e}'.
func (*ProjectsLocationsManagementServersService) GetIamPolicy ¶
func (r *ProjectsLocationsManagementServersService) GetIamPolicy(resource string) *ProjectsLocationsManagementServersGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsManagementServersService) List ¶
func (r *ProjectsLocationsManagementServersService) List(parent string) *ProjectsLocationsManagementServersListCall

List: Lists ManagementServers in a given project and location.

parent: The project and location for which to retrieve management servers information, in the format 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve management servers for all locations, use "-" for the '{location}' value.
func (*ProjectsLocationsManagementServersService) MsComplianceMetadata ¶
added in v0.243.0
func (r *ProjectsLocationsManagementServersService) MsComplianceMetadata(parent string, fetchmscompliancemetadatarequest *FetchMsComplianceMetadataRequest) *ProjectsLocationsManagementServersMsComplianceMetadataCall

MsComplianceMetadata: Returns the Assured Workloads compliance metadata for a given project.

parent: The project and location to be used to check CSS metadata for target project information, in the format 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**.
func (*ProjectsLocationsManagementServersService) SetIamPolicy ¶
func (r *ProjectsLocationsManagementServersService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsLocationsManagementServersSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsManagementServersService) TestIamPermissions ¶
func (r *ProjectsLocationsManagementServersService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsLocationsManagementServersTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsManagementServersSetIamPolicyCall ¶
type ProjectsLocationsManagementServersSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsManagementServersSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "backupdr.projects.locations.managementServers.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsManagementServersSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsManagementServersTestIamPermissionsCall ¶
type ProjectsLocationsManagementServersTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsManagementServersTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsManagementServersTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsManagementServersTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "backupdr.projects.locations.managementServers.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsManagementServersTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsManagementServersTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsManagementServersTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsManagementServersTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsCancelCall ¶
type ProjectsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsCancelCall) Context ¶
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsCancelCall) Do ¶
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "backupdr.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "backupdr.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "backupdr.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

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
func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall

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

type ProjectsLocationsResourceBackupConfigsListCall ¶
added in v0.220.0
type ProjectsLocationsResourceBackupConfigsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsResourceBackupConfigsListCall) Context ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Context(ctx context.Context) *ProjectsLocationsResourceBackupConfigsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsResourceBackupConfigsListCall) Do ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Do(opts ...googleapi.CallOption) (*ListResourceBackupConfigsResponse, error)

Do executes the "backupdr.projects.locations.resourceBackupConfigs.list" call. Any non-2xx status code is an error. Response headers are in either *ListResourceBackupConfigsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsResourceBackupConfigsListCall) Fields ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsResourceBackupConfigsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsResourceBackupConfigsListCall) Filter ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Filter(filter string) *ProjectsLocationsResourceBackupConfigsListCall

Filter sets the optional parameter "filter": Filtering results.

func (*ProjectsLocationsResourceBackupConfigsListCall) Header ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsResourceBackupConfigsListCall) IfNoneMatch ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsResourceBackupConfigsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsResourceBackupConfigsListCall) OrderBy ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) OrderBy(orderBy string) *ProjectsLocationsResourceBackupConfigsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results.

func (*ProjectsLocationsResourceBackupConfigsListCall) PageSize ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) PageSize(pageSize int64) *ProjectsLocationsResourceBackupConfigsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will use 100 as default. Maximum value is 500 and values above 500 will be coerced to 500.

func (*ProjectsLocationsResourceBackupConfigsListCall) PageToken ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) PageToken(pageToken string) *ProjectsLocationsResourceBackupConfigsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsResourceBackupConfigsListCall) Pages ¶
added in v0.220.0
func (c *ProjectsLocationsResourceBackupConfigsListCall) Pages(ctx context.Context, f func(*ListResourceBackupConfigsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsResourceBackupConfigsService ¶
added in v0.220.0
type ProjectsLocationsResourceBackupConfigsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsResourceBackupConfigsService ¶
added in v0.220.0
func NewProjectsLocationsResourceBackupConfigsService(s *Service) *ProjectsLocationsResourceBackupConfigsService
func (*ProjectsLocationsResourceBackupConfigsService) List ¶
added in v0.220.0
func (r *ProjectsLocationsResourceBackupConfigsService) List(parent string) *ProjectsLocationsResourceBackupConfigsListCall

List: Lists ResourceBackupConfigs.

parent: The project and location for which to retrieve resource backup configs. Format: 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**.
type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	BackupPlanAssociations *ProjectsLocationsBackupPlanAssociationsService

	BackupPlans *ProjectsLocationsBackupPlansService

	BackupVaults *ProjectsLocationsBackupVaultsService

	DataSourceReferences *ProjectsLocationsDataSourceReferencesService

	ManagementServers *ProjectsLocationsManagementServersService

	Operations *ProjectsLocationsOperationsService

	ResourceBackupConfigs *ProjectsLocationsResourceBackupConfigsService

	ServiceConfig *ProjectsLocationsServiceConfigService

	Trial *ProjectsLocationsTrialService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) Get ¶
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) GetTrial ¶
added in v0.249.0
func (r *ProjectsLocationsService) GetTrial(name string) *ProjectsLocationsGetTrialCall

GetTrial: Gets the Trial state for a given project

name: The project for which trial details need to be retrieved. Format: projects/{project}/locations/{location} Supported Locations are - us, eu and asia.
func (*ProjectsLocationsService) List ¶
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

type ProjectsLocationsServiceConfigInitializeCall ¶
added in v0.212.0
type ProjectsLocationsServiceConfigInitializeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsServiceConfigInitializeCall) Context ¶
added in v0.212.0
func (c *ProjectsLocationsServiceConfigInitializeCall) Context(ctx context.Context) *ProjectsLocationsServiceConfigInitializeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsServiceConfigInitializeCall) Do ¶
added in v0.212.0
func (c *ProjectsLocationsServiceConfigInitializeCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "backupdr.projects.locations.serviceConfig.initialize" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsServiceConfigInitializeCall) Fields ¶
added in v0.212.0
func (c *ProjectsLocationsServiceConfigInitializeCall) Fields(s ...googleapi.Field) *ProjectsLocationsServiceConfigInitializeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsServiceConfigInitializeCall) Header ¶
added in v0.212.0
func (c *ProjectsLocationsServiceConfigInitializeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsServiceConfigService ¶
added in v0.212.0
type ProjectsLocationsServiceConfigService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsServiceConfigService ¶
added in v0.212.0
func NewProjectsLocationsServiceConfigService(s *Service) *ProjectsLocationsServiceConfigService
func (*ProjectsLocationsServiceConfigService) Initialize ¶
added in v0.212.0
func (r *ProjectsLocationsServiceConfigService) Initialize(name string, initializeservicerequest *InitializeServiceRequest) *ProjectsLocationsServiceConfigInitializeCall

Initialize: Initializes the service related config for a project.

name: The resource name of the serviceConfig used to initialize the service. Format: `projects/{project_id}/locations/{location}/serviceConfig`.
type ProjectsLocationsTrialEndCall ¶
added in v0.257.0
type ProjectsLocationsTrialEndCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsTrialEndCall) Context ¶
added in v0.257.0
func (c *ProjectsLocationsTrialEndCall) Context(ctx context.Context) *ProjectsLocationsTrialEndCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsTrialEndCall) Do ¶
added in v0.257.0
func (c *ProjectsLocationsTrialEndCall) Do(opts ...googleapi.CallOption) (*Trial, error)

Do executes the "backupdr.projects.locations.trial.end" call. Any non-2xx status code is an error. Response headers are in either *Trial.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsTrialEndCall) Fields ¶
added in v0.257.0
func (c *ProjectsLocationsTrialEndCall) Fields(s ...googleapi.Field) *ProjectsLocationsTrialEndCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsTrialEndCall) Header ¶
added in v0.257.0
func (c *ProjectsLocationsTrialEndCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsTrialService ¶
added in v0.249.0
type ProjectsLocationsTrialService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsTrialService ¶
added in v0.249.0
func NewProjectsLocationsTrialService(s *Service) *ProjectsLocationsTrialService
func (*ProjectsLocationsTrialService) End ¶
added in v0.257.0
func (r *ProjectsLocationsTrialService) End(parent string, endtrialrequest *EndTrialRequest) *ProjectsLocationsTrialEndCall

End: Ends the trial for a project

parent: The parent resource where the trial has been created. Format: projects/{project}/locations/{location}.
func (*ProjectsLocationsTrialService) Subscribe ¶
added in v0.249.0
func (r *ProjectsLocationsTrialService) Subscribe(parent string, subscribetrialrequest *SubscribeTrialRequest) *ProjectsLocationsTrialSubscribeCall

Subscribe: Subscribes to a trial for a project

parent: The project where this trial will be created. Format: projects/{project}/locations/{location} Supported Locations are - us, eu and asia.
type ProjectsLocationsTrialSubscribeCall ¶
added in v0.249.0
type ProjectsLocationsTrialSubscribeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsTrialSubscribeCall) Context ¶
added in v0.249.0
func (c *ProjectsLocationsTrialSubscribeCall) Context(ctx context.Context) *ProjectsLocationsTrialSubscribeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsTrialSubscribeCall) Do ¶
added in v0.249.0
func (c *ProjectsLocationsTrialSubscribeCall) Do(opts ...googleapi.CallOption) (*Trial, error)

Do executes the "backupdr.projects.locations.trial.subscribe" call. Any non-2xx status code is an error. Response headers are in either *Trial.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsTrialSubscribeCall) Fields ¶
added in v0.249.0
func (c *ProjectsLocationsTrialSubscribeCall) Fields(s ...googleapi.Field) *ProjectsLocationsTrialSubscribeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsTrialSubscribeCall) Header ¶
added in v0.249.0
func (c *ProjectsLocationsTrialSubscribeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type RegionDiskTargetEnvironment ¶
added in v0.234.0
type RegionDiskTargetEnvironment struct {
	// Project: Required. Target project for the disk.
	Project string `json:"project,omitempty"`
	// Region: Required. Target region for the disk.
	Region string `json:"region,omitempty"`
	// ReplicaZones: Required. Target URLs of the replica zones for the disk.
	ReplicaZones []string `json:"replicaZones,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Project") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Project") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionDiskTargetEnvironment: RegionDiskTargetEnvironment represents the target environment for the disk.

func (RegionDiskTargetEnvironment) MarshalJSON ¶
added in v0.234.0
func (s RegionDiskTargetEnvironment) MarshalJSON() ([]byte, error)
type RemoveDataSourceRequest ¶
added in v0.188.0
type RemoveDataSourceRequest struct {
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes after the first request. For example,
	// consider a situation where you make an initial request and the request times
	// out. If you make the request again with the same request ID, the server can
	// check if original operation with the same request ID was received, and if
	// so, will ignore the second request. This prevents clients from accidentally
	// creating duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
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

RemoveDataSourceRequest: Message for deleting a DataSource.

func (RemoveDataSourceRequest) MarshalJSON ¶
added in v0.188.0
func (s RemoveDataSourceRequest) MarshalJSON() ([]byte, error)
type ResourceBackupConfig ¶
added in v0.220.0
type ResourceBackupConfig struct {
	// BackupConfigsDetails: Backup configurations applying to the target resource,
	// including those targeting its related/child resources. For example, backup
	// configuration applicable to Compute Engine disks will be populated in this
	// field for a Compute Engine VM which has the disk associated.
	BackupConfigsDetails []*BackupConfigDetails `json:"backupConfigsDetails,omitempty"`
	// BackupConfigured: Output only. Whether the target resource is configured for
	// backup. This is true if the backup_configs_details is not empty.
	BackupConfigured bool `json:"backupConfigured,omitempty"`
	// Name: Identifier. The resource name of the ResourceBackupConfig. Format:
	// projects/{project}/locations/{location}/resourceBackupConfigs/{uid}
	Name string `json:"name,omitempty"`
	// TargetResource: Output only. The full resource name
	// (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the
	// cloud resource that this configuration applies to. Supported resource types
	// are ResourceBackupConfig.ResourceType.
	TargetResource string `json:"targetResource,omitempty"`
	// TargetResourceDisplayName: Output only. The human friendly name of the
	// target resource.
	TargetResourceDisplayName string `json:"targetResourceDisplayName,omitempty"`
	// TargetResourceLabels: Labels associated with the target resource.
	TargetResourceLabels map[string]string `json:"targetResourceLabels,omitempty"`
	// TargetResourceType: Output only. The type of the target resource.
	//
	// Possible values:
	//   "RESOURCE_TYPE_UNSPECIFIED" - Resource type not set.
	//   "CLOUD_SQL_INSTANCE" - Cloud SQL instance.
	//   "COMPUTE_ENGINE_VM" - Compute Engine VM.
	//   "COMPUTE_ENGINE_DISK" - Compute Engine Disk.
	//   "COMPUTE_ENGINE_REGIONAL_DISK" - Compute Engine Regional Disk.
	TargetResourceType string `json:"targetResourceType,omitempty"`
	// Uid: Output only. The unique identifier of the resource backup config.
	Uid string `json:"uid,omitempty"`
	// Vaulted: Output only. Whether the target resource is protected by a backup
	// vault. This is true if the backup_configs_details is not empty and any of
	// the ResourceBackupConfig.backup_configs_details has a backup configuration
	// with BackupConfigDetails.backup_vault set.
	Vaulted bool `json:"vaulted,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupConfigsDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupConfigsDetails") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ResourceBackupConfig: ResourceBackupConfig represents a resource along with its backup configurations.

func (ResourceBackupConfig) MarshalJSON ¶
added in v0.220.0
func (s ResourceBackupConfig) MarshalJSON() ([]byte, error)
type RestoreBackupRequest ¶
added in v0.192.0
type RestoreBackupRequest struct {
	// ClearOverridesFieldMask: Optional. A field mask used to clear server-side
	// default values for fields within the `instance_properties` oneof. When a
	// field in this mask is cleared, the server will not apply its default logic
	// (like inheriting a value from the source) for that field. The most common
	// current use case is clearing default encryption keys. Examples of field mask
	// paths: - Compute Instance Disks:
	// `compute_instance_restore_properties.disks.*.disk_encryption_key` - Single
	// Disk: `disk_restore_properties.disk_encryption_key`
	ClearOverridesFieldMask string `json:"clearOverridesFieldMask,omitempty"`
	// ComputeInstanceRestoreProperties: Compute Engine instance properties to be
	// overridden during restore.
	ComputeInstanceRestoreProperties *ComputeInstanceRestoreProperties `json:"computeInstanceRestoreProperties,omitempty"`
	// ComputeInstanceTargetEnvironment: Compute Engine target environment to be
	// used during restore.
	ComputeInstanceTargetEnvironment *ComputeInstanceTargetEnvironment `json:"computeInstanceTargetEnvironment,omitempty"`
	// DiskRestoreProperties: Disk properties to be overridden during restore.
	DiskRestoreProperties *DiskRestoreProperties `json:"diskRestoreProperties,omitempty"`
	// DiskTargetEnvironment: Disk target environment to be used during restore.
	DiskTargetEnvironment *DiskTargetEnvironment `json:"diskTargetEnvironment,omitempty"`
	// RegionDiskTargetEnvironment: Region disk target environment to be used
	// during restore.
	RegionDiskTargetEnvironment *RegionDiskTargetEnvironment `json:"regionDiskTargetEnvironment,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes after the first request. For example,
	// consider a situation where you make an initial request and the request times
	// out. If you make the request again with the same request ID, the server can
	// check if original operation with the same request ID was received, and if
	// so, will ignore the second request. This prevents clients from accidentally
	// creating duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClearOverridesFieldMask") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClearOverridesFieldMask") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreBackupRequest: Request message for restoring from a Backup.

func (RestoreBackupRequest) MarshalJSON ¶
added in v0.192.0
func (s RestoreBackupRequest) MarshalJSON() ([]byte, error)
type RestoreBackupResponse ¶
added in v0.200.0
type RestoreBackupResponse struct {
	// TargetResource: Details of the target resource created/modified as part of
	// restore.
	TargetResource *TargetResource `json:"targetResource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TargetResource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TargetResource") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreBackupResponse: Response message for restoring from a Backup.

func (RestoreBackupResponse) MarshalJSON ¶
added in v0.200.0
func (s RestoreBackupResponse) MarshalJSON() ([]byte, error)
type RuleConfigInfo ¶
added in v0.192.0
type RuleConfigInfo struct {
	// LastBackupError: Output only. google.rpc.Status object to store the last
	// backup error.
	LastBackupError *Status `json:"lastBackupError,omitempty"`
	// LastBackupState: Output only. The last backup state for rule.
	//
	// Possible values:
	//   "LAST_BACKUP_STATE_UNSPECIFIED" - State not set.
	//   "FIRST_BACKUP_PENDING" - The first backup is pending.
	//   "PERMISSION_DENIED" - The most recent backup could not be run/failed
	// because of the lack of permissions.
	//   "SUCCEEDED" - The last backup operation succeeded.
	//   "FAILED" - The last backup operation failed.
	LastBackupState string `json:"lastBackupState,omitempty"`
	// LastSuccessfulBackupConsistencyTime: Output only. The point in time when the
	// last successful backup was captured from the source.
	LastSuccessfulBackupConsistencyTime string `json:"lastSuccessfulBackupConsistencyTime,omitempty"`
	// RuleId: Output only. Backup Rule id fetched from backup plan.
	RuleId string `json:"ruleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastBackupError") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastBackupError") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RuleConfigInfo: Message for rules config info.

func (RuleConfigInfo) MarshalJSON ¶
added in v0.192.0
func (s RuleConfigInfo) MarshalJSON() ([]byte, error)
type Scheduling ¶
added in v0.188.0
type Scheduling struct {
	// AutomaticRestart: Optional. Specifies whether the instance should be
	// automatically restarted if it is terminated by Compute Engine (not
	// terminated by a user).
	AutomaticRestart bool `json:"automaticRestart,omitempty"`
	// InstanceTerminationAction: Optional. Specifies the termination action for
	// the instance.
	//
	// Possible values:
	//   "INSTANCE_TERMINATION_ACTION_UNSPECIFIED" - Default value. This value is
	// unused.
	//   "DELETE" - Delete the VM.
	//   "STOP" - Stop the VM without storing in-memory content. default action.
	InstanceTerminationAction string `json:"instanceTerminationAction,omitempty"`
	// LocalSsdRecoveryTimeout: Optional. Specifies the maximum amount of time a
	// Local Ssd Vm should wait while recovery of the Local Ssd state is attempted.
	// Its value should be in between 0 and 168 hours with hour granularity and the
	// default value being 1 hour.
	LocalSsdRecoveryTimeout *SchedulingDuration `json:"localSsdRecoveryTimeout,omitempty"`
	// MinNodeCpus: Optional. The minimum number of virtual CPUs this instance will
	// consume when running on a sole-tenant node.
	MinNodeCpus int64 `json:"minNodeCpus,omitempty"`
	// NodeAffinities: Optional. A set of node affinity and anti-affinity
	// configurations. Overrides reservationAffinity.
	NodeAffinities []*NodeAffinity `json:"nodeAffinities,omitempty"`
	// OnHostMaintenance: Optional. Defines the maintenance behavior for this
	// instance.
	//
	// Possible values:
	//   "ON_HOST_MAINTENANCE_UNSPECIFIED" - Default value. This value is unused.
	//   "TERMINATE" - Tells Compute Engine to terminate and (optionally) restart
	// the instance away from the maintenance activity.
	//   "MIGRATE" - Default, Allows Compute Engine to automatically migrate
	// instances out of the way of maintenance events.
	OnHostMaintenance string `json:"onHostMaintenance,omitempty"`
	// Preemptible: Optional. Defines whether the instance is preemptible.
	Preemptible bool `json:"preemptible,omitempty"`
	// ProvisioningModel: Optional. Specifies the provisioning model of the
	// instance.
	//
	// Possible values:
	//   "PROVISIONING_MODEL_UNSPECIFIED" - Default value. This value is not used.
	//   "STANDARD" - Standard provisioning with user controlled runtime, no
	// discounts.
	//   "SPOT" - Heavily discounted, no guaranteed runtime.
	ProvisioningModel string `json:"provisioningModel,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutomaticRestart") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutomaticRestart") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Scheduling: Sets the scheduling options for an Instance.

func (Scheduling) MarshalJSON ¶
added in v0.188.0
func (s Scheduling) MarshalJSON() ([]byte, error)
type SchedulingDuration ¶
added in v0.188.0
type SchedulingDuration struct {
	// Nanos: Optional. Span of time that's a fraction of a second at nanosecond
	// resolution.
	Nanos int64 `json:"nanos,omitempty"`
	// Seconds: Optional. Span of time at a resolution of a second.
	Seconds int64 `json:"seconds,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "Nanos") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Nanos") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SchedulingDuration: A SchedulingDuration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years.

func (SchedulingDuration) MarshalJSON ¶
added in v0.188.0
func (s SchedulingDuration) MarshalJSON() ([]byte, error)
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

type ServiceAccount ¶
added in v0.188.0
type ServiceAccount struct {
	// Email: Optional. Email address of the service account.
	Email string `json:"email,omitempty"`
	// Scopes: Optional. The list of scopes to be made available for this service
	// account.
	Scopes []string `json:"scopes,omitempty"`
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

ServiceAccount: A service account.

func (ServiceAccount) MarshalJSON ¶
added in v0.188.0
func (s ServiceAccount) MarshalJSON() ([]byte, error)
type ServiceLockInfo ¶
added in v0.188.0
type ServiceLockInfo struct {
	// Operation: Output only. The name of the operation that created this lock.
	// The lock will automatically be released when the operation completes.
	Operation string `json:"operation,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServiceLockInfo: ServiceLockInfo represents the details of a lock taken by the service on a Backup resource.

func (ServiceLockInfo) MarshalJSON ¶
added in v0.188.0
func (s ServiceLockInfo) MarshalJSON() ([]byte, error)
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
type SetInternalStatusRequest ¶
added in v0.188.0
type SetInternalStatusRequest struct {
	// BackupConfigState: Required. Output only. The new BackupConfigState to set
	// for the DataSource.
	//
	// Possible values:
	//   "BACKUP_CONFIG_STATE_UNSPECIFIED" - The possible states of backup
	// configuration. Status not set.
	//   "ACTIVE" - The data source is actively protected (i.e. there is a
	// BackupPlanAssociation or Appliance SLA pointing to it)
	//   "PASSIVE" - The data source is no longer protected (but may have backups
	// under it)
	BackupConfigState string `json:"backupConfigState,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes after the first request. The request
	// ID must be a valid UUID with the exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// Value: Required. The value required for this method to work. This field must
	// be the 32-byte SHA256 hash of the DataSourceID. The DataSourceID used here
	// is only the final piece of the fully qualified resource path for this
	// DataSource (i.e. the part after '.../dataSources/'). This field exists to
	// make this method difficult to call since it is intended for use only by
	// Backup Appliances.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupConfigState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupConfigState") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SetInternalStatusRequest: Request message for SetStatusInternal method.

func (SetInternalStatusRequest) MarshalJSON ¶
added in v0.188.0
func (s SetInternalStatusRequest) MarshalJSON() ([]byte, error)
type SetInternalStatusResponse ¶
added in v0.200.0
type SetInternalStatusResponse struct {
}

SetInternalStatusResponse: Response message from SetStatusInternal method.

type StandardSchedule ¶
added in v0.192.0
type StandardSchedule struct {
	// BackupWindow: Required. A BackupWindow defines the window of day during
	// which backup jobs will run. Jobs are queued at the beginning of the window
	// and will be marked as `NOT_RUN` if they do not start by the end of the
	// window. Note: running jobs will not be cancelled at the end of the window.
	BackupWindow *BackupWindow `json:"backupWindow,omitempty"`
	// DaysOfMonth: Optional. Specifies days of months like 1, 5, or 14 on which
	// jobs will run. Values for `days_of_month` are only applicable for
	// `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if
	// other values are supplied.
	DaysOfMonth []int64 `json:"daysOfMonth,omitempty"`
	// DaysOfWeek: Optional. Specifies days of week like, MONDAY or TUESDAY, on
	// which jobs will run. This is required for `recurrence_type`, `WEEKLY` and is
	// not applicable otherwise. A validation error will occur if a value is
	// supplied and `recurrence_type` is not `WEEKLY`.
	//
	// Possible values:
	//   "DAY_OF_WEEK_UNSPECIFIED" - The day of the week is unspecified.
	//   "MONDAY" - Monday
	//   "TUESDAY" - Tuesday
	//   "WEDNESDAY" - Wednesday
	//   "THURSDAY" - Thursday
	//   "FRIDAY" - Friday
	//   "SATURDAY" - Saturday
	//   "SUNDAY" - Sunday
	DaysOfWeek []string `json:"daysOfWeek,omitempty"`
	// HourlyFrequency: Optional. Specifies frequency for hourly backups. A hourly
	// frequency of 2 means jobs will run every 2 hours from start time till end
	// time defined. This is required for `recurrence_type`, `HOURLY` and is not
	// applicable otherwise. A validation error will occur if a value is supplied
	// and `recurrence_type` is not `HOURLY`. Value of hourly frequency should be
	// between 4 and 23. Reason for limit : We found that there is bandwidth
	// limitation of 3GB/S for GMI while taking a backup and 5GB/S while doing a
	// restore. Given the amount of parallel backups and restore we are targeting,
	// this will potentially take the backup time to mins and hours (in worst case
	// scenario).
	HourlyFrequency int64 `json:"hourlyFrequency,omitempty"`
	// Months: Optional. Specifies the months of year, like `FEBRUARY` and/or
	// `MAY`, on which jobs will run. This field is only applicable when
	// `recurrence_type` is `YEARLY`. A validation error will occur if other values
	// are supplied.
	//
	// Possible values:
	//   "MONTH_UNSPECIFIED" - The unspecified month.
	//   "JANUARY" - The month of January.
	//   "FEBRUARY" - The month of February.
	//   "MARCH" - The month of March.
	//   "APRIL" - The month of April.
	//   "MAY" - The month of May.
	//   "JUNE" - The month of June.
	//   "JULY" - The month of July.
	//   "AUGUST" - The month of August.
	//   "SEPTEMBER" - The month of September.
	//   "OCTOBER" - The month of October.
	//   "NOVEMBER" - The month of November.
	//   "DECEMBER" - The month of December.
	Months []string `json:"months,omitempty"`
	// RecurrenceType: Required. Specifies the `RecurrenceType` for the schedule.
	//
	// Possible values:
	//   "RECURRENCE_TYPE_UNSPECIFIED" - recurrence type not set
	//   "HOURLY" - The `BackupRule` is to be applied hourly.
	//   "DAILY" - The `BackupRule` is to be applied daily.
	//   "WEEKLY" - The `BackupRule` is to be applied weekly.
	//   "MONTHLY" - The `BackupRule` is to be applied monthly.
	//   "YEARLY" - The `BackupRule` is to be applied yearly.
	RecurrenceType string `json:"recurrenceType,omitempty"`
	// TimeZone: Required. The time zone to be used when interpreting the schedule.
	// The value of this field must be a time zone name from the IANA tz database.
	// See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for the
	// list of valid timezone names. For example, Europe/Paris.
	TimeZone string `json:"timeZone,omitempty"`
	// WeekDayOfMonth: Optional. Specifies a week day of the month like, FIRST
	// SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two
	// fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the
	// week, e.g. `LAST`. This field is only applicable for `recurrence_type`,
	// `MONTHLY` and `YEARLY`. A validation error will occur if other values are
	// supplied.
	WeekDayOfMonth *WeekDayOfMonth `json:"weekDayOfMonth,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupWindow") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupWindow") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StandardSchedule: `StandardSchedule` defines a schedule that run within the confines of a defined window of days. We can define recurrence type for schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

func (StandardSchedule) MarshalJSON ¶
added in v0.192.0
func (s StandardSchedule) MarshalJSON() ([]byte, error)
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
type SubscribeTrialRequest ¶
added in v0.249.0
type SubscribeTrialRequest struct {
}

SubscribeTrialRequest: Request message for subscribing to a trial.

type Tags ¶
added in v0.188.0
type Tags struct {
	// Items: Optional. An array of tags. Each tag must be 1-63 characters long,
	// and comply with RFC1035.
	Items []string `json:"items,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Tags: A set of instance tags.

func (Tags) MarshalJSON ¶
added in v0.188.0
func (s Tags) MarshalJSON() ([]byte, error)
type TargetResource ¶
added in v0.200.0
type TargetResource struct {
	// GcpResource: Details of the native Google Cloud resource created as part of
	// restore.
	GcpResource *GcpResource `json:"gcpResource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcpResource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcpResource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetResource: Details of the target resource created/modified as part of restore.

func (TargetResource) MarshalJSON ¶
added in v0.200.0
func (s TargetResource) MarshalJSON() ([]byte, error)
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
type Trial ¶
added in v0.249.0
type Trial struct {
	// EndReason: Output only. The reason for ending the trial.
	//
	// Possible values:
	//   "END_REASON_UNSPECIFIED" - End reason not set.
	//   "MOVE_TO_PAID" - Trial is deliberately ended by the user to transition to
	// paid usage.
	//   "DISCONTINUED" - Trial is discontinued before expiration.
	EndReason string `json:"endReason,omitempty"`
	// EndTime: Output only. The time when the trial will expire.
	EndTime string `json:"endTime,omitempty"`
	// Name: Identifier. The resource name of the trial. Format:
	// projects/{project}/locations/{location}/trial
	Name string `json:"name,omitempty"`
	// StartTime: Output only. The time when the trial was subscribed.
	StartTime string `json:"startTime,omitempty"`
	// State: Output only. The state of the trial.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State not set.
	//   "SUBSCRIBED" - Trial is subscribed.
	//   "UNSUBSCRIBED" - Trial is unsubscribed before expiration.
	//   "EXPIRED" - Trial is expired post 30 days of subscription.
	//   "ELIGIBLE" - Trial is eligible for enablement.
	//   "NOT_ELIGIBLE" - Trial is not eligible for enablement.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EndReason") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndReason") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Trial: Represents a Trial for a project.

func (Trial) MarshalJSON ¶
added in v0.249.0
func (s Trial) MarshalJSON() ([]byte, error)
type TriggerBackupRequest ¶
added in v0.192.0
type TriggerBackupRequest struct {
	// CustomRetentionDays: Optional. The duration for which backup data will be
	// kept, while taking an on-demand backup with custom retention. It is defined
	// in "days". It is mutually exclusive with rule_id. This field is required if
	// rule_id is not provided.
	CustomRetentionDays int64 `json:"customRetentionDays,omitempty"`
	// Labels: Optional. Labels to be applied on the backup.
	Labels map[string]string `json:"labels,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes after the first request. For example,
	// consider a situation where you make an initial request and the request times
	// out. If you make the request again with the same request ID, the server can
	// check if original operation with the same request ID was received, and if
	// so, will ignore the second request. This prevents clients from accidentally
	// creating duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// RuleId: Optional. backup rule_id for which a backup needs to be triggered.
	// If not specified, on-demand backup with custom retention will be triggered.
	RuleId string `json:"ruleId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomRetentionDays") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomRetentionDays") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TriggerBackupRequest: Request message for triggering a backup.

func (TriggerBackupRequest) MarshalJSON ¶
added in v0.192.0
func (s TriggerBackupRequest) MarshalJSON() ([]byte, error)
type WeekDayOfMonth ¶
added in v0.192.0
type WeekDayOfMonth struct {
	// DayOfWeek: Required. Specifies the day of the week.
	//
	// Possible values:
	//   "DAY_OF_WEEK_UNSPECIFIED" - The day of the week is unspecified.
	//   "MONDAY" - Monday
	//   "TUESDAY" - Tuesday
	//   "WEDNESDAY" - Wednesday
	//   "THURSDAY" - Thursday
	//   "FRIDAY" - Friday
	//   "SATURDAY" - Saturday
	//   "SUNDAY" - Sunday
	DayOfWeek string `json:"dayOfWeek,omitempty"`
	// WeekOfMonth: Required. Specifies the week of the month.
	//
	// Possible values:
	//   "WEEK_OF_MONTH_UNSPECIFIED" - The zero value. Do not use.
	//   "FIRST" - The first week of the month.
	//   "SECOND" - The second week of the month.
	//   "THIRD" - The third week of the month.
	//   "FOURTH" - The fourth week of the month.
	//   "LAST" - The last week of the month.
	WeekOfMonth string `json:"weekOfMonth,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DayOfWeek") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DayOfWeek") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WeekDayOfMonth: `WeekDayOfMonth` defines the week day of the month on which the backups will run. The message combines a `WeekOfMonth` and `DayOfWeek` to produce values like `FIRST`/`MONDAY` or `LAST`/`FRIDAY`.

func (WeekDayOfMonth) MarshalJSON ¶
added in v0.192.0
func (s WeekDayOfMonth) MarshalJSON() ([]byte, error)
type WorkforceIdentityBasedManagementURI ¶
added in v0.151.0
type WorkforceIdentityBasedManagementURI struct {
	// FirstPartyManagementUri: Output only. First party Management URI for Google
	// Identities.
	FirstPartyManagementUri string `json:"firstPartyManagementUri,omitempty"`
	// ThirdPartyManagementUri: Output only. Third party Management URI for
	// External Identity Providers.
	ThirdPartyManagementUri string `json:"thirdPartyManagementUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FirstPartyManagementUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirstPartyManagementUri") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WorkforceIdentityBasedManagementURI: ManagementURI depending on the Workforce Identity i.e. either 1p or 3p.

func (WorkforceIdentityBasedManagementURI) MarshalJSON ¶
added in v0.151.0
func (s WorkforceIdentityBasedManagementURI) MarshalJSON() ([]byte, error)
type WorkforceIdentityBasedOAuth2ClientID ¶
added in v0.151.0
type WorkforceIdentityBasedOAuth2ClientID struct {
	// FirstPartyOauth2ClientId: Output only. First party OAuth Client ID for
	// Google Identities.
	FirstPartyOauth2ClientId string `json:"firstPartyOauth2ClientId,omitempty"`
	// ThirdPartyOauth2ClientId: Output only. Third party OAuth Client ID for
	// External Identity Providers.
	ThirdPartyOauth2ClientId string `json:"thirdPartyOauth2ClientId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FirstPartyOauth2ClientId")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirstPartyOauth2ClientId") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WorkforceIdentityBasedOAuth2ClientID: OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p,

func (WorkforceIdentityBasedOAuth2ClientID) MarshalJSON ¶
added in v0.151.0
func (s WorkforceIdentityBasedOAuth2ClientID) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
backupdr-gen.go
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
