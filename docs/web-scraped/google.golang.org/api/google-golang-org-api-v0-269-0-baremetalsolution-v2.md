# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/baremetalsolution/v2

Title: baremetalsolution package - google.golang.org/api/baremetalsolution/v2 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/baremetalsolution/v2

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
baremetalsolution
 
v2
baremetalsolution
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

Package baremetalsolution provides access to the Bare Metal Solution API.

For product documentation, see: https://cloud.google.com/bare-metal

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/baremetalsolution/v2"
...
ctx := context.Background()
baremetalsolutionService, err := baremetalsolution.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

baremetalsolutionService, err := baremetalsolution.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
baremetalsolutionService, err := baremetalsolution.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AllowedClient
func (s AllowedClient) MarshalJSON() ([]byte, error)
type DetachLunRequest
func (s DetachLunRequest) MarshalJSON() ([]byte, error)
type DisableHyperthreadingRequest
type DisableInteractiveSerialConsoleRequest
type DisableInteractiveSerialConsoleResponse
type Empty
type EnableHyperthreadingRequest
type EnableInteractiveSerialConsoleRequest
type EnableInteractiveSerialConsoleResponse
type EvictLunRequest
type EvictVolumeRequest
type GoogleCloudBaremetalsolutionV2LogicalInterface
func (s GoogleCloudBaremetalsolutionV2LogicalInterface) MarshalJSON() ([]byte, error)
type GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface
func (s GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface) MarshalJSON() ([]byte, error)
type Instance
func (s Instance) MarshalJSON() ([]byte, error)
type InstanceConfig
func (s InstanceConfig) MarshalJSON() ([]byte, error)
type InstanceQuota
func (s InstanceQuota) MarshalJSON() ([]byte, error)
type IntakeVlanAttachment
func (s IntakeVlanAttachment) MarshalJSON() ([]byte, error)
type ListInstancesResponse
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
type ListLocationsResponse
func (s ListLocationsResponse) MarshalJSON() ([]byte, error)
type ListLunsResponse
func (s ListLunsResponse) MarshalJSON() ([]byte, error)
type ListNetworkUsageResponse
func (s ListNetworkUsageResponse) MarshalJSON() ([]byte, error)
type ListNetworksResponse
func (s ListNetworksResponse) MarshalJSON() ([]byte, error)
type ListNfsSharesResponse
func (s ListNfsSharesResponse) MarshalJSON() ([]byte, error)
type ListOSImagesResponse
func (s ListOSImagesResponse) MarshalJSON() ([]byte, error)
type ListProvisioningQuotasResponse
func (s ListProvisioningQuotasResponse) MarshalJSON() ([]byte, error)
type ListSSHKeysResponse
func (s ListSSHKeysResponse) MarshalJSON() ([]byte, error)
type ListVolumeSnapshotsResponse
func (s ListVolumeSnapshotsResponse) MarshalJSON() ([]byte, error)
type ListVolumesResponse
func (s ListVolumesResponse) MarshalJSON() ([]byte, error)
type LoadInstanceAuthInfoResponse
func (s LoadInstanceAuthInfoResponse) MarshalJSON() ([]byte, error)
type Location
func (s Location) MarshalJSON() ([]byte, error)
type LogicalNetworkInterface
func (s LogicalNetworkInterface) MarshalJSON() ([]byte, error)
type Lun
func (s Lun) MarshalJSON() ([]byte, error)
type LunRange
func (s LunRange) MarshalJSON() ([]byte, error)
type Network
func (s Network) MarshalJSON() ([]byte, error)
type NetworkAddress
func (s NetworkAddress) MarshalJSON() ([]byte, error)
type NetworkAddressReservation
func (s NetworkAddressReservation) MarshalJSON() ([]byte, error)
type NetworkConfig
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type NetworkMountPoint
func (s NetworkMountPoint) MarshalJSON() ([]byte, error)
type NetworkUsage
func (s NetworkUsage) MarshalJSON() ([]byte, error)
type NfsExport
func (s NfsExport) MarshalJSON() ([]byte, error)
type NfsShare
func (s NfsShare) MarshalJSON() ([]byte, error)
type OSImage
func (s OSImage) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsInstancesDetachLunCall
func (c *ProjectsLocationsInstancesDetachLunCall) Context(ctx context.Context) *ProjectsLocationsInstancesDetachLunCall
func (c *ProjectsLocationsInstancesDetachLunCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesDetachLunCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDetachLunCall
func (c *ProjectsLocationsInstancesDetachLunCall) Header() http.Header
type ProjectsLocationsInstancesDisableHyperthreadingCall
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Context(ctx context.Context) *ProjectsLocationsInstancesDisableHyperthreadingCall
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDisableHyperthreadingCall
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Header() http.Header
type ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Context(ctx context.Context) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Header() http.Header
type ProjectsLocationsInstancesEnableHyperthreadingCall
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Context(ctx context.Context) *ProjectsLocationsInstancesEnableHyperthreadingCall
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesEnableHyperthreadingCall
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Header() http.Header
type ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Context(ctx context.Context) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Header() http.Header
type ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsLocationsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetCall
func (c *ProjectsLocationsInstancesGetCall) Header() http.Header
func (c *ProjectsLocationsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetCall
type ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) Context(ctx context.Context) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)
func (c *ProjectsLocationsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) Filter(filter string) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) Header() http.Header
func (c *ProjectsLocationsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) PageToken(pageToken string) *ProjectsLocationsInstancesListCall
func (c *ProjectsLocationsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error
type ProjectsLocationsInstancesLoadAuthInfoCall
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Context(ctx context.Context) *ProjectsLocationsInstancesLoadAuthInfoCall
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Do(opts ...googleapi.CallOption) (*LoadInstanceAuthInfoResponse, error)
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesLoadAuthInfoCall
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Header() http.Header
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesLoadAuthInfoCall
type ProjectsLocationsInstancesPatchCall
func (c *ProjectsLocationsInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsInstancesPatchCall
func (c *ProjectsLocationsInstancesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesPatchCall
func (c *ProjectsLocationsInstancesPatchCall) Header() http.Header
func (c *ProjectsLocationsInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsInstancesPatchCall
type ProjectsLocationsInstancesReimageCall
func (c *ProjectsLocationsInstancesReimageCall) Context(ctx context.Context) *ProjectsLocationsInstancesReimageCall
func (c *ProjectsLocationsInstancesReimageCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesReimageCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesReimageCall
func (c *ProjectsLocationsInstancesReimageCall) Header() http.Header
type ProjectsLocationsInstancesRenameCall
func (c *ProjectsLocationsInstancesRenameCall) Context(ctx context.Context) *ProjectsLocationsInstancesRenameCall
func (c *ProjectsLocationsInstancesRenameCall) Do(opts ...googleapi.CallOption) (*Instance, error)
func (c *ProjectsLocationsInstancesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesRenameCall
func (c *ProjectsLocationsInstancesRenameCall) Header() http.Header
type ProjectsLocationsInstancesResetCall
func (c *ProjectsLocationsInstancesResetCall) Context(ctx context.Context) *ProjectsLocationsInstancesResetCall
func (c *ProjectsLocationsInstancesResetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesResetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesResetCall
func (c *ProjectsLocationsInstancesResetCall) Header() http.Header
type ProjectsLocationsInstancesService
func NewProjectsLocationsInstancesService(s *Service) *ProjectsLocationsInstancesService
func (r *ProjectsLocationsInstancesService) DetachLun(instance string, detachlunrequest *DetachLunRequest) *ProjectsLocationsInstancesDetachLunCall
func (r *ProjectsLocationsInstancesService) DisableHyperthreading(name string, disablehyperthreadingrequest *DisableHyperthreadingRequest) *ProjectsLocationsInstancesDisableHyperthreadingCall
func (r *ProjectsLocationsInstancesService) DisableInteractiveSerialConsole(name string, ...) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall
func (r *ProjectsLocationsInstancesService) EnableHyperthreading(name string, enablehyperthreadingrequest *EnableHyperthreadingRequest) *ProjectsLocationsInstancesEnableHyperthreadingCall
func (r *ProjectsLocationsInstancesService) EnableInteractiveSerialConsole(name string, ...) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall
func (r *ProjectsLocationsInstancesService) Get(name string) *ProjectsLocationsInstancesGetCall
func (r *ProjectsLocationsInstancesService) List(parent string) *ProjectsLocationsInstancesListCall
func (r *ProjectsLocationsInstancesService) LoadAuthInfo(name string) *ProjectsLocationsInstancesLoadAuthInfoCall
func (r *ProjectsLocationsInstancesService) Patch(name string, instance *Instance) *ProjectsLocationsInstancesPatchCall
func (r *ProjectsLocationsInstancesService) Reimage(name string, reimageinstancerequest *ReimageInstanceRequest) *ProjectsLocationsInstancesReimageCall
func (r *ProjectsLocationsInstancesService) Rename(name string, renameinstancerequest *RenameInstanceRequest) *ProjectsLocationsInstancesRenameCall
func (r *ProjectsLocationsInstancesService) Reset(name string, resetinstancerequest *ResetInstanceRequest) *ProjectsLocationsInstancesResetCall
func (r *ProjectsLocationsInstancesService) Start(name string, startinstancerequest *StartInstanceRequest) *ProjectsLocationsInstancesStartCall
func (r *ProjectsLocationsInstancesService) Stop(name string, stopinstancerequest *StopInstanceRequest) *ProjectsLocationsInstancesStopCall
type ProjectsLocationsInstancesStartCall
func (c *ProjectsLocationsInstancesStartCall) Context(ctx context.Context) *ProjectsLocationsInstancesStartCall
func (c *ProjectsLocationsInstancesStartCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesStartCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesStartCall
func (c *ProjectsLocationsInstancesStartCall) Header() http.Header
type ProjectsLocationsInstancesStopCall
func (c *ProjectsLocationsInstancesStopCall) Context(ctx context.Context) *ProjectsLocationsInstancesStopCall
func (c *ProjectsLocationsInstancesStopCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsInstancesStopCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesStopCall
func (c *ProjectsLocationsInstancesStopCall) Header() http.Header
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
type ProjectsLocationsNetworksGetCall
func (c *ProjectsLocationsNetworksGetCall) Context(ctx context.Context) *ProjectsLocationsNetworksGetCall
func (c *ProjectsLocationsNetworksGetCall) Do(opts ...googleapi.CallOption) (*Network, error)
func (c *ProjectsLocationsNetworksGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksGetCall
func (c *ProjectsLocationsNetworksGetCall) Header() http.Header
func (c *ProjectsLocationsNetworksGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksGetCall
type ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) Context(ctx context.Context) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) Do(opts ...googleapi.CallOption) (*ListNetworksResponse, error)
func (c *ProjectsLocationsNetworksListCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) Filter(filter string) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) Header() http.Header
func (c *ProjectsLocationsNetworksListCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) PageSize(pageSize int64) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) PageToken(pageToken string) *ProjectsLocationsNetworksListCall
func (c *ProjectsLocationsNetworksListCall) Pages(ctx context.Context, f func(*ListNetworksResponse) error) error
type ProjectsLocationsNetworksListNetworkUsageCall
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Context(ctx context.Context) *ProjectsLocationsNetworksListNetworkUsageCall
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Do(opts ...googleapi.CallOption) (*ListNetworkUsageResponse, error)
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksListNetworkUsageCall
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Header() http.Header
func (c *ProjectsLocationsNetworksListNetworkUsageCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksListNetworkUsageCall
type ProjectsLocationsNetworksPatchCall
func (c *ProjectsLocationsNetworksPatchCall) Context(ctx context.Context) *ProjectsLocationsNetworksPatchCall
func (c *ProjectsLocationsNetworksPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsNetworksPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksPatchCall
func (c *ProjectsLocationsNetworksPatchCall) Header() http.Header
func (c *ProjectsLocationsNetworksPatchCall) UpdateMask(updateMask string) *ProjectsLocationsNetworksPatchCall
type ProjectsLocationsNetworksRenameCall
func (c *ProjectsLocationsNetworksRenameCall) Context(ctx context.Context) *ProjectsLocationsNetworksRenameCall
func (c *ProjectsLocationsNetworksRenameCall) Do(opts ...googleapi.CallOption) (*Network, error)
func (c *ProjectsLocationsNetworksRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksRenameCall
func (c *ProjectsLocationsNetworksRenameCall) Header() http.Header
type ProjectsLocationsNetworksService
func NewProjectsLocationsNetworksService(s *Service) *ProjectsLocationsNetworksService
func (r *ProjectsLocationsNetworksService) Get(name string) *ProjectsLocationsNetworksGetCall
func (r *ProjectsLocationsNetworksService) List(parent string) *ProjectsLocationsNetworksListCall
func (r *ProjectsLocationsNetworksService) ListNetworkUsage(location string) *ProjectsLocationsNetworksListNetworkUsageCall
func (r *ProjectsLocationsNetworksService) Patch(name string, network *Network) *ProjectsLocationsNetworksPatchCall
func (r *ProjectsLocationsNetworksService) Rename(name string, renamenetworkrequest *RenameNetworkRequest) *ProjectsLocationsNetworksRenameCall
type ProjectsLocationsNfsSharesCreateCall
func (c *ProjectsLocationsNfsSharesCreateCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesCreateCall
func (c *ProjectsLocationsNfsSharesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsNfsSharesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesCreateCall
func (c *ProjectsLocationsNfsSharesCreateCall) Header() http.Header
type ProjectsLocationsNfsSharesDeleteCall
func (c *ProjectsLocationsNfsSharesDeleteCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesDeleteCall
func (c *ProjectsLocationsNfsSharesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsNfsSharesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesDeleteCall
func (c *ProjectsLocationsNfsSharesDeleteCall) Header() http.Header
type ProjectsLocationsNfsSharesGetCall
func (c *ProjectsLocationsNfsSharesGetCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesGetCall
func (c *ProjectsLocationsNfsSharesGetCall) Do(opts ...googleapi.CallOption) (*NfsShare, error)
func (c *ProjectsLocationsNfsSharesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesGetCall
func (c *ProjectsLocationsNfsSharesGetCall) Header() http.Header
func (c *ProjectsLocationsNfsSharesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsNfsSharesGetCall
type ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) Do(opts ...googleapi.CallOption) (*ListNfsSharesResponse, error)
func (c *ProjectsLocationsNfsSharesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) Filter(filter string) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) Header() http.Header
func (c *ProjectsLocationsNfsSharesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) PageSize(pageSize int64) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) PageToken(pageToken string) *ProjectsLocationsNfsSharesListCall
func (c *ProjectsLocationsNfsSharesListCall) Pages(ctx context.Context, f func(*ListNfsSharesResponse) error) error
type ProjectsLocationsNfsSharesPatchCall
func (c *ProjectsLocationsNfsSharesPatchCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesPatchCall
func (c *ProjectsLocationsNfsSharesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsNfsSharesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesPatchCall
func (c *ProjectsLocationsNfsSharesPatchCall) Header() http.Header
func (c *ProjectsLocationsNfsSharesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsNfsSharesPatchCall
type ProjectsLocationsNfsSharesRenameCall
func (c *ProjectsLocationsNfsSharesRenameCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesRenameCall
func (c *ProjectsLocationsNfsSharesRenameCall) Do(opts ...googleapi.CallOption) (*NfsShare, error)
func (c *ProjectsLocationsNfsSharesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesRenameCall
func (c *ProjectsLocationsNfsSharesRenameCall) Header() http.Header
type ProjectsLocationsNfsSharesService
func NewProjectsLocationsNfsSharesService(s *Service) *ProjectsLocationsNfsSharesService
func (r *ProjectsLocationsNfsSharesService) Create(parent string, nfsshare *NfsShare) *ProjectsLocationsNfsSharesCreateCall
func (r *ProjectsLocationsNfsSharesService) Delete(name string) *ProjectsLocationsNfsSharesDeleteCall
func (r *ProjectsLocationsNfsSharesService) Get(name string) *ProjectsLocationsNfsSharesGetCall
func (r *ProjectsLocationsNfsSharesService) List(parent string) *ProjectsLocationsNfsSharesListCall
func (r *ProjectsLocationsNfsSharesService) Patch(name string, nfsshare *NfsShare) *ProjectsLocationsNfsSharesPatchCall
func (r *ProjectsLocationsNfsSharesService) Rename(name string, renamenfssharerequest *RenameNfsShareRequest) *ProjectsLocationsNfsSharesRenameCall
type ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOsImagesGetCall
func (c *ProjectsLocationsOsImagesGetCall) Context(ctx context.Context) *ProjectsLocationsOsImagesGetCall
func (c *ProjectsLocationsOsImagesGetCall) Do(opts ...googleapi.CallOption) (*OSImage, error)
func (c *ProjectsLocationsOsImagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOsImagesGetCall
func (c *ProjectsLocationsOsImagesGetCall) Header() http.Header
func (c *ProjectsLocationsOsImagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOsImagesGetCall
type ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) Context(ctx context.Context) *ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) Do(opts ...googleapi.CallOption) (*ListOSImagesResponse, error)
func (c *ProjectsLocationsOsImagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) Header() http.Header
func (c *ProjectsLocationsOsImagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) PageSize(pageSize int64) *ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) PageToken(pageToken string) *ProjectsLocationsOsImagesListCall
func (c *ProjectsLocationsOsImagesListCall) Pages(ctx context.Context, f func(*ListOSImagesResponse) error) error
type ProjectsLocationsOsImagesService
func NewProjectsLocationsOsImagesService(s *Service) *ProjectsLocationsOsImagesService
func (r *ProjectsLocationsOsImagesService) Get(name string) *ProjectsLocationsOsImagesGetCall
func (r *ProjectsLocationsOsImagesService) List(parent string) *ProjectsLocationsOsImagesListCall
type ProjectsLocationsProvisioningConfigsCreateCall
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsCreateCall
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Email(email string) *ProjectsLocationsProvisioningConfigsCreateCall
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsCreateCall
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Header() http.Header
type ProjectsLocationsProvisioningConfigsGetCall
func (c *ProjectsLocationsProvisioningConfigsGetCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsGetCall
func (c *ProjectsLocationsProvisioningConfigsGetCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)
func (c *ProjectsLocationsProvisioningConfigsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsGetCall
func (c *ProjectsLocationsProvisioningConfigsGetCall) Header() http.Header
func (c *ProjectsLocationsProvisioningConfigsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsProvisioningConfigsGetCall
type ProjectsLocationsProvisioningConfigsPatchCall
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsPatchCall
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Email(email string) *ProjectsLocationsProvisioningConfigsPatchCall
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsPatchCall
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Header() http.Header
func (c *ProjectsLocationsProvisioningConfigsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsProvisioningConfigsPatchCall
type ProjectsLocationsProvisioningConfigsService
func NewProjectsLocationsProvisioningConfigsService(s *Service) *ProjectsLocationsProvisioningConfigsService
func (r *ProjectsLocationsProvisioningConfigsService) Create(parent string, provisioningconfig *ProvisioningConfig) *ProjectsLocationsProvisioningConfigsCreateCall
func (r *ProjectsLocationsProvisioningConfigsService) Get(name string) *ProjectsLocationsProvisioningConfigsGetCall
func (r *ProjectsLocationsProvisioningConfigsService) Patch(name string, provisioningconfig *ProvisioningConfig) *ProjectsLocationsProvisioningConfigsPatchCall
func (r *ProjectsLocationsProvisioningConfigsService) Submit(parent string, ...) *ProjectsLocationsProvisioningConfigsSubmitCall
type ProjectsLocationsProvisioningConfigsSubmitCall
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsSubmitCall
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Do(opts ...googleapi.CallOption) (*SubmitProvisioningConfigResponse, error)
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsSubmitCall
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Header() http.Header
type ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) Context(ctx context.Context) *ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) Do(opts ...googleapi.CallOption) (*ListProvisioningQuotasResponse, error)
func (c *ProjectsLocationsProvisioningQuotasListCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) Header() http.Header
func (c *ProjectsLocationsProvisioningQuotasListCall) IfNoneMatch(entityTag string) *ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) PageSize(pageSize int64) *ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) PageToken(pageToken string) *ProjectsLocationsProvisioningQuotasListCall
func (c *ProjectsLocationsProvisioningQuotasListCall) Pages(ctx context.Context, f func(*ListProvisioningQuotasResponse) error) error
type ProjectsLocationsProvisioningQuotasService
func NewProjectsLocationsProvisioningQuotasService(s *Service) *ProjectsLocationsProvisioningQuotasService
func (r *ProjectsLocationsProvisioningQuotasService) List(parent string) *ProjectsLocationsProvisioningQuotasListCall
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsLocationsSshKeysCreateCall
func (c *ProjectsLocationsSshKeysCreateCall) Context(ctx context.Context) *ProjectsLocationsSshKeysCreateCall
func (c *ProjectsLocationsSshKeysCreateCall) Do(opts ...googleapi.CallOption) (*SSHKey, error)
func (c *ProjectsLocationsSshKeysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysCreateCall
func (c *ProjectsLocationsSshKeysCreateCall) Header() http.Header
func (c *ProjectsLocationsSshKeysCreateCall) SshKeyId(sshKeyId string) *ProjectsLocationsSshKeysCreateCall
type ProjectsLocationsSshKeysDeleteCall
func (c *ProjectsLocationsSshKeysDeleteCall) Context(ctx context.Context) *ProjectsLocationsSshKeysDeleteCall
func (c *ProjectsLocationsSshKeysDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsSshKeysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysDeleteCall
func (c *ProjectsLocationsSshKeysDeleteCall) Header() http.Header
type ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) Context(ctx context.Context) *ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) Do(opts ...googleapi.CallOption) (*ListSSHKeysResponse, error)
func (c *ProjectsLocationsSshKeysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) Header() http.Header
func (c *ProjectsLocationsSshKeysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) PageSize(pageSize int64) *ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) PageToken(pageToken string) *ProjectsLocationsSshKeysListCall
func (c *ProjectsLocationsSshKeysListCall) Pages(ctx context.Context, f func(*ListSSHKeysResponse) error) error
type ProjectsLocationsSshKeysService
func NewProjectsLocationsSshKeysService(s *Service) *ProjectsLocationsSshKeysService
func (r *ProjectsLocationsSshKeysService) Create(parent string, sshkey *SSHKey) *ProjectsLocationsSshKeysCreateCall
func (r *ProjectsLocationsSshKeysService) Delete(name string) *ProjectsLocationsSshKeysDeleteCall
func (r *ProjectsLocationsSshKeysService) List(parent string) *ProjectsLocationsSshKeysListCall
type ProjectsLocationsVolumesEvictCall
func (c *ProjectsLocationsVolumesEvictCall) Context(ctx context.Context) *ProjectsLocationsVolumesEvictCall
func (c *ProjectsLocationsVolumesEvictCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsVolumesEvictCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesEvictCall
func (c *ProjectsLocationsVolumesEvictCall) Header() http.Header
type ProjectsLocationsVolumesGetCall
func (c *ProjectsLocationsVolumesGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesGetCall
func (c *ProjectsLocationsVolumesGetCall) Do(opts ...googleapi.CallOption) (*Volume, error)
func (c *ProjectsLocationsVolumesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesGetCall
func (c *ProjectsLocationsVolumesGetCall) Header() http.Header
func (c *ProjectsLocationsVolumesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesGetCall
type ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) Context(ctx context.Context) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) Do(opts ...googleapi.CallOption) (*ListVolumesResponse, error)
func (c *ProjectsLocationsVolumesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) Filter(filter string) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) Header() http.Header
func (c *ProjectsLocationsVolumesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) PageToken(pageToken string) *ProjectsLocationsVolumesListCall
func (c *ProjectsLocationsVolumesListCall) Pages(ctx context.Context, f func(*ListVolumesResponse) error) error
type ProjectsLocationsVolumesLunsEvictCall
func (c *ProjectsLocationsVolumesLunsEvictCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsEvictCall
func (c *ProjectsLocationsVolumesLunsEvictCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsVolumesLunsEvictCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsEvictCall
func (c *ProjectsLocationsVolumesLunsEvictCall) Header() http.Header
type ProjectsLocationsVolumesLunsGetCall
func (c *ProjectsLocationsVolumesLunsGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsGetCall
func (c *ProjectsLocationsVolumesLunsGetCall) Do(opts ...googleapi.CallOption) (*Lun, error)
func (c *ProjectsLocationsVolumesLunsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsGetCall
func (c *ProjectsLocationsVolumesLunsGetCall) Header() http.Header
func (c *ProjectsLocationsVolumesLunsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesLunsGetCall
type ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) Do(opts ...googleapi.CallOption) (*ListLunsResponse, error)
func (c *ProjectsLocationsVolumesLunsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) Header() http.Header
func (c *ProjectsLocationsVolumesLunsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) PageToken(pageToken string) *ProjectsLocationsVolumesLunsListCall
func (c *ProjectsLocationsVolumesLunsListCall) Pages(ctx context.Context, f func(*ListLunsResponse) error) error
type ProjectsLocationsVolumesLunsService
func NewProjectsLocationsVolumesLunsService(s *Service) *ProjectsLocationsVolumesLunsService
func (r *ProjectsLocationsVolumesLunsService) Evict(name string, evictlunrequest *EvictLunRequest) *ProjectsLocationsVolumesLunsEvictCall
func (r *ProjectsLocationsVolumesLunsService) Get(name string) *ProjectsLocationsVolumesLunsGetCall
func (r *ProjectsLocationsVolumesLunsService) List(parent string) *ProjectsLocationsVolumesLunsListCall
type ProjectsLocationsVolumesPatchCall
func (c *ProjectsLocationsVolumesPatchCall) Context(ctx context.Context) *ProjectsLocationsVolumesPatchCall
func (c *ProjectsLocationsVolumesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsVolumesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesPatchCall
func (c *ProjectsLocationsVolumesPatchCall) Header() http.Header
func (c *ProjectsLocationsVolumesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsVolumesPatchCall
type ProjectsLocationsVolumesRenameCall
func (c *ProjectsLocationsVolumesRenameCall) Context(ctx context.Context) *ProjectsLocationsVolumesRenameCall
func (c *ProjectsLocationsVolumesRenameCall) Do(opts ...googleapi.CallOption) (*Volume, error)
func (c *ProjectsLocationsVolumesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesRenameCall
func (c *ProjectsLocationsVolumesRenameCall) Header() http.Header
type ProjectsLocationsVolumesResizeCall
func (c *ProjectsLocationsVolumesResizeCall) Context(ctx context.Context) *ProjectsLocationsVolumesResizeCall
func (c *ProjectsLocationsVolumesResizeCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsVolumesResizeCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesResizeCall
func (c *ProjectsLocationsVolumesResizeCall) Header() http.Header
type ProjectsLocationsVolumesService
func NewProjectsLocationsVolumesService(s *Service) *ProjectsLocationsVolumesService
func (r *ProjectsLocationsVolumesService) Evict(name string, evictvolumerequest *EvictVolumeRequest) *ProjectsLocationsVolumesEvictCall
func (r *ProjectsLocationsVolumesService) Get(name string) *ProjectsLocationsVolumesGetCall
func (r *ProjectsLocationsVolumesService) List(parent string) *ProjectsLocationsVolumesListCall
func (r *ProjectsLocationsVolumesService) Patch(name string, volume *Volume) *ProjectsLocationsVolumesPatchCall
func (r *ProjectsLocationsVolumesService) Rename(name string, renamevolumerequest *RenameVolumeRequest) *ProjectsLocationsVolumesRenameCall
func (r *ProjectsLocationsVolumesService) Resize(volume string, resizevolumerequest *ResizeVolumeRequest) *ProjectsLocationsVolumesResizeCall
type ProjectsLocationsVolumesSnapshotsCreateCall
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsCreateCall
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Do(opts ...googleapi.CallOption) (*VolumeSnapshot, error)
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsCreateCall
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Header() http.Header
type ProjectsLocationsVolumesSnapshotsDeleteCall
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsDeleteCall
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsDeleteCall
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Header() http.Header
type ProjectsLocationsVolumesSnapshotsGetCall
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsGetCall
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Do(opts ...googleapi.CallOption) (*VolumeSnapshot, error)
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsGetCall
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Header() http.Header
func (c *ProjectsLocationsVolumesSnapshotsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesSnapshotsGetCall
type ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) Do(opts ...googleapi.CallOption) (*ListVolumeSnapshotsResponse, error)
func (c *ProjectsLocationsVolumesSnapshotsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) Header() http.Header
func (c *ProjectsLocationsVolumesSnapshotsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) PageToken(pageToken string) *ProjectsLocationsVolumesSnapshotsListCall
func (c *ProjectsLocationsVolumesSnapshotsListCall) Pages(ctx context.Context, f func(*ListVolumeSnapshotsResponse) error) error
type ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Header() http.Header
type ProjectsLocationsVolumesSnapshotsService
func NewProjectsLocationsVolumesSnapshotsService(s *Service) *ProjectsLocationsVolumesSnapshotsService
func (r *ProjectsLocationsVolumesSnapshotsService) Create(parent string, volumesnapshot *VolumeSnapshot) *ProjectsLocationsVolumesSnapshotsCreateCall
func (r *ProjectsLocationsVolumesSnapshotsService) Delete(name string) *ProjectsLocationsVolumesSnapshotsDeleteCall
func (r *ProjectsLocationsVolumesSnapshotsService) Get(name string) *ProjectsLocationsVolumesSnapshotsGetCall
func (r *ProjectsLocationsVolumesSnapshotsService) List(parent string) *ProjectsLocationsVolumesSnapshotsListCall
func (r *ProjectsLocationsVolumesSnapshotsService) RestoreVolumeSnapshot(volumeSnapshot string, ...) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type ProvisioningConfig
func (s ProvisioningConfig) MarshalJSON() ([]byte, error)
type ProvisioningQuota
func (s ProvisioningQuota) MarshalJSON() ([]byte, error)
type QosPolicy
func (s QosPolicy) MarshalJSON() ([]byte, error)
func (s *QosPolicy) UnmarshalJSON(data []byte) error
type ReimageInstanceRequest
func (s ReimageInstanceRequest) MarshalJSON() ([]byte, error)
type RenameInstanceRequest
func (s RenameInstanceRequest) MarshalJSON() ([]byte, error)
type RenameNetworkRequest
func (s RenameNetworkRequest) MarshalJSON() ([]byte, error)
type RenameNfsShareRequest
func (s RenameNfsShareRequest) MarshalJSON() ([]byte, error)
type RenameVolumeRequest
func (s RenameVolumeRequest) MarshalJSON() ([]byte, error)
type ResetInstanceRequest
type ResetInstanceResponse
type ResizeVolumeRequest
func (s ResizeVolumeRequest) MarshalJSON() ([]byte, error)
type RestoreVolumeSnapshotRequest
type SSHKey
func (s SSHKey) MarshalJSON() ([]byte, error)
type ServerNetworkTemplate
func (s ServerNetworkTemplate) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SnapshotReservationDetail
func (s SnapshotReservationDetail) MarshalJSON() ([]byte, error)
type StartInstanceRequest
type StartInstanceResponse
type Status
func (s Status) MarshalJSON() ([]byte, error)
type StopInstanceRequest
type StopInstanceResponse
type SubmitProvisioningConfigRequest
func (s SubmitProvisioningConfigRequest) MarshalJSON() ([]byte, error)
type SubmitProvisioningConfigResponse
func (s SubmitProvisioningConfigResponse) MarshalJSON() ([]byte, error)
type UserAccount
func (s UserAccount) MarshalJSON() ([]byte, error)
type VRF
func (s VRF) MarshalJSON() ([]byte, error)
type VlanAttachment
func (s VlanAttachment) MarshalJSON() ([]byte, error)
type Volume
func (s Volume) MarshalJSON() ([]byte, error)
type VolumeConfig
func (s VolumeConfig) MarshalJSON() ([]byte, error)
type VolumeSnapshot
func (s VolumeSnapshot) MarshalJSON() ([]byte, error)
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
type AllowedClient ¶
added in v0.69.0
type AllowedClient struct {
	// AllowDev: Allow dev flag. Which controls whether to allow creation of
	// devices.
	AllowDev bool `json:"allowDev,omitempty"`
	// AllowSuid: Allow the setuid flag.
	AllowSuid bool `json:"allowSuid,omitempty"`
	// AllowedClientsCidr: The subnet of IP addresses permitted to access the
	// share.
	AllowedClientsCidr string `json:"allowedClientsCidr,omitempty"`
	// MountPermissions: Mount permissions.
	//
	// Possible values:
	//   "MOUNT_PERMISSIONS_UNSPECIFIED" - Permissions were not specified.
	//   "READ" - NFS share can be mount with read-only permissions.
	//   "READ_WRITE" - NFS share can be mount with read-write permissions.
	MountPermissions string `json:"mountPermissions,omitempty"`
	// Network: The network the access point sits on.
	Network string `json:"network,omitempty"`
	// NfsPath: Output only. The path to access NFS, in format shareIP:/InstanceID
	// InstanceID is the generated ID instead of customer provided name. example
	// like "10.0.0.0:/g123456789-nfs001"
	NfsPath string `json:"nfsPath,omitempty"`
	// NoRootSquash: Disable root squashing, which is a feature of NFS. Root squash
	// is a special mapping of the remote superuser (root) identity when using
	// identity authentication.
	NoRootSquash bool `json:"noRootSquash,omitempty"`
	// ShareIp: Output only. The IP address of the share on this network. Assigned
	// automatically during provisioning based on the network's services_cidr.
	ShareIp string `json:"shareIp,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowDev") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowDev") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AllowedClient: Represents an 'access point' for the share.

func (AllowedClient) MarshalJSON ¶
added in v0.69.0
func (s AllowedClient) MarshalJSON() ([]byte, error)
type DetachLunRequest ¶
added in v0.79.0
type DetachLunRequest struct {
	// Lun: Required. Name of the Lun to detach.
	Lun string `json:"lun,omitempty"`
	// SkipReboot: If true, performs lun unmapping without instance reboot.
	SkipReboot bool `json:"skipReboot,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Lun") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Lun") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DetachLunRequest: Message for detach specific LUN from an Instance.

func (DetachLunRequest) MarshalJSON ¶
added in v0.79.0
func (s DetachLunRequest) MarshalJSON() ([]byte, error)
type DisableHyperthreadingRequest ¶
added in v0.178.0
type DisableHyperthreadingRequest struct {
}

DisableHyperthreadingRequest: Message requesting to perform disable hyperthreading operation on a server.

type DisableInteractiveSerialConsoleRequest ¶
added in v0.98.0
type DisableInteractiveSerialConsoleRequest struct {
}

DisableInteractiveSerialConsoleRequest: Message for disabling the interactive serial console on an instance.

type DisableInteractiveSerialConsoleResponse ¶
added in v0.137.0
type DisableInteractiveSerialConsoleResponse struct {
}

DisableInteractiveSerialConsoleResponse: Message for response of DisableInteractiveSerialConsole.

type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EnableHyperthreadingRequest ¶
added in v0.178.0
type EnableHyperthreadingRequest struct {
}

EnableHyperthreadingRequest: Message requesting to perform enable hyperthreading operation on a server.

type EnableInteractiveSerialConsoleRequest ¶
added in v0.98.0
type EnableInteractiveSerialConsoleRequest struct {
}

EnableInteractiveSerialConsoleRequest: Message for enabling the interactive serial console on an instance.

type EnableInteractiveSerialConsoleResponse ¶
added in v0.137.0
type EnableInteractiveSerialConsoleResponse struct {
}

EnableInteractiveSerialConsoleResponse: Message for response of EnableInteractiveSerialConsole.

type EvictLunRequest ¶
added in v0.111.0
type EvictLunRequest struct {
}

EvictLunRequest: Request for skip lun cooloff and delete it.

type EvictVolumeRequest ¶
added in v0.111.0
type EvictVolumeRequest struct {
}

EvictVolumeRequest: Request for skip volume cooloff and delete it.

type GoogleCloudBaremetalsolutionV2LogicalInterface ¶
added in v0.82.0
type GoogleCloudBaremetalsolutionV2LogicalInterface struct {
	// InterfaceIndex: The index of the logical interface mapping to the index of
	// the hardware bond or nic on the chosen network template. This field is
	// deprecated.
	InterfaceIndex int64 `json:"interfaceIndex,omitempty"`
	// LogicalNetworkInterfaces: List of logical network interfaces within a
	// logical interface.
	LogicalNetworkInterfaces []*LogicalNetworkInterface `json:"logicalNetworkInterfaces,omitempty"`
	// Name: Interface name. This is of syntax or and forms part of the network
	// template name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InterfaceIndex") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InterfaceIndex") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBaremetalsolutionV2LogicalInterface: Each logical interface represents a logical abstraction of the underlying physical interface (for eg. bond, nic) of the instance. Each logical interface can effectively map to multiple network-IP pairs and still be mapped to one underlying physical interface.

func (GoogleCloudBaremetalsolutionV2LogicalInterface) MarshalJSON ¶
added in v0.82.0
func (s GoogleCloudBaremetalsolutionV2LogicalInterface) MarshalJSON() ([]byte, error)
type GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface ¶
added in v0.82.0
type GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface struct {
	// Name: Interface name. This is not a globally unique identifier. Name is
	// unique only inside the ServerNetworkTemplate. This is of syntax or and forms
	// part of the network template name.
	Name string `json:"name,omitempty"`
	// Required: If true, interface must have network connected.
	Required bool `json:"required,omitempty"`
	// Type: Interface type.
	//
	// Possible values:
	//   "INTERFACE_TYPE_UNSPECIFIED" - Unspecified value.
	//   "BOND" - Bond interface type.
	//   "NIC" - NIC interface type.
	Type string `json:"type,omitempty"`
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

GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface: Logical interface.

func (GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface) MarshalJSON ¶
added in v0.82.0
func (s GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface) MarshalJSON() ([]byte, error)
type Instance ¶
type Instance struct {
	// CreateTime: Output only. Create a time stamp.
	CreateTime string `json:"createTime,omitempty"`
	// FirmwareVersion: Output only. The firmware version for the instance.
	FirmwareVersion string `json:"firmwareVersion,omitempty"`
	// HyperthreadingEnabled: True if you enable hyperthreading for the server,
	// otherwise false. The default value is false.
	HyperthreadingEnabled bool `json:"hyperthreadingEnabled,omitempty"`
	// Id: Output only. An identifier for the `Instance`, generated by the backend.
	Id string `json:"id,omitempty"`
	// InteractiveSerialConsoleEnabled: Output only. True if the interactive serial
	// console feature is enabled for the instance, false otherwise. The default
	// value is false.
	InteractiveSerialConsoleEnabled bool `json:"interactiveSerialConsoleEnabled,omitempty"`
	// KmsKeyVersion: Optional. Name of the KMS crypto key version used to encrypt
	// the initial passwords. The key has to have ASYMMETRIC_DECRYPT purpose.
	// Format is
	// `projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/
	// cryptoKeyVersions/{version}`.
	KmsKeyVersion string `json:"kmsKeyVersion,omitempty"`
	// Labels: Labels as key value pairs.
	Labels map[string]string `json:"labels,omitempty"`
	// LogicalInterfaces: List of logical interfaces for the instance. The number
	// of logical interfaces will be the same as number of hardware bond/nic on the
	// chosen network template. For the non-multivlan configurations (for eg,
	// existing servers) that use existing default network template
	// (bondaa-bondaa), both the Instance.networks field and the
	// Instance.logical_interfaces fields will be filled to ensure backward
	// compatibility. For the others, only Instance.logical_interfaces will be
	// filled.
	LogicalInterfaces []*GoogleCloudBaremetalsolutionV2LogicalInterface `json:"logicalInterfaces,omitempty"`
	// LoginInfo: Output only. Text field about info for logging in.
	LoginInfo string `json:"loginInfo,omitempty"`
	// Luns: Immutable. List of LUNs associated with this server.
	Luns []*Lun `json:"luns,omitempty"`
	// MachineType: Immutable. The server type. Available server types
	// (https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations)
	MachineType string `json:"machineType,omitempty"`
	// Name: Immutable. The resource name of this `Instance`. Resource names are
	// schemeless URIs that follow the conventions in
	// https://cloud.google.com/apis/design/resource_names. Format:
	// `projects/{project}/locations/{location}/instances/{instance}`
	Name string `json:"name,omitempty"`
	// NetworkTemplate: Instance network template name. For eg, bondaa-bondaa,
	// bondab-nic, etc. Generally, the template name follows the syntax of "bond"
	// or "nic".
	NetworkTemplate string `json:"networkTemplate,omitempty"`
	// Networks: Output only. List of networks associated with this server.
	Networks []*Network `json:"networks,omitempty"`
	// OsImage: The OS image currently installed on the server.
	OsImage string `json:"osImage,omitempty"`
	// Pod: Immutable. Pod name. Pod is an independent part of infrastructure.
	// Instance can only be connected to the assets (networks, volumes) allocated
	// in the same pod.
	Pod string `json:"pod,omitempty"`
	// SshKeys: Optional. List of SSH Keys used during instance provisioning.
	SshKeys []string `json:"sshKeys,omitempty"`
	// State: Output only. The state of the server.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The server is in an unknown state.
	//   "PROVISIONING" - The server is being provisioned.
	//   "RUNNING" - The server is running.
	//   "DELETED" - The server has been deleted.
	//   "UPDATING" - The server is being updated.
	//   "STARTING" - The server is starting.
	//   "STOPPING" - The server is stopping.
	//   "SHUTDOWN" - The server is shutdown.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. Update a time stamp.
	UpdateTime string `json:"updateTime,omitempty"`
	// Volumes: Input only. List of Volumes to attach to this Instance on creation.
	// This field won't be populated in Get/List responses.
	Volumes []*Volume `json:"volumes,omitempty"`
	// WorkloadProfile: The workload profile for the instance.
	//
	// Possible values:
	//   "WORKLOAD_PROFILE_UNSPECIFIED" - The workload profile is in an unknown
	// state.
	//   "WORKLOAD_PROFILE_GENERIC" - The workload profile is generic.
	//   "WORKLOAD_PROFILE_HANA" - The workload profile is hana.
	WorkloadProfile string `json:"workloadProfile,omitempty"`

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

Instance: A server.

func (Instance) MarshalJSON ¶
func (s Instance) MarshalJSON() ([]byte, error)
type InstanceConfig ¶
added in v0.69.0
type InstanceConfig struct {
	// AccountNetworksEnabled: If true networks can be from different projects of
	// the same vendor account.
	AccountNetworksEnabled bool `json:"accountNetworksEnabled,omitempty"`
	// ClientNetwork: Client network address. Filled if
	// InstanceConfig.multivlan_config is false.
	ClientNetwork *NetworkAddress `json:"clientNetwork,omitempty"`
	// Hyperthreading: Whether the instance should be provisioned with
	// Hyperthreading enabled.
	Hyperthreading bool `json:"hyperthreading,omitempty"`
	// Id: A transient unique identifier to identify an instance within an
	// ProvisioningConfig request.
	Id string `json:"id,omitempty"`
	// InstanceType: Instance type. Available types
	// (https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations)
	InstanceType string `json:"instanceType,omitempty"`
	// KmsKeyVersion: Name of the KMS crypto key version used to encrypt the
	// initial passwords. The key has to have ASYMMETRIC_DECRYPT purpose.
	KmsKeyVersion string `json:"kmsKeyVersion,omitempty"`
	// LogicalInterfaces: List of logical interfaces for the instance. The number
	// of logical interfaces will be the same as number of hardware bond/nic on the
	// chosen network template. Filled if InstanceConfig.multivlan_config is true.
	LogicalInterfaces []*GoogleCloudBaremetalsolutionV2LogicalInterface `json:"logicalInterfaces,omitempty"`
	// Name: The name of the instance config.
	Name string `json:"name,omitempty"`
	// NetworkConfig: The type of network configuration on the instance.
	//
	// Possible values:
	//   "NETWORKCONFIG_UNSPECIFIED" - The unspecified network configuration.
	//   "SINGLE_VLAN" - Instance part of single client network and single private
	// network.
	//   "MULTI_VLAN" - Instance part of multiple (or single) client networks and
	// private networks.
	NetworkConfig string `json:"networkConfig,omitempty"`
	// NetworkTemplate: Server network template name. Filled if
	// InstanceConfig.multivlan_config is true.
	NetworkTemplate string `json:"networkTemplate,omitempty"`
	// OsImage: OS image to initialize the instance. Available images
	// (https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations)
	OsImage string `json:"osImage,omitempty"`
	// PrivateNetwork: Private network address, if any. Filled if
	// InstanceConfig.multivlan_config is false.
	PrivateNetwork *NetworkAddress `json:"privateNetwork,omitempty"`
	// SshKeyNames: Optional. List of names of ssh keys used to provision the
	// instance.
	SshKeyNames []string `json:"sshKeyNames,omitempty"`
	// UserNote: User note field, it can be used by customers to add additional
	// information for the BMS Ops team .
	UserNote string `json:"userNote,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountNetworksEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountNetworksEnabled") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstanceConfig: Configuration parameters for a new instance.

func (InstanceConfig) MarshalJSON ¶
added in v0.69.0
func (s InstanceConfig) MarshalJSON() ([]byte, error)
type InstanceQuota ¶
added in v0.69.0
type InstanceQuota struct {
	// AvailableMachineCount: Number of machines than can be created for the given
	// location and instance_type.
	AvailableMachineCount int64 `json:"availableMachineCount,omitempty"`
	// GcpService: The gcp service of the provisioning quota.
	GcpService string `json:"gcpService,omitempty"`
	// InstanceType: Instance type. Deprecated: use gcp_service.
	InstanceType string `json:"instanceType,omitempty"`
	// Location: Location where the quota applies.
	Location string `json:"location,omitempty"`
	// Name: Output only. The name of the instance quota.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AvailableMachineCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailableMachineCount") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstanceQuota: A resource budget.

func (InstanceQuota) MarshalJSON ¶
added in v0.69.0
func (s InstanceQuota) MarshalJSON() ([]byte, error)
type IntakeVlanAttachment ¶
added in v0.69.0
type IntakeVlanAttachment struct {
	// Id: Identifier of the VLAN attachment.
	Id string `json:"id,omitempty"`
	// PairingKey: Attachment pairing key.
	PairingKey string `json:"pairingKey,omitempty"`
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

IntakeVlanAttachment: A GCP vlan attachment.

func (IntakeVlanAttachment) MarshalJSON ¶
added in v0.69.0
func (s IntakeVlanAttachment) MarshalJSON() ([]byte, error)
type ListInstancesResponse ¶
type ListInstancesResponse struct {
	// Instances: The list of servers.
	Instances []*Instance `json:"instances,omitempty"`
	// NextPageToken: A token identifying a page of results from the server.
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

ListInstancesResponse: Response message for the list of servers.

func (ListInstancesResponse) MarshalJSON ¶
func (s ListInstancesResponse) MarshalJSON() ([]byte, error)
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
type ListLunsResponse ¶
added in v0.60.0
type ListLunsResponse struct {
	// Luns: The list of luns.
	Luns []*Lun `json:"luns,omitempty"`
	// NextPageToken: A token identifying a page of results from the server.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Luns") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Luns") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListLunsResponse: Response message containing the list of storage volume luns.

func (ListLunsResponse) MarshalJSON ¶
added in v0.60.0
func (s ListLunsResponse) MarshalJSON() ([]byte, error)
type ListNetworkUsageResponse ¶
added in v0.69.0
type ListNetworkUsageResponse struct {
	// Networks: Networks with IPs.
	Networks []*NetworkUsage `json:"networks,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Networks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Networks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListNetworkUsageResponse: Response with Networks with IPs

func (ListNetworkUsageResponse) MarshalJSON ¶
added in v0.69.0
func (s ListNetworkUsageResponse) MarshalJSON() ([]byte, error)
type ListNetworksResponse ¶
added in v0.62.0
type ListNetworksResponse struct {
	// Networks: The list of networks.
	Networks []*Network `json:"networks,omitempty"`
	// NextPageToken: A token identifying a page of results from the server.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Networks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Networks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListNetworksResponse: Response message containing the list of networks.

func (ListNetworksResponse) MarshalJSON ¶
added in v0.62.0
func (s ListNetworksResponse) MarshalJSON() ([]byte, error)
type ListNfsSharesResponse ¶
added in v0.69.0
type ListNfsSharesResponse struct {
	// NextPageToken: A token identifying a page of results from the server.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// NfsShares: The list of NFS shares.
	NfsShares []*NfsShare `json:"nfsShares,omitempty"`
	// Unreachable: Locations that could not be reached.
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

ListNfsSharesResponse: Response message containing the list of NFS shares.

func (ListNfsSharesResponse) MarshalJSON ¶
added in v0.69.0
func (s ListNfsSharesResponse) MarshalJSON() ([]byte, error)
type ListOSImagesResponse ¶
added in v0.137.0
type ListOSImagesResponse struct {
	// NextPageToken: Token to retrieve the next page of results, or empty if there
	// are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// OsImages: The OS images available.
	OsImages []*OSImage `json:"osImages,omitempty"`

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

ListOSImagesResponse: Request for getting all available OS images.

func (ListOSImagesResponse) MarshalJSON ¶
added in v0.137.0
func (s ListOSImagesResponse) MarshalJSON() ([]byte, error)
type ListProvisioningQuotasResponse ¶
added in v0.69.0
type ListProvisioningQuotasResponse struct {
	// NextPageToken: Token to retrieve the next page of results, or empty if there
	// are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// ProvisioningQuotas: The provisioning quotas registered in this project.
	ProvisioningQuotas []*ProvisioningQuota `json:"provisioningQuotas,omitempty"`

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

ListProvisioningQuotasResponse: Response message for the list of provisioning quotas.

func (ListProvisioningQuotasResponse) MarshalJSON ¶
added in v0.69.0
func (s ListProvisioningQuotasResponse) MarshalJSON() ([]byte, error)
type ListSSHKeysResponse ¶
added in v0.98.0
type ListSSHKeysResponse struct {
	// NextPageToken: Token to retrieve the next page of results, or empty if there
	// are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SshKeys: The SSH keys registered in the project.
	SshKeys []*SSHKey `json:"sshKeys,omitempty"`

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

ListSSHKeysResponse: Message for response of ListSSHKeys.

func (ListSSHKeysResponse) MarshalJSON ¶
added in v0.98.0
func (s ListSSHKeysResponse) MarshalJSON() ([]byte, error)
type ListVolumeSnapshotsResponse ¶
added in v0.62.0
type ListVolumeSnapshotsResponse struct {
	// NextPageToken: A token identifying a page of results from the server.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`
	// VolumeSnapshots: The list of snapshots.
	VolumeSnapshots []*VolumeSnapshot `json:"volumeSnapshots,omitempty"`

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

ListVolumeSnapshotsResponse: Response message containing the list of volume snapshots.

func (ListVolumeSnapshotsResponse) MarshalJSON ¶
added in v0.62.0
func (s ListVolumeSnapshotsResponse) MarshalJSON() ([]byte, error)
type ListVolumesResponse ¶
added in v0.55.0
type ListVolumesResponse struct {
	// NextPageToken: A token identifying a page of results from the server.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: Locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`
	// Volumes: The list of storage volumes.
	Volumes []*Volume `json:"volumes,omitempty"`

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

ListVolumesResponse: Response message containing the list of storage volumes.

func (ListVolumesResponse) MarshalJSON ¶
added in v0.55.0
func (s ListVolumesResponse) MarshalJSON() ([]byte, error)
type LoadInstanceAuthInfoResponse ¶
added in v0.154.0
type LoadInstanceAuthInfoResponse struct {
	// SshKeys: List of ssh keys.
	SshKeys []*SSHKey `json:"sshKeys,omitempty"`
	// UserAccounts: Map of username to the user account info.
	UserAccounts map[string]UserAccount `json:"userAccounts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "SshKeys") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SshKeys") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LoadInstanceAuthInfoResponse: Response for LoadInstanceAuthInfo.

func (LoadInstanceAuthInfoResponse) MarshalJSON ¶
added in v0.154.0
func (s LoadInstanceAuthInfoResponse) MarshalJSON() ([]byte, error)
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
type LogicalNetworkInterface ¶
added in v0.82.0
type LogicalNetworkInterface struct {
	// DefaultGateway: Whether this interface is the default gateway for the
	// instance. Only one interface can be the default gateway for the instance.
	DefaultGateway bool `json:"defaultGateway,omitempty"`
	// Id: An identifier for the `Network`, generated by the backend.
	Id string `json:"id,omitempty"`
	// IpAddress: IP address in the network
	IpAddress string `json:"ipAddress,omitempty"`
	// Network: Name of the network
	Network string `json:"network,omitempty"`
	// NetworkType: Type of network.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified value.
	//   "CLIENT" - Client network, a network peered to a Google Cloud VPC.
	//   "PRIVATE" - Private network, a network local to the Bare Metal Solution
	// environment.
	NetworkType string `json:"networkType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DefaultGateway") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DefaultGateway") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LogicalNetworkInterface: Each logical network interface is effectively a network and IP pair.

func (LogicalNetworkInterface) MarshalJSON ¶
added in v0.82.0
func (s LogicalNetworkInterface) MarshalJSON() ([]byte, error)
type Lun ¶
type Lun struct {
	// BootLun: Display if this LUN is a boot LUN.
	BootLun bool `json:"bootLun,omitempty"`
	// ExpireTime: Output only. Time after which LUN will be fully deleted. It is
	// filled only for LUNs in COOL_OFF state.
	ExpireTime string `json:"expireTime,omitempty"`
	// Id: An identifier for the LUN, generated by the backend.
	Id string `json:"id,omitempty"`
	// Instances: Output only. Instances this Lun is attached to.
	Instances []string `json:"instances,omitempty"`
	// MultiprotocolType: The LUN multiprotocol type ensures the characteristics of
	// the LUN are optimized for each operating system.
	//
	// Possible values:
	//   "MULTIPROTOCOL_TYPE_UNSPECIFIED" - Server has no OS specified.
	//   "LINUX" - Server with Linux OS.
	MultiprotocolType string `json:"multiprotocolType,omitempty"`
	// Name: Output only. The name of the LUN.
	Name string `json:"name,omitempty"`
	// Shareable: Display if this LUN can be shared between multiple physical
	// servers.
	Shareable bool `json:"shareable,omitempty"`
	// SizeGb: The size of this LUN, in GiB.
	SizeGb int64 `json:"sizeGb,omitempty,string"`
	// State: The state of this storage volume.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The LUN is in an unknown state.
	//   "CREATING" - The LUN is being created.
	//   "UPDATING" - The LUN is being updated.
	//   "READY" - The LUN is ready for use.
	//   "DELETING" - The LUN has been requested to be deleted.
	//   "COOL_OFF" - The LUN is in cool off state. It will be deleted after
	// `expire_time`.
	State string `json:"state,omitempty"`
	// StorageType: The storage type for this LUN.
	//
	// Possible values:
	//   "STORAGE_TYPE_UNSPECIFIED" - The storage type for this LUN is unknown.
	//   "SSD" - This storage type for this LUN is SSD.
	//   "HDD" - This storage type for this LUN is HDD.
	StorageType string `json:"storageType,omitempty"`
	// StorageVolume: Display the storage volume for this LUN.
	StorageVolume string `json:"storageVolume,omitempty"`
	// Wwid: The WWID for this LUN.
	Wwid string `json:"wwid,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BootLun") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BootLun") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Lun: A storage volume logical unit number (LUN).

func (Lun) MarshalJSON ¶
func (s Lun) MarshalJSON() ([]byte, error)
type LunRange ¶
added in v0.69.0
type LunRange struct {
	// Quantity: Number of LUNs to create.
	Quantity int64 `json:"quantity,omitempty"`
	// SizeGb: The requested size of each LUN, in GB.
	SizeGb int64 `json:"sizeGb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Quantity") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Quantity") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LunRange: A LUN(Logical Unit Number) range.

func (LunRange) MarshalJSON ¶
added in v0.69.0
func (s LunRange) MarshalJSON() ([]byte, error)
type Network ¶
type Network struct {
	// Cidr: The cidr of the Network.
	Cidr string `json:"cidr,omitempty"`
	// GatewayIp: Output only. Gateway ip address.
	GatewayIp string `json:"gatewayIp,omitempty"`
	// Id: An identifier for the `Network`, generated by the backend.
	Id string `json:"id,omitempty"`
	// IpAddress: IP address configured.
	IpAddress string `json:"ipAddress,omitempty"`
	// JumboFramesEnabled: Whether network uses standard frames or jumbo ones.
	JumboFramesEnabled bool `json:"jumboFramesEnabled,omitempty"`
	// Labels: Labels as key value pairs.
	Labels map[string]string `json:"labels,omitempty"`
	// MacAddress: List of physical interfaces.
	MacAddress []string `json:"macAddress,omitempty"`
	// MountPoints: Input only. List of mount points to attach the network to.
	MountPoints []*NetworkMountPoint `json:"mountPoints,omitempty"`
	// Name: Output only. The resource name of this `Network`. Resource names are
	// schemeless URIs that follow the conventions in
	// https://cloud.google.com/apis/design/resource_names. Format:
	// `projects/{project}/locations/{location}/networks/{network}`
	Name string `json:"name,omitempty"`
	// Pod: Immutable. Pod name. Pod is an independent part of infrastructure.
	// Network can only be connected to the assets (instances, nfsshares) allocated
	// in the same pod.
	Pod string `json:"pod,omitempty"`
	// Reservations: List of IP address reservations in this network. When updating
	// this field, an error will be generated if a reservation conflicts with an IP
	// address already allocated to a physical server.
	Reservations []*NetworkAddressReservation `json:"reservations,omitempty"`
	// ServicesCidr: IP range for reserved for services (e.g. NFS).
	ServicesCidr string `json:"servicesCidr,omitempty"`
	// State: The Network state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The Network is in an unknown state.
	//   "PROVISIONING" - The Network is provisioning.
	//   "PROVISIONED" - The Network has been provisioned.
	//   "DEPROVISIONING" - The Network is being deprovisioned.
	//   "UPDATING" - The Network is being updated.
	State string `json:"state,omitempty"`
	// Type: The type of this network.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified value.
	//   "CLIENT" - Client network, a network peered to a Google Cloud VPC.
	//   "PRIVATE" - Private network, a network local to the Bare Metal Solution
	// environment.
	Type string `json:"type,omitempty"`
	// VlanId: The vlan id of the Network.
	VlanId string `json:"vlanId,omitempty"`
	// Vrf: The Vrf for the Network. Use this only if a new Vrf needs to be
	// created.
	Vrf *VRF `json:"vrf,omitempty"`
	// VrfAttachment: Optional. The name of a pre-existing Vrf that the network
	// should be attached to. Format is `vrfs/{vrf}`.
	VrfAttachment string `json:"vrfAttachment,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Cidr") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cidr") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Network: A Network.

func (Network) MarshalJSON ¶
func (s Network) MarshalJSON() ([]byte, error)
type NetworkAddress ¶
added in v0.69.0
type NetworkAddress struct {
	// Address: IPv4 address to be assigned to the server.
	Address string `json:"address,omitempty"`
	// ExistingNetworkId: Name of the existing network to use.
	ExistingNetworkId string `json:"existingNetworkId,omitempty"`
	// NetworkId: Id of the network to use, within the same ProvisioningConfig
	// request.
	NetworkId string `json:"networkId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Address") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Address") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkAddress: A network.

func (NetworkAddress) MarshalJSON ¶
added in v0.69.0
func (s NetworkAddress) MarshalJSON() ([]byte, error)
type NetworkAddressReservation ¶
added in v0.79.0
type NetworkAddressReservation struct {
	// EndAddress: The last address of this reservation block, inclusive. I.e., for
	// cases when reservations are only single addresses, end_address and
	// start_address will be the same. Must be specified as a single IPv4 address,
	// e.g. 10.1.2.2.
	EndAddress string `json:"endAddress,omitempty"`
	// Note: A note about this reservation, intended for human consumption.
	Note string `json:"note,omitempty"`
	// StartAddress: The first address of this reservation block. Must be specified
	// as a single IPv4 address, e.g. 10.1.2.2.
	StartAddress string `json:"startAddress,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndAddress") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndAddress") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkAddressReservation: A reservation of one or more addresses in a network.

func (NetworkAddressReservation) MarshalJSON ¶
added in v0.79.0
func (s NetworkAddressReservation) MarshalJSON() ([]byte, error)
type NetworkConfig ¶
added in v0.69.0
type NetworkConfig struct {
	// Bandwidth: Interconnect bandwidth. Set only when type is CLIENT.
	//
	// Possible values:
	//   "BANDWIDTH_UNSPECIFIED" - Unspecified value.
	//   "BW_1_GBPS" - 1 Gbps.
	//   "BW_2_GBPS" - 2 Gbps.
	//   "BW_5_GBPS" - 5 Gbps.
	//   "BW_10_GBPS" - 10 Gbps.
	Bandwidth string `json:"bandwidth,omitempty"`
	// Cidr: CIDR range of the network.
	Cidr string `json:"cidr,omitempty"`
	// GcpService: The GCP service of the network. Available gcp_service are in
	// https://cloud.google.com/bare-metal/docs/bms-planning.
	GcpService string `json:"gcpService,omitempty"`
	// Id: A transient unique identifier to identify a volume within an
	// ProvisioningConfig request.
	Id string `json:"id,omitempty"`
	// JumboFramesEnabled: The JumboFramesEnabled option for customer to set.
	JumboFramesEnabled bool `json:"jumboFramesEnabled,omitempty"`
	// Name: Output only. The name of the network config.
	Name string `json:"name,omitempty"`
	// ServiceCidr: Service CIDR, if any.
	//
	// Possible values:
	//   "SERVICE_CIDR_UNSPECIFIED" - Unspecified value.
	//   "DISABLED" - Services are disabled for the given network.
	//   "HIGH_26" - Use the highest /26 block of the network to host services.
	//   "HIGH_27" - Use the highest /27 block of the network to host services.
	//   "HIGH_28" - Use the highest /28 block of the network to host services.
	ServiceCidr string `json:"serviceCidr,omitempty"`
	// Type: The type of this network, either Client or Private.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Unspecified value.
	//   "CLIENT" - Client network, that is a network peered to a GCP VPC.
	//   "PRIVATE" - Private network, that is a network local to the BMS POD.
	Type string `json:"type,omitempty"`
	// UserNote: User note field, it can be used by customers to add additional
	// information for the BMS Ops team .
	UserNote string `json:"userNote,omitempty"`
	// VlanAttachments: List of VLAN attachments. As of now there are always 2
	// attachments, but it is going to change in the future (multi vlan). Use only
	// one of vlan_attachments or vrf
	VlanAttachments []*IntakeVlanAttachment `json:"vlanAttachments,omitempty"`
	// VlanSameProject: Whether the VLAN attachment pair is located in the same
	// project.
	VlanSameProject bool `json:"vlanSameProject,omitempty"`
	// Vrf: Optional. The name of a pre-existing Vrf that the network should be
	// attached to. Format is `vrfs/{vrf}`. If vrf is specified, vlan_attachments
	// must be empty.
	Vrf string `json:"vrf,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Bandwidth") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Bandwidth") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkConfig: Configuration parameters for a new network.

func (NetworkConfig) MarshalJSON ¶
added in v0.69.0
func (s NetworkConfig) MarshalJSON() ([]byte, error)
type NetworkMountPoint ¶
added in v0.95.0
type NetworkMountPoint struct {
	// DefaultGateway: Network should be a default gateway.
	DefaultGateway bool `json:"defaultGateway,omitempty"`
	// Instance: Instance to attach network to.
	Instance string `json:"instance,omitempty"`
	// IpAddress: Ip address of the server.
	IpAddress string `json:"ipAddress,omitempty"`
	// LogicalInterface: Logical interface to detach from.
	LogicalInterface string `json:"logicalInterface,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DefaultGateway") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DefaultGateway") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NetworkMountPoint: Mount point for a network.

func (NetworkMountPoint) MarshalJSON ¶
added in v0.95.0
func (s NetworkMountPoint) MarshalJSON() ([]byte, error)
type NetworkUsage ¶
added in v0.69.0
type NetworkUsage struct {
	// Network: Network.
	Network *Network `json:"network,omitempty"`
	// UsedIps: All used IP addresses in this network.
	UsedIps []string `json:"usedIps,omitempty"`
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

NetworkUsage: Network with all used IP addresses.

func (NetworkUsage) MarshalJSON ¶
added in v0.69.0
func (s NetworkUsage) MarshalJSON() ([]byte, error)
type NfsExport ¶
added in v0.69.0
type NfsExport struct {
	// AllowDev: Allow dev flag in NfsShare AllowedClientsRequest.
	AllowDev bool `json:"allowDev,omitempty"`
	// AllowSuid: Allow the setuid flag.
	AllowSuid bool `json:"allowSuid,omitempty"`
	// Cidr: A CIDR range.
	Cidr string `json:"cidr,omitempty"`
	// MachineId: Either a single machine, identified by an ID, or a
	// comma-separated list of machine IDs.
	MachineId string `json:"machineId,omitempty"`
	// NetworkId: Network to use to publish the export.
	NetworkId string `json:"networkId,omitempty"`
	// NoRootSquash: Disable root squashing, which is a feature of NFS. Root squash
	// is a special mapping of the remote superuser (root) identity when using
	// identity authentication.
	NoRootSquash bool `json:"noRootSquash,omitempty"`
	// Permissions: Export permissions.
	//
	// Possible values:
	//   "PERMISSIONS_UNSPECIFIED" - Unspecified value.
	//   "READ_ONLY" - Read-only permission.
	//   "READ_WRITE" - Read-write permission.
	Permissions string `json:"permissions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowDev") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowDev") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NfsExport: A NFS export entry.

func (NfsExport) MarshalJSON ¶
added in v0.69.0
func (s NfsExport) MarshalJSON() ([]byte, error)
type NfsShare ¶
added in v0.69.0
type NfsShare struct {
	// AllowedClients: List of allowed access points.
	AllowedClients []*AllowedClient `json:"allowedClients,omitempty"`
	// Id: Output only. An identifier for the NFS share, generated by the backend.
	// This is the same value as nfs_share_id and will replace it in the future.
	Id string `json:"id,omitempty"`
	// Labels: Labels as key value pairs.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Immutable. The name of the NFS share.
	Name string `json:"name,omitempty"`
	// NfsShareId: Output only. An identifier for the NFS share, generated by the
	// backend. This field will be deprecated in the future, use `id` instead.
	NfsShareId string `json:"nfsShareId,omitempty"`
	// Pod: Immutable. Pod name. Pod is an independent part of infrastructure.
	// NFSShare can only be connected to the assets (networks, instances) allocated
	// in the same pod.
	Pod string `json:"pod,omitempty"`
	// RequestedSizeGib: The requested size, in GiB.
	RequestedSizeGib int64 `json:"requestedSizeGib,omitempty,string"`
	// State: Output only. The state of the NFS share.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The share is in an unknown state.
	//   "PROVISIONED" - The share has been provisioned.
	//   "CREATING" - The NFS Share is being created.
	//   "UPDATING" - The NFS Share is being updated.
	//   "DELETING" - The NFS Share has been requested to be deleted.
	State string `json:"state,omitempty"`
	// StorageType: Immutable. The storage type of the underlying volume.
	//
	// Possible values:
	//   "STORAGE_TYPE_UNSPECIFIED" - The storage type for this volume is unknown.
	//   "SSD" - The storage type for this volume is SSD.
	//   "HDD" - This storage type for this volume is HDD.
	StorageType string `json:"storageType,omitempty"`
	// Volume: Output only. The underlying volume of the share. Created
	// automatically during provisioning.
	Volume string `json:"volume,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AllowedClients") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedClients") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NfsShare: An NFS share.

func (NfsShare) MarshalJSON ¶
added in v0.69.0
func (s NfsShare) MarshalJSON() ([]byte, error)
type OSImage ¶
added in v0.75.0
type OSImage struct {
	// ApplicableInstanceTypes: Instance types this image is applicable to.
	// Available types
	// (https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations)
	ApplicableInstanceTypes []string `json:"applicableInstanceTypes,omitempty"`
	// Code: OS Image code.
	Code string `json:"code,omitempty"`
	// Description: OS Image description.
	Description string `json:"description,omitempty"`
	// Name: Output only. OS Image's unique name.
	Name string `json:"name,omitempty"`
	// SupportedNetworkTemplates: Network templates that can be used with this OS
	// Image.
	SupportedNetworkTemplates []string `json:"supportedNetworkTemplates,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApplicableInstanceTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicableInstanceTypes") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OSImage: Operation System image.

func (OSImage) MarshalJSON ¶
added in v0.75.0
func (s OSImage) MarshalJSON() ([]byte, error)
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
type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)

Do executes the "baremetalsolution.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsInstancesDetachLunCall ¶
added in v0.79.0
type ProjectsLocationsInstancesDetachLunCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesDetachLunCall) Context ¶
added in v0.79.0
func (c *ProjectsLocationsInstancesDetachLunCall) Context(ctx context.Context) *ProjectsLocationsInstancesDetachLunCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesDetachLunCall) Do ¶
added in v0.79.0
func (c *ProjectsLocationsInstancesDetachLunCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.detachLun" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesDetachLunCall) Fields ¶
added in v0.79.0
func (c *ProjectsLocationsInstancesDetachLunCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDetachLunCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesDetachLunCall) Header ¶
added in v0.79.0
func (c *ProjectsLocationsInstancesDetachLunCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesDisableHyperthreadingCall ¶
added in v0.178.0
type ProjectsLocationsInstancesDisableHyperthreadingCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesDisableHyperthreadingCall) Context ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Context(ctx context.Context) *ProjectsLocationsInstancesDisableHyperthreadingCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesDisableHyperthreadingCall) Do ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.disableHyperthreading" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesDisableHyperthreadingCall) Fields ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDisableHyperthreadingCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesDisableHyperthreadingCall) Header ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesDisableHyperthreadingCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall ¶
added in v0.98.0
type ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Context(ctx context.Context) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.disableInteractiveSerialConsole" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesEnableHyperthreadingCall ¶
added in v0.178.0
type ProjectsLocationsInstancesEnableHyperthreadingCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesEnableHyperthreadingCall) Context ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Context(ctx context.Context) *ProjectsLocationsInstancesEnableHyperthreadingCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesEnableHyperthreadingCall) Do ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.enableHyperthreading" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesEnableHyperthreadingCall) Fields ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesEnableHyperthreadingCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesEnableHyperthreadingCall) Header ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesEnableHyperthreadingCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall ¶
added in v0.98.0
type ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Context(ctx context.Context) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.enableInteractiveSerialConsole" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesGetCall ¶
type ProjectsLocationsInstancesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesGetCall) Context ¶
func (c *ProjectsLocationsInstancesGetCall) Context(ctx context.Context) *ProjectsLocationsInstancesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesGetCall) Do ¶
func (c *ProjectsLocationsInstancesGetCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "baremetalsolution.projects.locations.instances.get" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesGetCall) Fields ¶
func (c *ProjectsLocationsInstancesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesGetCall) Header ¶
func (c *ProjectsLocationsInstancesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsInstancesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsInstancesListCall ¶
type ProjectsLocationsInstancesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesListCall) Context ¶
func (c *ProjectsLocationsInstancesListCall) Context(ctx context.Context) *ProjectsLocationsInstancesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesListCall) Do ¶
func (c *ProjectsLocationsInstancesListCall) Do(opts ...googleapi.CallOption) (*ListInstancesResponse, error)

Do executes the "baremetalsolution.projects.locations.instances.list" call. Any non-2xx status code is an error. Response headers are in either *ListInstancesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesListCall) Fields ¶
func (c *ProjectsLocationsInstancesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesListCall) Filter ¶
func (c *ProjectsLocationsInstancesListCall) Filter(filter string) *ProjectsLocationsInstancesListCall

Filter sets the optional parameter "filter": List filter.

func (*ProjectsLocationsInstancesListCall) Header ¶
func (c *ProjectsLocationsInstancesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesListCall) IfNoneMatch ¶
func (c *ProjectsLocationsInstancesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsInstancesListCall) PageSize ¶
func (c *ProjectsLocationsInstancesListCall) PageSize(pageSize int64) *ProjectsLocationsInstancesListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer items than requested. If unspecified, the server will pick an appropriate default.

func (*ProjectsLocationsInstancesListCall) PageToken ¶
func (c *ProjectsLocationsInstancesListCall) PageToken(pageToken string) *ProjectsLocationsInstancesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsInstancesListCall) Pages ¶
func (c *ProjectsLocationsInstancesListCall) Pages(ctx context.Context, f func(*ListInstancesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsInstancesLoadAuthInfoCall ¶
added in v0.154.0
type ProjectsLocationsInstancesLoadAuthInfoCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesLoadAuthInfoCall) Context ¶
added in v0.154.0
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Context(ctx context.Context) *ProjectsLocationsInstancesLoadAuthInfoCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesLoadAuthInfoCall) Do ¶
added in v0.154.0
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Do(opts ...googleapi.CallOption) (*LoadInstanceAuthInfoResponse, error)

Do executes the "baremetalsolution.projects.locations.instances.loadAuthInfo" call. Any non-2xx status code is an error. Response headers are in either *LoadInstanceAuthInfoResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesLoadAuthInfoCall) Fields ¶
added in v0.154.0
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesLoadAuthInfoCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesLoadAuthInfoCall) Header ¶
added in v0.154.0
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesLoadAuthInfoCall) IfNoneMatch ¶
added in v0.154.0
func (c *ProjectsLocationsInstancesLoadAuthInfoCall) IfNoneMatch(entityTag string) *ProjectsLocationsInstancesLoadAuthInfoCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsInstancesPatchCall ¶
added in v0.69.0
type ProjectsLocationsInstancesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesPatchCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesPatchCall) Context(ctx context.Context) *ProjectsLocationsInstancesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesPatchCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesPatchCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesPatchCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsInstancesPatchCall) UpdateMask ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsInstancesPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. The currently supported fields are: `labels` `hyperthreading_enabled` `os_image` `ssh_keys` `kms_key_version`

type ProjectsLocationsInstancesReimageCall ¶
added in v0.178.0
type ProjectsLocationsInstancesReimageCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesReimageCall) Context ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesReimageCall) Context(ctx context.Context) *ProjectsLocationsInstancesReimageCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesReimageCall) Do ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesReimageCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.reimage" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesReimageCall) Fields ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesReimageCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesReimageCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesReimageCall) Header ¶
added in v0.178.0
func (c *ProjectsLocationsInstancesReimageCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesRenameCall ¶
added in v0.111.0
type ProjectsLocationsInstancesRenameCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesRenameCall) Context ¶
added in v0.111.0
func (c *ProjectsLocationsInstancesRenameCall) Context(ctx context.Context) *ProjectsLocationsInstancesRenameCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesRenameCall) Do ¶
added in v0.111.0
func (c *ProjectsLocationsInstancesRenameCall) Do(opts ...googleapi.CallOption) (*Instance, error)

Do executes the "baremetalsolution.projects.locations.instances.rename" call. Any non-2xx status code is an error. Response headers are in either *Instance.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesRenameCall) Fields ¶
added in v0.111.0
func (c *ProjectsLocationsInstancesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesRenameCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesRenameCall) Header ¶
added in v0.111.0
func (c *ProjectsLocationsInstancesRenameCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesResetCall ¶
added in v0.62.0
type ProjectsLocationsInstancesResetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesResetCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsInstancesResetCall) Context(ctx context.Context) *ProjectsLocationsInstancesResetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesResetCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsInstancesResetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.reset" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesResetCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsInstancesResetCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesResetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesResetCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsInstancesResetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesService ¶
type ProjectsLocationsInstancesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsInstancesService ¶
func NewProjectsLocationsInstancesService(s *Service) *ProjectsLocationsInstancesService
func (*ProjectsLocationsInstancesService) DetachLun ¶
added in v0.79.0
func (r *ProjectsLocationsInstancesService) DetachLun(instance string, detachlunrequest *DetachLunRequest) *ProjectsLocationsInstancesDetachLunCall

DetachLun: Detach LUN from Instance.

- instance: Name of the instance.

func (*ProjectsLocationsInstancesService) DisableHyperthreading ¶
added in v0.178.0
func (r *ProjectsLocationsInstancesService) DisableHyperthreading(name string, disablehyperthreadingrequest *DisableHyperthreadingRequest) *ProjectsLocationsInstancesDisableHyperthreadingCall

DisableHyperthreading: Perform disable hyperthreading operation on a single server.

name: The `name` field is used to identify the instance. Format: projects/{project}/locations/{location}/instances/{instance}.
func (*ProjectsLocationsInstancesService) DisableInteractiveSerialConsole ¶
added in v0.98.0
func (r *ProjectsLocationsInstancesService) DisableInteractiveSerialConsole(name string, disableinteractiveserialconsolerequest *DisableInteractiveSerialConsoleRequest) *ProjectsLocationsInstancesDisableInteractiveSerialConsoleCall

DisableInteractiveSerialConsole: Disable the interactive serial console feature on an instance.

- name: Name of the resource.

func (*ProjectsLocationsInstancesService) EnableHyperthreading ¶
added in v0.178.0
func (r *ProjectsLocationsInstancesService) EnableHyperthreading(name string, enablehyperthreadingrequest *EnableHyperthreadingRequest) *ProjectsLocationsInstancesEnableHyperthreadingCall

EnableHyperthreading: Perform enable hyperthreading operation on a single server.

name: The `name` field is used to identify the instance. Format: projects/{project}/locations/{location}/instances/{instance}.
func (*ProjectsLocationsInstancesService) EnableInteractiveSerialConsole ¶
added in v0.98.0
func (r *ProjectsLocationsInstancesService) EnableInteractiveSerialConsole(name string, enableinteractiveserialconsolerequest *EnableInteractiveSerialConsoleRequest) *ProjectsLocationsInstancesEnableInteractiveSerialConsoleCall

EnableInteractiveSerialConsole: Enable the interactive serial console feature on an instance.

- name: Name of the resource.

func (*ProjectsLocationsInstancesService) Get ¶
func (r *ProjectsLocationsInstancesService) Get(name string) *ProjectsLocationsInstancesGetCall

Get: Get details about a single server.

- name: Name of the resource.

func (*ProjectsLocationsInstancesService) List ¶
func (r *ProjectsLocationsInstancesService) List(parent string) *ProjectsLocationsInstancesListCall

List: List servers in a given project and location.

- parent: Parent value for ListInstancesRequest.

func (*ProjectsLocationsInstancesService) LoadAuthInfo ¶
added in v0.154.0
func (r *ProjectsLocationsInstancesService) LoadAuthInfo(name string) *ProjectsLocationsInstancesLoadAuthInfoCall

LoadAuthInfo: Load auth info for a server.

- name: Name of the server.

func (*ProjectsLocationsInstancesService) Patch ¶
added in v0.69.0
func (r *ProjectsLocationsInstancesService) Patch(name string, instance *Instance) *ProjectsLocationsInstancesPatchCall

Patch: Update details of a single server.

name: Immutable. The resource name of this `Instance`. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. Format: `projects/{project}/locations/{location}/instances/{instance}`.
func (*ProjectsLocationsInstancesService) Reimage ¶
added in v0.178.0
func (r *ProjectsLocationsInstancesService) Reimage(name string, reimageinstancerequest *ReimageInstanceRequest) *ProjectsLocationsInstancesReimageCall

Reimage: Perform reimage operation on a single server.

name: The `name` field is used to identify the instance. Format: projects/{project}/locations/{location}/instances/{instance}.
func (*ProjectsLocationsInstancesService) Rename ¶
added in v0.111.0
func (r *ProjectsLocationsInstancesService) Rename(name string, renameinstancerequest *RenameInstanceRequest) *ProjectsLocationsInstancesRenameCall

Rename: RenameInstance sets a new name for an instance. Use with caution, previous names become immediately invalidated.

name: The `name` field is used to identify the instance. Format: projects/{project}/locations/{location}/instances/{instance}.
func (*ProjectsLocationsInstancesService) Reset ¶
added in v0.62.0
func (r *ProjectsLocationsInstancesService) Reset(name string, resetinstancerequest *ResetInstanceRequest) *ProjectsLocationsInstancesResetCall

Reset: Perform an ungraceful, hard reset on a server. Equivalent to shutting the power off and then turning it back on.

- name: Name of the resource.

func (*ProjectsLocationsInstancesService) Start ¶
added in v0.69.0
func (r *ProjectsLocationsInstancesService) Start(name string, startinstancerequest *StartInstanceRequest) *ProjectsLocationsInstancesStartCall

Start: Starts a server that was shutdown.

- name: Name of the resource.

func (*ProjectsLocationsInstancesService) Stop ¶
added in v0.76.0
func (r *ProjectsLocationsInstancesService) Stop(name string, stopinstancerequest *StopInstanceRequest) *ProjectsLocationsInstancesStopCall

Stop: Stop a running server.

- name: Name of the resource.

type ProjectsLocationsInstancesStartCall ¶
added in v0.69.0
type ProjectsLocationsInstancesStartCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesStartCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesStartCall) Context(ctx context.Context) *ProjectsLocationsInstancesStartCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesStartCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesStartCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.start" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesStartCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesStartCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesStartCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesStartCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsInstancesStartCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsInstancesStopCall ¶
added in v0.76.0
type ProjectsLocationsInstancesStopCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsInstancesStopCall) Context ¶
added in v0.76.0
func (c *ProjectsLocationsInstancesStopCall) Context(ctx context.Context) *ProjectsLocationsInstancesStopCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsInstancesStopCall) Do ¶
added in v0.76.0
func (c *ProjectsLocationsInstancesStopCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.instances.stop" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsInstancesStopCall) Fields ¶
added in v0.76.0
func (c *ProjectsLocationsInstancesStopCall) Fields(s ...googleapi.Field) *ProjectsLocationsInstancesStopCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsInstancesStopCall) Header ¶
added in v0.76.0
func (c *ProjectsLocationsInstancesStopCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)

Do executes the "baremetalsolution.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsNetworksGetCall ¶
added in v0.62.0
type ProjectsLocationsNetworksGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNetworksGetCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksGetCall) Context(ctx context.Context) *ProjectsLocationsNetworksGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNetworksGetCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksGetCall) Do(opts ...googleapi.CallOption) (*Network, error)

Do executes the "baremetalsolution.projects.locations.networks.get" call. Any non-2xx status code is an error. Response headers are in either *Network.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNetworksGetCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNetworksGetCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNetworksGetCall) IfNoneMatch ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsNetworksListCall ¶
added in v0.62.0
type ProjectsLocationsNetworksListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNetworksListCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) Context(ctx context.Context) *ProjectsLocationsNetworksListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNetworksListCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) Do(opts ...googleapi.CallOption) (*ListNetworksResponse, error)

Do executes the "baremetalsolution.projects.locations.networks.list" call. Any non-2xx status code is an error. Response headers are in either *ListNetworksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNetworksListCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNetworksListCall) Filter ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListCall) Filter(filter string) *ProjectsLocationsNetworksListCall

Filter sets the optional parameter "filter": List filter.

func (*ProjectsLocationsNetworksListCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNetworksListCall) IfNoneMatch ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsNetworksListCall) PageSize ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) PageSize(pageSize int64) *ProjectsLocationsNetworksListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsNetworksListCall) PageToken ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) PageToken(pageToken string) *ProjectsLocationsNetworksListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsNetworksListCall) Pages ¶
added in v0.62.0
func (c *ProjectsLocationsNetworksListCall) Pages(ctx context.Context, f func(*ListNetworksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsNetworksListNetworkUsageCall ¶
added in v0.69.0
type ProjectsLocationsNetworksListNetworkUsageCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNetworksListNetworkUsageCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Context(ctx context.Context) *ProjectsLocationsNetworksListNetworkUsageCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNetworksListNetworkUsageCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Do(opts ...googleapi.CallOption) (*ListNetworkUsageResponse, error)

Do executes the "baremetalsolution.projects.locations.networks.listNetworkUsage" call. Any non-2xx status code is an error. Response headers are in either *ListNetworkUsageResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNetworksListNetworkUsageCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksListNetworkUsageCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNetworksListNetworkUsageCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListNetworkUsageCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNetworksListNetworkUsageCall) IfNoneMatch ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksListNetworkUsageCall) IfNoneMatch(entityTag string) *ProjectsLocationsNetworksListNetworkUsageCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsNetworksPatchCall ¶
added in v0.69.0
type ProjectsLocationsNetworksPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNetworksPatchCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksPatchCall) Context(ctx context.Context) *ProjectsLocationsNetworksPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNetworksPatchCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.networks.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNetworksPatchCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNetworksPatchCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNetworksPatchCall) UpdateMask ¶
added in v0.69.0
func (c *ProjectsLocationsNetworksPatchCall) UpdateMask(updateMask string) *ProjectsLocationsNetworksPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. The only currently supported fields are: `labels`, `reservations`, `vrf.vlan_attachments`

type ProjectsLocationsNetworksRenameCall ¶
added in v0.114.0
type ProjectsLocationsNetworksRenameCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNetworksRenameCall) Context ¶
added in v0.114.0
func (c *ProjectsLocationsNetworksRenameCall) Context(ctx context.Context) *ProjectsLocationsNetworksRenameCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNetworksRenameCall) Do ¶
added in v0.114.0
func (c *ProjectsLocationsNetworksRenameCall) Do(opts ...googleapi.CallOption) (*Network, error)

Do executes the "baremetalsolution.projects.locations.networks.rename" call. Any non-2xx status code is an error. Response headers are in either *Network.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNetworksRenameCall) Fields ¶
added in v0.114.0
func (c *ProjectsLocationsNetworksRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsNetworksRenameCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNetworksRenameCall) Header ¶
added in v0.114.0
func (c *ProjectsLocationsNetworksRenameCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsNetworksService ¶
added in v0.62.0
type ProjectsLocationsNetworksService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsNetworksService ¶
added in v0.62.0
func NewProjectsLocationsNetworksService(s *Service) *ProjectsLocationsNetworksService
func (*ProjectsLocationsNetworksService) Get ¶
added in v0.62.0
func (r *ProjectsLocationsNetworksService) Get(name string) *ProjectsLocationsNetworksGetCall

Get: Get details of a single network.

- name: Name of the resource.

func (*ProjectsLocationsNetworksService) List ¶
added in v0.62.0
func (r *ProjectsLocationsNetworksService) List(parent string) *ProjectsLocationsNetworksListCall

List: List network in a given project and location.

- parent: Parent value for ListNetworksRequest.

func (*ProjectsLocationsNetworksService) ListNetworkUsage ¶
added in v0.69.0
func (r *ProjectsLocationsNetworksService) ListNetworkUsage(location string) *ProjectsLocationsNetworksListNetworkUsageCall

ListNetworkUsage: List all Networks (and used IPs for each Network) in the vendor account associated with the specified project.

- location: Parent value (project and location).

func (*ProjectsLocationsNetworksService) Patch ¶
added in v0.69.0
func (r *ProjectsLocationsNetworksService) Patch(name string, network *Network) *ProjectsLocationsNetworksPatchCall

Patch: Update details of a single network.

name: Output only. The resource name of this `Network`. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. Format: `projects/{project}/locations/{location}/networks/{network}`.
func (*ProjectsLocationsNetworksService) Rename ¶
added in v0.114.0
func (r *ProjectsLocationsNetworksService) Rename(name string, renamenetworkrequest *RenameNetworkRequest) *ProjectsLocationsNetworksRenameCall

Rename: RenameNetwork sets a new name for a network. Use with caution, previous names become immediately invalidated.

name: The `name` field is used to identify the network. Format: projects/{project}/locations/{location}/networks/{network}.
type ProjectsLocationsNfsSharesCreateCall ¶
added in v0.95.0
type ProjectsLocationsNfsSharesCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesCreateCall) Context ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesCreateCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesCreateCall) Do ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesCreateCall) Fields ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesCreateCall) Header ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsNfsSharesDeleteCall ¶
added in v0.95.0
type ProjectsLocationsNfsSharesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesDeleteCall) Context ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesDeleteCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesDeleteCall) Do ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesDeleteCall) Fields ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesDeleteCall) Header ¶
added in v0.95.0
func (c *ProjectsLocationsNfsSharesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsNfsSharesGetCall ¶
added in v0.69.0
type ProjectsLocationsNfsSharesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesGetCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesGetCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesGetCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesGetCall) Do(opts ...googleapi.CallOption) (*NfsShare, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.get" call. Any non-2xx status code is an error. Response headers are in either *NfsShare.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesGetCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesGetCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNfsSharesGetCall) IfNoneMatch ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsNfsSharesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsNfsSharesListCall ¶
added in v0.69.0
type ProjectsLocationsNfsSharesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesListCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesListCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Do(opts ...googleapi.CallOption) (*ListNfsSharesResponse, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.list" call. Any non-2xx status code is an error. Response headers are in either *ListNfsSharesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesListCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesListCall) Filter ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Filter(filter string) *ProjectsLocationsNfsSharesListCall

Filter sets the optional parameter "filter": List filter.

func (*ProjectsLocationsNfsSharesListCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNfsSharesListCall) IfNoneMatch ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsNfsSharesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsNfsSharesListCall) PageSize ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) PageSize(pageSize int64) *ProjectsLocationsNfsSharesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsNfsSharesListCall) PageToken ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) PageToken(pageToken string) *ProjectsLocationsNfsSharesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsNfsSharesListCall) Pages ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesListCall) Pages(ctx context.Context, f func(*ListNfsSharesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsNfsSharesPatchCall ¶
added in v0.69.0
type ProjectsLocationsNfsSharesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesPatchCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesPatchCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesPatchCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesPatchCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesPatchCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsNfsSharesPatchCall) UpdateMask ¶
added in v0.69.0
func (c *ProjectsLocationsNfsSharesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsNfsSharesPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. The only currently supported fields are: `labels` `allowed_clients`

type ProjectsLocationsNfsSharesRenameCall ¶
added in v0.115.0
type ProjectsLocationsNfsSharesRenameCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsNfsSharesRenameCall) Context ¶
added in v0.115.0
func (c *ProjectsLocationsNfsSharesRenameCall) Context(ctx context.Context) *ProjectsLocationsNfsSharesRenameCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsNfsSharesRenameCall) Do ¶
added in v0.115.0
func (c *ProjectsLocationsNfsSharesRenameCall) Do(opts ...googleapi.CallOption) (*NfsShare, error)

Do executes the "baremetalsolution.projects.locations.nfsShares.rename" call. Any non-2xx status code is an error. Response headers are in either *NfsShare.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsNfsSharesRenameCall) Fields ¶
added in v0.115.0
func (c *ProjectsLocationsNfsSharesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsNfsSharesRenameCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsNfsSharesRenameCall) Header ¶
added in v0.115.0
func (c *ProjectsLocationsNfsSharesRenameCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsNfsSharesService ¶
added in v0.69.0
type ProjectsLocationsNfsSharesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsNfsSharesService ¶
added in v0.69.0
func NewProjectsLocationsNfsSharesService(s *Service) *ProjectsLocationsNfsSharesService
func (*ProjectsLocationsNfsSharesService) Create ¶
added in v0.95.0
func (r *ProjectsLocationsNfsSharesService) Create(parent string, nfsshare *NfsShare) *ProjectsLocationsNfsSharesCreateCall

Create: Create an NFS share.

- parent: The parent project and location.

func (*ProjectsLocationsNfsSharesService) Delete ¶
added in v0.95.0
func (r *ProjectsLocationsNfsSharesService) Delete(name string) *ProjectsLocationsNfsSharesDeleteCall

Delete: Delete an NFS share. The underlying volume is automatically deleted.

- name: The name of the NFS share to delete.

func (*ProjectsLocationsNfsSharesService) Get ¶
added in v0.69.0
func (r *ProjectsLocationsNfsSharesService) Get(name string) *ProjectsLocationsNfsSharesGetCall

Get: Get details of a single NFS share.

- name: Name of the resource.

func (*ProjectsLocationsNfsSharesService) List ¶
added in v0.69.0
func (r *ProjectsLocationsNfsSharesService) List(parent string) *ProjectsLocationsNfsSharesListCall

List: List NFS shares.

- parent: Parent value for ListNfsSharesRequest.

func (*ProjectsLocationsNfsSharesService) Patch ¶
added in v0.69.0
func (r *ProjectsLocationsNfsSharesService) Patch(name string, nfsshare *NfsShare) *ProjectsLocationsNfsSharesPatchCall

Patch: Update details of a single NFS share.

- name: Immutable. The name of the NFS share.

func (*ProjectsLocationsNfsSharesService) Rename ¶
added in v0.115.0
func (r *ProjectsLocationsNfsSharesService) Rename(name string, renamenfssharerequest *RenameNfsShareRequest) *ProjectsLocationsNfsSharesRenameCall

Rename: RenameNfsShare sets a new name for an nfsshare. Use with caution, previous names become immediately invalidated.

name: The `name` field is used to identify the nfsshare. Format: projects/{project}/locations/{location}/nfsshares/{nfsshare}.
type ProjectsLocationsOperationsGetCall ¶
type ProjectsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsGetCall) Context ¶
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsGetCall) Do ¶
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsGetCall) Fields ¶
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsGetCall) Header ¶
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsService ¶
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Get ¶
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall

Get: Get details about an operation.

- name: The name of the operation resource.

type ProjectsLocationsOsImagesGetCall ¶
added in v0.144.0
type ProjectsLocationsOsImagesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOsImagesGetCall) Context ¶
added in v0.144.0
func (c *ProjectsLocationsOsImagesGetCall) Context(ctx context.Context) *ProjectsLocationsOsImagesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOsImagesGetCall) Do ¶
added in v0.144.0
func (c *ProjectsLocationsOsImagesGetCall) Do(opts ...googleapi.CallOption) (*OSImage, error)

Do executes the "baremetalsolution.projects.locations.osImages.get" call. Any non-2xx status code is an error. Response headers are in either *OSImage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOsImagesGetCall) Fields ¶
added in v0.144.0
func (c *ProjectsLocationsOsImagesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOsImagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOsImagesGetCall) Header ¶
added in v0.144.0
func (c *ProjectsLocationsOsImagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOsImagesGetCall) IfNoneMatch ¶
added in v0.144.0
func (c *ProjectsLocationsOsImagesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOsImagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOsImagesListCall ¶
added in v0.137.0
type ProjectsLocationsOsImagesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOsImagesListCall) Context ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) Context(ctx context.Context) *ProjectsLocationsOsImagesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOsImagesListCall) Do ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) Do(opts ...googleapi.CallOption) (*ListOSImagesResponse, error)

Do executes the "baremetalsolution.projects.locations.osImages.list" call. Any non-2xx status code is an error. Response headers are in either *ListOSImagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOsImagesListCall) Fields ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOsImagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOsImagesListCall) Header ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOsImagesListCall) IfNoneMatch ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOsImagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsOsImagesListCall) PageSize ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) PageSize(pageSize int64) *ProjectsLocationsOsImagesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default. Notice that page_size field is not supported and won't be respected in the API request for now, will be updated when pagination is supported.

func (*ProjectsLocationsOsImagesListCall) PageToken ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) PageToken(pageToken string) *ProjectsLocationsOsImagesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsOsImagesListCall) Pages ¶
added in v0.137.0
func (c *ProjectsLocationsOsImagesListCall) Pages(ctx context.Context, f func(*ListOSImagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOsImagesService ¶
added in v0.137.0
type ProjectsLocationsOsImagesService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOsImagesService ¶
added in v0.137.0
func NewProjectsLocationsOsImagesService(s *Service) *ProjectsLocationsOsImagesService
func (*ProjectsLocationsOsImagesService) Get ¶
added in v0.144.0
func (r *ProjectsLocationsOsImagesService) Get(name string) *ProjectsLocationsOsImagesGetCall

Get: Get details of a single OS image.

- name: Name of the OS image.

func (*ProjectsLocationsOsImagesService) List ¶
added in v0.137.0
func (r *ProjectsLocationsOsImagesService) List(parent string) *ProjectsLocationsOsImagesListCall

List: Retrieves the list of OS images which are currently approved.

- parent: Parent value for ListOSImagesRequest.

type ProjectsLocationsProvisioningConfigsCreateCall ¶
added in v0.73.0
type ProjectsLocationsProvisioningConfigsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsProvisioningConfigsCreateCall) Context ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsProvisioningConfigsCreateCall) Do ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)

Do executes the "baremetalsolution.projects.locations.provisioningConfigs.create" call. Any non-2xx status code is an error. Response headers are in either *ProvisioningConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsProvisioningConfigsCreateCall) Email ¶
added in v0.74.0
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Email(email string) *ProjectsLocationsProvisioningConfigsCreateCall

Email sets the optional parameter "email": Email provided to send a confirmation with provisioning config to.

func (*ProjectsLocationsProvisioningConfigsCreateCall) Fields ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsProvisioningConfigsCreateCall) Header ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsProvisioningConfigsGetCall ¶
added in v0.73.0
type ProjectsLocationsProvisioningConfigsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsProvisioningConfigsGetCall) Context ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsGetCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsProvisioningConfigsGetCall) Do ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsGetCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)

Do executes the "baremetalsolution.projects.locations.provisioningConfigs.get" call. Any non-2xx status code is an error. Response headers are in either *ProvisioningConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsProvisioningConfigsGetCall) Fields ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsProvisioningConfigsGetCall) Header ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsProvisioningConfigsGetCall) IfNoneMatch ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsProvisioningConfigsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsProvisioningConfigsPatchCall ¶
added in v0.73.0
type ProjectsLocationsProvisioningConfigsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsProvisioningConfigsPatchCall) Context ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsProvisioningConfigsPatchCall) Do ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Do(opts ...googleapi.CallOption) (*ProvisioningConfig, error)

Do executes the "baremetalsolution.projects.locations.provisioningConfigs.patch" call. Any non-2xx status code is an error. Response headers are in either *ProvisioningConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsProvisioningConfigsPatchCall) Email ¶
added in v0.74.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Email(email string) *ProjectsLocationsProvisioningConfigsPatchCall

Email sets the optional parameter "email": Email provided to send a confirmation with provisioning config to.

func (*ProjectsLocationsProvisioningConfigsPatchCall) Fields ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsProvisioningConfigsPatchCall) Header ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsProvisioningConfigsPatchCall) UpdateMask ¶
added in v0.73.0
func (c *ProjectsLocationsProvisioningConfigsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsProvisioningConfigsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update.

type ProjectsLocationsProvisioningConfigsService ¶
added in v0.69.0
type ProjectsLocationsProvisioningConfigsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsProvisioningConfigsService ¶
added in v0.69.0
func NewProjectsLocationsProvisioningConfigsService(s *Service) *ProjectsLocationsProvisioningConfigsService
func (*ProjectsLocationsProvisioningConfigsService) Create ¶
added in v0.73.0
func (r *ProjectsLocationsProvisioningConfigsService) Create(parent string, provisioningconfig *ProvisioningConfig) *ProjectsLocationsProvisioningConfigsCreateCall

Create: Create new ProvisioningConfig.

- parent: The parent project and location containing the ProvisioningConfig.

func (*ProjectsLocationsProvisioningConfigsService) Get ¶
added in v0.73.0
func (r *ProjectsLocationsProvisioningConfigsService) Get(name string) *ProjectsLocationsProvisioningConfigsGetCall

Get: Get ProvisioningConfig by name.

- name: Name of the ProvisioningConfig.

func (*ProjectsLocationsProvisioningConfigsService) Patch ¶
added in v0.73.0
func (r *ProjectsLocationsProvisioningConfigsService) Patch(name string, provisioningconfig *ProvisioningConfig) *ProjectsLocationsProvisioningConfigsPatchCall

Patch: Update existing ProvisioningConfig.

name: Output only. The system-generated name of the provisioning config. This follows the UUID format.
func (*ProjectsLocationsProvisioningConfigsService) Submit ¶
added in v0.69.0
func (r *ProjectsLocationsProvisioningConfigsService) Submit(parent string, submitprovisioningconfigrequest *SubmitProvisioningConfigRequest) *ProjectsLocationsProvisioningConfigsSubmitCall

Submit: Submit a provisioning configuration for a given project.

- parent: The parent project and location containing the ProvisioningConfig.

type ProjectsLocationsProvisioningConfigsSubmitCall ¶
added in v0.69.0
type ProjectsLocationsProvisioningConfigsSubmitCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsProvisioningConfigsSubmitCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Context(ctx context.Context) *ProjectsLocationsProvisioningConfigsSubmitCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsProvisioningConfigsSubmitCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Do(opts ...googleapi.CallOption) (*SubmitProvisioningConfigResponse, error)

Do executes the "baremetalsolution.projects.locations.provisioningConfigs.submit" call. Any non-2xx status code is an error. Response headers are in either *SubmitProvisioningConfigResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsProvisioningConfigsSubmitCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningConfigsSubmitCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsProvisioningConfigsSubmitCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningConfigsSubmitCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsProvisioningQuotasListCall ¶
added in v0.69.0
type ProjectsLocationsProvisioningQuotasListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsProvisioningQuotasListCall) Context ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) Context(ctx context.Context) *ProjectsLocationsProvisioningQuotasListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsProvisioningQuotasListCall) Do ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) Do(opts ...googleapi.CallOption) (*ListProvisioningQuotasResponse, error)

Do executes the "baremetalsolution.projects.locations.provisioningQuotas.list" call. Any non-2xx status code is an error. Response headers are in either *ListProvisioningQuotasResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsProvisioningQuotasListCall) Fields ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) Fields(s ...googleapi.Field) *ProjectsLocationsProvisioningQuotasListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsProvisioningQuotasListCall) Header ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsProvisioningQuotasListCall) IfNoneMatch ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) IfNoneMatch(entityTag string) *ProjectsLocationsProvisioningQuotasListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsProvisioningQuotasListCall) PageSize ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) PageSize(pageSize int64) *ProjectsLocationsProvisioningQuotasListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default. Notice that page_size field is not supported and won't be respected in the API request for now, will be updated when pagination is supported.

func (*ProjectsLocationsProvisioningQuotasListCall) PageToken ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) PageToken(pageToken string) *ProjectsLocationsProvisioningQuotasListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsProvisioningQuotasListCall) Pages ¶
added in v0.69.0
func (c *ProjectsLocationsProvisioningQuotasListCall) Pages(ctx context.Context, f func(*ListProvisioningQuotasResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsProvisioningQuotasService ¶
added in v0.69.0
type ProjectsLocationsProvisioningQuotasService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsProvisioningQuotasService ¶
added in v0.69.0
func NewProjectsLocationsProvisioningQuotasService(s *Service) *ProjectsLocationsProvisioningQuotasService
func (*ProjectsLocationsProvisioningQuotasService) List ¶
added in v0.69.0
func (r *ProjectsLocationsProvisioningQuotasService) List(parent string) *ProjectsLocationsProvisioningQuotasListCall

List: List the budget details to provision resources on a given project.

- parent: Parent value for ListProvisioningQuotasRequest.

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	Instances *ProjectsLocationsInstancesService

	Networks *ProjectsLocationsNetworksService

	NfsShares *ProjectsLocationsNfsSharesService

	Operations *ProjectsLocationsOperationsService

	OsImages *ProjectsLocationsOsImagesService

	ProvisioningConfigs *ProjectsLocationsProvisioningConfigsService

	ProvisioningQuotas *ProjectsLocationsProvisioningQuotasService

	SshKeys *ProjectsLocationsSshKeysService

	Volumes *ProjectsLocationsVolumesService
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

type ProjectsLocationsSshKeysCreateCall ¶
added in v0.98.0
type ProjectsLocationsSshKeysCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSshKeysCreateCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysCreateCall) Context(ctx context.Context) *ProjectsLocationsSshKeysCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSshKeysCreateCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysCreateCall) Do(opts ...googleapi.CallOption) (*SSHKey, error)

Do executes the "baremetalsolution.projects.locations.sshKeys.create" call. Any non-2xx status code is an error. Response headers are in either *SSHKey.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSshKeysCreateCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSshKeysCreateCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSshKeysCreateCall) SshKeyId ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysCreateCall) SshKeyId(sshKeyId string) *ProjectsLocationsSshKeysCreateCall

SshKeyId sets the optional parameter "sshKeyId": Required. The ID to use for the key, which will become the final component of the key's resource name. This value must match the regex: [a-zA-Z0-9@.\-_]{1,64}

type ProjectsLocationsSshKeysDeleteCall ¶
added in v0.98.0
type ProjectsLocationsSshKeysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSshKeysDeleteCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysDeleteCall) Context(ctx context.Context) *ProjectsLocationsSshKeysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSshKeysDeleteCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "baremetalsolution.projects.locations.sshKeys.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSshKeysDeleteCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSshKeysDeleteCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsSshKeysListCall ¶
added in v0.98.0
type ProjectsLocationsSshKeysListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSshKeysListCall) Context ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) Context(ctx context.Context) *ProjectsLocationsSshKeysListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSshKeysListCall) Do ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) Do(opts ...googleapi.CallOption) (*ListSSHKeysResponse, error)

Do executes the "baremetalsolution.projects.locations.sshKeys.list" call. Any non-2xx status code is an error. Response headers are in either *ListSSHKeysResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSshKeysListCall) Fields ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSshKeysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSshKeysListCall) Header ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSshKeysListCall) IfNoneMatch ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSshKeysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSshKeysListCall) PageSize ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) PageSize(pageSize int64) *ProjectsLocationsSshKeysListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return.

func (*ProjectsLocationsSshKeysListCall) PageToken ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) PageToken(pageToken string) *ProjectsLocationsSshKeysListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous List request, if any.

func (*ProjectsLocationsSshKeysListCall) Pages ¶
added in v0.98.0
func (c *ProjectsLocationsSshKeysListCall) Pages(ctx context.Context, f func(*ListSSHKeysResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsSshKeysService ¶
added in v0.98.0
type ProjectsLocationsSshKeysService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsSshKeysService ¶
added in v0.98.0
func NewProjectsLocationsSshKeysService(s *Service) *ProjectsLocationsSshKeysService
func (*ProjectsLocationsSshKeysService) Create ¶
added in v0.98.0
func (r *ProjectsLocationsSshKeysService) Create(parent string, sshkey *SSHKey) *ProjectsLocationsSshKeysCreateCall

Create: Register a public SSH key in the specified project for use with the interactive serial console feature.

- parent: The parent containing the SSH keys.

func (*ProjectsLocationsSshKeysService) Delete ¶
added in v0.98.0
func (r *ProjectsLocationsSshKeysService) Delete(name string) *ProjectsLocationsSshKeysDeleteCall

Delete: Deletes a public SSH key registered in the specified project.

name: The name of the SSH key to delete. Currently, the only valid value for the location is "global".
func (*ProjectsLocationsSshKeysService) List ¶
added in v0.98.0
func (r *ProjectsLocationsSshKeysService) List(parent string) *ProjectsLocationsSshKeysListCall

List: Lists the public SSH keys registered for the specified project. These SSH keys are used only for the interactive serial console feature.

parent: The parent containing the SSH keys. Currently, the only valid value for the location is "global".
type ProjectsLocationsVolumesEvictCall ¶
added in v0.111.0
type ProjectsLocationsVolumesEvictCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesEvictCall) Context ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesEvictCall) Context(ctx context.Context) *ProjectsLocationsVolumesEvictCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesEvictCall) Do ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesEvictCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.volumes.evict" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesEvictCall) Fields ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesEvictCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesEvictCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesEvictCall) Header ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesEvictCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesGetCall ¶
added in v0.55.0
type ProjectsLocationsVolumesGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesGetCall) Context ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesGetCall) Do ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesGetCall) Do(opts ...googleapi.CallOption) (*Volume, error)

Do executes the "baremetalsolution.projects.locations.volumes.get" call. Any non-2xx status code is an error. Response headers are in either *Volume.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesGetCall) Fields ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesGetCall) Header ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesGetCall) IfNoneMatch ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsVolumesListCall ¶
added in v0.55.0
type ProjectsLocationsVolumesListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesListCall) Context ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Context(ctx context.Context) *ProjectsLocationsVolumesListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesListCall) Do ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Do(opts ...googleapi.CallOption) (*ListVolumesResponse, error)

Do executes the "baremetalsolution.projects.locations.volumes.list" call. Any non-2xx status code is an error. Response headers are in either *ListVolumesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesListCall) Fields ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesListCall) Filter ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Filter(filter string) *ProjectsLocationsVolumesListCall

Filter sets the optional parameter "filter": List filter.

func (*ProjectsLocationsVolumesListCall) Header ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesListCall) IfNoneMatch ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsVolumesListCall) PageSize ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsVolumesListCall) PageToken ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) PageToken(pageToken string) *ProjectsLocationsVolumesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsVolumesListCall) Pages ¶
added in v0.55.0
func (c *ProjectsLocationsVolumesListCall) Pages(ctx context.Context, f func(*ListVolumesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsVolumesLunsEvictCall ¶
added in v0.111.0
type ProjectsLocationsVolumesLunsEvictCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesLunsEvictCall) Context ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesLunsEvictCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsEvictCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesLunsEvictCall) Do ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesLunsEvictCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.volumes.luns.evict" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesLunsEvictCall) Fields ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesLunsEvictCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsEvictCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesLunsEvictCall) Header ¶
added in v0.111.0
func (c *ProjectsLocationsVolumesLunsEvictCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesLunsGetCall ¶
added in v0.60.0
type ProjectsLocationsVolumesLunsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesLunsGetCall) Context ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesLunsGetCall) Do ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsGetCall) Do(opts ...googleapi.CallOption) (*Lun, error)

Do executes the "baremetalsolution.projects.locations.volumes.luns.get" call. Any non-2xx status code is an error. Response headers are in either *Lun.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesLunsGetCall) Fields ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesLunsGetCall) Header ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesLunsGetCall) IfNoneMatch ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesLunsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsVolumesLunsListCall ¶
added in v0.60.0
type ProjectsLocationsVolumesLunsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesLunsListCall) Context ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) Context(ctx context.Context) *ProjectsLocationsVolumesLunsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesLunsListCall) Do ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) Do(opts ...googleapi.CallOption) (*ListLunsResponse, error)

Do executes the "baremetalsolution.projects.locations.volumes.luns.list" call. Any non-2xx status code is an error. Response headers are in either *ListLunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesLunsListCall) Fields ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesLunsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesLunsListCall) Header ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesLunsListCall) IfNoneMatch ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesLunsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsVolumesLunsListCall) PageSize ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesLunsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsVolumesLunsListCall) PageToken ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) PageToken(pageToken string) *ProjectsLocationsVolumesLunsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsVolumesLunsListCall) Pages ¶
added in v0.60.0
func (c *ProjectsLocationsVolumesLunsListCall) Pages(ctx context.Context, f func(*ListLunsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsVolumesLunsService ¶
added in v0.60.0
type ProjectsLocationsVolumesLunsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsVolumesLunsService ¶
added in v0.60.0
func NewProjectsLocationsVolumesLunsService(s *Service) *ProjectsLocationsVolumesLunsService
func (*ProjectsLocationsVolumesLunsService) Evict ¶
added in v0.111.0
func (r *ProjectsLocationsVolumesLunsService) Evict(name string, evictlunrequest *EvictLunRequest) *ProjectsLocationsVolumesLunsEvictCall

Evict: Skips lun's cooloff and deletes it now. Lun must be in cooloff state.

- name: The name of the lun.

func (*ProjectsLocationsVolumesLunsService) Get ¶
added in v0.60.0
func (r *ProjectsLocationsVolumesLunsService) Get(name string) *ProjectsLocationsVolumesLunsGetCall

Get: Get details of a single storage logical unit number(LUN).

- name: Name of the resource.

func (*ProjectsLocationsVolumesLunsService) List ¶
added in v0.60.0
func (r *ProjectsLocationsVolumesLunsService) List(parent string) *ProjectsLocationsVolumesLunsListCall

List: List storage volume luns for given storage volume.

- parent: Parent value for ListLunsRequest.

type ProjectsLocationsVolumesPatchCall ¶
added in v0.62.0
type ProjectsLocationsVolumesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesPatchCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesPatchCall) Context(ctx context.Context) *ProjectsLocationsVolumesPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesPatchCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.volumes.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesPatchCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesPatchCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesPatchCall) UpdateMask ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsVolumesPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. The only currently supported fields are: 'labels'

type ProjectsLocationsVolumesRenameCall ¶
added in v0.114.0
type ProjectsLocationsVolumesRenameCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesRenameCall) Context ¶
added in v0.114.0
func (c *ProjectsLocationsVolumesRenameCall) Context(ctx context.Context) *ProjectsLocationsVolumesRenameCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesRenameCall) Do ¶
added in v0.114.0
func (c *ProjectsLocationsVolumesRenameCall) Do(opts ...googleapi.CallOption) (*Volume, error)

Do executes the "baremetalsolution.projects.locations.volumes.rename" call. Any non-2xx status code is an error. Response headers are in either *Volume.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesRenameCall) Fields ¶
added in v0.114.0
func (c *ProjectsLocationsVolumesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesRenameCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesRenameCall) Header ¶
added in v0.114.0
func (c *ProjectsLocationsVolumesRenameCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesResizeCall ¶
added in v0.84.0
type ProjectsLocationsVolumesResizeCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesResizeCall) Context ¶
added in v0.84.0
func (c *ProjectsLocationsVolumesResizeCall) Context(ctx context.Context) *ProjectsLocationsVolumesResizeCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesResizeCall) Do ¶
added in v0.84.0
func (c *ProjectsLocationsVolumesResizeCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.volumes.resize" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesResizeCall) Fields ¶
added in v0.84.0
func (c *ProjectsLocationsVolumesResizeCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesResizeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesResizeCall) Header ¶
added in v0.84.0
func (c *ProjectsLocationsVolumesResizeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesService ¶
added in v0.55.0
type ProjectsLocationsVolumesService struct {
	Luns *ProjectsLocationsVolumesLunsService

	Snapshots *ProjectsLocationsVolumesSnapshotsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsVolumesService ¶
added in v0.55.0
func NewProjectsLocationsVolumesService(s *Service) *ProjectsLocationsVolumesService
func (*ProjectsLocationsVolumesService) Evict ¶
added in v0.111.0
func (r *ProjectsLocationsVolumesService) Evict(name string, evictvolumerequest *EvictVolumeRequest) *ProjectsLocationsVolumesEvictCall

Evict: Skips volume's cooloff and deletes it now. Volume must be in cooloff state.

- name: The name of the Volume.

func (*ProjectsLocationsVolumesService) Get ¶
added in v0.55.0
func (r *ProjectsLocationsVolumesService) Get(name string) *ProjectsLocationsVolumesGetCall

Get: Get details of a single storage volume.

- name: Name of the resource.

func (*ProjectsLocationsVolumesService) List ¶
added in v0.55.0
func (r *ProjectsLocationsVolumesService) List(parent string) *ProjectsLocationsVolumesListCall

List: List storage volumes in a given project and location.

- parent: Parent value for ListVolumesRequest.

func (*ProjectsLocationsVolumesService) Patch ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesService) Patch(name string, volume *Volume) *ProjectsLocationsVolumesPatchCall

Patch: Update details of a single storage volume.

name: Output only. The resource name of this `Volume`. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. Format: `projects/{project}/locations/{location}/volumes/{volume}`.
func (*ProjectsLocationsVolumesService) Rename ¶
added in v0.114.0
func (r *ProjectsLocationsVolumesService) Rename(name string, renamevolumerequest *RenameVolumeRequest) *ProjectsLocationsVolumesRenameCall

Rename: RenameVolume sets a new name for a volume. Use with caution, previous names become immediately invalidated.

name: The `name` field is used to identify the volume. Format: projects/{project}/locations/{location}/volumes/{volume}.
func (*ProjectsLocationsVolumesService) Resize ¶
added in v0.84.0
func (r *ProjectsLocationsVolumesService) Resize(volume string, resizevolumerequest *ResizeVolumeRequest) *ProjectsLocationsVolumesResizeCall

Resize: Emergency Volume resize.

- volume: Volume to resize.

type ProjectsLocationsVolumesSnapshotsCreateCall ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesSnapshotsCreateCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesSnapshotsCreateCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Do(opts ...googleapi.CallOption) (*VolumeSnapshot, error)

Do executes the "baremetalsolution.projects.locations.volumes.snapshots.create" call. Any non-2xx status code is an error. Response headers are in either *VolumeSnapshot.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesSnapshotsCreateCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesSnapshotsCreateCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesSnapshotsDeleteCall ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesSnapshotsDeleteCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesSnapshotsDeleteCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "baremetalsolution.projects.locations.volumes.snapshots.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesSnapshotsDeleteCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesSnapshotsDeleteCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesSnapshotsGetCall ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesSnapshotsGetCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesSnapshotsGetCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Do(opts ...googleapi.CallOption) (*VolumeSnapshot, error)

Do executes the "baremetalsolution.projects.locations.volumes.snapshots.get" call. Any non-2xx status code is an error. Response headers are in either *VolumeSnapshot.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesSnapshotsGetCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesSnapshotsGetCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesSnapshotsGetCall) IfNoneMatch ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesSnapshotsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsVolumesSnapshotsListCall ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesSnapshotsListCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesSnapshotsListCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) Do(opts ...googleapi.CallOption) (*ListVolumeSnapshotsResponse, error)

Do executes the "baremetalsolution.projects.locations.volumes.snapshots.list" call. Any non-2xx status code is an error. Response headers are in either *ListVolumeSnapshotsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesSnapshotsListCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesSnapshotsListCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsVolumesSnapshotsListCall) IfNoneMatch ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsVolumesSnapshotsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsVolumesSnapshotsListCall) PageSize ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) PageSize(pageSize int64) *ProjectsLocationsVolumesSnapshotsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server might return fewer items than requested. If unspecified, server will pick an appropriate default.

func (*ProjectsLocationsVolumesSnapshotsListCall) PageToken ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) PageToken(pageToken string) *ProjectsLocationsVolumesSnapshotsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results from the server.

func (*ProjectsLocationsVolumesSnapshotsListCall) Pages ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsListCall) Pages(ctx context.Context, f func(*ListVolumeSnapshotsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Context ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Context(ctx context.Context) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Do ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "baremetalsolution.projects.locations.volumes.snapshots.restoreVolumeSnapshot" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Fields ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Fields(s ...googleapi.Field) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Header ¶
added in v0.62.0
func (c *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsVolumesSnapshotsService ¶
added in v0.62.0
type ProjectsLocationsVolumesSnapshotsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsVolumesSnapshotsService ¶
added in v0.62.0
func NewProjectsLocationsVolumesSnapshotsService(s *Service) *ProjectsLocationsVolumesSnapshotsService
func (*ProjectsLocationsVolumesSnapshotsService) Create ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesSnapshotsService) Create(parent string, volumesnapshot *VolumeSnapshot) *ProjectsLocationsVolumesSnapshotsCreateCall

Create: Takes a snapshot of a boot volume. Returns INVALID_ARGUMENT if called for a non-boot volume.

- parent: The volume to snapshot.

func (*ProjectsLocationsVolumesSnapshotsService) Delete ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesSnapshotsService) Delete(name string) *ProjectsLocationsVolumesSnapshotsDeleteCall

Delete: Deletes a volume snapshot. Returns INVALID_ARGUMENT if called for a non-boot volume.

- name: The name of the snapshot to delete.

func (*ProjectsLocationsVolumesSnapshotsService) Get ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesSnapshotsService) Get(name string) *ProjectsLocationsVolumesSnapshotsGetCall

Get: Returns the specified snapshot resource. Returns INVALID_ARGUMENT if called for a non-boot volume.

- name: The name of the snapshot.

func (*ProjectsLocationsVolumesSnapshotsService) List ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesSnapshotsService) List(parent string) *ProjectsLocationsVolumesSnapshotsListCall

List: Retrieves the list of snapshots for the specified volume. Returns a response with an empty list of snapshots if called for a non-boot volume.

- parent: Parent value for ListVolumesRequest.

func (*ProjectsLocationsVolumesSnapshotsService) RestoreVolumeSnapshot ¶
added in v0.62.0
func (r *ProjectsLocationsVolumesSnapshotsService) RestoreVolumeSnapshot(volumeSnapshot string, restorevolumesnapshotrequest *RestoreVolumeSnapshotRequest) *ProjectsLocationsVolumesSnapshotsRestoreVolumeSnapshotCall

RestoreVolumeSnapshot: Uses the specified snapshot to restore its parent volume. Returns INVALID_ARGUMENT if called for a non-boot volume.

volumeSnapshot: Name of the snapshot which will be used to restore its parent volume.
type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type ProvisioningConfig ¶
added in v0.69.0
type ProvisioningConfig struct {
	// CloudConsoleUri: Output only. URI to Cloud Console UI view of this
	// provisioning config.
	CloudConsoleUri string `json:"cloudConsoleUri,omitempty"`
	// CustomId: Optional. The user-defined identifier of the provisioning config.
	CustomId string `json:"customId,omitempty"`
	// Email: Email provided to send a confirmation with provisioning config to.
	// Deprecated in favour of email field in request messages.
	Email string `json:"email,omitempty"`
	// HandoverServiceAccount: A service account to enable customers to access
	// instance credentials upon handover.
	HandoverServiceAccount string `json:"handoverServiceAccount,omitempty"`
	// Instances: Instances to be created.
	Instances []*InstanceConfig `json:"instances,omitempty"`
	// Location: Optional. Location name of this ProvisioningConfig. It is optional
	// only for Intake UI transition period.
	Location string `json:"location,omitempty"`
	// Name: Output only. The system-generated name of the provisioning config.
	// This follows the UUID format.
	Name string `json:"name,omitempty"`
	// Networks: Networks to be created.
	Networks []*NetworkConfig `json:"networks,omitempty"`
	// Pod: Optional. Pod name. Pod is an independent part of infrastructure.
	// Instance can be connected to the assets (networks, volumes, nfsshares)
	// allocated in the same pod only.
	Pod string `json:"pod,omitempty"`
	// State: Output only. State of ProvisioningConfig.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State wasn't specified.
	//   "DRAFT" - ProvisioningConfig is a draft and can be freely modified.
	//   "SUBMITTED" - ProvisioningConfig was already submitted and cannot be
	// modified.
	//   "PROVISIONING" - ProvisioningConfig was in the provisioning state.
	// Initially this state comes from the work order table in big query when SNOW
	// is used. Later this field can be set by the work order API.
	//   "PROVISIONED" - ProvisioningConfig was provisioned, meaning the resources
	// exist.
	//   "VALIDATED" - ProvisioningConfig was validated. A validation tool will be
	// run to set this state.
	//   "CANCELLED" - ProvisioningConfig was canceled.
	//   "FAILED" - The request is submitted for provisioning, with error return.
	State string `json:"state,omitempty"`
	// StatusMessage: Optional status messages associated with the FAILED state.
	StatusMessage string `json:"statusMessage,omitempty"`
	// TicketId: A generated ticket id to track provisioning request.
	TicketId string `json:"ticketId,omitempty"`
	// UpdateTime: Output only. Last update timestamp.
	UpdateTime string `json:"updateTime,omitempty"`
	// Volumes: Volumes to be created.
	Volumes []*VolumeConfig `json:"volumes,omitempty"`
	// VpcScEnabled: If true, VPC SC is enabled for the cluster.
	VpcScEnabled bool `json:"vpcScEnabled,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CloudConsoleUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CloudConsoleUri") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProvisioningConfig: A provisioning configuration.

func (ProvisioningConfig) MarshalJSON ¶
added in v0.69.0
func (s ProvisioningConfig) MarshalJSON() ([]byte, error)
type ProvisioningQuota ¶
added in v0.69.0
type ProvisioningQuota struct {
	// AssetType: The asset type of this provisioning quota.
	//
	// Possible values:
	//   "ASSET_TYPE_UNSPECIFIED" - The unspecified type.
	//   "ASSET_TYPE_SERVER" - The server asset type.
	//   "ASSET_TYPE_STORAGE" - The storage asset type.
	//   "ASSET_TYPE_NETWORK" - The network asset type.
	AssetType string `json:"assetType,omitempty"`
	// AvailableCount: The available count of the provisioning quota.
	AvailableCount int64 `json:"availableCount,omitempty"`
	// GcpService: The gcp service of the provisioning quota.
	GcpService string `json:"gcpService,omitempty"`
	// InstanceQuota: Instance quota.
	InstanceQuota *InstanceQuota `json:"instanceQuota,omitempty"`
	// Location: The specific location of the provisioining quota.
	Location string `json:"location,omitempty"`
	// Name: Output only. The name of the provisioning quota.
	Name string `json:"name,omitempty"`
	// NetworkBandwidth: Network bandwidth, Gbps
	NetworkBandwidth int64 `json:"networkBandwidth,omitempty,string"`
	// ServerCount: Server count.
	ServerCount int64 `json:"serverCount,omitempty,string"`
	// StorageGib: Storage size (GB).
	StorageGib int64 `json:"storageGib,omitempty,string"`
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

ProvisioningQuota: A provisioning quota for a given project.

func (ProvisioningQuota) MarshalJSON ¶
added in v0.69.0
func (s ProvisioningQuota) MarshalJSON() ([]byte, error)
type QosPolicy ¶
added in v0.66.0
type QosPolicy struct {
	// BandwidthGbps: The bandwidth permitted by the QOS policy, in gbps.
	BandwidthGbps float64 `json:"bandwidthGbps,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BandwidthGbps") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BandwidthGbps") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

QosPolicy: QOS policy parameters.

func (QosPolicy) MarshalJSON ¶
added in v0.66.0
func (s QosPolicy) MarshalJSON() ([]byte, error)
func (*QosPolicy) UnmarshalJSON ¶
added in v0.66.0
func (s *QosPolicy) UnmarshalJSON(data []byte) error
type ReimageInstanceRequest ¶
added in v0.178.0
type ReimageInstanceRequest struct {
	// KmsKeyVersion: Optional. Name of the KMS crypto key version used to encrypt
	// the initial passwords. The key has to have ASYMMETRIC_DECRYPT purpose.
	// Format is
	// `projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/
	// cryptoKeyVersions/{version}`.
	KmsKeyVersion string `json:"kmsKeyVersion,omitempty"`
	// OsImage: Required. The OS image code of the image which will be used in the
	// reimage operation.
	OsImage string `json:"osImage,omitempty"`
	// SshKeys: Optional. List of SSH Keys used during reimaging an instance.
	SshKeys []string `json:"sshKeys,omitempty"`
	// ForceSendFields is a list of field names (e.g. "KmsKeyVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KmsKeyVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReimageInstanceRequest: Message requesting to perform reimage operation on a server.

func (ReimageInstanceRequest) MarshalJSON ¶
added in v0.178.0
func (s ReimageInstanceRequest) MarshalJSON() ([]byte, error)
type RenameInstanceRequest ¶
added in v0.111.0
type RenameInstanceRequest struct {
	// NewInstanceId: Required. The new `id` of the instance.
	NewInstanceId string `json:"newInstanceId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewInstanceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewInstanceId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RenameInstanceRequest: Message requesting rename of a server.

func (RenameInstanceRequest) MarshalJSON ¶
added in v0.111.0
func (s RenameInstanceRequest) MarshalJSON() ([]byte, error)
type RenameNetworkRequest ¶
added in v0.114.0
type RenameNetworkRequest struct {
	// NewNetworkId: Required. The new `id` of the network.
	NewNetworkId string `json:"newNetworkId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewNetworkId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewNetworkId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RenameNetworkRequest: Message requesting rename of a server.

func (RenameNetworkRequest) MarshalJSON ¶
added in v0.114.0
func (s RenameNetworkRequest) MarshalJSON() ([]byte, error)
type RenameNfsShareRequest ¶
added in v0.114.0
type RenameNfsShareRequest struct {
	// NewNfsshareId: Required. The new `id` of the nfsshare.
	NewNfsshareId string `json:"newNfsshareId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewNfsshareId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewNfsshareId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RenameNfsShareRequest: Message requesting rename of a server.

func (RenameNfsShareRequest) MarshalJSON ¶
added in v0.114.0
func (s RenameNfsShareRequest) MarshalJSON() ([]byte, error)
type RenameVolumeRequest ¶
added in v0.114.0
type RenameVolumeRequest struct {
	// NewVolumeId: Required. The new `id` of the volume.
	NewVolumeId string `json:"newVolumeId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewVolumeId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewVolumeId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RenameVolumeRequest: Message requesting rename of a server.

func (RenameVolumeRequest) MarshalJSON ¶
added in v0.114.0
func (s RenameVolumeRequest) MarshalJSON() ([]byte, error)
type ResetInstanceRequest ¶
added in v0.62.0
type ResetInstanceRequest struct {
}

ResetInstanceRequest: Message requesting to reset a server.

type ResetInstanceResponse ¶
added in v0.125.0
type ResetInstanceResponse struct {
}

ResetInstanceResponse: Response message from resetting a server.

type ResizeVolumeRequest ¶
added in v0.84.0
type ResizeVolumeRequest struct {
	// SizeGib: New Volume size, in GiB.
	SizeGib int64 `json:"sizeGib,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "SizeGib") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SizeGib") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ResizeVolumeRequest: Request for emergency resize Volume.

func (ResizeVolumeRequest) MarshalJSON ¶
added in v0.84.0
func (s ResizeVolumeRequest) MarshalJSON() ([]byte, error)
type RestoreVolumeSnapshotRequest ¶
added in v0.62.0
type RestoreVolumeSnapshotRequest struct {
}

RestoreVolumeSnapshotRequest: Message for restoring a volume snapshot.

type SSHKey ¶
added in v0.98.0
type SSHKey struct {
	// Name: Output only. The name of this SSH key. Currently, the only valid value
	// for the location is "global".
	Name string `json:"name,omitempty"`
	// PublicKey: The public SSH key. This must be in OpenSSH .authorized_keys
	// format.
	PublicKey string `json:"publicKey,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

SSHKey: An SSH key, used for authorizing with the interactive serial console feature.

func (SSHKey) MarshalJSON ¶
added in v0.98.0
func (s SSHKey) MarshalJSON() ([]byte, error)
type ServerNetworkTemplate ¶
added in v0.75.0
type ServerNetworkTemplate struct {
	// ApplicableInstanceTypes: Instance types this template is applicable to.
	ApplicableInstanceTypes []string `json:"applicableInstanceTypes,omitempty"`
	// LogicalInterfaces: Logical interfaces.
	LogicalInterfaces []*GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface `json:"logicalInterfaces,omitempty"`
	// Name: Output only. Template's unique name. The full resource name follows
	// the pattern:
	// `projects/{project}/locations/{location}/serverNetworkTemplate/{server_networ
	// k_template}` Generally, the {server_network_template} follows the syntax of
	// "bond" or "nic".
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicableInstanceTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicableInstanceTypes") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServerNetworkTemplate: Network template.

func (ServerNetworkTemplate) MarshalJSON ¶
added in v0.75.0
func (s ServerNetworkTemplate) MarshalJSON() ([]byte, error)
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

type SnapshotReservationDetail ¶
added in v0.55.0
type SnapshotReservationDetail struct {
	// ReservedSpaceGib: The space on this storage volume reserved for snapshots,
	// shown in GiB.
	ReservedSpaceGib int64 `json:"reservedSpaceGib,omitempty,string"`
	// ReservedSpacePercent: Percent of the total Volume size reserved for snapshot
	// copies. Enabling snapshots requires reserving 20% or more of the storage
	// volume space for snapshots. Maximum reserved space for snapshots is 40%.
	// Setting this field will effectively set snapshot_enabled to true.
	ReservedSpacePercent int64 `json:"reservedSpacePercent,omitempty"`
	// ReservedSpaceRemainingGib: The amount, in GiB, of available space in this
	// storage volume's reserved snapshot space.
	ReservedSpaceRemainingGib int64 `json:"reservedSpaceRemainingGib,omitempty,string"`
	// ReservedSpaceUsedPercent: The percent of snapshot space on this storage
	// volume actually being used by the snapshot copies. This value might be
	// higher than 100% if the snapshot copies have overflowed into the data
	// portion of the storage volume.
	ReservedSpaceUsedPercent int64 `json:"reservedSpaceUsedPercent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReservedSpaceGib") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReservedSpaceGib") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SnapshotReservationDetail: Details about snapshot space reservation and usage on the storage volume.

func (SnapshotReservationDetail) MarshalJSON ¶
added in v0.55.0
func (s SnapshotReservationDetail) MarshalJSON() ([]byte, error)
type StartInstanceRequest ¶
added in v0.69.0
type StartInstanceRequest struct {
}

StartInstanceRequest: Message requesting to start a server.

type StartInstanceResponse ¶
added in v0.125.0
type StartInstanceResponse struct {
}

StartInstanceResponse: Response message from starting a server.

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
type StopInstanceRequest ¶
added in v0.76.0
type StopInstanceRequest struct {
}

StopInstanceRequest: Message requesting to stop a server.

type StopInstanceResponse ¶
added in v0.125.0
type StopInstanceResponse struct {
}

StopInstanceResponse: Response message from stopping a server.

type SubmitProvisioningConfigRequest ¶
added in v0.69.0
type SubmitProvisioningConfigRequest struct {
	// Email: Optional. Email provided to send a confirmation with provisioning
	// config to.
	Email string `json:"email,omitempty"`
	// ProvisioningConfig: Required. The ProvisioningConfig to create.
	ProvisioningConfig *ProvisioningConfig `json:"provisioningConfig,omitempty"`
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

SubmitProvisioningConfigRequest: Request for SubmitProvisioningConfig.

func (SubmitProvisioningConfigRequest) MarshalJSON ¶
added in v0.69.0
func (s SubmitProvisioningConfigRequest) MarshalJSON() ([]byte, error)
type SubmitProvisioningConfigResponse ¶
added in v0.69.0
type SubmitProvisioningConfigResponse struct {
	// ProvisioningConfig: The submitted provisioning config.
	ProvisioningConfig *ProvisioningConfig `json:"provisioningConfig,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ProvisioningConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProvisioningConfig") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubmitProvisioningConfigResponse: Response for SubmitProvisioningConfig.

func (SubmitProvisioningConfigResponse) MarshalJSON ¶
added in v0.69.0
func (s SubmitProvisioningConfigResponse) MarshalJSON() ([]byte, error)
type UserAccount ¶
added in v0.154.0
type UserAccount struct {
	// EncryptedPassword: Encrypted initial password value.
	EncryptedPassword string `json:"encryptedPassword,omitempty"`
	// KmsKeyVersion: KMS CryptoKey Version used to encrypt the password.
	KmsKeyVersion string `json:"kmsKeyVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EncryptedPassword") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EncryptedPassword") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserAccount: User account provisioned for the customer.

func (UserAccount) MarshalJSON ¶
added in v0.154.0
func (s UserAccount) MarshalJSON() ([]byte, error)
type VRF ¶
added in v0.60.0
type VRF struct {
	// Name: The name of the VRF.
	Name string `json:"name,omitempty"`
	// QosPolicy: The QOS policy applied to this VRF. The value is only meaningful
	// when all the vlan attachments have the same QoS. This field should not be
	// used for new integrations, use vlan attachment level qos instead. The field
	// is left for backward-compatibility.
	QosPolicy *QosPolicy `json:"qosPolicy,omitempty"`
	// State: The possible state of VRF.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The unspecified state.
	//   "PROVISIONING" - The vrf is provisioning.
	//   "PROVISIONED" - The vrf is provisioned.
	State string `json:"state,omitempty"`
	// VlanAttachments: The list of VLAN attachments for the VRF.
	VlanAttachments []*VlanAttachment `json:"vlanAttachments,omitempty"`
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

VRF: A network VRF.

func (VRF) MarshalJSON ¶
added in v0.60.0
func (s VRF) MarshalJSON() ([]byte, error)
type VlanAttachment ¶
added in v0.66.0
type VlanAttachment struct {
	// Id: Immutable. The identifier of the attachment within vrf.
	Id string `json:"id,omitempty"`
	// InterconnectAttachment: Optional. The name of the vlan attachment within
	// vrf. This is of the form
	// projects/{project_number}/regions/{region}/interconnectAttachments/{interconn
	// ect_attachment}
	InterconnectAttachment string `json:"interconnectAttachment,omitempty"`
	// PairingKey: Input only. Pairing key.
	PairingKey string `json:"pairingKey,omitempty"`
	// PeerIp: The peer IP of the attachment.
	PeerIp string `json:"peerIp,omitempty"`
	// PeerVlanId: The peer vlan ID of the attachment.
	PeerVlanId int64 `json:"peerVlanId,omitempty,string"`
	// QosPolicy: The QOS policy applied to this VLAN attachment. This value should
	// be preferred to using qos at vrf level.
	QosPolicy *QosPolicy `json:"qosPolicy,omitempty"`
	// RouterIp: The router IP of the attachment.
	RouterIp string `json:"routerIp,omitempty"`
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

VlanAttachment: VLAN attachment details.

func (VlanAttachment) MarshalJSON ¶
added in v0.66.0
func (s VlanAttachment) MarshalJSON() ([]byte, error)
type Volume ¶
added in v0.55.0
type Volume struct {
	// Attached: Output only. Is the Volume attached at at least one instance. This
	// field is a lightweight counterpart of `instances` field. It is filled in
	// List responses as well.
	Attached bool `json:"attached,omitempty"`
	// AutoGrownSizeGib: The size, in GiB, that this storage volume has expanded as
	// a result of an auto grow policy. In the absence of auto-grow, the value is
	// 0.
	AutoGrownSizeGib int64 `json:"autoGrownSizeGib,omitempty,string"`
	// BootVolume: Output only. Whether this volume is a boot volume. A boot volume
	// is one which contains a boot LUN.
	BootVolume bool `json:"bootVolume,omitempty"`
	// CurrentSizeGib: The current size of this storage volume, in GiB, including
	// space reserved for snapshots. This size might be different than the
	// requested size if the storage volume has been configured with auto grow or
	// auto shrink.
	CurrentSizeGib int64 `json:"currentSizeGib,omitempty,string"`
	// EmergencySizeGib: Additional emergency size that was requested for this
	// Volume, in GiB. current_size_gib includes this value.
	EmergencySizeGib int64 `json:"emergencySizeGib,omitempty,string"`
	// ExpireTime: Output only. Time after which volume will be fully deleted. It
	// is filled only for volumes in COOLOFF state.
	ExpireTime string `json:"expireTime,omitempty"`
	// Id: An identifier for the `Volume`, generated by the backend.
	Id string `json:"id,omitempty"`
	// Instances: Output only. Instances this Volume is attached to. This field is
	// set only in Get requests.
	Instances []string `json:"instances,omitempty"`
	// Labels: Labels as key value pairs.
	Labels map[string]string `json:"labels,omitempty"`
	// MaxSizeGib: Maximum size volume can be expanded to in case of evergency, in
	// GiB.
	MaxSizeGib int64 `json:"maxSizeGib,omitempty,string"`
	// Name: Output only. The resource name of this `Volume`. Resource names are
	// schemeless URIs that follow the conventions in
	// https://cloud.google.com/apis/design/resource_names. Format:
	// `projects/{project}/locations/{location}/volumes/{volume}`
	Name string `json:"name,omitempty"`
	// Notes: Input only. User-specified notes for new Volume. Used to provision
	// Volumes that require manual intervention.
	Notes string `json:"notes,omitempty"`
	// OriginallyRequestedSizeGib: Originally requested size, in GiB.
	OriginallyRequestedSizeGib int64 `json:"originallyRequestedSizeGib,omitempty,string"`
	// PerformanceTier: Immutable. Performance tier of the Volume. Default is
	// SHARED.
	//
	// Possible values:
	//   "VOLUME_PERFORMANCE_TIER_UNSPECIFIED" - Value is not specified.
	//   "VOLUME_PERFORMANCE_TIER_SHARED" - Regular volumes, shared aggregates.
	//   "VOLUME_PERFORMANCE_TIER_ASSIGNED" - Assigned aggregates.
	//   "VOLUME_PERFORMANCE_TIER_HT" - High throughput aggregates.
	//   "VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE" - QoS 2.0 high performance
	// storage.
	PerformanceTier string `json:"performanceTier,omitempty"`
	// Pod: Immutable. Pod name. Pod is an independent part of infrastructure.
	// Volume can only be connected to the instances allocated in the same pod.
	Pod string `json:"pod,omitempty"`
	// Protocol: Output only. Storage protocol for the Volume.
	//
	// Possible values:
	//   "PROTOCOL_UNSPECIFIED" - Value is not specified.
	//   "FIBRE_CHANNEL" - Fibre Channel protocol.
	//   "NFS" - NFS protocol means Volume is a NFS Share volume. Such volumes
	// cannot be manipulated via Volumes API.
	Protocol string `json:"protocol,omitempty"`
	// RemainingSpaceGib: The space remaining in the storage volume for new LUNs,
	// in GiB, excluding space reserved for snapshots.
	RemainingSpaceGib int64 `json:"remainingSpaceGib,omitempty,string"`
	// RequestedSizeGib: The requested size of this storage volume, in GiB.
	RequestedSizeGib int64 `json:"requestedSizeGib,omitempty,string"`
	// SnapshotAutoDeleteBehavior: The behavior to use when snapshot reserved space
	// is full.
	//
	// Possible values:
	//   "SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED" - The unspecified behavior.
	//   "DISABLED" - Don't delete any snapshots. This disables new snapshot
	// creation, as long as the snapshot reserved space is full.
	//   "OLDEST_FIRST" - Delete the oldest snapshots first.
	//   "NEWEST_FIRST" - Delete the newest snapshots first.
	SnapshotAutoDeleteBehavior string `json:"snapshotAutoDeleteBehavior,omitempty"`
	// SnapshotEnabled: Whether snapshots are enabled.
	SnapshotEnabled bool `json:"snapshotEnabled,omitempty"`
	// SnapshotReservationDetail: Details about snapshot space reservation and
	// usage on the storage volume.
	SnapshotReservationDetail *SnapshotReservationDetail `json:"snapshotReservationDetail,omitempty"`
	// State: The state of this storage volume.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The storage volume is in an unknown state.
	//   "CREATING" - The storage volume is being created.
	//   "READY" - The storage volume is ready for use.
	//   "DELETING" - The storage volume has been requested to be deleted.
	//   "UPDATING" - The storage volume is being updated.
	//   "COOL_OFF" - The storage volume is in cool off state. It will be deleted
	// after `expire_time`.
	State string `json:"state,omitempty"`
	// StorageType: The storage type for this volume.
	//
	// Possible values:
	//   "STORAGE_TYPE_UNSPECIFIED" - The storage type for this volume is unknown.
	//   "SSD" - The storage type for this volume is SSD.
	//   "HDD" - This storage type for this volume is HDD.
	StorageType string `json:"storageType,omitempty"`
	// WorkloadProfile: The workload profile for the volume.
	//
	// Possible values:
	//   "WORKLOAD_PROFILE_UNSPECIFIED" - The workload profile is in an unknown
	// state.
	//   "GENERIC" - The workload profile is generic.
	//   "HANA" - The workload profile is hana.
	WorkloadProfile string `json:"workloadProfile,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Attached") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attached") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Volume: A storage volume.

func (Volume) MarshalJSON ¶
added in v0.55.0
func (s Volume) MarshalJSON() ([]byte, error)
type VolumeConfig ¶
added in v0.69.0
type VolumeConfig struct {
	// GcpService: The GCP service of the storage volume. Available gcp_service are
	// in https://cloud.google.com/bare-metal/docs/bms-planning.
	GcpService string `json:"gcpService,omitempty"`
	// Id: A transient unique identifier to identify a volume within an
	// ProvisioningConfig request.
	Id string `json:"id,omitempty"`
	// LunRanges: LUN ranges to be configured. Set only when protocol is
	// PROTOCOL_FC.
	LunRanges []*LunRange `json:"lunRanges,omitempty"`
	// MachineIds: Machine ids connected to this volume. Set only when protocol is
	// PROTOCOL_FC.
	MachineIds []string `json:"machineIds,omitempty"`
	// Name: Output only. The name of the volume config.
	Name string `json:"name,omitempty"`
	// NfsExports: NFS exports. Set only when protocol is PROTOCOL_NFS.
	NfsExports []*NfsExport `json:"nfsExports,omitempty"`
	// PerformanceTier: Performance tier of the Volume. Default is SHARED.
	//
	// Possible values:
	//   "VOLUME_PERFORMANCE_TIER_UNSPECIFIED" - Value is not specified.
	//   "VOLUME_PERFORMANCE_TIER_SHARED" - Regular volumes, shared aggregates.
	//   "VOLUME_PERFORMANCE_TIER_ASSIGNED" - Assigned aggregates.
	//   "VOLUME_PERFORMANCE_TIER_HT" - High throughput aggregates.
	//   "VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE" - QoS 2.0 high performance
	// storage.
	PerformanceTier string `json:"performanceTier,omitempty"`
	// Protocol: Volume protocol.
	//
	// Possible values:
	//   "PROTOCOL_UNSPECIFIED" - Unspecified value.
	//   "PROTOCOL_FC" - Fibre channel.
	//   "PROTOCOL_NFS" - Network file system.
	Protocol string `json:"protocol,omitempty"`
	// SizeGb: The requested size of this volume, in GB.
	SizeGb int64 `json:"sizeGb,omitempty"`
	// SnapshotsEnabled: Whether snapshots should be enabled.
	SnapshotsEnabled bool `json:"snapshotsEnabled,omitempty"`
	// Type: The type of this Volume.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - The unspecified type.
	//   "FLASH" - This Volume is on flash.
	//   "DISK" - This Volume is on disk.
	Type string `json:"type,omitempty"`
	// UserNote: User note field, it can be used by customers to add additional
	// information for the BMS Ops team .
	UserNote string `json:"userNote,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GcpService") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcpService") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VolumeConfig: Configuration parameters for a new volume.

func (VolumeConfig) MarshalJSON ¶
added in v0.69.0
func (s VolumeConfig) MarshalJSON() ([]byte, error)
type VolumeSnapshot ¶
added in v0.62.0
type VolumeSnapshot struct {
	// CreateTime: Output only. The creation time of the snapshot.
	CreateTime string `json:"createTime,omitempty"`
	// Description: The description of the snapshot.
	Description string `json:"description,omitempty"`
	// Id: Output only. An identifier for the snapshot, generated by the backend.
	Id string `json:"id,omitempty"`
	// Name: The name of the snapshot.
	Name string `json:"name,omitempty"`
	// StorageVolume: Output only. The name of the volume which this snapshot
	// belongs to.
	StorageVolume string `json:"storageVolume,omitempty"`
	// Type: Output only. The type of the snapshot which indicates whether it was
	// scheduled or manual/ad-hoc.
	//
	// Possible values:
	//   "SNAPSHOT_TYPE_UNSPECIFIED" - Type is not specified.
	//   "AD_HOC" - Snapshot was taken manually by user.
	//   "SCHEDULED" - Snapshot was taken automatically as a part of a snapshot
	// schedule.
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

VolumeSnapshot: A snapshot of a volume. Only boot volumes can have snapshots.

func (VolumeSnapshot) MarshalJSON ¶
added in v0.62.0
func (s VolumeSnapshot) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
baremetalsolution-gen.go
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
