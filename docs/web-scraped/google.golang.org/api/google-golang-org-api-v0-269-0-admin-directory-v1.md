# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/directory/v1

Title: admin package - google.golang.org/api/admin/directory/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/admin/directory/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
admin
 
directory
 
v1
admin
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 318
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

Package admin provides access to the Admin SDK API.

For product documentation, see: https://developers.google.com/workspace/admin/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/admin/directory/v1"
...
ctx := context.Background()
adminService, err := admin.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

adminService, err := admin.NewService(ctx, option.WithScopes(admin.CloudPlatformScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

adminService, err := admin.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adminService, err := admin.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Alias
func (s Alias) MarshalJSON() ([]byte, error)
type Aliases
func (s Aliases) MarshalJSON() ([]byte, error)
type Asp
func (s Asp) MarshalJSON() ([]byte, error)
type Asps
func (s Asps) MarshalJSON() ([]byte, error)
type AspsDeleteCall
func (c *AspsDeleteCall) Context(ctx context.Context) *AspsDeleteCall
func (c *AspsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *AspsDeleteCall) Fields(s ...googleapi.Field) *AspsDeleteCall
func (c *AspsDeleteCall) Header() http.Header
type AspsGetCall
func (c *AspsGetCall) Context(ctx context.Context) *AspsGetCall
func (c *AspsGetCall) Do(opts ...googleapi.CallOption) (*Asp, error)
func (c *AspsGetCall) Fields(s ...googleapi.Field) *AspsGetCall
func (c *AspsGetCall) Header() http.Header
func (c *AspsGetCall) IfNoneMatch(entityTag string) *AspsGetCall
type AspsListCall
func (c *AspsListCall) Context(ctx context.Context) *AspsListCall
func (c *AspsListCall) Do(opts ...googleapi.CallOption) (*Asps, error)
func (c *AspsListCall) Fields(s ...googleapi.Field) *AspsListCall
func (c *AspsListCall) Header() http.Header
func (c *AspsListCall) IfNoneMatch(entityTag string) *AspsListCall
type AspsService
func NewAspsService(s *Service) *AspsService
func (r *AspsService) Delete(userKey string, codeId int64) *AspsDeleteCall
func (r *AspsService) Get(userKey string, codeId int64) *AspsGetCall
func (r *AspsService) List(userKey string) *AspsListCall
type AuxiliaryMessage
func (s AuxiliaryMessage) MarshalJSON() ([]byte, error)
type BacklightInfo
func (s BacklightInfo) MarshalJSON() ([]byte, error)
type BatchChangeChromeOsDeviceStatusRequest
func (s BatchChangeChromeOsDeviceStatusRequest) MarshalJSON() ([]byte, error)
type BatchChangeChromeOsDeviceStatusResponse
func (s BatchChangeChromeOsDeviceStatusResponse) MarshalJSON() ([]byte, error)
type BatchCreatePrintServersRequest
func (s BatchCreatePrintServersRequest) MarshalJSON() ([]byte, error)
type BatchCreatePrintServersResponse
func (s BatchCreatePrintServersResponse) MarshalJSON() ([]byte, error)
type BatchCreatePrintersRequest
func (s BatchCreatePrintersRequest) MarshalJSON() ([]byte, error)
type BatchCreatePrintersResponse
func (s BatchCreatePrintersResponse) MarshalJSON() ([]byte, error)
type BatchDeletePrintServersRequest
func (s BatchDeletePrintServersRequest) MarshalJSON() ([]byte, error)
type BatchDeletePrintServersResponse
func (s BatchDeletePrintServersResponse) MarshalJSON() ([]byte, error)
type BatchDeletePrintersRequest
func (s BatchDeletePrintersRequest) MarshalJSON() ([]byte, error)
type BatchDeletePrintersResponse
func (s BatchDeletePrintersResponse) MarshalJSON() ([]byte, error)
type BluetoothAdapterInfo
func (s BluetoothAdapterInfo) MarshalJSON() ([]byte, error)
type Building
func (s Building) MarshalJSON() ([]byte, error)
type BuildingAddress
func (s BuildingAddress) MarshalJSON() ([]byte, error)
type BuildingCoordinates
func (s BuildingCoordinates) MarshalJSON() ([]byte, error)
func (s *BuildingCoordinates) UnmarshalJSON(data []byte) error
type Buildings
func (s Buildings) MarshalJSON() ([]byte, error)
type ByteUsage
func (s ByteUsage) MarshalJSON() ([]byte, error)
type CalendarResource
func (s CalendarResource) MarshalJSON() ([]byte, error)
type CalendarResources
func (s CalendarResources) MarshalJSON() ([]byte, error)
type ChangeChromeOsDeviceStatusResult
func (s ChangeChromeOsDeviceStatusResult) MarshalJSON() ([]byte, error)
type ChangeChromeOsDeviceStatusSucceeded
type Channel
func (s Channel) MarshalJSON() ([]byte, error)
type ChannelsService
func NewChannelsService(s *Service) *ChannelsService
func (r *ChannelsService) Stop(channel *Channel) *ChannelsStopCall
type ChannelsStopCall
func (c *ChannelsStopCall) Context(ctx context.Context) *ChannelsStopCall
func (c *ChannelsStopCall) Do(opts ...googleapi.CallOption) error
func (c *ChannelsStopCall) Fields(s ...googleapi.Field) *ChannelsStopCall
func (c *ChannelsStopCall) Header() http.Header
type ChromeOsDevice
func (s ChromeOsDevice) MarshalJSON() ([]byte, error)
type ChromeOsDeviceAction
func (s ChromeOsDeviceAction) MarshalJSON() ([]byte, error)
type ChromeOsDeviceActiveTimeRanges
func (s ChromeOsDeviceActiveTimeRanges) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfo
func (s ChromeOsDeviceCpuInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfoLogicalCpus
func (s ChromeOsDeviceCpuInfoLogicalCpus) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfoLogicalCpusCStates
func (s ChromeOsDeviceCpuInfoLogicalCpusCStates) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuStatusReports
func (s ChromeOsDeviceCpuStatusReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo
func (s ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDeviceFiles
func (s ChromeOsDeviceDeviceFiles) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDiskVolumeReports
func (s ChromeOsDeviceDiskVolumeReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDiskVolumeReportsVolumeInfo
func (s ChromeOsDeviceDiskVolumeReportsVolumeInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceLastKnownNetwork
func (s ChromeOsDeviceLastKnownNetwork) MarshalJSON() ([]byte, error)
type ChromeOsDeviceRecentUsers
func (s ChromeOsDeviceRecentUsers) MarshalJSON() ([]byte, error)
type ChromeOsDeviceScreenshotFiles
func (s ChromeOsDeviceScreenshotFiles) MarshalJSON() ([]byte, error)
type ChromeOsDeviceSystemRamFreeReports
func (s ChromeOsDeviceSystemRamFreeReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceTpmVersionInfo
func (s ChromeOsDeviceTpmVersionInfo) MarshalJSON() ([]byte, error)
type ChromeOsDevices
func (s ChromeOsDevices) MarshalJSON() ([]byte, error)
type ChromeOsMoveDevicesToOu
func (s ChromeOsMoveDevicesToOu) MarshalJSON() ([]byte, error)
type ChromeosdevicesActionCall
func (c *ChromeosdevicesActionCall) Context(ctx context.Context) *ChromeosdevicesActionCall
func (c *ChromeosdevicesActionCall) Do(opts ...googleapi.CallOption) error
func (c *ChromeosdevicesActionCall) Fields(s ...googleapi.Field) *ChromeosdevicesActionCall
func (c *ChromeosdevicesActionCall) Header() http.Header
type ChromeosdevicesGetCall
func (c *ChromeosdevicesGetCall) Context(ctx context.Context) *ChromeosdevicesGetCall
func (c *ChromeosdevicesGetCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)
func (c *ChromeosdevicesGetCall) Fields(s ...googleapi.Field) *ChromeosdevicesGetCall
func (c *ChromeosdevicesGetCall) Header() http.Header
func (c *ChromeosdevicesGetCall) IfNoneMatch(entityTag string) *ChromeosdevicesGetCall
func (c *ChromeosdevicesGetCall) Projection(projection string) *ChromeosdevicesGetCall
type ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) Context(ctx context.Context) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevices, error)
func (c *ChromeosdevicesListCall) Fields(s ...googleapi.Field) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) Header() http.Header
func (c *ChromeosdevicesListCall) IfNoneMatch(entityTag string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) IncludeChildOrgunits(includeChildOrgunits bool) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) MaxResults(maxResults int64) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) OrderBy(orderBy string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) OrgUnitPath(orgUnitPath string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) PageToken(pageToken string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) Pages(ctx context.Context, f func(*ChromeOsDevices) error) error
func (c *ChromeosdevicesListCall) Projection(projection string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) Query(query string) *ChromeosdevicesListCall
func (c *ChromeosdevicesListCall) SortOrder(sortOrder string) *ChromeosdevicesListCall
type ChromeosdevicesMoveDevicesToOuCall
func (c *ChromeosdevicesMoveDevicesToOuCall) Context(ctx context.Context) *ChromeosdevicesMoveDevicesToOuCall
func (c *ChromeosdevicesMoveDevicesToOuCall) Do(opts ...googleapi.CallOption) error
func (c *ChromeosdevicesMoveDevicesToOuCall) Fields(s ...googleapi.Field) *ChromeosdevicesMoveDevicesToOuCall
func (c *ChromeosdevicesMoveDevicesToOuCall) Header() http.Header
type ChromeosdevicesPatchCall
func (c *ChromeosdevicesPatchCall) Context(ctx context.Context) *ChromeosdevicesPatchCall
func (c *ChromeosdevicesPatchCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)
func (c *ChromeosdevicesPatchCall) Fields(s ...googleapi.Field) *ChromeosdevicesPatchCall
func (c *ChromeosdevicesPatchCall) Header() http.Header
func (c *ChromeosdevicesPatchCall) Projection(projection string) *ChromeosdevicesPatchCall
type ChromeosdevicesService
func NewChromeosdevicesService(s *Service) *ChromeosdevicesService
func (r *ChromeosdevicesService) Action(customerId string, resourceId string, ...) *ChromeosdevicesActionCall
func (r *ChromeosdevicesService) Get(customerId string, deviceId string) *ChromeosdevicesGetCall
func (r *ChromeosdevicesService) List(customerId string) *ChromeosdevicesListCall
func (r *ChromeosdevicesService) MoveDevicesToOu(customerId string, orgUnitPath string, ...) *ChromeosdevicesMoveDevicesToOuCall
func (r *ChromeosdevicesService) Patch(customerId string, deviceId string, chromeosdevice *ChromeOsDevice) *ChromeosdevicesPatchCall
func (r *ChromeosdevicesService) Update(customerId string, deviceId string, chromeosdevice *ChromeOsDevice) *ChromeosdevicesUpdateCall
type ChromeosdevicesUpdateCall
func (c *ChromeosdevicesUpdateCall) Context(ctx context.Context) *ChromeosdevicesUpdateCall
func (c *ChromeosdevicesUpdateCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)
func (c *ChromeosdevicesUpdateCall) Fields(s ...googleapi.Field) *ChromeosdevicesUpdateCall
func (c *ChromeosdevicesUpdateCall) Header() http.Header
func (c *ChromeosdevicesUpdateCall) Projection(projection string) *ChromeosdevicesUpdateCall
type CountChromeOsDevicesResponse
func (s CountChromeOsDevicesResponse) MarshalJSON() ([]byte, error)
type CreatePrintServerRequest
func (s CreatePrintServerRequest) MarshalJSON() ([]byte, error)
type CreatePrinterRequest
func (s CreatePrinterRequest) MarshalJSON() ([]byte, error)
type Customer
func (s Customer) MarshalJSON() ([]byte, error)
type CustomerDevicesChromeosBatchChangeStatusCall
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Context(ctx context.Context) *CustomerDevicesChromeosBatchChangeStatusCall
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Do(opts ...googleapi.CallOption) (*BatchChangeChromeOsDeviceStatusResponse, error)
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosBatchChangeStatusCall
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Header() http.Header
type CustomerDevicesChromeosCommandsGetCall
func (c *CustomerDevicesChromeosCommandsGetCall) Context(ctx context.Context) *CustomerDevicesChromeosCommandsGetCall
func (c *CustomerDevicesChromeosCommandsGetCall) Do(opts ...googleapi.CallOption) (*DirectoryChromeosdevicesCommand, error)
func (c *CustomerDevicesChromeosCommandsGetCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosCommandsGetCall
func (c *CustomerDevicesChromeosCommandsGetCall) Header() http.Header
func (c *CustomerDevicesChromeosCommandsGetCall) IfNoneMatch(entityTag string) *CustomerDevicesChromeosCommandsGetCall
type CustomerDevicesChromeosCommandsService
func NewCustomerDevicesChromeosCommandsService(s *Service) *CustomerDevicesChromeosCommandsService
func (r *CustomerDevicesChromeosCommandsService) Get(customerId string, deviceId string, commandId int64) *CustomerDevicesChromeosCommandsGetCall
type CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Context(ctx context.Context) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Do(opts ...googleapi.CallOption) (*CountChromeOsDevicesResponse, error)
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Filter(filter string) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Header() http.Header
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) IfNoneMatch(entityTag string) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) IncludeChildOrgunits(includeChildOrgunits bool) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) OrgUnitPath(orgUnitPath string) *CustomerDevicesChromeosCountChromeOsDevicesCall
type CustomerDevicesChromeosIssueCommandCall
func (c *CustomerDevicesChromeosIssueCommandCall) Context(ctx context.Context) *CustomerDevicesChromeosIssueCommandCall
func (c *CustomerDevicesChromeosIssueCommandCall) Do(opts ...googleapi.CallOption) (*DirectoryChromeosdevicesIssueCommandResponse, error)
func (c *CustomerDevicesChromeosIssueCommandCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosIssueCommandCall
func (c *CustomerDevicesChromeosIssueCommandCall) Header() http.Header
type CustomerDevicesChromeosService
func NewCustomerDevicesChromeosService(s *Service) *CustomerDevicesChromeosService
func (r *CustomerDevicesChromeosService) BatchChangeStatus(customerId string, ...) *CustomerDevicesChromeosBatchChangeStatusCall
func (r *CustomerDevicesChromeosService) CountChromeOsDevices(customerId string) *CustomerDevicesChromeosCountChromeOsDevicesCall
func (r *CustomerDevicesChromeosService) IssueCommand(customerId string, deviceId string, ...) *CustomerDevicesChromeosIssueCommandCall
type CustomerDevicesService
func NewCustomerDevicesService(s *Service) *CustomerDevicesService
type CustomerPostalAddress
func (s CustomerPostalAddress) MarshalJSON() ([]byte, error)
type CustomerService
func NewCustomerService(s *Service) *CustomerService
type CustomersChromePrintServersBatchCreatePrintServersCall
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Context(ctx context.Context) *CustomersChromePrintServersBatchCreatePrintServersCall
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Do(opts ...googleapi.CallOption) (*BatchCreatePrintServersResponse, error)
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersBatchCreatePrintServersCall
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Header() http.Header
type CustomersChromePrintServersBatchDeletePrintServersCall
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Context(ctx context.Context) *CustomersChromePrintServersBatchDeletePrintServersCall
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Do(opts ...googleapi.CallOption) (*BatchDeletePrintServersResponse, error)
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersBatchDeletePrintServersCall
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Header() http.Header
type CustomersChromePrintServersCreateCall
func (c *CustomersChromePrintServersCreateCall) Context(ctx context.Context) *CustomersChromePrintServersCreateCall
func (c *CustomersChromePrintServersCreateCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)
func (c *CustomersChromePrintServersCreateCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersCreateCall
func (c *CustomersChromePrintServersCreateCall) Header() http.Header
type CustomersChromePrintServersDeleteCall
func (c *CustomersChromePrintServersDeleteCall) Context(ctx context.Context) *CustomersChromePrintServersDeleteCall
func (c *CustomersChromePrintServersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *CustomersChromePrintServersDeleteCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersDeleteCall
func (c *CustomersChromePrintServersDeleteCall) Header() http.Header
type CustomersChromePrintServersGetCall
func (c *CustomersChromePrintServersGetCall) Context(ctx context.Context) *CustomersChromePrintServersGetCall
func (c *CustomersChromePrintServersGetCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)
func (c *CustomersChromePrintServersGetCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersGetCall
func (c *CustomersChromePrintServersGetCall) Header() http.Header
func (c *CustomersChromePrintServersGetCall) IfNoneMatch(entityTag string) *CustomersChromePrintServersGetCall
type CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) Context(ctx context.Context) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) Do(opts ...googleapi.CallOption) (*ListPrintServersResponse, error)
func (c *CustomersChromePrintServersListCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) Filter(filter string) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) Header() http.Header
func (c *CustomersChromePrintServersListCall) IfNoneMatch(entityTag string) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) OrderBy(orderBy string) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) OrgUnitId(orgUnitId string) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) PageSize(pageSize int64) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) PageToken(pageToken string) *CustomersChromePrintServersListCall
func (c *CustomersChromePrintServersListCall) Pages(ctx context.Context, f func(*ListPrintServersResponse) error) error
type CustomersChromePrintServersPatchCall
func (c *CustomersChromePrintServersPatchCall) Context(ctx context.Context) *CustomersChromePrintServersPatchCall
func (c *CustomersChromePrintServersPatchCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)
func (c *CustomersChromePrintServersPatchCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersPatchCall
func (c *CustomersChromePrintServersPatchCall) Header() http.Header
func (c *CustomersChromePrintServersPatchCall) UpdateMask(updateMask string) *CustomersChromePrintServersPatchCall
type CustomersChromePrintServersService
func NewCustomersChromePrintServersService(s *Service) *CustomersChromePrintServersService
func (r *CustomersChromePrintServersService) BatchCreatePrintServers(parent string, batchcreateprintserversrequest *BatchCreatePrintServersRequest) *CustomersChromePrintServersBatchCreatePrintServersCall
func (r *CustomersChromePrintServersService) BatchDeletePrintServers(parent string, batchdeleteprintserversrequest *BatchDeletePrintServersRequest) *CustomersChromePrintServersBatchDeletePrintServersCall
func (r *CustomersChromePrintServersService) Create(parent string, printserver *PrintServer) *CustomersChromePrintServersCreateCall
func (r *CustomersChromePrintServersService) Delete(name string) *CustomersChromePrintServersDeleteCall
func (r *CustomersChromePrintServersService) Get(name string) *CustomersChromePrintServersGetCall
func (r *CustomersChromePrintServersService) List(parent string) *CustomersChromePrintServersListCall
func (r *CustomersChromePrintServersService) Patch(name string, printserver *PrintServer) *CustomersChromePrintServersPatchCall
type CustomersChromePrintersBatchCreatePrintersCall
func (c *CustomersChromePrintersBatchCreatePrintersCall) Context(ctx context.Context) *CustomersChromePrintersBatchCreatePrintersCall
func (c *CustomersChromePrintersBatchCreatePrintersCall) Do(opts ...googleapi.CallOption) (*BatchCreatePrintersResponse, error)
func (c *CustomersChromePrintersBatchCreatePrintersCall) Fields(s ...googleapi.Field) *CustomersChromePrintersBatchCreatePrintersCall
func (c *CustomersChromePrintersBatchCreatePrintersCall) Header() http.Header
type CustomersChromePrintersBatchDeletePrintersCall
func (c *CustomersChromePrintersBatchDeletePrintersCall) Context(ctx context.Context) *CustomersChromePrintersBatchDeletePrintersCall
func (c *CustomersChromePrintersBatchDeletePrintersCall) Do(opts ...googleapi.CallOption) (*BatchDeletePrintersResponse, error)
func (c *CustomersChromePrintersBatchDeletePrintersCall) Fields(s ...googleapi.Field) *CustomersChromePrintersBatchDeletePrintersCall
func (c *CustomersChromePrintersBatchDeletePrintersCall) Header() http.Header
type CustomersChromePrintersCreateCall
func (c *CustomersChromePrintersCreateCall) Context(ctx context.Context) *CustomersChromePrintersCreateCall
func (c *CustomersChromePrintersCreateCall) Do(opts ...googleapi.CallOption) (*Printer, error)
func (c *CustomersChromePrintersCreateCall) Fields(s ...googleapi.Field) *CustomersChromePrintersCreateCall
func (c *CustomersChromePrintersCreateCall) Header() http.Header
type CustomersChromePrintersDeleteCall
func (c *CustomersChromePrintersDeleteCall) Context(ctx context.Context) *CustomersChromePrintersDeleteCall
func (c *CustomersChromePrintersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *CustomersChromePrintersDeleteCall) Fields(s ...googleapi.Field) *CustomersChromePrintersDeleteCall
func (c *CustomersChromePrintersDeleteCall) Header() http.Header
type CustomersChromePrintersGetCall
func (c *CustomersChromePrintersGetCall) Context(ctx context.Context) *CustomersChromePrintersGetCall
func (c *CustomersChromePrintersGetCall) Do(opts ...googleapi.CallOption) (*Printer, error)
func (c *CustomersChromePrintersGetCall) Fields(s ...googleapi.Field) *CustomersChromePrintersGetCall
func (c *CustomersChromePrintersGetCall) Header() http.Header
func (c *CustomersChromePrintersGetCall) IfNoneMatch(entityTag string) *CustomersChromePrintersGetCall
type CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) Context(ctx context.Context) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) Do(opts ...googleapi.CallOption) (*ListPrintersResponse, error)
func (c *CustomersChromePrintersListCall) Fields(s ...googleapi.Field) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) Filter(filter string) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) Header() http.Header
func (c *CustomersChromePrintersListCall) IfNoneMatch(entityTag string) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) OrderBy(orderBy string) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) OrgUnitId(orgUnitId string) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) PageSize(pageSize int64) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) PageToken(pageToken string) *CustomersChromePrintersListCall
func (c *CustomersChromePrintersListCall) Pages(ctx context.Context, f func(*ListPrintersResponse) error) error
type CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) Context(ctx context.Context) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) Do(opts ...googleapi.CallOption) (*ListPrinterModelsResponse, error)
func (c *CustomersChromePrintersListPrinterModelsCall) Fields(s ...googleapi.Field) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) Filter(filter string) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) Header() http.Header
func (c *CustomersChromePrintersListPrinterModelsCall) IfNoneMatch(entityTag string) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) PageSize(pageSize int64) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) PageToken(pageToken string) *CustomersChromePrintersListPrinterModelsCall
func (c *CustomersChromePrintersListPrinterModelsCall) Pages(ctx context.Context, f func(*ListPrinterModelsResponse) error) error
type CustomersChromePrintersPatchCall
func (c *CustomersChromePrintersPatchCall) ClearMask(clearMask string) *CustomersChromePrintersPatchCall
func (c *CustomersChromePrintersPatchCall) Context(ctx context.Context) *CustomersChromePrintersPatchCall
func (c *CustomersChromePrintersPatchCall) Do(opts ...googleapi.CallOption) (*Printer, error)
func (c *CustomersChromePrintersPatchCall) Fields(s ...googleapi.Field) *CustomersChromePrintersPatchCall
func (c *CustomersChromePrintersPatchCall) Header() http.Header
func (c *CustomersChromePrintersPatchCall) UpdateMask(updateMask string) *CustomersChromePrintersPatchCall
type CustomersChromePrintersService
func NewCustomersChromePrintersService(s *Service) *CustomersChromePrintersService
func (r *CustomersChromePrintersService) BatchCreatePrinters(parent string, batchcreateprintersrequest *BatchCreatePrintersRequest) *CustomersChromePrintersBatchCreatePrintersCall
func (r *CustomersChromePrintersService) BatchDeletePrinters(parent string, batchdeleteprintersrequest *BatchDeletePrintersRequest) *CustomersChromePrintersBatchDeletePrintersCall
func (r *CustomersChromePrintersService) Create(parent string, printer *Printer) *CustomersChromePrintersCreateCall
func (r *CustomersChromePrintersService) Delete(name string) *CustomersChromePrintersDeleteCall
func (r *CustomersChromePrintersService) Get(name string) *CustomersChromePrintersGetCall
func (r *CustomersChromePrintersService) List(parent string) *CustomersChromePrintersListCall
func (r *CustomersChromePrintersService) ListPrinterModels(parent string) *CustomersChromePrintersListPrinterModelsCall
func (r *CustomersChromePrintersService) Patch(name string, printer *Printer) *CustomersChromePrintersPatchCall
type CustomersChromeService
func NewCustomersChromeService(s *Service) *CustomersChromeService
type CustomersGetCall
func (c *CustomersGetCall) Context(ctx context.Context) *CustomersGetCall
func (c *CustomersGetCall) Do(opts ...googleapi.CallOption) (*Customer, error)
func (c *CustomersGetCall) Fields(s ...googleapi.Field) *CustomersGetCall
func (c *CustomersGetCall) Header() http.Header
func (c *CustomersGetCall) IfNoneMatch(entityTag string) *CustomersGetCall
type CustomersPatchCall
func (c *CustomersPatchCall) Context(ctx context.Context) *CustomersPatchCall
func (c *CustomersPatchCall) Do(opts ...googleapi.CallOption) (*Customer, error)
func (c *CustomersPatchCall) Fields(s ...googleapi.Field) *CustomersPatchCall
func (c *CustomersPatchCall) Header() http.Header
type CustomersService
func NewCustomersService(s *Service) *CustomersService
func (r *CustomersService) Get(customerKey string) *CustomersGetCall
func (r *CustomersService) Patch(customerKey string, customer *Customer) *CustomersPatchCall
func (r *CustomersService) Update(customerKey string, customer *Customer) *CustomersUpdateCall
type CustomersUpdateCall
func (c *CustomersUpdateCall) Context(ctx context.Context) *CustomersUpdateCall
func (c *CustomersUpdateCall) Do(opts ...googleapi.CallOption) (*Customer, error)
func (c *CustomersUpdateCall) Fields(s ...googleapi.Field) *CustomersUpdateCall
func (c *CustomersUpdateCall) Header() http.Header
type DirectoryChromeosdevicesCommand
func (s DirectoryChromeosdevicesCommand) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesCommandResult
func (s DirectoryChromeosdevicesCommandResult) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesIssueCommandRequest
func (s DirectoryChromeosdevicesIssueCommandRequest) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesIssueCommandResponse
func (s DirectoryChromeosdevicesIssueCommandResponse) MarshalJSON() ([]byte, error)
type DirectoryUsersCreateGuestRequest
func (s DirectoryUsersCreateGuestRequest) MarshalJSON() ([]byte, error)
type DomainAlias
func (s DomainAlias) MarshalJSON() ([]byte, error)
type DomainAliases
func (s DomainAliases) MarshalJSON() ([]byte, error)
type DomainAliasesDeleteCall
func (c *DomainAliasesDeleteCall) Context(ctx context.Context) *DomainAliasesDeleteCall
func (c *DomainAliasesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *DomainAliasesDeleteCall) Fields(s ...googleapi.Field) *DomainAliasesDeleteCall
func (c *DomainAliasesDeleteCall) Header() http.Header
type DomainAliasesGetCall
func (c *DomainAliasesGetCall) Context(ctx context.Context) *DomainAliasesGetCall
func (c *DomainAliasesGetCall) Do(opts ...googleapi.CallOption) (*DomainAlias, error)
func (c *DomainAliasesGetCall) Fields(s ...googleapi.Field) *DomainAliasesGetCall
func (c *DomainAliasesGetCall) Header() http.Header
func (c *DomainAliasesGetCall) IfNoneMatch(entityTag string) *DomainAliasesGetCall
type DomainAliasesInsertCall
func (c *DomainAliasesInsertCall) Context(ctx context.Context) *DomainAliasesInsertCall
func (c *DomainAliasesInsertCall) Do(opts ...googleapi.CallOption) (*DomainAlias, error)
func (c *DomainAliasesInsertCall) Fields(s ...googleapi.Field) *DomainAliasesInsertCall
func (c *DomainAliasesInsertCall) Header() http.Header
type DomainAliasesListCall
func (c *DomainAliasesListCall) Context(ctx context.Context) *DomainAliasesListCall
func (c *DomainAliasesListCall) Do(opts ...googleapi.CallOption) (*DomainAliases, error)
func (c *DomainAliasesListCall) Fields(s ...googleapi.Field) *DomainAliasesListCall
func (c *DomainAliasesListCall) Header() http.Header
func (c *DomainAliasesListCall) IfNoneMatch(entityTag string) *DomainAliasesListCall
func (c *DomainAliasesListCall) ParentDomainName(parentDomainName string) *DomainAliasesListCall
type DomainAliasesService
func NewDomainAliasesService(s *Service) *DomainAliasesService
func (r *DomainAliasesService) Delete(customer string, domainAliasName string) *DomainAliasesDeleteCall
func (r *DomainAliasesService) Get(customer string, domainAliasName string) *DomainAliasesGetCall
func (r *DomainAliasesService) Insert(customer string, domainalias *DomainAlias) *DomainAliasesInsertCall
func (r *DomainAliasesService) List(customer string) *DomainAliasesListCall
type Domains
func (s Domains) MarshalJSON() ([]byte, error)
type Domains2
func (s Domains2) MarshalJSON() ([]byte, error)
type DomainsDeleteCall
func (c *DomainsDeleteCall) Context(ctx context.Context) *DomainsDeleteCall
func (c *DomainsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *DomainsDeleteCall) Fields(s ...googleapi.Field) *DomainsDeleteCall
func (c *DomainsDeleteCall) Header() http.Header
type DomainsGetCall
func (c *DomainsGetCall) Context(ctx context.Context) *DomainsGetCall
func (c *DomainsGetCall) Do(opts ...googleapi.CallOption) (*Domains, error)
func (c *DomainsGetCall) Fields(s ...googleapi.Field) *DomainsGetCall
func (c *DomainsGetCall) Header() http.Header
func (c *DomainsGetCall) IfNoneMatch(entityTag string) *DomainsGetCall
type DomainsInsertCall
func (c *DomainsInsertCall) Context(ctx context.Context) *DomainsInsertCall
func (c *DomainsInsertCall) Do(opts ...googleapi.CallOption) (*Domains, error)
func (c *DomainsInsertCall) Fields(s ...googleapi.Field) *DomainsInsertCall
func (c *DomainsInsertCall) Header() http.Header
type DomainsListCall
func (c *DomainsListCall) Context(ctx context.Context) *DomainsListCall
func (c *DomainsListCall) Do(opts ...googleapi.CallOption) (*Domains2, error)
func (c *DomainsListCall) Fields(s ...googleapi.Field) *DomainsListCall
func (c *DomainsListCall) Header() http.Header
func (c *DomainsListCall) IfNoneMatch(entityTag string) *DomainsListCall
type DomainsService
func NewDomainsService(s *Service) *DomainsService
func (r *DomainsService) Delete(customer string, domainName string) *DomainsDeleteCall
func (r *DomainsService) Get(customer string, domainName string) *DomainsGetCall
func (r *DomainsService) Insert(customer string, domains *Domains) *DomainsInsertCall
func (r *DomainsService) List(customer string) *DomainsListCall
type Empty
type FailureInfo
func (s FailureInfo) MarshalJSON() ([]byte, error)
type FanInfo
func (s FanInfo) MarshalJSON() ([]byte, error)
type Feature
func (s Feature) MarshalJSON() ([]byte, error)
type FeatureInstance
func (s FeatureInstance) MarshalJSON() ([]byte, error)
type FeatureRename
func (s FeatureRename) MarshalJSON() ([]byte, error)
type Features
func (s Features) MarshalJSON() ([]byte, error)
type Group
func (s Group) MarshalJSON() ([]byte, error)
type GroupAlias
func (s GroupAlias) MarshalJSON() ([]byte, error)
type Groups
func (s Groups) MarshalJSON() ([]byte, error)
type GroupsAliasesDeleteCall
func (c *GroupsAliasesDeleteCall) Context(ctx context.Context) *GroupsAliasesDeleteCall
func (c *GroupsAliasesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *GroupsAliasesDeleteCall) Fields(s ...googleapi.Field) *GroupsAliasesDeleteCall
func (c *GroupsAliasesDeleteCall) Header() http.Header
type GroupsAliasesInsertCall
func (c *GroupsAliasesInsertCall) Context(ctx context.Context) *GroupsAliasesInsertCall
func (c *GroupsAliasesInsertCall) Do(opts ...googleapi.CallOption) (*Alias, error)
func (c *GroupsAliasesInsertCall) Fields(s ...googleapi.Field) *GroupsAliasesInsertCall
func (c *GroupsAliasesInsertCall) Header() http.Header
type GroupsAliasesListCall
func (c *GroupsAliasesListCall) Context(ctx context.Context) *GroupsAliasesListCall
func (c *GroupsAliasesListCall) Do(opts ...googleapi.CallOption) (*Aliases, error)
func (c *GroupsAliasesListCall) Fields(s ...googleapi.Field) *GroupsAliasesListCall
func (c *GroupsAliasesListCall) Header() http.Header
func (c *GroupsAliasesListCall) IfNoneMatch(entityTag string) *GroupsAliasesListCall
type GroupsAliasesService
func NewGroupsAliasesService(s *Service) *GroupsAliasesService
func (r *GroupsAliasesService) Delete(groupKey string, alias string) *GroupsAliasesDeleteCall
func (r *GroupsAliasesService) Insert(groupKey string, alias *Alias) *GroupsAliasesInsertCall
func (r *GroupsAliasesService) List(groupKey string) *GroupsAliasesListCall
type GroupsDeleteCall
func (c *GroupsDeleteCall) Context(ctx context.Context) *GroupsDeleteCall
func (c *GroupsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *GroupsDeleteCall) Fields(s ...googleapi.Field) *GroupsDeleteCall
func (c *GroupsDeleteCall) Header() http.Header
type GroupsGetCall
func (c *GroupsGetCall) Context(ctx context.Context) *GroupsGetCall
func (c *GroupsGetCall) Do(opts ...googleapi.CallOption) (*Group, error)
func (c *GroupsGetCall) Fields(s ...googleapi.Field) *GroupsGetCall
func (c *GroupsGetCall) Header() http.Header
func (c *GroupsGetCall) IfNoneMatch(entityTag string) *GroupsGetCall
type GroupsInsertCall
func (c *GroupsInsertCall) Context(ctx context.Context) *GroupsInsertCall
func (c *GroupsInsertCall) Do(opts ...googleapi.CallOption) (*Group, error)
func (c *GroupsInsertCall) Fields(s ...googleapi.Field) *GroupsInsertCall
func (c *GroupsInsertCall) Header() http.Header
type GroupsListCall
func (c *GroupsListCall) Context(ctx context.Context) *GroupsListCall
func (c *GroupsListCall) Customer(customer string) *GroupsListCall
func (c *GroupsListCall) Do(opts ...googleapi.CallOption) (*Groups, error)
func (c *GroupsListCall) Domain(domain string) *GroupsListCall
func (c *GroupsListCall) Fields(s ...googleapi.Field) *GroupsListCall
func (c *GroupsListCall) Header() http.Header
func (c *GroupsListCall) IfNoneMatch(entityTag string) *GroupsListCall
func (c *GroupsListCall) MaxResults(maxResults int64) *GroupsListCall
func (c *GroupsListCall) OrderBy(orderBy string) *GroupsListCall
func (c *GroupsListCall) PageToken(pageToken string) *GroupsListCall
func (c *GroupsListCall) Pages(ctx context.Context, f func(*Groups) error) error
func (c *GroupsListCall) Query(query string) *GroupsListCall
func (c *GroupsListCall) SortOrder(sortOrder string) *GroupsListCall
func (c *GroupsListCall) UserKey(userKey string) *GroupsListCall
type GroupsPatchCall
func (c *GroupsPatchCall) Context(ctx context.Context) *GroupsPatchCall
func (c *GroupsPatchCall) Do(opts ...googleapi.CallOption) (*Group, error)
func (c *GroupsPatchCall) Fields(s ...googleapi.Field) *GroupsPatchCall
func (c *GroupsPatchCall) Header() http.Header
type GroupsService
func NewGroupsService(s *Service) *GroupsService
func (r *GroupsService) Delete(groupKey string) *GroupsDeleteCall
func (r *GroupsService) Get(groupKey string) *GroupsGetCall
func (r *GroupsService) Insert(group *Group) *GroupsInsertCall
func (r *GroupsService) List() *GroupsListCall
func (r *GroupsService) Patch(groupKey string, group *Group) *GroupsPatchCall
func (r *GroupsService) Update(groupKey string, group *Group) *GroupsUpdateCall
type GroupsUpdateCall
func (c *GroupsUpdateCall) Context(ctx context.Context) *GroupsUpdateCall
func (c *GroupsUpdateCall) Do(opts ...googleapi.CallOption) (*Group, error)
func (c *GroupsUpdateCall) Fields(s ...googleapi.Field) *GroupsUpdateCall
func (c *GroupsUpdateCall) Header() http.Header
type GuestAccountInfo
func (s GuestAccountInfo) MarshalJSON() ([]byte, error)
type ListPrintServersResponse
func (s ListPrintServersResponse) MarshalJSON() ([]byte, error)
type ListPrinterModelsResponse
func (s ListPrinterModelsResponse) MarshalJSON() ([]byte, error)
type ListPrintersResponse
func (s ListPrintersResponse) MarshalJSON() ([]byte, error)
type Member
func (s Member) MarshalJSON() ([]byte, error)
type Members
func (s Members) MarshalJSON() ([]byte, error)
type MembersDeleteCall
func (c *MembersDeleteCall) Context(ctx context.Context) *MembersDeleteCall
func (c *MembersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MembersDeleteCall) Fields(s ...googleapi.Field) *MembersDeleteCall
func (c *MembersDeleteCall) Header() http.Header
type MembersGetCall
func (c *MembersGetCall) Context(ctx context.Context) *MembersGetCall
func (c *MembersGetCall) Do(opts ...googleapi.CallOption) (*Member, error)
func (c *MembersGetCall) Fields(s ...googleapi.Field) *MembersGetCall
func (c *MembersGetCall) Header() http.Header
func (c *MembersGetCall) IfNoneMatch(entityTag string) *MembersGetCall
type MembersHasMember
func (s MembersHasMember) MarshalJSON() ([]byte, error)
type MembersHasMemberCall
func (c *MembersHasMemberCall) Context(ctx context.Context) *MembersHasMemberCall
func (c *MembersHasMemberCall) Do(opts ...googleapi.CallOption) (*MembersHasMember, error)
func (c *MembersHasMemberCall) Fields(s ...googleapi.Field) *MembersHasMemberCall
func (c *MembersHasMemberCall) Header() http.Header
func (c *MembersHasMemberCall) IfNoneMatch(entityTag string) *MembersHasMemberCall
type MembersInsertCall
func (c *MembersInsertCall) Context(ctx context.Context) *MembersInsertCall
func (c *MembersInsertCall) Do(opts ...googleapi.CallOption) (*Member, error)
func (c *MembersInsertCall) Fields(s ...googleapi.Field) *MembersInsertCall
func (c *MembersInsertCall) Header() http.Header
type MembersListCall
func (c *MembersListCall) Context(ctx context.Context) *MembersListCall
func (c *MembersListCall) Do(opts ...googleapi.CallOption) (*Members, error)
func (c *MembersListCall) Fields(s ...googleapi.Field) *MembersListCall
func (c *MembersListCall) Header() http.Header
func (c *MembersListCall) IfNoneMatch(entityTag string) *MembersListCall
func (c *MembersListCall) IncludeDerivedMembership(includeDerivedMembership bool) *MembersListCall
func (c *MembersListCall) MaxResults(maxResults int64) *MembersListCall
func (c *MembersListCall) PageToken(pageToken string) *MembersListCall
func (c *MembersListCall) Pages(ctx context.Context, f func(*Members) error) error
func (c *MembersListCall) Roles(roles string) *MembersListCall
type MembersPatchCall
func (c *MembersPatchCall) Context(ctx context.Context) *MembersPatchCall
func (c *MembersPatchCall) Do(opts ...googleapi.CallOption) (*Member, error)
func (c *MembersPatchCall) Fields(s ...googleapi.Field) *MembersPatchCall
func (c *MembersPatchCall) Header() http.Header
type MembersService
func NewMembersService(s *Service) *MembersService
func (r *MembersService) Delete(groupKey string, memberKey string) *MembersDeleteCall
func (r *MembersService) Get(groupKey string, memberKey string) *MembersGetCall
func (r *MembersService) HasMember(groupKey string, memberKey string) *MembersHasMemberCall
func (r *MembersService) Insert(groupKey string, member *Member) *MembersInsertCall
func (r *MembersService) List(groupKey string) *MembersListCall
func (r *MembersService) Patch(groupKey string, memberKey string, member *Member) *MembersPatchCall
func (r *MembersService) Update(groupKey string, memberKey string, member *Member) *MembersUpdateCall
type MembersUpdateCall
func (c *MembersUpdateCall) Context(ctx context.Context) *MembersUpdateCall
func (c *MembersUpdateCall) Do(opts ...googleapi.CallOption) (*Member, error)
func (c *MembersUpdateCall) Fields(s ...googleapi.Field) *MembersUpdateCall
func (c *MembersUpdateCall) Header() http.Header
type MobileDevice
func (s MobileDevice) MarshalJSON() ([]byte, error)
type MobileDeviceAction
func (s MobileDeviceAction) MarshalJSON() ([]byte, error)
type MobileDeviceApplications
func (s MobileDeviceApplications) MarshalJSON() ([]byte, error)
type MobileDevices
func (s MobileDevices) MarshalJSON() ([]byte, error)
type MobiledevicesActionCall
func (c *MobiledevicesActionCall) Context(ctx context.Context) *MobiledevicesActionCall
func (c *MobiledevicesActionCall) Do(opts ...googleapi.CallOption) error
func (c *MobiledevicesActionCall) Fields(s ...googleapi.Field) *MobiledevicesActionCall
func (c *MobiledevicesActionCall) Header() http.Header
type MobiledevicesDeleteCall
func (c *MobiledevicesDeleteCall) Context(ctx context.Context) *MobiledevicesDeleteCall
func (c *MobiledevicesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MobiledevicesDeleteCall) Fields(s ...googleapi.Field) *MobiledevicesDeleteCall
func (c *MobiledevicesDeleteCall) Header() http.Header
type MobiledevicesGetCall
func (c *MobiledevicesGetCall) Context(ctx context.Context) *MobiledevicesGetCall
func (c *MobiledevicesGetCall) Do(opts ...googleapi.CallOption) (*MobileDevice, error)
func (c *MobiledevicesGetCall) Fields(s ...googleapi.Field) *MobiledevicesGetCall
func (c *MobiledevicesGetCall) Header() http.Header
func (c *MobiledevicesGetCall) IfNoneMatch(entityTag string) *MobiledevicesGetCall
func (c *MobiledevicesGetCall) Projection(projection string) *MobiledevicesGetCall
type MobiledevicesListCall
func (c *MobiledevicesListCall) Context(ctx context.Context) *MobiledevicesListCall
func (c *MobiledevicesListCall) Do(opts ...googleapi.CallOption) (*MobileDevices, error)
func (c *MobiledevicesListCall) Fields(s ...googleapi.Field) *MobiledevicesListCall
func (c *MobiledevicesListCall) Header() http.Header
func (c *MobiledevicesListCall) IfNoneMatch(entityTag string) *MobiledevicesListCall
func (c *MobiledevicesListCall) MaxResults(maxResults int64) *MobiledevicesListCall
func (c *MobiledevicesListCall) OrderBy(orderBy string) *MobiledevicesListCall
func (c *MobiledevicesListCall) PageToken(pageToken string) *MobiledevicesListCall
func (c *MobiledevicesListCall) Pages(ctx context.Context, f func(*MobileDevices) error) error
func (c *MobiledevicesListCall) Projection(projection string) *MobiledevicesListCall
func (c *MobiledevicesListCall) Query(query string) *MobiledevicesListCall
func (c *MobiledevicesListCall) SortOrder(sortOrder string) *MobiledevicesListCall
type MobiledevicesService
func NewMobiledevicesService(s *Service) *MobiledevicesService
func (r *MobiledevicesService) Action(customerId string, resourceId string, mobiledeviceaction *MobileDeviceAction) *MobiledevicesActionCall
func (r *MobiledevicesService) Delete(customerId string, resourceId string) *MobiledevicesDeleteCall
func (r *MobiledevicesService) Get(customerId string, resourceId string) *MobiledevicesGetCall
func (r *MobiledevicesService) List(customerId string) *MobiledevicesListCall
type OrgUnit
func (s OrgUnit) MarshalJSON() ([]byte, error)
type OrgUnits
func (s OrgUnits) MarshalJSON() ([]byte, error)
type OrgunitsDeleteCall
func (c *OrgunitsDeleteCall) Context(ctx context.Context) *OrgunitsDeleteCall
func (c *OrgunitsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *OrgunitsDeleteCall) Fields(s ...googleapi.Field) *OrgunitsDeleteCall
func (c *OrgunitsDeleteCall) Header() http.Header
type OrgunitsGetCall
func (c *OrgunitsGetCall) Context(ctx context.Context) *OrgunitsGetCall
func (c *OrgunitsGetCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)
func (c *OrgunitsGetCall) Fields(s ...googleapi.Field) *OrgunitsGetCall
func (c *OrgunitsGetCall) Header() http.Header
func (c *OrgunitsGetCall) IfNoneMatch(entityTag string) *OrgunitsGetCall
type OrgunitsInsertCall
func (c *OrgunitsInsertCall) Context(ctx context.Context) *OrgunitsInsertCall
func (c *OrgunitsInsertCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)
func (c *OrgunitsInsertCall) Fields(s ...googleapi.Field) *OrgunitsInsertCall
func (c *OrgunitsInsertCall) Header() http.Header
type OrgunitsListCall
func (c *OrgunitsListCall) Context(ctx context.Context) *OrgunitsListCall
func (c *OrgunitsListCall) Do(opts ...googleapi.CallOption) (*OrgUnits, error)
func (c *OrgunitsListCall) Fields(s ...googleapi.Field) *OrgunitsListCall
func (c *OrgunitsListCall) Header() http.Header
func (c *OrgunitsListCall) IfNoneMatch(entityTag string) *OrgunitsListCall
func (c *OrgunitsListCall) OrgUnitPath(orgUnitPath string) *OrgunitsListCall
func (c *OrgunitsListCall) Type(type_ string) *OrgunitsListCall
type OrgunitsPatchCall
func (c *OrgunitsPatchCall) Context(ctx context.Context) *OrgunitsPatchCall
func (c *OrgunitsPatchCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)
func (c *OrgunitsPatchCall) Fields(s ...googleapi.Field) *OrgunitsPatchCall
func (c *OrgunitsPatchCall) Header() http.Header
type OrgunitsService
func NewOrgunitsService(s *Service) *OrgunitsService
func (r *OrgunitsService) Delete(customerId string, orgUnitPath string) *OrgunitsDeleteCall
func (r *OrgunitsService) Get(customerId string, orgUnitPath string) *OrgunitsGetCall
func (r *OrgunitsService) Insert(customerId string, orgunit *OrgUnit) *OrgunitsInsertCall
func (r *OrgunitsService) List(customerId string) *OrgunitsListCall
func (r *OrgunitsService) Patch(customerId string, orgUnitPath string, orgunit *OrgUnit) *OrgunitsPatchCall
func (r *OrgunitsService) Update(customerId string, orgUnitPath string, orgunit *OrgUnit) *OrgunitsUpdateCall
type OrgunitsUpdateCall
func (c *OrgunitsUpdateCall) Context(ctx context.Context) *OrgunitsUpdateCall
func (c *OrgunitsUpdateCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)
func (c *OrgunitsUpdateCall) Fields(s ...googleapi.Field) *OrgunitsUpdateCall
func (c *OrgunitsUpdateCall) Header() http.Header
type OsUpdateStatus
func (s OsUpdateStatus) MarshalJSON() ([]byte, error)
type PrintServer
func (s PrintServer) MarshalJSON() ([]byte, error)
type PrintServerFailureInfo
func (s PrintServerFailureInfo) MarshalJSON() ([]byte, error)
type Printer
func (s Printer) MarshalJSON() ([]byte, error)
type PrinterModel
func (s PrinterModel) MarshalJSON() ([]byte, error)
type Privilege
func (s Privilege) MarshalJSON() ([]byte, error)
type Privileges
func (s Privileges) MarshalJSON() ([]byte, error)
type PrivilegesListCall
func (c *PrivilegesListCall) Context(ctx context.Context) *PrivilegesListCall
func (c *PrivilegesListCall) Do(opts ...googleapi.CallOption) (*Privileges, error)
func (c *PrivilegesListCall) Fields(s ...googleapi.Field) *PrivilegesListCall
func (c *PrivilegesListCall) Header() http.Header
func (c *PrivilegesListCall) IfNoneMatch(entityTag string) *PrivilegesListCall
type PrivilegesService
func NewPrivilegesService(s *Service) *PrivilegesService
func (r *PrivilegesService) List(customer string) *PrivilegesListCall
type ResourcesBuildingsDeleteCall
func (c *ResourcesBuildingsDeleteCall) Context(ctx context.Context) *ResourcesBuildingsDeleteCall
func (c *ResourcesBuildingsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ResourcesBuildingsDeleteCall) Fields(s ...googleapi.Field) *ResourcesBuildingsDeleteCall
func (c *ResourcesBuildingsDeleteCall) Header() http.Header
type ResourcesBuildingsGetCall
func (c *ResourcesBuildingsGetCall) Context(ctx context.Context) *ResourcesBuildingsGetCall
func (c *ResourcesBuildingsGetCall) Do(opts ...googleapi.CallOption) (*Building, error)
func (c *ResourcesBuildingsGetCall) Fields(s ...googleapi.Field) *ResourcesBuildingsGetCall
func (c *ResourcesBuildingsGetCall) Header() http.Header
func (c *ResourcesBuildingsGetCall) IfNoneMatch(entityTag string) *ResourcesBuildingsGetCall
type ResourcesBuildingsInsertCall
func (c *ResourcesBuildingsInsertCall) Context(ctx context.Context) *ResourcesBuildingsInsertCall
func (c *ResourcesBuildingsInsertCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsInsertCall
func (c *ResourcesBuildingsInsertCall) Do(opts ...googleapi.CallOption) (*Building, error)
func (c *ResourcesBuildingsInsertCall) Fields(s ...googleapi.Field) *ResourcesBuildingsInsertCall
func (c *ResourcesBuildingsInsertCall) Header() http.Header
type ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) Context(ctx context.Context) *ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) Do(opts ...googleapi.CallOption) (*Buildings, error)
func (c *ResourcesBuildingsListCall) Fields(s ...googleapi.Field) *ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) Header() http.Header
func (c *ResourcesBuildingsListCall) IfNoneMatch(entityTag string) *ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) MaxResults(maxResults int64) *ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) PageToken(pageToken string) *ResourcesBuildingsListCall
func (c *ResourcesBuildingsListCall) Pages(ctx context.Context, f func(*Buildings) error) error
type ResourcesBuildingsPatchCall
func (c *ResourcesBuildingsPatchCall) Context(ctx context.Context) *ResourcesBuildingsPatchCall
func (c *ResourcesBuildingsPatchCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsPatchCall
func (c *ResourcesBuildingsPatchCall) Do(opts ...googleapi.CallOption) (*Building, error)
func (c *ResourcesBuildingsPatchCall) Fields(s ...googleapi.Field) *ResourcesBuildingsPatchCall
func (c *ResourcesBuildingsPatchCall) Header() http.Header
type ResourcesBuildingsService
func NewResourcesBuildingsService(s *Service) *ResourcesBuildingsService
func (r *ResourcesBuildingsService) Delete(customer string, buildingId string) *ResourcesBuildingsDeleteCall
func (r *ResourcesBuildingsService) Get(customer string, buildingId string) *ResourcesBuildingsGetCall
func (r *ResourcesBuildingsService) Insert(customer string, building *Building) *ResourcesBuildingsInsertCall
func (r *ResourcesBuildingsService) List(customer string) *ResourcesBuildingsListCall
func (r *ResourcesBuildingsService) Patch(customer string, buildingId string, building *Building) *ResourcesBuildingsPatchCall
func (r *ResourcesBuildingsService) Update(customer string, buildingId string, building *Building) *ResourcesBuildingsUpdateCall
type ResourcesBuildingsUpdateCall
func (c *ResourcesBuildingsUpdateCall) Context(ctx context.Context) *ResourcesBuildingsUpdateCall
func (c *ResourcesBuildingsUpdateCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsUpdateCall
func (c *ResourcesBuildingsUpdateCall) Do(opts ...googleapi.CallOption) (*Building, error)
func (c *ResourcesBuildingsUpdateCall) Fields(s ...googleapi.Field) *ResourcesBuildingsUpdateCall
func (c *ResourcesBuildingsUpdateCall) Header() http.Header
type ResourcesCalendarsDeleteCall
func (c *ResourcesCalendarsDeleteCall) Context(ctx context.Context) *ResourcesCalendarsDeleteCall
func (c *ResourcesCalendarsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ResourcesCalendarsDeleteCall) Fields(s ...googleapi.Field) *ResourcesCalendarsDeleteCall
func (c *ResourcesCalendarsDeleteCall) Header() http.Header
type ResourcesCalendarsGetCall
func (c *ResourcesCalendarsGetCall) Context(ctx context.Context) *ResourcesCalendarsGetCall
func (c *ResourcesCalendarsGetCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)
func (c *ResourcesCalendarsGetCall) Fields(s ...googleapi.Field) *ResourcesCalendarsGetCall
func (c *ResourcesCalendarsGetCall) Header() http.Header
func (c *ResourcesCalendarsGetCall) IfNoneMatch(entityTag string) *ResourcesCalendarsGetCall
type ResourcesCalendarsInsertCall
func (c *ResourcesCalendarsInsertCall) Context(ctx context.Context) *ResourcesCalendarsInsertCall
func (c *ResourcesCalendarsInsertCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)
func (c *ResourcesCalendarsInsertCall) Fields(s ...googleapi.Field) *ResourcesCalendarsInsertCall
func (c *ResourcesCalendarsInsertCall) Header() http.Header
type ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) Context(ctx context.Context) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) Do(opts ...googleapi.CallOption) (*CalendarResources, error)
func (c *ResourcesCalendarsListCall) Fields(s ...googleapi.Field) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) Header() http.Header
func (c *ResourcesCalendarsListCall) IfNoneMatch(entityTag string) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) MaxResults(maxResults int64) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) OrderBy(orderBy string) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) PageToken(pageToken string) *ResourcesCalendarsListCall
func (c *ResourcesCalendarsListCall) Pages(ctx context.Context, f func(*CalendarResources) error) error
func (c *ResourcesCalendarsListCall) Query(query string) *ResourcesCalendarsListCall
type ResourcesCalendarsPatchCall
func (c *ResourcesCalendarsPatchCall) Context(ctx context.Context) *ResourcesCalendarsPatchCall
func (c *ResourcesCalendarsPatchCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)
func (c *ResourcesCalendarsPatchCall) Fields(s ...googleapi.Field) *ResourcesCalendarsPatchCall
func (c *ResourcesCalendarsPatchCall) Header() http.Header
type ResourcesCalendarsService
func NewResourcesCalendarsService(s *Service) *ResourcesCalendarsService
func (r *ResourcesCalendarsService) Delete(customer string, calendarResourceId string) *ResourcesCalendarsDeleteCall
func (r *ResourcesCalendarsService) Get(customer string, calendarResourceId string) *ResourcesCalendarsGetCall
func (r *ResourcesCalendarsService) Insert(customer string, calendarresource *CalendarResource) *ResourcesCalendarsInsertCall
func (r *ResourcesCalendarsService) List(customer string) *ResourcesCalendarsListCall
func (r *ResourcesCalendarsService) Patch(customer string, calendarResourceId string, calendarresource *CalendarResource) *ResourcesCalendarsPatchCall
func (r *ResourcesCalendarsService) Update(customer string, calendarResourceId string, calendarresource *CalendarResource) *ResourcesCalendarsUpdateCall
type ResourcesCalendarsUpdateCall
func (c *ResourcesCalendarsUpdateCall) Context(ctx context.Context) *ResourcesCalendarsUpdateCall
func (c *ResourcesCalendarsUpdateCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)
func (c *ResourcesCalendarsUpdateCall) Fields(s ...googleapi.Field) *ResourcesCalendarsUpdateCall
func (c *ResourcesCalendarsUpdateCall) Header() http.Header
type ResourcesFeaturesDeleteCall
func (c *ResourcesFeaturesDeleteCall) Context(ctx context.Context) *ResourcesFeaturesDeleteCall
func (c *ResourcesFeaturesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ResourcesFeaturesDeleteCall) Fields(s ...googleapi.Field) *ResourcesFeaturesDeleteCall
func (c *ResourcesFeaturesDeleteCall) Header() http.Header
type ResourcesFeaturesGetCall
func (c *ResourcesFeaturesGetCall) Context(ctx context.Context) *ResourcesFeaturesGetCall
func (c *ResourcesFeaturesGetCall) Do(opts ...googleapi.CallOption) (*Feature, error)
func (c *ResourcesFeaturesGetCall) Fields(s ...googleapi.Field) *ResourcesFeaturesGetCall
func (c *ResourcesFeaturesGetCall) Header() http.Header
func (c *ResourcesFeaturesGetCall) IfNoneMatch(entityTag string) *ResourcesFeaturesGetCall
type ResourcesFeaturesInsertCall
func (c *ResourcesFeaturesInsertCall) Context(ctx context.Context) *ResourcesFeaturesInsertCall
func (c *ResourcesFeaturesInsertCall) Do(opts ...googleapi.CallOption) (*Feature, error)
func (c *ResourcesFeaturesInsertCall) Fields(s ...googleapi.Field) *ResourcesFeaturesInsertCall
func (c *ResourcesFeaturesInsertCall) Header() http.Header
type ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) Context(ctx context.Context) *ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) Do(opts ...googleapi.CallOption) (*Features, error)
func (c *ResourcesFeaturesListCall) Fields(s ...googleapi.Field) *ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) Header() http.Header
func (c *ResourcesFeaturesListCall) IfNoneMatch(entityTag string) *ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) MaxResults(maxResults int64) *ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) PageToken(pageToken string) *ResourcesFeaturesListCall
func (c *ResourcesFeaturesListCall) Pages(ctx context.Context, f func(*Features) error) error
type ResourcesFeaturesPatchCall
func (c *ResourcesFeaturesPatchCall) Context(ctx context.Context) *ResourcesFeaturesPatchCall
func (c *ResourcesFeaturesPatchCall) Do(opts ...googleapi.CallOption) (*Feature, error)
func (c *ResourcesFeaturesPatchCall) Fields(s ...googleapi.Field) *ResourcesFeaturesPatchCall
func (c *ResourcesFeaturesPatchCall) Header() http.Header
type ResourcesFeaturesRenameCall
func (c *ResourcesFeaturesRenameCall) Context(ctx context.Context) *ResourcesFeaturesRenameCall
func (c *ResourcesFeaturesRenameCall) Do(opts ...googleapi.CallOption) error
func (c *ResourcesFeaturesRenameCall) Fields(s ...googleapi.Field) *ResourcesFeaturesRenameCall
func (c *ResourcesFeaturesRenameCall) Header() http.Header
type ResourcesFeaturesService
func NewResourcesFeaturesService(s *Service) *ResourcesFeaturesService
func (r *ResourcesFeaturesService) Delete(customer string, featureKey string) *ResourcesFeaturesDeleteCall
func (r *ResourcesFeaturesService) Get(customer string, featureKey string) *ResourcesFeaturesGetCall
func (r *ResourcesFeaturesService) Insert(customer string, feature *Feature) *ResourcesFeaturesInsertCall
func (r *ResourcesFeaturesService) List(customer string) *ResourcesFeaturesListCall
func (r *ResourcesFeaturesService) Patch(customer string, featureKey string, feature *Feature) *ResourcesFeaturesPatchCall
func (r *ResourcesFeaturesService) Rename(customer string, oldName string, featurerename *FeatureRename) *ResourcesFeaturesRenameCall
func (r *ResourcesFeaturesService) Update(customer string, featureKey string, feature *Feature) *ResourcesFeaturesUpdateCall
type ResourcesFeaturesUpdateCall
func (c *ResourcesFeaturesUpdateCall) Context(ctx context.Context) *ResourcesFeaturesUpdateCall
func (c *ResourcesFeaturesUpdateCall) Do(opts ...googleapi.CallOption) (*Feature, error)
func (c *ResourcesFeaturesUpdateCall) Fields(s ...googleapi.Field) *ResourcesFeaturesUpdateCall
func (c *ResourcesFeaturesUpdateCall) Header() http.Header
type ResourcesService
func NewResourcesService(s *Service) *ResourcesService
type Role
func (s Role) MarshalJSON() ([]byte, error)
type RoleAssignment
func (s RoleAssignment) MarshalJSON() ([]byte, error)
type RoleAssignments
func (s RoleAssignments) MarshalJSON() ([]byte, error)
type RoleAssignmentsDeleteCall
func (c *RoleAssignmentsDeleteCall) Context(ctx context.Context) *RoleAssignmentsDeleteCall
func (c *RoleAssignmentsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *RoleAssignmentsDeleteCall) Fields(s ...googleapi.Field) *RoleAssignmentsDeleteCall
func (c *RoleAssignmentsDeleteCall) Header() http.Header
type RoleAssignmentsGetCall
func (c *RoleAssignmentsGetCall) Context(ctx context.Context) *RoleAssignmentsGetCall
func (c *RoleAssignmentsGetCall) Do(opts ...googleapi.CallOption) (*RoleAssignment, error)
func (c *RoleAssignmentsGetCall) Fields(s ...googleapi.Field) *RoleAssignmentsGetCall
func (c *RoleAssignmentsGetCall) Header() http.Header
func (c *RoleAssignmentsGetCall) IfNoneMatch(entityTag string) *RoleAssignmentsGetCall
type RoleAssignmentsInsertCall
func (c *RoleAssignmentsInsertCall) Context(ctx context.Context) *RoleAssignmentsInsertCall
func (c *RoleAssignmentsInsertCall) Do(opts ...googleapi.CallOption) (*RoleAssignment, error)
func (c *RoleAssignmentsInsertCall) Fields(s ...googleapi.Field) *RoleAssignmentsInsertCall
func (c *RoleAssignmentsInsertCall) Header() http.Header
type RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) Context(ctx context.Context) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) Do(opts ...googleapi.CallOption) (*RoleAssignments, error)
func (c *RoleAssignmentsListCall) Fields(s ...googleapi.Field) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) Header() http.Header
func (c *RoleAssignmentsListCall) IfNoneMatch(entityTag string) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) IncludeIndirectRoleAssignments(includeIndirectRoleAssignments bool) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) MaxResults(maxResults int64) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) PageToken(pageToken string) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) Pages(ctx context.Context, f func(*RoleAssignments) error) error
func (c *RoleAssignmentsListCall) RoleId(roleId string) *RoleAssignmentsListCall
func (c *RoleAssignmentsListCall) UserKey(userKey string) *RoleAssignmentsListCall
type RoleAssignmentsService
func NewRoleAssignmentsService(s *Service) *RoleAssignmentsService
func (r *RoleAssignmentsService) Delete(customer string, roleAssignmentId string) *RoleAssignmentsDeleteCall
func (r *RoleAssignmentsService) Get(customer string, roleAssignmentId string) *RoleAssignmentsGetCall
func (r *RoleAssignmentsService) Insert(customer string, roleassignment *RoleAssignment) *RoleAssignmentsInsertCall
func (r *RoleAssignmentsService) List(customer string) *RoleAssignmentsListCall
type RoleRolePrivileges
func (s RoleRolePrivileges) MarshalJSON() ([]byte, error)
type Roles
func (s Roles) MarshalJSON() ([]byte, error)
type RolesDeleteCall
func (c *RolesDeleteCall) Context(ctx context.Context) *RolesDeleteCall
func (c *RolesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *RolesDeleteCall) Fields(s ...googleapi.Field) *RolesDeleteCall
func (c *RolesDeleteCall) Header() http.Header
type RolesGetCall
func (c *RolesGetCall) Context(ctx context.Context) *RolesGetCall
func (c *RolesGetCall) Do(opts ...googleapi.CallOption) (*Role, error)
func (c *RolesGetCall) Fields(s ...googleapi.Field) *RolesGetCall
func (c *RolesGetCall) Header() http.Header
func (c *RolesGetCall) IfNoneMatch(entityTag string) *RolesGetCall
type RolesInsertCall
func (c *RolesInsertCall) Context(ctx context.Context) *RolesInsertCall
func (c *RolesInsertCall) Do(opts ...googleapi.CallOption) (*Role, error)
func (c *RolesInsertCall) Fields(s ...googleapi.Field) *RolesInsertCall
func (c *RolesInsertCall) Header() http.Header
type RolesListCall
func (c *RolesListCall) Context(ctx context.Context) *RolesListCall
func (c *RolesListCall) Do(opts ...googleapi.CallOption) (*Roles, error)
func (c *RolesListCall) Fields(s ...googleapi.Field) *RolesListCall
func (c *RolesListCall) Header() http.Header
func (c *RolesListCall) IfNoneMatch(entityTag string) *RolesListCall
func (c *RolesListCall) MaxResults(maxResults int64) *RolesListCall
func (c *RolesListCall) PageToken(pageToken string) *RolesListCall
func (c *RolesListCall) Pages(ctx context.Context, f func(*Roles) error) error
type RolesPatchCall
func (c *RolesPatchCall) Context(ctx context.Context) *RolesPatchCall
func (c *RolesPatchCall) Do(opts ...googleapi.CallOption) (*Role, error)
func (c *RolesPatchCall) Fields(s ...googleapi.Field) *RolesPatchCall
func (c *RolesPatchCall) Header() http.Header
type RolesService
func NewRolesService(s *Service) *RolesService
func (r *RolesService) Delete(customer string, roleId string) *RolesDeleteCall
func (r *RolesService) Get(customer string, roleId string) *RolesGetCall
func (r *RolesService) Insert(customer string, role *Role) *RolesInsertCall
func (r *RolesService) List(customer string) *RolesListCall
func (r *RolesService) Patch(customer string, roleId string, role *Role) *RolesPatchCall
func (r *RolesService) Update(customer string, roleId string, role *Role) *RolesUpdateCall
type RolesUpdateCall
func (c *RolesUpdateCall) Context(ctx context.Context) *RolesUpdateCall
func (c *RolesUpdateCall) Do(opts ...googleapi.CallOption) (*Role, error)
func (c *RolesUpdateCall) Fields(s ...googleapi.Field) *RolesUpdateCall
func (c *RolesUpdateCall) Header() http.Header
type Schema
func (s Schema) MarshalJSON() ([]byte, error)
type SchemaFieldSpec
func (s SchemaFieldSpec) MarshalJSON() ([]byte, error)
type SchemaFieldSpecNumericIndexingSpec
func (s SchemaFieldSpecNumericIndexingSpec) MarshalJSON() ([]byte, error)
func (s *SchemaFieldSpecNumericIndexingSpec) UnmarshalJSON(data []byte) error
type Schemas
func (s Schemas) MarshalJSON() ([]byte, error)
type SchemasDeleteCall
func (c *SchemasDeleteCall) Context(ctx context.Context) *SchemasDeleteCall
func (c *SchemasDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *SchemasDeleteCall) Fields(s ...googleapi.Field) *SchemasDeleteCall
func (c *SchemasDeleteCall) Header() http.Header
type SchemasGetCall
func (c *SchemasGetCall) Context(ctx context.Context) *SchemasGetCall
func (c *SchemasGetCall) Do(opts ...googleapi.CallOption) (*Schema, error)
func (c *SchemasGetCall) Fields(s ...googleapi.Field) *SchemasGetCall
func (c *SchemasGetCall) Header() http.Header
func (c *SchemasGetCall) IfNoneMatch(entityTag string) *SchemasGetCall
type SchemasInsertCall
func (c *SchemasInsertCall) Context(ctx context.Context) *SchemasInsertCall
func (c *SchemasInsertCall) Do(opts ...googleapi.CallOption) (*Schema, error)
func (c *SchemasInsertCall) Fields(s ...googleapi.Field) *SchemasInsertCall
func (c *SchemasInsertCall) Header() http.Header
type SchemasListCall
func (c *SchemasListCall) Context(ctx context.Context) *SchemasListCall
func (c *SchemasListCall) Do(opts ...googleapi.CallOption) (*Schemas, error)
func (c *SchemasListCall) Fields(s ...googleapi.Field) *SchemasListCall
func (c *SchemasListCall) Header() http.Header
func (c *SchemasListCall) IfNoneMatch(entityTag string) *SchemasListCall
type SchemasPatchCall
func (c *SchemasPatchCall) Context(ctx context.Context) *SchemasPatchCall
func (c *SchemasPatchCall) Do(opts ...googleapi.CallOption) (*Schema, error)
func (c *SchemasPatchCall) Fields(s ...googleapi.Field) *SchemasPatchCall
func (c *SchemasPatchCall) Header() http.Header
type SchemasService
func NewSchemasService(s *Service) *SchemasService
func (r *SchemasService) Delete(customerId string, schemaKey string) *SchemasDeleteCall
func (r *SchemasService) Get(customerId string, schemaKey string) *SchemasGetCall
func (r *SchemasService) Insert(customerId string, schema *Schema) *SchemasInsertCall
func (r *SchemasService) List(customerId string) *SchemasListCall
func (r *SchemasService) Patch(customerId string, schemaKey string, schema *Schema) *SchemasPatchCall
func (r *SchemasService) Update(customerId string, schemaKey string, schema *Schema) *SchemasUpdateCall
type SchemasUpdateCall
func (c *SchemasUpdateCall) Context(ctx context.Context) *SchemasUpdateCall
func (c *SchemasUpdateCall) Do(opts ...googleapi.CallOption) (*Schema, error)
func (c *SchemasUpdateCall) Fields(s ...googleapi.Field) *SchemasUpdateCall
func (c *SchemasUpdateCall) Header() http.Header
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type Token
func (s Token) MarshalJSON() ([]byte, error)
type Tokens
func (s Tokens) MarshalJSON() ([]byte, error)
type TokensDeleteCall
func (c *TokensDeleteCall) Context(ctx context.Context) *TokensDeleteCall
func (c *TokensDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *TokensDeleteCall) Fields(s ...googleapi.Field) *TokensDeleteCall
func (c *TokensDeleteCall) Header() http.Header
type TokensGetCall
func (c *TokensGetCall) Context(ctx context.Context) *TokensGetCall
func (c *TokensGetCall) Do(opts ...googleapi.CallOption) (*Token, error)
func (c *TokensGetCall) Fields(s ...googleapi.Field) *TokensGetCall
func (c *TokensGetCall) Header() http.Header
func (c *TokensGetCall) IfNoneMatch(entityTag string) *TokensGetCall
type TokensListCall
func (c *TokensListCall) Context(ctx context.Context) *TokensListCall
func (c *TokensListCall) Do(opts ...googleapi.CallOption) (*Tokens, error)
func (c *TokensListCall) Fields(s ...googleapi.Field) *TokensListCall
func (c *TokensListCall) Header() http.Header
func (c *TokensListCall) IfNoneMatch(entityTag string) *TokensListCall
type TokensService
func NewTokensService(s *Service) *TokensService
func (r *TokensService) Delete(userKey string, clientId string) *TokensDeleteCall
func (r *TokensService) Get(userKey string, clientId string) *TokensGetCall
func (r *TokensService) List(userKey string) *TokensListCall
type TwoStepVerificationService
func NewTwoStepVerificationService(s *Service) *TwoStepVerificationService
func (r *TwoStepVerificationService) TurnOff(userKey string) *TwoStepVerificationTurnOffCall
type TwoStepVerificationTurnOffCall
func (c *TwoStepVerificationTurnOffCall) Context(ctx context.Context) *TwoStepVerificationTurnOffCall
func (c *TwoStepVerificationTurnOffCall) Do(opts ...googleapi.CallOption) error
func (c *TwoStepVerificationTurnOffCall) Fields(s ...googleapi.Field) *TwoStepVerificationTurnOffCall
func (c *TwoStepVerificationTurnOffCall) Header() http.Header
type User
func (s User) MarshalJSON() ([]byte, error)
type UserAbout
func (s UserAbout) MarshalJSON() ([]byte, error)
type UserAddress
func (s UserAddress) MarshalJSON() ([]byte, error)
type UserAlias
func (s UserAlias) MarshalJSON() ([]byte, error)
type UserEmail
func (s UserEmail) MarshalJSON() ([]byte, error)
type UserEmailPublicKeyEncryptionCertificates
func (s UserEmailPublicKeyEncryptionCertificates) MarshalJSON() ([]byte, error)
type UserExternalId
func (s UserExternalId) MarshalJSON() ([]byte, error)
type UserGender
func (s UserGender) MarshalJSON() ([]byte, error)
type UserIm
func (s UserIm) MarshalJSON() ([]byte, error)
type UserKeyword
func (s UserKeyword) MarshalJSON() ([]byte, error)
type UserLanguage
func (s UserLanguage) MarshalJSON() ([]byte, error)
type UserLocation
func (s UserLocation) MarshalJSON() ([]byte, error)
type UserMakeAdmin
func (s UserMakeAdmin) MarshalJSON() ([]byte, error)
type UserName
func (s UserName) MarshalJSON() ([]byte, error)
type UserOrganization
func (s UserOrganization) MarshalJSON() ([]byte, error)
type UserPhone
func (s UserPhone) MarshalJSON() ([]byte, error)
type UserPhoto
func (s UserPhoto) MarshalJSON() ([]byte, error)
type UserPosixAccount
func (s UserPosixAccount) MarshalJSON() ([]byte, error)
type UserRelation
func (s UserRelation) MarshalJSON() ([]byte, error)
type UserSshPublicKey
func (s UserSshPublicKey) MarshalJSON() ([]byte, error)
type UserUndelete
func (s UserUndelete) MarshalJSON() ([]byte, error)
type UserWebsite
func (s UserWebsite) MarshalJSON() ([]byte, error)
type Users
func (s Users) MarshalJSON() ([]byte, error)
type UsersAliasesDeleteCall
func (c *UsersAliasesDeleteCall) Context(ctx context.Context) *UsersAliasesDeleteCall
func (c *UsersAliasesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersAliasesDeleteCall) Fields(s ...googleapi.Field) *UsersAliasesDeleteCall
func (c *UsersAliasesDeleteCall) Header() http.Header
type UsersAliasesInsertCall
func (c *UsersAliasesInsertCall) Context(ctx context.Context) *UsersAliasesInsertCall
func (c *UsersAliasesInsertCall) Do(opts ...googleapi.CallOption) (*Alias, error)
func (c *UsersAliasesInsertCall) Fields(s ...googleapi.Field) *UsersAliasesInsertCall
func (c *UsersAliasesInsertCall) Header() http.Header
type UsersAliasesListCall
func (c *UsersAliasesListCall) Context(ctx context.Context) *UsersAliasesListCall
func (c *UsersAliasesListCall) Do(opts ...googleapi.CallOption) (*Aliases, error)
func (c *UsersAliasesListCall) Event(event string) *UsersAliasesListCall
func (c *UsersAliasesListCall) Fields(s ...googleapi.Field) *UsersAliasesListCall
func (c *UsersAliasesListCall) Header() http.Header
func (c *UsersAliasesListCall) IfNoneMatch(entityTag string) *UsersAliasesListCall
type UsersAliasesService
func NewUsersAliasesService(s *Service) *UsersAliasesService
func (r *UsersAliasesService) Delete(userKey string, alias string) *UsersAliasesDeleteCall
func (r *UsersAliasesService) Insert(userKey string, alias *Alias) *UsersAliasesInsertCall
func (r *UsersAliasesService) List(userKey string) *UsersAliasesListCall
func (r *UsersAliasesService) Watch(userKey string, channel *Channel) *UsersAliasesWatchCall
type UsersAliasesWatchCall
func (c *UsersAliasesWatchCall) Context(ctx context.Context) *UsersAliasesWatchCall
func (c *UsersAliasesWatchCall) Do(opts ...googleapi.CallOption) (*Channel, error)
func (c *UsersAliasesWatchCall) Event(event string) *UsersAliasesWatchCall
func (c *UsersAliasesWatchCall) Fields(s ...googleapi.Field) *UsersAliasesWatchCall
func (c *UsersAliasesWatchCall) Header() http.Header
type UsersCreateGuestCall
func (c *UsersCreateGuestCall) Context(ctx context.Context) *UsersCreateGuestCall
func (c *UsersCreateGuestCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersCreateGuestCall) Fields(s ...googleapi.Field) *UsersCreateGuestCall
func (c *UsersCreateGuestCall) Header() http.Header
type UsersDeleteCall
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall
func (c *UsersDeleteCall) Header() http.Header
type UsersGetCall
func (c *UsersGetCall) Context(ctx context.Context) *UsersGetCall
func (c *UsersGetCall) CustomFieldMask(customFieldMask string) *UsersGetCall
func (c *UsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersGetCall) Fields(s ...googleapi.Field) *UsersGetCall
func (c *UsersGetCall) Header() http.Header
func (c *UsersGetCall) IfNoneMatch(entityTag string) *UsersGetCall
func (c *UsersGetCall) Projection(projection string) *UsersGetCall
func (c *UsersGetCall) ViewType(viewType string) *UsersGetCall
type UsersInsertCall
func (c *UsersInsertCall) Context(ctx context.Context) *UsersInsertCall
func (c *UsersInsertCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersInsertCall) Fields(s ...googleapi.Field) *UsersInsertCall
func (c *UsersInsertCall) Header() http.Header
func (c *UsersInsertCall) ResolveConflictAccount(resolveConflictAccount bool) *UsersInsertCall
type UsersListCall
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall
func (c *UsersListCall) CustomFieldMask(customFieldMask string) *UsersListCall
func (c *UsersListCall) Customer(customer string) *UsersListCall
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*Users, error)
func (c *UsersListCall) Domain(domain string) *UsersListCall
func (c *UsersListCall) Event(event string) *UsersListCall
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall
func (c *UsersListCall) Header() http.Header
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall
func (c *UsersListCall) MaxResults(maxResults int64) *UsersListCall
func (c *UsersListCall) OrderBy(orderBy string) *UsersListCall
func (c *UsersListCall) PageToken(pageToken string) *UsersListCall
func (c *UsersListCall) Pages(ctx context.Context, f func(*Users) error) error
func (c *UsersListCall) Projection(projection string) *UsersListCall
func (c *UsersListCall) Query(query string) *UsersListCall
func (c *UsersListCall) ShowDeleted(showDeleted string) *UsersListCall
func (c *UsersListCall) SortOrder(sortOrder string) *UsersListCall
func (c *UsersListCall) ViewType(viewType string) *UsersListCall
type UsersMakeAdminCall
func (c *UsersMakeAdminCall) Context(ctx context.Context) *UsersMakeAdminCall
func (c *UsersMakeAdminCall) Do(opts ...googleapi.CallOption) error
func (c *UsersMakeAdminCall) Fields(s ...googleapi.Field) *UsersMakeAdminCall
func (c *UsersMakeAdminCall) Header() http.Header
type UsersPatchCall
func (c *UsersPatchCall) Context(ctx context.Context) *UsersPatchCall
func (c *UsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersPatchCall) Fields(s ...googleapi.Field) *UsersPatchCall
func (c *UsersPatchCall) Header() http.Header
type UsersPhotosDeleteCall
func (c *UsersPhotosDeleteCall) Context(ctx context.Context) *UsersPhotosDeleteCall
func (c *UsersPhotosDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersPhotosDeleteCall) Fields(s ...googleapi.Field) *UsersPhotosDeleteCall
func (c *UsersPhotosDeleteCall) Header() http.Header
type UsersPhotosGetCall
func (c *UsersPhotosGetCall) Context(ctx context.Context) *UsersPhotosGetCall
func (c *UsersPhotosGetCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)
func (c *UsersPhotosGetCall) Fields(s ...googleapi.Field) *UsersPhotosGetCall
func (c *UsersPhotosGetCall) Header() http.Header
func (c *UsersPhotosGetCall) IfNoneMatch(entityTag string) *UsersPhotosGetCall
type UsersPhotosPatchCall
func (c *UsersPhotosPatchCall) Context(ctx context.Context) *UsersPhotosPatchCall
func (c *UsersPhotosPatchCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)
func (c *UsersPhotosPatchCall) Fields(s ...googleapi.Field) *UsersPhotosPatchCall
func (c *UsersPhotosPatchCall) Header() http.Header
type UsersPhotosService
func NewUsersPhotosService(s *Service) *UsersPhotosService
func (r *UsersPhotosService) Delete(userKey string) *UsersPhotosDeleteCall
func (r *UsersPhotosService) Get(userKey string) *UsersPhotosGetCall
func (r *UsersPhotosService) Patch(userKey string, userphoto *UserPhoto) *UsersPhotosPatchCall
func (r *UsersPhotosService) Update(userKey string, userphoto *UserPhoto) *UsersPhotosUpdateCall
type UsersPhotosUpdateCall
func (c *UsersPhotosUpdateCall) Context(ctx context.Context) *UsersPhotosUpdateCall
func (c *UsersPhotosUpdateCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)
func (c *UsersPhotosUpdateCall) Fields(s ...googleapi.Field) *UsersPhotosUpdateCall
func (c *UsersPhotosUpdateCall) Header() http.Header
type UsersService
func NewUsersService(s *Service) *UsersService
func (r *UsersService) CreateGuest(directoryuserscreateguestrequest *DirectoryUsersCreateGuestRequest) *UsersCreateGuestCall
func (r *UsersService) Delete(userKey string) *UsersDeleteCall
func (r *UsersService) Get(userKey string) *UsersGetCall
func (r *UsersService) Insert(user *User) *UsersInsertCall
func (r *UsersService) List() *UsersListCall
func (r *UsersService) MakeAdmin(userKey string, usermakeadmin *UserMakeAdmin) *UsersMakeAdminCall
func (r *UsersService) Patch(userKey string, user *User) *UsersPatchCall
func (r *UsersService) SignOut(userKey string) *UsersSignOutCall
func (r *UsersService) Undelete(userKey string, userundelete *UserUndelete) *UsersUndeleteCall
func (r *UsersService) Update(userKey string, user *User) *UsersUpdateCall
func (r *UsersService) Watch(channel *Channel) *UsersWatchCall
type UsersSignOutCall
func (c *UsersSignOutCall) Context(ctx context.Context) *UsersSignOutCall
func (c *UsersSignOutCall) Do(opts ...googleapi.CallOption) error
func (c *UsersSignOutCall) Fields(s ...googleapi.Field) *UsersSignOutCall
func (c *UsersSignOutCall) Header() http.Header
type UsersUndeleteCall
func (c *UsersUndeleteCall) Context(ctx context.Context) *UsersUndeleteCall
func (c *UsersUndeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersUndeleteCall) Fields(s ...googleapi.Field) *UsersUndeleteCall
func (c *UsersUndeleteCall) Header() http.Header
type UsersUpdateCall
func (c *UsersUpdateCall) Context(ctx context.Context) *UsersUpdateCall
func (c *UsersUpdateCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersUpdateCall) Fields(s ...googleapi.Field) *UsersUpdateCall
func (c *UsersUpdateCall) Header() http.Header
type UsersWatchCall
func (c *UsersWatchCall) Context(ctx context.Context) *UsersWatchCall
func (c *UsersWatchCall) CustomFieldMask(customFieldMask string) *UsersWatchCall
func (c *UsersWatchCall) Customer(customer string) *UsersWatchCall
func (c *UsersWatchCall) Do(opts ...googleapi.CallOption) (*Channel, error)
func (c *UsersWatchCall) Domain(domain string) *UsersWatchCall
func (c *UsersWatchCall) Event(event string) *UsersWatchCall
func (c *UsersWatchCall) Fields(s ...googleapi.Field) *UsersWatchCall
func (c *UsersWatchCall) Header() http.Header
func (c *UsersWatchCall) MaxResults(maxResults int64) *UsersWatchCall
func (c *UsersWatchCall) OrderBy(orderBy string) *UsersWatchCall
func (c *UsersWatchCall) PageToken(pageToken string) *UsersWatchCall
func (c *UsersWatchCall) Projection(projection string) *UsersWatchCall
func (c *UsersWatchCall) Query(query string) *UsersWatchCall
func (c *UsersWatchCall) ShowDeleted(showDeleted string) *UsersWatchCall
func (c *UsersWatchCall) SortOrder(sortOrder string) *UsersWatchCall
func (c *UsersWatchCall) ViewType(viewType string) *UsersWatchCall
type VerificationCode
func (s VerificationCode) MarshalJSON() ([]byte, error)
type VerificationCodes
func (s VerificationCodes) MarshalJSON() ([]byte, error)
type VerificationCodesGenerateCall
func (c *VerificationCodesGenerateCall) Context(ctx context.Context) *VerificationCodesGenerateCall
func (c *VerificationCodesGenerateCall) Do(opts ...googleapi.CallOption) error
func (c *VerificationCodesGenerateCall) Fields(s ...googleapi.Field) *VerificationCodesGenerateCall
func (c *VerificationCodesGenerateCall) Header() http.Header
type VerificationCodesInvalidateCall
func (c *VerificationCodesInvalidateCall) Context(ctx context.Context) *VerificationCodesInvalidateCall
func (c *VerificationCodesInvalidateCall) Do(opts ...googleapi.CallOption) error
func (c *VerificationCodesInvalidateCall) Fields(s ...googleapi.Field) *VerificationCodesInvalidateCall
func (c *VerificationCodesInvalidateCall) Header() http.Header
type VerificationCodesListCall
func (c *VerificationCodesListCall) Context(ctx context.Context) *VerificationCodesListCall
func (c *VerificationCodesListCall) Do(opts ...googleapi.CallOption) (*VerificationCodes, error)
func (c *VerificationCodesListCall) Fields(s ...googleapi.Field) *VerificationCodesListCall
func (c *VerificationCodesListCall) Header() http.Header
func (c *VerificationCodesListCall) IfNoneMatch(entityTag string) *VerificationCodesListCall
type VerificationCodesService
func NewVerificationCodesService(s *Service) *VerificationCodesService
func (r *VerificationCodesService) Generate(userKey string) *VerificationCodesGenerateCall
func (r *VerificationCodesService) Invalidate(userKey string) *VerificationCodesInvalidateCall
func (r *VerificationCodesService) List(userKey string) *VerificationCodesListCall
Constants ¶
View Source
const (
	// See, add, edit, and permanently delete the printers that your organization
	// can use with Chrome
	AdminChromePrintersScope = "https://www.googleapis.com/auth/admin.chrome.printers"

	// See the printers that your organization can use with Chrome
	AdminChromePrintersReadonlyScope = "https://www.googleapis.com/auth/admin.chrome.printers.readonly"

	// View and manage customer related information
	AdminDirectoryCustomerScope = "https://www.googleapis.com/auth/admin.directory.customer"

	// View customer related information
	AdminDirectoryCustomerReadonlyScope = "https://www.googleapis.com/auth/admin.directory.customer.readonly"

	// View and manage your ChromeOS devices' metadata
	AdminDirectoryDeviceChromeosScope = "https://www.googleapis.com/auth/admin.directory.device.chromeos"

	// View your ChromeOS devices' metadata
	AdminDirectoryDeviceChromeosReadonlyScope = "https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly"

	// View and manage your mobile devices' metadata
	AdminDirectoryDeviceMobileScope = "https://www.googleapis.com/auth/admin.directory.device.mobile"

	// Manage your mobile devices by performing administrative tasks
	AdminDirectoryDeviceMobileActionScope = "https://www.googleapis.com/auth/admin.directory.device.mobile.action"

	// View your mobile devices' metadata
	AdminDirectoryDeviceMobileReadonlyScope = "https://www.googleapis.com/auth/admin.directory.device.mobile.readonly"

	// View and manage the provisioning of domains for your customers
	AdminDirectoryDomainScope = "https://www.googleapis.com/auth/admin.directory.domain"

	// View domains related to your customers
	AdminDirectoryDomainReadonlyScope = "https://www.googleapis.com/auth/admin.directory.domain.readonly"

	// View and manage the provisioning of groups on your domain
	AdminDirectoryGroupScope = "https://www.googleapis.com/auth/admin.directory.group"

	// View and manage group subscriptions on your domain
	AdminDirectoryGroupMemberScope = "https://www.googleapis.com/auth/admin.directory.group.member"

	// View group subscriptions on your domain
	AdminDirectoryGroupMemberReadonlyScope = "https://www.googleapis.com/auth/admin.directory.group.member.readonly"

	// View groups on your domain
	AdminDirectoryGroupReadonlyScope = "https://www.googleapis.com/auth/admin.directory.group.readonly"

	// View and manage organization units on your domain
	AdminDirectoryOrgunitScope = "https://www.googleapis.com/auth/admin.directory.orgunit"

	// View organization units on your domain
	AdminDirectoryOrgunitReadonlyScope = "https://www.googleapis.com/auth/admin.directory.orgunit.readonly"

	// View and manage the provisioning of calendar resources on your domain
	AdminDirectoryResourceCalendarScope = "https://www.googleapis.com/auth/admin.directory.resource.calendar"

	// View calendar resources on your domain
	AdminDirectoryResourceCalendarReadonlyScope = "https://www.googleapis.com/auth/admin.directory.resource.calendar.readonly"

	// Manage delegated admin roles for your domain
	AdminDirectoryRolemanagementScope = "https://www.googleapis.com/auth/admin.directory.rolemanagement"

	// View delegated admin roles for your domain
	AdminDirectoryRolemanagementReadonlyScope = "https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly"

	// View and manage the provisioning of users on your domain
	AdminDirectoryUserScope = "https://www.googleapis.com/auth/admin.directory.user"

	// View and manage user aliases on your domain
	AdminDirectoryUserAliasScope = "https://www.googleapis.com/auth/admin.directory.user.alias"

	// View user aliases on your domain
	AdminDirectoryUserAliasReadonlyScope = "https://www.googleapis.com/auth/admin.directory.user.alias.readonly"

	// See info about users on your domain
	AdminDirectoryUserReadonlyScope = "https://www.googleapis.com/auth/admin.directory.user.readonly"

	// Manage data access permissions for users on your domain
	AdminDirectoryUserSecurityScope = "https://www.googleapis.com/auth/admin.directory.user.security"

	// View and manage the provisioning of user schemas on your domain
	AdminDirectoryUserschemaScope = "https://www.googleapis.com/auth/admin.directory.userschema"

	// View user schemas on your domain
	AdminDirectoryUserschemaReadonlyScope = "https://www.googleapis.com/auth/admin.directory.userschema.readonly"

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
type Alias ¶
type Alias struct {
	Alias        string `json:"alias,omitempty"`
	Etag         string `json:"etag,omitempty"`
	Id           string `json:"id,omitempty"`
	Kind         string `json:"kind,omitempty"`
	PrimaryEmail string `json:"primaryEmail,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Alias") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alias") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Alias: JSON template for Alias object in Directory API.

func (Alias) MarshalJSON ¶
func (s Alias) MarshalJSON() ([]byte, error)
type Aliases ¶
type Aliases struct {
	Aliases []interface{} `json:"aliases,omitempty"`
	Etag    string        `json:"etag,omitempty"`
	Kind    string        `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Aliases") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Aliases") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Aliases: JSON response template to list aliases in Directory API.

func (Aliases) MarshalJSON ¶
func (s Aliases) MarshalJSON() ([]byte, error)
type Asp ¶
type Asp struct {
	// CodeId: The unique ID of the ASP.
	CodeId int64 `json:"codeId,omitempty"`
	// CreationTime: The time when the ASP was created. Expressed in Unix time
	// (https://en.wikipedia.org/wiki/Epoch_time) format.
	CreationTime int64 `json:"creationTime,omitempty,string"`
	// Etag: ETag of the ASP.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the API resource. This is always `admin#directory#asp`.
	Kind string `json:"kind,omitempty"`
	// LastTimeUsed: The time when the ASP was last used. Expressed in Unix time
	// (https://en.wikipedia.org/wiki/Epoch_time) format.
	LastTimeUsed int64 `json:"lastTimeUsed,omitempty,string"`
	// Name: The name of the application that the user, represented by their
	// `userId`, entered when the ASP was created.
	Name string `json:"name,omitempty"`
	// UserKey: The unique ID of the user who issued the ASP.
	UserKey string `json:"userKey,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CodeId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CodeId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Asp: An application-specific password (ASP) is used with applications that do not accept a verification code when logging into the application on certain devices. The ASP access code is used instead of the login and password you commonly use when accessing an application through a browser. For more information about ASPs and how to create one, see the help center (https://support.google.com/a/answer/2537800#asp).

func (Asp) MarshalJSON ¶
func (s Asp) MarshalJSON() ([]byte, error)
type Asps ¶
type Asps struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of ASP resources.
	Items []*Asp `json:"items,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#aspList`.
	Kind string `json:"kind,omitempty"`

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
func (Asps) MarshalJSON ¶
func (s Asps) MarshalJSON() ([]byte, error)
type AspsDeleteCall ¶
type AspsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AspsDeleteCall) Context ¶
func (c *AspsDeleteCall) Context(ctx context.Context) *AspsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AspsDeleteCall) Do ¶
func (c *AspsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.asps.delete" call.

func (*AspsDeleteCall) Fields ¶
func (c *AspsDeleteCall) Fields(s ...googleapi.Field) *AspsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AspsDeleteCall) Header ¶
func (c *AspsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AspsGetCall ¶
type AspsGetCall struct {
	// contains filtered or unexported fields
}
func (*AspsGetCall) Context ¶
func (c *AspsGetCall) Context(ctx context.Context) *AspsGetCall

Context sets the context to be used in this call's Do method.

func (*AspsGetCall) Do ¶
func (c *AspsGetCall) Do(opts ...googleapi.CallOption) (*Asp, error)

Do executes the "directory.asps.get" call. Any non-2xx status code is an error. Response headers are in either *Asp.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AspsGetCall) Fields ¶
func (c *AspsGetCall) Fields(s ...googleapi.Field) *AspsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AspsGetCall) Header ¶
func (c *AspsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AspsGetCall) IfNoneMatch ¶
func (c *AspsGetCall) IfNoneMatch(entityTag string) *AspsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AspsListCall ¶
type AspsListCall struct {
	// contains filtered or unexported fields
}
func (*AspsListCall) Context ¶
func (c *AspsListCall) Context(ctx context.Context) *AspsListCall

Context sets the context to be used in this call's Do method.

func (*AspsListCall) Do ¶
func (c *AspsListCall) Do(opts ...googleapi.CallOption) (*Asps, error)

Do executes the "directory.asps.list" call. Any non-2xx status code is an error. Response headers are in either *Asps.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AspsListCall) Fields ¶
func (c *AspsListCall) Fields(s ...googleapi.Field) *AspsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AspsListCall) Header ¶
func (c *AspsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AspsListCall) IfNoneMatch ¶
func (c *AspsListCall) IfNoneMatch(entityTag string) *AspsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AspsService ¶
type AspsService struct {
	// contains filtered or unexported fields
}
func NewAspsService ¶
func NewAspsService(s *Service) *AspsService
func (*AspsService) Delete ¶
func (r *AspsService) Delete(userKey string, codeId int64) *AspsDeleteCall

Delete: Deletes an ASP issued by a user.

codeId: The unique ID of the ASP to be deleted.
userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*AspsService) Get ¶
func (r *AspsService) Get(userKey string, codeId int64) *AspsGetCall

Get: Gets information about an ASP issued by a user.

codeId: The unique ID of the ASP.
userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*AspsService) List ¶
func (r *AspsService) List(userKey string) *AspsListCall

List: Lists the ASPs issued by a user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
type AuxiliaryMessage ¶
added in v0.42.0
type AuxiliaryMessage struct {
	// AuxiliaryMessage: Human readable message in English. Example: "Given printer
	// is invalid or no longer supported."
	AuxiliaryMessage string `json:"auxiliaryMessage,omitempty"`
	// FieldMask: Field that this message concerns.
	FieldMask string `json:"fieldMask,omitempty"`
	// Severity: Message severity
	//
	// Possible values:
	//   "SEVERITY_UNSPECIFIED" - Message type unspecified.
	//   "SEVERITY_INFO" - Message of severity: info.
	//   "SEVERITY_WARNING" - Message of severity: warning.
	//   "SEVERITY_ERROR" - Message of severity: error.
	Severity string `json:"severity,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuxiliaryMessage") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuxiliaryMessage") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuxiliaryMessage: Auxiliary message about issues with printers or settings. Example: {message_type:AUXILIARY_MESSAGE_WARNING, field_mask:make_and_model, message:"Given printer is invalid or no longer supported."}

func (AuxiliaryMessage) MarshalJSON ¶
added in v0.42.0
func (s AuxiliaryMessage) MarshalJSON() ([]byte, error)
type BacklightInfo ¶
added in v0.169.0
type BacklightInfo struct {
	// Brightness: Output only. Current brightness of the backlight, between 0 and
	// max_brightness.
	Brightness int64 `json:"brightness,omitempty"`
	// MaxBrightness: Output only. Maximum brightness for the backlight.
	MaxBrightness int64 `json:"maxBrightness,omitempty"`
	// Path: Output only. Path to this backlight on the system. Useful if the
	// caller needs to correlate with other information.
	Path string `json:"path,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Brightness") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Brightness") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BacklightInfo: Information about the device's backlights.

func (BacklightInfo) MarshalJSON ¶
added in v0.169.0
func (s BacklightInfo) MarshalJSON() ([]byte, error)
type BatchChangeChromeOsDeviceStatusRequest ¶
added in v0.155.0
type BatchChangeChromeOsDeviceStatusRequest struct {
	// ChangeChromeOsDeviceStatusAction: Required. The action to take on the
	// ChromeOS device in order to change its status.
	//
	// Possible values:
	//   "CHANGE_CHROME_OS_DEVICE_STATUS_ACTION_UNSPECIFIED" - Default value. Value
	// is unused.
	//   "CHANGE_CHROME_OS_DEVICE_STATUS_ACTION_DEPROVISION" - Deprovisions a
	// ChromeOS device. If you have ChromeOS devices that are no longer being used
	// in your organization, you should deprovision them so that you’re no longer
	// managing them. Deprovisioning the device removes all policies that were on
	// the device as well as device-level printers and the ability to use the
	// device as a kiosk. Depending on the upgrade that’s associated with the
	// device this action might release the license back into the license pool;
	// which allows you to use the license on a different device.
	//   "CHANGE_CHROME_OS_DEVICE_STATUS_ACTION_DISABLE" - Disables a ChromeOS
	// device. Use this action if a user loses their device or it’s stolen, this
	// makes it such that the device is still managed, so it will still receive
	// policies, but no one can use it. Depending on the upgrade that’s
	// associated with the device this action might release the license back into
	// the license pool; which allows you to use the license on a different device.
	//   "CHANGE_CHROME_OS_DEVICE_STATUS_ACTION_REENABLE" - Reenables a ChromeOS
	// device to be used after being disabled. Reenables the device once it's no
	// longer lost or it's been recovered. This allows the device to be used again.
	// Depending on the upgrade associated with the device this might consume one
	// license from the license pool, meaning that if there aren't enough licenses
	// available the operation will fail.
	ChangeChromeOsDeviceStatusAction string `json:"changeChromeOsDeviceStatusAction,omitempty"`
	// DeprovisionReason: Optional. The reason behind a device deprovision. Must be
	// provided if 'changeChromeOsDeviceStatusAction' is set to
	// 'CHANGE_CHROME_OS_DEVICE_STATUS_ACTION_DEPROVISION'. Otherwise, omit this
	// field.
	//
	// Possible values:
	//   "DEPROVISION_REASON_UNSPECIFIED" - The deprovision reason is unknown.
	//   "DEPROVISION_REASON_SAME_MODEL_REPLACEMENT" - Same model replacement. You
	// have return materials authorization (RMA) or you are replacing a
	// malfunctioning device under warranty with the same device model.
	//   "DEPROVISION_REASON_UPGRADE" - The device was upgraded.
	//   "DEPROVISION_REASON_DOMAIN_MOVE" - The device's domain was changed.
	//   "DEPROVISION_REASON_SERVICE_EXPIRATION" - Service expired for the device.
	//   "DEPROVISION_REASON_OTHER" - The device was deprovisioned for a legacy
	// reason that is no longer supported.
	//   "DEPROVISION_REASON_DIFFERENT_MODEL_REPLACEMENT" - Different model
	// replacement. You are replacing this device with an upgraded or newer device
	// model.
	//   "DEPROVISION_REASON_RETIRING_DEVICE" - Retiring from fleet. You are
	// donating, discarding, or otherwise removing the device from use.
	//   "DEPROVISION_REASON_UPGRADE_TRANSFER" - ChromeOS Flex upgrade transfer.
	// This is a ChromeOS Flex device that you are replacing with a Chromebook
	// within a year.
	//   "DEPROVISION_REASON_NOT_REQUIRED" - A reason was not required. For
	// example, the licenses were returned to the customer's license pool.
	//   "DEPROVISION_REASON_REPAIR_CENTER" - The device was deprovisioned by the
	// Repair Service Center. Can only be set by Repair Service Center during RMA.
	DeprovisionReason string `json:"deprovisionReason,omitempty"`
	// DeviceIds: Required. List of the IDs of the ChromeOS devices to change.
	// Maximum 50.
	DeviceIds []string `json:"deviceIds,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ChangeChromeOsDeviceStatusAction") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ChangeChromeOsDeviceStatusAction") to include in API requests with the JSON
	// null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

BatchChangeChromeOsDeviceStatusRequest: A request for changing the status of a batch of ChromeOS devices.

func (BatchChangeChromeOsDeviceStatusRequest) MarshalJSON ¶
added in v0.155.0
func (s BatchChangeChromeOsDeviceStatusRequest) MarshalJSON() ([]byte, error)
type BatchChangeChromeOsDeviceStatusResponse ¶
added in v0.155.0
type BatchChangeChromeOsDeviceStatusResponse struct {
	// ChangeChromeOsDeviceStatusResults: The results for each of the ChromeOS
	// devices provided in the request.
	ChangeChromeOsDeviceStatusResults []*ChangeChromeOsDeviceStatusResult `json:"changeChromeOsDeviceStatusResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "ChangeChromeOsDeviceStatusResults") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ChangeChromeOsDeviceStatusResults") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

BatchChangeChromeOsDeviceStatusResponse: The response of changing the status of a batch of ChromeOS devices.

func (BatchChangeChromeOsDeviceStatusResponse) MarshalJSON ¶
added in v0.155.0
func (s BatchChangeChromeOsDeviceStatusResponse) MarshalJSON() ([]byte, error)
type BatchCreatePrintServersRequest ¶
added in v0.98.0
type BatchCreatePrintServersRequest struct {
	// Requests: Required. A list of `PrintServer` resources to be created (max
	// `50` per batch).
	Requests []*CreatePrintServerRequest `json:"requests,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Requests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Requests") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchCreatePrintServersRequest: Request to add multiple new print servers in a batch.

func (BatchCreatePrintServersRequest) MarshalJSON ¶
added in v0.98.0
func (s BatchCreatePrintServersRequest) MarshalJSON() ([]byte, error)
type BatchCreatePrintServersResponse ¶
added in v0.98.0
type BatchCreatePrintServersResponse struct {
	// Failures: A list of create failures. `PrintServer` IDs are not populated, as
	// print servers were not created.
	Failures []*PrintServerFailureInfo `json:"failures,omitempty"`
	// PrintServers: A list of successfully created print servers with their IDs
	// populated.
	PrintServers []*PrintServer `json:"printServers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Failures") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Failures") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (BatchCreatePrintServersResponse) MarshalJSON ¶
added in v0.98.0
func (s BatchCreatePrintServersResponse) MarshalJSON() ([]byte, error)
type BatchCreatePrintersRequest ¶
added in v0.42.0
type BatchCreatePrintersRequest struct {
	// Requests: A list of Printers to be created. Max 50 at a time.
	Requests []*CreatePrinterRequest `json:"requests,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Requests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Requests") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchCreatePrintersRequest: Request for adding new printers in batch.

func (BatchCreatePrintersRequest) MarshalJSON ¶
added in v0.42.0
func (s BatchCreatePrintersRequest) MarshalJSON() ([]byte, error)
type BatchCreatePrintersResponse ¶
added in v0.42.0
type BatchCreatePrintersResponse struct {
	// Failures: A list of create failures. Printer IDs are not populated, as
	// printer were not created.
	Failures []*FailureInfo `json:"failures,omitempty"`
	// Printers: A list of successfully created printers with their IDs populated.
	Printers []*Printer `json:"printers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Failures") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Failures") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchCreatePrintersResponse: Response for adding new printers in batch.

func (BatchCreatePrintersResponse) MarshalJSON ¶
added in v0.42.0
func (s BatchCreatePrintersResponse) MarshalJSON() ([]byte, error)
type BatchDeletePrintServersRequest ¶
added in v0.98.0
type BatchDeletePrintServersRequest struct {
	// PrintServerIds: A list of print server IDs that should be deleted (max `100`
	// per batch).
	PrintServerIds []string `json:"printServerIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrintServerIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrintServerIds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchDeletePrintServersRequest: Request to delete multiple existing print servers in a batch.

func (BatchDeletePrintServersRequest) MarshalJSON ¶
added in v0.98.0
func (s BatchDeletePrintServersRequest) MarshalJSON() ([]byte, error)
type BatchDeletePrintServersResponse ¶
added in v0.98.0
type BatchDeletePrintServersResponse struct {
	// FailedPrintServers: A list of update failures.
	FailedPrintServers []*PrintServerFailureInfo `json:"failedPrintServers,omitempty"`
	// PrintServerIds: A list of print server IDs that were successfully deleted.
	PrintServerIds []string `json:"printServerIds,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FailedPrintServers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FailedPrintServers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (BatchDeletePrintServersResponse) MarshalJSON ¶
added in v0.98.0
func (s BatchDeletePrintServersResponse) MarshalJSON() ([]byte, error)
type BatchDeletePrintersRequest ¶
added in v0.42.0
type BatchDeletePrintersRequest struct {
	// PrinterIds: A list of Printer.id that should be deleted. Max 100 at a time.
	PrinterIds []string `json:"printerIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrinterIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrinterIds") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchDeletePrintersRequest: Request for deleting existing printers in batch.

func (BatchDeletePrintersRequest) MarshalJSON ¶
added in v0.42.0
func (s BatchDeletePrintersRequest) MarshalJSON() ([]byte, error)
type BatchDeletePrintersResponse ¶
added in v0.42.0
type BatchDeletePrintersResponse struct {
	// FailedPrinters: A list of update failures.
	FailedPrinters []*FailureInfo `json:"failedPrinters,omitempty"`
	// PrinterIds: A list of Printer.id that were successfully deleted.
	PrinterIds []string `json:"printerIds,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FailedPrinters") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FailedPrinters") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchDeletePrintersResponse: Response for deleting existing printers in batch.

func (BatchDeletePrintersResponse) MarshalJSON ¶
added in v0.42.0
func (s BatchDeletePrintersResponse) MarshalJSON() ([]byte, error)
type BluetoothAdapterInfo ¶
added in v0.254.0
type BluetoothAdapterInfo struct {
	// Address: Output only. The MAC address of the adapter.
	Address string `json:"address,omitempty"`
	// NumConnectedDevices: Output only. The number of devices connected to this
	// adapter.
	NumConnectedDevices int64 `json:"numConnectedDevices,omitempty"`
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

BluetoothAdapterInfo: Information about a device's Bluetooth adapter.

func (BluetoothAdapterInfo) MarshalJSON ¶
added in v0.254.0
func (s BluetoothAdapterInfo) MarshalJSON() ([]byte, error)
type Building ¶
type Building struct {
	// Address: The postal address of the building. See `PostalAddress`
	// (/my-business/reference/rest/v4/PostalAddress) for details. Note that only a
	// single address line and region code are required.
	Address *BuildingAddress `json:"address,omitempty"`
	// BuildingId: Unique identifier for the building. The maximum length is 100
	// characters.
	BuildingId string `json:"buildingId,omitempty"`
	// BuildingName: The building name as seen by users in Calendar. Must be unique
	// for the customer. For example, "NYC-CHEL". The maximum length is 100
	// characters.
	BuildingName string `json:"buildingName,omitempty"`
	// Coordinates: The geographic coordinates of the center of the building,
	// expressed as latitude and longitude in decimal degrees.
	Coordinates *BuildingCoordinates `json:"coordinates,omitempty"`
	// Description: A brief description of the building. For example, "Chelsea
	// Market".
	Description string `json:"description,omitempty"`
	// Etags: ETag of the resource.
	Etags string `json:"etags,omitempty"`
	// FloorNames: The display names for all floors in this building. The floors
	// are expected to be sorted in ascending order, from lowest floor to highest
	// floor. For example, ["B2", "B1", "L", "1", "2", "2M", "3", "PH"] Must
	// contain at least one entry.
	FloorNames []string `json:"floorNames,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

Building: Public API: Resources.buildings

func (Building) MarshalJSON ¶
func (s Building) MarshalJSON() ([]byte, error)
type BuildingAddress ¶
added in v0.2.0
type BuildingAddress struct {
	// AddressLines: Unstructured address lines describing the lower levels of an
	// address.
	AddressLines []string `json:"addressLines,omitempty"`
	// AdministrativeArea: Optional. Highest administrative subdivision which is
	// used for postal addresses of a country or region.
	AdministrativeArea string `json:"administrativeArea,omitempty"`
	// LanguageCode: Optional. BCP-47 language code of the contents of this address
	// (if known).
	LanguageCode string `json:"languageCode,omitempty"`
	// Locality: Optional. Generally refers to the city/town portion of the
	// address. Examples: US city, IT comune, UK post town. In regions of the world
	// where localities are not well defined or do not fit into this structure
	// well, leave locality empty and use addressLines.
	Locality string `json:"locality,omitempty"`
	// PostalCode: Optional. Postal code of the address.
	PostalCode string `json:"postalCode,omitempty"`
	// RegionCode: Required. CLDR region code of the country/region of the address.
	RegionCode string `json:"regionCode,omitempty"`
	// Sublocality: Optional. Sublocality of the address.
	Sublocality string `json:"sublocality,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AddressLines") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AddressLines") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BuildingAddress: Public API: Resources.buildings

func (BuildingAddress) MarshalJSON ¶
added in v0.2.0
func (s BuildingAddress) MarshalJSON() ([]byte, error)
type BuildingCoordinates ¶
type BuildingCoordinates struct {
	// Latitude: Latitude in decimal degrees.
	Latitude float64 `json:"latitude,omitempty"`
	// Longitude: Longitude in decimal degrees.
	Longitude float64 `json:"longitude,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Latitude") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Latitude") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BuildingCoordinates: Public API: Resources.buildings

func (BuildingCoordinates) MarshalJSON ¶
func (s BuildingCoordinates) MarshalJSON() ([]byte, error)
func (*BuildingCoordinates) UnmarshalJSON ¶
func (s *BuildingCoordinates) UnmarshalJSON(data []byte) error
type Buildings ¶
type Buildings struct {
	// Buildings: The Buildings in this page of results.
	Buildings []*Building `json:"buildings,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: The continuation token, used to page through large result
	// sets. Provide this value in a subsequent request to return the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Buildings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Buildings") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Buildings: Public API: Resources.buildings

func (Buildings) MarshalJSON ¶
func (s Buildings) MarshalJSON() ([]byte, error)
type ByteUsage ¶
added in v0.205.0
type ByteUsage struct {
	// CapacityBytes: Output only. The total capacity value, in bytes.
	CapacityBytes int64 `json:"capacityBytes,omitempty,string"`
	// UsedBytes: Output only. The current usage value, in bytes.
	UsedBytes int64 `json:"usedBytes,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "CapacityBytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CapacityBytes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ByteUsage: Represents a data capacity with some amount of current usage in bytes.

func (ByteUsage) MarshalJSON ¶
added in v0.205.0
func (s ByteUsage) MarshalJSON() ([]byte, error)
type CalendarResource ¶
type CalendarResource struct {
	// BuildingId: Unique ID for the building a resource is located in.
	BuildingId string `json:"buildingId,omitempty"`
	// Capacity: Capacity of a resource, number of seats in a room.
	Capacity int64 `json:"capacity,omitempty"`
	// Etags: ETag of the resource.
	Etags string `json:"etags,omitempty"`
	// FeatureInstances: Instances of features for the calendar resource.
	FeatureInstances interface{} `json:"featureInstances,omitempty"`
	// FloorName: Name of the floor a resource is located on.
	FloorName string `json:"floorName,omitempty"`
	// FloorSection: Name of the section within a floor a resource is located in.
	FloorSection string `json:"floorSection,omitempty"`
	// GeneratedResourceName: The read-only auto-generated name of the calendar
	// resource which includes metadata about the resource such as building name,
	// floor, capacity, etc. For example, "NYC-2-Training Room 1A (16)".
	GeneratedResourceName string `json:"generatedResourceName,omitempty"`
	// Kind: The type of the resource. For calendar resources, the value is
	// `admin#directory#resources#calendars#CalendarResource`.
	Kind string `json:"kind,omitempty"`
	// ResourceCategory: The category of the calendar resource. Either
	// CONFERENCE_ROOM or OTHER. Legacy data is set to CATEGORY_UNKNOWN.
	ResourceCategory string `json:"resourceCategory,omitempty"`
	// ResourceDescription: Description of the resource, visible only to admins.
	ResourceDescription string `json:"resourceDescription,omitempty"`
	// ResourceEmail: The read-only email for the calendar resource. Generated as
	// part of creating a new calendar resource.
	ResourceEmail string `json:"resourceEmail,omitempty"`
	// ResourceId: The unique ID for the calendar resource.
	ResourceId string `json:"resourceId,omitempty"`
	// ResourceName: The name of the calendar resource. For example, "Training Room
	// 1A".
	ResourceName string `json:"resourceName,omitempty"`
	// ResourceType: The type of the calendar resource, intended for non-room
	// resources.
	ResourceType string `json:"resourceType,omitempty"`
	// UserVisibleDescription: Description of the resource, visible to users and
	// admins.
	UserVisibleDescription string `json:"userVisibleDescription,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BuildingId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuildingId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CalendarResource: Public API: Resources.calendars

func (CalendarResource) MarshalJSON ¶
func (s CalendarResource) MarshalJSON() ([]byte, error)
type CalendarResources ¶
type CalendarResources struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: The CalendarResources in this page of results.
	Items []*CalendarResource `json:"items,omitempty"`
	// Kind: Identifies this as a collection of CalendarResources. This is always
	// `admin#directory#resources#calendars#calendarResourcesList`.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: The continuation token, used to page through large result
	// sets. Provide this value in a subsequent request to return the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

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

CalendarResources: Public API: Resources.calendars

func (CalendarResources) MarshalJSON ¶
func (s CalendarResources) MarshalJSON() ([]byte, error)
type ChangeChromeOsDeviceStatusResult ¶
added in v0.155.0
type ChangeChromeOsDeviceStatusResult struct {
	// DeviceId: The unique ID of the ChromeOS device.
	DeviceId string `json:"deviceId,omitempty"`
	// Error: The error result of the operation in case of failure.
	Error *Status `json:"error,omitempty"`
	// Response: The device could change its status successfully.
	Response *ChangeChromeOsDeviceStatusSucceeded `json:"response,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChangeChromeOsDeviceStatusResult: The result of a single ChromeOS device for a Change state operation.

func (ChangeChromeOsDeviceStatusResult) MarshalJSON ¶
added in v0.155.0
func (s ChangeChromeOsDeviceStatusResult) MarshalJSON() ([]byte, error)
type ChangeChromeOsDeviceStatusSucceeded ¶
added in v0.155.0
type ChangeChromeOsDeviceStatusSucceeded struct {
}

ChangeChromeOsDeviceStatusSucceeded: Response for a successful ChromeOS device status change.

type Channel ¶
type Channel struct {
	// Address: The address where notifications are delivered for this channel.
	Address string `json:"address,omitempty"`
	// Expiration: Date and time of notification channel expiration, expressed as a
	// Unix timestamp, in milliseconds. Optional.
	Expiration int64 `json:"expiration,omitempty,string"`
	// Id: A UUID or similar unique string that identifies this channel.
	Id string `json:"id,omitempty"`
	// Kind: Identifies this as a notification channel used to watch for changes to
	// a resource, which is `api#channel`.
	Kind string `json:"kind,omitempty"`
	// Params: Additional parameters controlling delivery channel behavior.
	// Optional. For example, `params.ttl` specifies the time-to-live in seconds
	// for the notification channel, where the default is 2 hours and the maximum
	// TTL is 2 days.
	Params map[string]string `json:"params,omitempty"`
	// Payload: A Boolean value to indicate whether payload is wanted. Optional.
	Payload bool `json:"payload,omitempty"`
	// ResourceId: An opaque ID that identifies the resource being watched on this
	// channel. Stable across different API versions.
	ResourceId string `json:"resourceId,omitempty"`
	// ResourceUri: A version-specific identifier for the watched resource.
	ResourceUri string `json:"resourceUri,omitempty"`
	// Token: An arbitrary string delivered to the target address with each
	// notification delivered over this channel. Optional.
	Token string `json:"token,omitempty"`
	// Type: The type of delivery mechanism used for this channel.
	Type string `json:"type,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

Channel: An notification channel used to watch for resource changes.

func (Channel) MarshalJSON ¶
func (s Channel) MarshalJSON() ([]byte, error)
type ChannelsService ¶
type ChannelsService struct {
	// contains filtered or unexported fields
}
func NewChannelsService ¶
func NewChannelsService(s *Service) *ChannelsService
func (*ChannelsService) Stop ¶
func (r *ChannelsService) Stop(channel *Channel) *ChannelsStopCall

Stop: Stops watching resources through this channel.

type ChannelsStopCall ¶
type ChannelsStopCall struct {
	// contains filtered or unexported fields
}
func (*ChannelsStopCall) Context ¶
func (c *ChannelsStopCall) Context(ctx context.Context) *ChannelsStopCall

Context sets the context to be used in this call's Do method.

func (*ChannelsStopCall) Do ¶
func (c *ChannelsStopCall) Do(opts ...googleapi.CallOption) error

Do executes the "admin.channels.stop" call.

func (*ChannelsStopCall) Fields ¶
func (c *ChannelsStopCall) Fields(s ...googleapi.Field) *ChannelsStopCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChannelsStopCall) Header ¶
func (c *ChannelsStopCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ChromeOsDevice ¶
type ChromeOsDevice struct {
	// ActiveTimeRanges: A list of active time ranges (Read-only).
	ActiveTimeRanges []*ChromeOsDeviceActiveTimeRanges `json:"activeTimeRanges,omitempty"`
	// AnnotatedAssetId: The asset identifier as noted by an administrator or
	// specified during enrollment.
	AnnotatedAssetId string `json:"annotatedAssetId,omitempty"`
	// AnnotatedLocation: The address or location of the device as noted by the
	// administrator. Maximum length is `200` characters. Empty values are allowed.
	AnnotatedLocation string `json:"annotatedLocation,omitempty"`
	// AnnotatedUser: The user of the device as noted by the administrator. Maximum
	// length is 100 characters. Empty values are allowed.
	AnnotatedUser string `json:"annotatedUser,omitempty"`
	// AutoUpdateExpiration: (Read-only) The timestamp after which the device will
	// stop receiving Chrome updates or support. Please use "autoUpdateThrough"
	// instead.
	AutoUpdateExpiration int64 `json:"autoUpdateExpiration,omitempty,string"`
	// AutoUpdateThrough: Output only. The timestamp after which the device will
	// stop receiving Chrome updates or support.
	AutoUpdateThrough string `json:"autoUpdateThrough,omitempty"`
	// BacklightInfo: Output only. Contains backlight information for the device.
	BacklightInfo []*BacklightInfo `json:"backlightInfo,omitempty"`
	// BluetoothAdapterInfo: Output only. Information about Bluetooth adapters of
	// the device.
	BluetoothAdapterInfo []*BluetoothAdapterInfo `json:"bluetoothAdapterInfo,omitempty"`
	// BootMode: The boot mode for the device. The possible values are: *
	// `Verified`: The device is running a valid version of the Chrome OS. * `Dev`:
	// The devices's developer hardware switch is enabled. When booted, the device
	// has a command line shell. For an example of a developer switch, see the
	// Chromebook developer information
	// (https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/samsung-series-5-chromebook#TOC-Developer-switch).
	BootMode string `json:"bootMode,omitempty"`
	// ChromeOsType: Output only. Chrome OS type of the device.
	//
	// Possible values:
	//   "chromeOsTypeUnspecified" - Chrome OS Type unspecified.
	//   "chromeOsFlex" - Chrome OS Type Chrome OS Flex.
	//   "chromeOs" - Chrome OS Type Chrome OS.
	ChromeOsType string `json:"chromeOsType,omitempty"`
	// CpuInfo: Information regarding CPU specs in the device.
	CpuInfo []*ChromeOsDeviceCpuInfo `json:"cpuInfo,omitempty"`
	// CpuStatusReports: Reports of CPU utilization and temperature (Read-only)
	CpuStatusReports []*ChromeOsDeviceCpuStatusReports `json:"cpuStatusReports,omitempty"`
	// DeprovisionReason: (Read-only) Deprovision reason.
	//
	// Possible values:
	//   "DEPROVISION_REASON_UNSPECIFIED" - The deprovision reason is unknown.
	//   "DEPROVISION_REASON_SAME_MODEL_REPLACEMENT" - Same model replacement. You
	// have return materials authorization (RMA) or you are replacing a
	// malfunctioning device under warranty with the same device model.
	//   "DEPROVISION_REASON_UPGRADE" - The device was upgraded.
	//   "DEPROVISION_REASON_DOMAIN_MOVE" - The device's domain was changed.
	//   "DEPROVISION_REASON_SERVICE_EXPIRATION" - Service expired for the device.
	//   "DEPROVISION_REASON_OTHER" - The device was deprovisioned for a legacy
	// reason that is no longer supported.
	//   "DEPROVISION_REASON_DIFFERENT_MODEL_REPLACEMENT" - Different model
	// replacement. You are replacing this device with an upgraded or newer device
	// model.
	//   "DEPROVISION_REASON_RETIRING_DEVICE" - Retiring from fleet. You are
	// donating, discarding, or otherwise removing the device from use.
	//   "DEPROVISION_REASON_UPGRADE_TRANSFER" - ChromeOS Flex upgrade transfer.
	// This is a ChromeOS Flex device that you are replacing with a Chromebook
	// within a year.
	//   "DEPROVISION_REASON_NOT_REQUIRED" - A reason was not required. For
	// example, the licenses were returned to the customer's license pool.
	//   "DEPROVISION_REASON_REPAIR_CENTER" - The device was deprovisioned by the
	// Repair Service Center. Can only be set by Repair Service Center during RMA.
	DeprovisionReason string `json:"deprovisionReason,omitempty"`
	// DeviceFiles: A list of device files to download (Read-only)
	DeviceFiles []*ChromeOsDeviceDeviceFiles `json:"deviceFiles,omitempty"`
	// DeviceId: The unique ID of the Chrome device.
	DeviceId string `json:"deviceId,omitempty"`
	// DeviceLicenseType: Output only. Device license type.
	//
	// Possible values:
	//   "deviceLicenseTypeUnspecified" - The license type is unknown.
	//   "enterprise" - The device is bundled with a perpetual Chrome Enterprise
	// Upgrade.
	//   "enterpriseUpgrade" - The device has an annual standalone Chrome
	// Enterprise Upgrade.
	//   "educationUpgrade" - The device has a perpetual standalone Chrome
	// Education Upgrade.
	//   "education" - The device is bundled with a perpetual Chrome Education
	// Upgrade.
	//   "kioskUpgrade" - The device has an annual Kiosk Upgrade.
	//   "enterpriseUpgradePerpetual" - Indicates that the device is consuming a
	// standalone, perpetual Chrome Enterprise Upgrade, a Chrome Enterprise
	// license.
	//   "enterpriseUpgradeFixedTerm" - Indicates that the device is consuming a
	// standalone, fixed-term Chrome Enterprise Upgrade, a Chrome Enterprise
	// license.
	//   "educationUpgradePerpetual" - Indicates that the device is consuming a
	// standalone, perpetual Chrome Education Upgrade(AKA Chrome EDU perpetual
	// license).
	//   "educationUpgradeFixedTerm" - Indicates that the device is consuming a
	// standalone, fixed-term Chrome Education Upgrade(AKA Chrome EDU fixed-term
	// license).
	DeviceLicenseType string `json:"deviceLicenseType,omitempty"`
	// DiskSpaceUsage: Output only. How much disk space the device has available
	// and is currently using.
	DiskSpaceUsage *ByteUsage `json:"diskSpaceUsage,omitempty"`
	// DiskVolumeReports: Reports of disk space and other info about
	// mounted/connected volumes.
	DiskVolumeReports []*ChromeOsDeviceDiskVolumeReports `json:"diskVolumeReports,omitempty"`
	// DockMacAddress: (Read-only) Built-in MAC address for the docking station
	// that the device connected to. Factory sets Media access control address (MAC
	// address) assigned for use by a dock. It is reserved specifically for MAC
	// pass through device policy. The format is twelve (12) hexadecimal digits
	// without any delimiter (uppercase letters). This is only relevant for some
	// devices.
	DockMacAddress string `json:"dockMacAddress,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// EthernetMacAddress: The device's MAC address on the ethernet network
	// interface.
	EthernetMacAddress string `json:"ethernetMacAddress,omitempty"`
	// EthernetMacAddress0: (Read-only) MAC address used by the Chromebook’s
	// internal ethernet port, and for onboard network (ethernet) interface. The
	// format is twelve (12) hexadecimal digits without any delimiter (uppercase
	// letters). This is only relevant for some devices.
	EthernetMacAddress0 string `json:"ethernetMacAddress0,omitempty"`
	// ExtendedSupportEligible: Output only. Whether or not the device requires the
	// extended support opt in.
	ExtendedSupportEligible bool `json:"extendedSupportEligible,omitempty"`
	// ExtendedSupportEnabled: Output only. Whether extended support policy is
	// enabled on the device.
	ExtendedSupportEnabled bool `json:"extendedSupportEnabled,omitempty"`
	// ExtendedSupportStart: Output only. Date of the device when extended support
	// policy for automatic updates starts.
	ExtendedSupportStart string `json:"extendedSupportStart,omitempty"`
	// FanInfo: Output only. Fan information for the device.
	FanInfo []*FanInfo `json:"fanInfo,omitempty"`
	// FirmwareVersion: The Chrome device's firmware version.
	FirmwareVersion string `json:"firmwareVersion,omitempty"`
	// FirstEnrollmentTime: Date and time for the first time the device was
	// enrolled.
	FirstEnrollmentTime string `json:"firstEnrollmentTime,omitempty"`
	// Kind: The type of resource. For the Chromeosdevices resource, the value is
	// `admin#directory#chromeosdevice`.
	Kind string `json:"kind,omitempty"`
	// LastDeprovisionTimestamp: (Read-only) Date and time for the last deprovision
	// of the device.
	LastDeprovisionTimestamp string `json:"lastDeprovisionTimestamp,omitempty"`
	// LastEnrollmentTime: Date and time the device was last enrolled (Read-only)
	LastEnrollmentTime string `json:"lastEnrollmentTime,omitempty"`
	// LastKnownNetwork: Contains last known network (Read-only)
	LastKnownNetwork []*ChromeOsDeviceLastKnownNetwork `json:"lastKnownNetwork,omitempty"`
	// LastSync: Date and time the device was last synchronized with the policy
	// settings in the G Suite administrator control panel (Read-only)
	LastSync string `json:"lastSync,omitempty"`
	// MacAddress: The device's wireless MAC address. If the device does not have
	// this information, it is not included in the response.
	MacAddress string `json:"macAddress,omitempty"`
	// ManufactureDate: (Read-only) The date the device was manufactured in
	// yyyy-mm-dd format.
	ManufactureDate string `json:"manufactureDate,omitempty"`
	// Meid: The Mobile Equipment Identifier (MEID) or the International Mobile
	// Equipment Identity (IMEI) for the 3G mobile card in a mobile device. A
	// MEID/IMEI is typically used when adding a device to a wireless carrier's
	// post-pay service plan. If the device does not have this information, this
	// property is not included in the response. For more information on how to
	// export a MEID/IMEI list, see the Developer's Guide
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-chrome-devices.html#export_meid).
	Meid string `json:"meid,omitempty"`
	// Model: The device's model information. If the device does not have this
	// information, this property is not included in the response.
	Model string `json:"model,omitempty"`
	// Notes: Notes about this device added by the administrator. This property can
	// be searched (https://support.google.com/chrome/a/answer/1698333) with the
	// list
	// (https://developers.google.com/workspace/admin/directory/v1/reference/chromeosdevices/list)
	// method's `query` parameter. Maximum length is 500 characters. Empty values
	// are allowed.
	Notes string `json:"notes,omitempty"`
	// OrderNumber: The device's order number. Only devices directly purchased from
	// Google have an order number.
	OrderNumber string `json:"orderNumber,omitempty"`
	// OrgUnitId: The unique ID of the organizational unit. orgUnitPath is the
	// human readable version of orgUnitId. While orgUnitPath may change by
	// renaming an organizational unit within the path, orgUnitId is unchangeable
	// for one organizational unit. This property can be updated
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-chrome-devices#move_chrome_devices_to_ou)
	// using the API. For more information about how to create an organizational
	// structure for your device, see the administration help center
	// (https://support.google.com/a/answer/182433).
	OrgUnitId string `json:"orgUnitId,omitempty"`
	// OrgUnitPath: The full parent path with the organizational unit's name
	// associated with the device. Path names are case insensitive. If the parent
	// organizational unit is the top-level organization, it is represented as a
	// forward slash, `/`. This property can be updated
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-chrome-devices#move_chrome_devices_to_ou)
	// using the API. For more information about how to create an organizational
	// structure for your device, see the administration help center
	// (https://support.google.com/a/answer/182433).
	OrgUnitPath string `json:"orgUnitPath,omitempty"`
	// OsUpdateStatus: The status of the OS updates for the device.
	OsUpdateStatus *OsUpdateStatus `json:"osUpdateStatus,omitempty"`
	// OsVersion: The Chrome device's operating system version.
	OsVersion string `json:"osVersion,omitempty"`
	// OsVersionCompliance: Output only. Device policy compliance status of the OS
	// version.
	//
	// Possible values:
	//   "complianceUnspecified" - Compliance status unspecified.
	//   "compliant" - Compliance status compliant.
	//   "pending" - Compliance status pending.
	//   "notCompliant" - Compliance status not compliant.
	OsVersionCompliance string `json:"osVersionCompliance,omitempty"`
	// PlatformVersion: The Chrome device's platform version.
	PlatformVersion string `json:"platformVersion,omitempty"`
	// RecentUsers: A list of recent device users, in descending order, by last
	// login time.
	RecentUsers []*ChromeOsDeviceRecentUsers `json:"recentUsers,omitempty"`
	// ScreenshotFiles: A list of screenshot files to download. Type is always
	// "SCREENSHOT_FILE". (Read-only)
	ScreenshotFiles []*ChromeOsDeviceScreenshotFiles `json:"screenshotFiles,omitempty"`
	// SerialNumber: The Chrome device serial number entered when the device was
	// enabled. This value is the same as the Admin console's *Serial Number* in
	// the *Chrome OS Devices* tab.
	SerialNumber string `json:"serialNumber,omitempty"`
	// Status: The status of the device.
	Status string `json:"status,omitempty"`
	// SupportEndDate: Final date the device will be supported (Read-only)
	SupportEndDate string `json:"supportEndDate,omitempty"`
	// SystemRamFreeReports: Reports of amounts of available RAM memory (Read-only)
	SystemRamFreeReports []*ChromeOsDeviceSystemRamFreeReports `json:"systemRamFreeReports,omitempty"`
	// SystemRamTotal: Total RAM on the device [in bytes] (Read-only)
	SystemRamTotal int64 `json:"systemRamTotal,omitempty,string"`
	// TpmVersionInfo: Trusted Platform Module (TPM) (Read-only)
	TpmVersionInfo *ChromeOsDeviceTpmVersionInfo `json:"tpmVersionInfo,omitempty"`
	// WillAutoRenew: Determines if the device will auto renew its support after
	// the support end date. This is a read-only property.
	WillAutoRenew bool `json:"willAutoRenew,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ActiveTimeRanges") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActiveTimeRanges") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChromeOsDevice: Google Chrome devices run on the Chrome OS (https://support.google.com/chromeos). For more information about common API tasks, see the Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-chrome-devices).

func (ChromeOsDevice) MarshalJSON ¶
func (s ChromeOsDevice) MarshalJSON() ([]byte, error)
type ChromeOsDeviceAction ¶
type ChromeOsDeviceAction struct {
	// Action: Action to be taken on the Chrome OS device.
	Action string `json:"action,omitempty"`
	// DeprovisionReason: Only used when the action is `deprovision`. With the
	// `deprovision` action, this field is required. *Note*: The deprovision reason
	// is audited because it might have implications on licenses for perpetual
	// subscription customers.
	DeprovisionReason string `json:"deprovisionReason,omitempty"`
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

ChromeOsDeviceAction: Data about an update to the status of a Chrome OS device.

func (ChromeOsDeviceAction) MarshalJSON ¶
func (s ChromeOsDeviceAction) MarshalJSON() ([]byte, error)
type ChromeOsDeviceActiveTimeRanges ¶
type ChromeOsDeviceActiveTimeRanges struct {
	// ActiveTime: Duration of usage in milliseconds.
	ActiveTime int64 `json:"activeTime,omitempty"`
	// Date: Date of usage
	Date string `json:"date,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActiveTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActiveTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceActiveTimeRanges) MarshalJSON ¶
func (s ChromeOsDeviceActiveTimeRanges) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfo ¶
added in v0.59.0
type ChromeOsDeviceCpuInfo struct {
	// Architecture: The CPU architecture.
	Architecture string `json:"architecture,omitempty"`
	// LogicalCpus: Information for the Logical CPUs
	LogicalCpus []*ChromeOsDeviceCpuInfoLogicalCpus `json:"logicalCpus,omitempty"`
	// MaxClockSpeedKhz: The max CPU clock speed in kHz.
	MaxClockSpeedKhz int64 `json:"maxClockSpeedKhz,omitempty"`
	// Model: The CPU model name.
	Model string `json:"model,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Architecture") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Architecture") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChromeOsDeviceCpuInfo: CPU specs for a CPU.

func (ChromeOsDeviceCpuInfo) MarshalJSON ¶
added in v0.59.0
func (s ChromeOsDeviceCpuInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfoLogicalCpus ¶
added in v0.59.0
type ChromeOsDeviceCpuInfoLogicalCpus struct {
	// CStates: C-States indicate the power consumption state of the CPU. For more
	// information look at documentation published by the CPU maker.
	CStates []*ChromeOsDeviceCpuInfoLogicalCpusCStates `json:"cStates,omitempty"`
	// CurrentScalingFrequencyKhz: Current frequency the CPU is running at.
	CurrentScalingFrequencyKhz int64 `json:"currentScalingFrequencyKhz,omitempty"`
	// IdleDuration: Idle time since last boot.
	IdleDuration string `json:"idleDuration,omitempty"`
	// MaxScalingFrequencyKhz: Maximum frequency the CPU is allowed to run at, by
	// policy.
	MaxScalingFrequencyKhz int64 `json:"maxScalingFrequencyKhz,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CStates") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CStates") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChromeOsDeviceCpuInfoLogicalCpus: Status of a single logical CPU.

func (ChromeOsDeviceCpuInfoLogicalCpus) MarshalJSON ¶
added in v0.59.0
func (s ChromeOsDeviceCpuInfoLogicalCpus) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuInfoLogicalCpusCStates ¶
added in v0.59.0
type ChromeOsDeviceCpuInfoLogicalCpusCStates struct {
	// DisplayName: Name of the state.
	DisplayName string `json:"displayName,omitempty"`
	// SessionDuration: Time spent in the state since the last reboot.
	SessionDuration string `json:"sessionDuration,omitempty"`
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

ChromeOsDeviceCpuInfoLogicalCpusCStates: Status of a single C-state. C-states are various modes the CPU can transition to in order to use more or less power.

func (ChromeOsDeviceCpuInfoLogicalCpusCStates) MarshalJSON ¶
added in v0.59.0
func (s ChromeOsDeviceCpuInfoLogicalCpusCStates) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuStatusReports ¶
type ChromeOsDeviceCpuStatusReports struct {
	// CpuTemperatureInfo: A list of CPU temperature samples.
	CpuTemperatureInfo           []*ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo `json:"cpuTemperatureInfo,omitempty"`
	CpuUtilizationPercentageInfo []int64                                             `json:"cpuUtilizationPercentageInfo,omitempty"`
	// ReportTime: Date and time the report was received.
	ReportTime string `json:"reportTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CpuTemperatureInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CpuTemperatureInfo") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceCpuStatusReports) MarshalJSON ¶
func (s ChromeOsDeviceCpuStatusReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo ¶
type ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo struct {
	// Label: CPU label
	Label string `json:"label,omitempty"`
	// Temperature: Temperature in Celsius degrees.
	Temperature int64 `json:"temperature,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Label") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Label") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo) MarshalJSON ¶
func (s ChromeOsDeviceCpuStatusReportsCpuTemperatureInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDeviceFiles ¶
type ChromeOsDeviceDeviceFiles struct {
	// CreateTime: Date and time the file was created
	CreateTime string `json:"createTime,omitempty"`
	// DownloadUrl: File download URL
	DownloadUrl string `json:"downloadUrl,omitempty"`
	// Name: File name
	Name string `json:"name,omitempty"`
	// Type: File type
	Type string `json:"type,omitempty"`
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
func (ChromeOsDeviceDeviceFiles) MarshalJSON ¶
func (s ChromeOsDeviceDeviceFiles) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDiskVolumeReports ¶
type ChromeOsDeviceDiskVolumeReports struct {
	// VolumeInfo: Disk volumes
	VolumeInfo []*ChromeOsDeviceDiskVolumeReportsVolumeInfo `json:"volumeInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "VolumeInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "VolumeInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceDiskVolumeReports) MarshalJSON ¶
func (s ChromeOsDeviceDiskVolumeReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceDiskVolumeReportsVolumeInfo ¶
type ChromeOsDeviceDiskVolumeReportsVolumeInfo struct {
	// StorageFree: Free disk space [in bytes]
	StorageFree int64 `json:"storageFree,omitempty,string"`
	// StorageTotal: Total disk space [in bytes]
	StorageTotal int64 `json:"storageTotal,omitempty,string"`
	// VolumeId: Volume id
	VolumeId string `json:"volumeId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "StorageFree") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "StorageFree") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceDiskVolumeReportsVolumeInfo) MarshalJSON ¶
func (s ChromeOsDeviceDiskVolumeReportsVolumeInfo) MarshalJSON() ([]byte, error)
type ChromeOsDeviceLastKnownNetwork ¶
added in v0.29.0
type ChromeOsDeviceLastKnownNetwork struct {
	// IpAddress: The IP address.
	IpAddress string `json:"ipAddress,omitempty"`
	// WanIpAddress: The WAN IP address.
	WanIpAddress string `json:"wanIpAddress,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IpAddress") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IpAddress") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChromeOsDeviceLastKnownNetwork: Information for an ip address.

func (ChromeOsDeviceLastKnownNetwork) MarshalJSON ¶
added in v0.29.0
func (s ChromeOsDeviceLastKnownNetwork) MarshalJSON() ([]byte, error)
type ChromeOsDeviceRecentUsers ¶
type ChromeOsDeviceRecentUsers struct {
	// Email: The user's email address. This is only present if the user type is
	// `USER_TYPE_MANAGED`.
	Email string `json:"email,omitempty"`
	// Type: The type of the user.
	Type string `json:"type,omitempty"`
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

ChromeOsDeviceRecentUsers: A list of recent device users, in descending order, by last login time.

func (ChromeOsDeviceRecentUsers) MarshalJSON ¶
func (s ChromeOsDeviceRecentUsers) MarshalJSON() ([]byte, error)
type ChromeOsDeviceScreenshotFiles ¶
added in v0.42.0
type ChromeOsDeviceScreenshotFiles struct {
	// CreateTime: Date and time the file was created
	CreateTime string `json:"createTime,omitempty"`
	// DownloadUrl: File download URL
	DownloadUrl string `json:"downloadUrl,omitempty"`
	// Name: File name
	Name string `json:"name,omitempty"`
	// Type: File type
	Type string `json:"type,omitempty"`
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
func (ChromeOsDeviceScreenshotFiles) MarshalJSON ¶
added in v0.42.0
func (s ChromeOsDeviceScreenshotFiles) MarshalJSON() ([]byte, error)
type ChromeOsDeviceSystemRamFreeReports ¶
type ChromeOsDeviceSystemRamFreeReports struct {
	// ReportTime: Date and time the report was received.
	ReportTime        string           `json:"reportTime,omitempty"`
	SystemRamFreeInfo googleapi.Int64s `json:"systemRamFreeInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReportTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReportTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDeviceSystemRamFreeReports) MarshalJSON ¶
func (s ChromeOsDeviceSystemRamFreeReports) MarshalJSON() ([]byte, error)
type ChromeOsDeviceTpmVersionInfo ¶
type ChromeOsDeviceTpmVersionInfo struct {
	// Family: TPM family. We use the TPM 2.0 style encoding, e.g.: TPM 1.2: "1.2"
	// -> 312e3200 TPM 2.0: "2.0" -> 322e3000
	Family string `json:"family,omitempty"`
	// FirmwareVersion: TPM firmware version.
	FirmwareVersion string `json:"firmwareVersion,omitempty"`
	// Manufacturer: TPM manufacturer code.
	Manufacturer string `json:"manufacturer,omitempty"`
	// SpecLevel: TPM specification level. See Library Specification for TPM 2.0
	// and Main Specification for TPM 1.2.
	SpecLevel string `json:"specLevel,omitempty"`
	// TpmModel: TPM model number.
	TpmModel string `json:"tpmModel,omitempty"`
	// VendorSpecific: Vendor-specific information such as Vendor ID.
	VendorSpecific string `json:"vendorSpecific,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Family") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Family") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ChromeOsDeviceTpmVersionInfo: Trusted Platform Module (TPM) (Read-only)

func (ChromeOsDeviceTpmVersionInfo) MarshalJSON ¶
func (s ChromeOsDeviceTpmVersionInfo) MarshalJSON() ([]byte, error)
type ChromeOsDevices ¶
type ChromeOsDevices struct {
	// Chromeosdevices: A list of Chrome OS Device objects.
	Chromeosdevices []*ChromeOsDevice `json:"chromeosdevices,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: Token used to access the next page of this result. To access
	// the next page, use this token's value in the `pageToken` query string of
	// this request.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Chromeosdevices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Chromeosdevices") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsDevices) MarshalJSON ¶
func (s ChromeOsDevices) MarshalJSON() ([]byte, error)
type ChromeOsMoveDevicesToOu ¶
type ChromeOsMoveDevicesToOu struct {
	// DeviceIds: Chrome OS devices to be moved to OU
	DeviceIds []string `json:"deviceIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceIds") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ChromeOsMoveDevicesToOu) MarshalJSON ¶
func (s ChromeOsMoveDevicesToOu) MarshalJSON() ([]byte, error)
type ChromeosdevicesActionCall ¶
type ChromeosdevicesActionCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesActionCall) Context ¶
func (c *ChromeosdevicesActionCall) Context(ctx context.Context) *ChromeosdevicesActionCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesActionCall) Do ¶
func (c *ChromeosdevicesActionCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.chromeosdevices.action" call.

func (*ChromeosdevicesActionCall) Fields ¶
func (c *ChromeosdevicesActionCall) Fields(s ...googleapi.Field) *ChromeosdevicesActionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesActionCall) Header ¶
func (c *ChromeosdevicesActionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ChromeosdevicesGetCall ¶
type ChromeosdevicesGetCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesGetCall) Context ¶
func (c *ChromeosdevicesGetCall) Context(ctx context.Context) *ChromeosdevicesGetCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesGetCall) Do ¶
func (c *ChromeosdevicesGetCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)

Do executes the "directory.chromeosdevices.get" call. Any non-2xx status code is an error. Response headers are in either *ChromeOsDevice.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ChromeosdevicesGetCall) Fields ¶
func (c *ChromeosdevicesGetCall) Fields(s ...googleapi.Field) *ChromeosdevicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesGetCall) Header ¶
func (c *ChromeosdevicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ChromeosdevicesGetCall) IfNoneMatch ¶
func (c *ChromeosdevicesGetCall) IfNoneMatch(entityTag string) *ChromeosdevicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ChromeosdevicesGetCall) Projection ¶
func (c *ChromeosdevicesGetCall) Projection(projection string) *ChromeosdevicesGetCall

Projection sets the optional parameter "projection": Determines whether the response contains the full list of properties or only a subset.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId,


serialNumber, status, and user)

"FULL" - Includes all metadata fields

type ChromeosdevicesListCall ¶
type ChromeosdevicesListCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesListCall) Context ¶
func (c *ChromeosdevicesListCall) Context(ctx context.Context) *ChromeosdevicesListCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesListCall) Do ¶
func (c *ChromeosdevicesListCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevices, error)

Do executes the "directory.chromeosdevices.list" call. Any non-2xx status code is an error. Response headers are in either *ChromeOsDevices.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ChromeosdevicesListCall) Fields ¶
func (c *ChromeosdevicesListCall) Fields(s ...googleapi.Field) *ChromeosdevicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesListCall) Header ¶
func (c *ChromeosdevicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ChromeosdevicesListCall) IfNoneMatch ¶
func (c *ChromeosdevicesListCall) IfNoneMatch(entityTag string) *ChromeosdevicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ChromeosdevicesListCall) IncludeChildOrgunits ¶
added in v0.60.0
func (c *ChromeosdevicesListCall) IncludeChildOrgunits(includeChildOrgunits bool) *ChromeosdevicesListCall

IncludeChildOrgunits sets the optional parameter "includeChildOrgunits": Return devices from all child orgunits, as well as the specified org unit. If this is set to true, 'orgUnitPath' must be provided.

func (*ChromeosdevicesListCall) MaxResults ¶
func (c *ChromeosdevicesListCall) MaxResults(maxResults int64) *ChromeosdevicesListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return. Value should not exceed 300.

func (*ChromeosdevicesListCall) OrderBy ¶
func (c *ChromeosdevicesListCall) OrderBy(orderBy string) *ChromeosdevicesListCall

OrderBy sets the optional parameter "orderBy": Device property to use for sorting results.

Possible values:

"annotatedLocation" - Chrome device location as annotated by the


administrator.

"annotatedUser" - Chromebook user as annotated by administrator.
"lastSync" - The date and time the Chrome device was last synchronized


with the policy settings in the Admin console.

"notes" - Chrome device notes as annotated by the administrator.
"serialNumber" - The Chrome device serial number entered when the device


was enabled.

"status" - Chrome device status. For more information, see the <a


[chromeosdevices](https://developers.google.com/workspace/admin/directory/v1/ reference/chromeosdevices.html).

func (*ChromeosdevicesListCall) OrgUnitPath ¶
func (c *ChromeosdevicesListCall) OrgUnitPath(orgUnitPath string) *ChromeosdevicesListCall

OrgUnitPath sets the optional parameter "orgUnitPath": The full path of the organizational unit (minus the leading `/`) or its unique ID.

func (*ChromeosdevicesListCall) PageToken ¶
func (c *ChromeosdevicesListCall) PageToken(pageToken string) *ChromeosdevicesListCall

PageToken sets the optional parameter "pageToken": The `pageToken` query parameter is used to request the next page of query results. The follow-on request's `pageToken` query parameter is the `nextPageToken` from your previous response.

func (*ChromeosdevicesListCall) Pages ¶
func (c *ChromeosdevicesListCall) Pages(ctx context.Context, f func(*ChromeOsDevices) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ChromeosdevicesListCall) Projection ¶
func (c *ChromeosdevicesListCall) Projection(projection string) *ChromeosdevicesListCall

Projection sets the optional parameter "projection": Determines whether the response contains the full list of properties or only a subset.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId,


serialNumber, status, and user)

"FULL" - Includes all metadata fields

func (*ChromeosdevicesListCall) Query ¶
func (c *ChromeosdevicesListCall) Query(query string) *ChromeosdevicesListCall

Query sets the optional parameter "query": Search string in the format given at https://developers.google.com/workspace/admin/directory/v1/list-query-operators

func (*ChromeosdevicesListCall) SortOrder ¶
func (c *ChromeosdevicesListCall) SortOrder(sortOrder string) *ChromeosdevicesListCall

SortOrder sets the optional parameter "sortOrder": Whether to return results in ascending or descending order. Must be used with the `orderBy` parameter.

Possible values:

"ASCENDING" - Ascending order.
"DESCENDING" - Descending order.

type ChromeosdevicesMoveDevicesToOuCall ¶
type ChromeosdevicesMoveDevicesToOuCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesMoveDevicesToOuCall) Context ¶
func (c *ChromeosdevicesMoveDevicesToOuCall) Context(ctx context.Context) *ChromeosdevicesMoveDevicesToOuCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesMoveDevicesToOuCall) Do ¶
func (c *ChromeosdevicesMoveDevicesToOuCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.chromeosdevices.moveDevicesToOu" call.

func (*ChromeosdevicesMoveDevicesToOuCall) Fields ¶
func (c *ChromeosdevicesMoveDevicesToOuCall) Fields(s ...googleapi.Field) *ChromeosdevicesMoveDevicesToOuCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesMoveDevicesToOuCall) Header ¶
func (c *ChromeosdevicesMoveDevicesToOuCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ChromeosdevicesPatchCall ¶
type ChromeosdevicesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesPatchCall) Context ¶
func (c *ChromeosdevicesPatchCall) Context(ctx context.Context) *ChromeosdevicesPatchCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesPatchCall) Do ¶
func (c *ChromeosdevicesPatchCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)

Do executes the "directory.chromeosdevices.patch" call. Any non-2xx status code is an error. Response headers are in either *ChromeOsDevice.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ChromeosdevicesPatchCall) Fields ¶
func (c *ChromeosdevicesPatchCall) Fields(s ...googleapi.Field) *ChromeosdevicesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesPatchCall) Header ¶
func (c *ChromeosdevicesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ChromeosdevicesPatchCall) Projection ¶
func (c *ChromeosdevicesPatchCall) Projection(projection string) *ChromeosdevicesPatchCall

Projection sets the optional parameter "projection": Determines whether the response contains the full list of properties or only a subset.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId,


serialNumber, status, and user)

"FULL" - Includes all metadata fields

type ChromeosdevicesService ¶
type ChromeosdevicesService struct {
	// contains filtered or unexported fields
}
func NewChromeosdevicesService ¶
func NewChromeosdevicesService(s *Service) *ChromeosdevicesService
func (*ChromeosdevicesService) Action ¶
func (r *ChromeosdevicesService) Action(customerId string, resourceId string, chromeosdeviceaction *ChromeOsDeviceAction) *ChromeosdevicesActionCall

Action: Use BatchChangeChromeOsDeviceStatus (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customer.devices.chromeos/batchChangeStatus) instead. Takes an action that affects a Chrome OS Device. This includes deprovisioning, disabling, and re-enabling devices. *Warning:* * Deprovisioning a device will stop device policy syncing and remove device-level printers. After a device is deprovisioned, it must be wiped before it can be re-enrolled. * Lost or stolen devices should use the disable action. * Re-enabling a disabled device will consume a device license. If you do not have sufficient licenses available when completing the re-enable action, you will receive an error. For more information about deprovisioning and disabling devices, visit the help center (https://support.google.com/chrome/a/answer/3523633).

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
resourceId: The unique ID of the device. The `resourceId`s are returned in the response from the chromeosdevices.list (https://developers.google.com/workspace/admin/directory/v1/reference/chromeosdevices/list) method.
func (*ChromeosdevicesService) Get ¶
func (r *ChromeosdevicesService) Get(customerId string, deviceId string) *ChromeosdevicesGetCall

Get: Retrieves a Chrome OS device's properties.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
deviceId: The unique ID of the device. The `deviceId`s are returned in the response from the chromeosdevices.list (https://developers.google.com/workspace/admin/directory/v1/reference/chromeosdevices/list) method.
func (*ChromeosdevicesService) List ¶
func (r *ChromeosdevicesService) List(customerId string) *ChromeosdevicesListCall

List: Retrieves a paginated list of Chrome OS devices within an account.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
func (*ChromeosdevicesService) MoveDevicesToOu ¶
func (r *ChromeosdevicesService) MoveDevicesToOu(customerId string, orgUnitPath string, chromeosmovedevicestoou *ChromeOsMoveDevicesToOu) *ChromeosdevicesMoveDevicesToOuCall

MoveDevicesToOu: Moves or inserts multiple Chrome OS devices to an organizational unit. You can move up to 50 devices at once.

- customerId: Immutable. ID of the Google Workspace account. - orgUnitPath: Full path of the target organizational unit or its ID.

func (*ChromeosdevicesService) Patch ¶
func (r *ChromeosdevicesService) Patch(customerId string, deviceId string, chromeosdevice *ChromeOsDevice) *ChromeosdevicesPatchCall

Patch: Updates a device's updatable properties, such as `annotatedUser`, `annotatedLocation`, `notes`, `orgUnitPath`, or `annotatedAssetId`. This method supports patch semantics (https://developers.google.com/workspace/admin/directory/v1/guides/performance#patch).

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
deviceId: The unique ID of the device. The `deviceId`s are returned in the response from the chromeosdevices.list (https://developers.google.com/workspace/admin/v1/reference/chromeosdevices/list) method.
func (*ChromeosdevicesService) Update ¶
func (r *ChromeosdevicesService) Update(customerId string, deviceId string, chromeosdevice *ChromeOsDevice) *ChromeosdevicesUpdateCall

Update: Updates a device's updatable properties, such as `annotatedUser`, `annotatedLocation`, `notes`, `orgUnitPath`, or `annotatedAssetId`.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
deviceId: The unique ID of the device. The `deviceId`s are returned in the response from the chromeosdevices.list (https://developers.google.com/workspace/admin/v1/reference/chromeosdevices/list) method.
type ChromeosdevicesUpdateCall ¶
type ChromeosdevicesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ChromeosdevicesUpdateCall) Context ¶
func (c *ChromeosdevicesUpdateCall) Context(ctx context.Context) *ChromeosdevicesUpdateCall

Context sets the context to be used in this call's Do method.

func (*ChromeosdevicesUpdateCall) Do ¶
func (c *ChromeosdevicesUpdateCall) Do(opts ...googleapi.CallOption) (*ChromeOsDevice, error)

Do executes the "directory.chromeosdevices.update" call. Any non-2xx status code is an error. Response headers are in either *ChromeOsDevice.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ChromeosdevicesUpdateCall) Fields ¶
func (c *ChromeosdevicesUpdateCall) Fields(s ...googleapi.Field) *ChromeosdevicesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ChromeosdevicesUpdateCall) Header ¶
func (c *ChromeosdevicesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ChromeosdevicesUpdateCall) Projection ¶
func (c *ChromeosdevicesUpdateCall) Projection(projection string) *ChromeosdevicesUpdateCall

Projection sets the optional parameter "projection": Determines whether the response contains the full list of properties or only a subset.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId,


serialNumber, status, and user)

"FULL" - Includes all metadata fields

type CountChromeOsDevicesResponse ¶
added in v0.267.0
type CountChromeOsDevicesResponse struct {
	// Count: The total number of devices matching the request.
	Count int64 `json:"count,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

CountChromeOsDevicesResponse: A response for counting ChromeOS devices.

func (CountChromeOsDevicesResponse) MarshalJSON ¶
added in v0.267.0
func (s CountChromeOsDevicesResponse) MarshalJSON() ([]byte, error)
type CreatePrintServerRequest ¶
added in v0.98.0
type CreatePrintServerRequest struct {
	// Parent: Required. The unique ID
	// (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers)
	// of the customer's Google Workspace account. Format: `customers/{id}`
	Parent string `json:"parent,omitempty"`
	// PrintServer: Required. A print server to create. If you want to place the
	// print server under a specific organizational unit (OU), then populate the
	// `org_unit_id`. Otherwise the print server is created under the root OU. The
	// `org_unit_id` can be retrieved using the Directory API
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-org-units).
	PrintServer *PrintServer `json:"printServer,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Parent") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Parent") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreatePrintServerRequest: Request for adding a new print server.

func (CreatePrintServerRequest) MarshalJSON ¶
added in v0.98.0
func (s CreatePrintServerRequest) MarshalJSON() ([]byte, error)
type CreatePrinterRequest ¶
added in v0.42.0
type CreatePrinterRequest struct {
	// Parent: Required. The name of the customer. Format: customers/{customer_id}
	Parent string `json:"parent,omitempty"`
	// Printer: Required. A printer to create. If you want to place the printer
	// under particular OU then populate printer.org_unit_id filed. Otherwise the
	// printer will be placed under root OU.
	Printer *Printer `json:"printer,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Parent") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Parent") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreatePrinterRequest: Request for adding a new printer.

func (CreatePrinterRequest) MarshalJSON ¶
added in v0.42.0
func (s CreatePrinterRequest) MarshalJSON() ([]byte, error)
type Customer ¶
type Customer struct {
	// AlternateEmail: The customer's secondary contact email address. This email
	// address cannot be on the same domain as the `customerDomain`
	AlternateEmail string `json:"alternateEmail,omitempty"`
	// CustomerCreationTime: The customer's creation time (Readonly)
	CustomerCreationTime string `json:"customerCreationTime,omitempty"`
	// CustomerDomain: The customer's primary domain name string. Do not include
	// the `www` prefix when creating a new customer.
	CustomerDomain string `json:"customerDomain,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Id: The unique ID for the customer's Google Workspace account. (Readonly)
	Id string `json:"id,omitempty"`
	// Kind: Identifies the resource as a customer. Value:
	// `admin#directory#customer`
	Kind string `json:"kind,omitempty"`
	// Language: The customer's ISO 639-2 language code. See the Language Codes
	// (https://developers.google.com/workspace/admin/directory/v1/languages) page
	// for the list of supported codes. Valid language codes outside the supported
	// set will be accepted by the API but may lead to unexpected behavior. The
	// default value is `en`.
	Language string `json:"language,omitempty"`
	// PhoneNumber: The customer's contact phone number in E.164
	// (https://en.wikipedia.org/wiki/E.164) format.
	PhoneNumber string `json:"phoneNumber,omitempty"`
	// PostalAddress: The customer's postal address information.
	PostalAddress *CustomerPostalAddress `json:"postalAddress,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AlternateEmail") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AlternateEmail") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (Customer) MarshalJSON ¶
func (s Customer) MarshalJSON() ([]byte, error)
type CustomerDevicesChromeosBatchChangeStatusCall ¶
added in v0.155.0
type CustomerDevicesChromeosBatchChangeStatusCall struct {
	// contains filtered or unexported fields
}
func (*CustomerDevicesChromeosBatchChangeStatusCall) Context ¶
added in v0.155.0
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Context(ctx context.Context) *CustomerDevicesChromeosBatchChangeStatusCall

Context sets the context to be used in this call's Do method.

func (*CustomerDevicesChromeosBatchChangeStatusCall) Do ¶
added in v0.155.0
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Do(opts ...googleapi.CallOption) (*BatchChangeChromeOsDeviceStatusResponse, error)

Do executes the "admin.customer.devices.chromeos.batchChangeStatus" call. Any non-2xx status code is an error. Response headers are in either *BatchChangeChromeOsDeviceStatusResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomerDevicesChromeosBatchChangeStatusCall) Fields ¶
added in v0.155.0
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosBatchChangeStatusCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomerDevicesChromeosBatchChangeStatusCall) Header ¶
added in v0.155.0
func (c *CustomerDevicesChromeosBatchChangeStatusCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomerDevicesChromeosCommandsGetCall ¶
added in v0.34.0
type CustomerDevicesChromeosCommandsGetCall struct {
	// contains filtered or unexported fields
}
func (*CustomerDevicesChromeosCommandsGetCall) Context ¶
added in v0.34.0
func (c *CustomerDevicesChromeosCommandsGetCall) Context(ctx context.Context) *CustomerDevicesChromeosCommandsGetCall

Context sets the context to be used in this call's Do method.

func (*CustomerDevicesChromeosCommandsGetCall) Do ¶
added in v0.34.0
func (c *CustomerDevicesChromeosCommandsGetCall) Do(opts ...googleapi.CallOption) (*DirectoryChromeosdevicesCommand, error)

Do executes the "admin.customer.devices.chromeos.commands.get" call. Any non-2xx status code is an error. Response headers are in either *DirectoryChromeosdevicesCommand.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomerDevicesChromeosCommandsGetCall) Fields ¶
added in v0.34.0
func (c *CustomerDevicesChromeosCommandsGetCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosCommandsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomerDevicesChromeosCommandsGetCall) Header ¶
added in v0.34.0
func (c *CustomerDevicesChromeosCommandsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomerDevicesChromeosCommandsGetCall) IfNoneMatch ¶
added in v0.34.0
func (c *CustomerDevicesChromeosCommandsGetCall) IfNoneMatch(entityTag string) *CustomerDevicesChromeosCommandsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type CustomerDevicesChromeosCommandsService ¶
added in v0.34.0
type CustomerDevicesChromeosCommandsService struct {
	// contains filtered or unexported fields
}
func NewCustomerDevicesChromeosCommandsService ¶
added in v0.34.0
func NewCustomerDevicesChromeosCommandsService(s *Service) *CustomerDevicesChromeosCommandsService
func (*CustomerDevicesChromeosCommandsService) Get ¶
added in v0.34.0
func (r *CustomerDevicesChromeosCommandsService) Get(customerId string, deviceId string, commandId int64) *CustomerDevicesChromeosCommandsGetCall

Get: Gets command data a specific command issued to the device.

- commandId: Immutable. ID of Chrome OS Device Command. - customerId: Immutable. ID of the Google Workspace account. - deviceId: Immutable. ID of Chrome OS Device.

type CustomerDevicesChromeosCountChromeOsDevicesCall ¶
added in v0.267.0
type CustomerDevicesChromeosCountChromeOsDevicesCall struct {
	// contains filtered or unexported fields
}
func (*CustomerDevicesChromeosCountChromeOsDevicesCall) Context ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Context(ctx context.Context) *CustomerDevicesChromeosCountChromeOsDevicesCall

Context sets the context to be used in this call's Do method.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) Do ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Do(opts ...googleapi.CallOption) (*CountChromeOsDevicesResponse, error)

Do executes the "admin.customer.devices.chromeos.countChromeOsDevices" call. Any non-2xx status code is an error. Response headers are in either *CountChromeOsDevicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) Fields ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosCountChromeOsDevicesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) Filter ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Filter(filter string) *CustomerDevicesChromeosCountChromeOsDevicesCall

Filter sets the optional parameter "filter": Search string in the format given at https://developers.google.com/workspace/admin/directory/v1/list-query-operators

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) Header ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) IfNoneMatch ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) IfNoneMatch(entityTag string) *CustomerDevicesChromeosCountChromeOsDevicesCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) IncludeChildOrgunits ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) IncludeChildOrgunits(includeChildOrgunits bool) *CustomerDevicesChromeosCountChromeOsDevicesCall

IncludeChildOrgunits sets the optional parameter "includeChildOrgunits": Return devices from all child orgunits, as well as the specified org unit. If this is set to true, 'orgUnitPath' must be provided.

func (*CustomerDevicesChromeosCountChromeOsDevicesCall) OrgUnitPath ¶
added in v0.267.0
func (c *CustomerDevicesChromeosCountChromeOsDevicesCall) OrgUnitPath(orgUnitPath string) *CustomerDevicesChromeosCountChromeOsDevicesCall

OrgUnitPath sets the optional parameter "orgUnitPath": The full path of the organizational unit (minus the leading `/`) or its unique ID.

type CustomerDevicesChromeosIssueCommandCall ¶
added in v0.34.0
type CustomerDevicesChromeosIssueCommandCall struct {
	// contains filtered or unexported fields
}
func (*CustomerDevicesChromeosIssueCommandCall) Context ¶
added in v0.34.0
func (c *CustomerDevicesChromeosIssueCommandCall) Context(ctx context.Context) *CustomerDevicesChromeosIssueCommandCall

Context sets the context to be used in this call's Do method.

func (*CustomerDevicesChromeosIssueCommandCall) Do ¶
added in v0.34.0
func (c *CustomerDevicesChromeosIssueCommandCall) Do(opts ...googleapi.CallOption) (*DirectoryChromeosdevicesIssueCommandResponse, error)

Do executes the "admin.customer.devices.chromeos.issueCommand" call. Any non-2xx status code is an error. Response headers are in either *DirectoryChromeosdevicesIssueCommandResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomerDevicesChromeosIssueCommandCall) Fields ¶
added in v0.34.0
func (c *CustomerDevicesChromeosIssueCommandCall) Fields(s ...googleapi.Field) *CustomerDevicesChromeosIssueCommandCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomerDevicesChromeosIssueCommandCall) Header ¶
added in v0.34.0
func (c *CustomerDevicesChromeosIssueCommandCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomerDevicesChromeosService ¶
added in v0.34.0
type CustomerDevicesChromeosService struct {
	Commands *CustomerDevicesChromeosCommandsService
	// contains filtered or unexported fields
}
func NewCustomerDevicesChromeosService ¶
added in v0.34.0
func NewCustomerDevicesChromeosService(s *Service) *CustomerDevicesChromeosService
func (*CustomerDevicesChromeosService) BatchChangeStatus ¶
added in v0.155.0
func (r *CustomerDevicesChromeosService) BatchChangeStatus(customerId string, batchchangechromeosdevicestatusrequest *BatchChangeChromeOsDeviceStatusRequest) *CustomerDevicesChromeosBatchChangeStatusCall

BatchChangeStatus: Changes the status of a batch of ChromeOS devices. For more information about changing a ChromeOS device state Repair, repurpose, or retire ChromeOS devices (https://support.google.com/chrome/a/answer/3523633).

- customerId: Immutable ID of the Google Workspace account.

func (*CustomerDevicesChromeosService) CountChromeOsDevices ¶
added in v0.267.0
func (r *CustomerDevicesChromeosService) CountChromeOsDevices(customerId string) *CustomerDevicesChromeosCountChromeOsDevicesCall

CountChromeOsDevices: Counts ChromeOS devices matching the request.

- customerId: Immutable ID of the Google Workspace account.

func (*CustomerDevicesChromeosService) IssueCommand ¶
added in v0.34.0
func (r *CustomerDevicesChromeosService) IssueCommand(customerId string, deviceId string, directorychromeosdevicesissuecommandrequest *DirectoryChromeosdevicesIssueCommandRequest) *CustomerDevicesChromeosIssueCommandCall

IssueCommand: Issues a command for the device to execute.

- customerId: Immutable. ID of the Google Workspace account. - deviceId: Immutable. ID of Chrome OS Device.

type CustomerDevicesService ¶
added in v0.34.0
type CustomerDevicesService struct {
	Chromeos *CustomerDevicesChromeosService
	// contains filtered or unexported fields
}
func NewCustomerDevicesService ¶
added in v0.34.0
func NewCustomerDevicesService(s *Service) *CustomerDevicesService
type CustomerPostalAddress ¶
type CustomerPostalAddress struct {
	// AddressLine1: A customer's physical address. The address can be composed of
	// one to three lines.
	AddressLine1 string `json:"addressLine1,omitempty"`
	// AddressLine2: Address line 2 of the address.
	AddressLine2 string `json:"addressLine2,omitempty"`
	// AddressLine3: Address line 3 of the address.
	AddressLine3 string `json:"addressLine3,omitempty"`
	// ContactName: The customer contact's name.
	ContactName string `json:"contactName,omitempty"`
	// CountryCode: This is a required property. For `countryCode` information see
	// the ISO 3166 country code elements
	// (https://www.iso.org/iso/country_codes.htm).
	CountryCode string `json:"countryCode,omitempty"`
	// Locality: Name of the locality. An example of a locality value is the city
	// of `San Francisco`.
	Locality string `json:"locality,omitempty"`
	// OrganizationName: The company or company division name.
	OrganizationName string `json:"organizationName,omitempty"`
	// PostalCode: The postal code. A postalCode example is a postal zip code such
	// as `10009`. This is in accordance with - http:
	// //portablecontacts.net/draft-spec.html#address_element.
	PostalCode string `json:"postalCode,omitempty"`
	// Region: Name of the region. An example of a region value is `NY` for the
	// state of New York.
	Region string `json:"region,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AddressLine1") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AddressLine1") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (CustomerPostalAddress) MarshalJSON ¶
func (s CustomerPostalAddress) MarshalJSON() ([]byte, error)
type CustomerService ¶
added in v0.34.0
type CustomerService struct {
	Devices *CustomerDevicesService
	// contains filtered or unexported fields
}
func NewCustomerService ¶
added in v0.34.0
func NewCustomerService(s *Service) *CustomerService
type CustomersChromePrintServersBatchCreatePrintServersCall ¶
added in v0.98.0
type CustomersChromePrintServersBatchCreatePrintServersCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersBatchCreatePrintServersCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Context(ctx context.Context) *CustomersChromePrintServersBatchCreatePrintServersCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersBatchCreatePrintServersCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Do(opts ...googleapi.CallOption) (*BatchCreatePrintServersResponse, error)

Do executes the "admin.customers.chrome.printServers.batchCreatePrintServers" call. Any non-2xx status code is an error. Response headers are in either *BatchCreatePrintServersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersBatchCreatePrintServersCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersBatchCreatePrintServersCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersBatchCreatePrintServersCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchCreatePrintServersCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintServersBatchDeletePrintServersCall ¶
added in v0.98.0
type CustomersChromePrintServersBatchDeletePrintServersCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersBatchDeletePrintServersCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Context(ctx context.Context) *CustomersChromePrintServersBatchDeletePrintServersCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersBatchDeletePrintServersCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Do(opts ...googleapi.CallOption) (*BatchDeletePrintServersResponse, error)

Do executes the "admin.customers.chrome.printServers.batchDeletePrintServers" call. Any non-2xx status code is an error. Response headers are in either *BatchDeletePrintServersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersBatchDeletePrintServersCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersBatchDeletePrintServersCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersBatchDeletePrintServersCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersBatchDeletePrintServersCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintServersCreateCall ¶
added in v0.98.0
type CustomersChromePrintServersCreateCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersCreateCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersCreateCall) Context(ctx context.Context) *CustomersChromePrintServersCreateCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersCreateCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersCreateCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)

Do executes the "admin.customers.chrome.printServers.create" call. Any non-2xx status code is an error. Response headers are in either *PrintServer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersCreateCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersCreateCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersCreateCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintServersDeleteCall ¶
added in v0.98.0
type CustomersChromePrintServersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersDeleteCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersDeleteCall) Context(ctx context.Context) *CustomersChromePrintServersDeleteCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersDeleteCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "admin.customers.chrome.printServers.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersDeleteCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersDeleteCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersDeleteCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintServersGetCall ¶
added in v0.98.0
type CustomersChromePrintServersGetCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersGetCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersGetCall) Context(ctx context.Context) *CustomersChromePrintServersGetCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersGetCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersGetCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)

Do executes the "admin.customers.chrome.printServers.get" call. Any non-2xx status code is an error. Response headers are in either *PrintServer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersGetCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersGetCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersGetCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintServersGetCall) IfNoneMatch ¶
added in v0.98.0
func (c *CustomersChromePrintServersGetCall) IfNoneMatch(entityTag string) *CustomersChromePrintServersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type CustomersChromePrintServersListCall ¶
added in v0.98.0
type CustomersChromePrintServersListCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersListCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Context(ctx context.Context) *CustomersChromePrintServersListCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersListCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Do(opts ...googleapi.CallOption) (*ListPrintServersResponse, error)

Do executes the "admin.customers.chrome.printServers.list" call. Any non-2xx status code is an error. Response headers are in either *ListPrintServersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersListCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersListCall) Filter ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Filter(filter string) *CustomersChromePrintServersListCall

Filter sets the optional parameter "filter": Search query in Common Expression Language syntax (https://github.com/google/cel-spec). Supported filters are `display_name`, `description`, and `uri`. Example: `printServer.displayName=='marketing-queue'`.

func (*CustomersChromePrintServersListCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintServersListCall) IfNoneMatch ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) IfNoneMatch(entityTag string) *CustomersChromePrintServersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*CustomersChromePrintServersListCall) OrderBy ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) OrderBy(orderBy string) *CustomersChromePrintServersListCall

OrderBy sets the optional parameter "orderBy": Sort order for results. Supported values are `display_name`, `description`, or `create_time`. Default order is ascending, but descending order can be returned by appending "desc" to the `order_by` field. For instance, `orderBy=='description desc'` returns the print servers sorted by description in descending order.

func (*CustomersChromePrintServersListCall) OrgUnitId ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) OrgUnitId(orgUnitId string) *CustomersChromePrintServersListCall

OrgUnitId sets the optional parameter "orgUnitId": If `org_unit_id` is present in the request, only print servers owned or inherited by the organizational unit (OU) are returned. If the `PrintServer` resource's `org_unit_id` matches the one in the request, the OU owns the server. If `org_unit_id` is not specified in the request, all print servers are returned or filtered against.

func (*CustomersChromePrintServersListCall) PageSize ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) PageSize(pageSize int64) *CustomersChromePrintServersListCall

PageSize sets the optional parameter "pageSize": The maximum number of objects to return (default `100`, max `100`). The service might return fewer than this value.

func (*CustomersChromePrintServersListCall) PageToken ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) PageToken(pageToken string) *CustomersChromePrintServersListCall

PageToken sets the optional parameter "pageToken": A generated token to paginate results (the `next_page_token` from a previous call).

func (*CustomersChromePrintServersListCall) Pages ¶
added in v0.98.0
func (c *CustomersChromePrintServersListCall) Pages(ctx context.Context, f func(*ListPrintServersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomersChromePrintServersPatchCall ¶
added in v0.98.0
type CustomersChromePrintServersPatchCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintServersPatchCall) Context ¶
added in v0.98.0
func (c *CustomersChromePrintServersPatchCall) Context(ctx context.Context) *CustomersChromePrintServersPatchCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintServersPatchCall) Do ¶
added in v0.98.0
func (c *CustomersChromePrintServersPatchCall) Do(opts ...googleapi.CallOption) (*PrintServer, error)

Do executes the "admin.customers.chrome.printServers.patch" call. Any non-2xx status code is an error. Response headers are in either *PrintServer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintServersPatchCall) Fields ¶
added in v0.98.0
func (c *CustomersChromePrintServersPatchCall) Fields(s ...googleapi.Field) *CustomersChromePrintServersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintServersPatchCall) Header ¶
added in v0.98.0
func (c *CustomersChromePrintServersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintServersPatchCall) UpdateMask ¶
added in v0.98.0
func (c *CustomersChromePrintServersPatchCall) UpdateMask(updateMask string) *CustomersChromePrintServersPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. Some fields are read-only and cannot be updated. Values for unspecified fields are patched.

type CustomersChromePrintServersService ¶
added in v0.98.0
type CustomersChromePrintServersService struct {
	// contains filtered or unexported fields
}
func NewCustomersChromePrintServersService ¶
added in v0.98.0
func NewCustomersChromePrintServersService(s *Service) *CustomersChromePrintServersService
func (*CustomersChromePrintServersService) BatchCreatePrintServers ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) BatchCreatePrintServers(parent string, batchcreateprintserversrequest *BatchCreatePrintServersRequest) *CustomersChromePrintServersBatchCreatePrintServersCall

BatchCreatePrintServers: Creates multiple print servers.

parent: The unique ID (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers) of the customer's Google Workspace account. Format: `customers/{id}`.
func (*CustomersChromePrintServersService) BatchDeletePrintServers ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) BatchDeletePrintServers(parent string, batchdeleteprintserversrequest *BatchDeletePrintServersRequest) *CustomersChromePrintServersBatchDeletePrintServersCall

BatchDeletePrintServers: Deletes multiple print servers.

parent: The unique ID (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers) of the customer's Google Workspace account. Format: `customers/{customer.id}`.
func (*CustomersChromePrintServersService) Create ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) Create(parent string, printserver *PrintServer) *CustomersChromePrintServersCreateCall

Create: Creates a print server.

parent: The unique ID (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers) of the customer's Google Workspace account. Format: `customers/{id}`.
func (*CustomersChromePrintServersService) Delete ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) Delete(name string) *CustomersChromePrintServersDeleteCall

Delete: Deletes a print server.

name: The name of the print server to be deleted. Format: `customers/{customer.id}/chrome/printServers/{print_server.id}`.
func (*CustomersChromePrintServersService) Get ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) Get(name string) *CustomersChromePrintServersGetCall

Get: Returns a print server's configuration.

name: The unique ID (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers) of the customer's Google Workspace account. Format: `customers/{id}`.
func (*CustomersChromePrintServersService) List ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) List(parent string) *CustomersChromePrintServersListCall

List: Lists print server configurations.

parent: The unique ID (https://developers.google.com/workspace/admin/directory/reference/rest/v1/customers) of the customer's Google Workspace account. Format: `customers/{id}`.
func (*CustomersChromePrintServersService) Patch ¶
added in v0.98.0
func (r *CustomersChromePrintServersService) Patch(name string, printserver *PrintServer) *CustomersChromePrintServersPatchCall

Patch: Updates a print server's configuration.

name: Identifier. Resource name of the print server. Leave empty when creating. Format: `customers/{customer.id}/printServers/{print_server.id}`.
type CustomersChromePrintersBatchCreatePrintersCall ¶
added in v0.42.0
type CustomersChromePrintersBatchCreatePrintersCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersBatchCreatePrintersCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchCreatePrintersCall) Context(ctx context.Context) *CustomersChromePrintersBatchCreatePrintersCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersBatchCreatePrintersCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchCreatePrintersCall) Do(opts ...googleapi.CallOption) (*BatchCreatePrintersResponse, error)

Do executes the "admin.customers.chrome.printers.batchCreatePrinters" call. Any non-2xx status code is an error. Response headers are in either *BatchCreatePrintersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersBatchCreatePrintersCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchCreatePrintersCall) Fields(s ...googleapi.Field) *CustomersChromePrintersBatchCreatePrintersCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersBatchCreatePrintersCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchCreatePrintersCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintersBatchDeletePrintersCall ¶
added in v0.42.0
type CustomersChromePrintersBatchDeletePrintersCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersBatchDeletePrintersCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchDeletePrintersCall) Context(ctx context.Context) *CustomersChromePrintersBatchDeletePrintersCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersBatchDeletePrintersCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchDeletePrintersCall) Do(opts ...googleapi.CallOption) (*BatchDeletePrintersResponse, error)

Do executes the "admin.customers.chrome.printers.batchDeletePrinters" call. Any non-2xx status code is an error. Response headers are in either *BatchDeletePrintersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersBatchDeletePrintersCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchDeletePrintersCall) Fields(s ...googleapi.Field) *CustomersChromePrintersBatchDeletePrintersCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersBatchDeletePrintersCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersBatchDeletePrintersCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintersCreateCall ¶
added in v0.42.0
type CustomersChromePrintersCreateCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersCreateCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersCreateCall) Context(ctx context.Context) *CustomersChromePrintersCreateCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersCreateCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersCreateCall) Do(opts ...googleapi.CallOption) (*Printer, error)

Do executes the "admin.customers.chrome.printers.create" call. Any non-2xx status code is an error. Response headers are in either *Printer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersCreateCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersCreateCall) Fields(s ...googleapi.Field) *CustomersChromePrintersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersCreateCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintersDeleteCall ¶
added in v0.42.0
type CustomersChromePrintersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersDeleteCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersDeleteCall) Context(ctx context.Context) *CustomersChromePrintersDeleteCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersDeleteCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "admin.customers.chrome.printers.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersDeleteCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersDeleteCall) Fields(s ...googleapi.Field) *CustomersChromePrintersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersDeleteCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersChromePrintersGetCall ¶
added in v0.42.0
type CustomersChromePrintersGetCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersGetCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersGetCall) Context(ctx context.Context) *CustomersChromePrintersGetCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersGetCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersGetCall) Do(opts ...googleapi.CallOption) (*Printer, error)

Do executes the "admin.customers.chrome.printers.get" call. Any non-2xx status code is an error. Response headers are in either *Printer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersGetCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersGetCall) Fields(s ...googleapi.Field) *CustomersChromePrintersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersGetCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintersGetCall) IfNoneMatch ¶
added in v0.42.0
func (c *CustomersChromePrintersGetCall) IfNoneMatch(entityTag string) *CustomersChromePrintersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type CustomersChromePrintersListCall ¶
added in v0.42.0
type CustomersChromePrintersListCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersListCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Context(ctx context.Context) *CustomersChromePrintersListCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersListCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Do(opts ...googleapi.CallOption) (*ListPrintersResponse, error)

Do executes the "admin.customers.chrome.printers.list" call. Any non-2xx status code is an error. Response headers are in either *ListPrintersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersListCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Fields(s ...googleapi.Field) *CustomersChromePrintersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersListCall) Filter ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Filter(filter string) *CustomersChromePrintersListCall

Filter sets the optional parameter "filter": Search query. Search syntax is shared between this api and Admin Console printers pages.

func (*CustomersChromePrintersListCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintersListCall) IfNoneMatch ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) IfNoneMatch(entityTag string) *CustomersChromePrintersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*CustomersChromePrintersListCall) OrderBy ¶
added in v0.69.0
func (c *CustomersChromePrintersListCall) OrderBy(orderBy string) *CustomersChromePrintersListCall

OrderBy sets the optional parameter "orderBy": The order to sort results by. Must be one of display_name, description, make_and_model, or create_time. Default order is ascending, but descending order can be returned by appending "desc" to the order_by field. For instance, "description desc" will return the printers sorted by description in descending order.

func (*CustomersChromePrintersListCall) OrgUnitId ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) OrgUnitId(orgUnitId string) *CustomersChromePrintersListCall

OrgUnitId sets the optional parameter "orgUnitId": Organization Unit that we want to list the printers for. When org_unit is not present in the request then all printers of the customer are returned (or filtered). When org_unit is present in the request then only printers available to this OU will be returned (owned or inherited). You may see if printer is owned or inherited for this OU by looking at Printer.org_unit_id.

func (*CustomersChromePrintersListCall) PageSize ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) PageSize(pageSize int64) *CustomersChromePrintersListCall

PageSize sets the optional parameter "pageSize": The maximum number of objects to return. The service may return fewer than this value.

func (*CustomersChromePrintersListCall) PageToken ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) PageToken(pageToken string) *CustomersChromePrintersListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous call.

func (*CustomersChromePrintersListCall) Pages ¶
added in v0.42.0
func (c *CustomersChromePrintersListCall) Pages(ctx context.Context, f func(*ListPrintersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomersChromePrintersListPrinterModelsCall ¶
added in v0.42.0
type CustomersChromePrintersListPrinterModelsCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersListPrinterModelsCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Context(ctx context.Context) *CustomersChromePrintersListPrinterModelsCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersListPrinterModelsCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Do(opts ...googleapi.CallOption) (*ListPrinterModelsResponse, error)

Do executes the "admin.customers.chrome.printers.listPrinterModels" call. Any non-2xx status code is an error. Response headers are in either *ListPrinterModelsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersListPrinterModelsCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Fields(s ...googleapi.Field) *CustomersChromePrintersListPrinterModelsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersListPrinterModelsCall) Filter ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Filter(filter string) *CustomersChromePrintersListPrinterModelsCall

Filter sets the optional parameter "filter": Filer to list only models by a given manufacturer in format: "manufacturer:Brother". Search syntax is shared between this api and Admin Console printers pages.

func (*CustomersChromePrintersListPrinterModelsCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintersListPrinterModelsCall) IfNoneMatch ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) IfNoneMatch(entityTag string) *CustomersChromePrintersListPrinterModelsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*CustomersChromePrintersListPrinterModelsCall) PageSize ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) PageSize(pageSize int64) *CustomersChromePrintersListPrinterModelsCall

PageSize sets the optional parameter "pageSize": The maximum number of objects to return. The service may return fewer than this value.

func (*CustomersChromePrintersListPrinterModelsCall) PageToken ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) PageToken(pageToken string) *CustomersChromePrintersListPrinterModelsCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous call.

func (*CustomersChromePrintersListPrinterModelsCall) Pages ¶
added in v0.42.0
func (c *CustomersChromePrintersListPrinterModelsCall) Pages(ctx context.Context, f func(*ListPrinterModelsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomersChromePrintersPatchCall ¶
added in v0.42.0
type CustomersChromePrintersPatchCall struct {
	// contains filtered or unexported fields
}
func (*CustomersChromePrintersPatchCall) ClearMask ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) ClearMask(clearMask string) *CustomersChromePrintersPatchCall

ClearMask sets the optional parameter "clearMask": The list of fields to be cleared. Note, some of the fields are read only and cannot be updated. Values for not specified fields will be patched.

func (*CustomersChromePrintersPatchCall) Context ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) Context(ctx context.Context) *CustomersChromePrintersPatchCall

Context sets the context to be used in this call's Do method.

func (*CustomersChromePrintersPatchCall) Do ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) Do(opts ...googleapi.CallOption) (*Printer, error)

Do executes the "admin.customers.chrome.printers.patch" call. Any non-2xx status code is an error. Response headers are in either *Printer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersChromePrintersPatchCall) Fields ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) Fields(s ...googleapi.Field) *CustomersChromePrintersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersChromePrintersPatchCall) Header ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersChromePrintersPatchCall) UpdateMask ¶
added in v0.42.0
func (c *CustomersChromePrintersPatchCall) UpdateMask(updateMask string) *CustomersChromePrintersPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated. Note, some of the fields are read only and cannot be updated. Values for not specified fields will be patched.

type CustomersChromePrintersService ¶
added in v0.42.0
type CustomersChromePrintersService struct {
	// contains filtered or unexported fields
}
func NewCustomersChromePrintersService ¶
added in v0.42.0
func NewCustomersChromePrintersService(s *Service) *CustomersChromePrintersService
func (*CustomersChromePrintersService) BatchCreatePrinters ¶
added in v0.42.0
func (r *CustomersChromePrintersService) BatchCreatePrinters(parent string, batchcreateprintersrequest *BatchCreatePrintersRequest) *CustomersChromePrintersBatchCreatePrintersCall

BatchCreatePrinters: Creates printers under given Organization Unit.

- parent: The name of the customer. Format: customers/{customer_id}.

func (*CustomersChromePrintersService) BatchDeletePrinters ¶
added in v0.42.0
func (r *CustomersChromePrintersService) BatchDeletePrinters(parent string, batchdeleteprintersrequest *BatchDeletePrintersRequest) *CustomersChromePrintersBatchDeletePrintersCall

BatchDeletePrinters: Deletes printers in batch.

- parent: The name of the customer. Format: customers/{customer_id}.

func (*CustomersChromePrintersService) Create ¶
added in v0.42.0
func (r *CustomersChromePrintersService) Create(parent string, printer *Printer) *CustomersChromePrintersCreateCall

Create: Creates a printer under given Organization Unit.

- parent: The name of the customer. Format: customers/{customer_id}.

func (*CustomersChromePrintersService) Delete ¶
added in v0.42.0
func (r *CustomersChromePrintersService) Delete(name string) *CustomersChromePrintersDeleteCall

Delete: Deletes a `Printer`.

name: The name of the printer to be updated. Format: customers/{customer_id}/chrome/printers/{printer_id}.
func (*CustomersChromePrintersService) Get ¶
added in v0.42.0
func (r *CustomersChromePrintersService) Get(name string) *CustomersChromePrintersGetCall

Get: Returns a `Printer` resource (printer's config).

name: The name of the printer to retrieve. Format: customers/{customer_id}/chrome/printers/{printer_id}.
func (*CustomersChromePrintersService) List ¶
added in v0.42.0
func (r *CustomersChromePrintersService) List(parent string) *CustomersChromePrintersListCall

List: List printers configs.

parent: The name of the customer who owns this collection of printers. Format: customers/{customer_id}.
func (*CustomersChromePrintersService) ListPrinterModels ¶
added in v0.42.0
func (r *CustomersChromePrintersService) ListPrinterModels(parent string) *CustomersChromePrintersListPrinterModelsCall

ListPrinterModels: Lists the supported printer models.

parent: The name of the customer who owns this collection of printers. Format: customers/{customer_id}.
func (*CustomersChromePrintersService) Patch ¶
added in v0.42.0
func (r *CustomersChromePrintersService) Patch(name string, printer *Printer) *CustomersChromePrintersPatchCall

Patch: Updates a `Printer` resource.

name: Identifier. The resource name of the Printer object, in the format customers/{customer-id}/printers/{printer-id} (During printer creation leave empty).
type CustomersChromeService ¶
added in v0.42.0
type CustomersChromeService struct {
	PrintServers *CustomersChromePrintServersService

	Printers *CustomersChromePrintersService
	// contains filtered or unexported fields
}
func NewCustomersChromeService ¶
added in v0.42.0
func NewCustomersChromeService(s *Service) *CustomersChromeService
type CustomersGetCall ¶
type CustomersGetCall struct {
	// contains filtered or unexported fields
}
func (*CustomersGetCall) Context ¶
func (c *CustomersGetCall) Context(ctx context.Context) *CustomersGetCall

Context sets the context to be used in this call's Do method.

func (*CustomersGetCall) Do ¶
func (c *CustomersGetCall) Do(opts ...googleapi.CallOption) (*Customer, error)

Do executes the "directory.customers.get" call. Any non-2xx status code is an error. Response headers are in either *Customer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersGetCall) Fields ¶
func (c *CustomersGetCall) Fields(s ...googleapi.Field) *CustomersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersGetCall) Header ¶
func (c *CustomersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CustomersGetCall) IfNoneMatch ¶
func (c *CustomersGetCall) IfNoneMatch(entityTag string) *CustomersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type CustomersPatchCall ¶
type CustomersPatchCall struct {
	// contains filtered or unexported fields
}
func (*CustomersPatchCall) Context ¶
func (c *CustomersPatchCall) Context(ctx context.Context) *CustomersPatchCall

Context sets the context to be used in this call's Do method.

func (*CustomersPatchCall) Do ¶
func (c *CustomersPatchCall) Do(opts ...googleapi.CallOption) (*Customer, error)

Do executes the "directory.customers.patch" call. Any non-2xx status code is an error. Response headers are in either *Customer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersPatchCall) Fields ¶
func (c *CustomersPatchCall) Fields(s ...googleapi.Field) *CustomersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersPatchCall) Header ¶
func (c *CustomersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CustomersService ¶
type CustomersService struct {
	Chrome *CustomersChromeService
	// contains filtered or unexported fields
}
func NewCustomersService ¶
func NewCustomersService(s *Service) *CustomersService
func (*CustomersService) Get ¶
func (r *CustomersService) Get(customerKey string) *CustomersGetCall

Get: Retrieves a customer.

- customerKey: Id of the customer to be retrieved.

func (*CustomersService) Patch ¶
func (r *CustomersService) Patch(customerKey string, customer *Customer) *CustomersPatchCall

Patch: Patches a customer.

- customerKey: Id of the customer to be updated.

func (*CustomersService) Update ¶
func (r *CustomersService) Update(customerKey string, customer *Customer) *CustomersUpdateCall

Update: Updates a customer.

- customerKey: Id of the customer to be updated.

type CustomersUpdateCall ¶
type CustomersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*CustomersUpdateCall) Context ¶
func (c *CustomersUpdateCall) Context(ctx context.Context) *CustomersUpdateCall

Context sets the context to be used in this call's Do method.

func (*CustomersUpdateCall) Do ¶
func (c *CustomersUpdateCall) Do(opts ...googleapi.CallOption) (*Customer, error)

Do executes the "directory.customers.update" call. Any non-2xx status code is an error. Response headers are in either *Customer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomersUpdateCall) Fields ¶
func (c *CustomersUpdateCall) Fields(s ...googleapi.Field) *CustomersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CustomersUpdateCall) Header ¶
func (c *CustomersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DirectoryChromeosdevicesCommand ¶
added in v0.34.0
type DirectoryChromeosdevicesCommand struct {
	// CommandExpireTime: The time at which the command will expire. If the device
	// doesn't execute the command within this time the command will become
	// expired.
	CommandExpireTime string `json:"commandExpireTime,omitempty"`
	// CommandId: Unique ID of a device command.
	CommandId int64 `json:"commandId,omitempty,string"`
	// CommandResult: The result of the command execution.
	CommandResult *DirectoryChromeosdevicesCommandResult `json:"commandResult,omitempty"`
	// IssueTime: The timestamp when the command was issued by the admin.
	IssueTime string `json:"issueTime,omitempty"`
	// Payload: The payload that the command specified, if any.
	Payload string `json:"payload,omitempty"`
	// State: Indicates the command state.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - The command status was unspecified.
	//   "PENDING" - An unexpired command not yet sent to the client.
	//   "EXPIRED" - The command didn't get executed by the client within the
	// expected time.
	//   "CANCELLED" - The command is cancelled by admin while in PENDING.
	//   "SENT_TO_CLIENT" - The command has been sent to the client.
	//   "ACKED_BY_CLIENT" - The client has responded that it received the command.
	//   "EXECUTED_BY_CLIENT" - The client has (un)successfully executed the
	// command.
	State string `json:"state,omitempty"`
	// Type: The type of the command.
	//
	// Possible values:
	//   "COMMAND_TYPE_UNSPECIFIED" - The command type was unspecified.
	//   "REBOOT" - Reboot the device. Can be issued to Kiosk and managed guest
	// session devices, and regular devices running ChromeOS version 113 or later.
	//   "TAKE_A_SCREENSHOT" - Take a screenshot of the device. Only available if
	// the device is in Kiosk Mode.
	//   "SET_VOLUME" - Set the volume of the device. Can only be issued to Kiosk
	// and managed guest session devices.
	//   "WIPE_USERS" - Wipe all the users off of the device. Executing this
	// command in the device will remove all user profile data, but it will keep
	// device policy and enrollment.
	//   "REMOTE_POWERWASH" - Wipes the device by performing a power wash.
	// Executing this command in the device will remove all data including user
	// policies, device policies and enrollment policies. Warning: This will revert
	// the device back to a factory state with no enrollment unless the device is
	// subject to forced or auto enrollment. Use with caution, as this is an
	// irreversible action!
	//   "DEVICE_START_CRD_SESSION" - Starts a Chrome Remote Desktop session.
	//   "CAPTURE_LOGS" - Capture the system logs of a kiosk device. The logs can
	// be downloaded from the downloadUrl link present in `deviceFiles` field of
	// [chromeosdevices](https://developers.google.com/workspace/admin/directory/ref
	// erence/rest/v1/chromeosdevices)
	//   "FETCH_CRD_AVAILABILITY_INFO" - Fetches available type(s) of Chrome Remote
	// Desktop sessions (private or shared) that can be used to remotely connect to
	// the device.
	//   "FETCH_SUPPORT_PACKET" - Fetch support packet from a device remotely.
	// Support packet is a zip archive that contains various system logs and debug
	// data from a ChromeOS device. The support packet can be downloaded from the
	// downloadURL link present in the `deviceFiles` field of
	// [`chromeosdevices`](https://developers.google.com/workspace/admin/directory/r
	// eference/rest/v1/chromeosdevices)
	Type string `json:"type,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CommandExpireTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CommandExpireTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DirectoryChromeosdevicesCommand: Information regarding a command that was issued to a device.

func (DirectoryChromeosdevicesCommand) MarshalJSON ¶
added in v0.34.0
func (s DirectoryChromeosdevicesCommand) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesCommandResult ¶
added in v0.34.0
type DirectoryChromeosdevicesCommandResult struct {
	// CommandResultPayload: The payload for the command result. The following
	// commands respond with a payload: * `DEVICE_START_CRD_SESSION`: Payload is a
	// stringified JSON object in the form: { "url": url }. The provided URL links
	// to the Chrome Remote Desktop session and requires authentication using only
	// the `email` associated with the command's issuance. *
	// `FETCH_CRD_AVAILABILITY_INFO`: Payload is a stringified JSON object in the
	// form: { "deviceIdleTimeInSeconds": number, "userSessionType": string,
	// "remoteSupportAvailability": string, "remoteAccessAvailability": string }.
	// The "remoteSupportAvailability" field is set to "AVAILABLE" if `shared` CRD
	// session to the device is available. The "remoteAccessAvailability" field is
	// set to "AVAILABLE" if `private` CRD session to the device is available.
	CommandResultPayload string `json:"commandResultPayload,omitempty"`
	// ErrorMessage: The error message with a short explanation as to why the
	// command failed. Only present if the command failed.
	ErrorMessage string `json:"errorMessage,omitempty"`
	// ExecuteTime: The time at which the command was executed or failed to
	// execute.
	ExecuteTime string `json:"executeTime,omitempty"`
	// Result: The result of the command.
	//
	// Possible values:
	//   "COMMAND_RESULT_TYPE_UNSPECIFIED" - The command result was unspecified.
	//   "IGNORED" - The command was ignored as obsolete.
	//   "FAILURE" - The command could not be executed successfully.
	//   "SUCCESS" - The command was successfully executed.
	Result string `json:"result,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CommandResultPayload") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CommandResultPayload") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DirectoryChromeosdevicesCommandResult: The result of executing a command.

func (DirectoryChromeosdevicesCommandResult) MarshalJSON ¶
added in v0.34.0
func (s DirectoryChromeosdevicesCommandResult) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesIssueCommandRequest ¶
added in v0.34.0
type DirectoryChromeosdevicesIssueCommandRequest struct {
	// CommandType: The type of command.
	//
	// Possible values:
	//   "COMMAND_TYPE_UNSPECIFIED" - The command type was unspecified.
	//   "REBOOT" - Reboot the device. Can be issued to Kiosk and managed guest
	// session devices, and regular devices running ChromeOS version 113 or later.
	//   "TAKE_A_SCREENSHOT" - Take a screenshot of the device. Only available if
	// the device is in Kiosk Mode.
	//   "SET_VOLUME" - Set the volume of the device. Can only be issued to Kiosk
	// and managed guest session devices.
	//   "WIPE_USERS" - Wipe all the users off of the device. Executing this
	// command in the device will remove all user profile data, but it will keep
	// device policy and enrollment.
	//   "REMOTE_POWERWASH" - Wipes the device by performing a power wash.
	// Executing this command in the device will remove all data including user
	// policies, device policies and enrollment policies. Warning: This will revert
	// the device back to a factory state with no enrollment unless the device is
	// subject to forced or auto enrollment. Use with caution, as this is an
	// irreversible action!
	//   "DEVICE_START_CRD_SESSION" - Starts a Chrome Remote Desktop session.
	//   "CAPTURE_LOGS" - Capture the system logs of a kiosk device. The logs can
	// be downloaded from the downloadUrl link present in `deviceFiles` field of
	// [chromeosdevices](https://developers.google.com/workspace/admin/directory/ref
	// erence/rest/v1/chromeosdevices)
	//   "FETCH_CRD_AVAILABILITY_INFO" - Fetches available type(s) of Chrome Remote
	// Desktop sessions (private or shared) that can be used to remotely connect to
	// the device.
	//   "FETCH_SUPPORT_PACKET" - Fetch support packet from a device remotely.
	// Support packet is a zip archive that contains various system logs and debug
	// data from a ChromeOS device. The support packet can be downloaded from the
	// downloadURL link present in the `deviceFiles` field of
	// [`chromeosdevices`](https://developers.google.com/workspace/admin/directory/r
	// eference/rest/v1/chromeosdevices)
	CommandType string `json:"commandType,omitempty"`
	// Payload: The payload for the command, provide it only if command supports
	// it. The following commands support adding payload: * `SET_VOLUME`: Payload
	// is a stringified JSON object in the form: { "volume": 50 }. The volume has
	// to be an integer in the range [0,100]. * `DEVICE_START_CRD_SESSION`: Payload
	// is optionally a stringified JSON object in the form: { "ackedUserPresence":
	// true, "crdSessionType": string }. `ackedUserPresence` is a boolean. By
	// default, `ackedUserPresence` is set to `false`. To start a Chrome Remote
	// Desktop session for an active device, set `ackedUserPresence` to `true`.
	// `crdSessionType` can only select from values `private` (which grants the
	// remote admin exclusive control of the ChromeOS device) or `shared` (which
	// allows the admin and the local user to share control of the ChromeOS
	// device). If not set, `crdSessionType` defaults to `shared`. The
	// `FETCH_CRD_AVAILABILITY_INFO` command can be used to determine available
	// session types on the device. * `REBOOT`: Payload is a stringified JSON
	// object in the form: { "user_session_delay_seconds": 300 }. The
	// `user_session_delay_seconds` is the amount of seconds to wait before
	// rebooting the device if a user is logged in. It has to be an integer in the
	// range [0,300]. When payload is not present for reboot, 0 delay is the
	// default. Note: This only applies if an actual user is logged in, including a
	// Guest. If the device is in the login screen or in Kiosk mode the value is
	// not respected and the device immediately reboots. * `FETCH_SUPPORT_PACKET`:
	// Payload is optionally a stringified JSON object in the form:
	// {"supportPacketDetails":{ "issueCaseId": optional_support_case_id_string,
	// "issueDescription": optional_issue_description_string,
	// "requestedDataCollectors": []}} The list of available `data_collector_enums`
	// are as following: Chrome System Information (1), Crash IDs (2), Memory
	// Details (3), UI Hierarchy (4), Additional ChromeOS Platform Logs (5), Device
	// Event (6), Intel WiFi NICs Debug Dump (7), Touch Events (8), Lacros (9),
	// Lacros System Information (10), ChromeOS Flex Logs (11), DBus Details (12),
	// ChromeOS Network Routes (13), ChromeOS Shill (Connection Manager) Logs (14),
	// Policies (15), ChromeOS System State and Logs (16), ChromeOS System Logs
	// (17), ChromeOS Chrome User Logs (18), ChromeOS Bluetooth (19), ChromeOS
	// Connected Input Devices (20), ChromeOS Traffic Counters (21), ChromeOS
	// Virtual Keyboard (22), ChromeOS Network Health (23). See more details in
	// help article (https://support.google.com/chrome/a?p=remote-log).
	Payload string `json:"payload,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CommandType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CommandType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DirectoryChromeosdevicesIssueCommandRequest: A request for issuing a command.

func (DirectoryChromeosdevicesIssueCommandRequest) MarshalJSON ¶
added in v0.34.0
func (s DirectoryChromeosdevicesIssueCommandRequest) MarshalJSON() ([]byte, error)
type DirectoryChromeosdevicesIssueCommandResponse ¶
added in v0.34.0
type DirectoryChromeosdevicesIssueCommandResponse struct {
	// CommandId: The unique ID of the issued command, used to retrieve the command
	// status.
	CommandId int64 `json:"commandId,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CommandId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CommandId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DirectoryChromeosdevicesIssueCommandResponse: A response for issuing a command.

func (DirectoryChromeosdevicesIssueCommandResponse) MarshalJSON ¶
added in v0.34.0
func (s DirectoryChromeosdevicesIssueCommandResponse) MarshalJSON() ([]byte, error)
type DirectoryUsersCreateGuestRequest ¶
added in v0.257.0
type DirectoryUsersCreateGuestRequest struct {
	// Customer: Optional. Immutable ID of the Google Workspace account.
	Customer string `json:"customer,omitempty"`
	// PrimaryGuestEmail: Immutable. External email of the guest user being
	// created.
	PrimaryGuestEmail string `json:"primaryGuestEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Customer") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Customer") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DirectoryUsersCreateGuestRequest: Directory users guest creation request message.

func (DirectoryUsersCreateGuestRequest) MarshalJSON ¶
added in v0.257.0
func (s DirectoryUsersCreateGuestRequest) MarshalJSON() ([]byte, error)
type DomainAlias ¶
type DomainAlias struct {
	// CreationTime: The creation time of the domain alias. (Read-only).
	CreationTime int64 `json:"creationTime,omitempty,string"`
	// DomainAliasName: The domain alias name.
	DomainAliasName string `json:"domainAliasName,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// ParentDomainName: The parent domain name that the domain alias is associated
	// with. This can either be a primary or secondary domain name within a
	// customer.
	ParentDomainName string `json:"parentDomainName,omitempty"`
	// Verified: Indicates the verification state of a domain alias. (Read-only)
	Verified bool `json:"verified,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreationTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreationTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (DomainAlias) MarshalJSON ¶
func (s DomainAlias) MarshalJSON() ([]byte, error)
type DomainAliases ¶
type DomainAliases struct {
	// DomainAliases: A list of domain alias objects.
	DomainAliases []*DomainAlias `json:"domainAliases,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DomainAliases") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DomainAliases") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (DomainAliases) MarshalJSON ¶
func (s DomainAliases) MarshalJSON() ([]byte, error)
type DomainAliasesDeleteCall ¶
type DomainAliasesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*DomainAliasesDeleteCall) Context ¶
func (c *DomainAliasesDeleteCall) Context(ctx context.Context) *DomainAliasesDeleteCall

Context sets the context to be used in this call's Do method.

func (*DomainAliasesDeleteCall) Do ¶
func (c *DomainAliasesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.domainAliases.delete" call.

func (*DomainAliasesDeleteCall) Fields ¶
func (c *DomainAliasesDeleteCall) Fields(s ...googleapi.Field) *DomainAliasesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainAliasesDeleteCall) Header ¶
func (c *DomainAliasesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DomainAliasesGetCall ¶
type DomainAliasesGetCall struct {
	// contains filtered or unexported fields
}
func (*DomainAliasesGetCall) Context ¶
func (c *DomainAliasesGetCall) Context(ctx context.Context) *DomainAliasesGetCall

Context sets the context to be used in this call's Do method.

func (*DomainAliasesGetCall) Do ¶
func (c *DomainAliasesGetCall) Do(opts ...googleapi.CallOption) (*DomainAlias, error)

Do executes the "directory.domainAliases.get" call. Any non-2xx status code is an error. Response headers are in either *DomainAlias.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainAliasesGetCall) Fields ¶
func (c *DomainAliasesGetCall) Fields(s ...googleapi.Field) *DomainAliasesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainAliasesGetCall) Header ¶
func (c *DomainAliasesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DomainAliasesGetCall) IfNoneMatch ¶
func (c *DomainAliasesGetCall) IfNoneMatch(entityTag string) *DomainAliasesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DomainAliasesInsertCall ¶
type DomainAliasesInsertCall struct {
	// contains filtered or unexported fields
}
func (*DomainAliasesInsertCall) Context ¶
func (c *DomainAliasesInsertCall) Context(ctx context.Context) *DomainAliasesInsertCall

Context sets the context to be used in this call's Do method.

func (*DomainAliasesInsertCall) Do ¶
func (c *DomainAliasesInsertCall) Do(opts ...googleapi.CallOption) (*DomainAlias, error)

Do executes the "directory.domainAliases.insert" call. Any non-2xx status code is an error. Response headers are in either *DomainAlias.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainAliasesInsertCall) Fields ¶
func (c *DomainAliasesInsertCall) Fields(s ...googleapi.Field) *DomainAliasesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainAliasesInsertCall) Header ¶
func (c *DomainAliasesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DomainAliasesListCall ¶
type DomainAliasesListCall struct {
	// contains filtered or unexported fields
}
func (*DomainAliasesListCall) Context ¶
func (c *DomainAliasesListCall) Context(ctx context.Context) *DomainAliasesListCall

Context sets the context to be used in this call's Do method.

func (*DomainAliasesListCall) Do ¶
func (c *DomainAliasesListCall) Do(opts ...googleapi.CallOption) (*DomainAliases, error)

Do executes the "directory.domainAliases.list" call. Any non-2xx status code is an error. Response headers are in either *DomainAliases.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainAliasesListCall) Fields ¶
func (c *DomainAliasesListCall) Fields(s ...googleapi.Field) *DomainAliasesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainAliasesListCall) Header ¶
func (c *DomainAliasesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DomainAliasesListCall) IfNoneMatch ¶
func (c *DomainAliasesListCall) IfNoneMatch(entityTag string) *DomainAliasesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*DomainAliasesListCall) ParentDomainName ¶
func (c *DomainAliasesListCall) ParentDomainName(parentDomainName string) *DomainAliasesListCall

ParentDomainName sets the optional parameter "parentDomainName": Name of the parent domain for which domain aliases are to be fetched.

type DomainAliasesService ¶
type DomainAliasesService struct {
	// contains filtered or unexported fields
}
func NewDomainAliasesService ¶
func NewDomainAliasesService(s *Service) *DomainAliasesService
func (*DomainAliasesService) Delete ¶
func (r *DomainAliasesService) Delete(customer string, domainAliasName string) *DomainAliasesDeleteCall

Delete: Deletes a domain Alias of the customer.

- customer: Immutable ID of the Google Workspace account. - domainAliasName: Name of domain alias to be retrieved.

func (*DomainAliasesService) Get ¶
func (r *DomainAliasesService) Get(customer string, domainAliasName string) *DomainAliasesGetCall

Get: Retrieves a domain alias of the customer.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
domainAliasName: Name of domain alias to be retrieved.
func (*DomainAliasesService) Insert ¶
func (r *DomainAliasesService) Insert(customer string, domainalias *DomainAlias) *DomainAliasesInsertCall

Insert: Inserts a domain alias of the customer.

- customer: Immutable ID of the Google Workspace account.

func (*DomainAliasesService) List ¶
func (r *DomainAliasesService) List(customer string) *DomainAliasesListCall

List: Lists the domain aliases of the customer.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
type Domains ¶
type Domains struct {
	// CreationTime: Creation time of the domain. Expressed in Unix time
	// (https://en.wikipedia.org/wiki/Epoch_time) format. (Read-only).
	CreationTime int64 `json:"creationTime,omitempty,string"`
	// DomainAliases: A list of domain alias objects. (Read-only)
	DomainAliases []*DomainAlias `json:"domainAliases,omitempty"`
	// DomainName: The domain name of the customer.
	DomainName string `json:"domainName,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// IsPrimary: Indicates if the domain is a primary domain (Read-only).
	IsPrimary bool `json:"isPrimary,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// Verified: Indicates the verification state of a domain. (Read-only).
	Verified bool `json:"verified,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreationTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreationTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (Domains) MarshalJSON ¶
func (s Domains) MarshalJSON() ([]byte, error)
type Domains2 ¶
type Domains2 struct {
	// Domains: A list of domain objects.
	Domains []*Domains `json:"domains,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Domains") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Domains") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (Domains2) MarshalJSON ¶
func (s Domains2) MarshalJSON() ([]byte, error)
type DomainsDeleteCall ¶
type DomainsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*DomainsDeleteCall) Context ¶
func (c *DomainsDeleteCall) Context(ctx context.Context) *DomainsDeleteCall

Context sets the context to be used in this call's Do method.

func (*DomainsDeleteCall) Do ¶
func (c *DomainsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.domains.delete" call.

func (*DomainsDeleteCall) Fields ¶
func (c *DomainsDeleteCall) Fields(s ...googleapi.Field) *DomainsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainsDeleteCall) Header ¶
func (c *DomainsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DomainsGetCall ¶
type DomainsGetCall struct {
	// contains filtered or unexported fields
}
func (*DomainsGetCall) Context ¶
func (c *DomainsGetCall) Context(ctx context.Context) *DomainsGetCall

Context sets the context to be used in this call's Do method.

func (*DomainsGetCall) Do ¶
func (c *DomainsGetCall) Do(opts ...googleapi.CallOption) (*Domains, error)

Do executes the "directory.domains.get" call. Any non-2xx status code is an error. Response headers are in either *Domains.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainsGetCall) Fields ¶
func (c *DomainsGetCall) Fields(s ...googleapi.Field) *DomainsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainsGetCall) Header ¶
func (c *DomainsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DomainsGetCall) IfNoneMatch ¶
func (c *DomainsGetCall) IfNoneMatch(entityTag string) *DomainsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DomainsInsertCall ¶
type DomainsInsertCall struct {
	// contains filtered or unexported fields
}
func (*DomainsInsertCall) Context ¶
func (c *DomainsInsertCall) Context(ctx context.Context) *DomainsInsertCall

Context sets the context to be used in this call's Do method.

func (*DomainsInsertCall) Do ¶
func (c *DomainsInsertCall) Do(opts ...googleapi.CallOption) (*Domains, error)

Do executes the "directory.domains.insert" call. Any non-2xx status code is an error. Response headers are in either *Domains.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainsInsertCall) Fields ¶
func (c *DomainsInsertCall) Fields(s ...googleapi.Field) *DomainsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainsInsertCall) Header ¶
func (c *DomainsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DomainsListCall ¶
type DomainsListCall struct {
	// contains filtered or unexported fields
}
func (*DomainsListCall) Context ¶
func (c *DomainsListCall) Context(ctx context.Context) *DomainsListCall

Context sets the context to be used in this call's Do method.

func (*DomainsListCall) Do ¶
func (c *DomainsListCall) Do(opts ...googleapi.CallOption) (*Domains2, error)

Do executes the "directory.domains.list" call. Any non-2xx status code is an error. Response headers are in either *Domains2.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DomainsListCall) Fields ¶
func (c *DomainsListCall) Fields(s ...googleapi.Field) *DomainsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DomainsListCall) Header ¶
func (c *DomainsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DomainsListCall) IfNoneMatch ¶
func (c *DomainsListCall) IfNoneMatch(entityTag string) *DomainsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DomainsService ¶
type DomainsService struct {
	// contains filtered or unexported fields
}
func NewDomainsService ¶
func NewDomainsService(s *Service) *DomainsService
func (*DomainsService) Delete ¶
func (r *DomainsService) Delete(customer string, domainName string) *DomainsDeleteCall

Delete: Deletes a domain of the customer.

- customer: Immutable ID of the Google Workspace account. - domainName: Name of domain to be deleted.

func (*DomainsService) Get ¶
func (r *DomainsService) Get(customer string, domainName string) *DomainsGetCall

Get: Retrieves a domain of the customer.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
domainName: Name of domain to be retrieved.
func (*DomainsService) Insert ¶
func (r *DomainsService) Insert(customer string, domains *Domains) *DomainsInsertCall

Insert: Inserts a domain of the customer.

- customer: Immutable ID of the Google Workspace account.

func (*DomainsService) List ¶
func (r *DomainsService) List(customer string) *DomainsListCall

List: Lists the domains of the customer.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
type Empty ¶
added in v0.42.0
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type FailureInfo ¶
added in v0.42.0
type FailureInfo struct {
	// ErrorCode: Canonical code for why the update failed to apply.
	//
	// Possible values:
	//   "OK" - Not an error; returned on success. HTTP Mapping: 200 OK
	//   "CANCELLED" - The operation was cancelled, typically by the caller. HTTP
	// Mapping: 499 Client Closed Request
	//   "UNKNOWN" - Unknown error. For example, this error may be returned when a
	// `Status` value received from another address space belongs to an error space
	// that is not known in this address space. Also errors raised by APIs that do
	// not return enough error information may be converted to this error. HTTP
	// Mapping: 500 Internal Server Error
	//   "INVALID_ARGUMENT" - The client specified an invalid argument. Note that
	// this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates
	// arguments that are problematic regardless of the state of the system (e.g.,
	// a malformed file name). HTTP Mapping: 400 Bad Request
	//   "DEADLINE_EXCEEDED" - The deadline expired before the operation could
	// complete. For operations that change the state of the system, this error may
	// be returned even if the operation has completed successfully. For example, a
	// successful response from a server could have been delayed long enough for
	// the deadline to expire. HTTP Mapping: 504 Gateway Timeout
	//   "NOT_FOUND" - Some requested entity (e.g., file or directory) was not
	// found. Note to server developers: if a request is denied for an entire class
	// of users, such as gradual feature rollout or undocumented allowlist,
	// `NOT_FOUND` may be used. If a request is denied for some users within a
	// class of users, such as user-based access control, `PERMISSION_DENIED` must
	// be used. HTTP Mapping: 404 Not Found
	//   "ALREADY_EXISTS" - The entity that a client attempted to create (e.g.,
	// file or directory) already exists. HTTP Mapping: 409 Conflict
	//   "PERMISSION_DENIED" - The caller does not have permission to execute the
	// specified operation. `PERMISSION_DENIED` must not be used for rejections
	// caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for
	// those errors). `PERMISSION_DENIED` must not be used if the caller can not be
	// identified (use `UNAUTHENTICATED` instead for those errors). This error code
	// does not imply the request is valid or the requested entity exists or
	// satisfies other pre-conditions. HTTP Mapping: 403 Forbidden
	//   "UNAUTHENTICATED" - The request does not have valid authentication
	// credentials for the operation. HTTP Mapping: 401 Unauthorized
	//   "RESOURCE_EXHAUSTED" - Some resource has been exhausted, perhaps a
	// per-user quota, or perhaps the entire file system is out of space. HTTP
	// Mapping: 429 Too Many Requests
	//   "FAILED_PRECONDITION" - The operation was rejected because the system is
	// not in a state required for the operation's execution. For example, the
	// directory to be deleted is non-empty, an rmdir operation is applied to a
	// non-directory, etc. Service implementors can use the following guidelines to
	// decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use
	// `UNAVAILABLE` if the client can retry just the failing call. (b) Use
	// `ABORTED` if the client should retry at a higher level. For example, when a
	// client-specified test-and-set fails, indicating the client should restart a
	// read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client
	// should not retry until the system state has been explicitly fixed. For
	// example, if an "rmdir" fails because the directory is non-empty,
	// `FAILED_PRECONDITION` should be returned since the client should not retry
	// unless the files are deleted from the directory. HTTP Mapping: 400 Bad
	// Request
	//   "ABORTED" - The operation was aborted, typically due to a concurrency
	// issue such as a sequencer check failure or transaction abort. See the
	// guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and
	// `UNAVAILABLE`. HTTP Mapping: 409 Conflict
	//   "OUT_OF_RANGE" - The operation was attempted past the valid range. E.g.,
	// seeking or reading past end-of-file. Unlike `INVALID_ARGUMENT`, this error
	// indicates a problem that may be fixed if the system state changes. For
	// example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to
	// read at an offset that is not in the range [0,2^32-1], but it will generate
	// `OUT_OF_RANGE` if asked to read from an offset past the current file size.
	// There is a fair bit of overlap between `FAILED_PRECONDITION` and
	// `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error)
	// when it applies so that callers who are iterating through a space can easily
	// look for an `OUT_OF_RANGE` error to detect when they are done. HTTP Mapping:
	// 400 Bad Request
	//   "UNIMPLEMENTED" - The operation is not implemented or is not
	// supported/enabled in this service. HTTP Mapping: 501 Not Implemented
	//   "INTERNAL" - Internal errors. This means that some invariants expected by
	// the underlying system have been broken. This error code is reserved for
	// serious errors. HTTP Mapping: 500 Internal Server Error
	//   "UNAVAILABLE" - The service is currently unavailable. This is most likely
	// a transient condition, which can be corrected by retrying with a backoff.
	// Note that it is not always safe to retry non-idempotent operations. See the
	// guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and
	// `UNAVAILABLE`. HTTP Mapping: 503 Service Unavailable
	//   "DATA_LOSS" - Unrecoverable data loss or corruption. HTTP Mapping: 500
	// Internal Server Error
	ErrorCode string `json:"errorCode,omitempty"`
	// ErrorMessage: Failure reason message.
	ErrorMessage string `json:"errorMessage,omitempty"`
	// Printer: Failed printer.
	Printer *Printer `json:"printer,omitempty"`
	// PrinterId: Id of a failed printer.
	PrinterId string `json:"printerId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ErrorCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ErrorCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FailureInfo: Info about failures

func (FailureInfo) MarshalJSON ¶
added in v0.42.0
func (s FailureInfo) MarshalJSON() ([]byte, error)
type FanInfo ¶
added in v0.179.0
type FanInfo struct {
	// SpeedRpm: Output only. Fan speed in RPM.
	SpeedRpm int64 `json:"speedRpm,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SpeedRpm") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SpeedRpm") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FanInfo: Information about the device's fan.

func (FanInfo) MarshalJSON ¶
added in v0.179.0
func (s FanInfo) MarshalJSON() ([]byte, error)
type Feature ¶
type Feature struct {
	// Etags: ETag of the resource.
	Etags string `json:"etags,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// Name: The name of the feature.
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Etags") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Etags") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Feature: JSON template for Feature object in Directory API.

func (Feature) MarshalJSON ¶
func (s Feature) MarshalJSON() ([]byte, error)
type FeatureInstance ¶
type FeatureInstance struct {
	// Feature: The feature that this is an instance of. A calendar resource may
	// have multiple instances of a feature.
	Feature *Feature `json:"feature,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Feature") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Feature") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FeatureInstance: JSON template for a feature instance.

func (FeatureInstance) MarshalJSON ¶
func (s FeatureInstance) MarshalJSON() ([]byte, error)
type FeatureRename ¶
type FeatureRename struct {
	// NewName: New name of the feature.
	NewName string `json:"newName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewName") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (FeatureRename) MarshalJSON ¶
func (s FeatureRename) MarshalJSON() ([]byte, error)
type Features ¶
type Features struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Features: The Features in this page of results.
	Features []*Feature `json:"features,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: The continuation token, used to page through large result
	// sets. Provide this value in a subsequent request to return the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

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

Features: Public API: Resources.features

func (Features) MarshalJSON ¶
func (s Features) MarshalJSON() ([]byte, error)
type Group ¶
type Group struct {
	// AdminCreated: Read-only. Value is `true` if this group was created by an
	// administrator rather than a user.
	AdminCreated bool `json:"adminCreated,omitempty"`
	// Aliases: Read-only. The list of a group's alias email addresses. To add,
	// update, or remove a group's aliases, use the `groups.aliases` methods. If
	// edited in a group's POST or PUT request, the edit is ignored.
	Aliases []string `json:"aliases,omitempty"`
	// Description: An extended description to help users determine the purpose of
	// a group. For example, you can include information about who should join the
	// group, the types of messages to send to the group, links to FAQs about the
	// group, or related groups. Maximum length is `4,096` characters.
	Description string `json:"description,omitempty"`
	// DirectMembersCount: The number of users that are direct members of the
	// group. If a group is a member (child) of this group (the parent), members of
	// the child group are not counted in the `directMembersCount` property of the
	// parent group.
	DirectMembersCount int64 `json:"directMembersCount,omitempty,string"`
	// Email: The group's email address. If your account has multiple domains,
	// select the appropriate domain for the email address. The `email` must be
	// unique. This property is required when creating a group. Group email
	// addresses are subject to the same character usage rules as usernames, see
	// the help center (https://support.google.com/a/answer/9193374) for details.
	Email string `json:"email,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Id: Read-only. The unique ID of a group. A group `id` can be used as a group
	// request URI's `groupKey`.
	Id string `json:"id,omitempty"`
	// Kind: The type of the API resource. For Groups resources, the value is
	// `admin#directory#group`.
	Kind string `json:"kind,omitempty"`
	// Name: The group's display name.
	Name string `json:"name,omitempty"`
	// NonEditableAliases: Read-only. The list of the group's non-editable alias
	// email addresses that are outside of the account's primary domain or
	// subdomains. These are functioning email addresses used by the group. This is
	// a read-only property returned in the API's response for a group. If edited
	// in a group's POST or PUT request, the edit is ignored.
	NonEditableAliases []string `json:"nonEditableAliases,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdminCreated") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdminCreated") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Group: Google Groups provide your users the ability to send messages to groups of people using the group's email address. For more information about common tasks, see the Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-groups). For information about other types of groups, see the Cloud Identity Groups API documentation (https://cloud.google.com/identity/docs/groups). Note: The user calling the API (or being impersonated by a service account) must have an assigned role (https://developers.google.com/workspace/admin/directory/v1/guides/manage-roles) that includes Admin API Groups permissions, such as Super Admin or Groups Admin.

func (Group) MarshalJSON ¶
func (s Group) MarshalJSON() ([]byte, error)
type GroupAlias ¶
added in v0.93.0
type GroupAlias struct {
	// Alias: The alias email address.
	Alias string `json:"alias,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Id: The unique ID of the group.
	Id string `json:"id,omitempty"`
	// Kind: The type of the API resource. For Alias resources, the value is
	// `admin#directory#alias`.
	Kind string `json:"kind,omitempty"`
	// PrimaryEmail: The primary email address of the group.
	PrimaryEmail string `json:"primaryEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alias") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alias") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GroupAlias: The Directory API manages aliases, which are alternative email addresses.

func (GroupAlias) MarshalJSON ¶
added in v0.93.0
func (s GroupAlias) MarshalJSON() ([]byte, error)
type Groups ¶
type Groups struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Groups: A list of group objects.
	Groups []*Group `json:"groups,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: Token used to access next page of this result.
	NextPageToken string `json:"nextPageToken,omitempty"`

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
func (Groups) MarshalJSON ¶
func (s Groups) MarshalJSON() ([]byte, error)
type GroupsAliasesDeleteCall ¶
type GroupsAliasesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*GroupsAliasesDeleteCall) Context ¶
func (c *GroupsAliasesDeleteCall) Context(ctx context.Context) *GroupsAliasesDeleteCall

Context sets the context to be used in this call's Do method.

func (*GroupsAliasesDeleteCall) Do ¶
func (c *GroupsAliasesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.groups.aliases.delete" call.

func (*GroupsAliasesDeleteCall) Fields ¶
func (c *GroupsAliasesDeleteCall) Fields(s ...googleapi.Field) *GroupsAliasesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsAliasesDeleteCall) Header ¶
func (c *GroupsAliasesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GroupsAliasesInsertCall ¶
type GroupsAliasesInsertCall struct {
	// contains filtered or unexported fields
}
func (*GroupsAliasesInsertCall) Context ¶
func (c *GroupsAliasesInsertCall) Context(ctx context.Context) *GroupsAliasesInsertCall

Context sets the context to be used in this call's Do method.

func (*GroupsAliasesInsertCall) Do ¶
func (c *GroupsAliasesInsertCall) Do(opts ...googleapi.CallOption) (*Alias, error)

Do executes the "directory.groups.aliases.insert" call. Any non-2xx status code is an error. Response headers are in either *Alias.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsAliasesInsertCall) Fields ¶
func (c *GroupsAliasesInsertCall) Fields(s ...googleapi.Field) *GroupsAliasesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsAliasesInsertCall) Header ¶
func (c *GroupsAliasesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GroupsAliasesListCall ¶
type GroupsAliasesListCall struct {
	// contains filtered or unexported fields
}
func (*GroupsAliasesListCall) Context ¶
func (c *GroupsAliasesListCall) Context(ctx context.Context) *GroupsAliasesListCall

Context sets the context to be used in this call's Do method.

func (*GroupsAliasesListCall) Do ¶
func (c *GroupsAliasesListCall) Do(opts ...googleapi.CallOption) (*Aliases, error)

Do executes the "directory.groups.aliases.list" call. Any non-2xx status code is an error. Response headers are in either *Aliases.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsAliasesListCall) Fields ¶
func (c *GroupsAliasesListCall) Fields(s ...googleapi.Field) *GroupsAliasesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsAliasesListCall) Header ¶
func (c *GroupsAliasesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GroupsAliasesListCall) IfNoneMatch ¶
func (c *GroupsAliasesListCall) IfNoneMatch(entityTag string) *GroupsAliasesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GroupsAliasesService ¶
type GroupsAliasesService struct {
	// contains filtered or unexported fields
}
func NewGroupsAliasesService ¶
func NewGroupsAliasesService(s *Service) *GroupsAliasesService
func (*GroupsAliasesService) Delete ¶
func (r *GroupsAliasesService) Delete(groupKey string, alias string) *GroupsAliasesDeleteCall

Delete: Removes an alias.

alias: The alias to be removed.
groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*GroupsAliasesService) Insert ¶
func (r *GroupsAliasesService) Insert(groupKey string, alias *Alias) *GroupsAliasesInsertCall

Insert: Adds an alias for the group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*GroupsAliasesService) List ¶
func (r *GroupsAliasesService) List(groupKey string) *GroupsAliasesListCall

List: Lists all aliases for a group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
type GroupsDeleteCall ¶
type GroupsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*GroupsDeleteCall) Context ¶
func (c *GroupsDeleteCall) Context(ctx context.Context) *GroupsDeleteCall

Context sets the context to be used in this call's Do method.

func (*GroupsDeleteCall) Do ¶
func (c *GroupsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.groups.delete" call.

func (*GroupsDeleteCall) Fields ¶
func (c *GroupsDeleteCall) Fields(s ...googleapi.Field) *GroupsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsDeleteCall) Header ¶
func (c *GroupsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GroupsGetCall ¶
type GroupsGetCall struct {
	// contains filtered or unexported fields
}
func (*GroupsGetCall) Context ¶
func (c *GroupsGetCall) Context(ctx context.Context) *GroupsGetCall

Context sets the context to be used in this call's Do method.

func (*GroupsGetCall) Do ¶
func (c *GroupsGetCall) Do(opts ...googleapi.CallOption) (*Group, error)

Do executes the "directory.groups.get" call. Any non-2xx status code is an error. Response headers are in either *Group.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsGetCall) Fields ¶
func (c *GroupsGetCall) Fields(s ...googleapi.Field) *GroupsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsGetCall) Header ¶
func (c *GroupsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GroupsGetCall) IfNoneMatch ¶
func (c *GroupsGetCall) IfNoneMatch(entityTag string) *GroupsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GroupsInsertCall ¶
type GroupsInsertCall struct {
	// contains filtered or unexported fields
}
func (*GroupsInsertCall) Context ¶
func (c *GroupsInsertCall) Context(ctx context.Context) *GroupsInsertCall

Context sets the context to be used in this call's Do method.

func (*GroupsInsertCall) Do ¶
func (c *GroupsInsertCall) Do(opts ...googleapi.CallOption) (*Group, error)

Do executes the "directory.groups.insert" call. Any non-2xx status code is an error. Response headers are in either *Group.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsInsertCall) Fields ¶
func (c *GroupsInsertCall) Fields(s ...googleapi.Field) *GroupsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsInsertCall) Header ¶
func (c *GroupsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GroupsListCall ¶
type GroupsListCall struct {
	// contains filtered or unexported fields
}
func (*GroupsListCall) Context ¶
func (c *GroupsListCall) Context(ctx context.Context) *GroupsListCall

Context sets the context to be used in this call's Do method.

func (*GroupsListCall) Customer ¶
func (c *GroupsListCall) Customer(customer string) *GroupsListCall

Customer sets the optional parameter "customer": The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.

func (*GroupsListCall) Do ¶
func (c *GroupsListCall) Do(opts ...googleapi.CallOption) (*Groups, error)

Do executes the "directory.groups.list" call. Any non-2xx status code is an error. Response headers are in either *Groups.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsListCall) Domain ¶
func (c *GroupsListCall) Domain(domain string) *GroupsListCall

Domain sets the optional parameter "domain": The domain name. Use this field to get groups from only one domain. To return all domains for a customer account, use the `customer` query parameter instead.

func (*GroupsListCall) Fields ¶
func (c *GroupsListCall) Fields(s ...googleapi.Field) *GroupsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsListCall) Header ¶
func (c *GroupsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GroupsListCall) IfNoneMatch ¶
func (c *GroupsListCall) IfNoneMatch(entityTag string) *GroupsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*GroupsListCall) MaxResults ¶
func (c *GroupsListCall) MaxResults(maxResults int64) *GroupsListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return. Max allowed value is 200.

func (*GroupsListCall) OrderBy ¶
func (c *GroupsListCall) OrderBy(orderBy string) *GroupsListCall

OrderBy sets the optional parameter "orderBy": Column to use for sorting results

Possible values:

"email" - Email of the group.

func (*GroupsListCall) PageToken ¶
func (c *GroupsListCall) PageToken(pageToken string) *GroupsListCall

PageToken sets the optional parameter "pageToken": Token to specify next page in the list

func (*GroupsListCall) Pages ¶
func (c *GroupsListCall) Pages(ctx context.Context, f func(*Groups) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*GroupsListCall) Query ¶
func (c *GroupsListCall) Query(query string) *GroupsListCall

Query sets the optional parameter "query": Query string search. Contains one or more search clauses, each with a field, operator, and value. For complete documentation, go to Search for groups (https://developers.google.com/workspace/admin/directory/v1/guides/search-groups).

func (*GroupsListCall) SortOrder ¶
func (c *GroupsListCall) SortOrder(sortOrder string) *GroupsListCall

SortOrder sets the optional parameter "sortOrder": Whether to return results in ascending or descending order. Only of use when orderBy is also used

Possible values:

"ASCENDING" - Ascending order.
"DESCENDING" - Descending order.

func (*GroupsListCall) UserKey ¶
func (c *GroupsListCall) UserKey(userKey string) *GroupsListCall

UserKey sets the optional parameter "userKey": Email or immutable ID of the user if only those groups are to be listed, the given user is a member of. If it's an ID, it should match with the ID of the user object. Cannot be used with the `customer` parameter.

type GroupsPatchCall ¶
type GroupsPatchCall struct {
	// contains filtered or unexported fields
}
func (*GroupsPatchCall) Context ¶
func (c *GroupsPatchCall) Context(ctx context.Context) *GroupsPatchCall

Context sets the context to be used in this call's Do method.

func (*GroupsPatchCall) Do ¶
func (c *GroupsPatchCall) Do(opts ...googleapi.CallOption) (*Group, error)

Do executes the "directory.groups.patch" call. Any non-2xx status code is an error. Response headers are in either *Group.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsPatchCall) Fields ¶
func (c *GroupsPatchCall) Fields(s ...googleapi.Field) *GroupsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsPatchCall) Header ¶
func (c *GroupsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GroupsService ¶
type GroupsService struct {
	Aliases *GroupsAliasesService
	// contains filtered or unexported fields
}
func NewGroupsService ¶
func NewGroupsService(s *Service) *GroupsService
func (*GroupsService) Delete ¶
func (r *GroupsService) Delete(groupKey string) *GroupsDeleteCall

Delete: Deletes a group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*GroupsService) Get ¶
func (r *GroupsService) Get(groupKey string) *GroupsGetCall

Get: Retrieves a group's properties.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*GroupsService) Insert ¶
func (r *GroupsService) Insert(group *Group) *GroupsInsertCall

Insert: Creates a group.

func (*GroupsService) List ¶
func (r *GroupsService) List() *GroupsListCall

List: Retrieves all groups of a domain or of a user given a userKey (paginated).

func (*GroupsService) Patch ¶
func (r *GroupsService) Patch(groupKey string, group *Group) *GroupsPatchCall

Patch: Updates a group's properties. This method supports patch semantics (https://developers.google.com/workspace/admin/directory/v1/guides/performance#patch).

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*GroupsService) Update ¶
func (r *GroupsService) Update(groupKey string, group *Group) *GroupsUpdateCall

Update: Updates a group's properties.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
type GroupsUpdateCall ¶
type GroupsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*GroupsUpdateCall) Context ¶
func (c *GroupsUpdateCall) Context(ctx context.Context) *GroupsUpdateCall

Context sets the context to be used in this call's Do method.

func (*GroupsUpdateCall) Do ¶
func (c *GroupsUpdateCall) Do(opts ...googleapi.CallOption) (*Group, error)

Do executes the "directory.groups.update" call. Any non-2xx status code is an error. Response headers are in either *Group.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GroupsUpdateCall) Fields ¶
func (c *GroupsUpdateCall) Fields(s ...googleapi.Field) *GroupsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GroupsUpdateCall) Header ¶
func (c *GroupsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GuestAccountInfo ¶
added in v0.257.0
type GuestAccountInfo struct {
	// PrimaryGuestEmail: Immutable. The guest's external email.
	PrimaryGuestEmail string `json:"primaryGuestEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrimaryGuestEmail") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrimaryGuestEmail") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GuestAccountInfo: Account info specific to Guest users.

func (GuestAccountInfo) MarshalJSON ¶
added in v0.257.0
func (s GuestAccountInfo) MarshalJSON() ([]byte, error)
type ListPrintServersResponse ¶
added in v0.98.0
type ListPrintServersResponse struct {
	// NextPageToken: A token that can be sent as `page_token` in a request to
	// retrieve the next page. If this field is omitted, there are no subsequent
	// pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// PrintServers: List of print servers.
	PrintServers []*PrintServer `json:"printServers,omitempty"`

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
func (ListPrintServersResponse) MarshalJSON ¶
added in v0.98.0
func (s ListPrintServersResponse) MarshalJSON() ([]byte, error)
type ListPrinterModelsResponse ¶
added in v0.42.0
type ListPrinterModelsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// PrinterModels: Printer models that are currently allowed to be configured
	// for ChromeOs. Some printers may be added or removed over time.
	PrinterModels []*PrinterModel `json:"printerModels,omitempty"`

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

ListPrinterModelsResponse: Response for listing allowed printer models.

func (ListPrinterModelsResponse) MarshalJSON ¶
added in v0.42.0
func (s ListPrinterModelsResponse) MarshalJSON() ([]byte, error)
type ListPrintersResponse ¶
added in v0.42.0
type ListPrintersResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Printers: List of printers. If `org_unit_id` was given in the request, then
	// only printers visible for this OU will be returned. If `org_unit_id` was not
	// given in the request, then all printers will be returned.
	Printers []*Printer `json:"printers,omitempty"`

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

ListPrintersResponse: Response for listing printers.

func (ListPrintersResponse) MarshalJSON ¶
added in v0.42.0
func (s ListPrintersResponse) MarshalJSON() ([]byte, error)
type Member ¶
type Member struct {
	// DeliverySettings: Defines mail delivery preferences of member. This field is
	// only supported by `insert`, `update`, and `get` methods.
	DeliverySettings string `json:"delivery_settings,omitempty"`
	// Email: The member's email address. A member can be a user or another group.
	// This property is required when adding a member to a group. The `email` must
	// be unique and cannot be an alias of another group. If the email address is
	// changed, the API automatically reflects the email address changes.
	Email string `json:"email,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Id: The unique ID of the group member. A member `id` can be used as a member
	// request URI's `memberKey`.
	Id string `json:"id,omitempty"`
	// Kind: The type of the API resource. For Members resources, the value is
	// `admin#directory#member`.
	Kind string `json:"kind,omitempty"`
	// Role: The member's role in a group. The API returns an error for cycles in
	// group memberships. For example, if `group1` is a member of `group2`,
	// `group2` cannot be a member of `group1`. For more information about a
	// member's role, see the administration help center
	// (https://support.google.com/a/answer/167094).
	Role string `json:"role,omitempty"`
	// Status: Status of member (Immutable)
	Status string `json:"status,omitempty"`
	// Type: The type of group member.
	Type string `json:"type,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeliverySettings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeliverySettings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Member: A Google Groups member can be a user or another group. This member can be inside or outside of your account's domains. For more information about common group member tasks, see the Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-group-members).

func (Member) MarshalJSON ¶
func (s Member) MarshalJSON() ([]byte, error)
type Members ¶
type Members struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// Members: A list of member objects.
	Members []*Member `json:"members,omitempty"`
	// NextPageToken: Token used to access next page of this result.
	NextPageToken string `json:"nextPageToken,omitempty"`

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
func (Members) MarshalJSON ¶
func (s Members) MarshalJSON() ([]byte, error)
type MembersDeleteCall ¶
type MembersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MembersDeleteCall) Context ¶
func (c *MembersDeleteCall) Context(ctx context.Context) *MembersDeleteCall

Context sets the context to be used in this call's Do method.

func (*MembersDeleteCall) Do ¶
func (c *MembersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.members.delete" call.

func (*MembersDeleteCall) Fields ¶
func (c *MembersDeleteCall) Fields(s ...googleapi.Field) *MembersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersDeleteCall) Header ¶
func (c *MembersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MembersGetCall ¶
type MembersGetCall struct {
	// contains filtered or unexported fields
}
func (*MembersGetCall) Context ¶
func (c *MembersGetCall) Context(ctx context.Context) *MembersGetCall

Context sets the context to be used in this call's Do method.

func (*MembersGetCall) Do ¶
func (c *MembersGetCall) Do(opts ...googleapi.CallOption) (*Member, error)

Do executes the "directory.members.get" call. Any non-2xx status code is an error. Response headers are in either *Member.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersGetCall) Fields ¶
func (c *MembersGetCall) Fields(s ...googleapi.Field) *MembersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersGetCall) Header ¶
func (c *MembersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MembersGetCall) IfNoneMatch ¶
func (c *MembersGetCall) IfNoneMatch(entityTag string) *MembersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MembersHasMember ¶
type MembersHasMember struct {
	// IsMember: Output only. Identifies whether the given user is a member of the
	// group. Membership can be direct or nested.
	IsMember bool `json:"isMember,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "IsMember") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsMember") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MembersHasMember: JSON template for Has Member response in Directory API.

func (MembersHasMember) MarshalJSON ¶
func (s MembersHasMember) MarshalJSON() ([]byte, error)
type MembersHasMemberCall ¶
type MembersHasMemberCall struct {
	// contains filtered or unexported fields
}
func (*MembersHasMemberCall) Context ¶
func (c *MembersHasMemberCall) Context(ctx context.Context) *MembersHasMemberCall

Context sets the context to be used in this call's Do method.

func (*MembersHasMemberCall) Do ¶
func (c *MembersHasMemberCall) Do(opts ...googleapi.CallOption) (*MembersHasMember, error)

Do executes the "directory.members.hasMember" call. Any non-2xx status code is an error. Response headers are in either *MembersHasMember.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersHasMemberCall) Fields ¶
func (c *MembersHasMemberCall) Fields(s ...googleapi.Field) *MembersHasMemberCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersHasMemberCall) Header ¶
func (c *MembersHasMemberCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MembersHasMemberCall) IfNoneMatch ¶
func (c *MembersHasMemberCall) IfNoneMatch(entityTag string) *MembersHasMemberCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MembersInsertCall ¶
type MembersInsertCall struct {
	// contains filtered or unexported fields
}
func (*MembersInsertCall) Context ¶
func (c *MembersInsertCall) Context(ctx context.Context) *MembersInsertCall

Context sets the context to be used in this call's Do method.

func (*MembersInsertCall) Do ¶
func (c *MembersInsertCall) Do(opts ...googleapi.CallOption) (*Member, error)

Do executes the "directory.members.insert" call. Any non-2xx status code is an error. Response headers are in either *Member.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersInsertCall) Fields ¶
func (c *MembersInsertCall) Fields(s ...googleapi.Field) *MembersInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersInsertCall) Header ¶
func (c *MembersInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MembersListCall ¶
type MembersListCall struct {
	// contains filtered or unexported fields
}
func (*MembersListCall) Context ¶
func (c *MembersListCall) Context(ctx context.Context) *MembersListCall

Context sets the context to be used in this call's Do method.

func (*MembersListCall) Do ¶
func (c *MembersListCall) Do(opts ...googleapi.CallOption) (*Members, error)

Do executes the "directory.members.list" call. Any non-2xx status code is an error. Response headers are in either *Members.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersListCall) Fields ¶
func (c *MembersListCall) Fields(s ...googleapi.Field) *MembersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersListCall) Header ¶
func (c *MembersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MembersListCall) IfNoneMatch ¶
func (c *MembersListCall) IfNoneMatch(entityTag string) *MembersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MembersListCall) IncludeDerivedMembership ¶
func (c *MembersListCall) IncludeDerivedMembership(includeDerivedMembership bool) *MembersListCall

IncludeDerivedMembership sets the optional parameter "includeDerivedMembership": Whether to list indirect memberships. Default: false.

func (*MembersListCall) MaxResults ¶
func (c *MembersListCall) MaxResults(maxResults int64) *MembersListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return. Max allowed value is 200.

func (*MembersListCall) PageToken ¶
func (c *MembersListCall) PageToken(pageToken string) *MembersListCall

PageToken sets the optional parameter "pageToken": Token to specify next page in the list.

func (*MembersListCall) Pages ¶
func (c *MembersListCall) Pages(ctx context.Context, f func(*Members) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*MembersListCall) Roles ¶
func (c *MembersListCall) Roles(roles string) *MembersListCall

Roles sets the optional parameter "roles": The `roles` query parameter allows you to retrieve group members by role. Allowed values are `OWNER`, `MANAGER`, and `MEMBER`.

type MembersPatchCall ¶
type MembersPatchCall struct {
	// contains filtered or unexported fields
}
func (*MembersPatchCall) Context ¶
func (c *MembersPatchCall) Context(ctx context.Context) *MembersPatchCall

Context sets the context to be used in this call's Do method.

func (*MembersPatchCall) Do ¶
func (c *MembersPatchCall) Do(opts ...googleapi.CallOption) (*Member, error)

Do executes the "directory.members.patch" call. Any non-2xx status code is an error. Response headers are in either *Member.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersPatchCall) Fields ¶
func (c *MembersPatchCall) Fields(s ...googleapi.Field) *MembersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersPatchCall) Header ¶
func (c *MembersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MembersService ¶
type MembersService struct {
	// contains filtered or unexported fields
}
func NewMembersService ¶
func NewMembersService(s *Service) *MembersService
func (*MembersService) Delete ¶
func (r *MembersService) Delete(groupKey string, memberKey string) *MembersDeleteCall

Delete: Removes a member from a group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
memberKey: Identifies the group member in the API request. A group member can be a user or another group. The value can be the member's (group or user) primary email address, alias, or unique ID.
func (*MembersService) Get ¶
func (r *MembersService) Get(groupKey string, memberKey string) *MembersGetCall

Get: Retrieves a group member's properties.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
memberKey: Identifies the group member in the API request. A group member can be a user or another group. The value can be the member's (group or user) primary email address, alias, or unique ID.
func (*MembersService) HasMember ¶
func (r *MembersService) HasMember(groupKey string, memberKey string) *MembersHasMemberCall

HasMember: Checks whether the given user is a member of the group. Membership can be direct or nested, but if nested, the `memberKey` and `groupKey` must be entities in the same domain or an `Invalid input` error is returned. To check for nested memberships that include entities outside of the group's domain, use the `checkTransitiveMembership()` (https://cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/checkTransitiveMembership) method in the Cloud Identity Groups API.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
memberKey: Identifies the user member in the API request. The value can be the user's primary email address, alias, or unique ID.
func (*MembersService) Insert ¶
func (r *MembersService) Insert(groupKey string, member *Member) *MembersInsertCall

Insert: Adds a user to the specified group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*MembersService) List ¶
func (r *MembersService) List(groupKey string) *MembersListCall

List: Retrieves a paginated list of all members in a group. This method times out after 60 minutes. For more information, see Troubleshoot error codes (https://developers.google.com/workspace/admin/directory/v1/guides/troubleshoot-error-codes).

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
func (*MembersService) Patch ¶
func (r *MembersService) Patch(groupKey string, memberKey string, member *Member) *MembersPatchCall

Patch: Updates the membership properties of a user in the specified group. This method supports patch semantics (https://developers.google.com/workspace/admin/directory/v1/guides/performance#patch).

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
memberKey: Identifies the group member in the API request. A group member can be a user or another group. The value can be the member's (group or user) primary email address, alias, or unique ID.
func (*MembersService) Update ¶
func (r *MembersService) Update(groupKey string, memberKey string, member *Member) *MembersUpdateCall

Update: Updates the membership of a user in the specified group.

groupKey: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.
memberKey: Identifies the group member in the API request. A group member can be a user or another group. The value can be the member's (group or user) primary email address, alias, or unique ID.
type MembersUpdateCall ¶
type MembersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MembersUpdateCall) Context ¶
func (c *MembersUpdateCall) Context(ctx context.Context) *MembersUpdateCall

Context sets the context to be used in this call's Do method.

func (*MembersUpdateCall) Do ¶
func (c *MembersUpdateCall) Do(opts ...googleapi.CallOption) (*Member, error)

Do executes the "directory.members.update" call. Any non-2xx status code is an error. Response headers are in either *Member.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MembersUpdateCall) Fields ¶
func (c *MembersUpdateCall) Fields(s ...googleapi.Field) *MembersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MembersUpdateCall) Header ¶
func (c *MembersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MobileDevice ¶
type MobileDevice struct {
	// AdbStatus: Adb (USB debugging) enabled or disabled on device (Read-only)
	AdbStatus bool `json:"adbStatus,omitempty"`
	// Applications: The list of applications installed on an Android mobile
	// device. It is not applicable to Google Sync and iOS devices. The list
	// includes any Android applications that access Google Workspace data. When
	// updating an applications list, it is important to note that updates replace
	// the existing list. If the Android device has two existing applications and
	// the API updates the list with five applications, the is now the updated list
	// of five applications.
	Applications []*MobileDeviceApplications `json:"applications,omitempty"`
	// BasebandVersion: The device's baseband version.
	BasebandVersion string `json:"basebandVersion,omitempty"`
	// BootloaderVersion: Mobile Device Bootloader version (Read-only)
	BootloaderVersion string `json:"bootloaderVersion,omitempty"`
	// Brand: Mobile Device Brand (Read-only)
	Brand string `json:"brand,omitempty"`
	// BuildNumber: The device's operating system build number.
	BuildNumber string `json:"buildNumber,omitempty"`
	// DefaultLanguage: The default locale used on the device.
	DefaultLanguage string `json:"defaultLanguage,omitempty"`
	// DeveloperOptionsStatus: Developer options enabled or disabled on device
	// (Read-only)
	DeveloperOptionsStatus bool `json:"developerOptionsStatus,omitempty"`
	// DeviceCompromisedStatus: The compromised device status.
	DeviceCompromisedStatus string `json:"deviceCompromisedStatus,omitempty"`
	// DeviceId: The serial number for a Google Sync mobile device. For Android and
	// iOS devices, this is a software generated unique identifier.
	DeviceId string `json:"deviceId,omitempty"`
	// DevicePasswordStatus: DevicePasswordStatus (Read-only)
	DevicePasswordStatus string `json:"devicePasswordStatus,omitempty"`
	// Email: The list of the owner's email addresses. If your application needs
	// the current list of user emails, use the get
	// (https://developers.google.com/workspace/admin/directory/v1/reference/mobiledevices/get.html)
	// method. For additional information, see the retrieve a user
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#get_user)
	// method.
	Email []string `json:"email,omitempty"`
	// EncryptionStatus: Mobile Device Encryption Status (Read-only)
	EncryptionStatus string `json:"encryptionStatus,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// FirstSync: Date and time the device was first synchronized with the policy
	// settings in the G Suite administrator control panel (Read-only)
	FirstSync string `json:"firstSync,omitempty"`
	// Hardware: Mobile Device Hardware (Read-only)
	Hardware string `json:"hardware,omitempty"`
	// HardwareId: The IMEI/MEID unique identifier for Android hardware. It is not
	// applicable to Google Sync devices. When adding an Android mobile device,
	// this is an optional property. When updating one of these devices, this is a
	// read-only property.
	HardwareId string `json:"hardwareId,omitempty"`
	// Imei: The device's IMEI number.
	Imei string `json:"imei,omitempty"`
	// KernelVersion: The device's kernel version.
	KernelVersion string `json:"kernelVersion,omitempty"`
	// Kind: The type of the API resource. For Mobiledevices resources, the value
	// is `admin#directory#mobiledevice`.
	Kind string `json:"kind,omitempty"`
	// LastSync: Date and time the device was last synchronized with the policy
	// settings in the G Suite administrator control panel (Read-only)
	LastSync string `json:"lastSync,omitempty"`
	// ManagedAccountIsOnOwnerProfile: Boolean indicating if this account is on
	// owner/primary profile or not.
	ManagedAccountIsOnOwnerProfile bool `json:"managedAccountIsOnOwnerProfile,omitempty"`
	// Manufacturer: Mobile Device manufacturer (Read-only)
	Manufacturer string `json:"manufacturer,omitempty"`
	// Meid: The device's MEID number.
	Meid string `json:"meid,omitempty"`
	// Model: The mobile device's model name, for example Nexus S. This property
	// can be updated
	// (https://developers.google.com/workspace/admin/directory/v1/reference/mobiledevices/update.html).
	// For more information, see the Developer's Guide
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-mobile=devices#update_mobile_device).
	Model string `json:"model,omitempty"`
	// Name: The list of the owner's user names. If your application needs the
	// current list of device owner names, use the get
	// (https://developers.google.com/workspace/admin/directory/v1/reference/mobiledevices/get.html)
	// method. For more information about retrieving mobile device user
	// information, see the Developer's Guide
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#get_user).
	Name []string `json:"name,omitempty"`
	// NetworkOperator: Mobile Device mobile or network operator (if available)
	// (Read-only)
	NetworkOperator string `json:"networkOperator,omitempty"`
	// Os: The mobile device's operating system, for example IOS 4.3 or Android
	// 2.3.5. This property can be updated
	// (https://developers.google.com/workspace/admin/directory/v1/reference/mobiledevices/update.html).
	// For more information, see the Developer's Guide
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-mobile-devices#update_mobile_device).
	Os string `json:"os,omitempty"`
	// OtherAccountsInfo: The list of accounts added on device (Read-only)
	OtherAccountsInfo []string `json:"otherAccountsInfo,omitempty"`
	// Privilege: DMAgentPermission (Read-only)
	Privilege string `json:"privilege,omitempty"`
	// ReleaseVersion: Mobile Device release version version (Read-only)
	ReleaseVersion string `json:"releaseVersion,omitempty"`
	// ResourceId: The unique ID the API service uses to identify the mobile
	// device.
	ResourceId string `json:"resourceId,omitempty"`
	// SecurityPatchLevel: Mobile Device Security patch level (Read-only)
	SecurityPatchLevel int64 `json:"securityPatchLevel,omitempty,string"`
	// SerialNumber: The device's serial number.
	SerialNumber string `json:"serialNumber,omitempty"`
	// Status: The device's status.
	Status string `json:"status,omitempty"`
	// SupportsWorkProfile: Work profile supported on device (Read-only)
	SupportsWorkProfile bool `json:"supportsWorkProfile,omitempty"`
	// Type: The type of mobile device.
	Type string `json:"type,omitempty"`
	// UnknownSourcesStatus: Unknown sources enabled or disabled on device
	// (Read-only)
	UnknownSourcesStatus bool `json:"unknownSourcesStatus,omitempty"`
	// UserAgent: Gives information about the device such as `os` version. This
	// property can be updated
	// (https://developers.google.com/workspace/admin/directory/v1/reference/mobiledevices/update.html).
	// For more information, see the Developer's Guide
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-mobile-devices#update_mobile_device).
	UserAgent string `json:"userAgent,omitempty"`
	// WifiMacAddress: The device's MAC address on Wi-Fi networks.
	WifiMacAddress string `json:"wifiMacAddress,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdbStatus") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdbStatus") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MobileDevice: Google Workspace Mobile Management includes Android, Google Sync (https://support.google.com/a/answer/135937), and iOS devices. For more information about common group mobile device API tasks, see the Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-mobile-devices.html).

func (MobileDevice) MarshalJSON ¶
func (s MobileDevice) MarshalJSON() ([]byte, error)
type MobileDeviceAction ¶
type MobileDeviceAction struct {
	// Action: The action to be performed on the device.
	Action string `json:"action,omitempty"`
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
func (MobileDeviceAction) MarshalJSON ¶
func (s MobileDeviceAction) MarshalJSON() ([]byte, error)
type MobileDeviceApplications ¶
type MobileDeviceApplications struct {
	// DisplayName: The application's display name. An example is `Browser`.
	DisplayName string `json:"displayName,omitempty"`
	// PackageName: The application's package name. An example is
	// `com.android.browser`.
	PackageName string `json:"packageName,omitempty"`
	// Permission: The list of permissions of this application. These can be either
	// a standard Android permission or one defined by the application, and are
	// found in an application's Android manifest
	// (https://developer.android.com/guide/topics/manifest/uses-permission-element.html).
	// Examples of a Calendar application's permissions are `READ_CALENDAR`, or
	// `MANAGE_ACCOUNTS`.
	Permission []string `json:"permission,omitempty"`
	// VersionCode: The application's version code. An example is `13`.
	VersionCode int64 `json:"versionCode,omitempty"`
	// VersionName: The application's version name. An example is `3.2-140714`.
	VersionName string `json:"versionName,omitempty"`
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
func (MobileDeviceApplications) MarshalJSON ¶
func (s MobileDeviceApplications) MarshalJSON() ([]byte, error)
type MobileDevices ¶
type MobileDevices struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// Mobiledevices: A list of Mobile Device objects.
	Mobiledevices []*MobileDevice `json:"mobiledevices,omitempty"`
	// NextPageToken: Token used to access next page of this result.
	NextPageToken string `json:"nextPageToken,omitempty"`

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
func (MobileDevices) MarshalJSON ¶
func (s MobileDevices) MarshalJSON() ([]byte, error)
type MobiledevicesActionCall ¶
type MobiledevicesActionCall struct {
	// contains filtered or unexported fields
}
func (*MobiledevicesActionCall) Context ¶
func (c *MobiledevicesActionCall) Context(ctx context.Context) *MobiledevicesActionCall

Context sets the context to be used in this call's Do method.

func (*MobiledevicesActionCall) Do ¶
func (c *MobiledevicesActionCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.mobiledevices.action" call.

func (*MobiledevicesActionCall) Fields ¶
func (c *MobiledevicesActionCall) Fields(s ...googleapi.Field) *MobiledevicesActionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MobiledevicesActionCall) Header ¶
func (c *MobiledevicesActionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MobiledevicesDeleteCall ¶
type MobiledevicesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MobiledevicesDeleteCall) Context ¶
func (c *MobiledevicesDeleteCall) Context(ctx context.Context) *MobiledevicesDeleteCall

Context sets the context to be used in this call's Do method.

func (*MobiledevicesDeleteCall) Do ¶
func (c *MobiledevicesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.mobiledevices.delete" call.

func (*MobiledevicesDeleteCall) Fields ¶
func (c *MobiledevicesDeleteCall) Fields(s ...googleapi.Field) *MobiledevicesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MobiledevicesDeleteCall) Header ¶
func (c *MobiledevicesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MobiledevicesGetCall ¶
type MobiledevicesGetCall struct {
	// contains filtered or unexported fields
}
func (*MobiledevicesGetCall) Context ¶
func (c *MobiledevicesGetCall) Context(ctx context.Context) *MobiledevicesGetCall

Context sets the context to be used in this call's Do method.

func (*MobiledevicesGetCall) Do ¶
func (c *MobiledevicesGetCall) Do(opts ...googleapi.CallOption) (*MobileDevice, error)

Do executes the "directory.mobiledevices.get" call. Any non-2xx status code is an error. Response headers are in either *MobileDevice.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MobiledevicesGetCall) Fields ¶
func (c *MobiledevicesGetCall) Fields(s ...googleapi.Field) *MobiledevicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MobiledevicesGetCall) Header ¶
func (c *MobiledevicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MobiledevicesGetCall) IfNoneMatch ¶
func (c *MobiledevicesGetCall) IfNoneMatch(entityTag string) *MobiledevicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MobiledevicesGetCall) Projection ¶
func (c *MobiledevicesGetCall) Projection(projection string) *MobiledevicesGetCall

Projection sets the optional parameter "projection": Restrict information returned to a set of selected fields.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId, model,


status, type, and status)

"FULL" - Includes all metadata fields

type MobiledevicesListCall ¶
type MobiledevicesListCall struct {
	// contains filtered or unexported fields
}
func (*MobiledevicesListCall) Context ¶
func (c *MobiledevicesListCall) Context(ctx context.Context) *MobiledevicesListCall

Context sets the context to be used in this call's Do method.

func (*MobiledevicesListCall) Do ¶
func (c *MobiledevicesListCall) Do(opts ...googleapi.CallOption) (*MobileDevices, error)

Do executes the "directory.mobiledevices.list" call. Any non-2xx status code is an error. Response headers are in either *MobileDevices.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MobiledevicesListCall) Fields ¶
func (c *MobiledevicesListCall) Fields(s ...googleapi.Field) *MobiledevicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MobiledevicesListCall) Header ¶
func (c *MobiledevicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MobiledevicesListCall) IfNoneMatch ¶
func (c *MobiledevicesListCall) IfNoneMatch(entityTag string) *MobiledevicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MobiledevicesListCall) MaxResults ¶
func (c *MobiledevicesListCall) MaxResults(maxResults int64) *MobiledevicesListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return. Max allowed value is 100.

func (*MobiledevicesListCall) OrderBy ¶
func (c *MobiledevicesListCall) OrderBy(orderBy string) *MobiledevicesListCall

OrderBy sets the optional parameter "orderBy": Device property to use for sorting results.

Possible values:

"deviceId" - The serial number for a Google Sync mobile device. For


Android devices, this is a software generated unique identifier.

"email" - The device owner's email address.
"lastSync" - Last policy settings sync date time of the device.
"model" - The mobile device's model.
"name" - The device owner's user name.
"os" - The device's operating system.
"status" - The device status.
"type" - Type of the device.

func (*MobiledevicesListCall) PageToken ¶
func (c *MobiledevicesListCall) PageToken(pageToken string) *MobiledevicesListCall

PageToken sets the optional parameter "pageToken": Token to specify next page in the list

func (*MobiledevicesListCall) Pages ¶
func (c *MobiledevicesListCall) Pages(ctx context.Context, f func(*MobileDevices) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*MobiledevicesListCall) Projection ¶
func (c *MobiledevicesListCall) Projection(projection string) *MobiledevicesListCall

Projection sets the optional parameter "projection": Restrict information returned to a set of selected fields.

Possible values:

"BASIC" - Includes only the basic metadata fields (e.g., deviceId, model,


status, type, and status)

"FULL" - Includes all metadata fields

func (*MobiledevicesListCall) Query ¶
func (c *MobiledevicesListCall) Query(query string) *MobiledevicesListCall

Query sets the optional parameter "query": Search string in the format given at https://developers.google.com/workspace/admin/directory/v1/search-operators

func (*MobiledevicesListCall) SortOrder ¶
func (c *MobiledevicesListCall) SortOrder(sortOrder string) *MobiledevicesListCall

SortOrder sets the optional parameter "sortOrder": Whether to return results in ascending or descending order. Must be used with the `orderBy` parameter.

Possible values:

"ASCENDING" - Ascending order.
"DESCENDING" - Descending order.

type MobiledevicesService ¶
type MobiledevicesService struct {
	// contains filtered or unexported fields
}
func NewMobiledevicesService ¶
func NewMobiledevicesService(s *Service) *MobiledevicesService
func (*MobiledevicesService) Action ¶
func (r *MobiledevicesService) Action(customerId string, resourceId string, mobiledeviceaction *MobileDeviceAction) *MobiledevicesActionCall

Action: Takes an action that affects a mobile device. For example, remotely wiping a device.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
resourceId: The unique ID the API service uses to identify the mobile device.
func (*MobiledevicesService) Delete ¶
func (r *MobiledevicesService) Delete(customerId string, resourceId string) *MobiledevicesDeleteCall

Delete: Removes a mobile device.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
resourceId: The unique ID the API service uses to identify the mobile device.
func (*MobiledevicesService) Get ¶
func (r *MobiledevicesService) Get(customerId string, resourceId string) *MobiledevicesGetCall

Get: Retrieves a mobile device's properties.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
resourceId: The unique ID the API service uses to identify the mobile device.
func (*MobiledevicesService) List ¶
func (r *MobiledevicesService) List(customerId string) *MobiledevicesListCall

List: Retrieves a paginated list of all user-owned mobile devices for an account. To retrieve a list that includes company-owned devices, use the Cloud Identity Devices API (https://cloud.google.com/identity/docs/concepts/overview-devices) instead. This method times out after 60 minutes. For more information, see Troubleshoot error codes (https://developers.google.com/workspace/admin/directory/v1/guides/troubleshoot-error-codes).

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
type OrgUnit ¶
type OrgUnit struct {
	// BlockInheritance: This field is deprecated and setting its value has no
	// effect.
	BlockInheritance bool `json:"blockInheritance,omitempty"`
	// Description: Description of the organizational unit.
	Description string `json:"description,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the API resource. For Orgunits resources, the value is
	// `admin#directory#orgUnit`.
	Kind string `json:"kind,omitempty"`
	// Name: The organizational unit's path name. For example, an organizational
	// unit's name within the /corp/support/sales_support parent path is
	// sales_support. Required.
	Name string `json:"name,omitempty"`
	// OrgUnitId: The unique ID of the organizational unit.
	OrgUnitId string `json:"orgUnitId,omitempty"`
	// OrgUnitPath: The full path to the organizational unit. The `orgUnitPath` is
	// a derived property. When listed, it is derived from `parentOrgunitPath` and
	// organizational unit's `name`. For example, for an organizational unit named
	// 'apps' under parent organization '/engineering', the orgUnitPath is
	// '/engineering/apps'. In order to edit an `orgUnitPath`, either update the
	// name of the organization or the `parentOrgunitPath`. A user's organizational
	// unit determines which Google Workspace services the user has access to. If
	// the user is moved to a new organization, the user's access changes. For more
	// information about organization structures, see the administration help
	// center (https://support.google.com/a/answer/4352075). For more information
	// about moving a user to a different organization, see Update a user
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users.html#update_user).
	OrgUnitPath string `json:"orgUnitPath,omitempty"`
	// ParentOrgUnitId: The unique ID of the parent organizational unit. Required,
	// unless `parentOrgUnitPath` is set.
	ParentOrgUnitId string `json:"parentOrgUnitId,omitempty"`
	// ParentOrgUnitPath: The organizational unit's parent path. For example,
	// /corp/sales is the parent path for /corp/sales/sales_support organizational
	// unit. Required, unless `parentOrgUnitId` is set.
	ParentOrgUnitPath string `json:"parentOrgUnitPath,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BlockInheritance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BlockInheritance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OrgUnit: Managing your account's organizational units allows you to configure your users' access to services and custom settings. For more information about common organizational unit tasks, see the Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-org-units.html). The customer's organizational unit hierarchy is limited to 35 levels of depth.

func (OrgUnit) MarshalJSON ¶
func (s OrgUnit) MarshalJSON() ([]byte, error)
type OrgUnits ¶
type OrgUnits struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the API resource. For Org Unit resources, the type is
	// `admin#directory#orgUnits`.
	Kind string `json:"kind,omitempty"`
	// OrganizationUnits: A list of organizational unit objects.
	OrganizationUnits []*OrgUnit `json:"organizationUnits,omitempty"`

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
func (OrgUnits) MarshalJSON ¶
func (s OrgUnits) MarshalJSON() ([]byte, error)
type OrgunitsDeleteCall ¶
type OrgunitsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsDeleteCall) Context ¶
func (c *OrgunitsDeleteCall) Context(ctx context.Context) *OrgunitsDeleteCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsDeleteCall) Do ¶
func (c *OrgunitsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.orgunits.delete" call.

func (*OrgunitsDeleteCall) Fields ¶
func (c *OrgunitsDeleteCall) Fields(s ...googleapi.Field) *OrgunitsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsDeleteCall) Header ¶
func (c *OrgunitsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrgunitsGetCall ¶
type OrgunitsGetCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsGetCall) Context ¶
func (c *OrgunitsGetCall) Context(ctx context.Context) *OrgunitsGetCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsGetCall) Do ¶
func (c *OrgunitsGetCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)

Do executes the "directory.orgunits.get" call. Any non-2xx status code is an error. Response headers are in either *OrgUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrgunitsGetCall) Fields ¶
func (c *OrgunitsGetCall) Fields(s ...googleapi.Field) *OrgunitsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsGetCall) Header ¶
func (c *OrgunitsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrgunitsGetCall) IfNoneMatch ¶
func (c *OrgunitsGetCall) IfNoneMatch(entityTag string) *OrgunitsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrgunitsInsertCall ¶
type OrgunitsInsertCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsInsertCall) Context ¶
func (c *OrgunitsInsertCall) Context(ctx context.Context) *OrgunitsInsertCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsInsertCall) Do ¶
func (c *OrgunitsInsertCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)

Do executes the "directory.orgunits.insert" call. Any non-2xx status code is an error. Response headers are in either *OrgUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrgunitsInsertCall) Fields ¶
func (c *OrgunitsInsertCall) Fields(s ...googleapi.Field) *OrgunitsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsInsertCall) Header ¶
func (c *OrgunitsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrgunitsListCall ¶
type OrgunitsListCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsListCall) Context ¶
func (c *OrgunitsListCall) Context(ctx context.Context) *OrgunitsListCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsListCall) Do ¶
func (c *OrgunitsListCall) Do(opts ...googleapi.CallOption) (*OrgUnits, error)

Do executes the "directory.orgunits.list" call. Any non-2xx status code is an error. Response headers are in either *OrgUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrgunitsListCall) Fields ¶
func (c *OrgunitsListCall) Fields(s ...googleapi.Field) *OrgunitsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsListCall) Header ¶
func (c *OrgunitsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrgunitsListCall) IfNoneMatch ¶
func (c *OrgunitsListCall) IfNoneMatch(entityTag string) *OrgunitsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrgunitsListCall) OrgUnitPath ¶
func (c *OrgunitsListCall) OrgUnitPath(orgUnitPath string) *OrgunitsListCall

OrgUnitPath sets the optional parameter "orgUnitPath": The full path to the organizational unit or its unique ID. Returns the children of the specified organizational unit.

func (*OrgunitsListCall) Type ¶
func (c *OrgunitsListCall) Type(type_ string) *OrgunitsListCall

Type sets the optional parameter "type": Whether to return all sub-organizations or just immediate children.

Possible values:

"all" - All sub-organizational units.
"children" - Immediate children only (default).
"allIncludingParent" - All sub-organizational units and the specified


organizational unit (root if not specified).

type OrgunitsPatchCall ¶
type OrgunitsPatchCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsPatchCall) Context ¶
func (c *OrgunitsPatchCall) Context(ctx context.Context) *OrgunitsPatchCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsPatchCall) Do ¶
func (c *OrgunitsPatchCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)

Do executes the "directory.orgunits.patch" call. Any non-2xx status code is an error. Response headers are in either *OrgUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrgunitsPatchCall) Fields ¶
func (c *OrgunitsPatchCall) Fields(s ...googleapi.Field) *OrgunitsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsPatchCall) Header ¶
func (c *OrgunitsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrgunitsService ¶
type OrgunitsService struct {
	// contains filtered or unexported fields
}
func NewOrgunitsService ¶
func NewOrgunitsService(s *Service) *OrgunitsService
func (*OrgunitsService) Delete ¶
func (r *OrgunitsService) Delete(customerId string, orgUnitPath string) *OrgunitsDeleteCall

Delete: Removes an organizational unit.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
orgUnitPath: The full path of the organizational unit (minus the leading `/`) or its unique ID.
func (*OrgunitsService) Get ¶
func (r *OrgunitsService) Get(customerId string, orgUnitPath string) *OrgunitsGetCall

Get: Retrieves an organizational unit.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
orgUnitPath: The full path of the organizational unit (minus the leading `/`) or its unique ID.
func (*OrgunitsService) Insert ¶
func (r *OrgunitsService) Insert(customerId string, orgunit *OrgUnit) *OrgunitsInsertCall

Insert: Adds an organizational unit.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
func (*OrgunitsService) List ¶
func (r *OrgunitsService) List(customerId string) *OrgunitsListCall

List: Retrieves a list of all organizational units for an account.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
func (*OrgunitsService) Patch ¶
func (r *OrgunitsService) Patch(customerId string, orgUnitPath string, orgunit *OrgUnit) *OrgunitsPatchCall

Patch: Updates an organizational unit. This method supports patch semantics (https://developers.google.com/workspace/admin/directory/v1/guides/performance#patch)

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
orgUnitPath: The full path of the organizational unit (minus the leading `/`) or its unique ID.
func (*OrgunitsService) Update ¶
func (r *OrgunitsService) Update(customerId string, orgUnitPath string, orgunit *OrgUnit) *OrgunitsUpdateCall

Update: Updates an organizational unit.

customerId: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users resource (https://developers.google.com/workspace/admin/directory/v1/reference/users).
orgUnitPath: The full path of the organizational unit (minus the leading `/`) or its unique ID.
type OrgunitsUpdateCall ¶
type OrgunitsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*OrgunitsUpdateCall) Context ¶
func (c *OrgunitsUpdateCall) Context(ctx context.Context) *OrgunitsUpdateCall

Context sets the context to be used in this call's Do method.

func (*OrgunitsUpdateCall) Do ¶
func (c *OrgunitsUpdateCall) Do(opts ...googleapi.CallOption) (*OrgUnit, error)

Do executes the "directory.orgunits.update" call. Any non-2xx status code is an error. Response headers are in either *OrgUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrgunitsUpdateCall) Fields ¶
func (c *OrgunitsUpdateCall) Fields(s ...googleapi.Field) *OrgunitsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrgunitsUpdateCall) Header ¶
func (c *OrgunitsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OsUpdateStatus ¶
added in v0.92.0
type OsUpdateStatus struct {
	// RebootTime: Date and time of the last reboot.
	RebootTime string `json:"rebootTime,omitempty"`
	// State: The update state of an OS update.
	//
	// Possible values:
	//   "updateStateUnspecified" - The update state is unspecified.
	//   "updateStateNotStarted" - There is an update pending but it hasn't
	// started.
	//   "updateStateDownloadInProgress" - The pending update is being downloaded.
	//   "updateStateNeedReboot" - The device is ready to install the update, but
	// must reboot.
	State string `json:"state,omitempty"`
	// TargetKioskAppVersion: New required platform version from the pending
	// updated kiosk app.
	TargetKioskAppVersion string `json:"targetKioskAppVersion,omitempty"`
	// TargetOsVersion: New platform version of the OS image being downloaded and
	// applied. It is only set when update status is
	// UPDATE_STATUS_DOWNLOAD_IN_PROGRESS or UPDATE_STATUS_NEED_REBOOT. Note this
	// could be a dummy "0.0.0.0" for UPDATE_STATUS_NEED_REBOOT for some edge
	// cases, e.g. update engine is restarted without a reboot.
	TargetOsVersion string `json:"targetOsVersion,omitempty"`
	// UpdateCheckTime: Date and time of the last update check.
	UpdateCheckTime string `json:"updateCheckTime,omitempty"`
	// UpdateTime: Date and time of the last successful OS update.
	UpdateTime string `json:"updateTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RebootTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RebootTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OsUpdateStatus: Contains information regarding the current OS update status.

func (OsUpdateStatus) MarshalJSON ¶
added in v0.92.0
func (s OsUpdateStatus) MarshalJSON() ([]byte, error)
type PrintServer ¶
added in v0.98.0
type PrintServer struct {
	// CreateTime: Output only. Time when the print server was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Editable. Description of the print server (as shown in the
	// Admin console).
	Description string `json:"description,omitempty"`
	// DisplayName: Editable. Display name of the print server (as shown in the
	// Admin console).
	DisplayName string `json:"displayName,omitempty"`
	// Id: Immutable. ID of the print server. Leave empty when creating.
	Id string `json:"id,omitempty"`
	// Name: Identifier. Resource name of the print server. Leave empty when
	// creating. Format: `customers/{customer.id}/printServers/{print_server.id}`
	Name string `json:"name,omitempty"`
	// OrgUnitId: ID of the organization unit (OU) that owns this print server.
	// This value can only be set when the print server is initially created. If
	// it's not populated, the print server is placed under the root OU. The
	// `org_unit_id` can be retrieved using the Directory API
	// (https://developers.google.com/workspace/admin/directory/reference/rest/v1/orgunits).
	OrgUnitId string `json:"orgUnitId,omitempty"`
	// Uri: Editable. Print server URI.
	Uri string `json:"uri,omitempty"`

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

PrintServer: Configuration for a print server.

func (PrintServer) MarshalJSON ¶
added in v0.98.0
func (s PrintServer) MarshalJSON() ([]byte, error)
type PrintServerFailureInfo ¶
added in v0.98.0
type PrintServerFailureInfo struct {
	// ErrorCode: Canonical code for why the update failed to apply.
	//
	// Possible values:
	//   "OK" - Not an error; returned on success. HTTP Mapping: 200 OK
	//   "CANCELLED" - The operation was cancelled, typically by the caller. HTTP
	// Mapping: 499 Client Closed Request
	//   "UNKNOWN" - Unknown error. For example, this error may be returned when a
	// `Status` value received from another address space belongs to an error space
	// that is not known in this address space. Also errors raised by APIs that do
	// not return enough error information may be converted to this error. HTTP
	// Mapping: 500 Internal Server Error
	//   "INVALID_ARGUMENT" - The client specified an invalid argument. Note that
	// this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates
	// arguments that are problematic regardless of the state of the system (e.g.,
	// a malformed file name). HTTP Mapping: 400 Bad Request
	//   "DEADLINE_EXCEEDED" - The deadline expired before the operation could
	// complete. For operations that change the state of the system, this error may
	// be returned even if the operation has completed successfully. For example, a
	// successful response from a server could have been delayed long enough for
	// the deadline to expire. HTTP Mapping: 504 Gateway Timeout
	//   "NOT_FOUND" - Some requested entity (e.g., file or directory) was not
	// found. Note to server developers: if a request is denied for an entire class
	// of users, such as gradual feature rollout or undocumented allowlist,
	// `NOT_FOUND` may be used. If a request is denied for some users within a
	// class of users, such as user-based access control, `PERMISSION_DENIED` must
	// be used. HTTP Mapping: 404 Not Found
	//   "ALREADY_EXISTS" - The entity that a client attempted to create (e.g.,
	// file or directory) already exists. HTTP Mapping: 409 Conflict
	//   "PERMISSION_DENIED" - The caller does not have permission to execute the
	// specified operation. `PERMISSION_DENIED` must not be used for rejections
	// caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for
	// those errors). `PERMISSION_DENIED` must not be used if the caller can not be
	// identified (use `UNAUTHENTICATED` instead for those errors). This error code
	// does not imply the request is valid or the requested entity exists or
	// satisfies other pre-conditions. HTTP Mapping: 403 Forbidden
	//   "UNAUTHENTICATED" - The request does not have valid authentication
	// credentials for the operation. HTTP Mapping: 401 Unauthorized
	//   "RESOURCE_EXHAUSTED" - Some resource has been exhausted, perhaps a
	// per-user quota, or perhaps the entire file system is out of space. HTTP
	// Mapping: 429 Too Many Requests
	//   "FAILED_PRECONDITION" - The operation was rejected because the system is
	// not in a state required for the operation's execution. For example, the
	// directory to be deleted is non-empty, an rmdir operation is applied to a
	// non-directory, etc. Service implementors can use the following guidelines to
	// decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use
	// `UNAVAILABLE` if the client can retry just the failing call. (b) Use
	// `ABORTED` if the client should retry at a higher level. For example, when a
	// client-specified test-and-set fails, indicating the client should restart a
	// read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client
	// should not retry until the system state has been explicitly fixed. For
	// example, if an "rmdir" fails because the directory is non-empty,
	// `FAILED_PRECONDITION` should be returned since the client should not retry
	// unless the files are deleted from the directory. HTTP Mapping: 400 Bad
	// Request
	//   "ABORTED" - The operation was aborted, typically due to a concurrency
	// issue such as a sequencer check failure or transaction abort. See the
	// guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and
	// `UNAVAILABLE`. HTTP Mapping: 409 Conflict
	//   "OUT_OF_RANGE" - The operation was attempted past the valid range. E.g.,
	// seeking or reading past end-of-file. Unlike `INVALID_ARGUMENT`, this error
	// indicates a problem that may be fixed if the system state changes. For
	// example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to
	// read at an offset that is not in the range [0,2^32-1], but it will generate
	// `OUT_OF_RANGE` if asked to read from an offset past the current file size.
	// There is a fair bit of overlap between `FAILED_PRECONDITION` and
	// `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error)
	// when it applies so that callers who are iterating through a space can easily
	// look for an `OUT_OF_RANGE` error to detect when they are done. HTTP Mapping:
	// 400 Bad Request
	//   "UNIMPLEMENTED" - The operation is not implemented or is not
	// supported/enabled in this service. HTTP Mapping: 501 Not Implemented
	//   "INTERNAL" - Internal errors. This means that some invariants expected by
	// the underlying system have been broken. This error code is reserved for
	// serious errors. HTTP Mapping: 500 Internal Server Error
	//   "UNAVAILABLE" - The service is currently unavailable. This is most likely
	// a transient condition, which can be corrected by retrying with a backoff.
	// Note that it is not always safe to retry non-idempotent operations. See the
	// guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and
	// `UNAVAILABLE`. HTTP Mapping: 503 Service Unavailable
	//   "DATA_LOSS" - Unrecoverable data loss or corruption. HTTP Mapping: 500
	// Internal Server Error
	ErrorCode string `json:"errorCode,omitempty"`
	// ErrorMessage: Failure reason message.
	ErrorMessage string `json:"errorMessage,omitempty"`
	// PrintServer: Failed print server.
	PrintServer *PrintServer `json:"printServer,omitempty"`
	// PrintServerId: ID of a failed print server.
	PrintServerId string `json:"printServerId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ErrorCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ErrorCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrintServerFailureInfo: Info about failures

func (PrintServerFailureInfo) MarshalJSON ¶
added in v0.98.0
func (s PrintServerFailureInfo) MarshalJSON() ([]byte, error)
type Printer ¶
added in v0.42.0
type Printer struct {
	// AuxiliaryMessages: Output only. Auxiliary messages about issues with the
	// printer configuration if any.
	AuxiliaryMessages []*AuxiliaryMessage `json:"auxiliaryMessages,omitempty"`
	// CreateTime: Output only. Time when printer was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Editable. Description of printer.
	Description string `json:"description,omitempty"`
	// DisplayName: Editable. Name of printer.
	DisplayName string `json:"displayName,omitempty"`
	// Id: Id of the printer. (During printer creation leave empty)
	Id string `json:"id,omitempty"`
	// MakeAndModel: Editable. Make and model of printer. e.g. Lexmark MS610de
	// Value must be in format as seen in ListPrinterModels response.
	MakeAndModel string `json:"makeAndModel,omitempty"`
	// Name: Identifier. The resource name of the Printer object, in the format
	// customers/{customer-id}/printers/{printer-id} (During printer creation leave
	// empty)
	Name string `json:"name,omitempty"`
	// OrgUnitId: Organization Unit that owns this printer (Only can be set during
	// Printer creation)
	OrgUnitId string `json:"orgUnitId,omitempty"`
	// Uri: Editable. Printer URI.
	Uri string `json:"uri,omitempty"`
	// UseDriverlessConfig: Editable. flag to use driverless configuration or not.
	// If it's set to be true, make_and_model can be ignored
	UseDriverlessConfig bool `json:"useDriverlessConfig,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuxiliaryMessages") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuxiliaryMessages") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Printer: Printer configuration.

func (Printer) MarshalJSON ¶
added in v0.42.0
func (s Printer) MarshalJSON() ([]byte, error)
type PrinterModel ¶
added in v0.42.0
type PrinterModel struct {
	// DisplayName: Display name. eq. "Brother MFC-8840D"
	DisplayName string `json:"displayName,omitempty"`
	// MakeAndModel: Make and model as represented in "make_and_model" field in
	// Printer object. eq. "brother mfc-8840d"
	MakeAndModel string `json:"makeAndModel,omitempty"`
	// Manufacturer: Manufacturer. eq. "Brother"
	Manufacturer string `json:"manufacturer,omitempty"`
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

PrinterModel: Printer manufacturer and model

func (PrinterModel) MarshalJSON ¶
added in v0.42.0
func (s PrinterModel) MarshalJSON() ([]byte, error)
type Privilege ¶
type Privilege struct {
	// ChildPrivileges: A list of child privileges. Privileges for a service form a
	// tree. Each privilege can have a list of child privileges; this list is empty
	// for a leaf privilege.
	ChildPrivileges []*Privilege `json:"childPrivileges,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// IsOuScopable: If the privilege can be restricted to an organization unit.
	IsOuScopable bool `json:"isOuScopable,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#privilege`.
	Kind string `json:"kind,omitempty"`
	// PrivilegeName: The name of the privilege.
	PrivilegeName string `json:"privilegeName,omitempty"`
	// ServiceId: The obfuscated ID of the service this privilege is for. This
	// value is returned with `Privileges.list()`
	// (https://developers.google.com/workspace/admin/directory/v1/reference/privileges/list).
	ServiceId string `json:"serviceId,omitempty"`
	// ServiceName: The name of the service this privilege is for.
	ServiceName string `json:"serviceName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ChildPrivileges") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChildPrivileges") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (Privilege) MarshalJSON ¶
func (s Privilege) MarshalJSON() ([]byte, error)
type Privileges ¶
type Privileges struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of Privilege resources.
	Items []*Privilege `json:"items,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#privileges`.
	Kind string `json:"kind,omitempty"`

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
func (Privileges) MarshalJSON ¶
func (s Privileges) MarshalJSON() ([]byte, error)
type PrivilegesListCall ¶
type PrivilegesListCall struct {
	// contains filtered or unexported fields
}
func (*PrivilegesListCall) Context ¶
func (c *PrivilegesListCall) Context(ctx context.Context) *PrivilegesListCall

Context sets the context to be used in this call's Do method.

func (*PrivilegesListCall) Do ¶
func (c *PrivilegesListCall) Do(opts ...googleapi.CallOption) (*Privileges, error)

Do executes the "directory.privileges.list" call. Any non-2xx status code is an error. Response headers are in either *Privileges.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PrivilegesListCall) Fields ¶
func (c *PrivilegesListCall) Fields(s ...googleapi.Field) *PrivilegesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PrivilegesListCall) Header ¶
func (c *PrivilegesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PrivilegesListCall) IfNoneMatch ¶
func (c *PrivilegesListCall) IfNoneMatch(entityTag string) *PrivilegesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PrivilegesService ¶
type PrivilegesService struct {
	// contains filtered or unexported fields
}
func NewPrivilegesService ¶
func NewPrivilegesService(s *Service) *PrivilegesService
func (*PrivilegesService) List ¶
func (r *PrivilegesService) List(customer string) *PrivilegesListCall

List: Retrieves a paginated list of all privileges for a customer.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
type ResourcesBuildingsDeleteCall ¶
type ResourcesBuildingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsDeleteCall) Context ¶
func (c *ResourcesBuildingsDeleteCall) Context(ctx context.Context) *ResourcesBuildingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsDeleteCall) Do ¶
func (c *ResourcesBuildingsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.resources.buildings.delete" call.

func (*ResourcesBuildingsDeleteCall) Fields ¶
func (c *ResourcesBuildingsDeleteCall) Fields(s ...googleapi.Field) *ResourcesBuildingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsDeleteCall) Header ¶
func (c *ResourcesBuildingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesBuildingsGetCall ¶
type ResourcesBuildingsGetCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsGetCall) Context ¶
func (c *ResourcesBuildingsGetCall) Context(ctx context.Context) *ResourcesBuildingsGetCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsGetCall) Do ¶
func (c *ResourcesBuildingsGetCall) Do(opts ...googleapi.CallOption) (*Building, error)

Do executes the "directory.resources.buildings.get" call. Any non-2xx status code is an error. Response headers are in either *Building.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesBuildingsGetCall) Fields ¶
func (c *ResourcesBuildingsGetCall) Fields(s ...googleapi.Field) *ResourcesBuildingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsGetCall) Header ¶
func (c *ResourcesBuildingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesBuildingsGetCall) IfNoneMatch ¶
func (c *ResourcesBuildingsGetCall) IfNoneMatch(entityTag string) *ResourcesBuildingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ResourcesBuildingsInsertCall ¶
type ResourcesBuildingsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsInsertCall) Context ¶
func (c *ResourcesBuildingsInsertCall) Context(ctx context.Context) *ResourcesBuildingsInsertCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsInsertCall) CoordinatesSource ¶
added in v0.2.0
func (c *ResourcesBuildingsInsertCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsInsertCall

CoordinatesSource sets the optional parameter "coordinatesSource": Source from which Building.coordinates are derived.

Possible values:

"CLIENT_SPECIFIED" - Building.coordinates are set to the coordinates


included in the request.

"RESOLVED_FROM_ADDRESS" - Building.coordinates are automatically populated


based on the postal address.

"SOURCE_UNSPECIFIED" (default) - Defaults to `RESOLVED_FROM_ADDRESS` if


postal address is provided. Otherwise, defaults to `CLIENT_SPECIFIED` if coordinates are provided.

func (*ResourcesBuildingsInsertCall) Do ¶
func (c *ResourcesBuildingsInsertCall) Do(opts ...googleapi.CallOption) (*Building, error)

Do executes the "directory.resources.buildings.insert" call. Any non-2xx status code is an error. Response headers are in either *Building.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesBuildingsInsertCall) Fields ¶
func (c *ResourcesBuildingsInsertCall) Fields(s ...googleapi.Field) *ResourcesBuildingsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsInsertCall) Header ¶
func (c *ResourcesBuildingsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesBuildingsListCall ¶
type ResourcesBuildingsListCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsListCall) Context ¶
func (c *ResourcesBuildingsListCall) Context(ctx context.Context) *ResourcesBuildingsListCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsListCall) Do ¶
func (c *ResourcesBuildingsListCall) Do(opts ...googleapi.CallOption) (*Buildings, error)

Do executes the "directory.resources.buildings.list" call. Any non-2xx status code is an error. Response headers are in either *Buildings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesBuildingsListCall) Fields ¶
func (c *ResourcesBuildingsListCall) Fields(s ...googleapi.Field) *ResourcesBuildingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsListCall) Header ¶
func (c *ResourcesBuildingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesBuildingsListCall) IfNoneMatch ¶
func (c *ResourcesBuildingsListCall) IfNoneMatch(entityTag string) *ResourcesBuildingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ResourcesBuildingsListCall) MaxResults ¶
func (c *ResourcesBuildingsListCall) MaxResults(maxResults int64) *ResourcesBuildingsListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*ResourcesBuildingsListCall) PageToken ¶
func (c *ResourcesBuildingsListCall) PageToken(pageToken string) *ResourcesBuildingsListCall

PageToken sets the optional parameter "pageToken": Token to specify the next page in the list.

func (*ResourcesBuildingsListCall) Pages ¶
func (c *ResourcesBuildingsListCall) Pages(ctx context.Context, f func(*Buildings) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ResourcesBuildingsPatchCall ¶
type ResourcesBuildingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsPatchCall) Context ¶
func (c *ResourcesBuildingsPatchCall) Context(ctx context.Context) *ResourcesBuildingsPatchCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsPatchCall) CoordinatesSource ¶
added in v0.2.0
func (c *ResourcesBuildingsPatchCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsPatchCall

CoordinatesSource sets the optional parameter "coordinatesSource": Source from which Building.coordinates are derived.

Possible values:

"CLIENT_SPECIFIED" - Building.coordinates are set to the coordinates


included in the request.

"RESOLVED_FROM_ADDRESS" - Building.coordinates are automatically populated


based on the postal address.

"SOURCE_UNSPECIFIED" (default) - Defaults to `RESOLVED_FROM_ADDRESS` if


postal address is provided. Otherwise, defaults to `CLIENT_SPECIFIED` if coordinates are provided.

func (*ResourcesBuildingsPatchCall) Do ¶
func (c *ResourcesBuildingsPatchCall) Do(opts ...googleapi.CallOption) (*Building, error)

Do executes the "directory.resources.buildings.patch" call. Any non-2xx status code is an error. Response headers are in either *Building.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesBuildingsPatchCall) Fields ¶
func (c *ResourcesBuildingsPatchCall) Fields(s ...googleapi.Field) *ResourcesBuildingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsPatchCall) Header ¶
func (c *ResourcesBuildingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesBuildingsService ¶
type ResourcesBuildingsService struct {
	// contains filtered or unexported fields
}
func NewResourcesBuildingsService ¶
func NewResourcesBuildingsService(s *Service) *ResourcesBuildingsService
func (*ResourcesBuildingsService) Delete ¶
func (r *ResourcesBuildingsService) Delete(customer string, buildingId string) *ResourcesBuildingsDeleteCall

Delete: Deletes a building.

buildingId: The id of the building to delete.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesBuildingsService) Get ¶
func (r *ResourcesBuildingsService) Get(customer string, buildingId string) *ResourcesBuildingsGetCall

Get: Retrieves a building.

buildingId: The unique ID of the building to retrieve.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesBuildingsService) Insert ¶
func (r *ResourcesBuildingsService) Insert(customer string, building *Building) *ResourcesBuildingsInsertCall

Insert: Inserts a building.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesBuildingsService) List ¶
func (r *ResourcesBuildingsService) List(customer string) *ResourcesBuildingsListCall

List: Retrieves a list of buildings for an account.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesBuildingsService) Patch ¶
func (r *ResourcesBuildingsService) Patch(customer string, buildingId string, building *Building) *ResourcesBuildingsPatchCall

Patch: Patches a building.

buildingId: The id of the building to update.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesBuildingsService) Update ¶
func (r *ResourcesBuildingsService) Update(customer string, buildingId string, building *Building) *ResourcesBuildingsUpdateCall

Update: Updates a building.

buildingId: The id of the building to update.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
type ResourcesBuildingsUpdateCall ¶
type ResourcesBuildingsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesBuildingsUpdateCall) Context ¶
func (c *ResourcesBuildingsUpdateCall) Context(ctx context.Context) *ResourcesBuildingsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ResourcesBuildingsUpdateCall) CoordinatesSource ¶
added in v0.2.0
func (c *ResourcesBuildingsUpdateCall) CoordinatesSource(coordinatesSource string) *ResourcesBuildingsUpdateCall

CoordinatesSource sets the optional parameter "coordinatesSource": Source from which Building.coordinates are derived.

Possible values:

"CLIENT_SPECIFIED" - Building.coordinates are set to the coordinates


included in the request.

"RESOLVED_FROM_ADDRESS" - Building.coordinates are automatically populated


based on the postal address.

"SOURCE_UNSPECIFIED" (default) - Defaults to `RESOLVED_FROM_ADDRESS` if


postal address is provided. Otherwise, defaults to `CLIENT_SPECIFIED` if coordinates are provided.

func (*ResourcesBuildingsUpdateCall) Do ¶
func (c *ResourcesBuildingsUpdateCall) Do(opts ...googleapi.CallOption) (*Building, error)

Do executes the "directory.resources.buildings.update" call. Any non-2xx status code is an error. Response headers are in either *Building.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesBuildingsUpdateCall) Fields ¶
func (c *ResourcesBuildingsUpdateCall) Fields(s ...googleapi.Field) *ResourcesBuildingsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesBuildingsUpdateCall) Header ¶
func (c *ResourcesBuildingsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesCalendarsDeleteCall ¶
type ResourcesCalendarsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsDeleteCall) Context ¶
func (c *ResourcesCalendarsDeleteCall) Context(ctx context.Context) *ResourcesCalendarsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsDeleteCall) Do ¶
func (c *ResourcesCalendarsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.resources.calendars.delete" call.

func (*ResourcesCalendarsDeleteCall) Fields ¶
func (c *ResourcesCalendarsDeleteCall) Fields(s ...googleapi.Field) *ResourcesCalendarsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsDeleteCall) Header ¶
func (c *ResourcesCalendarsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesCalendarsGetCall ¶
type ResourcesCalendarsGetCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsGetCall) Context ¶
func (c *ResourcesCalendarsGetCall) Context(ctx context.Context) *ResourcesCalendarsGetCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsGetCall) Do ¶
func (c *ResourcesCalendarsGetCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)

Do executes the "directory.resources.calendars.get" call. Any non-2xx status code is an error. Response headers are in either *CalendarResource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesCalendarsGetCall) Fields ¶
func (c *ResourcesCalendarsGetCall) Fields(s ...googleapi.Field) *ResourcesCalendarsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsGetCall) Header ¶
func (c *ResourcesCalendarsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesCalendarsGetCall) IfNoneMatch ¶
func (c *ResourcesCalendarsGetCall) IfNoneMatch(entityTag string) *ResourcesCalendarsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ResourcesCalendarsInsertCall ¶
type ResourcesCalendarsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsInsertCall) Context ¶
func (c *ResourcesCalendarsInsertCall) Context(ctx context.Context) *ResourcesCalendarsInsertCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsInsertCall) Do ¶
func (c *ResourcesCalendarsInsertCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)

Do executes the "directory.resources.calendars.insert" call. Any non-2xx status code is an error. Response headers are in either *CalendarResource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesCalendarsInsertCall) Fields ¶
func (c *ResourcesCalendarsInsertCall) Fields(s ...googleapi.Field) *ResourcesCalendarsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsInsertCall) Header ¶
func (c *ResourcesCalendarsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesCalendarsListCall ¶
type ResourcesCalendarsListCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsListCall) Context ¶
func (c *ResourcesCalendarsListCall) Context(ctx context.Context) *ResourcesCalendarsListCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsListCall) Do ¶
func (c *ResourcesCalendarsListCall) Do(opts ...googleapi.CallOption) (*CalendarResources, error)

Do executes the "directory.resources.calendars.list" call. Any non-2xx status code is an error. Response headers are in either *CalendarResources.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesCalendarsListCall) Fields ¶
func (c *ResourcesCalendarsListCall) Fields(s ...googleapi.Field) *ResourcesCalendarsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsListCall) Header ¶
func (c *ResourcesCalendarsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesCalendarsListCall) IfNoneMatch ¶
func (c *ResourcesCalendarsListCall) IfNoneMatch(entityTag string) *ResourcesCalendarsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ResourcesCalendarsListCall) MaxResults ¶
func (c *ResourcesCalendarsListCall) MaxResults(maxResults int64) *ResourcesCalendarsListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*ResourcesCalendarsListCall) OrderBy ¶
func (c *ResourcesCalendarsListCall) OrderBy(orderBy string) *ResourcesCalendarsListCall

OrderBy sets the optional parameter "orderBy": Field(s) to sort results by in either ascending or descending order. Supported fields include `resourceId`, `resourceName`, `capacity`, `buildingId`, and `floorName`. If no order is specified, defaults to ascending. Should be of the form "field [asc|desc], field [asc|desc], ...". For example `buildingId, capacity desc` would return results sorted first by `buildingId` in ascending order then by `capacity` in descending order.

func (*ResourcesCalendarsListCall) PageToken ¶
func (c *ResourcesCalendarsListCall) PageToken(pageToken string) *ResourcesCalendarsListCall

PageToken sets the optional parameter "pageToken": Token to specify the next page in the list.

func (*ResourcesCalendarsListCall) Pages ¶
func (c *ResourcesCalendarsListCall) Pages(ctx context.Context, f func(*CalendarResources) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ResourcesCalendarsListCall) Query ¶
func (c *ResourcesCalendarsListCall) Query(query string) *ResourcesCalendarsListCall

Query sets the optional parameter "query": String query used to filter results. Contains one or more search clauses, each with a field, operator, and value. A field can be any of supported fields and operators can be any of supported operations. Operators include '=' for exact match, '!=' for mismatch and ':' for prefix match or HAS match where applicable. For prefix match, the value should always be followed by a *. Logical operators NOT and AND are supported (in this order of precedence). Supported fields include `generatedResourceName`, `name`, `buildingId`, `floor_name`, `capacity`, `featureInstances.feature.name`, `resourceEmail`, `resourceCategory`. For example `buildingId=US-NYC-9TH AND featureInstances.feature.name:Phone`.

type ResourcesCalendarsPatchCall ¶
type ResourcesCalendarsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsPatchCall) Context ¶
func (c *ResourcesCalendarsPatchCall) Context(ctx context.Context) *ResourcesCalendarsPatchCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsPatchCall) Do ¶
func (c *ResourcesCalendarsPatchCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)

Do executes the "directory.resources.calendars.patch" call. Any non-2xx status code is an error. Response headers are in either *CalendarResource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesCalendarsPatchCall) Fields ¶
func (c *ResourcesCalendarsPatchCall) Fields(s ...googleapi.Field) *ResourcesCalendarsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsPatchCall) Header ¶
func (c *ResourcesCalendarsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesCalendarsService ¶
type ResourcesCalendarsService struct {
	// contains filtered or unexported fields
}
func NewResourcesCalendarsService ¶
func NewResourcesCalendarsService(s *Service) *ResourcesCalendarsService
func (*ResourcesCalendarsService) Delete ¶
func (r *ResourcesCalendarsService) Delete(customer string, calendarResourceId string) *ResourcesCalendarsDeleteCall

Delete: Deletes a calendar resource.

calendarResourceId: The unique ID of the calendar resource to delete.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesCalendarsService) Get ¶
func (r *ResourcesCalendarsService) Get(customer string, calendarResourceId string) *ResourcesCalendarsGetCall

Get: Retrieves a calendar resource.

calendarResourceId: The unique ID of the calendar resource to retrieve.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesCalendarsService) Insert ¶
func (r *ResourcesCalendarsService) Insert(customer string, calendarresource *CalendarResource) *ResourcesCalendarsInsertCall

Insert: Inserts a calendar resource.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesCalendarsService) List ¶
func (r *ResourcesCalendarsService) List(customer string) *ResourcesCalendarsListCall

List: Retrieves a list of calendar resources for an account.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesCalendarsService) Patch ¶
func (r *ResourcesCalendarsService) Patch(customer string, calendarResourceId string, calendarresource *CalendarResource) *ResourcesCalendarsPatchCall

Patch: Patches a calendar resource.

calendarResourceId: The unique ID of the calendar resource to update.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesCalendarsService) Update ¶
func (r *ResourcesCalendarsService) Update(customer string, calendarResourceId string, calendarresource *CalendarResource) *ResourcesCalendarsUpdateCall

Update: Updates a calendar resource. This method supports patch semantics, meaning you only need to include the fields you wish to update. Fields that are not present in the request will be preserved.

calendarResourceId: The unique ID of the calendar resource to update.
customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
type ResourcesCalendarsUpdateCall ¶
type ResourcesCalendarsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesCalendarsUpdateCall) Context ¶
func (c *ResourcesCalendarsUpdateCall) Context(ctx context.Context) *ResourcesCalendarsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ResourcesCalendarsUpdateCall) Do ¶
func (c *ResourcesCalendarsUpdateCall) Do(opts ...googleapi.CallOption) (*CalendarResource, error)

Do executes the "directory.resources.calendars.update" call. Any non-2xx status code is an error. Response headers are in either *CalendarResource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesCalendarsUpdateCall) Fields ¶
func (c *ResourcesCalendarsUpdateCall) Fields(s ...googleapi.Field) *ResourcesCalendarsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesCalendarsUpdateCall) Header ¶
func (c *ResourcesCalendarsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesFeaturesDeleteCall ¶
type ResourcesFeaturesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesDeleteCall) Context ¶
func (c *ResourcesFeaturesDeleteCall) Context(ctx context.Context) *ResourcesFeaturesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesDeleteCall) Do ¶
func (c *ResourcesFeaturesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.resources.features.delete" call.

func (*ResourcesFeaturesDeleteCall) Fields ¶
func (c *ResourcesFeaturesDeleteCall) Fields(s ...googleapi.Field) *ResourcesFeaturesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesDeleteCall) Header ¶
func (c *ResourcesFeaturesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesFeaturesGetCall ¶
type ResourcesFeaturesGetCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesGetCall) Context ¶
func (c *ResourcesFeaturesGetCall) Context(ctx context.Context) *ResourcesFeaturesGetCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesGetCall) Do ¶
func (c *ResourcesFeaturesGetCall) Do(opts ...googleapi.CallOption) (*Feature, error)

Do executes the "directory.resources.features.get" call. Any non-2xx status code is an error. Response headers are in either *Feature.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesFeaturesGetCall) Fields ¶
func (c *ResourcesFeaturesGetCall) Fields(s ...googleapi.Field) *ResourcesFeaturesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesGetCall) Header ¶
func (c *ResourcesFeaturesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesFeaturesGetCall) IfNoneMatch ¶
func (c *ResourcesFeaturesGetCall) IfNoneMatch(entityTag string) *ResourcesFeaturesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ResourcesFeaturesInsertCall ¶
type ResourcesFeaturesInsertCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesInsertCall) Context ¶
func (c *ResourcesFeaturesInsertCall) Context(ctx context.Context) *ResourcesFeaturesInsertCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesInsertCall) Do ¶
func (c *ResourcesFeaturesInsertCall) Do(opts ...googleapi.CallOption) (*Feature, error)

Do executes the "directory.resources.features.insert" call. Any non-2xx status code is an error. Response headers are in either *Feature.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesFeaturesInsertCall) Fields ¶
func (c *ResourcesFeaturesInsertCall) Fields(s ...googleapi.Field) *ResourcesFeaturesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesInsertCall) Header ¶
func (c *ResourcesFeaturesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesFeaturesListCall ¶
type ResourcesFeaturesListCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesListCall) Context ¶
func (c *ResourcesFeaturesListCall) Context(ctx context.Context) *ResourcesFeaturesListCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesListCall) Do ¶
func (c *ResourcesFeaturesListCall) Do(opts ...googleapi.CallOption) (*Features, error)

Do executes the "directory.resources.features.list" call. Any non-2xx status code is an error. Response headers are in either *Features.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesFeaturesListCall) Fields ¶
func (c *ResourcesFeaturesListCall) Fields(s ...googleapi.Field) *ResourcesFeaturesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesListCall) Header ¶
func (c *ResourcesFeaturesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ResourcesFeaturesListCall) IfNoneMatch ¶
func (c *ResourcesFeaturesListCall) IfNoneMatch(entityTag string) *ResourcesFeaturesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ResourcesFeaturesListCall) MaxResults ¶
func (c *ResourcesFeaturesListCall) MaxResults(maxResults int64) *ResourcesFeaturesListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*ResourcesFeaturesListCall) PageToken ¶
func (c *ResourcesFeaturesListCall) PageToken(pageToken string) *ResourcesFeaturesListCall

PageToken sets the optional parameter "pageToken": Token to specify the next page in the list.

func (*ResourcesFeaturesListCall) Pages ¶
func (c *ResourcesFeaturesListCall) Pages(ctx context.Context, f func(*Features) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ResourcesFeaturesPatchCall ¶
type ResourcesFeaturesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesPatchCall) Context ¶
func (c *ResourcesFeaturesPatchCall) Context(ctx context.Context) *ResourcesFeaturesPatchCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesPatchCall) Do ¶
func (c *ResourcesFeaturesPatchCall) Do(opts ...googleapi.CallOption) (*Feature, error)

Do executes the "directory.resources.features.patch" call. Any non-2xx status code is an error. Response headers are in either *Feature.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesFeaturesPatchCall) Fields ¶
func (c *ResourcesFeaturesPatchCall) Fields(s ...googleapi.Field) *ResourcesFeaturesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesPatchCall) Header ¶
func (c *ResourcesFeaturesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesFeaturesRenameCall ¶
type ResourcesFeaturesRenameCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesRenameCall) Context ¶
func (c *ResourcesFeaturesRenameCall) Context(ctx context.Context) *ResourcesFeaturesRenameCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesRenameCall) Do ¶
func (c *ResourcesFeaturesRenameCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.resources.features.rename" call.

func (*ResourcesFeaturesRenameCall) Fields ¶
func (c *ResourcesFeaturesRenameCall) Fields(s ...googleapi.Field) *ResourcesFeaturesRenameCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesRenameCall) Header ¶
func (c *ResourcesFeaturesRenameCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesFeaturesService ¶
type ResourcesFeaturesService struct {
	// contains filtered or unexported fields
}
func NewResourcesFeaturesService ¶
func NewResourcesFeaturesService(s *Service) *ResourcesFeaturesService
func (*ResourcesFeaturesService) Delete ¶
func (r *ResourcesFeaturesService) Delete(customer string, featureKey string) *ResourcesFeaturesDeleteCall

Delete: Deletes a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
featureKey: The unique ID of the feature to delete.
func (*ResourcesFeaturesService) Get ¶
func (r *ResourcesFeaturesService) Get(customer string, featureKey string) *ResourcesFeaturesGetCall

Get: Retrieves a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
featureKey: The unique ID of the feature to retrieve.
func (*ResourcesFeaturesService) Insert ¶
func (r *ResourcesFeaturesService) Insert(customer string, feature *Feature) *ResourcesFeaturesInsertCall

Insert: Inserts a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesFeaturesService) List ¶
func (r *ResourcesFeaturesService) List(customer string) *ResourcesFeaturesListCall

List: Retrieves a list of features for an account.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
func (*ResourcesFeaturesService) Patch ¶
func (r *ResourcesFeaturesService) Patch(customer string, featureKey string, feature *Feature) *ResourcesFeaturesPatchCall

Patch: Patches a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
featureKey: The unique ID of the feature to update.
func (*ResourcesFeaturesService) Rename ¶
func (r *ResourcesFeaturesService) Rename(customer string, oldName string, featurerename *FeatureRename) *ResourcesFeaturesRenameCall

Rename: Renames a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
oldName: The unique ID of the feature to rename.
func (*ResourcesFeaturesService) Update ¶
func (r *ResourcesFeaturesService) Update(customer string, featureKey string, feature *Feature) *ResourcesFeaturesUpdateCall

Update: Updates a feature.

customer: The unique ID for the customer's Google Workspace account. As an account administrator, you can also use the `my_customer` alias to represent your account's customer ID.
featureKey: The unique ID of the feature to update.
type ResourcesFeaturesUpdateCall ¶
type ResourcesFeaturesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ResourcesFeaturesUpdateCall) Context ¶
func (c *ResourcesFeaturesUpdateCall) Context(ctx context.Context) *ResourcesFeaturesUpdateCall

Context sets the context to be used in this call's Do method.

func (*ResourcesFeaturesUpdateCall) Do ¶
func (c *ResourcesFeaturesUpdateCall) Do(opts ...googleapi.CallOption) (*Feature, error)

Do executes the "directory.resources.features.update" call. Any non-2xx status code is an error. Response headers are in either *Feature.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ResourcesFeaturesUpdateCall) Fields ¶
func (c *ResourcesFeaturesUpdateCall) Fields(s ...googleapi.Field) *ResourcesFeaturesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ResourcesFeaturesUpdateCall) Header ¶
func (c *ResourcesFeaturesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ResourcesService ¶
type ResourcesService struct {
	Buildings *ResourcesBuildingsService

	Calendars *ResourcesCalendarsService

	Features *ResourcesFeaturesService
	// contains filtered or unexported fields
}
func NewResourcesService ¶
func NewResourcesService(s *Service) *ResourcesService
type Role ¶
type Role struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// IsSuperAdminRole: Returns `true` if the role is a super admin role.
	IsSuperAdminRole bool `json:"isSuperAdminRole,omitempty"`
	// IsSystemRole: Returns `true` if this is a pre-defined system role.
	IsSystemRole bool `json:"isSystemRole,omitempty"`
	// Kind: The type of the API resource. This is always `admin#directory#role`.
	Kind string `json:"kind,omitempty"`
	// RoleDescription: A short description of the role.
	RoleDescription string `json:"roleDescription,omitempty"`
	// RoleId: ID of the role.
	RoleId int64 `json:"roleId,omitempty,string"`
	// RoleName: Name of the role.
	RoleName string `json:"roleName,omitempty"`
	// RolePrivileges: The set of privileges that are granted to this role.
	RolePrivileges []*RoleRolePrivileges `json:"rolePrivileges,omitempty"`

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
func (Role) MarshalJSON ¶
func (s Role) MarshalJSON() ([]byte, error)
type RoleAssignment ¶
type RoleAssignment struct {
	// AssignedTo: The unique ID of the entity this role is assigned to—either
	// the `user_id` of a user, the `group_id` of a group, or the `uniqueId` of a
	// service account as defined in Identity and Access Management (IAM)
	// (https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts).
	AssignedTo string `json:"assignedTo,omitempty"`
	// AssigneeType: Output only. The type of the assignee (`USER` or `GROUP`).
	//
	// Possible values:
	//   "user" - An individual user within the domain.
	//   "group" - A group within the domain.
	AssigneeType string `json:"assigneeType,omitempty"`
	// Condition: Optional. The condition associated with this role assignment.
	// Note: Feature is available to Enterprise Standard, Enterprise Plus, Google
	// Workspace for Education Plus and Cloud Identity Premium customers. A
	// `RoleAssignment` with the `condition` field set will only take effect when
	// the resource being accessed meets the condition. If `condition` is empty,
	// the role (`role_id`) is applied to the actor (`assigned_to`) at the scope
	// (`scope_type`) unconditionally. Currently, the following conditions are
	// supported: - To make the `RoleAssignment` only applicable to Security Groups
	// (https://cloud.google.com/identity/docs/groups#group_types):
	// `api.getAttribute('cloudidentity.googleapis.com/groups.labels',
	// []).hasAny(['groups.security']) && resource.type ==
	// 'cloudidentity.googleapis.com/Group'` - To make the `RoleAssignment` not
	// applicable to Security Groups
	// (https://cloud.google.com/identity/docs/groups#group_types):
	// `!api.getAttribute('cloudidentity.googleapis.com/groups.labels',
	// []).hasAny(['groups.security']) && resource.type ==
	// 'cloudidentity.googleapis.com/Group'` Currently, the condition strings have
	// to be verbatim and they only work with the following pre-built administrator
	// roles (https://support.google.com/a/answer/2405986): - Groups Editor -
	// Groups Reader The condition follows Cloud IAM condition syntax
	// (https://cloud.google.com/iam/docs/conditions-overview). - To make the
	// `RoleAssignment` not applicable to Locked Groups
	// (https://cloud.google.com/identity/docs/groups#group_types):
	// `!api.getAttribute('cloudidentity.googleapis.com/groups.labels',
	// []).hasAny(['groups.locked']) && resource.type ==
	// 'cloudidentity.googleapis.com/Group'` This condition can also be used in
	// conjunction with a Security-related condition.
	Condition string `json:"condition,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#roleAssignment`.
	Kind string `json:"kind,omitempty"`
	// OrgUnitId: If the role is restricted to an organization unit, this contains
	// the ID for the organization unit the exercise of this role is restricted to.
	OrgUnitId string `json:"orgUnitId,omitempty"`
	// RoleAssignmentId: ID of this roleAssignment.
	RoleAssignmentId int64 `json:"roleAssignmentId,omitempty,string"`
	// RoleId: The ID of the role that is assigned.
	RoleId int64 `json:"roleId,omitempty,string"`
	// ScopeType: The scope in which this role is assigned.
	ScopeType string `json:"scopeType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AssignedTo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssignedTo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RoleAssignment: Defines an assignment of a role.

func (RoleAssignment) MarshalJSON ¶
func (s RoleAssignment) MarshalJSON() ([]byte, error)
type RoleAssignments ¶
type RoleAssignments struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of RoleAssignment resources.
	Items []*RoleAssignment `json:"items,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#roleAssignments`.
	Kind          string `json:"kind,omitempty"`
	NextPageToken string `json:"nextPageToken,omitempty"`

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
func (RoleAssignments) MarshalJSON ¶
func (s RoleAssignments) MarshalJSON() ([]byte, error)
type RoleAssignmentsDeleteCall ¶
type RoleAssignmentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*RoleAssignmentsDeleteCall) Context ¶
func (c *RoleAssignmentsDeleteCall) Context(ctx context.Context) *RoleAssignmentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*RoleAssignmentsDeleteCall) Do ¶
func (c *RoleAssignmentsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.roleAssignments.delete" call.

func (*RoleAssignmentsDeleteCall) Fields ¶
func (c *RoleAssignmentsDeleteCall) Fields(s ...googleapi.Field) *RoleAssignmentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RoleAssignmentsDeleteCall) Header ¶
func (c *RoleAssignmentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type RoleAssignmentsGetCall ¶
type RoleAssignmentsGetCall struct {
	// contains filtered or unexported fields
}
func (*RoleAssignmentsGetCall) Context ¶
func (c *RoleAssignmentsGetCall) Context(ctx context.Context) *RoleAssignmentsGetCall

Context sets the context to be used in this call's Do method.

func (*RoleAssignmentsGetCall) Do ¶
func (c *RoleAssignmentsGetCall) Do(opts ...googleapi.CallOption) (*RoleAssignment, error)

Do executes the "directory.roleAssignments.get" call. Any non-2xx status code is an error. Response headers are in either *RoleAssignment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RoleAssignmentsGetCall) Fields ¶
func (c *RoleAssignmentsGetCall) Fields(s ...googleapi.Field) *RoleAssignmentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RoleAssignmentsGetCall) Header ¶
func (c *RoleAssignmentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*RoleAssignmentsGetCall) IfNoneMatch ¶
func (c *RoleAssignmentsGetCall) IfNoneMatch(entityTag string) *RoleAssignmentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type RoleAssignmentsInsertCall ¶
type RoleAssignmentsInsertCall struct {
	// contains filtered or unexported fields
}
func (*RoleAssignmentsInsertCall) Context ¶
func (c *RoleAssignmentsInsertCall) Context(ctx context.Context) *RoleAssignmentsInsertCall

Context sets the context to be used in this call's Do method.

func (*RoleAssignmentsInsertCall) Do ¶
func (c *RoleAssignmentsInsertCall) Do(opts ...googleapi.CallOption) (*RoleAssignment, error)

Do executes the "directory.roleAssignments.insert" call. Any non-2xx status code is an error. Response headers are in either *RoleAssignment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RoleAssignmentsInsertCall) Fields ¶
func (c *RoleAssignmentsInsertCall) Fields(s ...googleapi.Field) *RoleAssignmentsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RoleAssignmentsInsertCall) Header ¶
func (c *RoleAssignmentsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type RoleAssignmentsListCall ¶
type RoleAssignmentsListCall struct {
	// contains filtered or unexported fields
}
func (*RoleAssignmentsListCall) Context ¶
func (c *RoleAssignmentsListCall) Context(ctx context.Context) *RoleAssignmentsListCall

Context sets the context to be used in this call's Do method.

func (*RoleAssignmentsListCall) Do ¶
func (c *RoleAssignmentsListCall) Do(opts ...googleapi.CallOption) (*RoleAssignments, error)

Do executes the "directory.roleAssignments.list" call. Any non-2xx status code is an error. Response headers are in either *RoleAssignments.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RoleAssignmentsListCall) Fields ¶
func (c *RoleAssignmentsListCall) Fields(s ...googleapi.Field) *RoleAssignmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RoleAssignmentsListCall) Header ¶
func (c *RoleAssignmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*RoleAssignmentsListCall) IfNoneMatch ¶
func (c *RoleAssignmentsListCall) IfNoneMatch(entityTag string) *RoleAssignmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*RoleAssignmentsListCall) IncludeIndirectRoleAssignments ¶
added in v0.115.0
func (c *RoleAssignmentsListCall) IncludeIndirectRoleAssignments(includeIndirectRoleAssignments bool) *RoleAssignmentsListCall

IncludeIndirectRoleAssignments sets the optional parameter "includeIndirectRoleAssignments": When set to `true`, fetches indirect role assignments (i.e. role assignment via a group) as well as direct ones. Defaults to `false`. You must specify `user_key` or the indirect role assignments will not be included.

func (*RoleAssignmentsListCall) MaxResults ¶
func (c *RoleAssignmentsListCall) MaxResults(maxResults int64) *RoleAssignmentsListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*RoleAssignmentsListCall) PageToken ¶
func (c *RoleAssignmentsListCall) PageToken(pageToken string) *RoleAssignmentsListCall

PageToken sets the optional parameter "pageToken": Token to specify the next page in the list.

func (*RoleAssignmentsListCall) Pages ¶
func (c *RoleAssignmentsListCall) Pages(ctx context.Context, f func(*RoleAssignments) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*RoleAssignmentsListCall) RoleId ¶
func (c *RoleAssignmentsListCall) RoleId(roleId string) *RoleAssignmentsListCall

RoleId sets the optional parameter "roleId": Immutable ID of a role. If included in the request, returns only role assignments containing this role ID.

func (*RoleAssignmentsListCall) UserKey ¶
func (c *RoleAssignmentsListCall) UserKey(userKey string) *RoleAssignmentsListCall

UserKey sets the optional parameter "userKey": The primary email address, alias email address, or unique user or group ID. If included in the request, returns role assignments only for this user or group.

type RoleAssignmentsService ¶
type RoleAssignmentsService struct {
	// contains filtered or unexported fields
}
func NewRoleAssignmentsService ¶
func NewRoleAssignmentsService(s *Service) *RoleAssignmentsService
func (*RoleAssignmentsService) Delete ¶
func (r *RoleAssignmentsService) Delete(customer string, roleAssignmentId string) *RoleAssignmentsDeleteCall

Delete: Deletes a role assignment.

- customer: Immutable ID of the Google Workspace account. - roleAssignmentId: Immutable ID of the role assignment.

func (*RoleAssignmentsService) Get ¶
func (r *RoleAssignmentsService) Get(customer string, roleAssignmentId string) *RoleAssignmentsGetCall

Get: Retrieves a role assignment.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
roleAssignmentId: Immutable ID of the role assignment.
func (*RoleAssignmentsService) Insert ¶
func (r *RoleAssignmentsService) Insert(customer string, roleassignment *RoleAssignment) *RoleAssignmentsInsertCall

Insert: Creates a role assignment.

- customer: Immutable ID of the Google Workspace account.

func (*RoleAssignmentsService) List ¶
func (r *RoleAssignmentsService) List(customer string) *RoleAssignmentsListCall

List: Retrieves a paginated list of all roleAssignments.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
type RoleRolePrivileges ¶
type RoleRolePrivileges struct {
	// PrivilegeName: The name of the privilege.
	PrivilegeName string `json:"privilegeName,omitempty"`
	// ServiceId: The obfuscated ID of the service this privilege is for. This
	// value is returned with `Privileges.list()`
	// (https://developers.google.com/workspace/admin/directory/v1/reference/privileges/list).
	ServiceId string `json:"serviceId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PrivilegeName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PrivilegeName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (RoleRolePrivileges) MarshalJSON ¶
func (s RoleRolePrivileges) MarshalJSON() ([]byte, error)
type Roles ¶
type Roles struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of Role resources.
	Items []*Role `json:"items,omitempty"`
	// Kind: The type of the API resource. This is always `admin#directory#roles`.
	Kind          string `json:"kind,omitempty"`
	NextPageToken string `json:"nextPageToken,omitempty"`

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
func (Roles) MarshalJSON ¶
func (s Roles) MarshalJSON() ([]byte, error)
type RolesDeleteCall ¶
type RolesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*RolesDeleteCall) Context ¶
func (c *RolesDeleteCall) Context(ctx context.Context) *RolesDeleteCall

Context sets the context to be used in this call's Do method.

func (*RolesDeleteCall) Do ¶
func (c *RolesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.roles.delete" call.

func (*RolesDeleteCall) Fields ¶
func (c *RolesDeleteCall) Fields(s ...googleapi.Field) *RolesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesDeleteCall) Header ¶
func (c *RolesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type RolesGetCall ¶
type RolesGetCall struct {
	// contains filtered or unexported fields
}
func (*RolesGetCall) Context ¶
func (c *RolesGetCall) Context(ctx context.Context) *RolesGetCall

Context sets the context to be used in this call's Do method.

func (*RolesGetCall) Do ¶
func (c *RolesGetCall) Do(opts ...googleapi.CallOption) (*Role, error)

Do executes the "directory.roles.get" call. Any non-2xx status code is an error. Response headers are in either *Role.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RolesGetCall) Fields ¶
func (c *RolesGetCall) Fields(s ...googleapi.Field) *RolesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesGetCall) Header ¶
func (c *RolesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*RolesGetCall) IfNoneMatch ¶
func (c *RolesGetCall) IfNoneMatch(entityTag string) *RolesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type RolesInsertCall ¶
type RolesInsertCall struct {
	// contains filtered or unexported fields
}
func (*RolesInsertCall) Context ¶
func (c *RolesInsertCall) Context(ctx context.Context) *RolesInsertCall

Context sets the context to be used in this call's Do method.

func (*RolesInsertCall) Do ¶
func (c *RolesInsertCall) Do(opts ...googleapi.CallOption) (*Role, error)

Do executes the "directory.roles.insert" call. Any non-2xx status code is an error. Response headers are in either *Role.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RolesInsertCall) Fields ¶
func (c *RolesInsertCall) Fields(s ...googleapi.Field) *RolesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesInsertCall) Header ¶
func (c *RolesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type RolesListCall ¶
type RolesListCall struct {
	// contains filtered or unexported fields
}
func (*RolesListCall) Context ¶
func (c *RolesListCall) Context(ctx context.Context) *RolesListCall

Context sets the context to be used in this call's Do method.

func (*RolesListCall) Do ¶
func (c *RolesListCall) Do(opts ...googleapi.CallOption) (*Roles, error)

Do executes the "directory.roles.list" call. Any non-2xx status code is an error. Response headers are in either *Roles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RolesListCall) Fields ¶
func (c *RolesListCall) Fields(s ...googleapi.Field) *RolesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesListCall) Header ¶
func (c *RolesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*RolesListCall) IfNoneMatch ¶
func (c *RolesListCall) IfNoneMatch(entityTag string) *RolesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*RolesListCall) MaxResults ¶
func (c *RolesListCall) MaxResults(maxResults int64) *RolesListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*RolesListCall) PageToken ¶
func (c *RolesListCall) PageToken(pageToken string) *RolesListCall

PageToken sets the optional parameter "pageToken": Token to specify the next page in the list.

func (*RolesListCall) Pages ¶
func (c *RolesListCall) Pages(ctx context.Context, f func(*Roles) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type RolesPatchCall ¶
type RolesPatchCall struct {
	// contains filtered or unexported fields
}
func (*RolesPatchCall) Context ¶
func (c *RolesPatchCall) Context(ctx context.Context) *RolesPatchCall

Context sets the context to be used in this call's Do method.

func (*RolesPatchCall) Do ¶
func (c *RolesPatchCall) Do(opts ...googleapi.CallOption) (*Role, error)

Do executes the "directory.roles.patch" call. Any non-2xx status code is an error. Response headers are in either *Role.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RolesPatchCall) Fields ¶
func (c *RolesPatchCall) Fields(s ...googleapi.Field) *RolesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesPatchCall) Header ¶
func (c *RolesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type RolesService ¶
type RolesService struct {
	// contains filtered or unexported fields
}
func NewRolesService ¶
func NewRolesService(s *Service) *RolesService
func (*RolesService) Delete ¶
func (r *RolesService) Delete(customer string, roleId string) *RolesDeleteCall

Delete: Deletes a role.

- customer: Immutable ID of the Google Workspace account. - roleId: Immutable ID of the role.

func (*RolesService) Get ¶
func (r *RolesService) Get(customer string, roleId string) *RolesGetCall

Get: Retrieves a role.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
roleId: Immutable ID of the role.
func (*RolesService) Insert ¶
func (r *RolesService) Insert(customer string, role *Role) *RolesInsertCall

Insert: Creates a role.

- customer: Immutable ID of the Google Workspace account.

func (*RolesService) List ¶
func (r *RolesService) List(customer string) *RolesListCall

List: Retrieves a paginated list of all the roles in a domain.

customer: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
func (*RolesService) Patch ¶
func (r *RolesService) Patch(customer string, roleId string, role *Role) *RolesPatchCall

Patch: Patches a role.

- customer: Immutable ID of the Google Workspace account. - roleId: Immutable ID of the role.

func (*RolesService) Update ¶
func (r *RolesService) Update(customer string, roleId string, role *Role) *RolesUpdateCall

Update: Updates a role.

- customer: Immutable ID of the Google Workspace account. - roleId: Immutable ID of the role.

type RolesUpdateCall ¶
type RolesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*RolesUpdateCall) Context ¶
func (c *RolesUpdateCall) Context(ctx context.Context) *RolesUpdateCall

Context sets the context to be used in this call's Do method.

func (*RolesUpdateCall) Do ¶
func (c *RolesUpdateCall) Do(opts ...googleapi.CallOption) (*Role, error)

Do executes the "directory.roles.update" call. Any non-2xx status code is an error. Response headers are in either *Role.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*RolesUpdateCall) Fields ¶
func (c *RolesUpdateCall) Fields(s ...googleapi.Field) *RolesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*RolesUpdateCall) Header ¶
func (c *RolesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type Schema ¶
type Schema struct {
	// DisplayName: Display name for the schema.
	DisplayName string `json:"displayName,omitempty"`
	// Etag: The ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Fields: A list of fields in the schema.
	Fields []*SchemaFieldSpec `json:"fields,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// SchemaId: The unique identifier of the schema (Read-only)
	SchemaId string `json:"schemaId,omitempty"`
	// SchemaName: The schema's name. Each `schema_name` must be unique within a
	// customer. Reusing a name results in a `409: Entity already exists` error.
	SchemaName string `json:"schemaName,omitempty"`

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

Schema: The type of API resource. For Schema resources, this is always `admin#directory#schema`.

func (Schema) MarshalJSON ¶
func (s Schema) MarshalJSON() ([]byte, error)
type SchemaFieldSpec ¶
type SchemaFieldSpec struct {
	// DisplayName: Display Name of the field.
	DisplayName string `json:"displayName,omitempty"`
	// Etag: The ETag of the field.
	Etag string `json:"etag,omitempty"`
	// FieldId: The unique identifier of the field (Read-only)
	FieldId string `json:"fieldId,omitempty"`
	// FieldName: The name of the field.
	FieldName string `json:"fieldName,omitempty"`
	// FieldType: The type of the field.
	FieldType string `json:"fieldType,omitempty"`
	// Indexed: Boolean specifying whether the field is indexed or not. Default:
	// `true`.
	//
	// Default: true
	Indexed *bool `json:"indexed,omitempty"`
	// Kind: The kind of resource this is. For schema fields this is always
	// `admin#directory#schema#fieldspec`.
	Kind string `json:"kind,omitempty"`
	// MultiValued: A boolean specifying whether this is a multi-valued field or
	// not. Default: `false`.
	MultiValued bool `json:"multiValued,omitempty"`
	// NumericIndexingSpec: Indexing spec for a numeric field. By default, only
	// exact match queries will be supported for numeric fields. Setting the
	// `numericIndexingSpec` allows range queries to be supported.
	NumericIndexingSpec *SchemaFieldSpecNumericIndexingSpec `json:"numericIndexingSpec,omitempty"`
	// ReadAccessType: Specifies who can view values of this field. See Retrieve
	// users as a non-administrator
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#retrieve_users_non_admin)
	// for more information. Note: It may take up to 24 hours for changes to this
	// field to be reflected.
	ReadAccessType string `json:"readAccessType,omitempty"`
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

SchemaFieldSpec: You can use schemas to add custom fields to user profiles. You can use these fields to store information such as the projects your users work on, their physical locations, their hire dates, or whatever else fits your business needs. For more information, see Custom User Fields (https://developers.google.com/workspace/admin/directory/v1/guides/manage-schemas).

func (SchemaFieldSpec) MarshalJSON ¶
func (s SchemaFieldSpec) MarshalJSON() ([]byte, error)
type SchemaFieldSpecNumericIndexingSpec ¶
type SchemaFieldSpecNumericIndexingSpec struct {
	// MaxValue: Maximum value of this field. This is meant to be indicative rather
	// than enforced. Values outside this range will still be indexed, but search
	// may not be as performant.
	MaxValue float64 `json:"maxValue,omitempty"`
	// MinValue: Minimum value of this field. This is meant to be indicative rather
	// than enforced. Values outside this range will still be indexed, but search
	// may not be as performant.
	MinValue float64 `json:"minValue,omitempty"`
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

SchemaFieldSpecNumericIndexingSpec: Indexing spec for a numeric field. By default, only exact match queries will be supported for numeric fields. Setting the `numericIndexingSpec` allows range queries to be supported.

func (SchemaFieldSpecNumericIndexingSpec) MarshalJSON ¶
func (s SchemaFieldSpecNumericIndexingSpec) MarshalJSON() ([]byte, error)
func (*SchemaFieldSpecNumericIndexingSpec) UnmarshalJSON ¶
func (s *SchemaFieldSpecNumericIndexingSpec) UnmarshalJSON(data []byte) error
type Schemas ¶
type Schemas struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// Schemas: A list of UserSchema objects.
	Schemas []*Schema `json:"schemas,omitempty"`

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

Schemas: JSON response template for List Schema operation in Directory API.

func (Schemas) MarshalJSON ¶
func (s Schemas) MarshalJSON() ([]byte, error)
type SchemasDeleteCall ¶
type SchemasDeleteCall struct {
	// contains filtered or unexported fields
}
func (*SchemasDeleteCall) Context ¶
func (c *SchemasDeleteCall) Context(ctx context.Context) *SchemasDeleteCall

Context sets the context to be used in this call's Do method.

func (*SchemasDeleteCall) Do ¶
func (c *SchemasDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.schemas.delete" call.

func (*SchemasDeleteCall) Fields ¶
func (c *SchemasDeleteCall) Fields(s ...googleapi.Field) *SchemasDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasDeleteCall) Header ¶
func (c *SchemasDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type SchemasGetCall ¶
type SchemasGetCall struct {
	// contains filtered or unexported fields
}
func (*SchemasGetCall) Context ¶
func (c *SchemasGetCall) Context(ctx context.Context) *SchemasGetCall

Context sets the context to be used in this call's Do method.

func (*SchemasGetCall) Do ¶
func (c *SchemasGetCall) Do(opts ...googleapi.CallOption) (*Schema, error)

Do executes the "directory.schemas.get" call. Any non-2xx status code is an error. Response headers are in either *Schema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SchemasGetCall) Fields ¶
func (c *SchemasGetCall) Fields(s ...googleapi.Field) *SchemasGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasGetCall) Header ¶
func (c *SchemasGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*SchemasGetCall) IfNoneMatch ¶
func (c *SchemasGetCall) IfNoneMatch(entityTag string) *SchemasGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type SchemasInsertCall ¶
type SchemasInsertCall struct {
	// contains filtered or unexported fields
}
func (*SchemasInsertCall) Context ¶
func (c *SchemasInsertCall) Context(ctx context.Context) *SchemasInsertCall

Context sets the context to be used in this call's Do method.

func (*SchemasInsertCall) Do ¶
func (c *SchemasInsertCall) Do(opts ...googleapi.CallOption) (*Schema, error)

Do executes the "directory.schemas.insert" call. Any non-2xx status code is an error. Response headers are in either *Schema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SchemasInsertCall) Fields ¶
func (c *SchemasInsertCall) Fields(s ...googleapi.Field) *SchemasInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasInsertCall) Header ¶
func (c *SchemasInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type SchemasListCall ¶
type SchemasListCall struct {
	// contains filtered or unexported fields
}
func (*SchemasListCall) Context ¶
func (c *SchemasListCall) Context(ctx context.Context) *SchemasListCall

Context sets the context to be used in this call's Do method.

func (*SchemasListCall) Do ¶
func (c *SchemasListCall) Do(opts ...googleapi.CallOption) (*Schemas, error)

Do executes the "directory.schemas.list" call. Any non-2xx status code is an error. Response headers are in either *Schemas.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SchemasListCall) Fields ¶
func (c *SchemasListCall) Fields(s ...googleapi.Field) *SchemasListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasListCall) Header ¶
func (c *SchemasListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*SchemasListCall) IfNoneMatch ¶
func (c *SchemasListCall) IfNoneMatch(entityTag string) *SchemasListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type SchemasPatchCall ¶
type SchemasPatchCall struct {
	// contains filtered or unexported fields
}
func (*SchemasPatchCall) Context ¶
func (c *SchemasPatchCall) Context(ctx context.Context) *SchemasPatchCall

Context sets the context to be used in this call's Do method.

func (*SchemasPatchCall) Do ¶
func (c *SchemasPatchCall) Do(opts ...googleapi.CallOption) (*Schema, error)

Do executes the "directory.schemas.patch" call. Any non-2xx status code is an error. Response headers are in either *Schema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SchemasPatchCall) Fields ¶
func (c *SchemasPatchCall) Fields(s ...googleapi.Field) *SchemasPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasPatchCall) Header ¶
func (c *SchemasPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type SchemasService ¶
type SchemasService struct {
	// contains filtered or unexported fields
}
func NewSchemasService ¶
func NewSchemasService(s *Service) *SchemasService
func (*SchemasService) Delete ¶
func (r *SchemasService) Delete(customerId string, schemaKey string) *SchemasDeleteCall

Delete: Deletes a schema.

- customerId: Immutable ID of the Google Workspace account. - schemaKey: Name or immutable ID of the schema.

func (*SchemasService) Get ¶
func (r *SchemasService) Get(customerId string, schemaKey string) *SchemasGetCall

Get: Retrieves a schema.

customerId: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
schemaKey: Name or immutable ID of the schema.
func (*SchemasService) Insert ¶
func (r *SchemasService) Insert(customerId string, schema *Schema) *SchemasInsertCall

Insert: Creates a schema.

- customerId: Immutable ID of the Google Workspace account.

func (*SchemasService) List ¶
func (r *SchemasService) List(customerId string) *SchemasListCall

List: Retrieves all schemas for a customer.

customerId: The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all groups for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.
func (*SchemasService) Patch ¶
func (r *SchemasService) Patch(customerId string, schemaKey string, schema *Schema) *SchemasPatchCall

Patch: Patches a schema.

- customerId: Immutable ID of the Google Workspace account. - schemaKey: Name or immutable ID of the schema.

func (*SchemasService) Update ¶
func (r *SchemasService) Update(customerId string, schemaKey string, schema *Schema) *SchemasUpdateCall

Update: Updates a schema.

- customerId: Immutable ID of the Google Workspace account. - schemaKey: Name or immutable ID of the schema.

type SchemasUpdateCall ¶
type SchemasUpdateCall struct {
	// contains filtered or unexported fields
}
func (*SchemasUpdateCall) Context ¶
func (c *SchemasUpdateCall) Context(ctx context.Context) *SchemasUpdateCall

Context sets the context to be used in this call's Do method.

func (*SchemasUpdateCall) Do ¶
func (c *SchemasUpdateCall) Do(opts ...googleapi.CallOption) (*Schema, error)

Do executes the "directory.schemas.update" call. Any non-2xx status code is an error. Response headers are in either *Schema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SchemasUpdateCall) Fields ¶
func (c *SchemasUpdateCall) Fields(s ...googleapi.Field) *SchemasUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SchemasUpdateCall) Header ¶
func (c *SchemasUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Asps *AspsService

	Channels *ChannelsService

	Chromeosdevices *ChromeosdevicesService

	Customer *CustomerService

	Customers *CustomersService

	DomainAliases *DomainAliasesService

	Domains *DomainsService

	Groups *GroupsService

	Members *MembersService

	Mobiledevices *MobiledevicesService

	Orgunits *OrgunitsService

	Privileges *PrivilegesService

	Resources *ResourcesService

	RoleAssignments *RoleAssignmentsService

	Roles *RolesService

	Schemas *SchemasService

	Tokens *TokensService

	TwoStepVerification *TwoStepVerificationService

	Users *UsersService

	VerificationCodes *VerificationCodesService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type Status ¶
added in v0.155.0
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
added in v0.155.0
func (s Status) MarshalJSON() ([]byte, error)
type Token ¶
type Token struct {
	// Anonymous: Whether the application is registered with Google. The value is
	// `true` if the application has an anonymous Client ID.
	Anonymous bool `json:"anonymous,omitempty"`
	// ClientId: The Client ID of the application the token is issued to.
	ClientId string `json:"clientId,omitempty"`
	// DisplayText: The displayable name of the application the token is issued to.
	DisplayText string `json:"displayText,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the API resource. This is always `admin#directory#token`.
	Kind string `json:"kind,omitempty"`
	// NativeApp: Whether the token is issued to an installed application. The
	// value is `true` if the application is installed to a desktop or mobile
	// device.
	NativeApp bool `json:"nativeApp,omitempty"`
	// Scopes: A list of authorization scopes the application is granted.
	Scopes []string `json:"scopes,omitempty"`
	// UserKey: The unique ID of the user that issued the token.
	UserKey string `json:"userKey,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Anonymous") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Anonymous") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Token: JSON template for token resource in Directory API.

func (Token) MarshalJSON ¶
func (s Token) MarshalJSON() ([]byte, error)
type Tokens ¶
type Tokens struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of Token resources.
	Items []*Token `json:"items,omitempty"`
	// Kind: The type of the API resource. This is always
	// `admin#directory#tokenList`.
	Kind string `json:"kind,omitempty"`

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

Tokens: JSON response template for List tokens operation in Directory API.

func (Tokens) MarshalJSON ¶
func (s Tokens) MarshalJSON() ([]byte, error)
type TokensDeleteCall ¶
type TokensDeleteCall struct {
	// contains filtered or unexported fields
}
func (*TokensDeleteCall) Context ¶
func (c *TokensDeleteCall) Context(ctx context.Context) *TokensDeleteCall

Context sets the context to be used in this call's Do method.

func (*TokensDeleteCall) Do ¶
func (c *TokensDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.tokens.delete" call.

func (*TokensDeleteCall) Fields ¶
func (c *TokensDeleteCall) Fields(s ...googleapi.Field) *TokensDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*TokensDeleteCall) Header ¶
func (c *TokensDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type TokensGetCall ¶
type TokensGetCall struct {
	// contains filtered or unexported fields
}
func (*TokensGetCall) Context ¶
func (c *TokensGetCall) Context(ctx context.Context) *TokensGetCall

Context sets the context to be used in this call's Do method.

func (*TokensGetCall) Do ¶
func (c *TokensGetCall) Do(opts ...googleapi.CallOption) (*Token, error)

Do executes the "directory.tokens.get" call. Any non-2xx status code is an error. Response headers are in either *Token.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*TokensGetCall) Fields ¶
func (c *TokensGetCall) Fields(s ...googleapi.Field) *TokensGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*TokensGetCall) Header ¶
func (c *TokensGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*TokensGetCall) IfNoneMatch ¶
func (c *TokensGetCall) IfNoneMatch(entityTag string) *TokensGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type TokensListCall ¶
type TokensListCall struct {
	// contains filtered or unexported fields
}
func (*TokensListCall) Context ¶
func (c *TokensListCall) Context(ctx context.Context) *TokensListCall

Context sets the context to be used in this call's Do method.

func (*TokensListCall) Do ¶
func (c *TokensListCall) Do(opts ...googleapi.CallOption) (*Tokens, error)

Do executes the "directory.tokens.list" call. Any non-2xx status code is an error. Response headers are in either *Tokens.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*TokensListCall) Fields ¶
func (c *TokensListCall) Fields(s ...googleapi.Field) *TokensListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*TokensListCall) Header ¶
func (c *TokensListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*TokensListCall) IfNoneMatch ¶
func (c *TokensListCall) IfNoneMatch(entityTag string) *TokensListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type TokensService ¶
type TokensService struct {
	// contains filtered or unexported fields
}
func NewTokensService ¶
func NewTokensService(s *Service) *TokensService
func (*TokensService) Delete ¶
func (r *TokensService) Delete(userKey string, clientId string) *TokensDeleteCall

Delete: Deletes all access tokens issued by a user for an application.

clientId: The Client ID of the application the token is issued to.
userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*TokensService) Get ¶
func (r *TokensService) Get(userKey string, clientId string) *TokensGetCall

Get: Gets information about an access token issued by a user.

clientId: The Client ID of the application the token is issued to.
userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*TokensService) List ¶
func (r *TokensService) List(userKey string) *TokensListCall

List: Returns the set of tokens specified user has issued to 3rd party applications.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
type TwoStepVerificationService ¶
added in v0.32.0
type TwoStepVerificationService struct {
	// contains filtered or unexported fields
}
func NewTwoStepVerificationService ¶
added in v0.32.0
func NewTwoStepVerificationService(s *Service) *TwoStepVerificationService
func (*TwoStepVerificationService) TurnOff ¶
added in v0.32.0
func (r *TwoStepVerificationService) TurnOff(userKey string) *TwoStepVerificationTurnOffCall

TurnOff: Turns off 2-Step Verification for user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
type TwoStepVerificationTurnOffCall ¶
added in v0.32.0
type TwoStepVerificationTurnOffCall struct {
	// contains filtered or unexported fields
}
func (*TwoStepVerificationTurnOffCall) Context ¶
added in v0.32.0
func (c *TwoStepVerificationTurnOffCall) Context(ctx context.Context) *TwoStepVerificationTurnOffCall

Context sets the context to be used in this call's Do method.

func (*TwoStepVerificationTurnOffCall) Do ¶
added in v0.32.0
func (c *TwoStepVerificationTurnOffCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.twoStepVerification.turnOff" call.

func (*TwoStepVerificationTurnOffCall) Fields ¶
added in v0.32.0
func (c *TwoStepVerificationTurnOffCall) Fields(s ...googleapi.Field) *TwoStepVerificationTurnOffCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*TwoStepVerificationTurnOffCall) Header ¶
added in v0.32.0
func (c *TwoStepVerificationTurnOffCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type User ¶
type User struct {
	// Addresses: The list of the user's addresses. The maximum allowed data size
	// for this field is 10KB.
	Addresses interface{} `json:"addresses,omitempty"`
	// AgreedToTerms: Output only. This property is `true` if the user has
	// completed an initial login and accepted the Terms of Service agreement.
	AgreedToTerms bool `json:"agreedToTerms,omitempty"`
	// Aliases: Output only. The list of the user's alias email addresses.
	Aliases []string `json:"aliases,omitempty"`
	// Archived: Indicates if user is archived.
	Archived bool `json:"archived,omitempty"`
	// ChangePasswordAtNextLogin: Indicates if the user is forced to change their
	// password at next login. This setting doesn't apply when the user signs in
	// via a third-party identity provider
	// (https://support.google.com/a/answer/60224).
	ChangePasswordAtNextLogin bool `json:"changePasswordAtNextLogin,omitempty"`
	// CreationTime: User's G Suite account creation time. (Read-only)
	CreationTime string `json:"creationTime,omitempty"`
	// CustomSchemas: Custom fields of the user. The key is a `schema_name` and its
	// values are `'field_name': 'field_value'`.
	CustomSchemas map[string]googleapi.RawMessage `json:"customSchemas,omitempty"`
	// CustomerId: Output only. The customer ID to retrieve all account users
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users.html#get_all_users).
	// You can use the alias `my_customer` to represent your account's
	// `customerId`. As a reseller administrator, you can use the resold customer
	// account's `customerId`. To get a `customerId`, use the account's primary
	// domain in the `domain` parameter of a users.list
	// (https://developers.google.com/workspace/admin/directory/v1/reference/users/list)
	// request.
	CustomerId   string `json:"customerId,omitempty"`
	DeletionTime string `json:"deletionTime,omitempty"`
	// Emails: The list of the user's email addresses. The maximum allowed data
	// size for this field is 10KB. This excludes
	// `publicKeyEncryptionCertificates`.
	Emails interface{} `json:"emails,omitempty"`
	// Etag: Output only. ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// ExternalIds: The list of external IDs for the user, such as an employee or
	// network ID. The maximum allowed data size for this field is 2KB.
	ExternalIds interface{} `json:"externalIds,omitempty"`
	// Gender: The user's gender. The maximum allowed data size for this field is
	// 1KB.
	Gender interface{} `json:"gender,omitempty"`
	// GuestAccountInfo: Immutable. Additional guest-related metadata fields
	GuestAccountInfo *GuestAccountInfo `json:"guestAccountInfo,omitempty"`
	// HashFunction: Stores the hash format of the `password` property. The
	// following `hashFunction` values are allowed: * `MD5` - Accepts simple
	// hex-encoded values. * `SHA-1` - Accepts simple hex-encoded values. * `crypt`
	// - Compliant with the C crypt library
	// (https://en.wikipedia.org/wiki/Crypt_%28C%29). Supports the DES, MD5 (hash
	// prefix `$1$`), SHA-256 (hash prefix `$5$`), and SHA-512 (hash prefix `$6$`)
	// hash algorithms. If rounds are specified as part of the prefix, they must be
	// 10,000 or fewer.
	HashFunction string `json:"hashFunction,omitempty"`
	// Id: The unique ID for the user. A user `id` can be used as a user request
	// URI's `userKey`.
	Id string `json:"id,omitempty"`
	// Ims: The list of the user's Instant Messenger (IM) accounts. A user account
	// can have multiple ims properties. But, only one of these ims properties can
	// be the primary IM contact. The maximum allowed data size for this field is
	// 2KB.
	Ims interface{} `json:"ims,omitempty"`
	// IncludeInGlobalAddressList: Indicates if the user's profile is visible in
	// the Google Workspace global address list when the contact sharing feature is
	// enabled for the domain. For more information about excluding user profiles,
	// see the administration help center
	// (https://support.google.com/a/answer/1285988).
	IncludeInGlobalAddressList bool `json:"includeInGlobalAddressList,omitempty"`
	// IpWhitelisted: If `true`, the user's IP address is subject to a deprecated
	// IP address `allowlist` (https://support.google.com/a/answer/60752)
	// configuration.
	IpWhitelisted bool `json:"ipWhitelisted,omitempty"`
	// IsAdmin: Output only. Indicates a user with super administrator privileges.
	// The `isAdmin` property can only be edited in the Make a user an
	// administrator
	// (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users.html#make_admin)
	// operation ( makeAdmin
	// (https://developers.google.com/workspace/admin/directory/v1/reference/users/makeAdmin.html)
	// method). If edited in the user insert
	// (https://developers.google.com/workspace/admin/directory/v1/reference/users/insert.html)
	// or update
	// (https://developers.google.com/workspace/admin/directory/v1/reference/users/update.html)
	// methods, the edit is ignored by the API service.
	IsAdmin bool `json:"isAdmin,omitempty"`
	// IsDelegatedAdmin: Output only. Indicates if the user is a delegated
	// administrator. Delegated administrators are supported by the API but cannot
	// create or undelete users, or make users administrators. These requests are
	// ignored by the API service. Roles and privileges for administrators are
	// assigned using the Admin console
	// (https://support.google.com/a/answer/33325).
	IsDelegatedAdmin bool `json:"isDelegatedAdmin,omitempty"`
	// IsEnforcedIn2Sv: Output only. Is 2-step verification enforced (Read-only)
	IsEnforcedIn2Sv bool `json:"isEnforcedIn2Sv,omitempty"`
	// IsEnrolledIn2Sv: Output only. Is enrolled in 2-step verification (Read-only)
	IsEnrolledIn2Sv bool `json:"isEnrolledIn2Sv,omitempty"`
	// IsGuestUser: Immutable. Indicates if the inserted user is a guest.
	IsGuestUser bool `json:"isGuestUser,omitempty"`
	// IsMailboxSetup: Output only. Indicates if the user's Google mailbox is
	// created. This property is only applicable if the user has been assigned a
	// Gmail license.
	IsMailboxSetup bool `json:"isMailboxSetup,omitempty"`
	// Keywords: The list of the user's keywords. The maximum allowed data size for
	// this field is 1KB.
	Keywords interface{} `json:"keywords,omitempty"`
	// Kind: Output only. The type of the API resource. For Users resources, the
	// value is `admin#directory#user`.
	Kind string `json:"kind,omitempty"`
	// Languages: The user's languages. The maximum allowed data size for this
	// field is 1KB.
	Languages interface{} `json:"languages,omitempty"`
	// LastLoginTime: User's last login time. (Read-only)
	LastLoginTime string `json:"lastLoginTime,omitempty"`
	// Locations: The user's locations. The maximum allowed data size for this
	// field is 10KB.
	Locations interface{} `json:"locations,omitempty"`
	// Name: Holds the given and family names of the user, and the read-only
	// `fullName` value. The maximum number of characters in the `givenName` and in
	// the `familyName` values is 60. In addition, name values support
	// unicode/UTF-8 characters, and can contain spaces, letters (a-z), numbers
	// (0-9), dashes (-), forward slashes (/), and periods (.). For more
	// information about character usage rules, see the administration help center
	// (https://support.google.com/a/answer/9193374). Maximum allowed data size for
	// this field is 1KB.
	Name *UserName `json:"name,omitempty"`
	// NonEditableAliases: Output only. The list of the user's non-editable alias
	// email addresses. These are typically outside the account's primary domain or
	// sub-domain.
	NonEditableAliases []string `json:"nonEditableAliases,omitempty"`
	// Notes: Notes for the user.
	Notes interface{} `json:"notes,omitempty"`
	// OrgUnitPath: The full path of the parent organization associated with the
	// user. If the parent organization is the top-level, it is represented as a
	// forward slash (`/`).
	OrgUnitPath string `json:"orgUnitPath,omitempty"`
	// Organizations: The list of organizations the user belongs to. The maximum
	// allowed data size for this field is 10KB.
	Organizations interface{} `json:"organizations,omitempty"`
	// Password: User's password
	Password string `json:"password,omitempty"`
	// Phones: The list of the user's phone numbers. The maximum allowed data size
	// for this field is 1KB.
	Phones interface{} `json:"phones,omitempty"`
	// PosixAccounts: The list of POSIX
	// (https://www.opengroup.org/austin/papers/posix_faq.html) account information
	// for the user.
	PosixAccounts interface{} `json:"posixAccounts,omitempty"`
	// PrimaryEmail: The user's primary email address. This property is required in
	// a request to create a user account. The `primaryEmail` must be unique and
	// cannot be an alias of another user.
	PrimaryEmail string `json:"primaryEmail,omitempty"`
	// RecoveryEmail: Recovery email of the user.
	RecoveryEmail string `json:"recoveryEmail,omitempty"`
	// RecoveryPhone: Recovery phone of the user. The phone number must be in the
	// E.164 format, starting with the plus sign (+). Example: *+16506661212*.
	RecoveryPhone string `json:"recoveryPhone,omitempty"`
	// Relations: The list of the user's relationships to other users. The maximum
	// allowed data size for this field is 2KB.
	Relations interface{} `json:"relations,omitempty"`
	// SshPublicKeys: A list of SSH public keys.
	SshPublicKeys interface{} `json:"sshPublicKeys,omitempty"`
	// Suspended: Indicates if user is suspended.
	Suspended bool `json:"suspended,omitempty"`
	// SuspensionReason: Output only. Has the reason a user account is suspended
	// either by the administrator or by Google at the time of suspension. The
	// property is returned only if the `suspended` property is `true`.
	SuspensionReason string `json:"suspensionReason,omitempty"`
	// ThumbnailPhotoEtag: Output only. ETag of the user's photo (Read-only)
	ThumbnailPhotoEtag string `json:"thumbnailPhotoEtag,omitempty"`
	// ThumbnailPhotoUrl: Output only. The URL of the user's profile photo. The URL
	// might be temporary or private.
	ThumbnailPhotoUrl string `json:"thumbnailPhotoUrl,omitempty"`
	// Websites: The user's websites. The maximum allowed data size for this field
	// is 2KB.
	Websites interface{} `json:"websites,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Addresses") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Addresses") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

User: The Directory API allows you to create and manage your account's users, user aliases, and user Google profile photos. For more information about common tasks, see the User Accounts Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users.html) and the User Aliases Developer's Guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-user-aliases.html).

func (User) MarshalJSON ¶
func (s User) MarshalJSON() ([]byte, error)
type UserAbout ¶
type UserAbout struct {
	// ContentType: About entry can have a type which indicates the content type.
	// It can either be plain or html. By default, notes contents are assumed to
	// contain plain text.
	ContentType string `json:"contentType,omitempty"`
	// Value: Actual value of notes.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ContentType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ContentType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserAbout: JSON template for About (notes) of a user in Directory API.

func (UserAbout) MarshalJSON ¶
func (s UserAbout) MarshalJSON() ([]byte, error)
type UserAddress ¶
type UserAddress struct {
	// Country: Country.
	Country string `json:"country,omitempty"`
	// CountryCode: Country code.
	CountryCode string `json:"countryCode,omitempty"`
	// CustomType: Custom type.
	CustomType string `json:"customType,omitempty"`
	// ExtendedAddress: Extended Address.
	ExtendedAddress string `json:"extendedAddress,omitempty"`
	// Formatted: Formatted address.
	Formatted string `json:"formatted,omitempty"`
	// Locality: Locality.
	Locality string `json:"locality,omitempty"`
	// PoBox: Other parts of address.
	PoBox string `json:"poBox,omitempty"`
	// PostalCode: Postal code.
	PostalCode string `json:"postalCode,omitempty"`
	// Primary: If this is user's primary address. Only one entry could be marked
	// as primary.
	Primary bool `json:"primary,omitempty"`
	// Region: Region.
	Region string `json:"region,omitempty"`
	// SourceIsStructured: User supplied address was structured. Structured
	// addresses are NOT supported at this time. You might be able to write
	// structured addresses but any values will eventually be clobbered.
	SourceIsStructured bool `json:"sourceIsStructured,omitempty"`
	// StreetAddress: Street.
	StreetAddress string `json:"streetAddress,omitempty"`
	// Type: Each entry can have a type which indicates standard values of that
	// entry. For example address could be of home work etc. In addition to the
	// standard type an entry can have a custom type and can take any value. Such
	// type should have the CUSTOM value as type and also have a customType value.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Country") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Country") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserAddress: JSON template for address.

func (UserAddress) MarshalJSON ¶
func (s UserAddress) MarshalJSON() ([]byte, error)
type UserAlias ¶
added in v0.93.0
type UserAlias struct {
	// Alias: The alias email address.
	Alias string `json:"alias,omitempty"`
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Id: The unique ID for the user.
	Id string `json:"id,omitempty"`
	// Kind: The type of the API resource. For Alias resources, the value is
	// `admin#directory#alias`.
	Kind string `json:"kind,omitempty"`
	// PrimaryEmail: The user's primary email address.
	PrimaryEmail string `json:"primaryEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alias") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alias") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserAlias: The Directory API manages aliases, which are alternative email addresses.

func (UserAlias) MarshalJSON ¶
added in v0.93.0
func (s UserAlias) MarshalJSON() ([]byte, error)
type UserEmail ¶
type UserEmail struct {
	// Address: Email id of the user.
	Address string `json:"address,omitempty"`
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// Primary: If this is user's primary email. Only one entry could be marked as
	// primary.
	Primary bool `json:"primary,omitempty"`
	// PublicKeyEncryptionCertificates: Public Key Encryption Certificates. Current
	// limit: 1 per email address, and 5 per user.
	PublicKeyEncryptionCertificates *UserEmailPublicKeyEncryptionCertificates `json:"public_key_encryption_certificates,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example email could be of home, work etc. In addition to the
	// standard type, an entry can have a custom type and can take any value Such
	// types should have the CUSTOM value as type and also have a customType value.
	Type string `json:"type,omitempty"`
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

UserEmail: JSON template for an email.

func (UserEmail) MarshalJSON ¶
func (s UserEmail) MarshalJSON() ([]byte, error)
type UserEmailPublicKeyEncryptionCertificates ¶
added in v0.151.0
type UserEmailPublicKeyEncryptionCertificates struct {
	// Certificate: X.509 encryption certificate in `PEM` format. Must only be an
	// end-entity (leaf) certificate.
	Certificate string `json:"certificate,omitempty"`
	// IsDefault: Whether this is the default certificate for the given email
	// address.
	IsDefault bool `json:"is_default,omitempty"`
	// State: Denotes the certificate's state in its lifecycle. Possible values are
	// `not_yet_validated`, `valid`, `invalid`, `expired`, and `revoked`.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Certificate") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Certificate") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserEmailPublicKeyEncryptionCertificates: Public Key Encryption Certificates. Current limit: 1 per email address, and 5 per user.

func (UserEmailPublicKeyEncryptionCertificates) MarshalJSON ¶
added in v0.151.0
func (s UserEmailPublicKeyEncryptionCertificates) MarshalJSON() ([]byte, error)
type UserExternalId ¶
type UserExternalId struct {
	// CustomType: Custom type.
	CustomType string `json:"customType,omitempty"`
	// Type: The type of the Id.
	Type string `json:"type,omitempty"`
	// Value: The value of the id.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserExternalId: JSON template for an externalId entry.

func (UserExternalId) MarshalJSON ¶
func (s UserExternalId) MarshalJSON() ([]byte, error)
type UserGender ¶
type UserGender struct {
	// AddressMeAs: AddressMeAs. A human-readable string containing the proper way
	// to refer to the profile owner by humans for example he/him/his or
	// they/them/their.
	AddressMeAs string `json:"addressMeAs,omitempty"`
	// CustomGender: Custom gender.
	CustomGender string `json:"customGender,omitempty"`
	// Type: Gender.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AddressMeAs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AddressMeAs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (UserGender) MarshalJSON ¶
func (s UserGender) MarshalJSON() ([]byte, error)
type UserIm ¶
type UserIm struct {
	// CustomProtocol: Custom protocol.
	CustomProtocol string `json:"customProtocol,omitempty"`
	// CustomType: Custom type.
	CustomType string `json:"customType,omitempty"`
	// Im: Instant messenger id.
	Im string `json:"im,omitempty"`
	// Primary: If this is user's primary im. Only one entry could be marked as
	// primary.
	Primary bool `json:"primary,omitempty"`
	// Protocol: Protocol used in the instant messenger. It should be one of the
	// values from ImProtocolTypes map. Similar to type it can take a CUSTOM value
	// and specify the custom name in customProtocol field.
	Protocol string `json:"protocol,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example instant messengers could be of home work etc. In addition
	// to the standard type an entry can have a custom type and can take any value.
	// Such types should have the CUSTOM value as type and also have a customType
	// value.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomProtocol") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomProtocol") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserIm: JSON template for instant messenger of an user.

func (UserIm) MarshalJSON ¶
func (s UserIm) MarshalJSON() ([]byte, error)
type UserKeyword ¶
type UserKeyword struct {
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// Type: Each entry can have a type which indicates standard type of that
	// entry. For example keyword could be of type occupation or outlook. In
	// addition to the standard type an entry can have a custom type and can give
	// it any name. Such types should have the CUSTOM value as type and also have a
	// customType value.
	Type string `json:"type,omitempty"`
	// Value: Keyword.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserKeyword: JSON template for a keyword entry.

func (UserKeyword) MarshalJSON ¶
func (s UserKeyword) MarshalJSON() ([]byte, error)
type UserLanguage ¶
type UserLanguage struct {
	// CustomLanguage: Other language. User can provide their own language name if
	// there is no corresponding ISO 639 language code. If this is set,
	// `languageCode` can't be set.
	CustomLanguage string `json:"customLanguage,omitempty"`
	// LanguageCode: ISO 639 string representation of a language. See Language
	// Codes (/admin-sdk/directory/v1/languages) for the list of supported codes.
	// Valid language codes outside the supported set will be accepted by the API
	// but may lead to unexpected behavior. Illegal values cause `SchemaException`.
	// If this is set, `customLanguage` can't be set.
	LanguageCode string `json:"languageCode,omitempty"`
	// Preference: Optional. If present, controls whether the specified
	// `languageCode` is the user's preferred language. If `customLanguage` is set,
	// this can't be set. Allowed values are `preferred` and `not_preferred`.
	Preference string `json:"preference,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomLanguage") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomLanguage") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserLanguage: JSON template for a language entry.

func (UserLanguage) MarshalJSON ¶
func (s UserLanguage) MarshalJSON() ([]byte, error)
type UserLocation ¶
type UserLocation struct {
	// Area: Textual location. This is most useful for display purposes to
	// concisely describe the location. For example 'Mountain View, CA', 'Near
	// Seattle', 'US-NYC-9TH 9A209A.”
	Area string `json:"area,omitempty"`
	// BuildingId: Building Identifier.
	BuildingId string `json:"buildingId,omitempty"`
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// DeskCode: Most specific textual code of individual desk location.
	DeskCode string `json:"deskCode,omitempty"`
	// FloorName: Floor name/number.
	FloorName string `json:"floorName,omitempty"`
	// FloorSection: Floor section. More specific location within the floor. For
	// example if a floor is divided into sections 'A', 'B' and 'C' this field
	// would identify one of those values.
	FloorSection string `json:"floorSection,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example location could be of types default and desk. In addition
	// to standard type an entry can have a custom type and can give it any name.
	// Such types should have 'custom' as type and also have a customType value.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Area") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Area") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserLocation: JSON template for a location entry.

func (UserLocation) MarshalJSON ¶
func (s UserLocation) MarshalJSON() ([]byte, error)
type UserMakeAdmin ¶
type UserMakeAdmin struct {
	// Status: Indicates the administrator status of the user.
	Status bool `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Status") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Status") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (UserMakeAdmin) MarshalJSON ¶
func (s UserMakeAdmin) MarshalJSON() ([]byte, error)
type UserName ¶
type UserName struct {
	// DisplayName: The user's display name. Limit: 256 characters.
	DisplayName string `json:"displayName,omitempty"`
	// FamilyName: The user's last name. Required when creating a user account.
	FamilyName string `json:"familyName,omitempty"`
	// FullName: The user's full name formed by concatenating the first and last
	// name values.
	FullName string `json:"fullName,omitempty"`
	// GivenName: The user's first name. Required when creating a user account.
	GivenName string `json:"givenName,omitempty"`
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
func (UserName) MarshalJSON ¶
func (s UserName) MarshalJSON() ([]byte, error)
type UserOrganization ¶
type UserOrganization struct {
	// CostCenter: The cost center of the users department.
	CostCenter string `json:"costCenter,omitempty"`
	// CustomType: Custom type.
	CustomType string `json:"customType,omitempty"`
	// Department: Department within the organization.
	Department string `json:"department,omitempty"`
	// Description: Description of the organization.
	Description string `json:"description,omitempty"`
	// Domain: The domain to which the organization belongs to.
	Domain string `json:"domain,omitempty"`
	// FullTimeEquivalent: The full-time equivalent millipercent within the
	// organization (100000 = 100%).
	FullTimeEquivalent int64 `json:"fullTimeEquivalent,omitempty"`
	// Location: Location of the organization. This need not be fully qualified
	// address.
	Location string `json:"location,omitempty"`
	// Name: Name of the organization
	Name string `json:"name,omitempty"`
	// Primary: If it user's primary organization.
	Primary bool `json:"primary,omitempty"`
	// Symbol: Symbol of the organization.
	Symbol string `json:"symbol,omitempty"`
	// Title: Title (designation) of the user in the organization.
	Title string `json:"title,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example organization could be of school work etc. In addition to
	// the standard type an entry can have a custom type and can give it any name.
	// Such types should have the CUSTOM value as type and also have a CustomType
	// value.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CostCenter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CostCenter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserOrganization: JSON template for an organization entry.

func (UserOrganization) MarshalJSON ¶
func (s UserOrganization) MarshalJSON() ([]byte, error)
type UserPhone ¶
type UserPhone struct {
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// Primary: If this is user's primary phone or not.
	Primary bool `json:"primary,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example phone could be of home_fax work mobile etc. In addition
	// to the standard type an entry can have a custom type and can give it any
	// name. Such types should have the CUSTOM value as type and also have a
	// customType value.
	Type string `json:"type,omitempty"`
	// Value: Phone number.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserPhone: JSON template for a phone entry.

func (UserPhone) MarshalJSON ¶
func (s UserPhone) MarshalJSON() ([]byte, error)
type UserPhoto ¶
type UserPhoto struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Height: Height of the photo in pixels.
	Height int64 `json:"height,omitempty"`
	// Id: The ID the API uses to uniquely identify the user.
	Id string `json:"id,omitempty"`
	// Kind: The type of the API resource. For Photo resources, this is
	// `admin#directory#user#photo`.
	Kind string `json:"kind,omitempty"`
	// MimeType: The MIME type of the photo. Allowed values are `JPEG`, `PNG`,
	// `GIF`, `BMP`, `TIFF`, and web-safe base64 encoding.
	MimeType string `json:"mimeType,omitempty"`
	// PhotoData: The user photo's upload data in web-safe Base64
	// (https://en.wikipedia.org/wiki/Base64#URL_applications) format in bytes.
	// This means: * The slash (/) character is replaced with the underscore (_)
	// character. * The plus sign (+) character is replaced with the hyphen (-)
	// character. * The equals sign (=) character is replaced with the asterisk
	// (*). * For padding, the period (.) character is used instead of the RFC-4648
	// baseURL definition which uses the equals sign (=) for padding. This is done
	// to simplify URL-parsing. * Whatever the size of the photo being uploaded,
	// the API downsizes it to 96x96 pixels.
	PhotoData string `json:"photoData,omitempty"`
	// PrimaryEmail: The user's primary email address.
	PrimaryEmail string `json:"primaryEmail,omitempty"`
	// Width: Width of the photo in pixels.
	Width int64 `json:"width,omitempty"`

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
func (UserPhoto) MarshalJSON ¶
func (s UserPhoto) MarshalJSON() ([]byte, error)
type UserPosixAccount ¶
type UserPosixAccount struct {
	// AccountId: A POSIX account field identifier.
	AccountId string `json:"accountId,omitempty"`
	// Gecos: The GECOS (user information) for this account.
	Gecos string `json:"gecos,omitempty"`
	// Gid: The default group ID.
	Gid uint64 `json:"gid,omitempty,string"`
	// HomeDirectory: The path to the home directory for this account.
	HomeDirectory string `json:"homeDirectory,omitempty"`
	// OperatingSystemType: The operating system type for this account.
	OperatingSystemType string `json:"operatingSystemType,omitempty"`
	// Primary: If this is user's primary account within the SystemId.
	Primary bool `json:"primary,omitempty"`
	// Shell: The path to the login shell for this account.
	Shell string `json:"shell,omitempty"`
	// SystemId: System identifier for which account Username or Uid apply to.
	SystemId string `json:"systemId,omitempty"`
	// Uid: The POSIX compliant user ID.
	Uid uint64 `json:"uid,omitempty,string"`
	// Username: The username of the account.
	Username string `json:"username,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserPosixAccount: JSON template for a POSIX account entry.

func (UserPosixAccount) MarshalJSON ¶
func (s UserPosixAccount) MarshalJSON() ([]byte, error)
type UserRelation ¶
type UserRelation struct {
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// Type: The relation of the user. Some of the possible values are mother
	// father sister brother manager assistant partner.
	Type string `json:"type,omitempty"`
	// Value: The name of the relation.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserRelation: JSON template for a relation entry.

func (UserRelation) MarshalJSON ¶
func (s UserRelation) MarshalJSON() ([]byte, error)
type UserSshPublicKey ¶
type UserSshPublicKey struct {
	// ExpirationTimeUsec: An expiration time in microseconds since epoch.
	ExpirationTimeUsec int64 `json:"expirationTimeUsec,omitempty,string"`
	// Fingerprint: A SHA-256 fingerprint of the SSH public key. (Read-only)
	Fingerprint string `json:"fingerprint,omitempty"`
	// Key: An SSH public key.
	Key string `json:"key,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExpirationTimeUsec") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpirationTimeUsec") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserSshPublicKey: JSON template for a POSIX account entry.

func (UserSshPublicKey) MarshalJSON ¶
func (s UserSshPublicKey) MarshalJSON() ([]byte, error)
type UserUndelete ¶
type UserUndelete struct {
	// OrgUnitPath: OrgUnit of User
	OrgUnitPath string `json:"orgUnitPath,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OrgUnitPath") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OrgUnitPath") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (UserUndelete) MarshalJSON ¶
func (s UserUndelete) MarshalJSON() ([]byte, error)
type UserWebsite ¶
type UserWebsite struct {
	// CustomType: Custom Type.
	CustomType string `json:"customType,omitempty"`
	// Primary: If this is user's primary website or not.
	Primary bool `json:"primary,omitempty"`
	// Type: Each entry can have a type which indicates standard types of that
	// entry. For example website could be of home work blog etc. In addition to
	// the standard type an entry can have a custom type and can give it any name.
	// Such types should have the CUSTOM value as type and also have a customType
	// value.
	Type string `json:"type,omitempty"`
	// Value: Website.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserWebsite: JSON template for a website entry.

func (UserWebsite) MarshalJSON ¶
func (s UserWebsite) MarshalJSON() ([]byte, error)
type Users ¶
type Users struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: Kind of resource this is.
	Kind string `json:"kind,omitempty"`
	// NextPageToken: Token used to access next page of this result. The page token
	// is only valid for three days.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// TriggerEvent: Event that triggered this response (only used in case of Push
	// Response)
	TriggerEvent string `json:"trigger_event,omitempty"`
	// Users: A list of user objects.
	Users []*User `json:"users,omitempty"`

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
func (Users) MarshalJSON ¶
func (s Users) MarshalJSON() ([]byte, error)
type UsersAliasesDeleteCall ¶
type UsersAliasesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersAliasesDeleteCall) Context ¶
func (c *UsersAliasesDeleteCall) Context(ctx context.Context) *UsersAliasesDeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersAliasesDeleteCall) Do ¶
func (c *UsersAliasesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.aliases.delete" call.

func (*UsersAliasesDeleteCall) Fields ¶
func (c *UsersAliasesDeleteCall) Fields(s ...googleapi.Field) *UsersAliasesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersAliasesDeleteCall) Header ¶
func (c *UsersAliasesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersAliasesInsertCall ¶
type UsersAliasesInsertCall struct {
	// contains filtered or unexported fields
}
func (*UsersAliasesInsertCall) Context ¶
func (c *UsersAliasesInsertCall) Context(ctx context.Context) *UsersAliasesInsertCall

Context sets the context to be used in this call's Do method.

func (*UsersAliasesInsertCall) Do ¶
func (c *UsersAliasesInsertCall) Do(opts ...googleapi.CallOption) (*Alias, error)

Do executes the "directory.users.aliases.insert" call. Any non-2xx status code is an error. Response headers are in either *Alias.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersAliasesInsertCall) Fields ¶
func (c *UsersAliasesInsertCall) Fields(s ...googleapi.Field) *UsersAliasesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersAliasesInsertCall) Header ¶
func (c *UsersAliasesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersAliasesListCall ¶
type UsersAliasesListCall struct {
	// contains filtered or unexported fields
}
func (*UsersAliasesListCall) Context ¶
func (c *UsersAliasesListCall) Context(ctx context.Context) *UsersAliasesListCall

Context sets the context to be used in this call's Do method.

func (*UsersAliasesListCall) Do ¶
func (c *UsersAliasesListCall) Do(opts ...googleapi.CallOption) (*Aliases, error)

Do executes the "directory.users.aliases.list" call. Any non-2xx status code is an error. Response headers are in either *Aliases.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersAliasesListCall) Event ¶
func (c *UsersAliasesListCall) Event(event string) *UsersAliasesListCall

Event sets the optional parameter "event": Events to watch for.

Possible values:

"add" - Alias Created Event
"delete" - Alias Deleted Event

func (*UsersAliasesListCall) Fields ¶
func (c *UsersAliasesListCall) Fields(s ...googleapi.Field) *UsersAliasesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersAliasesListCall) Header ¶
func (c *UsersAliasesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersAliasesListCall) IfNoneMatch ¶
func (c *UsersAliasesListCall) IfNoneMatch(entityTag string) *UsersAliasesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type UsersAliasesService ¶
type UsersAliasesService struct {
	// contains filtered or unexported fields
}
func NewUsersAliasesService ¶
func NewUsersAliasesService(s *Service) *UsersAliasesService
func (*UsersAliasesService) Delete ¶
func (r *UsersAliasesService) Delete(userKey string, alias string) *UsersAliasesDeleteCall

Delete: Removes an alias.

alias: The alias to be removed.
userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersAliasesService) Insert ¶
func (r *UsersAliasesService) Insert(userKey string, alias *Alias) *UsersAliasesInsertCall

Insert: Adds an alias.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersAliasesService) List ¶
func (r *UsersAliasesService) List(userKey string) *UsersAliasesListCall

List: Lists all aliases for a user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersAliasesService) Watch ¶
func (r *UsersAliasesService) Watch(userKey string, channel *Channel) *UsersAliasesWatchCall

Watch: Watches for changes in users list.

- userKey: Email or immutable ID of the user.

type UsersAliasesWatchCall ¶
type UsersAliasesWatchCall struct {
	// contains filtered or unexported fields
}
func (*UsersAliasesWatchCall) Context ¶
func (c *UsersAliasesWatchCall) Context(ctx context.Context) *UsersAliasesWatchCall

Context sets the context to be used in this call's Do method.

func (*UsersAliasesWatchCall) Do ¶
func (c *UsersAliasesWatchCall) Do(opts ...googleapi.CallOption) (*Channel, error)

Do executes the "directory.users.aliases.watch" call. Any non-2xx status code is an error. Response headers are in either *Channel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersAliasesWatchCall) Event ¶
func (c *UsersAliasesWatchCall) Event(event string) *UsersAliasesWatchCall

Event sets the optional parameter "event": Events to watch for.

Possible values:

"add" - Alias Created Event
"delete" - Alias Deleted Event

func (*UsersAliasesWatchCall) Fields ¶
func (c *UsersAliasesWatchCall) Fields(s ...googleapi.Field) *UsersAliasesWatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersAliasesWatchCall) Header ¶
func (c *UsersAliasesWatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersCreateGuestCall ¶
added in v0.257.0
type UsersCreateGuestCall struct {
	// contains filtered or unexported fields
}
func (*UsersCreateGuestCall) Context ¶
added in v0.257.0
func (c *UsersCreateGuestCall) Context(ctx context.Context) *UsersCreateGuestCall

Context sets the context to be used in this call's Do method.

func (*UsersCreateGuestCall) Do ¶
added in v0.257.0
func (c *UsersCreateGuestCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "directory.users.createGuest" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersCreateGuestCall) Fields ¶
added in v0.257.0
func (c *UsersCreateGuestCall) Fields(s ...googleapi.Field) *UsersCreateGuestCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersCreateGuestCall) Header ¶
added in v0.257.0
func (c *UsersCreateGuestCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersDeleteCall ¶
type UsersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersDeleteCall) Context ¶
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersDeleteCall) Do ¶
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.delete" call.

func (*UsersDeleteCall) Fields ¶
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersDeleteCall) Header ¶
func (c *UsersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersGetCall ¶
type UsersGetCall struct {
	// contains filtered or unexported fields
}
func (*UsersGetCall) Context ¶
func (c *UsersGetCall) Context(ctx context.Context) *UsersGetCall

Context sets the context to be used in this call's Do method.

func (*UsersGetCall) CustomFieldMask ¶
func (c *UsersGetCall) CustomFieldMask(customFieldMask string) *UsersGetCall

CustomFieldMask sets the optional parameter "customFieldMask": A comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when `projection=custom`.

func (*UsersGetCall) Do ¶
func (c *UsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "directory.users.get" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersGetCall) Fields ¶
func (c *UsersGetCall) Fields(s ...googleapi.Field) *UsersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersGetCall) Header ¶
func (c *UsersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersGetCall) IfNoneMatch ¶
func (c *UsersGetCall) IfNoneMatch(entityTag string) *UsersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*UsersGetCall) Projection ¶
func (c *UsersGetCall) Projection(projection string) *UsersGetCall

Projection sets the optional parameter "projection": What subset of fields to fetch for this user.

Possible values:

"basic" (default) - Do not include any custom fields for the user.
"custom" - Include custom fields from schemas requested in


`customFieldMask`.

"full" - Include all fields associated with this user.

func (*UsersGetCall) ViewType ¶
func (c *UsersGetCall) ViewType(viewType string) *UsersGetCall

ViewType sets the optional parameter "viewType": Whether to fetch the administrator-only or domain-wide public view of the user. For more information, see Retrieve a user as a non-administrator (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#retrieve_users_non_admin).

Possible values:

"admin_view" (default) - Results include both administrator-only and


domain-public fields for the user.

"domain_public" - Results only include fields for the user that are


publicly visible to other users in the domain.

type UsersInsertCall ¶
type UsersInsertCall struct {
	// contains filtered or unexported fields
}
func (*UsersInsertCall) Context ¶
func (c *UsersInsertCall) Context(ctx context.Context) *UsersInsertCall

Context sets the context to be used in this call's Do method.

func (*UsersInsertCall) Do ¶
func (c *UsersInsertCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "directory.users.insert" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersInsertCall) Fields ¶
func (c *UsersInsertCall) Fields(s ...googleapi.Field) *UsersInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersInsertCall) Header ¶
func (c *UsersInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersInsertCall) ResolveConflictAccount ¶
added in v0.138.0
func (c *UsersInsertCall) ResolveConflictAccount(resolveConflictAccount bool) *UsersInsertCall

ResolveConflictAccount sets the optional parameter "resolveConflictAccount": If set to `true`, the option selected for handling unmanaged user accounts (https://support.google.com/a/answer/11112794) will apply. Default: `false`

type UsersListCall ¶
type UsersListCall struct {
	// contains filtered or unexported fields
}
func (*UsersListCall) Context ¶
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall

Context sets the context to be used in this call's Do method.

func (*UsersListCall) CustomFieldMask ¶
func (c *UsersListCall) CustomFieldMask(customFieldMask string) *UsersListCall

CustomFieldMask sets the optional parameter "customFieldMask": A comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when `projection=custom`.

func (*UsersListCall) Customer ¶
func (c *UsersListCall) Customer(customer string) *UsersListCall

Customer sets the optional parameter "customer": The unique ID for the customer's Google Workspace account. In case of a multi-domain account, to fetch all users for a customer, use this field instead of `domain`. You can also use the `my_customer` alias to represent your account's `customerId`. The `customerId` is also returned as part of the Users (https://developers.google.com/workspace/admin/directory/v1/reference/users) resource. You must provide either the `customer` or the `domain` parameter.

func (*UsersListCall) Do ¶
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*Users, error)

Do executes the "directory.users.list" call. Any non-2xx status code is an error. Response headers are in either *Users.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersListCall) Domain ¶
func (c *UsersListCall) Domain(domain string) *UsersListCall

Domain sets the optional parameter "domain": The domain name. Use this field to get users from only one domain. To return all domains for a customer account, use the `customer` query parameter instead. Either the `customer` or the `domain` parameter must be provided.

func (*UsersListCall) Event ¶
func (c *UsersListCall) Event(event string) *UsersListCall

Event sets the optional parameter "event": Event on which subscription is intended (if subscribing)

Possible values:

"add" - User Created Event
"delete" - User Deleted Event
"makeAdmin" - User Admin Status Change Event
"undelete" - User Undeleted Event
"update" - User Updated Event

func (*UsersListCall) Fields ¶
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersListCall) Header ¶
func (c *UsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersListCall) IfNoneMatch ¶
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*UsersListCall) MaxResults ¶
func (c *UsersListCall) MaxResults(maxResults int64) *UsersListCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*UsersListCall) OrderBy ¶
func (c *UsersListCall) OrderBy(orderBy string) *UsersListCall

OrderBy sets the optional parameter "orderBy": Property to use for sorting results.

Possible values:

"email" - Primary email of the user.
"familyName" - User's family name.
"givenName" - User's given name.

func (*UsersListCall) PageToken ¶
func (c *UsersListCall) PageToken(pageToken string) *UsersListCall

PageToken sets the optional parameter "pageToken": Token to specify next page in the list. The page token is only valid for three days.

func (*UsersListCall) Pages ¶
func (c *UsersListCall) Pages(ctx context.Context, f func(*Users) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*UsersListCall) Projection ¶
func (c *UsersListCall) Projection(projection string) *UsersListCall

Projection sets the optional parameter "projection": What subset of fields to fetch for this user.

Possible values:

"basic" (default) - Do not include any custom fields for the user.
"custom" - Include custom fields from schemas requested in


`customFieldMask`.

"full" - Include all fields associated with this user.

func (*UsersListCall) Query ¶
func (c *UsersListCall) Query(query string) *UsersListCall

Query sets the optional parameter "query": Query string for searching user fields. For more information on constructing user queries, see Search for Users (https://developers.google.com/workspace/admin/directory/v1/guides/search-users).

func (*UsersListCall) ShowDeleted ¶
func (c *UsersListCall) ShowDeleted(showDeleted string) *UsersListCall

ShowDeleted sets the optional parameter "showDeleted": If set to `true`, retrieves the list of deleted users. (Default: `false`)

func (*UsersListCall) SortOrder ¶
func (c *UsersListCall) SortOrder(sortOrder string) *UsersListCall

SortOrder sets the optional parameter "sortOrder": Whether to return results in ascending or descending order, ignoring case.

Possible values:

"ASCENDING" - Ascending order.
"DESCENDING" - Descending order.

func (*UsersListCall) ViewType ¶
func (c *UsersListCall) ViewType(viewType string) *UsersListCall

ViewType sets the optional parameter "viewType": Whether to fetch the administrator-only or domain-wide public view of the user. For more information, see Retrieve a user as a non-administrator (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#retrieve_users_non_admin).

Possible values:

"admin_view" (default) - Results include both administrator-only and


domain-public fields for the user.

"domain_public" - Results only include fields for the user that are


publicly visible to other users in the domain.

type UsersMakeAdminCall ¶
type UsersMakeAdminCall struct {
	// contains filtered or unexported fields
}
func (*UsersMakeAdminCall) Context ¶
func (c *UsersMakeAdminCall) Context(ctx context.Context) *UsersMakeAdminCall

Context sets the context to be used in this call's Do method.

func (*UsersMakeAdminCall) Do ¶
func (c *UsersMakeAdminCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.makeAdmin" call.

func (*UsersMakeAdminCall) Fields ¶
func (c *UsersMakeAdminCall) Fields(s ...googleapi.Field) *UsersMakeAdminCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersMakeAdminCall) Header ¶
func (c *UsersMakeAdminCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersPatchCall ¶
type UsersPatchCall struct {
	// contains filtered or unexported fields
}
func (*UsersPatchCall) Context ¶
func (c *UsersPatchCall) Context(ctx context.Context) *UsersPatchCall

Context sets the context to be used in this call's Do method.

func (*UsersPatchCall) Do ¶
func (c *UsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "directory.users.patch" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersPatchCall) Fields ¶
func (c *UsersPatchCall) Fields(s ...googleapi.Field) *UsersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPatchCall) Header ¶
func (c *UsersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersPhotosDeleteCall ¶
type UsersPhotosDeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersPhotosDeleteCall) Context ¶
func (c *UsersPhotosDeleteCall) Context(ctx context.Context) *UsersPhotosDeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersPhotosDeleteCall) Do ¶
func (c *UsersPhotosDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.photos.delete" call.

func (*UsersPhotosDeleteCall) Fields ¶
func (c *UsersPhotosDeleteCall) Fields(s ...googleapi.Field) *UsersPhotosDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPhotosDeleteCall) Header ¶
func (c *UsersPhotosDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersPhotosGetCall ¶
type UsersPhotosGetCall struct {
	// contains filtered or unexported fields
}
func (*UsersPhotosGetCall) Context ¶
func (c *UsersPhotosGetCall) Context(ctx context.Context) *UsersPhotosGetCall

Context sets the context to be used in this call's Do method.

func (*UsersPhotosGetCall) Do ¶
func (c *UsersPhotosGetCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)

Do executes the "directory.users.photos.get" call. Any non-2xx status code is an error. Response headers are in either *UserPhoto.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersPhotosGetCall) Fields ¶
func (c *UsersPhotosGetCall) Fields(s ...googleapi.Field) *UsersPhotosGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPhotosGetCall) Header ¶
func (c *UsersPhotosGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersPhotosGetCall) IfNoneMatch ¶
func (c *UsersPhotosGetCall) IfNoneMatch(entityTag string) *UsersPhotosGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type UsersPhotosPatchCall ¶
type UsersPhotosPatchCall struct {
	// contains filtered or unexported fields
}
func (*UsersPhotosPatchCall) Context ¶
func (c *UsersPhotosPatchCall) Context(ctx context.Context) *UsersPhotosPatchCall

Context sets the context to be used in this call's Do method.

func (*UsersPhotosPatchCall) Do ¶
func (c *UsersPhotosPatchCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)

Do executes the "directory.users.photos.patch" call. Any non-2xx status code is an error. Response headers are in either *UserPhoto.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersPhotosPatchCall) Fields ¶
func (c *UsersPhotosPatchCall) Fields(s ...googleapi.Field) *UsersPhotosPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPhotosPatchCall) Header ¶
func (c *UsersPhotosPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersPhotosService ¶
type UsersPhotosService struct {
	// contains filtered or unexported fields
}
func NewUsersPhotosService ¶
func NewUsersPhotosService(s *Service) *UsersPhotosService
func (*UsersPhotosService) Delete ¶
func (r *UsersPhotosService) Delete(userKey string) *UsersPhotosDeleteCall

Delete: Removes the user's photo.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersPhotosService) Get ¶
func (r *UsersPhotosService) Get(userKey string) *UsersPhotosGetCall

Get: Retrieves the user's photo.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersPhotosService) Patch ¶
func (r *UsersPhotosService) Patch(userKey string, userphoto *UserPhoto) *UsersPhotosPatchCall

Patch: Adds a photo for the user. This method supports patch semantics (https://developers.google.com/workspace/admin/directory/v1/guides/performance#patch).

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersPhotosService) Update ¶
func (r *UsersPhotosService) Update(userKey string, userphoto *UserPhoto) *UsersPhotosUpdateCall

Update: Adds a photo for the user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
type UsersPhotosUpdateCall ¶
type UsersPhotosUpdateCall struct {
	// contains filtered or unexported fields
}
func (*UsersPhotosUpdateCall) Context ¶
func (c *UsersPhotosUpdateCall) Context(ctx context.Context) *UsersPhotosUpdateCall

Context sets the context to be used in this call's Do method.

func (*UsersPhotosUpdateCall) Do ¶
func (c *UsersPhotosUpdateCall) Do(opts ...googleapi.CallOption) (*UserPhoto, error)

Do executes the "directory.users.photos.update" call. Any non-2xx status code is an error. Response headers are in either *UserPhoto.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersPhotosUpdateCall) Fields ¶
func (c *UsersPhotosUpdateCall) Fields(s ...googleapi.Field) *UsersPhotosUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPhotosUpdateCall) Header ¶
func (c *UsersPhotosUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersService ¶
type UsersService struct {
	Aliases *UsersAliasesService

	Photos *UsersPhotosService
	// contains filtered or unexported fields
}
func NewUsersService ¶
func NewUsersService(s *Service) *UsersService
func (*UsersService) CreateGuest ¶
added in v0.257.0
func (r *UsersService) CreateGuest(directoryuserscreateguestrequest *DirectoryUsersCreateGuestRequest) *UsersCreateGuestCall

CreateGuest: Create a guest user with access to a subset of Workspace capabilities (https://support.google.com/a/answer/16558545?hl=en). This feature is currently in Alpha. Please reach out to support if you are interested in trying this feature.

func (*UsersService) Delete ¶
func (r *UsersService) Delete(userKey string) *UsersDeleteCall

Delete: Deletes a user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) Get ¶
func (r *UsersService) Get(userKey string) *UsersGetCall

Get: Retrieves a user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) Insert ¶
func (r *UsersService) Insert(user *User) *UsersInsertCall

Insert: Creates a user. Mutate calls immediately following user creation might sometimes fail as the user isn't fully created due to propagation delay in our backends. Check the error details for the "User creation is not complete" message to see if this is the case. Retrying the calls after some time can help in this case. If `resolveConflictAccount` is set to `true`, a `202` response code means that a conflicting unmanaged account exists and was invited to join the organization. A `409` response code means that a conflicting account exists so the user wasn't created based on the handling unmanaged user accounts (https://support.google.com/a/answer/11112794) option selected.

func (*UsersService) List ¶
func (r *UsersService) List() *UsersListCall

List: Retrieves a paginated list of either deleted users or all users in a domain.

func (*UsersService) MakeAdmin ¶
func (r *UsersService) MakeAdmin(userKey string, usermakeadmin *UserMakeAdmin) *UsersMakeAdminCall

MakeAdmin: Makes a user a super administrator.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) Patch ¶
func (r *UsersService) Patch(userKey string, user *User) *UsersPatchCall

Patch: Updates a user using patch semantics. The update method should be used instead, because it also supports patch semantics and has better performance. If you're mapping an external identity to a Google identity, use the `update` (https://developers.google.com/workspace/admin/directory/v1/reference/users/update) method instead of the `patch` method. This method is unable to clear fields that contain repeated objects (`addresses`, `phones`, etc). Use the update method instead.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) SignOut ¶
added in v0.32.0
func (r *UsersService) SignOut(userKey string) *UsersSignOutCall

SignOut: Signs a user out of all web and device sessions and reset their sign-in cookies. User will have to sign in by authenticating again.

userKey: Identifies the target user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) Undelete ¶
func (r *UsersService) Undelete(userKey string, userundelete *UserUndelete) *UsersUndeleteCall

Undelete: Undeletes a deleted user.

- userKey: The immutable id of the user.

func (*UsersService) Update ¶
func (r *UsersService) Update(userKey string, user *User) *UsersUpdateCall

Update: Updates a user. This method supports patch semantics, meaning that you only need to include the fields you wish to update. Fields that are not present in the request will be preserved, and fields set to `null` will be cleared. For repeating fields that contain arrays, individual items in the array can't be patched piecemeal; they must be supplied in the request body with the desired values for all items. See the user accounts guide (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#update_user) for more information.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
func (*UsersService) Watch ¶
func (r *UsersService) Watch(channel *Channel) *UsersWatchCall

Watch: Watches for changes in users list.

type UsersSignOutCall ¶
added in v0.32.0
type UsersSignOutCall struct {
	// contains filtered or unexported fields
}
func (*UsersSignOutCall) Context ¶
added in v0.32.0
func (c *UsersSignOutCall) Context(ctx context.Context) *UsersSignOutCall

Context sets the context to be used in this call's Do method.

func (*UsersSignOutCall) Do ¶
added in v0.32.0
func (c *UsersSignOutCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.signOut" call.

func (*UsersSignOutCall) Fields ¶
added in v0.32.0
func (c *UsersSignOutCall) Fields(s ...googleapi.Field) *UsersSignOutCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersSignOutCall) Header ¶
added in v0.32.0
func (c *UsersSignOutCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersUndeleteCall ¶
type UsersUndeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersUndeleteCall) Context ¶
func (c *UsersUndeleteCall) Context(ctx context.Context) *UsersUndeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersUndeleteCall) Do ¶
func (c *UsersUndeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.users.undelete" call.

func (*UsersUndeleteCall) Fields ¶
func (c *UsersUndeleteCall) Fields(s ...googleapi.Field) *UsersUndeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersUndeleteCall) Header ¶
func (c *UsersUndeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersUpdateCall ¶
type UsersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*UsersUpdateCall) Context ¶
func (c *UsersUpdateCall) Context(ctx context.Context) *UsersUpdateCall

Context sets the context to be used in this call's Do method.

func (*UsersUpdateCall) Do ¶
func (c *UsersUpdateCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "directory.users.update" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersUpdateCall) Fields ¶
func (c *UsersUpdateCall) Fields(s ...googleapi.Field) *UsersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersUpdateCall) Header ¶
func (c *UsersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersWatchCall ¶
type UsersWatchCall struct {
	// contains filtered or unexported fields
}
func (*UsersWatchCall) Context ¶
func (c *UsersWatchCall) Context(ctx context.Context) *UsersWatchCall

Context sets the context to be used in this call's Do method.

func (*UsersWatchCall) CustomFieldMask ¶
func (c *UsersWatchCall) CustomFieldMask(customFieldMask string) *UsersWatchCall

CustomFieldMask sets the optional parameter "customFieldMask": Comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when projection=custom.

func (*UsersWatchCall) Customer ¶
func (c *UsersWatchCall) Customer(customer string) *UsersWatchCall

Customer sets the optional parameter "customer": Immutable ID of the Google Workspace account. In case of multi-domain, to fetch all users for a customer, fill this field instead of domain.

func (*UsersWatchCall) Do ¶
func (c *UsersWatchCall) Do(opts ...googleapi.CallOption) (*Channel, error)

Do executes the "directory.users.watch" call. Any non-2xx status code is an error. Response headers are in either *Channel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersWatchCall) Domain ¶
func (c *UsersWatchCall) Domain(domain string) *UsersWatchCall

Domain sets the optional parameter "domain": Name of the domain. Fill this field to get users from only this domain. To return all users in a multi-domain fill customer field instead."

func (*UsersWatchCall) Event ¶
func (c *UsersWatchCall) Event(event string) *UsersWatchCall

Event sets the optional parameter "event": Events to watch for.

Possible values:

"add" - User Created Event
"delete" - User Deleted Event
"makeAdmin" - User Admin Status Change Event
"undelete" - User Undeleted Event
"update" - User Updated Event

func (*UsersWatchCall) Fields ¶
func (c *UsersWatchCall) Fields(s ...googleapi.Field) *UsersWatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersWatchCall) Header ¶
func (c *UsersWatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersWatchCall) MaxResults ¶
func (c *UsersWatchCall) MaxResults(maxResults int64) *UsersWatchCall

MaxResults sets the optional parameter "maxResults": Maximum number of results to return.

func (*UsersWatchCall) OrderBy ¶
func (c *UsersWatchCall) OrderBy(orderBy string) *UsersWatchCall

OrderBy sets the optional parameter "orderBy": Column to use for sorting results

Possible values:

"email" - Primary email of the user.
"familyName" - User's family name.
"givenName" - User's given name.

func (*UsersWatchCall) PageToken ¶
func (c *UsersWatchCall) PageToken(pageToken string) *UsersWatchCall

PageToken sets the optional parameter "pageToken": Token to specify next page in the list

func (*UsersWatchCall) Projection ¶
func (c *UsersWatchCall) Projection(projection string) *UsersWatchCall

Projection sets the optional parameter "projection": What subset of fields to fetch for this user.

Possible values:

"basic" (default) - Do not include any custom fields for the user.
"custom" - Include custom fields from schemas mentioned in


customFieldMask.

"full" - Include all fields associated with this user.

func (*UsersWatchCall) Query ¶
func (c *UsersWatchCall) Query(query string) *UsersWatchCall

Query sets the optional parameter "query": Query string search. Contains one or more search clauses, each with a field, operator, and value. For complete documentation, go to Search for users (https://developers.google.com/workspace/admin/directory/v1/guides/search-users).

func (*UsersWatchCall) ShowDeleted ¶
func (c *UsersWatchCall) ShowDeleted(showDeleted string) *UsersWatchCall

ShowDeleted sets the optional parameter "showDeleted": If set to true, retrieves the list of deleted users. (Default: false)

func (*UsersWatchCall) SortOrder ¶
func (c *UsersWatchCall) SortOrder(sortOrder string) *UsersWatchCall

SortOrder sets the optional parameter "sortOrder": Whether to return results in ascending or descending order.

Possible values:

"ASCENDING" - Ascending order.
"DESCENDING" - Descending order.

func (*UsersWatchCall) ViewType ¶
func (c *UsersWatchCall) ViewType(viewType string) *UsersWatchCall

ViewType sets the optional parameter "viewType": Whether to fetch the administrator-only or domain-wide public view of the user. For more information, see Retrieve a user as a non-administrator (https://developers.google.com/workspace/admin/directory/v1/guides/manage-users#retrieve_users_non_admin).

Possible values:

"admin_view" (default) - Results include both administrator-only and


domain-public fields.

"domain_public" - Results only include fields for the user that are


publicly visible to other users in the domain.

type VerificationCode ¶
type VerificationCode struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Kind: The type of the resource. This is always
	// `admin#directory#verificationCode`.
	Kind string `json:"kind,omitempty"`
	// UserId: The obfuscated unique ID of the user.
	UserId string `json:"userId,omitempty"`
	// VerificationCode: A current verification code for the user. Invalidated or
	// used verification codes are not returned as part of the result.
	VerificationCode string `json:"verificationCode,omitempty"`
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

VerificationCode: The Directory API allows you to view, generate, and invalidate backup verification codes for a user.

func (VerificationCode) MarshalJSON ¶
func (s VerificationCode) MarshalJSON() ([]byte, error)
type VerificationCodes ¶
type VerificationCodes struct {
	// Etag: ETag of the resource.
	Etag string `json:"etag,omitempty"`
	// Items: A list of verification code resources.
	Items []*VerificationCode `json:"items,omitempty"`
	// Kind: The type of the resource. This is always
	// `admin#directory#verificationCodesList`.
	Kind string `json:"kind,omitempty"`

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

VerificationCodes: JSON response template for list verification codes operation in Directory API.

func (VerificationCodes) MarshalJSON ¶
func (s VerificationCodes) MarshalJSON() ([]byte, error)
type VerificationCodesGenerateCall ¶
type VerificationCodesGenerateCall struct {
	// contains filtered or unexported fields
}
func (*VerificationCodesGenerateCall) Context ¶
func (c *VerificationCodesGenerateCall) Context(ctx context.Context) *VerificationCodesGenerateCall

Context sets the context to be used in this call's Do method.

func (*VerificationCodesGenerateCall) Do ¶
func (c *VerificationCodesGenerateCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.verificationCodes.generate" call.

func (*VerificationCodesGenerateCall) Fields ¶
func (c *VerificationCodesGenerateCall) Fields(s ...googleapi.Field) *VerificationCodesGenerateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*VerificationCodesGenerateCall) Header ¶
func (c *VerificationCodesGenerateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type VerificationCodesInvalidateCall ¶
type VerificationCodesInvalidateCall struct {
	// contains filtered or unexported fields
}
func (*VerificationCodesInvalidateCall) Context ¶
func (c *VerificationCodesInvalidateCall) Context(ctx context.Context) *VerificationCodesInvalidateCall

Context sets the context to be used in this call's Do method.

func (*VerificationCodesInvalidateCall) Do ¶
func (c *VerificationCodesInvalidateCall) Do(opts ...googleapi.CallOption) error

Do executes the "directory.verificationCodes.invalidate" call.

func (*VerificationCodesInvalidateCall) Fields ¶
func (c *VerificationCodesInvalidateCall) Fields(s ...googleapi.Field) *VerificationCodesInvalidateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*VerificationCodesInvalidateCall) Header ¶
func (c *VerificationCodesInvalidateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type VerificationCodesListCall ¶
type VerificationCodesListCall struct {
	// contains filtered or unexported fields
}
func (*VerificationCodesListCall) Context ¶
func (c *VerificationCodesListCall) Context(ctx context.Context) *VerificationCodesListCall

Context sets the context to be used in this call's Do method.

func (*VerificationCodesListCall) Do ¶
func (c *VerificationCodesListCall) Do(opts ...googleapi.CallOption) (*VerificationCodes, error)

Do executes the "directory.verificationCodes.list" call. Any non-2xx status code is an error. Response headers are in either *VerificationCodes.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*VerificationCodesListCall) Fields ¶
func (c *VerificationCodesListCall) Fields(s ...googleapi.Field) *VerificationCodesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*VerificationCodesListCall) Header ¶
func (c *VerificationCodesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*VerificationCodesListCall) IfNoneMatch ¶
func (c *VerificationCodesListCall) IfNoneMatch(entityTag string) *VerificationCodesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type VerificationCodesService ¶
type VerificationCodesService struct {
	// contains filtered or unexported fields
}
func NewVerificationCodesService ¶
func NewVerificationCodesService(s *Service) *VerificationCodesService
func (*VerificationCodesService) Generate ¶
func (r *VerificationCodesService) Generate(userKey string) *VerificationCodesGenerateCall

Generate: Generates new backup verification codes for the user.

- userKey: Email or immutable ID of the user.

func (*VerificationCodesService) Invalidate ¶
func (r *VerificationCodesService) Invalidate(userKey string) *VerificationCodesInvalidateCall

Invalidate: Invalidates the current backup verification codes for the user.

- userKey: Email or immutable ID of the user.

func (*VerificationCodesService) List ¶
func (r *VerificationCodesService) List(userKey string) *VerificationCodesListCall

List: Returns the current set of valid backup verification codes for the specified user.

userKey: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
 Source Files ¶
View all Source files
admin-gen.go
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

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more.
Okay
