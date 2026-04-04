# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/alloydb/v1alpha

Title: alloydb package - google.golang.org/api/alloydb/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/alloydb/v1alpha

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
alloydb
 
v1alpha
alloydb
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

Package alloydb provides access to the AlloyDB API.

For product documentation, see: https://cloud.google.com/alloydb/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/alloydb/v1alpha"
...
ctx := context.Background()
alloydbService, err := alloydb.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

alloydbService, err := alloydb.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
alloydbService, err := alloydb.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AuthorizedNetwork
func (s AuthorizedNetwork) MarshalJSON() ([]byte, error)
type AutoScalingConfig
func (s AutoScalingConfig) MarshalJSON() ([]byte, error)
type AutomatedBackupPolicy
func (s AutomatedBackupPolicy) MarshalJSON() ([]byte, error)
type Backup
func (s Backup) MarshalJSON() ([]byte, error)
type BackupDrBackupSource
func (s BackupDrBackupSource) MarshalJSON() ([]byte, error)
type BackupDrEnabledWindow
func (s BackupDrEnabledWindow) MarshalJSON() ([]byte, error)
type BackupDrInfo
func (s BackupDrInfo) MarshalJSON() ([]byte, error)
type BackupDrPitrSource
func (s BackupDrPitrSource) MarshalJSON() ([]byte, error)
type BackupSource
func (s BackupSource) MarshalJSON() ([]byte, error)
type CancelOperationRequest
type ClientConnectionConfig
func (s ClientConnectionConfig) MarshalJSON() ([]byte, error)
type CloudControl2SharedOperationsReconciliationOperationMetadata
func (s CloudControl2SharedOperationsReconciliationOperationMetadata) MarshalJSON() ([]byte, error)
type CloudSQLBackupRunSource
func (s CloudSQLBackupRunSource) MarshalJSON() ([]byte, error)
type Cluster
func (s Cluster) MarshalJSON() ([]byte, error)
type ClusterUpgradeDetails
func (s ClusterUpgradeDetails) MarshalJSON() ([]byte, error)
type ConnectionInfo
func (s ConnectionInfo) MarshalJSON() ([]byte, error)
type ConnectionPoolConfig
func (s ConnectionPoolConfig) MarshalJSON() ([]byte, error)
type ContinuousBackupConfig
func (s ContinuousBackupConfig) MarshalJSON() ([]byte, error)
type ContinuousBackupInfo
func (s ContinuousBackupInfo) MarshalJSON() ([]byte, error)
type ContinuousBackupSource
func (s ContinuousBackupSource) MarshalJSON() ([]byte, error)
type CpuUtilization
func (s CpuUtilization) MarshalJSON() ([]byte, error)
func (s *CpuUtilization) UnmarshalJSON(data []byte) error
type CsvExportOptions
func (s CsvExportOptions) MarshalJSON() ([]byte, error)
type CsvImportOptions
func (s CsvImportOptions) MarshalJSON() ([]byte, error)
type DataplexConfig
func (s DataplexConfig) MarshalJSON() ([]byte, error)
type DenyMaintenancePeriod
func (s DenyMaintenancePeriod) MarshalJSON() ([]byte, error)
type Empty
type EncryptionConfig
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EncryptionInfo
func (s EncryptionInfo) MarshalJSON() ([]byte, error)
type ExportClusterRequest
func (s ExportClusterRequest) MarshalJSON() ([]byte, error)
type FailoverInstanceRequest
func (s FailoverInstanceRequest) MarshalJSON() ([]byte, error)
type GCAInstanceConfig
func (s GCAInstanceConfig) MarshalJSON() ([]byte, error)
type GcsDestination
func (s GcsDestination) MarshalJSON() ([]byte, error)
type GeminiClusterConfig
func (s GeminiClusterConfig) MarshalJSON() ([]byte, error)
type GeminiInstanceConfig
func (s GeminiInstanceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudLocationListLocationsResponse
func (s GoogleCloudLocationListLocationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudLocationLocation
func (s GoogleCloudLocationLocation) MarshalJSON() ([]byte, error)
type GoogleTypeDate
func (s GoogleTypeDate) MarshalJSON() ([]byte, error)
type GoogleTypeTimeOfDay
func (s GoogleTypeTimeOfDay) MarshalJSON() ([]byte, error)
type ImportClusterRequest
func (s ImportClusterRequest) MarshalJSON() ([]byte, error)
type InjectFaultRequest
func (s InjectFaultRequest) MarshalJSON() ([]byte, error)
type Instance
func (s Instance) MarshalJSON() ([]byte, error)
type InstanceNetworkConfig
func (s InstanceNetworkConfig) MarshalJSON() ([]byte, error)
type InstanceUpgradeDetails
func (s InstanceUpgradeDetails) MarshalJSON() ([]byte, error)
type IntegerRestrictions
func (s IntegerRestrictions) MarshalJSON() ([]byte, error)
type ListBackupsResponse
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListClustersResponse
func (s ListClustersResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListSupportedDatabaseFlagsResponse
func (s ListSupportedDatabaseFlagsResponse) MarshalJSON() ([]byte, error)
type ListUsersResponse
func (s ListUsersResponse) MarshalJSON() ([]byte, error)
type MachineConfig
func (s MachineConfig) MarshalJSON() ([]byte, error)
type MaintenanceSchedule
func (s MaintenanceSchedule) MarshalJSON() ([]byte, error)
type MaintenanceUpdatePolicy
func (s MaintenanceUpdatePolicy) MarshalJSON() ([]byte, error)
type MaintenanceWindow
func (s MaintenanceWindow) MarshalJSON() ([]byte, error)
type MigrationSource
func (s MigrationSource) MarshalJSON() ([]byte, error)
type NetworkConfig
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type Node
func (s Node) MarshalJSON() ([]byte, error)
type ObservabilityInstanceConfig
func (s ObservabilityInstanceConfig) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationMetadata
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type PrimaryConfig
func (s PrimaryConfig) MarshalJSON() ([]byte, error)
type ProjectsLocationsBackupsCreateCall
func (c *ProjectsLocationsBackupsCreateCall) BackupId(backupId string) *ProjectsLocationsBackupsCreateCall
func (c *ProjectsLocationsBackupsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupsCreateCall
func (c *ProjectsLocationsBackupsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsCreateCall
func (c *ProjectsLocationsBackupsCreateCall) Header() http.Header
func (c *ProjectsLocationsBackupsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupsCreateCall
func (c *ProjectsLocationsBackupsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsCreateCall
type ProjectsLocationsBackupsDeleteCall
func (c *ProjectsLocationsBackupsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupsDeleteCall
func (c *ProjectsLocationsBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupsDeleteCall) Etag(etag string) *ProjectsLocationsBackupsDeleteCall
func (c *ProjectsLocationsBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsDeleteCall
func (c *ProjectsLocationsBackupsDeleteCall) Header() http.Header
func (c *ProjectsLocationsBackupsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupsDeleteCall
func (c *ProjectsLocationsBackupsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsDeleteCall
type ProjectsLocationsBackupsGetCall
func (c *ProjectsLocationsBackupsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupsGetCall
func (c *ProjectsLocationsBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)
func (c *ProjectsLocationsBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsGetCall
func (c *ProjectsLocationsBackupsGetCall) Header() http.Header
func (c *ProjectsLocationsBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupsGetCall
func (c *ProjectsLocationsBackupsGetCall) View(view string) *ProjectsLocationsBackupsGetCall
type ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) Context(ctx context.Context) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)
func (c *ProjectsLocationsBackupsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) Filter(filter string) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) Header() http.Header
func (c *ProjectsLocationsBackupsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) PageToken(pageToken string) *ProjectsLocationsBackupsListCall
func (c *ProjectsLocationsBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error
func (c *ProjectsLocationsBackupsListCall) View(view string) *ProjectsLocationsBackupsListCall
type ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) Header() http.Header
func (c *ProjectsLocationsBackupsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupsPatchCall
func (c *ProjectsLocationsBackupsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsPatchCall
type ProjectsLocationsBackupsService
func NewProjectsLocationsBackupsService(s *Service) *ProjectsLocationsBackupsService
func (r *ProjectsLocationsBackupsService) Create(parent string, backup *Backup) *ProjectsLocationsBackupsCreateCall
func (r *ProjectsLocationsBackupsService) Delete(name string) *ProjectsLocationsBackupsDeleteCall
func (r *ProjectsLocationsBackupsService) Get(name string) *ProjectsLocationsBackupsGetCall
func (r *ProjectsLocationsBackupsService) List(parent string) *ProjectsLocationsBackupsListCall
func (r *ProjectsLocationsBackupsService) Patch(name string, backup *Backup) *ProjectsLocationsBackupsPatchCall
type ProjectsLocationsClustersCreateCall
func (c *ProjectsLocationsClustersCreateCall) ClusterId(clusterId string) *ProjectsLocationsClustersCreateCall
func (c *ProjectsLocationsClustersCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersCreateCall
func (c *ProjectsLocationsClustersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersCreateCall
func (c *ProjectsLocationsClustersCreateCall) Header() http.Header
func (c *ProjectsLocationsClustersCreateCall) RequestId(requestId string) *ProjectsLocationsClustersCreateCall
func (c *ProjectsLocationsClustersCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersCreateCall
type ProjectsLocationsClustersCreatesecondaryCall
func (c *ProjectsLocationsClustersCreatesecondaryCall) ClusterId(clusterId string) *ProjectsLocationsClustersCreatesecondaryCall
func (c *ProjectsLocationsClustersCreatesecondaryCall) Context(ctx context.Context) *ProjectsLocationsClustersCreatesecondaryCall
func (c *ProjectsLocationsClustersCreatesecondaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersCreatesecondaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersCreatesecondaryCall
func (c *ProjectsLocationsClustersCreatesecondaryCall) Header() http.Header
func (c *ProjectsLocationsClustersCreatesecondaryCall) RequestId(requestId string) *ProjectsLocationsClustersCreatesecondaryCall
func (c *ProjectsLocationsClustersCreatesecondaryCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersCreatesecondaryCall
type ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersDeleteCall) Etag(etag string) *ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) Force(force bool) *ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) Header() http.Header
func (c *ProjectsLocationsClustersDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersDeleteCall
func (c *ProjectsLocationsClustersDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersDeleteCall
type ProjectsLocationsClustersExportCall
func (c *ProjectsLocationsClustersExportCall) Context(ctx context.Context) *ProjectsLocationsClustersExportCall
func (c *ProjectsLocationsClustersExportCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersExportCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersExportCall
func (c *ProjectsLocationsClustersExportCall) Header() http.Header
type ProjectsLocationsClustersGetCall
func (c *ProjectsLocationsClustersGetCall) Context(ctx context.Context) *ProjectsLocationsClustersGetCall
func (c *ProjectsLocationsClustersGetCall) Do(opts ...googleapi.CallOption) (*Cluster, error)
func (c *ProjectsLocationsClustersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersGetCall
func (c *ProjectsLocationsClustersGetCall) Header() http.Header
func (c *ProjectsLocationsClustersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersGetCall
func (c *ProjectsLocationsClustersGetCall) View(view string) *ProjectsLocationsClustersGetCall
type ProjectsLocationsClustersImportCall
func (c *ProjectsLocationsClustersImportCall) Context(ctx context.Context) *ProjectsLocationsClustersImportCall
func (c *ProjectsLocationsClustersImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersImportCall
func (c *ProjectsLocationsClustersImportCall) Header() http.Header
type ProjectsLocationsClustersInstancesCreateCall
func (c *ProjectsLocationsClustersInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesCreateCall
func (c *ProjectsLocationsClustersInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesCreateCall
func (c *ProjectsLocationsClustersInstancesCreateCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesCreateCall) InstanceId(instanceId string) *ProjectsLocationsClustersInstancesCreateCall
func (c *ProjectsLocationsClustersInstancesCreateCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesCreateCall
func (c *ProjectsLocationsClustersInstancesCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesCreateCall
type ProjectsLocationsClustersInstancesCreatesecondaryCall
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesCreatesecondaryCall
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesCreatesecondaryCall
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) InstanceId(instanceId string) *ProjectsLocationsClustersInstancesCreatesecondaryCall
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesCreatesecondaryCall
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesCreatesecondaryCall
type ProjectsLocationsClustersInstancesDeleteCall
func (c *ProjectsLocationsClustersInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesDeleteCall
func (c *ProjectsLocationsClustersInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesDeleteCall) Etag(etag string) *ProjectsLocationsClustersInstancesDeleteCall
func (c *ProjectsLocationsClustersInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesDeleteCall
func (c *ProjectsLocationsClustersInstancesDeleteCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesDeleteCall
func (c *ProjectsLocationsClustersInstancesDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesDeleteCall
type ProjectsLocationsClustersInstancesFailoverCall
func (c *ProjectsLocationsClustersInstancesFailoverCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesFailoverCall
func (c *ProjectsLocationsClustersInstancesFailoverCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesFailoverCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesFailoverCall
func (c *ProjectsLocationsClustersInstancesFailoverCall) Header() http.Header
type ProjectsLocationsClustersInstancesGetCall
func (c *ProjectsLocationsClustersInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesGetCall
func (c *ProjectsLocationsClustersInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsLocationsClustersInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesGetCall
func (c *ProjectsLocationsClustersInstancesGetCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesGetCall
func (c *ProjectsLocationsClustersInstancesGetCall) View(view string) *ProjectsLocationsClustersInstancesGetCall
type ProjectsLocationsClustersInstancesGetConnectionInfoCall
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesGetConnectionInfoCall
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Do(opts ...googleapi.CallOption) (*ConnectionInfo, error)
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesGetConnectionInfoCall
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall
type ProjectsLocationsClustersInstancesInjectFaultCall
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesInjectFaultCall
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesInjectFaultCall
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Header() http.Header
type ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)
func (c *ProjectsLocationsClustersInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) Filter(filter string) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) OrderBy(orderBy string) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) PageToken(pageToken string) *ProjectsLocationsClustersInstancesListCall
func (c *ProjectsLocationsClustersInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error
type ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) Header() http.Header
func (c *ProjectsLocationsClustersInstancesPatchCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersInstancesPatchCall
func (c *ProjectsLocationsClustersInstancesPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesPatchCall
type ProjectsLocationsClustersInstancesRestartCall
func (c *ProjectsLocationsClustersInstancesRestartCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesRestartCall
func (c *ProjectsLocationsClustersInstancesRestartCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersInstancesRestartCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesRestartCall
func (c *ProjectsLocationsClustersInstancesRestartCall) Header() http.Header
type ProjectsLocationsClustersInstancesService
func NewProjectsLocationsClustersInstancesService(s *Service) *ProjectsLocationsClustersInstancesService
func (r *ProjectsLocationsClustersInstancesService) Create(parent string, instance *Instance) *ProjectsLocationsClustersInstancesCreateCall
func (r *ProjectsLocationsClustersInstancesService) Createsecondary(parent string, instance *Instance) *ProjectsLocationsClustersInstancesCreatesecondaryCall
func (r *ProjectsLocationsClustersInstancesService) Delete(name string) *ProjectsLocationsClustersInstancesDeleteCall
func (r *ProjectsLocationsClustersInstancesService) Failover(name string, failoverinstancerequest *FailoverInstanceRequest) *ProjectsLocationsClustersInstancesFailoverCall
func (r *ProjectsLocationsClustersInstancesService) Get(name string) *ProjectsLocationsClustersInstancesGetCall
func (r *ProjectsLocationsClustersInstancesService) GetConnectionInfo(parent string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall
func (r *ProjectsLocationsClustersInstancesService) InjectFault(name string, injectfaultrequest *InjectFaultRequest) *ProjectsLocationsClustersInstancesInjectFaultCall
func (r *ProjectsLocationsClustersInstancesService) List(parent string) *ProjectsLocationsClustersInstancesListCall
func (r *ProjectsLocationsClustersInstancesService) Patch(name string, instance *Instance) *ProjectsLocationsClustersInstancesPatchCall
func (r *ProjectsLocationsClustersInstancesService) Restart(name string, restartinstancerequest *RestartInstanceRequest) *ProjectsLocationsClustersInstancesRestartCall
type ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) Context(ctx context.Context) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) Do(opts ...googleapi.CallOption) (*ListClustersResponse, error)
func (c *ProjectsLocationsClustersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) Filter(filter string) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) Header() http.Header
func (c *ProjectsLocationsClustersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) OrderBy(orderBy string) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) PageSize(pageSize int64) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) PageToken(pageToken string) *ProjectsLocationsClustersListCall
func (c *ProjectsLocationsClustersListCall) Pages(ctx context.Context, f func(*ListClustersResponse) error) error
type ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) Header() http.Header
func (c *ProjectsLocationsClustersPatchCall) RequestId(requestId string) *ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersPatchCall
func (c *ProjectsLocationsClustersPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersPatchCall
type ProjectsLocationsClustersPromoteCall
func (c *ProjectsLocationsClustersPromoteCall) Context(ctx context.Context) *ProjectsLocationsClustersPromoteCall
func (c *ProjectsLocationsClustersPromoteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersPromoteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersPromoteCall
func (c *ProjectsLocationsClustersPromoteCall) Header() http.Header
type ProjectsLocationsClustersRestoreCall
func (c *ProjectsLocationsClustersRestoreCall) Context(ctx context.Context) *ProjectsLocationsClustersRestoreCall
func (c *ProjectsLocationsClustersRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersRestoreCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersRestoreCall
func (c *ProjectsLocationsClustersRestoreCall) Header() http.Header
type ProjectsLocationsClustersRestoreFromCloudSQLCall
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Context(ctx context.Context) *ProjectsLocationsClustersRestoreFromCloudSQLCall
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersRestoreFromCloudSQLCall
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Header() http.Header
type ProjectsLocationsClustersService
func NewProjectsLocationsClustersService(s *Service) *ProjectsLocationsClustersService
func (r *ProjectsLocationsClustersService) Create(parent string, cluster *Cluster) *ProjectsLocationsClustersCreateCall
func (r *ProjectsLocationsClustersService) Createsecondary(parent string, cluster *Cluster) *ProjectsLocationsClustersCreatesecondaryCall
func (r *ProjectsLocationsClustersService) Delete(name string) *ProjectsLocationsClustersDeleteCall
func (r *ProjectsLocationsClustersService) Export(name string, exportclusterrequest *ExportClusterRequest) *ProjectsLocationsClustersExportCall
func (r *ProjectsLocationsClustersService) Get(name string) *ProjectsLocationsClustersGetCall
func (r *ProjectsLocationsClustersService) Import(name string, importclusterrequest *ImportClusterRequest) *ProjectsLocationsClustersImportCall
func (r *ProjectsLocationsClustersService) List(parent string) *ProjectsLocationsClustersListCall
func (r *ProjectsLocationsClustersService) Patch(name string, cluster *Cluster) *ProjectsLocationsClustersPatchCall
func (r *ProjectsLocationsClustersService) Promote(name string, promoteclusterrequest *PromoteClusterRequest) *ProjectsLocationsClustersPromoteCall
func (r *ProjectsLocationsClustersService) Restore(parent string, restoreclusterrequest *RestoreClusterRequest) *ProjectsLocationsClustersRestoreCall
func (r *ProjectsLocationsClustersService) RestoreFromCloudSQL(parent string, restorefromcloudsqlrequest *RestoreFromCloudSQLRequest) *ProjectsLocationsClustersRestoreFromCloudSQLCall
func (r *ProjectsLocationsClustersService) Switchover(name string, switchoverclusterrequest *SwitchoverClusterRequest) *ProjectsLocationsClustersSwitchoverCall
func (r *ProjectsLocationsClustersService) Upgrade(name string, upgradeclusterrequest *UpgradeClusterRequest) *ProjectsLocationsClustersUpgradeCall
type ProjectsLocationsClustersSwitchoverCall
func (c *ProjectsLocationsClustersSwitchoverCall) Context(ctx context.Context) *ProjectsLocationsClustersSwitchoverCall
func (c *ProjectsLocationsClustersSwitchoverCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersSwitchoverCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersSwitchoverCall
func (c *ProjectsLocationsClustersSwitchoverCall) Header() http.Header
type ProjectsLocationsClustersUpgradeCall
func (c *ProjectsLocationsClustersUpgradeCall) Context(ctx context.Context) *ProjectsLocationsClustersUpgradeCall
func (c *ProjectsLocationsClustersUpgradeCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsClustersUpgradeCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUpgradeCall
func (c *ProjectsLocationsClustersUpgradeCall) Header() http.Header
type ProjectsLocationsClustersUsersCreateCall
func (c *ProjectsLocationsClustersUsersCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersCreateCall
func (c *ProjectsLocationsClustersUsersCreateCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *ProjectsLocationsClustersUsersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersCreateCall
func (c *ProjectsLocationsClustersUsersCreateCall) Header() http.Header
func (c *ProjectsLocationsClustersUsersCreateCall) RequestId(requestId string) *ProjectsLocationsClustersUsersCreateCall
func (c *ProjectsLocationsClustersUsersCreateCall) UserId(userId string) *ProjectsLocationsClustersUsersCreateCall
func (c *ProjectsLocationsClustersUsersCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersCreateCall
type ProjectsLocationsClustersUsersDeleteCall
func (c *ProjectsLocationsClustersUsersDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersDeleteCall
func (c *ProjectsLocationsClustersUsersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsClustersUsersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersDeleteCall
func (c *ProjectsLocationsClustersUsersDeleteCall) Header() http.Header
func (c *ProjectsLocationsClustersUsersDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersUsersDeleteCall
func (c *ProjectsLocationsClustersUsersDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersDeleteCall
type ProjectsLocationsClustersUsersGetCall
func (c *ProjectsLocationsClustersUsersGetCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersGetCall
func (c *ProjectsLocationsClustersUsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *ProjectsLocationsClustersUsersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersGetCall
func (c *ProjectsLocationsClustersUsersGetCall) Header() http.Header
func (c *ProjectsLocationsClustersUsersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersUsersGetCall
type ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) Do(opts ...googleapi.CallOption) (*ListUsersResponse, error)
func (c *ProjectsLocationsClustersUsersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) Filter(filter string) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) Header() http.Header
func (c *ProjectsLocationsClustersUsersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) OrderBy(orderBy string) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) PageSize(pageSize int64) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) PageToken(pageToken string) *ProjectsLocationsClustersUsersListCall
func (c *ProjectsLocationsClustersUsersListCall) Pages(ctx context.Context, f func(*ListUsersResponse) error) error
type ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *ProjectsLocationsClustersUsersPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) Header() http.Header
func (c *ProjectsLocationsClustersUsersPatchCall) RequestId(requestId string) *ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersUsersPatchCall
func (c *ProjectsLocationsClustersUsersPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersPatchCall
type ProjectsLocationsClustersUsersService
func NewProjectsLocationsClustersUsersService(s *Service) *ProjectsLocationsClustersUsersService
func (r *ProjectsLocationsClustersUsersService) Create(parent string, user *User) *ProjectsLocationsClustersUsersCreateCall
func (r *ProjectsLocationsClustersUsersService) Delete(name string) *ProjectsLocationsClustersUsersDeleteCall
func (r *ProjectsLocationsClustersUsersService) Get(name string) *ProjectsLocationsClustersUsersGetCall
func (r *ProjectsLocationsClustersUsersService) List(parent string) *ProjectsLocationsClustersUsersListCall
func (r *ProjectsLocationsClustersUsersService) Patch(name string, user *User) *ProjectsLocationsClustersUsersPatchCall
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
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Context(ctx context.Context) *ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Do(opts ...googleapi.CallOption) (*ListSupportedDatabaseFlagsResponse, error)
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Header() http.Header
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) PageSize(pageSize int64) *ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) PageToken(pageToken string) *ProjectsLocationsSupportedDatabaseFlagsListCall
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Pages(ctx context.Context, f func(*ListSupportedDatabaseFlagsResponse) error) error
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Scope(scope string) *ProjectsLocationsSupportedDatabaseFlagsListCall
type ProjectsLocationsSupportedDatabaseFlagsService
func NewProjectsLocationsSupportedDatabaseFlagsService(s *Service) *ProjectsLocationsSupportedDatabaseFlagsService
func (r *ProjectsLocationsSupportedDatabaseFlagsService) List(parent string) *ProjectsLocationsSupportedDatabaseFlagsListCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type PromoteClusterRequest
func (s PromoteClusterRequest) MarshalJSON() ([]byte, error)
type PscAutoConnectionConfig
func (s PscAutoConnectionConfig) MarshalJSON() ([]byte, error)
type PscConfig
func (s PscConfig) MarshalJSON() ([]byte, error)
type PscInstanceConfig
func (s PscInstanceConfig) MarshalJSON() ([]byte, error)
type PscInterfaceConfig
func (s PscInterfaceConfig) MarshalJSON() ([]byte, error)
type QuantityBasedExpiry
func (s QuantityBasedExpiry) MarshalJSON() ([]byte, error)
type QuantityBasedRetention
func (s QuantityBasedRetention) MarshalJSON() ([]byte, error)
type QueryInsightsInstanceConfig
func (s QueryInsightsInstanceConfig) MarshalJSON() ([]byte, error)
type ReadPoolConfig
func (s ReadPoolConfig) MarshalJSON() ([]byte, error)
type ReadPoolInstancesUpgradeStageStatus
func (s ReadPoolInstancesUpgradeStageStatus) MarshalJSON() ([]byte, error)
type RestartInstanceRequest
func (s RestartInstanceRequest) MarshalJSON() ([]byte, error)
type RestoreClusterRequest
func (s RestoreClusterRequest) MarshalJSON() ([]byte, error)
type RestoreFromCloudSQLRequest
func (s RestoreFromCloudSQLRequest) MarshalJSON() ([]byte, error)
type Schedule
func (s Schedule) MarshalJSON() ([]byte, error)
type SecondaryConfig
func (s SecondaryConfig) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SqlExportOptions
func (s SqlExportOptions) MarshalJSON() ([]byte, error)
type SqlImportOptions
type SslConfig
func (s SslConfig) MarshalJSON() ([]byte, error)
type StageInfo
func (s StageInfo) MarshalJSON() ([]byte, error)
type StageStatus
func (s StageStatus) MarshalJSON() ([]byte, error)
type Stats
func (s Stats) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration
func (s StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupConfiguration
func (s StorageDatabasecenterPartnerapiV1mainBackupConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration
func (s StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupDRMetadata
func (s StorageDatabasecenterPartnerapiV1mainBackupDRMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupRun
func (s StorageDatabasecenterPartnerapiV1mainBackupRun) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainCompliance
func (s StorageDatabasecenterPartnerapiV1mainCompliance) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData
func (s StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainCustomMetadataData
func (s StorageDatabasecenterPartnerapiV1mainCustomMetadataData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceId) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainEntitlement
func (s StorageDatabasecenterPartnerapiV1mainEntitlement) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration
func (s StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata
func (s StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainMachineConfiguration
func (s StorageDatabasecenterPartnerapiV1mainMachineConfiguration) MarshalJSON() ([]byte, error)
func (s *StorageDatabasecenterPartnerapiV1mainMachineConfiguration) UnmarshalJSON(data []byte) error
type StorageDatabasecenterPartnerapiV1mainObservabilityMetricData
func (s StorageDatabasecenterPartnerapiV1mainObservabilityMetricData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainOperationError
func (s StorageDatabasecenterPartnerapiV1mainOperationError) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceFlags
func (s StorageDatabasecenterPartnerapiV1mainResourceFlags) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainRetentionSettings
func (s StorageDatabasecenterPartnerapiV1mainRetentionSettings) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainTags
func (s StorageDatabasecenterPartnerapiV1mainTags) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance
func (s StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainUserLabels
func (s StorageDatabasecenterPartnerapiV1mainUserLabels) MarshalJSON() ([]byte, error)
type StorageDatabasecenterProtoCommonProduct
func (s StorageDatabasecenterProtoCommonProduct) MarshalJSON() ([]byte, error)
type StorageDatabasecenterProtoCommonTypedValue
func (s StorageDatabasecenterProtoCommonTypedValue) MarshalJSON() ([]byte, error)
func (s *StorageDatabasecenterProtoCommonTypedValue) UnmarshalJSON(data []byte) error
type StringRestrictions
func (s StringRestrictions) MarshalJSON() ([]byte, error)
type SupportedDatabaseFlag
func (s SupportedDatabaseFlag) MarshalJSON() ([]byte, error)
type SwitchoverClusterRequest
func (s SwitchoverClusterRequest) MarshalJSON() ([]byte, error)
type TimeBasedRetention
func (s TimeBasedRetention) MarshalJSON() ([]byte, error)
type TrialMetadata
func (s TrialMetadata) MarshalJSON() ([]byte, error)
type UpdatePolicy
func (s UpdatePolicy) MarshalJSON() ([]byte, error)
type UpgradeClusterRequest
func (s UpgradeClusterRequest) MarshalJSON() ([]byte, error)
type UpgradeClusterResponse
func (s UpgradeClusterResponse) MarshalJSON() ([]byte, error)
type UpgradeClusterStatus
func (s UpgradeClusterStatus) MarshalJSON() ([]byte, error)
type User
func (s User) MarshalJSON() ([]byte, error)
type UserPassword
func (s UserPassword) MarshalJSON() ([]byte, error)
type WeeklySchedule
func (s WeeklySchedule) MarshalJSON() ([]byte, error)
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
type AuthorizedNetwork ¶
added in v0.155.0
type AuthorizedNetwork struct {
	// CidrRange: CIDR range for one authorzied network of the instance.
	CidrRange string `json:"cidrRange,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CidrRange") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CidrRange") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuthorizedNetwork: AuthorizedNetwork contains metadata for an authorized network.

func (AuthorizedNetwork) MarshalJSON ¶
added in v0.155.0
func (s AuthorizedNetwork) MarshalJSON() ([]byte, error)
type AutoScalingConfig ¶
added in v0.252.0
type AutoScalingConfig struct {
	// Policy: Policy for the MIG autoscaler.
	Policy *Policy `json:"policy,omitempty"`
	// Schedules: Optional list of schedules for the MIG autoscaler. If not set, no
	// schedules are created.
	Schedules []*Schedule `json:"schedules,omitempty"`
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

AutoScalingConfig: Configuration for autoscaling.

func (AutoScalingConfig) MarshalJSON ¶
added in v0.252.0
func (s AutoScalingConfig) MarshalJSON() ([]byte, error)
type AutomatedBackupPolicy ¶
type AutomatedBackupPolicy struct {
	// BackupWindow: The length of the time window during which a backup can be
	// taken. If a backup does not succeed within this time window, it will be
	// canceled and considered failed. The backup window must be at least 5 minutes
	// long. There is no upper bound on the window. If not set, it defaults to 1
	// hour.
	BackupWindow string `json:"backupWindow,omitempty"`
	// Enabled: Whether automated automated backups are enabled. If not set,
	// defaults to true.
	Enabled bool `json:"enabled,omitempty"`
	// EncryptionConfig: Optional. The encryption config can be specified to
	// encrypt the backups with a customer-managed encryption key (CMEK). When this
	// field is not specified, the backup will use the cluster's encryption config.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// Labels: Labels to apply to backups created using this configuration.
	Labels map[string]string `json:"labels,omitempty"`
	// Location: The location where the backup will be stored. Currently, the only
	// supported option is to store the backup in the same region as the cluster.
	// If empty, defaults to the region of the cluster.
	Location string `json:"location,omitempty"`
	// QuantityBasedRetention: Quantity-based Backup retention policy to retain
	// recent backups.
	QuantityBasedRetention *QuantityBasedRetention `json:"quantityBasedRetention,omitempty"`
	// TimeBasedRetention: Time-based Backup retention policy.
	TimeBasedRetention *TimeBasedRetention `json:"timeBasedRetention,omitempty"`
	// WeeklySchedule: Weekly schedule for the Backup.
	WeeklySchedule *WeeklySchedule `json:"weeklySchedule,omitempty"`
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

AutomatedBackupPolicy: Message describing the user-specified automated backup policy. All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set.

func (AutomatedBackupPolicy) MarshalJSON ¶
func (s AutomatedBackupPolicy) MarshalJSON() ([]byte, error)
type Backup ¶
type Backup struct {
	// Annotations: Annotations to allow client tools to store small amount of
	// arbitrary data. This is distinct from labels. https://google.aip.dev/128
	Annotations map[string]string `json:"annotations,omitempty"`
	// ClusterDeleted: Output only. Set to true if the cluster corresponding to
	// this backup is deleted. This field is only populated for when using the
	// BACKUP_VIEW_CLUSTER_DELETED view.
	ClusterDeleted bool `json:"clusterDeleted,omitempty"`
	// ClusterName: Required. The full resource name of the backup source cluster
	// (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).
	ClusterName string `json:"clusterName,omitempty"`
	// ClusterUid: Output only. The system-generated UID of the cluster which was
	// used to create this resource.
	ClusterUid string `json:"clusterUid,omitempty"`
	// CreateCompletionTime: Output only. Timestamp when the resource finished
	// being created.
	CreateCompletionTime string `json:"createCompletionTime,omitempty"`
	// CreateTime: Output only. Create time stamp
	CreateTime string `json:"createTime,omitempty"`
	// DatabaseVersion: Output only. The database engine major version of the
	// cluster this backup was created from. Any restored cluster created from this
	// backup will have the same database version.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	DatabaseVersion string `json:"databaseVersion,omitempty"`
	// DeleteTime: Output only. Delete time stamp
	DeleteTime string `json:"deleteTime,omitempty"`
	// Description: User-provided description of the backup.
	Description string `json:"description,omitempty"`
	// DisplayName: User-settable and human-readable display name for the Backup.
	DisplayName string `json:"displayName,omitempty"`
	// EncryptionConfig: Optional. The encryption config can be specified to
	// encrypt the backup with a customer-managed encryption key (CMEK). When this
	// field is not specified, the backup will then use default encryption scheme
	// to protect the user data.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// EncryptionInfo: Output only. The encryption information for the backup.
	EncryptionInfo *EncryptionInfo `json:"encryptionInfo,omitempty"`
	// Etag: For Resource freshness validation (https://google.aip.dev/154)
	Etag string `json:"etag,omitempty"`
	// ExpiryQuantity: Output only. The QuantityBasedExpiry of the backup,
	// specified by the backup's retention policy. Once the expiry quantity is over
	// retention, the backup is eligible to be garbage collected.
	ExpiryQuantity *QuantityBasedExpiry `json:"expiryQuantity,omitempty"`
	// ExpiryTime: Output only. The time at which after the backup is eligible to
	// be garbage collected. It is the duration specified by the backup's retention
	// policy, added to the backup's create_time.
	ExpiryTime string `json:"expiryTime,omitempty"`
	// Labels: Labels as key value pairs
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Output only. The name of the backup resource with the format: *
	// projects/{project}/locations/{region}/backups/{backup_id} where the cluster
	// and backup ID segments should satisfy the regex expression
	// `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase
	// letters, numbers, and dashes, starting with a letter, and ending with a
	// letter or number. For more details see https://google.aip.dev/122. The
	// prefix of the backup resource name is the name of the parent resource: *
	// projects/{project}/locations/{region}
	Name string `json:"name,omitempty"`
	// Reconciling: Output only. Reconciling
	// (https://google.aip.dev/128#reconciliation), if true, indicates that the
	// service is actively updating the resource. This can happen due to
	// user-triggered updates or system actions like failover or maintenance.
	Reconciling bool `json:"reconciling,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// SizeBytes: Output only. The size of the backup in bytes.
	SizeBytes int64 `json:"sizeBytes,omitempty,string"`
	// State: Output only. The current state of the backup.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The state of the backup is unknown.
	//   "READY" - The backup is ready.
	//   "CREATING" - The backup is creating.
	//   "FAILED" - The backup failed.
	//   "DELETING" - The backup is being deleted.
	State string `json:"state,omitempty"`
	// Tags: Optional. Input only. Immutable. Tag keys/values directly bound to
	// this resource. For example: “` "123/environment": "production",
	// "123/costCenter": "marketing" “`
	Tags map[string]string `json:"tags,omitempty"`
	// Type: The backup type, which suggests the trigger for the backup.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Backup Type is unknown.
	//   "ON_DEMAND" - ON_DEMAND backups that were triggered by the customer (e.g.,
	// not AUTOMATED).
	//   "AUTOMATED" - AUTOMATED backups triggered by the automated backups
	// scheduler pursuant to an automated backup policy.
	//   "CONTINUOUS" - CONTINUOUS backups triggered by the automated backups
	// scheduler due to a continuous backup policy.
	Type string `json:"type,omitempty"`
	// Uid: Output only. The system-generated UID of the resource. The UID is
	// assigned when the resource is created, and it is retained until it is
	// deleted.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Update time stamp Users should not infer any
	// meaning from this field. Its value is generally unrelated to the timing of
	// the backup creation operation.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

Backup: Message describing Backup object

func (Backup) MarshalJSON ¶
func (s Backup) MarshalJSON() ([]byte, error)
type BackupDrBackupSource ¶
added in v0.252.0
type BackupDrBackupSource struct {
	// Backup: Required. The name of the backup resource with the format: *
	// projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSou
	// rces/{datasource_id}/backups/{backup_id}
	Backup string `json:"backup,omitempty"`
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

BackupDrBackupSource: Message describing a BackupDrBackupSource.

func (BackupDrBackupSource) MarshalJSON ¶
added in v0.252.0
func (s BackupDrBackupSource) MarshalJSON() ([]byte, error)
type BackupDrEnabledWindow ¶
added in v0.252.0
type BackupDrEnabledWindow struct {
	// AutomatedBackupPreviouslyEnabled: Whether automated backup was previously
	// enabled prior to enabling BackupDR protection for this cluster.
	AutomatedBackupPreviouslyEnabled bool `json:"automatedBackupPreviouslyEnabled,omitempty"`
	// BackupPlanAssociation: The BackupPlanAssociation resource that was used to
	// enable BackupDR protection for this cluster.
	BackupPlanAssociation string `json:"backupPlanAssociation,omitempty"`
	// ContinuousBackupPreviousRecoveryWindowDays: The retention set for the
	// continuous backup that was previously enabled prior to enabling BackupDR
	// protection for this cluster.
	ContinuousBackupPreviousRecoveryWindowDays int64 `json:"continuousBackupPreviousRecoveryWindowDays,omitempty"`
	// ContinuousBackupPreviouslyEnabled: Whether continuous backup was previously
	// enabled prior to enabling BackupDR protection for this cluster.
	ContinuousBackupPreviouslyEnabled bool `json:"continuousBackupPreviouslyEnabled,omitempty"`
	// ContinuousBackupPreviouslyEnabledTime: The time when continuous backup was
	// previously enabled prior to enabling BackupDR protection for this cluster.
	ContinuousBackupPreviouslyEnabledTime string `json:"continuousBackupPreviouslyEnabledTime,omitempty"`
	// DataSource: The DataSource resource that represents the cluster in BackupDR.
	DataSource string `json:"dataSource,omitempty"`
	// DisabledTime: Time when the BackupDR protection for this cluster was
	// disabled. This field will be empty if this BackupDR window is the
	// `current_window`.
	DisabledTime string `json:"disabledTime,omitempty"`
	// EnabledTime: Time when the BackupDR protection for this cluster was enabled.
	EnabledTime string `json:"enabledTime,omitempty"`
	// LogRetentionPeriod: The retention period for logs generated by BackupDR for
	// this cluster.
	LogRetentionPeriod string `json:"logRetentionPeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AutomatedBackupPreviouslyEnabled") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AutomatedBackupPreviouslyEnabled") to include in API requests with the JSON
	// null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

BackupDrEnabledWindow: Information about a single window when BackupDR was enabled for this cluster.

func (BackupDrEnabledWindow) MarshalJSON ¶
added in v0.252.0
func (s BackupDrEnabledWindow) MarshalJSON() ([]byte, error)
type BackupDrInfo ¶
added in v0.252.0
type BackupDrInfo struct {
	// CurrentWindow: The current BackupDR configuration for this cluster. If
	// BackupDR protection is not enabled for this cluster, this field will be
	// empty.
	CurrentWindow *BackupDrEnabledWindow `json:"currentWindow,omitempty"`
	// PreviousWindows: Windows during which BackupDR was enabled for this cluster,
	// along with associated configuration for that window. These are used to
	// determine points-in-time for which restores can be performed. The windows
	// are ordered with the most recent window last. Windows are mutally exclusive.
	// Windows which closed more than 1 year ago will be removed from this list.
	PreviousWindows []*BackupDrEnabledWindow `json:"previousWindows,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentWindow") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentWindow") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupDrInfo: Information about BackupDR protection for this cluster.

func (BackupDrInfo) MarshalJSON ¶
added in v0.252.0
func (s BackupDrInfo) MarshalJSON() ([]byte, error)
type BackupDrPitrSource ¶
added in v0.252.0
type BackupDrPitrSource struct {
	// DataSource: Required. The name of the backup resource with the format: *
	// projects/{project}/locations/{location}/backupVaults/{backupvault_id}/dataSou
	// rces/{datasource_id}
	DataSource string `json:"dataSource,omitempty"`
	// PointInTime: Required. The point in time to restore to.
	PointInTime string `json:"pointInTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DataSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupDrPitrSource: Message describing a BackupDrPitrSource.

func (BackupDrPitrSource) MarshalJSON ¶
added in v0.252.0
func (s BackupDrPitrSource) MarshalJSON() ([]byte, error)
type BackupSource ¶
type BackupSource struct {
	// BackupName: Required. The name of the backup resource with the format: *
	// projects/{project}/locations/{region}/backups/{backup_id}
	BackupName string `json:"backupName,omitempty"`
	// BackupUid: Output only. The system-generated UID of the backup which was
	// used to create this resource. The UID is generated when the backup is
	// created, and it is retained until the backup is deleted.
	BackupUid string `json:"backupUid,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BackupSource: Message describing a BackupSource.

func (BackupSource) MarshalJSON ¶
func (s BackupSource) MarshalJSON() ([]byte, error)
type CancelOperationRequest ¶
type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type ClientConnectionConfig ¶
type ClientConnectionConfig struct {
	// RequireConnectors: Optional. Configuration to enforce connectors only (ex:
	// AuthProxy) connections to the database.
	RequireConnectors bool `json:"requireConnectors,omitempty"`
	// SslConfig: Optional. SSL configuration option for this instance.
	SslConfig *SslConfig `json:"sslConfig,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RequireConnectors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RequireConnectors") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClientConnectionConfig: Client connection configuration

func (ClientConnectionConfig) MarshalJSON ¶
func (s ClientConnectionConfig) MarshalJSON() ([]byte, error)
type CloudControl2SharedOperationsReconciliationOperationMetadata ¶
type CloudControl2SharedOperationsReconciliationOperationMetadata struct {
	// DeleteResource: DEPRECATED. Use exclusive_action instead.
	DeleteResource bool `json:"deleteResource,omitempty"`
	// ExclusiveAction: Excluisive action returned by the CLH.
	//
	// Possible values:
	//   "UNKNOWN_REPAIR_ACTION" - Unknown repair action.
	//   "DELETE" - The resource has to be deleted. When using this bit, the CLH
	// should fail the operation. DEPRECATED. Instead use DELETE_RESOURCE
	// OperationSignal in SideChannel.
	//   "RETRY" - This resource could not be repaired but the repair should be
	// tried again at a later time. This can happen if there is a dependency that
	// needs to be resolved first- e.g. if a parent resource must be repaired
	// before a child resource.
	ExclusiveAction string `json:"exclusiveAction,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeleteResource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeleteResource") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudControl2SharedOperationsReconciliationOperationMetadata: Operation metadata returned by the CLH during resource state reconciliation.

func (CloudControl2SharedOperationsReconciliationOperationMetadata) MarshalJSON ¶
func (s CloudControl2SharedOperationsReconciliationOperationMetadata) MarshalJSON() ([]byte, error)
type CloudSQLBackupRunSource ¶
added in v0.193.0
type CloudSQLBackupRunSource struct {
	// BackupRunId: Required. The CloudSQL backup run ID.
	BackupRunId int64 `json:"backupRunId,omitempty,string"`
	// InstanceId: Required. The CloudSQL instance ID.
	InstanceId string `json:"instanceId,omitempty"`
	// Project: The project ID of the source CloudSQL instance. This should be the
	// same as the AlloyDB cluster's project.
	Project string `json:"project,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupRunId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupRunId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSQLBackupRunSource: The source CloudSQL backup resource.

func (CloudSQLBackupRunSource) MarshalJSON ¶
added in v0.193.0
func (s CloudSQLBackupRunSource) MarshalJSON() ([]byte, error)
type Cluster ¶
type Cluster struct {
	// Annotations: Annotations to allow client tools to store small amount of
	// arbitrary data. This is distinct from labels. https://google.aip.dev/128
	Annotations map[string]string `json:"annotations,omitempty"`
	// AutomatedBackupPolicy: The automated backup policy for this cluster. If no
	// policy is provided then the default policy will be used. If backups are
	// supported for the cluster, the default policy takes one backup a day, has a
	// backup window of 1 hour, and retains backups for 14 days. For more
	// information on the defaults, consult the documentation for the message type.
	AutomatedBackupPolicy *AutomatedBackupPolicy `json:"automatedBackupPolicy,omitempty"`
	// BackupSource: Output only. Cluster created from backup.
	BackupSource *BackupSource `json:"backupSource,omitempty"`
	// BackupdrBackupSource: Output only. Cluster created from a BackupDR backup.
	BackupdrBackupSource *BackupDrBackupSource `json:"backupdrBackupSource,omitempty"`
	// BackupdrInfo: Output only. Output only information about BackupDR protection
	// for this cluster.
	BackupdrInfo *BackupDrInfo `json:"backupdrInfo,omitempty"`
	// CloudsqlBackupRunSource: Output only. Cluster created from CloudSQL
	// snapshot.
	CloudsqlBackupRunSource *CloudSQLBackupRunSource `json:"cloudsqlBackupRunSource,omitempty"`
	// ClusterType: Output only. The type of the cluster. This is an output-only
	// field and it's populated at the Cluster creation time or the Cluster
	// promotion time. The cluster type is determined by which RPC was used to
	// create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`
	//
	// Possible values:
	//   "CLUSTER_TYPE_UNSPECIFIED" - The type of the cluster is unknown.
	//   "PRIMARY" - Primary cluster that support read and write operations.
	//   "SECONDARY" - Secondary cluster that is replicating from another region.
	// This only supports read.
	ClusterType string `json:"clusterType,omitempty"`
	// ContinuousBackupConfig: Optional. Continuous backup configuration for this
	// cluster.
	ContinuousBackupConfig *ContinuousBackupConfig `json:"continuousBackupConfig,omitempty"`
	// ContinuousBackupInfo: Output only. Continuous backup properties for this
	// cluster.
	ContinuousBackupInfo *ContinuousBackupInfo `json:"continuousBackupInfo,omitempty"`
	// CreateTime: Output only. Create time stamp
	CreateTime string `json:"createTime,omitempty"`
	// DatabaseVersion: Optional. The database engine major version. This is an
	// optional field and it is populated at the Cluster creation time. If a
	// database version is not supplied at cluster creation time, then a default
	// database version will be used.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	DatabaseVersion string `json:"databaseVersion,omitempty"`
	// DataplexConfig: Optional. Configuration for Dataplex integration.
	DataplexConfig *DataplexConfig `json:"dataplexConfig,omitempty"`
	// DeleteTime: Output only. Delete time stamp
	DeleteTime string `json:"deleteTime,omitempty"`
	// DisplayName: User-settable and human-readable display name for the Cluster.
	DisplayName string `json:"displayName,omitempty"`
	// EncryptionConfig: Optional. The encryption config can be specified to
	// encrypt the data disks and other persistent data resources of a cluster with
	// a customer-managed encryption key (CMEK). When this field is not specified,
	// the cluster will then use default encryption scheme to protect the user
	// data.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// EncryptionInfo: Output only. The encryption information for the cluster.
	EncryptionInfo *EncryptionInfo `json:"encryptionInfo,omitempty"`
	// Etag: For Resource freshness validation (https://google.aip.dev/154)
	Etag string `json:"etag,omitempty"`
	// GeminiConfig: Optional. Deprecated and unused. This field will be removed in
	// the near future.
	GeminiConfig *GeminiClusterConfig `json:"geminiConfig,omitempty"`
	// InitialUser: Input only. Initial user to setup during cluster creation.
	// Required. If used in `RestoreCluster` this is ignored.
	InitialUser *UserPassword `json:"initialUser,omitempty"`
	// Labels: Labels as key value pairs
	Labels map[string]string `json:"labels,omitempty"`
	// MaintenanceSchedule: Output only. The maintenance schedule for the cluster,
	// generated for a specific rollout if a maintenance window is set.
	MaintenanceSchedule *MaintenanceSchedule `json:"maintenanceSchedule,omitempty"`
	// MaintenanceUpdatePolicy: Optional. The maintenance update policy determines
	// when to allow or deny updates.
	MaintenanceUpdatePolicy *MaintenanceUpdatePolicy `json:"maintenanceUpdatePolicy,omitempty"`
	// MaintenanceVersionSelectionPolicy: Input only. Policy to use to
	// automatically select the maintenance version to which to update the
	// cluster's instances.
	//
	// Possible values:
	//   "MAINTENANCE_VERSION_SELECTION_POLICY_UNSPECIFIED" - The maintenance
	// version selection policy is not specified.
	//   "MAINTENANCE_VERSION_SELECTION_POLICY_LATEST" - Use the latest available
	// maintenance version.
	//   "MAINTENANCE_VERSION_SELECTION_POLICY_DEFAULT" - Use the current default
	// maintenance version.
	MaintenanceVersionSelectionPolicy string `json:"maintenanceVersionSelectionPolicy,omitempty"`
	// MigrationSource: Output only. Cluster created via DMS migration.
	MigrationSource *MigrationSource `json:"migrationSource,omitempty"`
	// Name: Output only. The name of the cluster resource with the format: *
	// projects/{project}/locations/{region}/clusters/{cluster_id} where the
	// cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For
	// more details see https://google.aip.dev/122. The prefix of the cluster
	// resource name is the name of the parent resource: *
	// projects/{project}/locations/{region}
	Name string `json:"name,omitempty"`
	// Network: Required. The resource link for the VPC network in which cluster
	// resources are created and from which they are accessible via Private IP. The
	// network must belong to the same project as the cluster. It is specified in
	// the form: `projects/{project}/global/networks/{network_id}`. This is
	// required to create a cluster. Deprecated, use network_config.network
	// instead.
	Network       string         `json:"network,omitempty"`
	NetworkConfig *NetworkConfig `json:"networkConfig,omitempty"`
	// PrimaryConfig: Output only. Cross Region replication config specific to
	// PRIMARY cluster.
	PrimaryConfig *PrimaryConfig `json:"primaryConfig,omitempty"`
	// PscConfig: Optional. The configuration for Private Service Connect (PSC) for
	// the cluster.
	PscConfig *PscConfig `json:"pscConfig,omitempty"`
	// Reconciling: Output only. Reconciling
	// (https://google.aip.dev/128#reconciliation). Set to true if the current
	// state of Cluster does not match the user's intended state, and the service
	// is actively updating the resource to reconcile them. This can happen due to
	// user-triggered updates or system actions like failover or maintenance.
	Reconciling bool `json:"reconciling,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// SecondaryConfig: Cross Region replication config specific to SECONDARY
	// cluster.
	SecondaryConfig *SecondaryConfig `json:"secondaryConfig,omitempty"`
	// ServiceAccountEmail: Output only. AlloyDB per-cluster service account. This
	// service account is created per-cluster per-project, and is different from
	// the per-project service account. The per-cluster service account naming
	// format is subject to change.
	ServiceAccountEmail string `json:"serviceAccountEmail,omitempty"`
	// SslConfig: SSL configuration for this AlloyDB cluster.
	SslConfig *SslConfig `json:"sslConfig,omitempty"`
	// State: Output only. The current serving state of the cluster.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The state of the cluster is unknown.
	//   "READY" - The cluster is active and running.
	//   "STOPPED" - This is unused. Even when all instances in the cluster are
	// stopped, the cluster remains in READY state.
	//   "EMPTY" - The cluster is empty and has no associated resources. All
	// instances, associated storage and backups have been deleted.
	//   "CREATING" - The cluster is being created.
	//   "DELETING" - The cluster is being deleted.
	//   "FAILED" - The creation of the cluster failed.
	//   "BOOTSTRAPPING" - The cluster is bootstrapping with data from some other
	// source. Direct mutations to the cluster (e.g. adding read pool) are not
	// allowed.
	//   "MAINTENANCE" - The cluster is under maintenance. AlloyDB regularly
	// performs maintenance and upgrades on customer clusters. Updates on the
	// cluster are not allowed while the cluster is in this state.
	//   "PROMOTING" - The cluster is being promoted.
	//   "SWITCHOVER" - The cluster has entered switchover state. All updates on
	// cluster and its associated instances are restricted while the cluster is in
	// this state.
	State string `json:"state,omitempty"`
	// SubscriptionType: Optional. Subscription type of the cluster.
	//
	// Possible values:
	//   "SUBSCRIPTION_TYPE_UNSPECIFIED" - This is an unknown subscription type. By
	// default, the subscription type is STANDARD.
	//   "STANDARD" - Standard subscription.
	//   "TRIAL" - Trial subscription.
	SubscriptionType string `json:"subscriptionType,omitempty"`
	// Tags: Optional. Input only. Immutable. Tag keys/values directly bound to
	// this resource. For example: “` "123/environment": "production",
	// "123/costCenter": "marketing" “`
	Tags map[string]string `json:"tags,omitempty"`
	// TrialMetadata: Output only. Metadata for free trial clusters
	TrialMetadata *TrialMetadata `json:"trialMetadata,omitempty"`
	// Uid: Output only. The system-generated UID of the resource. The UID is
	// assigned when the resource is created, and it is retained until it is
	// deleted.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Update time stamp
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

Cluster: A cluster is a collection of regional AlloyDB resources. It can include a primary instance and one or more read pool instances. All cluster resources share a storage layer, which scales as needed.

func (Cluster) MarshalJSON ¶
func (s Cluster) MarshalJSON() ([]byte, error)
type ClusterUpgradeDetails ¶
added in v0.193.0
type ClusterUpgradeDetails struct {
	// ClusterType: Cluster type which can either be primary or secondary.
	//
	// Possible values:
	//   "CLUSTER_TYPE_UNSPECIFIED" - The type of the cluster is unknown.
	//   "PRIMARY" - Primary cluster that support read and write operations.
	//   "SECONDARY" - Secondary cluster that is replicating from another region.
	// This only supports read.
	ClusterType string `json:"clusterType,omitempty"`
	// DatabaseVersion: Database version of the cluster after the upgrade
	// operation. This will be the target version if the upgrade was successful
	// otherwise it remains the same as that before the upgrade operation.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	DatabaseVersion string `json:"databaseVersion,omitempty"`
	// InstanceUpgradeDetails: Upgrade details of the instances directly associated
	// with this cluster.
	InstanceUpgradeDetails []*InstanceUpgradeDetails `json:"instanceUpgradeDetails,omitempty"`
	// Name: Normalized name of the cluster
	Name string `json:"name,omitempty"`
	// StageInfo: Array containing stage info associated with this cluster.
	StageInfo []*StageInfo `json:"stageInfo,omitempty"`
	// UpgradeStatus: Upgrade status of the cluster.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	UpgradeStatus string `json:"upgradeStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClusterUpgradeDetails: Upgrade details of a cluster. This cluster can be primary or secondary.

func (ClusterUpgradeDetails) MarshalJSON ¶
added in v0.193.0
func (s ClusterUpgradeDetails) MarshalJSON() ([]byte, error)
type ConnectionInfo ¶
type ConnectionInfo struct {
	// InstanceUid: Output only. The unique ID of the Instance.
	InstanceUid string `json:"instanceUid,omitempty"`
	// IpAddress: Output only. The private network IP address for the Instance.
	// This is the default IP for the instance and is always created (even if
	// enable_public_ip is set). This is the connection endpoint for an end-user
	// application.
	IpAddress string `json:"ipAddress,omitempty"`
	// Name: The name of the ConnectionInfo singleton resource, e.g.:
	// projects/{project}/locations/{location}/clusters/*/instances/*/connectionInfo
	//  This field currently has no semantic meaning.
	Name string `json:"name,omitempty"`
	// PemCertificateChain: Output only. The pem-encoded chain that may be used to
	// verify the X.509 certificate. Expected to be in issuer-to-root order
	// according to RFC 5246.
	PemCertificateChain []string `json:"pemCertificateChain,omitempty"`
	// PscDnsName: Output only. The DNS name to use with PSC for the Instance.
	PscDnsName string `json:"pscDnsName,omitempty"`
	// PublicIpAddress: Output only. The public IP addresses for the Instance. This
	// is available ONLY when enable_public_ip is set. This is the connection
	// endpoint for an end-user application.
	PublicIpAddress string `json:"publicIpAddress,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "InstanceUid") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstanceUid") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConnectionInfo: ConnectionInfo singleton resource. https://google.aip.dev/156

func (ConnectionInfo) MarshalJSON ¶
func (s ConnectionInfo) MarshalJSON() ([]byte, error)
type ConnectionPoolConfig ¶
added in v0.228.0
type ConnectionPoolConfig struct {
	// Enabled: Optional. Whether to enable Managed Connection Pool (MCP).
	Enabled bool `json:"enabled,omitempty"`
	// Flags: Optional. Connection Pool flags, as a list of "key": "value" pairs.
	Flags map[string]string `json:"flags,omitempty"`
	// PoolerCount: Output only. The number of running poolers per instance.
	PoolerCount int64 `json:"poolerCount,omitempty"`
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

ConnectionPoolConfig: Configuration for Managed Connection Pool (MCP).

func (ConnectionPoolConfig) MarshalJSON ¶
added in v0.228.0
func (s ConnectionPoolConfig) MarshalJSON() ([]byte, error)
type ContinuousBackupConfig ¶
type ContinuousBackupConfig struct {
	// Enabled: Whether ContinuousBackup is enabled.
	Enabled bool `json:"enabled,omitempty"`
	// EncryptionConfig: The encryption config can be specified to encrypt the
	// backups with a customer-managed encryption key (CMEK). When this field is
	// not specified, the backup will use the cluster's encryption config.
	EncryptionConfig *EncryptionConfig `json:"encryptionConfig,omitempty"`
	// RecoveryWindowDays: The number of days that are eligible to restore from
	// using PITR. To support the entire recovery window, backups and logs are
	// retained for one day more than the recovery window. If not set, defaults to
	// 14 days.
	RecoveryWindowDays int64 `json:"recoveryWindowDays,omitempty"`
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

ContinuousBackupConfig: ContinuousBackupConfig describes the continuous backups recovery configurations of a cluster.

func (ContinuousBackupConfig) MarshalJSON ¶
func (s ContinuousBackupConfig) MarshalJSON() ([]byte, error)
type ContinuousBackupInfo ¶
type ContinuousBackupInfo struct {
	// EarliestRestorableTime: Output only. The earliest restorable time that can
	// be restored to. If continuous backups and recovery was recently enabled, the
	// earliest restorable time is the creation time of the earliest eligible
	// backup within this cluster's continuous backup recovery window. After a
	// cluster has had continuous backups enabled for the duration of its recovery
	// window, the earliest restorable time becomes "now minus the recovery
	// window". For example, assuming a point in time recovery is attempted at
	// 04/16/2025 3:23:00PM with a 14d recovery window, the earliest restorable
	// time would be 04/02/2025 3:23:00PM. This field is only visible if the
	// CLUSTER_VIEW_CONTINUOUS_BACKUP cluster view is provided.
	EarliestRestorableTime string `json:"earliestRestorableTime,omitempty"`
	// EnabledTime: Output only. When ContinuousBackup was most recently enabled.
	// Set to null if ContinuousBackup is not enabled.
	EnabledTime string `json:"enabledTime,omitempty"`
	// EncryptionInfo: Output only. The encryption information for the WALs and
	// backups required for ContinuousBackup.
	EncryptionInfo *EncryptionInfo `json:"encryptionInfo,omitempty"`
	// Schedule: Output only. Days of the week on which a continuous backup is
	// taken.
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
	Schedule []string `json:"schedule,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EarliestRestorableTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EarliestRestorableTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ContinuousBackupInfo: ContinuousBackupInfo describes the continuous backup properties of a cluster.

func (ContinuousBackupInfo) MarshalJSON ¶
func (s ContinuousBackupInfo) MarshalJSON() ([]byte, error)
type ContinuousBackupSource ¶
type ContinuousBackupSource struct {
	// Cluster: Required. The source cluster from which to restore. This cluster
	// must have continuous backup enabled for this operation to succeed. For the
	// required format, see the comment on the Cluster.name field.
	Cluster string `json:"cluster,omitempty"`
	// PointInTime: Required. The point in time to restore to.
	PointInTime string `json:"pointInTime,omitempty"`
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

ContinuousBackupSource: Message describing a ContinuousBackupSource.

func (ContinuousBackupSource) MarshalJSON ¶
func (s ContinuousBackupSource) MarshalJSON() ([]byte, error)
type CpuUtilization ¶
added in v0.252.0
type CpuUtilization struct {
	// UtilizationTarget: Target CPU utilization as a float between 0 and 1.
	UtilizationTarget float64 `json:"utilizationTarget,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UtilizationTarget") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UtilizationTarget") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CpuUtilization: CPU utilization policy for the autoscaler.

func (CpuUtilization) MarshalJSON ¶
added in v0.252.0
func (s CpuUtilization) MarshalJSON() ([]byte, error)
func (*CpuUtilization) UnmarshalJSON ¶
added in v0.252.0
func (s *CpuUtilization) UnmarshalJSON(data []byte) error
type CsvExportOptions ¶
added in v0.209.0
type CsvExportOptions struct {
	// EscapeCharacter: Optional. Specifies the character that should appear before
	// a data character that needs to be escaped. The default is the same as quote
	// character. The value of this argument has to be a character in Hex ASCII
	// Code.
	EscapeCharacter string `json:"escapeCharacter,omitempty"`
	// FieldDelimiter: Optional. Specifies the character that separates columns
	// within each row (line) of the file. The default is comma. The value of this
	// argument has to be a character in Hex ASCII Code.
	FieldDelimiter string `json:"fieldDelimiter,omitempty"`
	// QuoteCharacter: Optional. Specifies the quoting character to be used when a
	// data value is quoted. The default is double-quote. The value of this
	// argument has to be a character in Hex ASCII Code.
	QuoteCharacter string `json:"quoteCharacter,omitempty"`
	// SelectQuery: Required. The SELECT query used to extract the data.
	SelectQuery string `json:"selectQuery,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EscapeCharacter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EscapeCharacter") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CsvExportOptions: Options for exporting data in CSV format.

func (CsvExportOptions) MarshalJSON ¶
added in v0.209.0
func (s CsvExportOptions) MarshalJSON() ([]byte, error)
type CsvImportOptions ¶
added in v0.222.0
type CsvImportOptions struct {
	// Columns: Optional. The columns to which CSV data is imported. If not
	// specified, all columns of the database table are loaded with CSV data.
	Columns []string `json:"columns,omitempty"`
	// EscapeCharacter: Optional. Specifies the character that should appear before
	// a data character that needs to be escaped. The default is same as quote
	// character. The value of this argument has to be a character in Hex ASCII
	// Code.
	EscapeCharacter string `json:"escapeCharacter,omitempty"`
	// FieldDelimiter: Optional. Specifies the character that separates columns
	// within each row (line) of the file. The default is comma. The value of this
	// argument has to be a character in Hex ASCII Code.
	FieldDelimiter string `json:"fieldDelimiter,omitempty"`
	// QuoteCharacter: Optional. Specifies the quoting character to be used when a
	// data value is quoted. The default is double-quote. The value of this
	// argument has to be a character in Hex ASCII Code.
	QuoteCharacter string `json:"quoteCharacter,omitempty"`
	// Table: Required. The database table to import CSV file into.
	Table string `json:"table,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Columns") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Columns") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CsvImportOptions: Options for importing data in CSV format.

func (CsvImportOptions) MarshalJSON ¶
added in v0.222.0
func (s CsvImportOptions) MarshalJSON() ([]byte, error)
type DataplexConfig ¶
added in v0.254.0
type DataplexConfig struct {
	// Enabled: Dataplex is enabled by default for resources such as clusters and
	// instances. This flag controls the integration of AlloyDB PG resources (like
	// databases, schemas, and tables) with Dataplex."
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

DataplexConfig: Configuration for Dataplex integration.

func (DataplexConfig) MarshalJSON ¶
added in v0.254.0
func (s DataplexConfig) MarshalJSON() ([]byte, error)
type DenyMaintenancePeriod ¶
added in v0.171.0
type DenyMaintenancePeriod struct {
	// EndDate: Deny period end date. This can be: * A full date, with non-zero
	// year, month and day values OR * A month and day value, with a zero year for
	// recurring
	EndDate *GoogleTypeDate `json:"endDate,omitempty"`
	// StartDate: Deny period start date. This can be: * A full date, with non-zero
	// year, month and day values OR * A month and day value, with a zero year for
	// recurring
	StartDate *GoogleTypeDate `json:"startDate,omitempty"`
	// Time: Time in UTC when the deny period starts on start_date and ends on
	// end_date. This can be: * Full time OR * All zeros for 00:00:00 UTC
	Time *GoogleTypeTimeOfDay `json:"time,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndDate") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndDate") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DenyMaintenancePeriod: DenyMaintenancePeriod definition. Excepting emergencies, maintenance will not be scheduled to start within this deny period. The start_date must be less than the end_date.

func (DenyMaintenancePeriod) MarshalJSON ¶
added in v0.171.0
func (s DenyMaintenancePeriod) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EncryptionConfig ¶
type EncryptionConfig struct {
	// KmsKeyName: The fully-qualified resource name of the KMS key. Each Cloud KMS
	// key is regionalized and has the following format:
	// projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME]
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

EncryptionConfig: EncryptionConfig describes the encryption config of a cluster or a backup that is encrypted with a CMEK (customer-managed encryption key).

func (EncryptionConfig) MarshalJSON ¶
func (s EncryptionConfig) MarshalJSON() ([]byte, error)
type EncryptionInfo ¶
type EncryptionInfo struct {
	// EncryptionType: Output only. Type of encryption.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Encryption type not specified. Defaults to
	// GOOGLE_DEFAULT_ENCRYPTION.
	//   "GOOGLE_DEFAULT_ENCRYPTION" - The data is encrypted at rest with a key
	// that is fully managed by Google. No key version will be populated. This is
	// the default state.
	//   "CUSTOMER_MANAGED_ENCRYPTION" - The data is encrypted at rest with a key
	// that is managed by the customer. KMS key versions will be populated.
	EncryptionType string `json:"encryptionType,omitempty"`
	// KmsKeyVersions: Output only. Cloud KMS key versions that are being used to
	// protect the database or the backup.
	KmsKeyVersions []string `json:"kmsKeyVersions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EncryptionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EncryptionType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EncryptionInfo: EncryptionInfo describes the encryption information of a cluster or a backup.

func (EncryptionInfo) MarshalJSON ¶
func (s EncryptionInfo) MarshalJSON() ([]byte, error)
type ExportClusterRequest ¶
added in v0.209.0
type ExportClusterRequest struct {
	// CsvExportOptions: Options for exporting data in CSV format. Required field
	// to be set for CSV file type.
	CsvExportOptions *CsvExportOptions `json:"csvExportOptions,omitempty"`
	// Database: Required. Name of the database where the export command will be
	// executed. Note - Value provided should be the same as expected from `SELECT
	// current_database();` and NOT as a resource reference.
	Database string `json:"database,omitempty"`
	// GcsDestination: Required. Option to export data to cloud storage.
	GcsDestination *GcsDestination `json:"gcsDestination,omitempty"`
	// SqlExportOptions: Options for exporting data in SQL format. Required field
	// to be set for SQL file type.
	SqlExportOptions *SqlExportOptions `json:"sqlExportOptions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CsvExportOptions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CsvExportOptions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExportClusterRequest: Export cluster request.

func (ExportClusterRequest) MarshalJSON ¶
added in v0.209.0
func (s ExportClusterRequest) MarshalJSON() ([]byte, error)
type FailoverInstanceRequest ¶
type FailoverInstanceRequest struct {
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
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

FailoverInstanceRequest: Message for triggering failover on an Instance

func (FailoverInstanceRequest) MarshalJSON ¶
func (s FailoverInstanceRequest) MarshalJSON() ([]byte, error)
type GCAInstanceConfig ¶
added in v0.224.0
type GCAInstanceConfig struct {
	// GcaEntitlement: Output only. Represents the GCA entitlement state of the
	// instance.
	//
	// Possible values:
	//   "GCA_ENTITLEMENT_TYPE_UNSPECIFIED" - No GCA entitlement is assigned.
	//   "GCA_STANDARD" - The resource is entitled to the GCA Standard Tier.
	GcaEntitlement string `json:"gcaEntitlement,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcaEntitlement") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcaEntitlement") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GCAInstanceConfig: Instance level configuration parameters related to the Gemini Cloud Assist product.

func (GCAInstanceConfig) MarshalJSON ¶
added in v0.224.0
func (s GCAInstanceConfig) MarshalJSON() ([]byte, error)
type GcsDestination ¶
added in v0.209.0
type GcsDestination struct {
	// Uri: Required. The path to the file in Google Cloud Storage where the export
	// will be stored. The URI is in the form `gs://bucketName/fileName`.
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Uri") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Uri") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GcsDestination: Destination for Export. Export will be done to cloud storage.

func (GcsDestination) MarshalJSON ¶
added in v0.209.0
func (s GcsDestination) MarshalJSON() ([]byte, error)
type GeminiClusterConfig ¶
added in v0.171.0
type GeminiClusterConfig struct {
	// Entitled: Output only. Deprecated and unused. This field will be removed in
	// the near future.
	Entitled bool `json:"entitled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Entitled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Entitled") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeminiClusterConfig: Deprecated and unused. This message will be removed in the near future.

func (GeminiClusterConfig) MarshalJSON ¶
added in v0.171.0
func (s GeminiClusterConfig) MarshalJSON() ([]byte, error)
type GeminiInstanceConfig ¶
added in v0.171.0
type GeminiInstanceConfig struct {
	// Entitled: Output only. Deprecated and unused. This field will be removed in
	// the near future.
	Entitled bool `json:"entitled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Entitled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Entitled") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeminiInstanceConfig: Deprecated and unused. This message will be removed in the near future.

func (GeminiInstanceConfig) MarshalJSON ¶
added in v0.171.0
func (s GeminiInstanceConfig) MarshalJSON() ([]byte, error)
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
type GoogleTypeDate ¶
added in v0.171.0
type GoogleTypeDate struct {
	// Day: Day of a month. Must be from 1 to 31 and valid for the year and month,
	// or 0 to specify a year by itself or a year and month where the day isn't
	// significant.
	Day int64 `json:"day,omitempty"`
	// Month: Month of a year. Must be from 1 to 12, or 0 to specify a year without
	// a month and day.
	Month int64 `json:"month,omitempty"`
	// Year: Year of the date. Must be from 1 to 9999, or 0 to specify a date
	// without a year.
	Year int64 `json:"year,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Day") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Day") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleTypeDate: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp

func (GoogleTypeDate) MarshalJSON ¶
added in v0.171.0
func (s GoogleTypeDate) MarshalJSON() ([]byte, error)
type GoogleTypeTimeOfDay ¶
type GoogleTypeTimeOfDay struct {
	// Hours: Hours of a day in 24 hour format. Must be greater than or equal to 0
	// and typically must be less than or equal to 23. An API may choose to allow
	// the value "24:00:00" for scenarios like business closing time.
	Hours int64 `json:"hours,omitempty"`
	// Minutes: Minutes of an hour. Must be greater than or equal to 0 and less
	// than or equal to 59.
	Minutes int64 `json:"minutes,omitempty"`
	// Nanos: Fractions of seconds, in nanoseconds. Must be greater than or equal
	// to 0 and less than or equal to 999,999,999.
	Nanos int64 `json:"nanos,omitempty"`
	// Seconds: Seconds of a minute. Must be greater than or equal to 0 and
	// typically must be less than or equal to 59. An API may allow the value 60 if
	// it allows leap-seconds.
	Seconds int64 `json:"seconds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Hours") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Hours") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleTypeTimeOfDay: Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`.

func (GoogleTypeTimeOfDay) MarshalJSON ¶
func (s GoogleTypeTimeOfDay) MarshalJSON() ([]byte, error)
type ImportClusterRequest ¶
added in v0.222.0
type ImportClusterRequest struct {
	// CsvImportOptions: Options for importing data in CSV format.
	CsvImportOptions *CsvImportOptions `json:"csvImportOptions,omitempty"`
	// Database: Optional. Name of the database to which the import will be done.
	// For import from SQL file, this is required only if the file does not specify
	// a database. Note - Value provided should be the same as expected from
	// `SELECT current_database();` and NOT as a resource reference.
	Database string `json:"database,omitempty"`
	// GcsUri: Required. The path to the file in Google Cloud Storage where the
	// source file for import will be stored. The URI is in the form
	// `gs://bucketName/fileName`.
	GcsUri string `json:"gcsUri,omitempty"`
	// SqlImportOptions: Options for importing data in SQL format.
	SqlImportOptions *SqlImportOptions `json:"sqlImportOptions,omitempty"`
	// User: Optional. Database user to be used for importing the data. Note -
	// Value provided should be the same as expected from `SELECT current_user;`
	// and NOT as a resource reference.
	User string `json:"user,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CsvImportOptions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CsvImportOptions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImportClusterRequest: Import cluster request.

func (ImportClusterRequest) MarshalJSON ¶
added in v0.222.0
func (s ImportClusterRequest) MarshalJSON() ([]byte, error)
type InjectFaultRequest ¶
type InjectFaultRequest struct {
	// FaultType: Required. The type of fault to be injected in an instance.
	//
	// Possible values:
	//   "FAULT_TYPE_UNSPECIFIED" - The fault type is unknown.
	//   "STOP_VM" - Stop the VM
	FaultType string `json:"faultType,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FaultType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FaultType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InjectFaultRequest: Message for triggering fault injection on an instance

func (InjectFaultRequest) MarshalJSON ¶
func (s InjectFaultRequest) MarshalJSON() ([]byte, error)
type Instance ¶
type Instance struct {
	// ActivationPolicy: Optional. Specifies whether an instance needs to spin up.
	// Once the instance is active, the activation policy can be updated to the
	// `NEVER` to stop the instance. Likewise, the activation policy can be updated
	// to `ALWAYS` to start the instance. There are restrictions around when an
	// instance can/cannot be activated (for example, a read pool instance should
	// be stopped before stopping primary etc.). Please refer to the API
	// documentation for more details.
	//
	// Possible values:
	//   "ACTIVATION_POLICY_UNSPECIFIED" - The policy is not specified.
	//   "ALWAYS" - The instance is running.
	//   "NEVER" - The instance is not running.
	ActivationPolicy string `json:"activationPolicy,omitempty"`
	// Annotations: Annotations to allow client tools to store small amount of
	// arbitrary data. This is distinct from labels. https://google.aip.dev/128
	Annotations map[string]string `json:"annotations,omitempty"`
	// AvailabilityType: Availability type of an Instance. If empty, defaults to
	// REGIONAL for primary instances. For read pools, availability_type is always
	// UNSPECIFIED. Instances in the read pools are evenly distributed across
	// available zones within the region (i.e. read pools with more than one node
	// will have a node in at least two zones).
	//
	// Possible values:
	//   "AVAILABILITY_TYPE_UNSPECIFIED" - This is an unknown Availability type.
	//   "ZONAL" - Zonal available instance.
	//   "REGIONAL" - Regional (or Highly) available instance.
	AvailabilityType string `json:"availabilityType,omitempty"`
	// ClientConnectionConfig: Optional. Client connection specific configurations
	ClientConnectionConfig *ClientConnectionConfig `json:"clientConnectionConfig,omitempty"`
	// ConnectionPoolConfig: Optional. The configuration for Managed Connection
	// Pool (MCP).
	ConnectionPoolConfig *ConnectionPoolConfig `json:"connectionPoolConfig,omitempty"`
	// CreateTime: Output only. Create time stamp
	CreateTime string `json:"createTime,omitempty"`
	// DataApiAccess: Optional. Controls whether the Data API is enabled for this
	// instance. When enabled, this allows authorized users to connect to the
	// instance from the public internet using the `executeSql` API, even for
	// private IP instances. If this is not specified, the data API is enabled by
	// default for Google internal services like AlloyDB Studio. Disable it
	// explicitly to disallow Google internal services as well.
	//
	// Possible values:
	//   "DEFAULT_DATA_API_ENABLED_FOR_GOOGLE_CLOUD_SERVICES" -
	// DEFAULT_DATA_API_ENABLED_FOR_GOOGLE_CLOUD_SERVICES is a default value that
	// allows Google internal services like AlloyDB Studio to access the instance.
	//   "DISABLED" - Data API access is disabled for this instance.
	//   "ENABLED" - Data API access is enabled for this instance. For private IP
	// instances, this allows authorized users to access the instance from the
	// public internet using the ExecuteSql API.
	DataApiAccess string `json:"dataApiAccess,omitempty"`
	// DatabaseFlags: Database flags. Set at the instance level. They are copied
	// from the primary instance on secondary instance creation. Flags that have
	// restrictions default to the value at primary instance on read instances
	// during creation. Read instances can set new flags or override existing flags
	// that are relevant for reads, for example, for enabling columnar cache on a
	// read instance. Flags set on read instance might or might not be present on
	// the primary instance. This is a list of "key": "value" pairs. "key": The
	// name of the flag. These flags are passed at instance setup time, so include
	// both server options and system variables for Postgres. Flags are specified
	// with underscores, not hyphens. "value": The value of the flag. Booleans are
	// set to **on** for true and **off** for false. This field must be omitted if
	// the flag doesn't take a value.
	DatabaseFlags map[string]string `json:"databaseFlags,omitempty"`
	// DeleteTime: Output only. Delete time stamp
	DeleteTime string `json:"deleteTime,omitempty"`
	// DisplayName: User-settable and human-readable display name for the Instance.
	DisplayName string `json:"displayName,omitempty"`
	// Etag: For Resource freshness validation (https://google.aip.dev/154)
	Etag string `json:"etag,omitempty"`
	// GcaConfig: Output only. Configuration parameters related to Gemini Cloud
	// Assist.
	GcaConfig *GCAInstanceConfig `json:"gcaConfig,omitempty"`
	// GceZone: The Compute Engine zone that the instance should serve from, per
	// https://cloud.google.com/compute/docs/regions-zones This can ONLY be
	// specified for ZONAL instances. If present for a REGIONAL instance, an error
	// will be thrown. If this is absent for a ZONAL instance, instance is created
	// in a random zone with available capacity.
	GceZone string `json:"gceZone,omitempty"`
	// GeminiConfig: Optional. Deprecated and unused. This field will be removed in
	// the near future.
	GeminiConfig *GeminiInstanceConfig `json:"geminiConfig,omitempty"`
	// InstanceType: Required. The type of the instance. Specified at creation
	// time.
	//
	// Possible values:
	//   "INSTANCE_TYPE_UNSPECIFIED" - The type of the instance is unknown.
	//   "PRIMARY" - PRIMARY instances support read and write operations.
	//   "READ_POOL" - READ POOL instances support read operations only. Each read
	// pool instance consists of one or more homogeneous nodes. * Read pool of size
	// 1 can only have zonal availability. * Read pools with node count of 2 or
	// more can have regional availability (nodes are present in 2 or more zones in
	// a region).
	//   "SECONDARY" - SECONDARY instances support read operations only. SECONDARY
	// instance is a cross-region read replica
	InstanceType string `json:"instanceType,omitempty"`
	// IpAddress: Output only. The IP address for the Instance. This is the
	// connection endpoint for an end-user application.
	IpAddress string `json:"ipAddress,omitempty"`
	// Labels: Labels as key value pairs
	Labels map[string]string `json:"labels,omitempty"`
	// MachineConfig: Configurations for the machines that host the underlying
	// database engine.
	MachineConfig *MachineConfig `json:"machineConfig,omitempty"`
	// MaintenanceVersionName: Output only. Maintenance version of the instance,
	// for example: POSTGRES_15.2025_07_15.04_00. Output only. Update this field
	// via the parent cluster's maintenance_version field(s).
	MaintenanceVersionName string `json:"maintenanceVersionName,omitempty"`
	// Name: Output only. The name of the instance resource with the format: *
	// projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instan
	// ce_id} where the cluster and instance ID segments should satisfy the regex
	// expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of
	// lowercase letters, numbers, and dashes, starting with a letter, and ending
	// with a letter or number. For more details see https://google.aip.dev/122.
	// The prefix of the instance resource name is the name of the parent resource:
	// * projects/{project}/locations/{region}/clusters/{cluster_id}
	Name string `json:"name,omitempty"`
	// NetworkConfig: Optional. Instance-level network configuration.
	NetworkConfig *InstanceNetworkConfig `json:"networkConfig,omitempty"`
	// Nodes: Output only. List of available read-only VMs in this instance,
	// including the standby for a PRIMARY instance.
	Nodes []*Node `json:"nodes,omitempty"`
	// ObservabilityConfig: Configuration for observability.
	ObservabilityConfig *ObservabilityInstanceConfig `json:"observabilityConfig,omitempty"`
	// OutboundPublicIpAddresses: Output only. All outbound public IP addresses
	// configured for the instance.
	OutboundPublicIpAddresses []string `json:"outboundPublicIpAddresses,omitempty"`
	// PscInstanceConfig: Optional. The configuration for Private Service Connect
	// (PSC) for the instance.
	PscInstanceConfig *PscInstanceConfig `json:"pscInstanceConfig,omitempty"`
	// PublicIpAddress: Output only. The public IP addresses for the Instance. This
	// is available ONLY when enable_public_ip is set. This is the connection
	// endpoint for an end-user application.
	PublicIpAddress string `json:"publicIpAddress,omitempty"`
	// QueryInsightsConfig: Configuration for query insights.
	QueryInsightsConfig *QueryInsightsInstanceConfig `json:"queryInsightsConfig,omitempty"`
	// ReadPoolConfig: Read pool instance configuration. This is required if the
	// value of instanceType is READ_POOL.
	ReadPoolConfig *ReadPoolConfig `json:"readPoolConfig,omitempty"`
	// Reconciling: Output only. Reconciling
	// (https://google.aip.dev/128#reconciliation). Set to true if the current
	// state of Instance does not match the user's intended state, and the service
	// is actively updating the resource to reconcile them. This can happen due to
	// user-triggered updates or system actions like failover or maintenance.
	Reconciling bool `json:"reconciling,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// State: Output only. The current serving state of the instance.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The state of the instance is unknown.
	//   "READY" - The instance is active and running.
	//   "STOPPED" - The instance is stopped. Instance name and IP resources are
	// preserved.
	//   "CREATING" - The instance is being created.
	//   "DELETING" - The instance is being deleted.
	//   "MAINTENANCE" - The instance is down for maintenance.
	//   "FAILED" - The creation of the instance failed or a fatal error occurred
	// during an operation on the instance. Note: Instances in this state would
	// tried to be auto-repaired. And Customers should be able to restart, update
	// or delete these instances.
	//   "BOOTSTRAPPING" - The instance has been configured to sync data from some
	// other source.
	//   "PROMOTING" - The instance is being promoted.
	//   "SWITCHOVER" - The instance has entered switchover state. All updates on
	// instance are restricted while the instance is in this state.
	//   "STOPPING" - The instance is being stopped.
	//   "STARTING" - The instance is being started.
	State string `json:"state,omitempty"`
	// Uid: Output only. The system-generated UID of the resource. The UID is
	// assigned when the resource is created, and it is retained until it is
	// deleted.
	Uid string `json:"uid,omitempty"`
	// UpdatePolicy: Update policy that will be applied during instance update.
	// This field is not persisted when you update the instance. To use a
	// non-default update policy, you must specify explicitly specify the value in
	// each update request.
	UpdatePolicy *UpdatePolicy `json:"updatePolicy,omitempty"`
	// UpdateTime: Output only. Update time stamp
	UpdateTime string `json:"updateTime,omitempty"`
	// WritableNode: Output only. This is set for the read-write VM of the PRIMARY
	// instance only.
	WritableNode *Node `json:"writableNode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ActivationPolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActivationPolicy") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Instance: An Instance is a computing unit that an end customer can connect to. It's the main unit of computing resources in AlloyDB.

func (Instance) MarshalJSON ¶
func (s Instance) MarshalJSON() ([]byte, error)
type InstanceNetworkConfig ¶
added in v0.155.0
type InstanceNetworkConfig struct {
	// AllocatedIpRangeOverride: Optional. Name of the allocated IP range for the
	// private IP AlloyDB instance, for example: "google-managed-services-default".
	// If set, the instance IPs will be created from this allocated range and will
	// override the IP range used by the parent cluster. The range name must comply
	// with RFC 1035 (https://datatracker.ietf.org/doc/html/rfc1035). Specifically,
	// the name must be 1-63 characters long and match the regular expression a-z
	// ([-a-z0-9]*[a-z0-9])?.
	AllocatedIpRangeOverride string `json:"allocatedIpRangeOverride,omitempty"`
	// AuthorizedExternalNetworks: Optional. A list of external network authorized
	// to access this instance.
	AuthorizedExternalNetworks []*AuthorizedNetwork `json:"authorizedExternalNetworks,omitempty"`
	// EnableOutboundPublicIp: Optional. Enabling an outbound public IP address to
	// support a database server sending requests out into the internet.
	EnableOutboundPublicIp bool `json:"enableOutboundPublicIp,omitempty"`
	// EnablePublicIp: Optional. Enabling public ip for the instance.
	EnablePublicIp bool `json:"enablePublicIp,omitempty"`
	// Network: Output only. The resource link for the VPC network in which
	// instance resources are created and from which they are accessible via
	// Private IP. This will be the same value as the parent cluster's network. It
	// is specified in the form: //
	// `projects/{project_number}/global/networks/{network_id}`.
	Network string `json:"network,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllocatedIpRangeOverride")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllocatedIpRangeOverride") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstanceNetworkConfig: Metadata related to instance-level network configuration.

func (InstanceNetworkConfig) MarshalJSON ¶
added in v0.155.0
func (s InstanceNetworkConfig) MarshalJSON() ([]byte, error)
type InstanceUpgradeDetails ¶
added in v0.193.0
type InstanceUpgradeDetails struct {
	// InstanceType: Instance type.
	//
	// Possible values:
	//   "INSTANCE_TYPE_UNSPECIFIED" - The type of the instance is unknown.
	//   "PRIMARY" - PRIMARY instances support read and write operations.
	//   "READ_POOL" - READ POOL instances support read operations only. Each read
	// pool instance consists of one or more homogeneous nodes. * Read pool of size
	// 1 can only have zonal availability. * Read pools with node count of 2 or
	// more can have regional availability (nodes are present in 2 or more zones in
	// a region).
	//   "SECONDARY" - SECONDARY instances support read operations only. SECONDARY
	// instance is a cross-region read replica
	InstanceType string `json:"instanceType,omitempty"`
	// Name: Normalized name of the instance.
	Name string `json:"name,omitempty"`
	// UpgradeStatus: Upgrade status of the instance.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	UpgradeStatus string `json:"upgradeStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InstanceType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstanceType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstanceUpgradeDetails: Details regarding the upgrade of instances associated with a cluster.

func (InstanceUpgradeDetails) MarshalJSON ¶
added in v0.193.0
func (s InstanceUpgradeDetails) MarshalJSON() ([]byte, error)
type IntegerRestrictions ¶
type IntegerRestrictions struct {
	// MaxValue: The maximum value that can be specified, if applicable.
	MaxValue int64 `json:"maxValue,omitempty,string"`
	// MinValue: The minimum value that can be specified, if applicable.
	MinValue int64 `json:"minValue,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "MaxValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IntegerRestrictions: Restrictions on INTEGER type values.

func (IntegerRestrictions) MarshalJSON ¶
func (s IntegerRestrictions) MarshalJSON() ([]byte, error)
type ListBackupsResponse ¶
type ListBackupsResponse struct {
	// Backups: The list of Backup
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

ListBackupsResponse: Message for response to listing Backups

func (ListBackupsResponse) MarshalJSON ¶
func (s ListBackupsResponse) MarshalJSON() ([]byte, error)
type ListClustersResponse ¶
type ListClustersResponse struct {
	// Clusters: The list of Cluster
	Clusters []*Cluster `json:"clusters,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

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

ListClustersResponse: Message for response to listing Clusters

func (ListClustersResponse) MarshalJSON ¶
func (s ListClustersResponse) MarshalJSON() ([]byte, error)
type ListInstancesResponse ¶
type ListInstancesResponse struct {
	// Instances: The list of Instance
	Instances []*Instance `json:"instances,omitempty"`
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Instances") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Instances") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListInstancesResponse: Message for response to listing Instances

func (ListInstancesResponse) MarshalJSON ¶
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
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
type ListSupportedDatabaseFlagsResponse ¶
type ListSupportedDatabaseFlagsResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SupportedDatabaseFlags: The list of SupportedDatabaseFlags.
	SupportedDatabaseFlags []*SupportedDatabaseFlag `json:"supportedDatabaseFlags,omitempty"`

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

ListSupportedDatabaseFlagsResponse: Message for response to listing SupportedDatabaseFlags.

func (ListSupportedDatabaseFlagsResponse) MarshalJSON ¶
func (s ListSupportedDatabaseFlagsResponse) MarshalJSON() ([]byte, error)
type ListUsersResponse ¶
type ListUsersResponse struct {
	// NextPageToken: A token identifying a page of results the server should
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`
	// Users: The list of User
	Users []*User `json:"users,omitempty"`

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

ListUsersResponse: Message for response to listing Users

func (ListUsersResponse) MarshalJSON ¶
func (s ListUsersResponse) MarshalJSON() ([]byte, error)
type MachineConfig ¶
type MachineConfig struct {
	// CpuCount: The number of CPU's in the VM instance.
	CpuCount int64 `json:"cpuCount,omitempty"`
	// MachineType: Machine type of the VM instance. E.g. "n2-highmem-4",
	// "n2-highmem-8", "c4a-highmem-4-lssd". cpu_count must match the number of
	// vCPUs in the machine type.
	MachineType string `json:"machineType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CpuCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CpuCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MachineConfig: MachineConfig describes the configuration of a machine.

func (MachineConfig) MarshalJSON ¶
func (s MachineConfig) MarshalJSON() ([]byte, error)
type MaintenanceSchedule ¶
added in v0.173.0
type MaintenanceSchedule struct {
	// StartTime: Output only. The scheduled start time for the maintenance.
	StartTime string `json:"startTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "StartTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "StartTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MaintenanceSchedule: MaintenanceSchedule stores the maintenance schedule generated from the MaintenanceUpdatePolicy, once a maintenance rollout is triggered, if MaintenanceWindow is set, and if there is no conflicting DenyPeriod. The schedule is cleared once the update takes place. This field cannot be manually changed; modify the MaintenanceUpdatePolicy instead.

func (MaintenanceSchedule) MarshalJSON ¶
added in v0.173.0
func (s MaintenanceSchedule) MarshalJSON() ([]byte, error)
type MaintenanceUpdatePolicy ¶
added in v0.171.0
type MaintenanceUpdatePolicy struct {
	// DenyMaintenancePeriods: Periods to deny maintenance. Currently limited to 1.
	DenyMaintenancePeriods []*DenyMaintenancePeriod `json:"denyMaintenancePeriods,omitempty"`
	// MaintenanceWindows: Preferred windows to perform maintenance. Currently
	// limited to 1.
	MaintenanceWindows []*MaintenanceWindow `json:"maintenanceWindows,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DenyMaintenancePeriods") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DenyMaintenancePeriods") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MaintenanceUpdatePolicy: MaintenanceUpdatePolicy defines the policy for system updates.

func (MaintenanceUpdatePolicy) MarshalJSON ¶
added in v0.171.0
func (s MaintenanceUpdatePolicy) MarshalJSON() ([]byte, error)
type MaintenanceWindow ¶
added in v0.171.0
type MaintenanceWindow struct {
	// Day: Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.
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
	Day string `json:"day,omitempty"`
	// StartTime: Preferred time to start the maintenance operation on the
	// specified day. Maintenance will start within 1 hour of this time.
	StartTime *GoogleTypeTimeOfDay `json:"startTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Day") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Day") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MaintenanceWindow: MaintenanceWindow specifies a preferred day and time for maintenance.

func (MaintenanceWindow) MarshalJSON ¶
added in v0.171.0
func (s MaintenanceWindow) MarshalJSON() ([]byte, error)
type MigrationSource ¶
type MigrationSource struct {
	// HostPort: Output only. The host and port of the on-premises instance in
	// host:port format
	HostPort string `json:"hostPort,omitempty"`
	// ReferenceId: Output only. Place holder for the external source
	// identifier(e.g DMS job name) that created the cluster.
	ReferenceId string `json:"referenceId,omitempty"`
	// SourceType: Output only. Type of migration source.
	//
	// Possible values:
	//   "MIGRATION_SOURCE_TYPE_UNSPECIFIED" - Migration source is unknown.
	//   "DMS" - DMS source means the cluster was created via DMS migration job.
	SourceType string `json:"sourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "HostPort") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HostPort") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MigrationSource: Subset of the source instance configuration that is available when reading the cluster resource.

func (MigrationSource) MarshalJSON ¶
func (s MigrationSource) MarshalJSON() ([]byte, error)
type NetworkConfig ¶
type NetworkConfig struct {
	// AllocatedIpRange: Optional. Name of the allocated IP range for the private
	// IP AlloyDB cluster, for example: "google-managed-services-default". If set,
	// the instance IPs for this cluster will be created in the allocated range.
	// The range name must comply with RFC 1035. Specifically, the name must be
	// 1-63 characters long and match the regular expression
	// `[a-z]([-a-z0-9]*[a-z0-9])?`. Field name is intended to be consistent with
	// Cloud SQL.
	AllocatedIpRange string `json:"allocatedIpRange,omitempty"`
	// Network: Optional. The resource link for the VPC network in which cluster
	// resources are created and from which they are accessible via Private IP. The
	// network must belong to the same project as the cluster. It is specified in
	// the form: `projects/{project_number}/global/networks/{network_id}`. This is
	// required to create a cluster.
	Network string `json:"network,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllocatedIpRange") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllocatedIpRange") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkConfig: Metadata related to network configuration.

func (NetworkConfig) MarshalJSON ¶
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type Node ¶
type Node struct {
	// Id: Output only. The identifier of the VM e.g.
	// "test-read-0601-407e52be-ms3l".
	Id string `json:"id,omitempty"`
	// Ip: Output only. The private IP address of the VM e.g. "10.57.0.34".
	Ip string `json:"ip,omitempty"`
	// State: Output only. Determined by state of the compute VM and
	// postgres-service health. Compute VM state can have values listed in
	// https://cloud.google.com/compute/docs/instances/instance-life-cycle and
	// postgres-service health can have values: HEALTHY and UNHEALTHY.
	State string `json:"state,omitempty"`
	// ZoneId: Output only. The Compute Engine zone of the VM e.g. "us-central1-b".
	ZoneId string `json:"zoneId,omitempty"`
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

Node: Details of a single node in the instance. Nodes in an AlloyDB instance are ephemeral, they can change during update, failover, autohealing and resize operations.

func (Node) MarshalJSON ¶
func (s Node) MarshalJSON() ([]byte, error)
type ObservabilityInstanceConfig ¶
added in v0.171.0
type ObservabilityInstanceConfig struct {
	// AssistiveExperiencesEnabled: Whether assistive experiences are enabled for
	// this AlloyDB instance.
	AssistiveExperiencesEnabled bool `json:"assistiveExperiencesEnabled,omitempty"`
	// Enabled: Observability feature status for an instance. This flag is turned
	// "off" by default.
	Enabled bool `json:"enabled,omitempty"`
	// MaxQueryStringLength: Query string length. The default value is 10k.
	MaxQueryStringLength int64 `json:"maxQueryStringLength,omitempty"`
	// PreserveComments: Preserve comments in query string for an instance. This
	// flag is turned "off" by default.
	PreserveComments bool `json:"preserveComments,omitempty"`
	// QueryPlansPerMinute: Number of query execution plans captured by Insights
	// per minute for all queries combined. The default value is 200. Any integer
	// between 0 to 200 is considered valid.
	QueryPlansPerMinute int64 `json:"queryPlansPerMinute,omitempty"`
	// RecordApplicationTags: Record application tags for an instance. This flag is
	// turned "off" by default.
	RecordApplicationTags bool `json:"recordApplicationTags,omitempty"`
	// TrackActiveQueries: Track actively running queries on the instance. If not
	// set, this flag is "off" by default.
	TrackActiveQueries bool `json:"trackActiveQueries,omitempty"`
	// TrackClientAddress: Track client address for an instance. If not set,
	// default value is "off".
	TrackClientAddress bool `json:"trackClientAddress,omitempty"`
	// TrackWaitEventTypes: Output only. Track wait event types during query
	// execution for an instance. This flag is turned "on" by default but tracking
	// is enabled only after observability enabled flag is also turned on. This is
	// read-only flag and only modifiable by internal API.
	TrackWaitEventTypes bool `json:"trackWaitEventTypes,omitempty"`
	// TrackWaitEvents: Track wait events during query execution for an instance.
	// This flag is turned "on" by default but tracking is enabled only after
	// observability enabled flag is also turned on.
	TrackWaitEvents bool `json:"trackWaitEvents,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AssistiveExperiencesEnabled") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssistiveExperiencesEnabled") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ObservabilityInstanceConfig: Observability Instance specific configuration.

func (ObservabilityInstanceConfig) MarshalJSON ¶
added in v0.171.0
func (s ObservabilityInstanceConfig) MarshalJSON() ([]byte, error)
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
	// UpgradeClusterStatus: Output only. UpgradeClusterStatus related metadata.
	UpgradeClusterStatus *UpgradeClusterStatus `json:"upgradeClusterStatus,omitempty"`
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

OperationMetadata: Represents the metadata of the long-running operation.

func (OperationMetadata) MarshalJSON ¶
func (s OperationMetadata) MarshalJSON() ([]byte, error)
type Policy ¶
added in v0.252.0
type Policy struct {
	// CoolDownPeriodSec: The period of time in seconds after a new node is created
	// before the autoscaler will incorporate its resource usage (e.g. CPU
	// utilization) into the autoscaling recommendation algorithm.
	CoolDownPeriodSec int64 `json:"coolDownPeriodSec,omitempty,string"`
	// CpuUtilization: CPU utilization policy for the autoscaler.
	CpuUtilization *CpuUtilization `json:"cpuUtilization,omitempty"`
	// Enabled: If true, autoscaling is enabled for the instance. If not set, the
	// default value is false.
	Enabled bool `json:"enabled,omitempty"`
	// MaxNodeCount: Maximum number of nodes for the autoscaler.
	MaxNodeCount int64 `json:"maxNodeCount,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "CoolDownPeriodSec") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CoolDownPeriodSec") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Policy: Policy for the autoscaler.

func (Policy) MarshalJSON ¶
added in v0.252.0
func (s Policy) MarshalJSON() ([]byte, error)
type PrimaryConfig ¶
type PrimaryConfig struct {
	// SecondaryClusterNames: Output only. Names of the clusters that are
	// replicating from this cluster.
	SecondaryClusterNames []string `json:"secondaryClusterNames,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SecondaryClusterNames") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SecondaryClusterNames") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrimaryConfig: Configuration for the primary cluster. It has the list of clusters that are replicating from this cluster. This should be set if and only if the cluster is of type PRIMARY.

func (PrimaryConfig) MarshalJSON ¶
func (s PrimaryConfig) MarshalJSON() ([]byte, error)
type ProjectsLocationsBackupsCreateCall ¶
type ProjectsLocationsBackupsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupsCreateCall) BackupId ¶
func (c *ProjectsLocationsBackupsCreateCall) BackupId(backupId string) *ProjectsLocationsBackupsCreateCall

BackupId sets the optional parameter "backupId": Required. ID of the requesting object.

func (*ProjectsLocationsBackupsCreateCall) Context ¶
func (c *ProjectsLocationsBackupsCreateCall) Context(ctx context.Context) *ProjectsLocationsBackupsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupsCreateCall) Do ¶
func (c *ProjectsLocationsBackupsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.backups.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupsCreateCall) Fields ¶
func (c *ProjectsLocationsBackupsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupsCreateCall) Header ¶
func (c *ProjectsLocationsBackupsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupsCreateCall) RequestId ¶
func (c *ProjectsLocationsBackupsCreateCall) RequestId(requestId string) *ProjectsLocationsBackupsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupsCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsBackupsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsBackupsDeleteCall ¶
type ProjectsLocationsBackupsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupsDeleteCall) Context ¶
func (c *ProjectsLocationsBackupsDeleteCall) Context(ctx context.Context) *ProjectsLocationsBackupsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupsDeleteCall) Do ¶
func (c *ProjectsLocationsBackupsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.backups.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupsDeleteCall) Etag ¶
func (c *ProjectsLocationsBackupsDeleteCall) Etag(etag string) *ProjectsLocationsBackupsDeleteCall

Etag sets the optional parameter "etag": The current etag of the Backup. If an etag is provided and does not match the current etag of the Backup, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsLocationsBackupsDeleteCall) Fields ¶
func (c *ProjectsLocationsBackupsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupsDeleteCall) Header ¶
func (c *ProjectsLocationsBackupsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupsDeleteCall) RequestId ¶
func (c *ProjectsLocationsBackupsDeleteCall) RequestId(requestId string) *ProjectsLocationsBackupsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupsDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsBackupsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsBackupsGetCall ¶
type ProjectsLocationsBackupsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupsGetCall) Context ¶
func (c *ProjectsLocationsBackupsGetCall) Context(ctx context.Context) *ProjectsLocationsBackupsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupsGetCall) Do ¶
func (c *ProjectsLocationsBackupsGetCall) Do(opts ...googleapi.CallOption) (*Backup, error)

Do executes the "alloydb.projects.locations.backups.get" call. Any non-2xx status code is an error. Response headers are in either *Backup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupsGetCall) Fields ¶
func (c *ProjectsLocationsBackupsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupsGetCall) Header ¶
func (c *ProjectsLocationsBackupsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsBackupsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupsGetCall) View ¶
added in v0.257.0
func (c *ProjectsLocationsBackupsGetCall) View(view string) *ProjectsLocationsBackupsGetCall

View sets the optional parameter "view": The view of the backup to return.

Possible values:

"BACKUP_VIEW_UNSPECIFIED" - Value unspecified, equivalent to BASIC.
"BACKUP_VIEW_BASIC" - Responses include all fields that aren't explicitly


gated behind another view.

"BACKUP_VIEW_CLUSTER_DELETED" - Response include all the field from BASIC


plus the field cluster_deleted, which specifies if the cluster corresponding to this backup is deleted.

type ProjectsLocationsBackupsListCall ¶
type ProjectsLocationsBackupsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupsListCall) Context ¶
func (c *ProjectsLocationsBackupsListCall) Context(ctx context.Context) *ProjectsLocationsBackupsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupsListCall) Do ¶
func (c *ProjectsLocationsBackupsListCall) Do(opts ...googleapi.CallOption) (*ListBackupsResponse, error)

Do executes the "alloydb.projects.locations.backups.list" call. Any non-2xx status code is an error. Response headers are in either *ListBackupsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupsListCall) Fields ¶
func (c *ProjectsLocationsBackupsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupsListCall) Filter ¶
func (c *ProjectsLocationsBackupsListCall) Filter(filter string) *ProjectsLocationsBackupsListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsBackupsListCall) Header ¶
func (c *ProjectsLocationsBackupsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsBackupsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsBackupsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsBackupsListCall) OrderBy ¶
func (c *ProjectsLocationsBackupsListCall) OrderBy(orderBy string) *ProjectsLocationsBackupsListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results

func (*ProjectsLocationsBackupsListCall) PageSize ¶
func (c *ProjectsLocationsBackupsListCall) PageSize(pageSize int64) *ProjectsLocationsBackupsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsBackupsListCall) PageToken ¶
func (c *ProjectsLocationsBackupsListCall) PageToken(pageToken string) *ProjectsLocationsBackupsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsBackupsListCall) Pages ¶
func (c *ProjectsLocationsBackupsListCall) Pages(ctx context.Context, f func(*ListBackupsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsBackupsListCall) View ¶
added in v0.257.0
func (c *ProjectsLocationsBackupsListCall) View(view string) *ProjectsLocationsBackupsListCall

View sets the optional parameter "view": The view of the backup to return.

Possible values:

"BACKUP_VIEW_UNSPECIFIED" - Value unspecified, equivalent to BASIC.
"BACKUP_VIEW_BASIC" - Responses include all fields that aren't explicitly


gated behind another view.

"BACKUP_VIEW_CLUSTER_DELETED" - Response include all the field from BASIC


plus the field cluster_deleted, which specifies if the cluster corresponding to this backup is deleted.

type ProjectsLocationsBackupsPatchCall ¶
type ProjectsLocationsBackupsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsBackupsPatchCall) AllowMissing ¶
func (c *ProjectsLocationsBackupsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsBackupsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, update succeeds even if instance is not found. In that case, a new backup is created and `update_mask` is ignored.

func (*ProjectsLocationsBackupsPatchCall) Context ¶
func (c *ProjectsLocationsBackupsPatchCall) Context(ctx context.Context) *ProjectsLocationsBackupsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsBackupsPatchCall) Do ¶
func (c *ProjectsLocationsBackupsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.backups.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsBackupsPatchCall) Fields ¶
func (c *ProjectsLocationsBackupsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsBackupsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsBackupsPatchCall) Header ¶
func (c *ProjectsLocationsBackupsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsBackupsPatchCall) RequestId ¶
func (c *ProjectsLocationsBackupsPatchCall) RequestId(requestId string) *ProjectsLocationsBackupsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsBackupsPatchCall) UpdateMask ¶
func (c *ProjectsLocationsBackupsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsBackupsPatchCall

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

func (*ProjectsLocationsBackupsPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsBackupsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsBackupsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsBackupsService ¶
type ProjectsLocationsBackupsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsBackupsService ¶
func NewProjectsLocationsBackupsService(s *Service) *ProjectsLocationsBackupsService
func (*ProjectsLocationsBackupsService) Create ¶
func (r *ProjectsLocationsBackupsService) Create(parent string, backup *Backup) *ProjectsLocationsBackupsCreateCall

Create: Creates a new Backup in a given project and location.

- parent: Value for parent.

func (*ProjectsLocationsBackupsService) Delete ¶
func (r *ProjectsLocationsBackupsService) Delete(name string) *ProjectsLocationsBackupsDeleteCall

Delete: Deletes a single Backup.

name: Name of the resource. For the required format, see the comment on the Backup.name field.
func (*ProjectsLocationsBackupsService) Get ¶
func (r *ProjectsLocationsBackupsService) Get(name string) *ProjectsLocationsBackupsGetCall

Get: Gets details of a single Backup.

- name: Name of the resource.

func (*ProjectsLocationsBackupsService) List ¶
func (r *ProjectsLocationsBackupsService) List(parent string) *ProjectsLocationsBackupsListCall

List: Lists Backups in a given project and location.

- parent: Parent value for ListBackupsRequest.

func (*ProjectsLocationsBackupsService) Patch ¶
func (r *ProjectsLocationsBackupsService) Patch(name string, backup *Backup) *ProjectsLocationsBackupsPatchCall

Patch: Updates the parameters of a single Backup.

name: Output only. The name of the backup resource with the format: * projects/{project}/locations/{region}/backups/{backup_id} where the cluster and backup ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the backup resource name is the name of the parent resource: * projects/{project}/locations/{region}.
type ProjectsLocationsClustersCreateCall ¶
type ProjectsLocationsClustersCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersCreateCall) ClusterId ¶
func (c *ProjectsLocationsClustersCreateCall) ClusterId(clusterId string) *ProjectsLocationsClustersCreateCall

ClusterId sets the optional parameter "clusterId": Required. ID of the requesting object.

func (*ProjectsLocationsClustersCreateCall) Context ¶
func (c *ProjectsLocationsClustersCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersCreateCall) Do ¶
func (c *ProjectsLocationsClustersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersCreateCall) Fields ¶
func (c *ProjectsLocationsClustersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersCreateCall) Header ¶
func (c *ProjectsLocationsClustersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersCreateCall) RequestId ¶
func (c *ProjectsLocationsClustersCreateCall) RequestId(requestId string) *ProjectsLocationsClustersCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersCreatesecondaryCall ¶
type ProjectsLocationsClustersCreatesecondaryCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersCreatesecondaryCall) ClusterId ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) ClusterId(clusterId string) *ProjectsLocationsClustersCreatesecondaryCall

ClusterId sets the optional parameter "clusterId": Required. ID of the requesting object (the secondary cluster).

func (*ProjectsLocationsClustersCreatesecondaryCall) Context ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) Context(ctx context.Context) *ProjectsLocationsClustersCreatesecondaryCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersCreatesecondaryCall) Do ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.createsecondary" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersCreatesecondaryCall) Fields ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersCreatesecondaryCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersCreatesecondaryCall) Header ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersCreatesecondaryCall) RequestId ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) RequestId(requestId string) *ProjectsLocationsClustersCreatesecondaryCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersCreatesecondaryCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersCreatesecondaryCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersCreatesecondaryCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersDeleteCall ¶
type ProjectsLocationsClustersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersDeleteCall) Context ¶
func (c *ProjectsLocationsClustersDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersDeleteCall) Do ¶
func (c *ProjectsLocationsClustersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersDeleteCall) Etag ¶
func (c *ProjectsLocationsClustersDeleteCall) Etag(etag string) *ProjectsLocationsClustersDeleteCall

Etag sets the optional parameter "etag": The current etag of the Cluster. If an etag is provided and does not match the current etag of the Cluster, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsLocationsClustersDeleteCall) Fields ¶
func (c *ProjectsLocationsClustersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersDeleteCall) Force ¶
func (c *ProjectsLocationsClustersDeleteCall) Force(force bool) *ProjectsLocationsClustersDeleteCall

Force sets the optional parameter "force": Whether to cascade delete child instances for given cluster.

func (*ProjectsLocationsClustersDeleteCall) Header ¶
func (c *ProjectsLocationsClustersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersDeleteCall) RequestId ¶
func (c *ProjectsLocationsClustersDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersExportCall ¶
added in v0.209.0
type ProjectsLocationsClustersExportCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersExportCall) Context ¶
added in v0.209.0
func (c *ProjectsLocationsClustersExportCall) Context(ctx context.Context) *ProjectsLocationsClustersExportCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersExportCall) Do ¶
added in v0.209.0
func (c *ProjectsLocationsClustersExportCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.export" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersExportCall) Fields ¶
added in v0.209.0
func (c *ProjectsLocationsClustersExportCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersExportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersExportCall) Header ¶
added in v0.209.0
func (c *ProjectsLocationsClustersExportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersGetCall ¶
type ProjectsLocationsClustersGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersGetCall) Context ¶
func (c *ProjectsLocationsClustersGetCall) Context(ctx context.Context) *ProjectsLocationsClustersGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersGetCall) Do ¶
func (c *ProjectsLocationsClustersGetCall) Do(opts ...googleapi.CallOption) (*Cluster, error)

Do executes the "alloydb.projects.locations.clusters.get" call. Any non-2xx status code is an error. Response headers are in either *Cluster.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersGetCall) Fields ¶
func (c *ProjectsLocationsClustersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersGetCall) Header ¶
func (c *ProjectsLocationsClustersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersGetCall) View ¶
func (c *ProjectsLocationsClustersGetCall) View(view string) *ProjectsLocationsClustersGetCall

View sets the optional parameter "view": The view of the cluster to return. Returns all default fields if not set.

Possible values:

"CLUSTER_VIEW_UNSPECIFIED" - CLUSTER_VIEW_UNSPECIFIED Not specified,


equivalent to BASIC.

"CLUSTER_VIEW_BASIC" - BASIC server responses include all the relevant


cluster details, excluding Cluster.ContinuousBackupInfo.EarliestRestorableTime and other view-specific fields. The default value.

"CLUSTER_VIEW_CONTINUOUS_BACKUP" - CONTINUOUS_BACKUP response returns all


the fields from BASIC plus the earliest restorable time if continuous backups are enabled. May increase latency.

type ProjectsLocationsClustersImportCall ¶
added in v0.222.0
type ProjectsLocationsClustersImportCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersImportCall) Context ¶
added in v0.222.0
func (c *ProjectsLocationsClustersImportCall) Context(ctx context.Context) *ProjectsLocationsClustersImportCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersImportCall) Do ¶
added in v0.222.0
func (c *ProjectsLocationsClustersImportCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.import" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersImportCall) Fields ¶
added in v0.222.0
func (c *ProjectsLocationsClustersImportCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersImportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersImportCall) Header ¶
added in v0.222.0
func (c *ProjectsLocationsClustersImportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersInstancesCreateCall ¶
type ProjectsLocationsClustersInstancesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesCreateCall) Context ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesCreateCall) Do ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesCreateCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesCreateCall) Header ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesCreateCall) InstanceId ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) InstanceId(instanceId string) *ProjectsLocationsClustersInstancesCreateCall

InstanceId sets the optional parameter "instanceId": Required. ID of the requesting object.

func (*ProjectsLocationsClustersInstancesCreateCall) RequestId ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersInstancesCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersInstancesCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersInstancesCreatesecondaryCall ¶
type ProjectsLocationsClustersInstancesCreatesecondaryCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) Context ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesCreatesecondaryCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) Do ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.createsecondary" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesCreatesecondaryCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) Header ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) InstanceId ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) InstanceId(instanceId string) *ProjectsLocationsClustersInstancesCreatesecondaryCall

InstanceId sets the optional parameter "instanceId": Required. ID of the requesting object.

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) RequestId ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesCreatesecondaryCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersInstancesCreatesecondaryCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersInstancesCreatesecondaryCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesCreatesecondaryCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersInstancesDeleteCall ¶
type ProjectsLocationsClustersInstancesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesDeleteCall) Context ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesDeleteCall) Do ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesDeleteCall) Etag ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) Etag(etag string) *ProjectsLocationsClustersInstancesDeleteCall

Etag sets the optional parameter "etag": The current etag of the Instance. If an etag is provided and does not match the current etag of the Instance, deletion will be blocked and an ABORTED error will be returned.

func (*ProjectsLocationsClustersInstancesDeleteCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesDeleteCall) Header ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesDeleteCall) RequestId ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersInstancesDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersInstancesDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersInstancesFailoverCall ¶
type ProjectsLocationsClustersInstancesFailoverCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesFailoverCall) Context ¶
func (c *ProjectsLocationsClustersInstancesFailoverCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesFailoverCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesFailoverCall) Do ¶
func (c *ProjectsLocationsClustersInstancesFailoverCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.failover" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesFailoverCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesFailoverCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesFailoverCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesFailoverCall) Header ¶
func (c *ProjectsLocationsClustersInstancesFailoverCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersInstancesGetCall ¶
type ProjectsLocationsClustersInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesGetCall) Context ¶
func (c *ProjectsLocationsClustersInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesGetCall) Do ¶
func (c *ProjectsLocationsClustersInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "alloydb.projects.locations.clusters.instances.get" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesGetCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesGetCall) Header ¶
func (c *ProjectsLocationsClustersInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersInstancesGetCall) View ¶
func (c *ProjectsLocationsClustersInstancesGetCall) View(view string) *ProjectsLocationsClustersInstancesGetCall

View sets the optional parameter "view": The view of the instance to return.

Possible values:

"INSTANCE_VIEW_UNSPECIFIED" - INSTANCE_VIEW_UNSPECIFIED Not specified,


equivalent to BASIC.

"INSTANCE_VIEW_BASIC" - BASIC server responses for a primary or read


instance include all the relevant instance details, excluding the details of each node in the instance. The default value.

"INSTANCE_VIEW_FULL" - FULL response is equivalent to BASIC for primary


instance (for now). For read pool instance, this includes details of each node in the pool.

type ProjectsLocationsClustersInstancesGetConnectionInfoCall ¶
type ProjectsLocationsClustersInstancesGetConnectionInfoCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) Context ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesGetConnectionInfoCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) Do ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Do(opts ...googleapi.CallOption) (*ConnectionInfo, error)

Do executes the "alloydb.projects.locations.clusters.instances.getConnectionInfo" call. Any non-2xx status code is an error. Response headers are in either *ConnectionInfo.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesGetConnectionInfoCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) Header ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersInstancesGetConnectionInfoCall) RequestId ¶
func (c *ProjectsLocationsClustersInstancesGetConnectionInfoCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsClustersInstancesInjectFaultCall ¶
type ProjectsLocationsClustersInstancesInjectFaultCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesInjectFaultCall) Context ¶
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesInjectFaultCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesInjectFaultCall) Do ¶
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.injectFault" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesInjectFaultCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesInjectFaultCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesInjectFaultCall) Header ¶
func (c *ProjectsLocationsClustersInstancesInjectFaultCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersInstancesListCall ¶
type ProjectsLocationsClustersInstancesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesListCall) Context ¶
func (c *ProjectsLocationsClustersInstancesListCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesListCall) Do ¶
func (c *ProjectsLocationsClustersInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)

Do executes the "alloydb.projects.locations.clusters.instances.list" call. Any non-2xx status code is an error. Response headers are in either *ListInstancesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesListCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesListCall) Filter ¶
func (c *ProjectsLocationsClustersInstancesListCall) Filter(filter string) *ProjectsLocationsClustersInstancesListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsClustersInstancesListCall) Header ¶
func (c *ProjectsLocationsClustersInstancesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersInstancesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersInstancesListCall) OrderBy ¶
func (c *ProjectsLocationsClustersInstancesListCall) OrderBy(orderBy string) *ProjectsLocationsClustersInstancesListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results

func (*ProjectsLocationsClustersInstancesListCall) PageSize ¶
func (c *ProjectsLocationsClustersInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsClustersInstancesListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsClustersInstancesListCall) PageToken ¶
func (c *ProjectsLocationsClustersInstancesListCall) PageToken(pageToken string) *ProjectsLocationsClustersInstancesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsClustersInstancesListCall) Pages ¶
func (c *ProjectsLocationsClustersInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsClustersInstancesPatchCall ¶
type ProjectsLocationsClustersInstancesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesPatchCall) AllowMissing ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersInstancesPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, update succeeds even if instance is not found. In that case, a new instance is created and `update_mask` is ignored.

func (*ProjectsLocationsClustersInstancesPatchCall) Context ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesPatchCall) Do ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesPatchCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesPatchCall) Header ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersInstancesPatchCall) RequestId ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) RequestId(requestId string) *ProjectsLocationsClustersInstancesPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersInstancesPatchCall) UpdateMask ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersInstancesPatchCall

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

func (*ProjectsLocationsClustersInstancesPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersInstancesPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersInstancesPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersInstancesRestartCall ¶
type ProjectsLocationsClustersInstancesRestartCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersInstancesRestartCall) Context ¶
func (c *ProjectsLocationsClustersInstancesRestartCall) Context(ctx context.Context) *ProjectsLocationsClustersInstancesRestartCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersInstancesRestartCall) Do ¶
func (c *ProjectsLocationsClustersInstancesRestartCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.instances.restart" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersInstancesRestartCall) Fields ¶
func (c *ProjectsLocationsClustersInstancesRestartCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersInstancesRestartCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersInstancesRestartCall) Header ¶
func (c *ProjectsLocationsClustersInstancesRestartCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersInstancesService ¶
type ProjectsLocationsClustersInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsClustersInstancesService ¶
func NewProjectsLocationsClustersInstancesService(s *Service) *ProjectsLocationsClustersInstancesService
func (*ProjectsLocationsClustersInstancesService) Create ¶
func (r *ProjectsLocationsClustersInstancesService) Create(parent string, instance *Instance) *ProjectsLocationsClustersInstancesCreateCall

Create: Creates a new Instance in a given project and location.

parent: The name of the parent resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) Createsecondary ¶
func (r *ProjectsLocationsClustersInstancesService) Createsecondary(parent string, instance *Instance) *ProjectsLocationsClustersInstancesCreatesecondaryCall

Createsecondary: Creates a new SECONDARY Instance in a given project and location.

parent: The name of the parent resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) Delete ¶
func (r *ProjectsLocationsClustersInstancesService) Delete(name string) *ProjectsLocationsClustersInstancesDeleteCall

Delete: Deletes a single Instance.

name: The name of the resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) Failover ¶
func (r *ProjectsLocationsClustersInstancesService) Failover(name string, failoverinstancerequest *FailoverInstanceRequest) *ProjectsLocationsClustersInstancesFailoverCall

Failover: Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

name: The name of the resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) Get ¶
func (r *ProjectsLocationsClustersInstancesService) Get(name string) *ProjectsLocationsClustersInstancesGetCall

Get: Gets details of a single Instance.

name: The name of the resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) GetConnectionInfo ¶
func (r *ProjectsLocationsClustersInstancesService) GetConnectionInfo(parent string) *ProjectsLocationsClustersInstancesGetConnectionInfoCall

GetConnectionInfo: Get instance metadata used for a connection.

parent: The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{insta nce}.
func (*ProjectsLocationsClustersInstancesService) InjectFault ¶
func (r *ProjectsLocationsClustersInstancesService) InjectFault(name string, injectfaultrequest *InjectFaultRequest) *ProjectsLocationsClustersInstancesInjectFaultCall

InjectFault: Injects fault in an instance. Imperative only.

name: The name of the resource. For the required format, see the comment on the Instance.name field.
func (*ProjectsLocationsClustersInstancesService) List ¶
func (r *ProjectsLocationsClustersInstancesService) List(parent string) *ProjectsLocationsClustersInstancesListCall

List: Lists Instances in a given project and location.

parent: The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats: * projects/{project}/locations/-/clusters/- * projects/{project}/locations/{region}/clusters/-.
func (*ProjectsLocationsClustersInstancesService) Patch ¶
func (r *ProjectsLocationsClustersInstancesService) Patch(name string, instance *Instance) *ProjectsLocationsClustersInstancesPatchCall

Patch: Updates the parameters of a single Instance.

name: Output only. The name of the instance resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{inst ance_id} where the cluster and instance ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: * projects/{project}/locations/{region}/clusters/{cluster_id}.
func (*ProjectsLocationsClustersInstancesService) Restart ¶
func (r *ProjectsLocationsClustersInstancesService) Restart(name string, restartinstancerequest *RestartInstanceRequest) *ProjectsLocationsClustersInstancesRestartCall

Restart: Restart an Instance in a cluster. Imperative only.

name: The name of the resource. For the required format, see the comment on the Instance.name field.
type ProjectsLocationsClustersListCall ¶
type ProjectsLocationsClustersListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersListCall) Context ¶
func (c *ProjectsLocationsClustersListCall) Context(ctx context.Context) *ProjectsLocationsClustersListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersListCall) Do ¶
func (c *ProjectsLocationsClustersListCall) Do(opts ...googleapi.CallOption) (*ListClustersResponse, error)

Do executes the "alloydb.projects.locations.clusters.list" call. Any non-2xx status code is an error. Response headers are in either *ListClustersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersListCall) Fields ¶
func (c *ProjectsLocationsClustersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersListCall) Filter ¶
func (c *ProjectsLocationsClustersListCall) Filter(filter string) *ProjectsLocationsClustersListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsClustersListCall) Header ¶
func (c *ProjectsLocationsClustersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersListCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersListCall) OrderBy ¶
func (c *ProjectsLocationsClustersListCall) OrderBy(orderBy string) *ProjectsLocationsClustersListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results

func (*ProjectsLocationsClustersListCall) PageSize ¶
func (c *ProjectsLocationsClustersListCall) PageSize(pageSize int64) *ProjectsLocationsClustersListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsClustersListCall) PageToken ¶
func (c *ProjectsLocationsClustersListCall) PageToken(pageToken string) *ProjectsLocationsClustersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsClustersListCall) Pages ¶
func (c *ProjectsLocationsClustersListCall) Pages(ctx context.Context, f func(*ListClustersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsClustersPatchCall ¶
type ProjectsLocationsClustersPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersPatchCall) AllowMissing ¶
func (c *ProjectsLocationsClustersPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, update succeeds even if cluster is not found. In that case, a new cluster is created and `update_mask` is ignored.

func (*ProjectsLocationsClustersPatchCall) Context ¶
func (c *ProjectsLocationsClustersPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersPatchCall) Do ¶
func (c *ProjectsLocationsClustersPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersPatchCall) Fields ¶
func (c *ProjectsLocationsClustersPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersPatchCall) Header ¶
func (c *ProjectsLocationsClustersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersPatchCall) RequestId ¶
func (c *ProjectsLocationsClustersPatchCall) RequestId(requestId string) *ProjectsLocationsClustersPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersPatchCall) UpdateMask ¶
func (c *ProjectsLocationsClustersPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersPatchCall

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

func (*ProjectsLocationsClustersPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

type ProjectsLocationsClustersPromoteCall ¶
type ProjectsLocationsClustersPromoteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersPromoteCall) Context ¶
func (c *ProjectsLocationsClustersPromoteCall) Context(ctx context.Context) *ProjectsLocationsClustersPromoteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersPromoteCall) Do ¶
func (c *ProjectsLocationsClustersPromoteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.promote" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersPromoteCall) Fields ¶
func (c *ProjectsLocationsClustersPromoteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersPromoteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersPromoteCall) Header ¶
func (c *ProjectsLocationsClustersPromoteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersRestoreCall ¶
type ProjectsLocationsClustersRestoreCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersRestoreCall) Context ¶
func (c *ProjectsLocationsClustersRestoreCall) Context(ctx context.Context) *ProjectsLocationsClustersRestoreCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersRestoreCall) Do ¶
func (c *ProjectsLocationsClustersRestoreCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.restore" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersRestoreCall) Fields ¶
func (c *ProjectsLocationsClustersRestoreCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersRestoreCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersRestoreCall) Header ¶
func (c *ProjectsLocationsClustersRestoreCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersRestoreFromCloudSQLCall ¶
added in v0.212.0
type ProjectsLocationsClustersRestoreFromCloudSQLCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersRestoreFromCloudSQLCall) Context ¶
added in v0.212.0
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Context(ctx context.Context) *ProjectsLocationsClustersRestoreFromCloudSQLCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersRestoreFromCloudSQLCall) Do ¶
added in v0.212.0
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.restoreFromCloudSQL" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersRestoreFromCloudSQLCall) Fields ¶
added in v0.212.0
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersRestoreFromCloudSQLCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersRestoreFromCloudSQLCall) Header ¶
added in v0.212.0
func (c *ProjectsLocationsClustersRestoreFromCloudSQLCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersService ¶
type ProjectsLocationsClustersService struct {
	Instances *ProjectsLocationsClustersInstancesService

	Users *ProjectsLocationsClustersUsersService
	// contains filtered or unexported fields
}
func NewProjectsLocationsClustersService ¶
func NewProjectsLocationsClustersService(s *Service) *ProjectsLocationsClustersService
func (*ProjectsLocationsClustersService) Create ¶
func (r *ProjectsLocationsClustersService) Create(parent string, cluster *Cluster) *ProjectsLocationsClustersCreateCall

Create: Creates a new Cluster in a given project and location.

parent: The location of the new cluster. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Createsecondary ¶
func (r *ProjectsLocationsClustersService) Createsecondary(parent string, cluster *Cluster) *ProjectsLocationsClustersCreatesecondaryCall

Createsecondary: Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

parent: The location of the new cluster. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Delete ¶
func (r *ProjectsLocationsClustersService) Delete(name string) *ProjectsLocationsClustersDeleteCall

Delete: Deletes a single Cluster.

name: The name of the resource. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Export ¶
added in v0.209.0
func (r *ProjectsLocationsClustersService) Export(name string, exportclusterrequest *ExportClusterRequest) *ProjectsLocationsClustersExportCall

Export: Exports data from the cluster. Imperative only.

- name: The resource name of the cluster.

func (*ProjectsLocationsClustersService) Get ¶
func (r *ProjectsLocationsClustersService) Get(name string) *ProjectsLocationsClustersGetCall

Get: Gets details of a single Cluster.

name: The name of the resource. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Import ¶
added in v0.222.0
func (r *ProjectsLocationsClustersService) Import(name string, importclusterrequest *ImportClusterRequest) *ProjectsLocationsClustersImportCall

Import: Imports data to the cluster. Imperative only.

- name: The resource name of the cluster.

func (*ProjectsLocationsClustersService) List ¶
func (r *ProjectsLocationsClustersService) List(parent string) *ProjectsLocationsClustersListCall

List: Lists Clusters in a given project and location.

parent: The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:
projects/{project}/locations/-.
func (*ProjectsLocationsClustersService) Patch ¶
func (r *ProjectsLocationsClustersService) Patch(name string, cluster *Cluster) *ProjectsLocationsClustersPatchCall

Patch: Updates the parameters of a single Cluster.

name: Output only. The name of the cluster resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see https://google.aip.dev/122. The prefix of the cluster resource name is the name of the parent resource: * projects/{project}/locations/{region}.
func (*ProjectsLocationsClustersService) Promote ¶
func (r *ProjectsLocationsClustersService) Promote(name string, promoteclusterrequest *PromoteClusterRequest) *ProjectsLocationsClustersPromoteCall

Promote: Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

name: The name of the resource. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Restore ¶
func (r *ProjectsLocationsClustersService) Restore(parent string, restoreclusterrequest *RestoreClusterRequest) *ProjectsLocationsClustersRestoreCall

Restore: Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

parent: The name of the parent resource. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) RestoreFromCloudSQL ¶
added in v0.212.0
func (r *ProjectsLocationsClustersService) RestoreFromCloudSQL(parent string, restorefromcloudsqlrequest *RestoreFromCloudSQLRequest) *ProjectsLocationsClustersRestoreFromCloudSQLCall

RestoreFromCloudSQL: Restores an AlloyDB cluster from a CloudSQL resource.

parent: The location of the new cluster. For the required format, see the comment on Cluster.name field.
func (*ProjectsLocationsClustersService) Switchover ¶
added in v0.186.0
func (r *ProjectsLocationsClustersService) Switchover(name string, switchoverclusterrequest *SwitchoverClusterRequest) *ProjectsLocationsClustersSwitchoverCall

Switchover: Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

name: The name of the resource. For the required format, see the comment on the Cluster.name field.
func (*ProjectsLocationsClustersService) Upgrade ¶
added in v0.193.0
func (r *ProjectsLocationsClustersService) Upgrade(name string, upgradeclusterrequest *UpgradeClusterRequest) *ProjectsLocationsClustersUpgradeCall

Upgrade: Upgrades a single Cluster. Imperative only.

- name: The resource name of the cluster.

type ProjectsLocationsClustersSwitchoverCall ¶
added in v0.186.0
type ProjectsLocationsClustersSwitchoverCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersSwitchoverCall) Context ¶
added in v0.186.0
func (c *ProjectsLocationsClustersSwitchoverCall) Context(ctx context.Context) *ProjectsLocationsClustersSwitchoverCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersSwitchoverCall) Do ¶
added in v0.186.0
func (c *ProjectsLocationsClustersSwitchoverCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.switchover" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersSwitchoverCall) Fields ¶
added in v0.186.0
func (c *ProjectsLocationsClustersSwitchoverCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersSwitchoverCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersSwitchoverCall) Header ¶
added in v0.186.0
func (c *ProjectsLocationsClustersSwitchoverCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersUpgradeCall ¶
added in v0.193.0
type ProjectsLocationsClustersUpgradeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUpgradeCall) Context ¶
added in v0.193.0
func (c *ProjectsLocationsClustersUpgradeCall) Context(ctx context.Context) *ProjectsLocationsClustersUpgradeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUpgradeCall) Do ¶
added in v0.193.0
func (c *ProjectsLocationsClustersUpgradeCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "alloydb.projects.locations.clusters.upgrade" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUpgradeCall) Fields ¶
added in v0.193.0
func (c *ProjectsLocationsClustersUpgradeCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUpgradeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUpgradeCall) Header ¶
added in v0.193.0
func (c *ProjectsLocationsClustersUpgradeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsClustersUsersCreateCall ¶
type ProjectsLocationsClustersUsersCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUsersCreateCall) Context ¶
func (c *ProjectsLocationsClustersUsersCreateCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUsersCreateCall) Do ¶
func (c *ProjectsLocationsClustersUsersCreateCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "alloydb.projects.locations.clusters.users.create" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUsersCreateCall) Fields ¶
func (c *ProjectsLocationsClustersUsersCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUsersCreateCall) Header ¶
func (c *ProjectsLocationsClustersUsersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersUsersCreateCall) RequestId ¶
func (c *ProjectsLocationsClustersUsersCreateCall) RequestId(requestId string) *ProjectsLocationsClustersUsersCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersUsersCreateCall) UserId ¶
func (c *ProjectsLocationsClustersUsersCreateCall) UserId(userId string) *ProjectsLocationsClustersUsersCreateCall

UserId sets the optional parameter "userId": Required. ID of the requesting object.

func (*ProjectsLocationsClustersUsersCreateCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersUsersCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsClustersUsersDeleteCall ¶
type ProjectsLocationsClustersUsersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUsersDeleteCall) Context ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUsersDeleteCall) Do ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "alloydb.projects.locations.clusters.users.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUsersDeleteCall) Fields ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUsersDeleteCall) Header ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersUsersDeleteCall) RequestId ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) RequestId(requestId string) *ProjectsLocationsClustersUsersDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersUsersDeleteCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersUsersDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsClustersUsersGetCall ¶
type ProjectsLocationsClustersUsersGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUsersGetCall) Context ¶
func (c *ProjectsLocationsClustersUsersGetCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUsersGetCall) Do ¶
func (c *ProjectsLocationsClustersUsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "alloydb.projects.locations.clusters.users.get" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUsersGetCall) Fields ¶
func (c *ProjectsLocationsClustersUsersGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUsersGetCall) Header ¶
func (c *ProjectsLocationsClustersUsersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersUsersGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersUsersGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersUsersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsClustersUsersListCall ¶
type ProjectsLocationsClustersUsersListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUsersListCall) Context ¶
func (c *ProjectsLocationsClustersUsersListCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUsersListCall) Do ¶
func (c *ProjectsLocationsClustersUsersListCall) Do(opts ...googleapi.CallOption) (*ListUsersResponse, error)

Do executes the "alloydb.projects.locations.clusters.users.list" call. Any non-2xx status code is an error. Response headers are in either *ListUsersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUsersListCall) Fields ¶
func (c *ProjectsLocationsClustersUsersListCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUsersListCall) Filter ¶
func (c *ProjectsLocationsClustersUsersListCall) Filter(filter string) *ProjectsLocationsClustersUsersListCall

Filter sets the optional parameter "filter": Filtering results

func (*ProjectsLocationsClustersUsersListCall) Header ¶
func (c *ProjectsLocationsClustersUsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersUsersListCall) IfNoneMatch ¶
func (c *ProjectsLocationsClustersUsersListCall) IfNoneMatch(entityTag string) *ProjectsLocationsClustersUsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsClustersUsersListCall) OrderBy ¶
func (c *ProjectsLocationsClustersUsersListCall) OrderBy(orderBy string) *ProjectsLocationsClustersUsersListCall

OrderBy sets the optional parameter "orderBy": Hint for how to order the results

func (*ProjectsLocationsClustersUsersListCall) PageSize ¶
func (c *ProjectsLocationsClustersUsersListCall) PageSize(pageSize int64) *ProjectsLocationsClustersUsersListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsClustersUsersListCall) PageToken ¶
func (c *ProjectsLocationsClustersUsersListCall) PageToken(pageToken string) *ProjectsLocationsClustersUsersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsClustersUsersListCall) Pages ¶
func (c *ProjectsLocationsClustersUsersListCall) Pages(ctx context.Context, f func(*ListUsersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsClustersUsersPatchCall ¶
type ProjectsLocationsClustersUsersPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsClustersUsersPatchCall) AllowMissing ¶
func (c *ProjectsLocationsClustersUsersPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsClustersUsersPatchCall

AllowMissing sets the optional parameter "allowMissing": Allow missing fields in the update mask.

func (*ProjectsLocationsClustersUsersPatchCall) Context ¶
func (c *ProjectsLocationsClustersUsersPatchCall) Context(ctx context.Context) *ProjectsLocationsClustersUsersPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsClustersUsersPatchCall) Do ¶
func (c *ProjectsLocationsClustersUsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "alloydb.projects.locations.clusters.users.patch" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsClustersUsersPatchCall) Fields ¶
func (c *ProjectsLocationsClustersUsersPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsClustersUsersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsClustersUsersPatchCall) Header ¶
func (c *ProjectsLocationsClustersUsersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsClustersUsersPatchCall) RequestId ¶
func (c *ProjectsLocationsClustersUsersPatchCall) RequestId(requestId string) *ProjectsLocationsClustersUsersPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsClustersUsersPatchCall) UpdateMask ¶
func (c *ProjectsLocationsClustersUsersPatchCall) UpdateMask(updateMask string) *ProjectsLocationsClustersUsersPatchCall

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

func (*ProjectsLocationsClustersUsersPatchCall) ValidateOnly ¶
func (c *ProjectsLocationsClustersUsersPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsClustersUsersPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, the backend validates the request, but doesn't actually execute it.

type ProjectsLocationsClustersUsersService ¶
type ProjectsLocationsClustersUsersService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsClustersUsersService ¶
func NewProjectsLocationsClustersUsersService(s *Service) *ProjectsLocationsClustersUsersService
func (*ProjectsLocationsClustersUsersService) Create ¶
func (r *ProjectsLocationsClustersUsersService) Create(parent string, user *User) *ProjectsLocationsClustersUsersCreateCall

Create: Creates a new User in a given project, location, and cluster.

- parent: Value for parent.

func (*ProjectsLocationsClustersUsersService) Delete ¶
func (r *ProjectsLocationsClustersUsersService) Delete(name string) *ProjectsLocationsClustersUsersDeleteCall

Delete: Deletes a single User.

name: The name of the resource. For the required format, see the comment on the User.name field.
func (*ProjectsLocationsClustersUsersService) Get ¶
func (r *ProjectsLocationsClustersUsersService) Get(name string) *ProjectsLocationsClustersUsersGetCall

Get: Gets details of a single User.

name: The name of the resource. For the required format, see the comment on the User.name field.
func (*ProjectsLocationsClustersUsersService) List ¶
func (r *ProjectsLocationsClustersUsersService) List(parent string) *ProjectsLocationsClustersUsersListCall

List: Lists Users in a given project and location.

- parent: Parent value for ListUsersRequest.

func (*ProjectsLocationsClustersUsersService) Patch ¶
func (r *ProjectsLocationsClustersUsersService) Patch(name string, user *User) *ProjectsLocationsClustersUsersPatchCall

Patch: Updates the parameters of a single User.

name: Output only. Name of the resource in the form of projects/{project}/locations/{location}/cluster/{cluster}/users/{user}.
type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)

Do executes the "alloydb.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationLocation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "alloydb.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "alloydb.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "alloydb.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "alloydb.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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

Do executes the "alloydb.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
added in v0.252.0
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

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	Backups *ProjectsLocationsBackupsService

	Clusters *ProjectsLocationsClustersService

	Operations *ProjectsLocationsOperationsService

	SupportedDatabaseFlags *ProjectsLocationsSupportedDatabaseFlagsService
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

type ProjectsLocationsSupportedDatabaseFlagsListCall ¶
type ProjectsLocationsSupportedDatabaseFlagsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Context ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Context(ctx context.Context) *ProjectsLocationsSupportedDatabaseFlagsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Do ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Do(opts ...googleapi.CallOption) (*ListSupportedDatabaseFlagsResponse, error)

Do executes the "alloydb.projects.locations.supportedDatabaseFlags.list" call. Any non-2xx status code is an error. Response headers are in either *ListSupportedDatabaseFlagsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Fields ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSupportedDatabaseFlagsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Header ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSupportedDatabaseFlagsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) PageSize ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) PageSize(pageSize int64) *ProjectsLocationsSupportedDatabaseFlagsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) PageToken ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) PageToken(pageToken string) *ProjectsLocationsSupportedDatabaseFlagsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Pages ¶
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Pages(ctx context.Context, f func(*ListSupportedDatabaseFlagsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsSupportedDatabaseFlagsListCall) Scope ¶
added in v0.224.0
func (c *ProjectsLocationsSupportedDatabaseFlagsListCall) Scope(scope string) *ProjectsLocationsSupportedDatabaseFlagsListCall

Scope sets the optional parameter "scope": The scope for which supported flags are requested. If not specified, default is DATABASE.

Possible values:

"SCOPE_UNSPECIFIED" - The scope of the flag is not specified. Default is


DATABASE.

"DATABASE" - The flag is a database flag.
"CONNECTION_POOL" - The flag is a connection pool flag.

type ProjectsLocationsSupportedDatabaseFlagsService ¶
type ProjectsLocationsSupportedDatabaseFlagsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsSupportedDatabaseFlagsService ¶
func NewProjectsLocationsSupportedDatabaseFlagsService(s *Service) *ProjectsLocationsSupportedDatabaseFlagsService
func (*ProjectsLocationsSupportedDatabaseFlagsService) List ¶
func (r *ProjectsLocationsSupportedDatabaseFlagsService) List(parent string) *ProjectsLocationsSupportedDatabaseFlagsListCall

List: Lists SupportedDatabaseFlags for a given project and location.

parent: The name of the parent resource. The required format is: * projects/{project}/locations/{location} Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.
type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type PromoteClusterRequest ¶
type PromoteClusterRequest struct {
	// Etag: Optional. The current etag of the Cluster. If an etag is provided and
	// does not match the current etag of the Cluster, deletion will be blocked and
	// an ABORTED error will be returned.
	Etag string `json:"etag,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// original operation with the same request ID was received, and if so, will
	// ignore the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
	ValidateOnly bool `json:"validateOnly,omitempty"`
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

PromoteClusterRequest: Message for promoting a Cluster

func (PromoteClusterRequest) MarshalJSON ¶
func (s PromoteClusterRequest) MarshalJSON() ([]byte, error)
type PscAutoConnectionConfig ¶
added in v0.224.0
type PscAutoConnectionConfig struct {
	// ConsumerNetwork: The consumer network for the PSC service automation,
	// example: "projects/vpc-host-project/global/networks/default". The consumer
	// network might be hosted a different project than the consumer project.
	ConsumerNetwork string `json:"consumerNetwork,omitempty"`
	// ConsumerNetworkStatus: Output only. The status of the service connection
	// policy. Possible values: "STATE_UNSPECIFIED" - Default state, when
	// Connection Map is created initially. "VALID" - Set when policy and map
	// configuration is valid, and their matching can lead to allowing creation of
	// PSC Connections subject to other constraints like connections limit.
	// "CONNECTION_POLICY_MISSING" - No Service Connection Policy found for this
	// network and Service Class "POLICY_LIMIT_REACHED" - Service Connection Policy
	// limit reached for this network and Service Class
	// "CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED" - The consumer instance project
	// is not in AllowedGoogleProducersResourceHierarchyLevels of the matching
	// ServiceConnectionPolicy.
	ConsumerNetworkStatus string `json:"consumerNetworkStatus,omitempty"`
	// ConsumerProject: The consumer project to which the PSC service automation
	// endpoint will be created.
	ConsumerProject string `json:"consumerProject,omitempty"`
	// IpAddress: Output only. The IP address of the PSC service automation
	// endpoint.
	IpAddress string `json:"ipAddress,omitempty"`
	// Status: Output only. The status of the PSC service automation connection.
	// Possible values: "STATE_UNSPECIFIED" - An invalid state as the default case.
	// "ACTIVE" - The connection has been created successfully. "FAILED" - The
	// connection is not functional since some resources on the connection fail to
	// be created. "CREATING" - The connection is being created. "DELETING" - The
	// connection is being deleted. "CREATE_REPAIRING" - The connection is being
	// repaired to complete creation. "DELETE_REPAIRING" - The connection is being
	// repaired to complete deletion.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConsumerNetwork") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsumerNetwork") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PscAutoConnectionConfig: Configuration for setting up PSC service automation. Consumer projects in the configs will be allowlisted automatically for the instance.

func (PscAutoConnectionConfig) MarshalJSON ¶
added in v0.224.0
func (s PscAutoConnectionConfig) MarshalJSON() ([]byte, error)
type PscConfig ¶
added in v0.151.0
type PscConfig struct {
	// PscEnabled: Optional. Create an instance that allows connections from
	// Private Service Connect endpoints to the instance.
	PscEnabled bool `json:"pscEnabled,omitempty"`
	// ServiceOwnedProjectNumber: Output only. The project number that needs to be
	// allowlisted on the network attachment to enable outbound connectivity.
	ServiceOwnedProjectNumber int64 `json:"serviceOwnedProjectNumber,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "PscEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PscEnabled") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PscConfig: PscConfig contains PSC related configuration at a cluster level.

func (PscConfig) MarshalJSON ¶
added in v0.151.0
func (s PscConfig) MarshalJSON() ([]byte, error)
type PscInstanceConfig ¶
added in v0.155.0
type PscInstanceConfig struct {
	// AllowedConsumerProjects: Optional. List of consumer projects that are
	// allowed to create PSC endpoints to service-attachments to this instance.
	AllowedConsumerProjects []string `json:"allowedConsumerProjects,omitempty"`
	// PscAutoConnections: Optional. Configurations for setting up PSC service
	// automation.
	PscAutoConnections []*PscAutoConnectionConfig `json:"pscAutoConnections,omitempty"`
	// PscDnsName: Output only. The DNS name of the instance for PSC connectivity.
	// Name convention: ...alloydb-psc.goog
	PscDnsName string `json:"pscDnsName,omitempty"`
	// PscInterfaceConfigs: Optional. Configurations for setting up PSC interfaces
	// attached to the instance which are used for outbound connectivity. Only
	// primary instances can have PSC interface attached. Currently we only support
	// 0 or 1 PSC interface.
	PscInterfaceConfigs []*PscInterfaceConfig `json:"pscInterfaceConfigs,omitempty"`
	// ServiceAttachmentLink: Output only. The service attachment created when
	// Private Service Connect (PSC) is enabled for the instance. The name of the
	// resource will be in the format of `projects//regions//serviceAttachments/`
	ServiceAttachmentLink string `json:"serviceAttachmentLink,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowedConsumerProjects") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedConsumerProjects") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PscInstanceConfig: PscInstanceConfig contains PSC related configuration at an instance level.

func (PscInstanceConfig) MarshalJSON ¶
added in v0.155.0
func (s PscInstanceConfig) MarshalJSON() ([]byte, error)
type PscInterfaceConfig ¶
added in v0.155.0
type PscInterfaceConfig struct {
	// NetworkAttachmentResource: The network attachment resource created in the
	// consumer network to which the PSC interface will be linked. This is of the
	// format:
	// "projects/${CONSUMER_PROJECT}/regions/${REGION}/networkAttachments/${NETWORK_
	// ATTACHMENT_NAME}". The network attachment must be in the same region as the
	// instance.
	NetworkAttachmentResource string `json:"networkAttachmentResource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NetworkAttachmentResource")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NetworkAttachmentResource") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PscInterfaceConfig: Configuration for setting up a PSC interface to enable outbound connectivity.

func (PscInterfaceConfig) MarshalJSON ¶
added in v0.155.0
func (s PscInterfaceConfig) MarshalJSON() ([]byte, error)
type QuantityBasedExpiry ¶
type QuantityBasedExpiry struct {
	// RetentionCount: Output only. The backup's position among its backups with
	// the same source cluster and type, by descending chronological order create
	// time(i.e. newest first).
	RetentionCount int64 `json:"retentionCount,omitempty"`
	// TotalRetentionCount: Output only. The length of the quantity-based queue,
	// specified by the backup's retention policy.
	TotalRetentionCount int64 `json:"totalRetentionCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RetentionCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RetentionCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

QuantityBasedExpiry: A backup's position in a quantity-based retention queue, of backups with the same source cluster and type, with length, retention, specified by the backup's retention policy. Once the position is greater than the retention, the backup is eligible to be garbage collected. Example: 5 backups from the same source cluster and type with a quantity-based retention of 3 and denoted by backup_id (position, retention). Safe: backup_5 (1, 3), backup_4, (2, 3), backup_3 (3, 3). Awaiting garbage collection: backup_2 (4, 3), backup_1 (5, 3)

func (QuantityBasedExpiry) MarshalJSON ¶
func (s QuantityBasedExpiry) MarshalJSON() ([]byte, error)
type QuantityBasedRetention ¶
type QuantityBasedRetention struct {
	// Count: The number of backups to retain.
	Count int64 `json:"count,omitempty"`
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

QuantityBasedRetention: A quantity based policy specifies that a certain number of the most recent successful backups should be retained.

func (QuantityBasedRetention) MarshalJSON ¶
func (s QuantityBasedRetention) MarshalJSON() ([]byte, error)
type QueryInsightsInstanceConfig ¶
type QueryInsightsInstanceConfig struct {
	// QueryPlansPerMinute: Number of query execution plans captured by Insights
	// per minute for all queries combined. The default value is 5. Any integer
	// between 0 and 20 is considered valid.
	QueryPlansPerMinute int64 `json:"queryPlansPerMinute,omitempty"`
	// QueryStringLength: Query string length. The default value is 1024. Any
	// integer between 256 and 4500 is considered valid.
	QueryStringLength int64 `json:"queryStringLength,omitempty"`
	// RecordApplicationTags: Record application tags for an instance. This flag is
	// turned "on" by default.
	RecordApplicationTags bool `json:"recordApplicationTags,omitempty"`
	// RecordClientAddress: Record client address for an instance. Client address
	// is PII information. This flag is turned "on" by default.
	RecordClientAddress bool `json:"recordClientAddress,omitempty"`
	// ForceSendFields is a list of field names (e.g. "QueryPlansPerMinute") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "QueryPlansPerMinute") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

QueryInsightsInstanceConfig: QueryInsights Instance specific configuration.

func (QueryInsightsInstanceConfig) MarshalJSON ¶
func (s QueryInsightsInstanceConfig) MarshalJSON() ([]byte, error)
type ReadPoolConfig ¶
type ReadPoolConfig struct {
	// AutoScalingConfig: Autoscaling configuration for the read pool instance. If
	// not set, the read pool instance will not be autoscaled.
	AutoScalingConfig *AutoScalingConfig `json:"autoScalingConfig,omitempty"`
	// NodeCount: Read capacity, i.e. number of nodes in a read pool instance.
	NodeCount int64 `json:"nodeCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoScalingConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoScalingConfig") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReadPoolConfig: Configuration for a read pool instance.

func (ReadPoolConfig) MarshalJSON ¶
func (s ReadPoolConfig) MarshalJSON() ([]byte, error)
type ReadPoolInstancesUpgradeStageStatus ¶
added in v0.224.0
type ReadPoolInstancesUpgradeStageStatus struct {
	// UpgradeStats: Read pool instances upgrade statistics.
	UpgradeStats *Stats `json:"upgradeStats,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UpgradeStats") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UpgradeStats") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReadPoolInstancesUpgradeStageStatus: Read pool instances upgrade specific status.

func (ReadPoolInstancesUpgradeStageStatus) MarshalJSON ¶
added in v0.224.0
func (s ReadPoolInstancesUpgradeStageStatus) MarshalJSON() ([]byte, error)
type RestartInstanceRequest ¶
type RestartInstanceRequest struct {
	// NodeIds: Optional. Full name of the nodes as obtained from
	// INSTANCE_VIEW_FULL to restart upon. Applicable only to read instances.
	NodeIds []string `json:"nodeIds,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NodeIds") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NodeIds") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (RestartInstanceRequest) MarshalJSON ¶
func (s RestartInstanceRequest) MarshalJSON() ([]byte, error)
type RestoreClusterRequest ¶
type RestoreClusterRequest struct {
	// BackupSource: Backup source.
	BackupSource *BackupSource `json:"backupSource,omitempty"`
	// BackupdrBackupSource: BackupDR backup source.
	BackupdrBackupSource *BackupDrBackupSource `json:"backupdrBackupSource,omitempty"`
	// BackupdrPitrSource: BackupDR source used for point in time recovery.
	BackupdrPitrSource *BackupDrPitrSource `json:"backupdrPitrSource,omitempty"`
	// Cluster: Required. The resource being created
	Cluster *Cluster `json:"cluster,omitempty"`
	// ClusterId: Required. ID of the requesting object.
	ClusterId string `json:"clusterId,omitempty"`
	// ContinuousBackupSource: ContinuousBackup source. Continuous backup needs to
	// be enabled in the source cluster for this operation to succeed.
	ContinuousBackupSource *ContinuousBackupSource `json:"continuousBackupSource,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreClusterRequest: Message for restoring a Cluster from a backup or another cluster at a given point in time. NEXT_ID: 11

func (RestoreClusterRequest) MarshalJSON ¶
func (s RestoreClusterRequest) MarshalJSON() ([]byte, error)
type RestoreFromCloudSQLRequest ¶
added in v0.212.0
type RestoreFromCloudSQLRequest struct {
	// CloudsqlBackupRunSource: Cluster created from CloudSQL backup run.
	CloudsqlBackupRunSource *CloudSQLBackupRunSource `json:"cloudsqlBackupRunSource,omitempty"`
	// Cluster: Required. The resource being created
	Cluster *Cluster `json:"cluster,omitempty"`
	// ClusterId: Required. ID of the requesting object.
	ClusterId string `json:"clusterId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CloudsqlBackupRunSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudsqlBackupRunSource") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestoreFromCloudSQLRequest: Message for registering Restoring from CloudSQL resource.

func (RestoreFromCloudSQLRequest) MarshalJSON ¶
added in v0.212.0
func (s RestoreFromCloudSQLRequest) MarshalJSON() ([]byte, error)
type Schedule ¶
added in v0.252.0
type Schedule struct {
	// CronExpression: Cron expression for the triggering the schedule. See
	// https://cloud.google.com/compute/docs/autoscaler/scaling-schedules#cron_expressions
	// for the syntax.
	CronExpression string `json:"cronExpression,omitempty"`
	// Description: Description of the schedule.
	Description string `json:"description,omitempty"`
	// Disabled: If true, the schedule is disabled.
	Disabled bool `json:"disabled,omitempty"`
	// DurationSec: Duration of the schedule.
	DurationSec int64 `json:"durationSec,omitempty,string"`
	// MinNodeCount: Minimum number of nodes in while the schedule is active.
	MinNodeCount int64 `json:"minNodeCount,omitempty,string"`
	// Name: Name of the schedule.
	Name string `json:"name,omitempty"`
	// TimeZone: The location-based IANA time zone for interpreting the schedule's
	// start time. If no time zone is provided, UTC is used by default.
	TimeZone string `json:"timeZone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CronExpression") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CronExpression") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Schedule: A schedule for the autoscaler.

func (Schedule) MarshalJSON ¶
added in v0.252.0
func (s Schedule) MarshalJSON() ([]byte, error)
type SecondaryConfig ¶
type SecondaryConfig struct {
	// PrimaryClusterName: The name of the primary cluster name with the format: *
	// projects/{project}/locations/{region}/clusters/{cluster_id}
	PrimaryClusterName string `json:"primaryClusterName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrimaryClusterName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrimaryClusterName") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SecondaryConfig: Configuration information for the secondary cluster. This should be set if and only if the cluster is of type SECONDARY.

func (SecondaryConfig) MarshalJSON ¶
func (s SecondaryConfig) MarshalJSON() ([]byte, error)
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

type SqlExportOptions ¶
added in v0.209.0
type SqlExportOptions struct {
	// CleanTargetObjects: Optional. If true, output commands to DROP all the
	// dumped database objects prior to outputting the commands for creating them.
	CleanTargetObjects bool `json:"cleanTargetObjects,omitempty"`
	// IfExistTargetObjects: Optional. If true, use DROP ... IF EXISTS commands to
	// check for the object's existence before dropping it in clean_target_objects
	// mode.
	IfExistTargetObjects bool `json:"ifExistTargetObjects,omitempty"`
	// SchemaOnly: Optional. If true, only export the schema.
	SchemaOnly bool `json:"schemaOnly,omitempty"`
	// Tables: Optional. Tables to export from.
	Tables []string `json:"tables,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CleanTargetObjects") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CleanTargetObjects") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SqlExportOptions: Options for exporting data in SQL format.

func (SqlExportOptions) MarshalJSON ¶
added in v0.209.0
func (s SqlExportOptions) MarshalJSON() ([]byte, error)
type SqlImportOptions ¶
added in v0.222.0
type SqlImportOptions struct {
}

SqlImportOptions: Options for importing data in SQL format.

type SslConfig ¶
type SslConfig struct {
	// CaSource: Optional. Certificate Authority (CA) source. Only
	// CA_SOURCE_MANAGED is supported currently, and is the default value.
	//
	// Possible values:
	//   "CA_SOURCE_UNSPECIFIED" - Certificate Authority (CA) source not specified.
	// Defaults to CA_SOURCE_MANAGED.
	//   "CA_SOURCE_MANAGED" - Certificate Authority (CA) managed by the AlloyDB
	// Cluster.
	CaSource string `json:"caSource,omitempty"`
	// SslMode: Optional. SSL mode. Specifies client-server SSL/TLS connection
	// behavior.
	//
	// Possible values:
	//   "SSL_MODE_UNSPECIFIED" - SSL mode is not specified. Defaults to
	// ENCRYPTED_ONLY.
	//   "SSL_MODE_ALLOW" - SSL connections are optional. CA verification not
	// enforced.
	//   "SSL_MODE_REQUIRE" - SSL connections are required. CA verification not
	// enforced. Clients may use locally self-signed certificates (default psql
	// client behavior).
	//   "SSL_MODE_VERIFY_CA" - SSL connections are required. CA verification
	// enforced. Clients must have certificates signed by a Cluster CA, for
	// example, using GenerateClientCertificate.
	//   "ALLOW_UNENCRYPTED_AND_ENCRYPTED" - SSL connections are optional. CA
	// verification not enforced.
	//   "ENCRYPTED_ONLY" - SSL connections are required. CA verification not
	// enforced.
	SslMode string `json:"sslMode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CaSource") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CaSource") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SslConfig: SSL configuration.

func (SslConfig) MarshalJSON ¶
func (s SslConfig) MarshalJSON() ([]byte, error)
type StageInfo ¶
added in v0.193.0
type StageInfo struct {
	// LogsUrl: logs_url is the URL for the logs associated with a stage if that
	// stage has logs. Right now, only three stages have logs: ALLOYDB_PRECHECK,
	// PG_UPGRADE_CHECK, PRIMARY_INSTANCE_UPGRADE.
	LogsUrl string `json:"logsUrl,omitempty"`
	// Stage: The stage.
	//
	// Possible values:
	//   "STAGE_UNSPECIFIED" - Unspecified stage.
	//   "ALLOYDB_PRECHECK" - Pre-upgrade custom checks, not covered by pg_upgrade.
	//   "PG_UPGRADE_CHECK" - Pre-upgrade pg_upgrade checks.
	//   "PREPARE_FOR_UPGRADE" - Clone the original cluster.
	//   "PRIMARY_INSTANCE_UPGRADE" - Upgrade the primary instance(downtime).
	//   "READ_POOL_INSTANCES_UPGRADE" - This stage is read pool upgrade.
	//   "ROLLBACK" - Rollback in case of critical failures.
	//   "CLEANUP" - Cleanup.
	Stage string `json:"stage,omitempty"`
	// Status: Status of the stage.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LogsUrl") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LogsUrl") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StageInfo: Stage information for different stages in the upgrade process.

func (StageInfo) MarshalJSON ¶
added in v0.193.0
func (s StageInfo) MarshalJSON() ([]byte, error)
type StageStatus ¶
added in v0.224.0
type StageStatus struct {
	// ReadPoolInstancesUpgrade: Read pool instances upgrade metadata.
	ReadPoolInstancesUpgrade *ReadPoolInstancesUpgradeStageStatus `json:"readPoolInstancesUpgrade,omitempty"`
	// Stage: Upgrade stage.
	//
	// Possible values:
	//   "STAGE_UNSPECIFIED" - Unspecified stage.
	//   "ALLOYDB_PRECHECK" - Pre-upgrade custom checks, not covered by pg_upgrade.
	//   "PG_UPGRADE_CHECK" - Pre-upgrade pg_upgrade checks.
	//   "PREPARE_FOR_UPGRADE" - Clone the original cluster.
	//   "PRIMARY_INSTANCE_UPGRADE" - Upgrade the primary instance(downtime).
	//   "READ_POOL_INSTANCES_UPGRADE" - This stage is read pool upgrade.
	//   "ROLLBACK" - Rollback in case of critical failures.
	//   "CLEANUP" - Cleanup.
	Stage string `json:"stage,omitempty"`
	// State: State of this stage.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReadPoolInstancesUpgrade")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReadPoolInstancesUpgrade") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StageStatus: Status of an upgrade stage.

func (StageStatus) MarshalJSON ¶
added in v0.224.0
func (s StageStatus) MarshalJSON() ([]byte, error)
type Stats ¶
added in v0.224.0
type Stats struct {
	// Failed: Number of read pool instances which failed to upgrade.
	Failed int64 `json:"failed,omitempty"`
	// NotStarted: Number of read pool instances for which upgrade has not started.
	NotStarted int64 `json:"notStarted,omitempty"`
	// Ongoing: Number of read pool instances undergoing upgrade.
	Ongoing int64 `json:"ongoing,omitempty"`
	// Success: Number of read pool instances successfully upgraded.
	Success int64 `json:"success,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Failed") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Failed") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Stats: Upgrade stats for read pool instances.

func (Stats) MarshalJSON ¶
added in v0.224.0
func (s Stats) MarshalJSON() ([]byte, error)
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
type StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration ¶
type StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration struct {
	// AutomaticFailoverRoutingConfigured: Checks for existence of (multi-cluster)
	// routing configuration that allows automatic failover to a different
	// zone/region in case of an outage. Applicable to Bigtable resources.
	AutomaticFailoverRoutingConfigured bool `json:"automaticFailoverRoutingConfigured,omitempty"`
	// AvailabilityType: Availability type. Potential values: * `ZONAL`: The
	// instance serves data from only one zone. Outages in that zone affect data
	// accessibility. * `REGIONAL`: The instance can serve data from more than one
	// zone in a region (it is highly available).
	//
	// Possible values:
	//   "AVAILABILITY_TYPE_UNSPECIFIED"
	//   "ZONAL" - Zonal available instance.
	//   "REGIONAL" - Regional available instance.
	//   "MULTI_REGIONAL" - Multi regional instance
	//   "AVAILABILITY_TYPE_OTHER" - For rest of the other category
	AvailabilityType string `json:"availabilityType,omitempty"`
	// CrossRegionReplicaConfigured: Checks for resources that are configured to
	// have redundancy, and ongoing replication across regions
	CrossRegionReplicaConfigured bool `json:"crossRegionReplicaConfigured,omitempty"`
	ExternalReplicaConfigured    bool `json:"externalReplicaConfigured,omitempty"`
	PromotableReplicaConfigured  bool `json:"promotableReplicaConfigured,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AutomaticFailoverRoutingConfigured") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AutomaticFailoverRoutingConfigured") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration: Configuration for availability of database instance

func (StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupConfiguration ¶
type StorageDatabasecenterPartnerapiV1mainBackupConfiguration struct {
	// AutomatedBackupEnabled: Whether customer visible automated backups are
	// enabled on the instance.
	AutomatedBackupEnabled bool `json:"automatedBackupEnabled,omitempty"`
	// BackupRetentionSettings: Backup retention settings.
	BackupRetentionSettings *StorageDatabasecenterPartnerapiV1mainRetentionSettings `json:"backupRetentionSettings,omitempty"`
	// PointInTimeRecoveryEnabled: Whether point-in-time recovery is enabled. This
	// is optional field, if the database service does not have this feature or
	// metadata is not available in control plane, this can be omitted.
	PointInTimeRecoveryEnabled bool `json:"pointInTimeRecoveryEnabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutomatedBackupEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutomatedBackupEnabled") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainBackupConfiguration: Configuration for automatic backups

func (StorageDatabasecenterPartnerapiV1mainBackupConfiguration) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainBackupConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration ¶
added in v0.244.0
type StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration struct {
	// BackupdrManaged: Indicates if the resource is managed by BackupDR.
	BackupdrManaged bool `json:"backupdrManaged,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupdrManaged") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupdrManaged") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration: BackupDRConfiguration to capture the backup and disaster recovery details of database resource.

func (StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration) MarshalJSON ¶
added in v0.244.0
func (s StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupDRMetadata ¶
added in v0.247.0
type StorageDatabasecenterPartnerapiV1mainBackupDRMetadata struct {
	// BackupConfiguration: Backup configuration for this instance.
	BackupConfiguration *StorageDatabasecenterPartnerapiV1mainBackupConfiguration `json:"backupConfiguration,omitempty"`
	// BackupRun: Latest backup run information for this instance.
	BackupRun *StorageDatabasecenterPartnerapiV1mainBackupRun `json:"backupRun,omitempty"`
	// BackupdrConfiguration: BackupDR configuration for this instance.
	BackupdrConfiguration *StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration `json:"backupdrConfiguration,omitempty"`
	// FullResourceName: Required. Full resource name of this instance.
	FullResourceName string `json:"fullResourceName,omitempty"`
	// LastRefreshTime: Required. Last time backup configuration was refreshed.
	LastRefreshTime string `json:"lastRefreshTime,omitempty"`
	// ResourceId: Required. Database resource id.
	ResourceId *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"resourceId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupConfiguration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupConfiguration") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainBackupDRMetadata: BackupDRMetadata contains information about the backup and disaster recovery metadata of a database resource.

func (StorageDatabasecenterPartnerapiV1mainBackupDRMetadata) MarshalJSON ¶
added in v0.247.0
func (s StorageDatabasecenterPartnerapiV1mainBackupDRMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainBackupRun ¶
type StorageDatabasecenterPartnerapiV1mainBackupRun struct {
	// EndTime: The time the backup operation completed. REQUIRED
	EndTime string `json:"endTime,omitempty"`
	// Error: Information about why the backup operation failed. This is only
	// present if the run has the FAILED status. OPTIONAL
	Error *StorageDatabasecenterPartnerapiV1mainOperationError `json:"error,omitempty"`
	// StartTime: The time the backup operation started. REQUIRED
	StartTime string `json:"startTime,omitempty"`
	// Status: The status of this run. REQUIRED
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED"
	//   "SUCCESSFUL" - The backup was successful.
	//   "FAILED" - The backup was unsuccessful.
	Status string `json:"status,omitempty"`
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

StorageDatabasecenterPartnerapiV1mainBackupRun: A backup run.

func (StorageDatabasecenterPartnerapiV1mainBackupRun) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainBackupRun) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainCompliance ¶
type StorageDatabasecenterPartnerapiV1mainCompliance struct {
	// Standard: Industry-wide compliance standards or benchmarks, such as CIS,
	// PCI, and OWASP.
	Standard string `json:"standard,omitempty"`
	// Version: Version of the standard or benchmark, for example, 1.1
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Standard") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Standard") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainCompliance: Contains compliance information about a security standard indicating unmet recommendations.

func (StorageDatabasecenterPartnerapiV1mainCompliance) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainCompliance) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData ¶
added in v0.244.0
type StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData struct {
	// FullResourceName: Required. Full Resource name of the source resource.
	FullResourceName string `json:"fullResourceName,omitempty"`
	// LastRefreshTime: Required. Last time signal was refreshed
	LastRefreshTime string `json:"lastRefreshTime,omitempty"`
	// ResourceId: Database resource id.
	ResourceId *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"resourceId,omitempty"`
	// SignalBoolValue: Signal data for boolean signals.
	SignalBoolValue bool `json:"signalBoolValue,omitempty"`
	// SignalType: Required. Signal type of the signal
	//
	// Possible values:
	//   "SIGNAL_TYPE_UNSPECIFIED" - Unspecified signal type.
	//   "SIGNAL_TYPE_OUTDATED_MINOR_VERSION" - Outdated Minor Version
	//   "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED" - Represents database auditing is
	// disabled.
	//   "SIGNAL_TYPE_NO_ROOT_PASSWORD" - Represents if a database has a password
	// configured for the root account or not.
	//   "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS" - Represents if a resource is
	// exposed to public access.
	//   "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS" - Represents if a resources requires
	// all incoming connections to use SSL or not.
	//   "SIGNAL_TYPE_EXTENDED_SUPPORT" - Represents if a resource version is in
	// extended support.
	//   "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY" - Represents if a resource has no
	// automated backup policy.
	SignalType string `json:"signalType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FullResourceName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FullResourceName") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData: Config based signal data. This is used to send signals to Condor which are based on the DB level configurations. These will be used to send signals for self managed databases.

func (StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData) MarshalJSON ¶
added in v0.244.0
func (s StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainCustomMetadataData ¶
added in v0.156.0
type StorageDatabasecenterPartnerapiV1mainCustomMetadataData struct {
	// InternalResourceMetadata: Metadata for individual internal resources in an
	// instance. e.g. spanner instance can have multiple databases with unique
	// configuration.
	InternalResourceMetadata []*StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata `json:"internalResourceMetadata,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InternalResourceMetadata")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InternalResourceMetadata") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainCustomMetadataData: Any custom metadata associated with the resource. e.g. A spanner instance can have multiple databases with its own unique metadata. Information for these individual databases can be captured in custom metadata data

func (StorageDatabasecenterPartnerapiV1mainCustomMetadataData) MarshalJSON ¶
added in v0.156.0
func (s StorageDatabasecenterPartnerapiV1mainCustomMetadataData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed ¶
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed struct {
	// BackupdrMetadata: BackupDR metadata is used to ingest metadata from
	// BackupDR.
	BackupdrMetadata *StorageDatabasecenterPartnerapiV1mainBackupDRMetadata `json:"backupdrMetadata,omitempty"`
	// ConfigBasedSignalData: Config based signal data is used to ingest signals
	// that are generated based on the configuration of the database resource.
	ConfigBasedSignalData *StorageDatabasecenterPartnerapiV1mainConfigBasedSignalData `json:"configBasedSignalData,omitempty"`
	// DatabaseResourceSignalData: Database resource signal data is used to ingest
	// signals from database resource signal feeds.
	DatabaseResourceSignalData *StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData `json:"databaseResourceSignalData,omitempty"`
	// FeedTimestamp: Required. Timestamp when feed is generated.
	FeedTimestamp string `json:"feedTimestamp,omitempty"`
	// FeedType: Required. Type feed to be ingested into condor
	//
	// Possible values:
	//   "FEEDTYPE_UNSPECIFIED"
	//   "RESOURCE_METADATA" - Database resource metadata feed from control plane
	//   "OBSERVABILITY_DATA" - Database resource monitoring data
	//   "SECURITY_FINDING_DATA" - Database resource security health signal data
	//   "RECOMMENDATION_SIGNAL_DATA" - Database resource recommendation signal
	// data
	//   "CONFIG_BASED_SIGNAL_DATA" - Database config based signal data
	//   "BACKUPDR_METADATA" - Database resource metadata from BackupDR
	//   "DATABASE_RESOURCE_SIGNAL_DATA" - Database resource signal data
	FeedType                 string                                                                         `json:"feedType,omitempty"`
	ObservabilityMetricData  *StorageDatabasecenterPartnerapiV1mainObservabilityMetricData                  `json:"observabilityMetricData,omitempty"`
	RecommendationSignalData *StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData `json:"recommendationSignalData,omitempty"`
	ResourceHealthSignalData *StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData         `json:"resourceHealthSignalData,omitempty"`
	// ResourceId: Primary key associated with the Resource. resource_id is
	// available in individual feed level as well.
	ResourceId       *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId       `json:"resourceId,omitempty"`
	ResourceMetadata *StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata `json:"resourceMetadata,omitempty"`
	// SkipIngestion: Optional. If true, the feed won't be ingested by DB Center.
	// This indicates that the feed is intentionally skipped. For example, BackupDR
	// feeds are only needed for resources integrated with DB Center (e.g.,
	// CloudSQL, AlloyDB). Feeds for non-integrated resources (e.g., Compute
	// Engine, Persistent Disk) can be skipped.
	SkipIngestion bool `json:"skipIngestion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupdrMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupdrMetadata") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed: DatabaseResourceFeed is the top level proto to be used to ingest different database resource level events into Condor platform. Next ID: 13

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData ¶
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData struct {
	// AdditionalMetadata: Any other additional metadata
	AdditionalMetadata googleapi.RawMessage `json:"additionalMetadata,omitempty"`
	// Compliance: Industry standards associated with this signal; if this signal
	// is an issue, that could be a violation of the associated industry
	// standard(s). For example, AUTO_BACKUP_DISABLED signal is associated with CIS
	// GCP 1.1, CIS GCP 1.2, CIS GCP 1.3, NIST 800-53 and ISO-27001 compliance
	// standards. If a database resource does not have automated backup enable, it
	// will violate these following industry standards.
	Compliance []*StorageDatabasecenterPartnerapiV1mainCompliance `json:"compliance,omitempty"`
	// Description: Description associated with signal
	Description string `json:"description,omitempty"`
	// EventTime: Required. The last time at which the event described by this
	// signal took place
	EventTime string `json:"eventTime,omitempty"`
	// ExternalUri: The external-uri of the signal, using which more information
	// about this signal can be obtained. In GCP, this will take user to SCC page
	// to get more details about signals.
	ExternalUri string `json:"externalUri,omitempty"`
	// Location: This is used to identify the location of the resource. Example:
	// "us-central1"
	Location string `json:"location,omitempty"`
	// Name: Required. The name of the signal, ex: PUBLIC_SQL_INSTANCE,
	// SQL_LOG_ERROR_VERBOSITY etc.
	Name string `json:"name,omitempty"`
	// Provider: Cloud provider name. Ex: GCP/AWS/Azure/OnPrem/SelfManaged
	//
	// Possible values:
	//   "PROVIDER_UNSPECIFIED"
	//   "GCP" - Google cloud platform provider
	//   "AWS" - Amazon web service
	//   "AZURE" - Azure web service
	//   "ONPREM" - On-prem database resources.
	//   "SELFMANAGED" - Self-managed database provider. These are resources on a
	// cloud platform, e.g., database resource installed in a GCE VM, but not a
	// managed database service.
	//   "PROVIDER_OTHER" - For the rest of the other categories. Other refers to
	// the rest of other database service providers, this could be smaller cloud
	// provider. This needs to be provided when the provider is known, but it is
	// not present in the existing set of enum values.
	Provider string `json:"provider,omitempty"`
	// ResourceContainer: Closest parent container of this resource. In GCP,
	// 'container' refers to a Cloud Resource Manager project. It must be resource
	// name of a Cloud Resource Manager project with the format of "provider//",
	// such as "projects/123". For GCP provided resources, number should be project
	// number.
	ResourceContainer string `json:"resourceContainer,omitempty"`
	// ResourceName: Required. Database resource name associated with the signal.
	// Resource name to follow CAIS resource_name format as noted here
	// go/condor-common-datamodel
	ResourceName string `json:"resourceName,omitempty"`
	// SignalClass: Required. The class of the signal, such as if it's a THREAT or
	// VULNERABILITY.
	//
	// Possible values:
	//   "CLASS_UNSPECIFIED" - Unspecified signal class.
	//   "THREAT" - Describes unwanted or malicious activity.
	//   "VULNERABILITY" - Describes a potential weakness in software that
	// increases risk to Confidentiality & Integrity & Availability.
	//   "MISCONFIGURATION" - Describes a potential weakness in cloud
	// resource/asset configuration that increases risk.
	//   "OBSERVATION" - Describes a security observation that is for informational
	// purposes.
	//   "ERROR" - Describes an error that prevents some SCC functionality.
	SignalClass string `json:"signalClass,omitempty"`
	// SignalId: Required. Unique identifier for the signal. This is an unique id
	// which would be mainatined by partner to identify a signal.
	SignalId string `json:"signalId,omitempty"`
	// SignalSeverity: The severity of the signal, such as if it's a HIGH or LOW
	// severity.
	//
	// Possible values:
	//   "SIGNAL_SEVERITY_UNSPECIFIED" - This value is used for findings when a
	// source doesn't write a severity value.
	//   "CRITICAL" - A critical vulnerability is easily discoverable by an
	// external actor, exploitable.
	//   "HIGH" - A high risk vulnerability can be easily discovered and exploited
	// in combination with other vulnerabilities.
	//   "MEDIUM" - A medium risk vulnerability could be used by an actor to gain
	// access to resources or privileges that enable them to eventually gain access
	// and the ability to execute arbitrary code or exfiltrate data.
	//   "LOW" - A low risk vulnerability hampers a security organization's ability
	// to detect vulnerabilities or active threats in their deployment.
	SignalSeverity string `json:"signalSeverity,omitempty"`
	// SignalType: Required. Type of signal, for example,
	// `AVAILABLE_IN_MULTIPLE_ZONES`, `LOGGING_MOST_ERRORS`, etc.
	//
	// Possible values:
	//   "SIGNAL_TYPE_UNSPECIFIED" - Unspecified.
	//   "SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER" - Represents if a
	// resource is protected by automatic failover. Checks for resources that are
	// configured to have redundancy within a region that enables automatic
	// failover.
	//   "SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS" - Represents if a group
	// is replicating across regions. Checks for resources that are configured to
	// have redundancy, and ongoing replication, across regions.
	//   "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES" - Represents if the resource
	// is available in multiple zones or not.
	//   "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS" - Represents if a resource
	// is available in multiple regions.
	//   "SIGNAL_TYPE_NO_PROMOTABLE_REPLICA" - Represents if a resource has a
	// promotable replica.
	//   "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY" - Represents if a resource has an
	// automated backup policy.
	//   "SIGNAL_TYPE_SHORT_BACKUP_RETENTION" - Represents if a resources has a
	// short backup retention period.
	//   "SIGNAL_TYPE_LAST_BACKUP_FAILED" - Represents if the last backup of a
	// resource failed.
	//   "SIGNAL_TYPE_LAST_BACKUP_OLD" - Represents if the last backup of a
	// resource is older than some threshold value.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0" - Represents if a resource
	// violates CIS GCP Foundation 2.0.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3" - Represents if a resource
	// violates CIS GCP Foundation 1.3.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2" - Represents if a resource
	// violates CIS GCP Foundation 1.2.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1" - Represents if a resource
	// violates CIS GCP Foundation 1.1.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0" - Represents if a resource
	// violates CIS GCP Foundation 1.0.
	//   "SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0" - Represents if a resource
	// violates CIS Controls 8.0.
	//   "SIGNAL_TYPE_VIOLATES_NIST_800_53" - Represents if a resource violates
	// NIST 800-53.
	//   "SIGNAL_TYPE_VIOLATES_NIST_800_53_R5" - Represents if a resource violates
	// NIST 800-53 R5.
	//   "SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0" - Represents if a
	// resource violates NIST Cybersecurity Framework 1.0.
	//   "SIGNAL_TYPE_VIOLATES_ISO_27001" - Represents if a resource violates
	// ISO-27001.
	//   "SIGNAL_TYPE_VIOLATES_ISO_27001_V2022" - Represents if a resource violates
	// ISO 27001 2022.
	//   "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1" - Represents if a resource violates
	// PCI-DSS v3.2.1.
	//   "SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0" - Represents if a resource violates
	// PCI-DSS v4.0.
	//   "SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4" - Represents if a resource
	// violates Cloud Controls Matrix v4.0.
	//   "SIGNAL_TYPE_VIOLATES_HIPAA" - Represents if a resource violates HIPAA.
	//   "SIGNAL_TYPE_VIOLATES_SOC2_V2017" - Represents if a resource violates SOC2
	// v2017.
	//   "SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING" - Represents if
	// log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED" - Represents if the log_duration
	// database flag for a Cloud SQL for PostgreSQL instance is not set to on.
	//   "SIGNAL_TYPE_VERBOSE_ERROR_LOGGING" - Represents if the
	// log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is
	// not set to default or stricter (default or terse).
	//   "SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED" - Represents if the
	// log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_LOGGING_MOST_ERRORS" - Represents if the
	// log_min_error_statement database flag for a Cloud SQL for PostgreSQL
	// instance is not set appropriately.
	//   "SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS" - Represents if the
	// log_min_error_statement database flag for a Cloud SQL for PostgreSQL
	// instance does not have an appropriate severity level.
	//   "SIGNAL_TYPE_MINIMAL_ERROR_LOGGING" - Represents if the log_min_messages
	// database flag for a Cloud SQL for PostgreSQL instance is not set to warning
	// or another recommended value.
	//   "SIGNAL_TYPE_QUERY_STATISTICS_LOGGED" - Represents if the databaseFlags
	// property of instance metadata for the log_executor_status field is set to
	// on.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME" - Represents if the
	// log_hostname database flag for a Cloud SQL for PostgreSQL instance is not
	// set to off.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS" - Represents if the
	// log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS" - Represents if the
	// log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS" - Represents if the
	// log_statement database flag for a Cloud SQL for PostgreSQL instance is not
	// set to DDL (all data definition statements).
	//   "SIGNAL_TYPE_LOGGING_QUERY_STATISTICS" - Represents if the
	// log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES" - Represents if the
	// log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not
	// set to "0". (NOTE: 0 = ON)
	//   "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED" - Represents if the user
	// connections database flag for a Cloud SQL for SQL Server instance is
	// configured.
	//   "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED" - Represents if the user options
	// database flag for Cloud SQL SQL Server instance is configured or not.
	//   "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS" - Represents if a resource is
	// exposed to public access.
	//   "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS" - Represents if a resources requires
	// all incoming connections to use SSL or not.
	//   "SIGNAL_TYPE_NO_ROOT_PASSWORD" - Represents if a Cloud SQL database has a
	// password configured for the root account or not.
	//   "SIGNAL_TYPE_WEAK_ROOT_PASSWORD" - Represents if a Cloud SQL database has
	// a weak password configured for the root account.
	//   "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED" - Represents if a SQL
	// database instance is not encrypted with customer-managed encryption keys
	// (CMEK).
	//   "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED" - Represents if The
	// contained database authentication database flag for a Cloud SQL for SQL
	// Server instance is not set to off.
	//   "SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING" - Represents if the
	// cross_db_ownership_chaining database flag for a Cloud SQL for SQL Server
	// instance is not set to off.
	//   "SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS" - Represents if he external
	// scripts enabled database flag for a Cloud SQL for SQL Server instance is not
	// set to off.
	//   "SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS" - Represents if the local_infile
	// database flag for a Cloud SQL for MySQL instance is not set to off.
	//   "SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED" - Represents if the
	// log_connections database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED" - Represents if the
	// log_disconnections database flag for a Cloud SQL for PostgreSQL instance is
	// not set to on.
	//   "SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO" - Represents if the
	// log_min_duration_statement database flag for a Cloud SQL for PostgreSQL
	// instance is not set to -1.
	//   "SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS" - Represents if the remote access
	// database flag for a Cloud SQL for SQL Server instance is not set to off.
	//   "SIGNAL_TYPE_DATABASE_NAMES_EXPOSED" - Represents if the
	// skip_show_database database flag for a Cloud SQL for MySQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED" - Represents if the 3625
	// (trace flag) database flag for a Cloud SQL for SQL Server instance is not
	// set to on.
	//   "SIGNAL_TYPE_PUBLIC_IP_ENABLED" - Represents if public IP is enabled.
	//   "SIGNAL_TYPE_IDLE" - Represents Idle instance helps to reduce costs.
	//   "SIGNAL_TYPE_OVERPROVISIONED" - Represents instances that are
	// unnecessarily large for given workload.
	//   "SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES" - Represents high number of
	// concurrently opened tables.
	//   "SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES" - Represents high table count close to
	// SLA limit.
	//   "SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION" - Represents high number of
	// unvacuumed transactions
	//   "SIGNAL_TYPE_UNDERPROVISIONED" - Represents need for more CPU and/or
	// memory
	//   "SIGNAL_TYPE_OUT_OF_DISK" - Represents out of disk.
	//   "SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY" - Represents server
	// certificate is near expiry.
	//   "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED" - Represents database auditing is
	// disabled.
	//   "SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS" - Represents not restricted to
	// authorized networks.
	//   "SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP" - Represents violate org
	// policy restrict public ip.
	//   "SIGNAL_TYPE_QUOTA_LIMIT" - Cluster nearing quota limit
	//   "SIGNAL_TYPE_NO_PASSWORD_POLICY" - No password policy set on resources
	//   "SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT" - Performance impact of
	// connections settings
	//   "SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT" - Performance impact of
	// temporary tables settings
	//   "SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT" - Performance impact of
	// transaction logs settings
	//   "SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES" - Performance impact of high
	// joins without indexes
	//   "SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES" - Detects events where a
	// Cloud SQL superuser (postgres for PostgreSQL servers or root for MySQL
	// users) writes to non-system tables.
	//   "SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS" - Detects events where a
	// database user or role has been granted all privileges to a database, or to
	// all tables, procedures, or functions in a schema.
	//   "SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET" - Detects if
	// database instance data exported to a Cloud Storage bucket outside of the
	// organization.
	//   "SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET" - Detects if
	// database instance data exported to a Cloud Storage bucket that is owned by
	// the organization and is publicly accessible.
	//   "SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM" - Detects if a database
	// instance is using a weak password hash algorithm.
	//   "SIGNAL_TYPE_NO_USER_PASSWORD_POLICY" - Detects if a database instance has
	// no user password policy set.
	//   "SIGNAL_TYPE_HOT_NODE" - Detects if a database instance/cluster has a hot
	// node.
	//   "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY" - Detects if a database instance
	// has no point in time recovery enabled.
	//   "SIGNAL_TYPE_RESOURCE_SUSPENDED" - Detects if a database instance/cluster
	// is suspended.
	//   "SIGNAL_TYPE_EXPENSIVE_COMMANDS" - Detects that expensive commands are
	// being run on a database instance impacting overall performance.
	//   "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED" - Indicates that the
	// instance does not have a maintenance policy configured.
	//   "SIGNAL_TYPE_NO_DELETION_PROTECTION" - Deletion Protection Disabled for
	// the resource
	//   "SIGNAL_TYPE_INEFFICIENT_QUERY" - Indicates that the instance has
	// inefficient queries detected.
	//   "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD" - Indicates that the instance has
	// read intensive workload.
	//   "SIGNAL_TYPE_MEMORY_LIMIT" - Indicates that the instance is nearing memory
	// limit.
	//   "SIGNAL_TYPE_MAX_SERVER_MEMORY" - Indicates that the instance's max server
	// memory is configured higher than the recommended value.
	//   "SIGNAL_TYPE_LARGE_ROWS" - Indicates that the database has large rows
	// beyond the recommended limit.
	//   "SIGNAL_TYPE_HIGH_WRITE_PRESSURE" - Heavy write pressure on the database
	// rows.
	//   "SIGNAL_TYPE_HIGH_READ_PRESSURE" - Heavy read pressure on the database
	// rows.
	//   "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED" - Encryption org policy
	// not satisfied.
	//   "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED" - Location org policy not
	// satisfied.
	//   "SIGNAL_TYPE_OUTDATED_MINOR_VERSION" - Outdated DB minor version.
	//   "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED" - Schema not optimized.
	//   "SIGNAL_TYPE_MANY_IDLE_CONNECTIONS" - High number of idle connections.
	//   "SIGNAL_TYPE_REPLICATION_LAG" - Replication delay.
	//   "SIGNAL_TYPE_OUTDATED_VERSION" - Outdated version.
	//   "SIGNAL_TYPE_OUTDATED_CLIENT" - Outdated client.
	//   "SIGNAL_TYPE_DATABOOST_DISABLED" - Databoost is disabled.
	//   "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES" - Recommended maintenance
	// policy.
	//   "SIGNAL_TYPE_EXTENDED_SUPPORT" - Resource version is in extended support.
	//   "SIGNAL_TYPE_PERFORMANCE_KPI_CHANGE" - Change in performance KPIs.
	SignalType string `json:"signalType,omitempty"`
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "ACTIVE" - The signal requires attention and has not been addressed yet.
	//   "RESOLVED" - The signal has been fixed, triaged as a non-issue or
	// otherwise addressed and is no longer active.
	//   "MUTED" - The signal has been muted.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdditionalMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalMetadata") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData: Common model for database resource health signal data.

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceId ¶
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceId struct {
	// Provider: Required. Cloud provider name. Ex:
	// GCP/AWS/Azure/OnPrem/SelfManaged
	//
	// Possible values:
	//   "PROVIDER_UNSPECIFIED"
	//   "GCP" - Google cloud platform provider
	//   "AWS" - Amazon web service
	//   "AZURE" - Azure web service
	//   "ONPREM" - On-prem database resources.
	//   "SELFMANAGED" - Self-managed database provider. These are resources on a
	// cloud platform, e.g., database resource installed in a GCE VM, but not a
	// managed database service.
	//   "PROVIDER_OTHER" - For the rest of the other categories. Other refers to
	// the rest of other database service providers, this could be smaller cloud
	// provider. This needs to be provided when the provider is known, but it is
	// not present in the existing set of enum values.
	Provider string `json:"provider,omitempty"`
	// ProviderDescription: Optional. Needs to be used only when the provider is
	// PROVIDER_OTHER.
	ProviderDescription string `json:"providerDescription,omitempty"`
	// ResourceType: Required. The type of resource this ID is identifying. Ex
	// go/keep-sorted start alloydb.googleapis.com/Cluster,
	// alloydb.googleapis.com/Instance, bigtableadmin.googleapis.com/Cluster,
	// bigtableadmin.googleapis.com/Instance compute.googleapis.com/Instance
	// firestore.googleapis.com/Database, redis.googleapis.com/Instance,
	// redis.googleapis.com/Cluster,
	// oracledatabase.googleapis.com/CloudExadataInfrastructure
	// oracledatabase.googleapis.com/CloudVmCluster
	// oracledatabase.googleapis.com/AutonomousDatabase
	// spanner.googleapis.com/Instance, spanner.googleapis.com/Database,
	// sqladmin.googleapis.com/Instance, go/keep-sorted end REQUIRED Please refer
	// go/condor-common-datamodel
	ResourceType string `json:"resourceType,omitempty"`
	// UniqueId: Required. A service-local token that distinguishes this resource
	// from other resources within the same service.
	UniqueId string `json:"uniqueId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Provider") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Provider") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceId: DatabaseResourceId will serve as primary key for any resource ingestion event.

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceId) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceId) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata ¶
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata struct {
	// AvailabilityConfiguration: Availability configuration for this instance
	AvailabilityConfiguration *StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration `json:"availabilityConfiguration,omitempty"`
	// BackupConfiguration: Backup configuration for this instance
	BackupConfiguration *StorageDatabasecenterPartnerapiV1mainBackupConfiguration `json:"backupConfiguration,omitempty"`
	// BackupRun: Latest backup run information for this instance
	BackupRun *StorageDatabasecenterPartnerapiV1mainBackupRun `json:"backupRun,omitempty"`
	// BackupdrConfiguration: Optional. BackupDR Configuration for the resource.
	BackupdrConfiguration *StorageDatabasecenterPartnerapiV1mainBackupDRConfiguration `json:"backupdrConfiguration,omitempty"`
	// CreationTime: The creation time of the resource, i.e. the time when resource
	// is created and recorded in partner service.
	CreationTime string `json:"creationTime,omitempty"`
	// CurrentState: Current state of the instance.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED"
	//   "HEALTHY" - The instance is running.
	//   "UNHEALTHY" - Instance being created, updated, deleted or under
	// maintenance
	//   "SUSPENDED" - When instance is suspended
	//   "DELETED" - Instance is deleted.
	//   "STATE_OTHER" - For rest of the other category
	//   "STOPPED" - Instance is in STOPPED state.
	CurrentState string `json:"currentState,omitempty"`
	// CustomMetadata: Any custom metadata associated with the resource
	CustomMetadata *StorageDatabasecenterPartnerapiV1mainCustomMetadataData `json:"customMetadata,omitempty"`
	// Edition: Optional. Edition represents whether the instance is ENTERPRISE or
	// ENTERPRISE_PLUS. This information is core to Cloud SQL only and is used to
	// identify the edition of the instance.
	//
	// Possible values:
	//   "EDITION_UNSPECIFIED" - Default, to make it consistent with instance
	// edition enum.
	//   "EDITION_ENTERPRISE" - Represents the enterprise edition.
	//   "EDITION_ENTERPRISE_PLUS" - Represents the enterprise plus edition.
	//   "EDITION_STANDARD" - Represents the standard edition.
	Edition string `json:"edition,omitempty"`
	// Entitlements: Entitlements associated with the resource
	Entitlements []*StorageDatabasecenterPartnerapiV1mainEntitlement `json:"entitlements,omitempty"`
	// ExpectedState: The state that the instance is expected to be in. For
	// example, an instance state can transition to UNHEALTHY due to wrong patch
	// update, while the expected state will remain at the HEALTHY.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED"
	//   "HEALTHY" - The instance is running.
	//   "UNHEALTHY" - Instance being created, updated, deleted or under
	// maintenance
	//   "SUSPENDED" - When instance is suspended
	//   "DELETED" - Instance is deleted.
	//   "STATE_OTHER" - For rest of the other category
	//   "STOPPED" - Instance is in STOPPED state.
	ExpectedState string `json:"expectedState,omitempty"`
	// GcbdrConfiguration: GCBDR configuration for the resource.
	GcbdrConfiguration *StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration `json:"gcbdrConfiguration,omitempty"`
	// Id: Required. Unique identifier for a Database resource
	Id *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"id,omitempty"`
	// InstanceType: The type of the instance. Specified at creation time.
	//
	// Possible values:
	//   "INSTANCE_TYPE_UNSPECIFIED" - Unspecified.
	//   "SUB_RESOURCE_TYPE_UNSPECIFIED" - For rest of the other categories.
	//   "PRIMARY" - A regular primary database instance.
	//   "SECONDARY" - A cluster or an instance acting as a secondary.
	//   "READ_REPLICA" - An instance acting as a read-replica.
	//   "OTHER" - For rest of the other categories.
	//   "SUB_RESOURCE_TYPE_PRIMARY" - A regular primary database instance.
	//   "SUB_RESOURCE_TYPE_SECONDARY" - A cluster or an instance acting as a
	// secondary.
	//   "SUB_RESOURCE_TYPE_READ_REPLICA" - An instance acting as a read-replica.
	//   "SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY" - An instance acting as an external
	// primary.
	//   "SUB_RESOURCE_TYPE_OTHER" - For rest of the other categories.
	InstanceType string `json:"instanceType,omitempty"`
	// IsDeletionProtectionEnabled: Optional. Whether deletion protection is
	// enabled for this resource.
	IsDeletionProtectionEnabled bool `json:"isDeletionProtectionEnabled,omitempty"`
	// Location: The resource location. REQUIRED
	Location string `json:"location,omitempty"`
	// MachineConfiguration: Machine configuration for this resource.
	MachineConfiguration *StorageDatabasecenterPartnerapiV1mainMachineConfiguration `json:"machineConfiguration,omitempty"`
	// MaintenanceInfo: Optional. Maintenance info for the resource.
	MaintenanceInfo *StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo `json:"maintenanceInfo,omitempty"`
	// PrimaryResourceId: Identifier for this resource's immediate parent/primary
	// resource if the current resource is a replica or derived form of another
	// Database resource. Else it would be NULL. REQUIRED if the immediate parent
	// exists when first time resource is getting ingested, otherwise optional.
	PrimaryResourceId *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"primaryResourceId,omitempty"`
	// PrimaryResourceLocation: Primary resource location. REQUIRED if the
	// immediate parent exists when first time resource is getting ingested,
	// otherwise optional.
	PrimaryResourceLocation string `json:"primaryResourceLocation,omitempty"`
	// Product: The product this resource represents.
	Product *StorageDatabasecenterProtoCommonProduct `json:"product,omitempty"`
	// ResourceContainer: Closest parent Cloud Resource Manager container of this
	// resource. It must be resource name of a Cloud Resource Manager project with
	// the format of "/", such as "projects/123". For GCP provided resources,
	// number should be project number.
	ResourceContainer string `json:"resourceContainer,omitempty"`
	// ResourceFlags: Optional. List of resource flags for the database resource.
	ResourceFlags []*StorageDatabasecenterPartnerapiV1mainResourceFlags `json:"resourceFlags,omitempty"`
	// ResourceName: Required. Different from DatabaseResourceId.unique_id, a
	// resource name can be reused over time. That is, after a resource named "ABC"
	// is deleted, the name "ABC" can be used to to create a new resource within
	// the same source. Resource name to follow CAIS resource_name format as noted
	// here go/condor-common-datamodel
	ResourceName string `json:"resourceName,omitempty"`
	// SuspensionReason: Optional. Suspension reason for the resource.
	//
	// Possible values:
	//   "SUSPENSION_REASON_UNSPECIFIED" - Suspension reason is unspecified.
	//   "WIPEOUT_HIDE_EVENT" - Wipeout hide event.
	//   "WIPEOUT_PURGE_EVENT" - Wipeout purge event.
	//   "BILLING_DISABLED" - Billing disabled for project
	//   "ABUSER_DETECTED" - Abuse detected for resource
	//   "ENCRYPTION_KEY_INACCESSIBLE" - Encryption key inaccessible.
	//   "REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE" - Replicated cluster
	// encryption key inaccessible.
	SuspensionReason string `json:"suspensionReason,omitempty"`
	// TagsSet: Optional. Tags associated with this resources.
	TagsSet *StorageDatabasecenterPartnerapiV1mainTags `json:"tagsSet,omitempty"`
	// UpdationTime: The time at which the resource was updated and recorded at
	// partner service.
	UpdationTime string `json:"updationTime,omitempty"`
	// UserLabelSet: User-provided labels associated with the resource
	UserLabelSet *StorageDatabasecenterPartnerapiV1mainUserLabels `json:"userLabelSet,omitempty"`
	// Zone: The resource zone. This is only applicable for zonal resources and
	// will be empty for regional and multi-regional resources.
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AvailabilityConfiguration")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailabilityConfiguration") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata: Common model for database resource instance metadata. Next ID: 31

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData ¶
added in v0.167.0
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData struct {
	// AdditionalMetadata: Optional. Any other additional metadata specific to
	// recommendation
	AdditionalMetadata googleapi.RawMessage `json:"additionalMetadata,omitempty"`
	// LastRefreshTime: Required. last time recommendationw as refreshed
	LastRefreshTime string `json:"lastRefreshTime,omitempty"`
	// RecommendationState: Required. Recommendation state
	//
	// Possible values:
	//   "UNSPECIFIED"
	//   "ACTIVE" - Recommendation is active and can be applied. ACTIVE
	// recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.
	//   "CLAIMED" - Recommendation is in claimed state. Recommendations content is
	// immutable and cannot be updated by Google. CLAIMED recommendations can be
	// marked as CLAIMED, SUCCEEDED, or FAILED.
	//   "SUCCEEDED" - Recommendation is in succeeded state. Recommendations
	// content is immutable and cannot be updated by Google. SUCCEEDED
	// recommendations can be marked as SUCCEEDED, or FAILED.
	//   "FAILED" - Recommendation is in failed state. Recommendations content is
	// immutable and cannot be updated by Google. FAILED recommendations can be
	// marked as SUCCEEDED, or FAILED.
	//   "DISMISSED" - Recommendation is in dismissed state. Recommendation content
	// can be updated by Google. DISMISSED recommendations can be marked as ACTIVE.
	RecommendationState string `json:"recommendationState,omitempty"`
	// Recommender: Required. Name of recommendation. Examples:
	// organizations/1234/locations/us-central1/recommenders/google.cloudsql.instanc
	// e.PerformanceRecommender/recommendations/9876
	Recommender string `json:"recommender,omitempty"`
	// RecommenderId: Required. ID of recommender. Examples:
	// "google.cloudsql.instance.PerformanceRecommender"
	RecommenderId string `json:"recommenderId,omitempty"`
	// RecommenderSubtype: Required. Contains an identifier for a subtype of
	// recommendations produced for the same recommender. Subtype is a function of
	// content and impact, meaning a new subtype might be added when significant
	// changes to `content` or `primary_impact.category` are introduced. See the
	// Recommenders section to see a list of subtypes for a given Recommender.
	// Examples: For recommender =
	// "google.cloudsql.instance.PerformanceRecommender", recommender_subtype can
	// be
	// "MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE"/"POSTGRES_HIGH_TRANSACTION_I
	// D_UTILIZATION_BEST_PRACTICE"
	RecommenderSubtype string `json:"recommenderSubtype,omitempty"`
	// ResourceName: Required. Database resource name associated with the signal.
	// Resource name to follow CAIS resource_name format as noted here
	// go/condor-common-datamodel
	ResourceName string `json:"resourceName,omitempty"`
	// SignalType: Required. Type of signal, for example, `SIGNAL_TYPE_IDLE`,
	// `SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES`, etc.
	//
	// Possible values:
	//   "SIGNAL_TYPE_UNSPECIFIED" - Unspecified.
	//   "SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER" - Represents if a
	// resource is protected by automatic failover. Checks for resources that are
	// configured to have redundancy within a region that enables automatic
	// failover.
	//   "SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS" - Represents if a group
	// is replicating across regions. Checks for resources that are configured to
	// have redundancy, and ongoing replication, across regions.
	//   "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES" - Represents if the resource
	// is available in multiple zones or not.
	//   "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS" - Represents if a resource
	// is available in multiple regions.
	//   "SIGNAL_TYPE_NO_PROMOTABLE_REPLICA" - Represents if a resource has a
	// promotable replica.
	//   "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY" - Represents if a resource has an
	// automated backup policy.
	//   "SIGNAL_TYPE_SHORT_BACKUP_RETENTION" - Represents if a resources has a
	// short backup retention period.
	//   "SIGNAL_TYPE_LAST_BACKUP_FAILED" - Represents if the last backup of a
	// resource failed.
	//   "SIGNAL_TYPE_LAST_BACKUP_OLD" - Represents if the last backup of a
	// resource is older than some threshold value.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0" - Represents if a resource
	// violates CIS GCP Foundation 2.0.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3" - Represents if a resource
	// violates CIS GCP Foundation 1.3.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2" - Represents if a resource
	// violates CIS GCP Foundation 1.2.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1" - Represents if a resource
	// violates CIS GCP Foundation 1.1.
	//   "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0" - Represents if a resource
	// violates CIS GCP Foundation 1.0.
	//   "SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0" - Represents if a resource
	// violates CIS Controls 8.0.
	//   "SIGNAL_TYPE_VIOLATES_NIST_800_53" - Represents if a resource violates
	// NIST 800-53.
	//   "SIGNAL_TYPE_VIOLATES_NIST_800_53_R5" - Represents if a resource violates
	// NIST 800-53 R5.
	//   "SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0" - Represents if a
	// resource violates NIST Cybersecurity Framework 1.0.
	//   "SIGNAL_TYPE_VIOLATES_ISO_27001" - Represents if a resource violates
	// ISO-27001.
	//   "SIGNAL_TYPE_VIOLATES_ISO_27001_V2022" - Represents if a resource violates
	// ISO 27001 2022.
	//   "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1" - Represents if a resource violates
	// PCI-DSS v3.2.1.
	//   "SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0" - Represents if a resource violates
	// PCI-DSS v4.0.
	//   "SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4" - Represents if a resource
	// violates Cloud Controls Matrix v4.0.
	//   "SIGNAL_TYPE_VIOLATES_HIPAA" - Represents if a resource violates HIPAA.
	//   "SIGNAL_TYPE_VIOLATES_SOC2_V2017" - Represents if a resource violates SOC2
	// v2017.
	//   "SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING" - Represents if
	// log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED" - Represents if the log_duration
	// database flag for a Cloud SQL for PostgreSQL instance is not set to on.
	//   "SIGNAL_TYPE_VERBOSE_ERROR_LOGGING" - Represents if the
	// log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is
	// not set to default or stricter (default or terse).
	//   "SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED" - Represents if the
	// log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_LOGGING_MOST_ERRORS" - Represents if the
	// log_min_error_statement database flag for a Cloud SQL for PostgreSQL
	// instance is not set appropriately.
	//   "SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS" - Represents if the
	// log_min_error_statement database flag for a Cloud SQL for PostgreSQL
	// instance does not have an appropriate severity level.
	//   "SIGNAL_TYPE_MINIMAL_ERROR_LOGGING" - Represents if the log_min_messages
	// database flag for a Cloud SQL for PostgreSQL instance is not set to warning
	// or another recommended value.
	//   "SIGNAL_TYPE_QUERY_STATISTICS_LOGGED" - Represents if the databaseFlags
	// property of instance metadata for the log_executor_status field is set to
	// on.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME" - Represents if the
	// log_hostname database flag for a Cloud SQL for PostgreSQL instance is not
	// set to off.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS" - Represents if the
	// log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS" - Represents if the
	// log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS" - Represents if the
	// log_statement database flag for a Cloud SQL for PostgreSQL instance is not
	// set to DDL (all data definition statements).
	//   "SIGNAL_TYPE_LOGGING_QUERY_STATISTICS" - Represents if the
	// log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is
	// not set to off.
	//   "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES" - Represents if the
	// log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not
	// set to "0". (NOTE: 0 = ON)
	//   "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED" - Represents if the user
	// connections database flag for a Cloud SQL for SQL Server instance is
	// configured.
	//   "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED" - Represents if the user options
	// database flag for Cloud SQL SQL Server instance is configured or not.
	//   "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS" - Represents if a resource is
	// exposed to public access.
	//   "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS" - Represents if a resources requires
	// all incoming connections to use SSL or not.
	//   "SIGNAL_TYPE_NO_ROOT_PASSWORD" - Represents if a Cloud SQL database has a
	// password configured for the root account or not.
	//   "SIGNAL_TYPE_WEAK_ROOT_PASSWORD" - Represents if a Cloud SQL database has
	// a weak password configured for the root account.
	//   "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED" - Represents if a SQL
	// database instance is not encrypted with customer-managed encryption keys
	// (CMEK).
	//   "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED" - Represents if The
	// contained database authentication database flag for a Cloud SQL for SQL
	// Server instance is not set to off.
	//   "SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING" - Represents if the
	// cross_db_ownership_chaining database flag for a Cloud SQL for SQL Server
	// instance is not set to off.
	//   "SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS" - Represents if he external
	// scripts enabled database flag for a Cloud SQL for SQL Server instance is not
	// set to off.
	//   "SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS" - Represents if the local_infile
	// database flag for a Cloud SQL for MySQL instance is not set to off.
	//   "SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED" - Represents if the
	// log_connections database flag for a Cloud SQL for PostgreSQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED" - Represents if the
	// log_disconnections database flag for a Cloud SQL for PostgreSQL instance is
	// not set to on.
	//   "SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO" - Represents if the
	// log_min_duration_statement database flag for a Cloud SQL for PostgreSQL
	// instance is not set to -1.
	//   "SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS" - Represents if the remote access
	// database flag for a Cloud SQL for SQL Server instance is not set to off.
	//   "SIGNAL_TYPE_DATABASE_NAMES_EXPOSED" - Represents if the
	// skip_show_database database flag for a Cloud SQL for MySQL instance is not
	// set to on.
	//   "SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED" - Represents if the 3625
	// (trace flag) database flag for a Cloud SQL for SQL Server instance is not
	// set to on.
	//   "SIGNAL_TYPE_PUBLIC_IP_ENABLED" - Represents if public IP is enabled.
	//   "SIGNAL_TYPE_IDLE" - Represents Idle instance helps to reduce costs.
	//   "SIGNAL_TYPE_OVERPROVISIONED" - Represents instances that are
	// unnecessarily large for given workload.
	//   "SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES" - Represents high number of
	// concurrently opened tables.
	//   "SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES" - Represents high table count close to
	// SLA limit.
	//   "SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION" - Represents high number of
	// unvacuumed transactions
	//   "SIGNAL_TYPE_UNDERPROVISIONED" - Represents need for more CPU and/or
	// memory
	//   "SIGNAL_TYPE_OUT_OF_DISK" - Represents out of disk.
	//   "SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY" - Represents server
	// certificate is near expiry.
	//   "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED" - Represents database auditing is
	// disabled.
	//   "SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS" - Represents not restricted to
	// authorized networks.
	//   "SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP" - Represents violate org
	// policy restrict public ip.
	//   "SIGNAL_TYPE_QUOTA_LIMIT" - Cluster nearing quota limit
	//   "SIGNAL_TYPE_NO_PASSWORD_POLICY" - No password policy set on resources
	//   "SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT" - Performance impact of
	// connections settings
	//   "SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT" - Performance impact of
	// temporary tables settings
	//   "SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT" - Performance impact of
	// transaction logs settings
	//   "SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES" - Performance impact of high
	// joins without indexes
	//   "SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES" - Detects events where a
	// Cloud SQL superuser (postgres for PostgreSQL servers or root for MySQL
	// users) writes to non-system tables.
	//   "SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS" - Detects events where a
	// database user or role has been granted all privileges to a database, or to
	// all tables, procedures, or functions in a schema.
	//   "SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET" - Detects if
	// database instance data exported to a Cloud Storage bucket outside of the
	// organization.
	//   "SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET" - Detects if
	// database instance data exported to a Cloud Storage bucket that is owned by
	// the organization and is publicly accessible.
	//   "SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM" - Detects if a database
	// instance is using a weak password hash algorithm.
	//   "SIGNAL_TYPE_NO_USER_PASSWORD_POLICY" - Detects if a database instance has
	// no user password policy set.
	//   "SIGNAL_TYPE_HOT_NODE" - Detects if a database instance/cluster has a hot
	// node.
	//   "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY" - Detects if a database instance
	// has no point in time recovery enabled.
	//   "SIGNAL_TYPE_RESOURCE_SUSPENDED" - Detects if a database instance/cluster
	// is suspended.
	//   "SIGNAL_TYPE_EXPENSIVE_COMMANDS" - Detects that expensive commands are
	// being run on a database instance impacting overall performance.
	//   "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED" - Indicates that the
	// instance does not have a maintenance policy configured.
	//   "SIGNAL_TYPE_NO_DELETION_PROTECTION" - Deletion Protection Disabled for
	// the resource
	//   "SIGNAL_TYPE_INEFFICIENT_QUERY" - Indicates that the instance has
	// inefficient queries detected.
	//   "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD" - Indicates that the instance has
	// read intensive workload.
	//   "SIGNAL_TYPE_MEMORY_LIMIT" - Indicates that the instance is nearing memory
	// limit.
	//   "SIGNAL_TYPE_MAX_SERVER_MEMORY" - Indicates that the instance's max server
	// memory is configured higher than the recommended value.
	//   "SIGNAL_TYPE_LARGE_ROWS" - Indicates that the database has large rows
	// beyond the recommended limit.
	//   "SIGNAL_TYPE_HIGH_WRITE_PRESSURE" - Heavy write pressure on the database
	// rows.
	//   "SIGNAL_TYPE_HIGH_READ_PRESSURE" - Heavy read pressure on the database
	// rows.
	//   "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED" - Encryption org policy
	// not satisfied.
	//   "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED" - Location org policy not
	// satisfied.
	//   "SIGNAL_TYPE_OUTDATED_MINOR_VERSION" - Outdated DB minor version.
	//   "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED" - Schema not optimized.
	//   "SIGNAL_TYPE_MANY_IDLE_CONNECTIONS" - High number of idle connections.
	//   "SIGNAL_TYPE_REPLICATION_LAG" - Replication delay.
	//   "SIGNAL_TYPE_OUTDATED_VERSION" - Outdated version.
	//   "SIGNAL_TYPE_OUTDATED_CLIENT" - Outdated client.
	//   "SIGNAL_TYPE_DATABOOST_DISABLED" - Databoost is disabled.
	//   "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES" - Recommended maintenance
	// policy.
	//   "SIGNAL_TYPE_EXTENDED_SUPPORT" - Resource version is in extended support.
	//   "SIGNAL_TYPE_PERFORMANCE_KPI_CHANGE" - Change in performance KPIs.
	SignalType string `json:"signalType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdditionalMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdditionalMetadata") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData : Common model for database resource recommendation signal data.

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData) MarshalJSON ¶
added in v0.167.0
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData ¶
added in v0.250.0
type StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData struct {
	// FullResourceName: Required. Full Resource name of the source resource.
	FullResourceName string `json:"fullResourceName,omitempty"`
	// LastRefreshTime: Required. Last time signal was refreshed
	LastRefreshTime string `json:"lastRefreshTime,omitempty"`
	// ResourceId: Database resource id.
	ResourceId *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"resourceId,omitempty"`
	// SignalBoolValue: Signal data for boolean signals.
	SignalBoolValue bool `json:"signalBoolValue,omitempty"`
	// SignalState: Required. Output only. Signal state of the signal
	//
	// Possible values:
	//   "SIGNAL_STATE_UNSPECIFIED" - Unspecified signal state.
	//   "ACTIVE" - Signal is active and requires attention.
	//   "INACTIVE" - Signal is inactive and does not require attention.
	//   "DISMISSED" - Signal is dismissed by the user and should not be shown to
	// the user again.
	SignalState string `json:"signalState,omitempty"`
	// SignalType: Required. Signal type of the signal
	//
	// Possible values:
	//   "SIGNAL_TYPE_UNSPECIFIED" - Unspecified signal type.
	//   "SIGNAL_TYPE_OUTDATED_MINOR_VERSION" - Outdated Minor Version
	//   "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED" - Represents database auditing is
	// disabled.
	//   "SIGNAL_TYPE_NO_ROOT_PASSWORD" - Represents if a database has a password
	// configured for the root account or not.
	//   "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS" - Represents if a resource is
	// exposed to public access.
	//   "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS" - Represents if a resources requires
	// all incoming connections to use SSL or not.
	//   "SIGNAL_TYPE_EXTENDED_SUPPORT" - Represents if a resource version is in
	// extended support.
	//   "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY" - Represents if a resource has no
	// automated backup policy.
	SignalType string `json:"signalType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FullResourceName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FullResourceName") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData: Database resource signal data. This is used to send signals to Condor which are based on the DB/Instance/Fleet level configurations. These will be used to send signals for all inventory types. Next ID: 7

func (StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData) MarshalJSON ¶
added in v0.250.0
func (s StorageDatabasecenterPartnerapiV1mainDatabaseResourceSignalData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainEntitlement ¶
added in v0.167.0
type StorageDatabasecenterPartnerapiV1mainEntitlement struct {
	// EntitlementState: The current state of user's accessibility to a
	// feature/benefit.
	//
	// Possible values:
	//   "ENTITLEMENT_STATE_UNSPECIFIED"
	//   "ENTITLED" - User is entitled to a feature/benefit, but whether it has
	// been successfully provisioned is decided by provisioning state.
	//   "REVOKED" - User is entitled to a feature/benefit, but it was requested to
	// be revoked. Whether the revoke has been successful is decided by
	// provisioning state.
	EntitlementState string `json:"entitlementState,omitempty"`
	// Type: An enum that represents the type of this entitlement.
	//
	// Possible values:
	//   "ENTITLEMENT_TYPE_UNSPECIFIED" - The entitlement type is unspecified.
	//   "GEMINI" - The root entitlement representing Gemini package ownership.This
	// will no longer be supported in the future.
	//   "NATIVE" - The entitlement representing Native Tier, This will be the
	// default Entitlement going forward with GCA Enablement.
	//   "GCA_STANDARD" - The entitlement representing GCA-Standard Tier.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EntitlementState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EntitlementState") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainEntitlement: Proto representing the access that a user has to a specific feature/service. NextId: 3.

func (StorageDatabasecenterPartnerapiV1mainEntitlement) MarshalJSON ¶
added in v0.167.0
func (s StorageDatabasecenterPartnerapiV1mainEntitlement) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration ¶
added in v0.224.0
type StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration struct {
	// GcbdrManaged: Whether the resource is managed by GCBDR.
	GcbdrManaged bool `json:"gcbdrManaged,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcbdrManaged") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcbdrManaged") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration: GCBDR Configuration for the resource.

func (StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration) MarshalJSON ¶
added in v0.224.0
func (s StorageDatabasecenterPartnerapiV1mainGCBDRConfiguration) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata ¶
added in v0.193.0
type StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata struct {
	// BackupConfiguration: Backup configuration for this database
	BackupConfiguration *StorageDatabasecenterPartnerapiV1mainBackupConfiguration `json:"backupConfiguration,omitempty"`
	// BackupRun: Information about the last backup attempt for this database
	BackupRun *StorageDatabasecenterPartnerapiV1mainBackupRun `json:"backupRun,omitempty"`
	// IsDeletionProtectionEnabled: Whether deletion protection is enabled for this
	// internal resource.
	IsDeletionProtectionEnabled bool                                                     `json:"isDeletionProtectionEnabled,omitempty"`
	Product                     *StorageDatabasecenterProtoCommonProduct                 `json:"product,omitempty"`
	ResourceId                  *StorageDatabasecenterPartnerapiV1mainDatabaseResourceId `json:"resourceId,omitempty"`
	// ResourceName: Required. internal resource name for spanner this will be
	// database name
	// e.g."spanner.googleapis.com/projects/123/abc/instances/inst1/databases/db1"
	ResourceName string `json:"resourceName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackupConfiguration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackupConfiguration") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata: Metadata for individual internal resources in an instance. e.g. spanner instance can have multiple databases with unique configuration settings. Similarly bigtable can have multiple clusters within same bigtable instance.

func (StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata) MarshalJSON ¶
added in v0.193.0
func (s StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainMachineConfiguration ¶
added in v0.182.0
type StorageDatabasecenterPartnerapiV1mainMachineConfiguration struct {
	// BaselineSlots: Optional. Baseline slots for BigQuery Reservations. Baseline
	// slots are in increments of 50.
	BaselineSlots int64 `json:"baselineSlots,omitempty,string"`
	// CpuCount: The number of CPUs. Deprecated. Use vcpu_count instead.
	// TODO(b/342344482) add proto validations again after bug fix.
	CpuCount int64 `json:"cpuCount,omitempty"`
	// MaxReservationSlots: Optional. Max slots for BigQuery Reservations. Max
	// slots are in increments of 50.
	MaxReservationSlots int64 `json:"maxReservationSlots,omitempty,string"`
	// MemorySizeInBytes: Memory size in bytes. TODO(b/342344482) add proto
	// validations again after bug fix.
	MemorySizeInBytes int64 `json:"memorySizeInBytes,omitempty,string"`
	// ShardCount: Optional. Number of shards (if applicable).
	ShardCount int64 `json:"shardCount,omitempty"`
	// VcpuCount: Optional. The number of vCPUs. TODO(b/342344482) add proto
	// validations again after bug fix.
	VcpuCount float64 `json:"vcpuCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BaselineSlots") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BaselineSlots") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainMachineConfiguration: MachineConfiguration describes the configuration of a machine specific to Database Resource.

func (StorageDatabasecenterPartnerapiV1mainMachineConfiguration) MarshalJSON ¶
added in v0.182.0
func (s StorageDatabasecenterPartnerapiV1mainMachineConfiguration) MarshalJSON() ([]byte, error)
func (*StorageDatabasecenterPartnerapiV1mainMachineConfiguration) UnmarshalJSON ¶
added in v0.212.0
func (s *StorageDatabasecenterPartnerapiV1mainMachineConfiguration) UnmarshalJSON(data []byte) error
type StorageDatabasecenterPartnerapiV1mainObservabilityMetricData ¶
added in v0.182.0
type StorageDatabasecenterPartnerapiV1mainObservabilityMetricData struct {
	// AggregationType: Required. Type of aggregation performed on the metric.
	//
	// Possible values:
	//   "AGGREGATION_TYPE_UNSPECIFIED" - Unspecified aggregation type.
	//   "PEAK" - PEAK aggregation type.
	//   "P99" - P99 aggregation type.
	//   "P95" - P95 aggregation type.
	//   "CURRENT" - current aggregation type.
	AggregationType string `json:"aggregationType,omitempty"`
	// MetricType: Required. Type of metric like CPU, Memory, etc.
	//
	// Possible values:
	//   "METRIC_TYPE_UNSPECIFIED" - Unspecified metric type.
	//   "CPU_UTILIZATION" - CPU utilization for a resource. The value is a
	// fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).
	//   "MEMORY_UTILIZATION" - Memory utilization for a resource. The value is a
	// fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).
	//   "NETWORK_CONNECTIONS" - Number of network connections for a resource.
	//   "STORAGE_UTILIZATION" - Storage utilization for a resource. The value is a
	// fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).
	//   "STORAGE_USED_BYTES" - Sotrage used by a resource.
	//   "NODE_COUNT" - Node count for a resource. It represents the number of node
	// units in a bigtable/spanner instance.
	//   "MEMORY_USED_BYTES" - Memory used by a resource (in bytes).
	//   "PROCESSING_UNIT_COUNT" - Processing units used by a resource. It
	// represents the number of processing units in a spanner instance.
	MetricType string `json:"metricType,omitempty"`
	// ObservationTime: Required. The time the metric value was observed.
	ObservationTime string `json:"observationTime,omitempty"`
	// ResourceName: Required. Database resource name associated with the signal.
	// Resource name to follow CAIS resource_name format as noted here
	// go/condor-common-datamodel
	ResourceName string `json:"resourceName,omitempty"`
	// Value: Required. Value of the metric type.
	Value *StorageDatabasecenterProtoCommonTypedValue `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AggregationType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AggregationType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (StorageDatabasecenterPartnerapiV1mainObservabilityMetricData) MarshalJSON ¶
added in v0.182.0
func (s StorageDatabasecenterPartnerapiV1mainObservabilityMetricData) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainOperationError ¶
type StorageDatabasecenterPartnerapiV1mainOperationError struct {
	// Code: Identifies the specific error that occurred. REQUIRED
	Code string `json:"code,omitempty"`
	// Possible values:
	//   "OPERATION_ERROR_TYPE_UNSPECIFIED" - UNSPECIFIED means product type is not
	// known or available.
	//   "KMS_KEY_ERROR" - key destroyed, expired, not found, unreachable or
	// permission denied.
	//   "DATABASE_ERROR" - Database is not accessible
	//   "STOCKOUT_ERROR" - The zone or region does not have sufficient resources
	// to handle the request at the moment
	//   "CANCELLATION_ERROR" - User initiated cancellation
	//   "SQLSERVER_ERROR" - SQL server specific error
	//   "INTERNAL_ERROR" - Any other internal error.
	ErrorType string `json:"errorType,omitempty"`
	// Message: Additional information about the error encountered. REQUIRED
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

StorageDatabasecenterPartnerapiV1mainOperationError: An error that occurred during a backup creation operation.

func (StorageDatabasecenterPartnerapiV1mainOperationError) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainOperationError) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceFlags ¶
added in v0.266.0
type StorageDatabasecenterPartnerapiV1mainResourceFlags struct {
	// Key: Optional. Key of the resource flag.
	Key string `json:"key,omitempty"`
	// Value: Optional. Value of the resource flag.
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

StorageDatabasecenterPartnerapiV1mainResourceFlags: Message type for storing resource flags.

func (StorageDatabasecenterPartnerapiV1mainResourceFlags) MarshalJSON ¶
added in v0.266.0
func (s StorageDatabasecenterPartnerapiV1mainResourceFlags) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule ¶
added in v0.252.0
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule struct {
	// EndDate: Optional. Deny period end date.
	EndDate *GoogleTypeDate `json:"endDate,omitempty"`
	// StartDate: Optional. The start date of the deny maintenance period.
	StartDate *GoogleTypeDate `json:"startDate,omitempty"`
	// Time: Optional. Time in UTC when the deny period starts on start_date and
	// ends on end_date.
	Time *GoogleTypeTimeOfDay `json:"time,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndDate") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndDate") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule: Deny maintenance period for the database resource. It specifies the time range during which the maintenance cannot start. This is configured by the customer.

func (StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule) MarshalJSON ¶
added in v0.252.0
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo ¶
added in v0.252.0
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo struct {
	// CurrentVersionReleaseDate: Optional. The date when the current maintenance
	// version was released.
	CurrentVersionReleaseDate *GoogleTypeDate `json:"currentVersionReleaseDate,omitempty"`
	// DenyMaintenanceSchedules: Optional. List of Deny maintenance period for the
	// database resource.
	DenyMaintenanceSchedules []*StorageDatabasecenterPartnerapiV1mainResourceMaintenanceDenySchedule `json:"denyMaintenanceSchedules,omitempty"`
	// IsInstanceStopped: Optional. Whether the instance is in stopped state. This
	// information is temporarily being captured in maintenanceInfo, till STOPPED
	// state is supported by DB Center.
	IsInstanceStopped bool `json:"isInstanceStopped,omitempty"`
	// MaintenanceSchedule: Optional. Maintenance window for the database resource.
	MaintenanceSchedule *StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule `json:"maintenanceSchedule,omitempty"`
	// MaintenanceState: Output only. Current state of maintenance on the database
	// resource.
	//
	// Possible values:
	//   "MAINTENANCE_STATE_UNSPECIFIED" - Unspecified state.
	//   "CREATING" - Database resource is being created.
	//   "READY" - Database resource has been created and is ready to use.
	//   "UPDATING" - Database resource is being updated.
	//   "REPAIRING" - Database resource is unheathy and under repair.
	//   "DELETING" - Database resource is being deleted.
	//   "ERROR" - Database resource encountered an error and is in indeterministic
	// state.
	MaintenanceState string `json:"maintenanceState,omitempty"`
	// MaintenanceVersion: Optional. Current Maintenance version of the database
	// resource. Example: "MYSQL_8_0_41.R20250531.01_15"
	MaintenanceVersion string `json:"maintenanceVersion,omitempty"`
	// UpcomingMaintenance: Optional. Upcoming maintenance for the database
	// resource. This field is populated once SLM generates and publishes upcoming
	// maintenance window.
	UpcomingMaintenance *StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance `json:"upcomingMaintenance,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentVersionReleaseDate")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentVersionReleaseDate") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo: MaintenanceInfo to capture the maintenance details of database resource.

func (StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo) MarshalJSON ¶
added in v0.252.0
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceInfo) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule ¶
added in v0.252.0
type StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule struct {
	// Day: Optional. Preferred day of the week for maintenance, e.g. MONDAY,
	// TUESDAY, etc.
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
	Day string `json:"day,omitempty"`
	// Phase: Optional. Phase of the maintenance window. This is to capture order
	// of maintenance. For example, for Cloud SQL resources, this can be used to
	// capture if the maintenance window is in Week1, Week2, Week5, etc. Non
	// production resources are usually part of early phase. For more details,
	// refer to Cloud SQL resources -
	// https://cloud.google.com/sql/docs/mysql/maintenance
	//
	// Possible values:
	//   "PHASE_UNSPECIFIED" - Phase is unspecified.
	//   "ANY" - Any phase.
	//   "WEEK1" - Week 1.
	//   "WEEK2" - Week 2.
	//   "WEEK5" - Week 5.
	Phase string `json:"phase,omitempty"`
	// Time: Optional. Preferred time to start the maintenance operation on the
	// specified day.
	Time *GoogleTypeTimeOfDay `json:"time,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Day") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Day") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule: Maintenance window for the database resource. It specifies preferred time and day of the week and phase in some cases, when the maintenance can start. This is configured by the customer.

func (StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule) MarshalJSON ¶
added in v0.252.0
func (s StorageDatabasecenterPartnerapiV1mainResourceMaintenanceSchedule) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainRetentionSettings ¶
type StorageDatabasecenterPartnerapiV1mainRetentionSettings struct {
	// DurationBasedRetention: Duration based retention period i.e. 172800 seconds
	// (2 days)
	DurationBasedRetention string `json:"durationBasedRetention,omitempty"`
	QuantityBasedRetention int64  `json:"quantityBasedRetention,omitempty"`
	// RetentionUnit: The unit that 'retained_backups' represents.
	//
	// Possible values:
	//   "RETENTION_UNIT_UNSPECIFIED" - Backup retention unit is unspecified, will
	// be treated as COUNT.
	//   "COUNT" - Retention will be by count, eg. "retain the most recent 7
	// backups".
	//   "TIME" - Retention will be by Time, eg. "retain backups till a specific
	// time" i.e. till 2024-05-01T00:00:00Z.
	//   "DURATION" - Retention will be by duration, eg. "retain the backups for
	// 172800 seconds (2 days)".
	//   "RETENTION_UNIT_OTHER" - For rest of the other category
	RetentionUnit      string `json:"retentionUnit,omitempty"`
	TimeBasedRetention string `json:"timeBasedRetention,omitempty"`
	// TimestampBasedRetentionTime: Timestamp based retention period i.e.
	// 2024-05-01T00:00:00Z
	TimestampBasedRetentionTime string `json:"timestampBasedRetentionTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DurationBasedRetention") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DurationBasedRetention") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (StorageDatabasecenterPartnerapiV1mainRetentionSettings) MarshalJSON ¶
func (s StorageDatabasecenterPartnerapiV1mainRetentionSettings) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainTags ¶
added in v0.199.0
type StorageDatabasecenterPartnerapiV1mainTags struct {
	// Tags: The Tag key/value mappings.
	Tags map[string]string `json:"tags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Tags") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Tags") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainTags: Message type for storing tags. Tags provide a way to create annotations for resources, and in some cases conditionally allow or deny policies based on whether a resource has a specific tag.

func (StorageDatabasecenterPartnerapiV1mainTags) MarshalJSON ¶
added in v0.199.0
func (s StorageDatabasecenterPartnerapiV1mainTags) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance ¶
added in v0.265.0
type StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance struct {
	// EndTime: Optional. The end time of the upcoming maintenance.
	EndTime string `json:"endTime,omitempty"`
	// StartTime: Optional. The start time of the upcoming maintenance.
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

StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance: Upcoming maintenance for the database resource. This is generated by SLM once the upcoming maintenance schedule is published.

func (StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance) MarshalJSON ¶
added in v0.265.0
func (s StorageDatabasecenterPartnerapiV1mainUpcomingMaintenance) MarshalJSON() ([]byte, error)
type StorageDatabasecenterPartnerapiV1mainUserLabels ¶
added in v0.171.0
type StorageDatabasecenterPartnerapiV1mainUserLabels struct {
	Labels map[string]string `json:"labels,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Labels") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Labels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterPartnerapiV1mainUserLabels: Message type for storing user labels. User labels are used to tag App Engine resources, allowing users to search for resources matching a set of labels and to aggregate usage data by labels.

func (StorageDatabasecenterPartnerapiV1mainUserLabels) MarshalJSON ¶
added in v0.171.0
func (s StorageDatabasecenterPartnerapiV1mainUserLabels) MarshalJSON() ([]byte, error)
type StorageDatabasecenterProtoCommonProduct ¶
type StorageDatabasecenterProtoCommonProduct struct {
	// Engine: The specific engine that the underlying database is running.
	//
	// Possible values:
	//   "ENGINE_UNSPECIFIED" - UNSPECIFIED means engine type is not known or
	// available.
	//   "ENGINE_MYSQL" - MySQL binary running as an engine in the database
	// instance.
	//   "MYSQL" - MySQL binary running as engine in database instance.
	//   "ENGINE_POSTGRES" - Postgres binary running as engine in database
	// instance.
	//   "POSTGRES" - Postgres binary running as engine in database instance.
	//   "ENGINE_SQL_SERVER" - SQLServer binary running as engine in database
	// instance.
	//   "SQL_SERVER" - SQLServer binary running as engine in database instance.
	//   "ENGINE_NATIVE" - Native database binary running as engine in instance.
	//   "NATIVE" - Native database binary running as engine in instance.
	//   "ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT" - Cloud Spanner with
	// PostgreSQL dialect.
	//   "ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT" - Cloud Spanner with Google
	// SQL dialect.
	//   "ENGINE_MEMORYSTORE_FOR_REDIS" - Memorystore with Redis dialect.
	//   "ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER" - Memorystore with Redis cluster
	// dialect.
	//   "ENGINE_OTHER" - Other refers to rest of other database engine. This is to
	// be when engine is known, but it is not present in this enum.
	//   "ENGINE_FIRESTORE_WITH_NATIVE_MODE" - Firestore with native mode.
	//   "ENGINE_FIRESTORE_WITH_DATASTORE_MODE" - Firestore with datastore mode.
	//   "ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE" - Firestore with
	// MongoDB compatibility mode.
	//   "ENGINE_EXADATA_ORACLE" - Oracle Exadata engine.
	//   "ENGINE_ADB_SERVERLESS_ORACLE" - Oracle Autonomous DB Serverless engine.
	Engine string `json:"engine,omitempty"`
	// MinorVersion: Minor version of the underlying database engine. Example
	// values: For MySQL, it could be "8.0.32", "5.7.32" etc.. For Postgres, it
	// could be "14.3", "15.3" etc..
	MinorVersion string `json:"minorVersion,omitempty"`
	// Type: Type of specific database product. It could be CloudSQL, AlloyDB etc..
	//
	// Possible values:
	//   "PRODUCT_TYPE_UNSPECIFIED" - UNSPECIFIED means product type is not known
	// or available.
	//   "PRODUCT_TYPE_CLOUD_SQL" - Cloud SQL product area in GCP
	//   "CLOUD_SQL" - Cloud SQL product area in GCP
	//   "PRODUCT_TYPE_ALLOYDB" - AlloyDB product area in GCP
	//   "ALLOYDB" - AlloyDB product area in GCP
	//   "PRODUCT_TYPE_SPANNER" - Spanner product area in GCP
	//   "PRODUCT_TYPE_ON_PREM" - On premises database product.
	//   "ON_PREM" - On premises database product.
	//   "PRODUCT_TYPE_MEMORYSTORE" - Memorystore product area in GCP
	//   "PRODUCT_TYPE_BIGTABLE" - Bigtable product area in GCP
	//   "PRODUCT_TYPE_FIRESTORE" - Firestore product area in GCP.
	//   "PRODUCT_TYPE_COMPUTE_ENGINE" - Compute Engine self managed databases
	//   "PRODUCT_TYPE_ORACLE_ON_GCP" - Oracle product area in GCP
	//   "PRODUCT_TYPE_BIGQUERY" - BigQuery product area in GCP
	//   "PRODUCT_TYPE_OTHER" - Other refers to rest of other product type. This is
	// to be when product type is known, but it is not present in this enum.
	Type string `json:"type,omitempty"`
	// Version: Version of the underlying database engine. Example values: For
	// MySQL, it could be "8.0", "5.7" etc.. For Postgres, it could be "14", "15"
	// etc..
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Engine") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Engine") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StorageDatabasecenterProtoCommonProduct: Product specification for Condor resources.

func (StorageDatabasecenterProtoCommonProduct) MarshalJSON ¶
func (s StorageDatabasecenterProtoCommonProduct) MarshalJSON() ([]byte, error)
type StorageDatabasecenterProtoCommonTypedValue ¶
added in v0.185.0
type StorageDatabasecenterProtoCommonTypedValue struct {
	// BoolValue: For boolean value
	BoolValue bool `json:"boolValue,omitempty"`
	// DoubleValue: For double value
	DoubleValue float64 `json:"doubleValue,omitempty"`
	// Int64Value: For integer value
	Int64Value int64 `json:"int64Value,omitempty,string"`
	// StringValue: For string value
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

StorageDatabasecenterProtoCommonTypedValue: TypedValue represents the value of a metric type. It can either be a double, an int64, a string or a bool.

func (StorageDatabasecenterProtoCommonTypedValue) MarshalJSON ¶
added in v0.185.0
func (s StorageDatabasecenterProtoCommonTypedValue) MarshalJSON() ([]byte, error)
func (*StorageDatabasecenterProtoCommonTypedValue) UnmarshalJSON ¶
added in v0.185.0
func (s *StorageDatabasecenterProtoCommonTypedValue) UnmarshalJSON(data []byte) error
type StringRestrictions ¶
type StringRestrictions struct {
	// AllowedValues: The list of allowed values, if bounded. This field will be
	// empty if there is a unbounded number of allowed values.
	AllowedValues []string `json:"allowedValues,omitempty"`
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

StringRestrictions: Restrictions on STRING type values

func (StringRestrictions) MarshalJSON ¶
func (s StringRestrictions) MarshalJSON() ([]byte, error)
type SupportedDatabaseFlag ¶
type SupportedDatabaseFlag struct {
	// AcceptsMultipleValues: Whether the database flag accepts multiple values. If
	// true, a comma-separated list of stringified values may be specified.
	AcceptsMultipleValues bool `json:"acceptsMultipleValues,omitempty"`
	// FlagName: The name of the database flag, e.g. "max_allowed_packets". The is
	// a possibly key for the Instance.database_flags map field.
	FlagName string `json:"flagName,omitempty"`
	// IntegerRestrictions: Restriction on INTEGER type value.
	IntegerRestrictions *IntegerRestrictions `json:"integerRestrictions,omitempty"`
	// Name: The name of the flag resource, following Google Cloud conventions,
	// e.g.: * projects/{project}/locations/{location}/flags/{flag} This field
	// currently has no semantic meaning.
	Name string `json:"name,omitempty"`
	// RecommendedIntegerValue: The recommended value for an INTEGER flag.
	RecommendedIntegerValue int64 `json:"recommendedIntegerValue,omitempty,string"`
	// RecommendedStringValue: The recommended value for a STRING flag.
	RecommendedStringValue string `json:"recommendedStringValue,omitempty"`
	// RequiresDbRestart: Whether setting or updating this flag on an Instance
	// requires a database restart. If a flag that requires database restart is
	// set, the backend will automatically restart the database (making sure to
	// satisfy any availability SLO's).
	RequiresDbRestart bool `json:"requiresDbRestart,omitempty"`
	// Scope: The scope of the flag.
	//
	// Possible values:
	//   "SCOPE_UNSPECIFIED" - The scope of the flag is not specified. Default is
	// DATABASE.
	//   "DATABASE" - The flag is a database flag.
	//   "CONNECTION_POOL" - The flag is a connection pool flag.
	Scope string `json:"scope,omitempty"`
	// StringRestrictions: Restriction on STRING type value.
	StringRestrictions *StringRestrictions `json:"stringRestrictions,omitempty"`
	// SupportedDbVersions: Major database engine versions for which this flag is
	// supported.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	SupportedDbVersions []string `json:"supportedDbVersions,omitempty"`
	// Possible values:
	//   "VALUE_TYPE_UNSPECIFIED" - This is an unknown flag type.
	//   "STRING" - String type flag.
	//   "INTEGER" - Integer type flag.
	//   "FLOAT" - Float type flag.
	//   "NONE" - Denotes that the flag does not accept any values.
	ValueType string `json:"valueType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AcceptsMultipleValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcceptsMultipleValues") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SupportedDatabaseFlag: SupportedDatabaseFlag gives general information about a database flag, like type and allowed values. This is a static value that is defined on the server side, and it cannot be modified by callers. To set the Database flags on a particular Instance, a caller should modify the Instance.database_flags field.

func (SupportedDatabaseFlag) MarshalJSON ¶
func (s SupportedDatabaseFlag) MarshalJSON() ([]byte, error)
type SwitchoverClusterRequest ¶
added in v0.186.0
type SwitchoverClusterRequest struct {
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
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

SwitchoverClusterRequest: Message for switching over to a cluster

func (SwitchoverClusterRequest) MarshalJSON ¶
added in v0.186.0
func (s SwitchoverClusterRequest) MarshalJSON() ([]byte, error)
type TimeBasedRetention ¶
type TimeBasedRetention struct {
	// RetentionPeriod: The retention period.
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

TimeBasedRetention: A time based retention policy specifies that all backups within a certain time period should be retained.

func (TimeBasedRetention) MarshalJSON ¶
func (s TimeBasedRetention) MarshalJSON() ([]byte, error)
type TrialMetadata ¶
added in v0.186.0
type TrialMetadata struct {
	// EndTime: End time of the trial cluster.
	EndTime string `json:"endTime,omitempty"`
	// GraceEndTime: grace end time of the cluster.
	GraceEndTime string `json:"graceEndTime,omitempty"`
	// StartTime: start time of the trial cluster.
	StartTime string `json:"startTime,omitempty"`
	// UpgradeTime: Upgrade time of trial cluster to Standard cluster.
	UpgradeTime string `json:"upgradeTime,omitempty"`
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

TrialMetadata: Contains information and all metadata related to TRIAL clusters.

func (TrialMetadata) MarshalJSON ¶
added in v0.186.0
func (s TrialMetadata) MarshalJSON() ([]byte, error)
type UpdatePolicy ¶
type UpdatePolicy struct {
	// Mode: Mode for updating the instance.
	//
	// Possible values:
	//   "MODE_UNSPECIFIED" - Mode is unknown.
	//   "DEFAULT" - Least disruptive way to apply the update.
	//   "FORCE_APPLY" - Performs a forced update when applicable. This will be
	// fast but may incur a downtime.
	Mode string `json:"mode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Mode") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Mode") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdatePolicy: Policy to be used while updating the instance.

func (UpdatePolicy) MarshalJSON ¶
func (s UpdatePolicy) MarshalJSON() ([]byte, error)
type UpgradeClusterRequest ¶
added in v0.193.0
type UpgradeClusterRequest struct {
	// Etag: Optional. The current etag of the Cluster. If an etag is provided and
	// does not match the current etag of the Cluster, upgrade will be blocked and
	// an ABORTED error will be returned.
	Etag string `json:"etag,omitempty"`
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server ignores
	// the request if it has already been completed. The server guarantees that for
	// at least 60 minutes since the first request. For example, consider a
	// situation where you make an initial request and the request times out. If
	// you make the request again with the same request ID, the server can check if
	// the original operation with the same request ID was received, and if so,
	// ignores the second request. This prevents clients from accidentally creating
	// duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ValidateOnly: Optional. If set, performs request validation, for example,
	// permission checks and any other type of validation, but does not actually
	// execute the create request.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// Version: Required. The version the cluster is going to be upgraded to.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	Version string `json:"version,omitempty"`
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

UpgradeClusterRequest: Upgrades a cluster.

func (UpgradeClusterRequest) MarshalJSON ¶
added in v0.193.0
func (s UpgradeClusterRequest) MarshalJSON() ([]byte, error)
type UpgradeClusterResponse ¶
added in v0.193.0
type UpgradeClusterResponse struct {
	// ClusterUpgradeDetails: Array of upgrade details for the current cluster and
	// all the secondary clusters associated with this cluster.
	ClusterUpgradeDetails []*ClusterUpgradeDetails `json:"clusterUpgradeDetails,omitempty"`
	// Message: A user friendly message summarising the upgrade operation details
	// and the next steps for the user if there is any.
	Message string `json:"message,omitempty"`
	// Status: Status of upgrade operation.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClusterUpgradeDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClusterUpgradeDetails") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpgradeClusterResponse: UpgradeClusterResponse contains the response for upgrade cluster operation.

func (UpgradeClusterResponse) MarshalJSON ¶
added in v0.193.0
func (s UpgradeClusterResponse) MarshalJSON() ([]byte, error)
type UpgradeClusterStatus ¶
added in v0.224.0
type UpgradeClusterStatus struct {
	// Cancellable: Whether the operation is cancellable.
	Cancellable bool `json:"cancellable,omitempty"`
	// SourceVersion: Source database major version.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	SourceVersion string `json:"sourceVersion,omitempty"`
	// Stages: Status of all upgrade stages.
	Stages []*StageStatus `json:"stages,omitempty"`
	// State: Cluster Major Version Upgrade state.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - Unspecified status.
	//   "NOT_STARTED" - Not started.
	//   "IN_PROGRESS" - In progress.
	//   "SUCCESS" - Operation succeeded.
	//   "FAILED" - Operation failed.
	//   "PARTIAL_SUCCESS" - Operation partially succeeded.
	//   "CANCEL_IN_PROGRESS" - Cancel is in progress.
	//   "CANCELLED" - Cancellation complete.
	State string `json:"state,omitempty"`
	// TargetVersion: Target database major version.
	//
	// Possible values:
	//   "DATABASE_VERSION_UNSPECIFIED" - This is an unknown database version.
	//   "POSTGRES_13" - DEPRECATED - The database version is Postgres 13.
	//   "POSTGRES_14" - The database version is Postgres 14.
	//   "POSTGRES_15" - The database version is Postgres 15.
	//   "POSTGRES_16" - The database version is Postgres 16.
	//   "POSTGRES_17" - The database version is Postgres 17.
	//   "POSTGRES_18" - The database version is Postgres 18.
	TargetVersion string `json:"targetVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Cancellable") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cancellable") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpgradeClusterStatus: Message for current status of the Major Version Upgrade operation.

func (UpgradeClusterStatus) MarshalJSON ¶
added in v0.224.0
func (s UpgradeClusterStatus) MarshalJSON() ([]byte, error)
type User ¶
type User struct {
	// DatabaseRoles: Optional. List of database roles this user has. The database
	// role strings are subject to the PostgreSQL naming conventions.
	DatabaseRoles []string `json:"databaseRoles,omitempty"`
	// KeepExtraRoles: Input only. If the user already exists and it has additional
	// roles, keep them granted.
	KeepExtraRoles bool `json:"keepExtraRoles,omitempty"`
	// Name: Output only. Name of the resource in the form of
	// projects/{project}/locations/{location}/cluster/{cluster}/users/{user}.
	Name string `json:"name,omitempty"`
	// Password: Input only. Password for the user.
	Password string `json:"password,omitempty"`
	// UserType: Optional. Type of this user.
	//
	// Possible values:
	//   "USER_TYPE_UNSPECIFIED" - Unspecified user type.
	//   "ALLOYDB_BUILT_IN" - The default user type that authenticates via
	// password-based authentication.
	//   "ALLOYDB_IAM_USER" - Database user that can authenticate via IAM-Based
	// authentication.
	UserType string `json:"userType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DatabaseRoles") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DatabaseRoles") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

User: Message describing User object.

func (User) MarshalJSON ¶
func (s User) MarshalJSON() ([]byte, error)
type UserPassword ¶
type UserPassword struct {
	// Password: The initial password for the user.
	Password string `json:"password,omitempty"`
	// User: The database username.
	User string `json:"user,omitempty"`
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

UserPassword: The username/password for a database user. Used for specifying initial users at cluster creation time.

func (UserPassword) MarshalJSON ¶
func (s UserPassword) MarshalJSON() ([]byte, error)
type WeeklySchedule ¶
type WeeklySchedule struct {
	// DaysOfWeek: The days of the week to perform a backup. If this field is left
	// empty, the default of every day of the week is used.
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
	// StartTimes: The times during the day to start a backup. The start times are
	// assumed to be in UTC and to be an exact hour (e.g., 04:00:00). If no start
	// times are provided, a single fixed start time is chosen arbitrarily.
	StartTimes []*GoogleTypeTimeOfDay `json:"startTimes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DaysOfWeek") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DaysOfWeek") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WeeklySchedule: A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week. The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element "22:00" and the `days_of_week` field to have all seven days of the week.

func (WeeklySchedule) MarshalJSON ¶
func (s WeeklySchedule) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
alloydb-gen.go
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
