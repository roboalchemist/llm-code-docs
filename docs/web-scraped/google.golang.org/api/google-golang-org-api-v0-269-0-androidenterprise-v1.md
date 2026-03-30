# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/androidenterprise/v1

Title: androidenterprise package - google.golang.org/api/androidenterprise/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/androidenterprise/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
androidenterprise
 
v1
androidenterprise
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

Package androidenterprise provides access to the Google Play EMM API.

For product documentation, see: https://developers.google.com/android/work/play/emm-api

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/androidenterprise/v1"
...
ctx := context.Background()
androidenterpriseService, err := androidenterprise.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

androidenterpriseService, err := androidenterprise.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
androidenterpriseService, err := androidenterprise.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Administrator
func (s Administrator) MarshalJSON() ([]byte, error)
type AdministratorWebToken
func (s AdministratorWebToken) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpec
func (s AdministratorWebTokenSpec) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecManagedConfigurations
func (s AdministratorWebTokenSpecManagedConfigurations) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecPlaySearch
func (s AdministratorWebTokenSpecPlaySearch) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecPrivateApps
func (s AdministratorWebTokenSpecPrivateApps) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecStoreBuilder
func (s AdministratorWebTokenSpecStoreBuilder) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecWebApps
func (s AdministratorWebTokenSpecWebApps) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecZeroTouch
func (s AdministratorWebTokenSpecZeroTouch) MarshalJSON() ([]byte, error)
type AppRestrictionsSchema
func (s AppRestrictionsSchema) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaChangeEvent
func (s AppRestrictionsSchemaChangeEvent) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaRestriction
func (s AppRestrictionsSchemaRestriction) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaRestrictionRestrictionValue
func (s AppRestrictionsSchemaRestrictionRestrictionValue) MarshalJSON() ([]byte, error)
type AppState
func (s AppState) MarshalJSON() ([]byte, error)
type AppUpdateEvent
func (s AppUpdateEvent) MarshalJSON() ([]byte, error)
type AppVersion
func (s AppVersion) MarshalJSON() ([]byte, error)
type ApprovalUrlInfo
func (s ApprovalUrlInfo) MarshalJSON() ([]byte, error)
type AuthenticationToken
func (s AuthenticationToken) MarshalJSON() ([]byte, error)
type AutoInstallConstraint
func (s AutoInstallConstraint) MarshalJSON() ([]byte, error)
type AutoInstallPolicy
func (s AutoInstallPolicy) MarshalJSON() ([]byte, error)
type ConfigurationVariables
func (s ConfigurationVariables) MarshalJSON() ([]byte, error)
type Device
func (s Device) MarshalJSON() ([]byte, error)
type DeviceReport
func (s DeviceReport) MarshalJSON() ([]byte, error)
type DeviceReportUpdateEvent
func (s DeviceReportUpdateEvent) MarshalJSON() ([]byte, error)
type DeviceState
func (s DeviceState) MarshalJSON() ([]byte, error)
type DevicesForceReportUploadCall
func (c *DevicesForceReportUploadCall) Context(ctx context.Context) *DevicesForceReportUploadCall
func (c *DevicesForceReportUploadCall) Do(opts ...googleapi.CallOption) error
func (c *DevicesForceReportUploadCall) Fields(s ...googleapi.Field) *DevicesForceReportUploadCall
func (c *DevicesForceReportUploadCall) Header() http.Header
type DevicesGetCall
func (c *DevicesGetCall) Context(ctx context.Context) *DevicesGetCall
func (c *DevicesGetCall) Do(opts ...googleapi.CallOption) (*Device, error)
func (c *DevicesGetCall) Fields(s ...googleapi.Field) *DevicesGetCall
func (c *DevicesGetCall) Header() http.Header
func (c *DevicesGetCall) IfNoneMatch(entityTag string) *DevicesGetCall
type DevicesGetStateCall
func (c *DevicesGetStateCall) Context(ctx context.Context) *DevicesGetStateCall
func (c *DevicesGetStateCall) Do(opts ...googleapi.CallOption) (*DeviceState, error)
func (c *DevicesGetStateCall) Fields(s ...googleapi.Field) *DevicesGetStateCall
func (c *DevicesGetStateCall) Header() http.Header
func (c *DevicesGetStateCall) IfNoneMatch(entityTag string) *DevicesGetStateCall
type DevicesListCall
func (c *DevicesListCall) Context(ctx context.Context) *DevicesListCall
func (c *DevicesListCall) Do(opts ...googleapi.CallOption) (*DevicesListResponse, error)
func (c *DevicesListCall) Fields(s ...googleapi.Field) *DevicesListCall
func (c *DevicesListCall) Header() http.Header
func (c *DevicesListCall) IfNoneMatch(entityTag string) *DevicesListCall
type DevicesListResponse
func (s DevicesListResponse) MarshalJSON() ([]byte, error)
type DevicesService
func NewDevicesService(s *Service) *DevicesService
func (r *DevicesService) ForceReportUpload(enterpriseId string, userId string, deviceId string) *DevicesForceReportUploadCall
func (r *DevicesService) Get(enterpriseId string, userId string, deviceId string) *DevicesGetCall
func (r *DevicesService) GetState(enterpriseId string, userId string, deviceId string) *DevicesGetStateCall
func (r *DevicesService) List(enterpriseId string, userId string) *DevicesListCall
func (r *DevicesService) SetState(enterpriseId string, userId string, deviceId string, devicestate *DeviceState) *DevicesSetStateCall
func (r *DevicesService) Update(enterpriseId string, userId string, deviceId string, device *Device) *DevicesUpdateCall
type DevicesSetStateCall
func (c *DevicesSetStateCall) Context(ctx context.Context) *DevicesSetStateCall
func (c *DevicesSetStateCall) Do(opts ...googleapi.CallOption) (*DeviceState, error)
func (c *DevicesSetStateCall) Fields(s ...googleapi.Field) *DevicesSetStateCall
func (c *DevicesSetStateCall) Header() http.Header
type DevicesUpdateCall
func (c *DevicesUpdateCall) Context(ctx context.Context) *DevicesUpdateCall
func (c *DevicesUpdateCall) Do(opts ...googleapi.CallOption) (*Device, error)
func (c *DevicesUpdateCall) Fields(s ...googleapi.Field) *DevicesUpdateCall
func (c *DevicesUpdateCall) Header() http.Header
func (c *DevicesUpdateCall) UpdateMask(updateMask string) *DevicesUpdateCall
type EnrollmentToken
func (s EnrollmentToken) MarshalJSON() ([]byte, error)
type EnrollmentTokenGoogleAuthenticationOptions
func (s EnrollmentTokenGoogleAuthenticationOptions) MarshalJSON() ([]byte, error)
type EnrollmentTokensCreateCall
func (c *EnrollmentTokensCreateCall) Context(ctx context.Context) *EnrollmentTokensCreateCall
func (c *EnrollmentTokensCreateCall) Do(opts ...googleapi.CallOption) (*EnrollmentToken, error)
func (c *EnrollmentTokensCreateCall) Fields(s ...googleapi.Field) *EnrollmentTokensCreateCall
func (c *EnrollmentTokensCreateCall) Header() http.Header
type EnrollmentTokensService
func NewEnrollmentTokensService(s *Service) *EnrollmentTokensService
func (r *EnrollmentTokensService) Create(enterpriseId string, enrollmenttoken *EnrollmentToken) *EnrollmentTokensCreateCall
type Enterprise
func (s Enterprise) MarshalJSON() ([]byte, error)
type EnterpriseAccount
func (s EnterpriseAccount) MarshalJSON() ([]byte, error)
type EnterpriseAuthenticationAppLinkConfig
func (s EnterpriseAuthenticationAppLinkConfig) MarshalJSON() ([]byte, error)
type EnterpriseUpgradeEvent
func (s EnterpriseUpgradeEvent) MarshalJSON() ([]byte, error)
type EnterprisesAcknowledgeNotificationSetCall
func (c *EnterprisesAcknowledgeNotificationSetCall) Context(ctx context.Context) *EnterprisesAcknowledgeNotificationSetCall
func (c *EnterprisesAcknowledgeNotificationSetCall) Do(opts ...googleapi.CallOption) error
func (c *EnterprisesAcknowledgeNotificationSetCall) Fields(s ...googleapi.Field) *EnterprisesAcknowledgeNotificationSetCall
func (c *EnterprisesAcknowledgeNotificationSetCall) Header() http.Header
func (c *EnterprisesAcknowledgeNotificationSetCall) NotificationSetId(notificationSetId string) *EnterprisesAcknowledgeNotificationSetCall
type EnterprisesCompleteSignupCall
func (c *EnterprisesCompleteSignupCall) CompletionToken(completionToken string) *EnterprisesCompleteSignupCall
func (c *EnterprisesCompleteSignupCall) Context(ctx context.Context) *EnterprisesCompleteSignupCall
func (c *EnterprisesCompleteSignupCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)
func (c *EnterprisesCompleteSignupCall) EnterpriseToken(enterpriseToken string) *EnterprisesCompleteSignupCall
func (c *EnterprisesCompleteSignupCall) Fields(s ...googleapi.Field) *EnterprisesCompleteSignupCall
func (c *EnterprisesCompleteSignupCall) Header() http.Header
type EnterprisesCreateWebTokenCall
func (c *EnterprisesCreateWebTokenCall) Context(ctx context.Context) *EnterprisesCreateWebTokenCall
func (c *EnterprisesCreateWebTokenCall) Do(opts ...googleapi.CallOption) (*AdministratorWebToken, error)
func (c *EnterprisesCreateWebTokenCall) Fields(s ...googleapi.Field) *EnterprisesCreateWebTokenCall
func (c *EnterprisesCreateWebTokenCall) Header() http.Header
type EnterprisesEnrollCall
func (c *EnterprisesEnrollCall) Context(ctx context.Context) *EnterprisesEnrollCall
func (c *EnterprisesEnrollCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)
func (c *EnterprisesEnrollCall) Fields(s ...googleapi.Field) *EnterprisesEnrollCall
func (c *EnterprisesEnrollCall) Header() http.Header
type EnterprisesGenerateEnterpriseUpgradeUrlCall
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) AdminEmail(adminEmail string) *EnterprisesGenerateEnterpriseUpgradeUrlCall
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) AllowedDomains(allowedDomains ...string) *EnterprisesGenerateEnterpriseUpgradeUrlCall
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Context(ctx context.Context) *EnterprisesGenerateEnterpriseUpgradeUrlCall
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Do(opts ...googleapi.CallOption) (*GenerateEnterpriseUpgradeUrlResponse, error)
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Fields(s ...googleapi.Field) *EnterprisesGenerateEnterpriseUpgradeUrlCall
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Header() http.Header
type EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) AdminEmail(adminEmail string) *EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) AllowedDomains(allowedDomains ...string) *EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) CallbackUrl(callbackUrl string) *EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) Context(ctx context.Context) *EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) Do(opts ...googleapi.CallOption) (*SignupInfo, error)
func (c *EnterprisesGenerateSignupUrlCall) Fields(s ...googleapi.Field) *EnterprisesGenerateSignupUrlCall
func (c *EnterprisesGenerateSignupUrlCall) Header() http.Header
type EnterprisesGetCall
func (c *EnterprisesGetCall) Context(ctx context.Context) *EnterprisesGetCall
func (c *EnterprisesGetCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)
func (c *EnterprisesGetCall) Fields(s ...googleapi.Field) *EnterprisesGetCall
func (c *EnterprisesGetCall) Header() http.Header
func (c *EnterprisesGetCall) IfNoneMatch(entityTag string) *EnterprisesGetCall
type EnterprisesGetServiceAccountCall
func (c *EnterprisesGetServiceAccountCall) Context(ctx context.Context) *EnterprisesGetServiceAccountCall
func (c *EnterprisesGetServiceAccountCall) Do(opts ...googleapi.CallOption) (*ServiceAccount, error)
func (c *EnterprisesGetServiceAccountCall) Fields(s ...googleapi.Field) *EnterprisesGetServiceAccountCall
func (c *EnterprisesGetServiceAccountCall) Header() http.Header
func (c *EnterprisesGetServiceAccountCall) IfNoneMatch(entityTag string) *EnterprisesGetServiceAccountCall
func (c *EnterprisesGetServiceAccountCall) KeyType(keyType string) *EnterprisesGetServiceAccountCall
type EnterprisesGetStoreLayoutCall
func (c *EnterprisesGetStoreLayoutCall) Context(ctx context.Context) *EnterprisesGetStoreLayoutCall
func (c *EnterprisesGetStoreLayoutCall) Do(opts ...googleapi.CallOption) (*StoreLayout, error)
func (c *EnterprisesGetStoreLayoutCall) Fields(s ...googleapi.Field) *EnterprisesGetStoreLayoutCall
func (c *EnterprisesGetStoreLayoutCall) Header() http.Header
func (c *EnterprisesGetStoreLayoutCall) IfNoneMatch(entityTag string) *EnterprisesGetStoreLayoutCall
type EnterprisesListCall
func (c *EnterprisesListCall) Context(ctx context.Context) *EnterprisesListCall
func (c *EnterprisesListCall) Do(opts ...googleapi.CallOption) (*EnterprisesListResponse, error)
func (c *EnterprisesListCall) Fields(s ...googleapi.Field) *EnterprisesListCall
func (c *EnterprisesListCall) Header() http.Header
func (c *EnterprisesListCall) IfNoneMatch(entityTag string) *EnterprisesListCall
type EnterprisesListResponse
func (s EnterprisesListResponse) MarshalJSON() ([]byte, error)
type EnterprisesPullNotificationSetCall
func (c *EnterprisesPullNotificationSetCall) Context(ctx context.Context) *EnterprisesPullNotificationSetCall
func (c *EnterprisesPullNotificationSetCall) Do(opts ...googleapi.CallOption) (*NotificationSet, error)
func (c *EnterprisesPullNotificationSetCall) Fields(s ...googleapi.Field) *EnterprisesPullNotificationSetCall
func (c *EnterprisesPullNotificationSetCall) Header() http.Header
func (c *EnterprisesPullNotificationSetCall) RequestMode(requestMode string) *EnterprisesPullNotificationSetCall
type EnterprisesSendTestPushNotificationCall
func (c *EnterprisesSendTestPushNotificationCall) Context(ctx context.Context) *EnterprisesSendTestPushNotificationCall
func (c *EnterprisesSendTestPushNotificationCall) Do(opts ...googleapi.CallOption) (*EnterprisesSendTestPushNotificationResponse, error)
func (c *EnterprisesSendTestPushNotificationCall) Fields(s ...googleapi.Field) *EnterprisesSendTestPushNotificationCall
func (c *EnterprisesSendTestPushNotificationCall) Header() http.Header
type EnterprisesSendTestPushNotificationResponse
func (s EnterprisesSendTestPushNotificationResponse) MarshalJSON() ([]byte, error)
type EnterprisesService
func NewEnterprisesService(s *Service) *EnterprisesService
func (r *EnterprisesService) AcknowledgeNotificationSet() *EnterprisesAcknowledgeNotificationSetCall
func (r *EnterprisesService) CompleteSignup() *EnterprisesCompleteSignupCall
func (r *EnterprisesService) CreateWebToken(enterpriseId string, administratorwebtokenspec *AdministratorWebTokenSpec) *EnterprisesCreateWebTokenCall
func (r *EnterprisesService) Enroll(token string, enterprise *Enterprise) *EnterprisesEnrollCall
func (r *EnterprisesService) GenerateEnterpriseUpgradeUrl(enterpriseId string) *EnterprisesGenerateEnterpriseUpgradeUrlCall
func (r *EnterprisesService) GenerateSignupUrl() *EnterprisesGenerateSignupUrlCall
func (r *EnterprisesService) Get(enterpriseId string) *EnterprisesGetCall
func (r *EnterprisesService) GetServiceAccount(enterpriseId string) *EnterprisesGetServiceAccountCall
func (r *EnterprisesService) GetStoreLayout(enterpriseId string) *EnterprisesGetStoreLayoutCall
func (r *EnterprisesService) List(domain string) *EnterprisesListCall
func (r *EnterprisesService) PullNotificationSet() *EnterprisesPullNotificationSetCall
func (r *EnterprisesService) SendTestPushNotification(enterpriseId string) *EnterprisesSendTestPushNotificationCall
func (r *EnterprisesService) SetAccount(enterpriseId string, enterpriseaccount *EnterpriseAccount) *EnterprisesSetAccountCall
func (r *EnterprisesService) SetStoreLayout(enterpriseId string, storelayout *StoreLayout) *EnterprisesSetStoreLayoutCall
func (r *EnterprisesService) Unenroll(enterpriseId string) *EnterprisesUnenrollCall
type EnterprisesSetAccountCall
func (c *EnterprisesSetAccountCall) Context(ctx context.Context) *EnterprisesSetAccountCall
func (c *EnterprisesSetAccountCall) Do(opts ...googleapi.CallOption) (*EnterpriseAccount, error)
func (c *EnterprisesSetAccountCall) Fields(s ...googleapi.Field) *EnterprisesSetAccountCall
func (c *EnterprisesSetAccountCall) Header() http.Header
type EnterprisesSetStoreLayoutCall
func (c *EnterprisesSetStoreLayoutCall) Context(ctx context.Context) *EnterprisesSetStoreLayoutCall
func (c *EnterprisesSetStoreLayoutCall) Do(opts ...googleapi.CallOption) (*StoreLayout, error)
func (c *EnterprisesSetStoreLayoutCall) Fields(s ...googleapi.Field) *EnterprisesSetStoreLayoutCall
func (c *EnterprisesSetStoreLayoutCall) Header() http.Header
type EnterprisesUnenrollCall
func (c *EnterprisesUnenrollCall) Context(ctx context.Context) *EnterprisesUnenrollCall
func (c *EnterprisesUnenrollCall) Do(opts ...googleapi.CallOption) error
func (c *EnterprisesUnenrollCall) Fields(s ...googleapi.Field) *EnterprisesUnenrollCall
func (c *EnterprisesUnenrollCall) Header() http.Header
type Entitlement
func (s Entitlement) MarshalJSON() ([]byte, error)
type EntitlementsDeleteCall
func (c *EntitlementsDeleteCall) Context(ctx context.Context) *EntitlementsDeleteCall
func (c *EntitlementsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *EntitlementsDeleteCall) Fields(s ...googleapi.Field) *EntitlementsDeleteCall
func (c *EntitlementsDeleteCall) Header() http.Header
type EntitlementsGetCall
func (c *EntitlementsGetCall) Context(ctx context.Context) *EntitlementsGetCall
func (c *EntitlementsGetCall) Do(opts ...googleapi.CallOption) (*Entitlement, error)
func (c *EntitlementsGetCall) Fields(s ...googleapi.Field) *EntitlementsGetCall
func (c *EntitlementsGetCall) Header() http.Header
func (c *EntitlementsGetCall) IfNoneMatch(entityTag string) *EntitlementsGetCall
type EntitlementsListCall
func (c *EntitlementsListCall) Context(ctx context.Context) *EntitlementsListCall
func (c *EntitlementsListCall) Do(opts ...googleapi.CallOption) (*EntitlementsListResponse, error)
func (c *EntitlementsListCall) Fields(s ...googleapi.Field) *EntitlementsListCall
func (c *EntitlementsListCall) Header() http.Header
func (c *EntitlementsListCall) IfNoneMatch(entityTag string) *EntitlementsListCall
type EntitlementsListResponse
func (s EntitlementsListResponse) MarshalJSON() ([]byte, error)
type EntitlementsService
func NewEntitlementsService(s *Service) *EntitlementsService
func (r *EntitlementsService) Delete(enterpriseId string, userId string, entitlementId string) *EntitlementsDeleteCall
func (r *EntitlementsService) Get(enterpriseId string, userId string, entitlementId string) *EntitlementsGetCall
func (r *EntitlementsService) List(enterpriseId string, userId string) *EntitlementsListCall
func (r *EntitlementsService) Update(enterpriseId string, userId string, entitlementId string, ...) *EntitlementsUpdateCall
type EntitlementsUpdateCall
func (c *EntitlementsUpdateCall) Context(ctx context.Context) *EntitlementsUpdateCall
func (c *EntitlementsUpdateCall) Do(opts ...googleapi.CallOption) (*Entitlement, error)
func (c *EntitlementsUpdateCall) Fields(s ...googleapi.Field) *EntitlementsUpdateCall
func (c *EntitlementsUpdateCall) Header() http.Header
func (c *EntitlementsUpdateCall) Install(install bool) *EntitlementsUpdateCall
type GenerateEnterpriseUpgradeUrlResponse
func (s GenerateEnterpriseUpgradeUrlResponse) MarshalJSON() ([]byte, error)
type GoogleAuthenticationSettings
func (s GoogleAuthenticationSettings) MarshalJSON() ([]byte, error)
type GroupLicense
func (s GroupLicense) MarshalJSON() ([]byte, error)
type GroupLicenseUsersListResponse
func (s GroupLicenseUsersListResponse) MarshalJSON() ([]byte, error)
type GroupLicensesListResponse
func (s GroupLicensesListResponse) MarshalJSON() ([]byte, error)
type GrouplicensesGetCall
func (c *GrouplicensesGetCall) Context(ctx context.Context) *GrouplicensesGetCall
func (c *GrouplicensesGetCall) Do(opts ...googleapi.CallOption) (*GroupLicense, error)
func (c *GrouplicensesGetCall) Fields(s ...googleapi.Field) *GrouplicensesGetCall
func (c *GrouplicensesGetCall) Header() http.Header
func (c *GrouplicensesGetCall) IfNoneMatch(entityTag string) *GrouplicensesGetCall
type GrouplicensesListCall
func (c *GrouplicensesListCall) Context(ctx context.Context) *GrouplicensesListCall
func (c *GrouplicensesListCall) Do(opts ...googleapi.CallOption) (*GroupLicensesListResponse, error)
func (c *GrouplicensesListCall) Fields(s ...googleapi.Field) *GrouplicensesListCall
func (c *GrouplicensesListCall) Header() http.Header
func (c *GrouplicensesListCall) IfNoneMatch(entityTag string) *GrouplicensesListCall
type GrouplicensesService
func NewGrouplicensesService(s *Service) *GrouplicensesService
func (r *GrouplicensesService) Get(enterpriseId string, groupLicenseId string) *GrouplicensesGetCall
func (r *GrouplicensesService) List(enterpriseId string) *GrouplicensesListCall
type GrouplicenseusersListCall
func (c *GrouplicenseusersListCall) Context(ctx context.Context) *GrouplicenseusersListCall
func (c *GrouplicenseusersListCall) Do(opts ...googleapi.CallOption) (*GroupLicenseUsersListResponse, error)
func (c *GrouplicenseusersListCall) Fields(s ...googleapi.Field) *GrouplicenseusersListCall
func (c *GrouplicenseusersListCall) Header() http.Header
func (c *GrouplicenseusersListCall) IfNoneMatch(entityTag string) *GrouplicenseusersListCall
type GrouplicenseusersService
func NewGrouplicenseusersService(s *Service) *GrouplicenseusersService
func (r *GrouplicenseusersService) List(enterpriseId string, groupLicenseId string) *GrouplicenseusersListCall
type Install
func (s Install) MarshalJSON() ([]byte, error)
type InstallFailureEvent
func (s InstallFailureEvent) MarshalJSON() ([]byte, error)
type InstallsDeleteCall
func (c *InstallsDeleteCall) Context(ctx context.Context) *InstallsDeleteCall
func (c *InstallsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *InstallsDeleteCall) Fields(s ...googleapi.Field) *InstallsDeleteCall
func (c *InstallsDeleteCall) Header() http.Header
type InstallsGetCall
func (c *InstallsGetCall) Context(ctx context.Context) *InstallsGetCall
func (c *InstallsGetCall) Do(opts ...googleapi.CallOption) (*Install, error)
func (c *InstallsGetCall) Fields(s ...googleapi.Field) *InstallsGetCall
func (c *InstallsGetCall) Header() http.Header
func (c *InstallsGetCall) IfNoneMatch(entityTag string) *InstallsGetCall
type InstallsListCall
func (c *InstallsListCall) Context(ctx context.Context) *InstallsListCall
func (c *InstallsListCall) Do(opts ...googleapi.CallOption) (*InstallsListResponse, error)
func (c *InstallsListCall) Fields(s ...googleapi.Field) *InstallsListCall
func (c *InstallsListCall) Header() http.Header
func (c *InstallsListCall) IfNoneMatch(entityTag string) *InstallsListCall
type InstallsListResponse
func (s InstallsListResponse) MarshalJSON() ([]byte, error)
type InstallsService
func NewInstallsService(s *Service) *InstallsService
func (r *InstallsService) Delete(enterpriseId string, userId string, deviceId string, installId string) *InstallsDeleteCall
func (r *InstallsService) Get(enterpriseId string, userId string, deviceId string, installId string) *InstallsGetCall
func (r *InstallsService) List(enterpriseId string, userId string, deviceId string) *InstallsListCall
func (r *InstallsService) Update(enterpriseId string, userId string, deviceId string, installId string, ...) *InstallsUpdateCall
type InstallsUpdateCall
func (c *InstallsUpdateCall) Context(ctx context.Context) *InstallsUpdateCall
func (c *InstallsUpdateCall) Do(opts ...googleapi.CallOption) (*Install, error)
func (c *InstallsUpdateCall) Fields(s ...googleapi.Field) *InstallsUpdateCall
func (c *InstallsUpdateCall) Header() http.Header
type KeyedAppState
func (s KeyedAppState) MarshalJSON() ([]byte, error)
type LocalizedText
func (s LocalizedText) MarshalJSON() ([]byte, error)
type MaintenanceWindow
func (s MaintenanceWindow) MarshalJSON() ([]byte, error)
type ManagedConfiguration
func (s ManagedConfiguration) MarshalJSON() ([]byte, error)
type ManagedConfigurationsForDeviceListResponse
func (s ManagedConfigurationsForDeviceListResponse) MarshalJSON() ([]byte, error)
type ManagedConfigurationsForUserListResponse
func (s ManagedConfigurationsForUserListResponse) MarshalJSON() ([]byte, error)
type ManagedConfigurationsSettings
func (s ManagedConfigurationsSettings) MarshalJSON() ([]byte, error)
type ManagedConfigurationsSettingsListResponse
func (s ManagedConfigurationsSettingsListResponse) MarshalJSON() ([]byte, error)
type ManagedProperty
func (s ManagedProperty) MarshalJSON() ([]byte, error)
type ManagedPropertyBundle
func (s ManagedPropertyBundle) MarshalJSON() ([]byte, error)
type ManagedconfigurationsfordeviceDeleteCall
func (c *ManagedconfigurationsfordeviceDeleteCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceDeleteCall
func (c *ManagedconfigurationsfordeviceDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagedconfigurationsfordeviceDeleteCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceDeleteCall
func (c *ManagedconfigurationsfordeviceDeleteCall) Header() http.Header
type ManagedconfigurationsfordeviceGetCall
func (c *ManagedconfigurationsfordeviceGetCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceGetCall
func (c *ManagedconfigurationsfordeviceGetCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)
func (c *ManagedconfigurationsfordeviceGetCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceGetCall
func (c *ManagedconfigurationsfordeviceGetCall) Header() http.Header
func (c *ManagedconfigurationsfordeviceGetCall) IfNoneMatch(entityTag string) *ManagedconfigurationsfordeviceGetCall
type ManagedconfigurationsfordeviceListCall
func (c *ManagedconfigurationsfordeviceListCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceListCall
func (c *ManagedconfigurationsfordeviceListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsForDeviceListResponse, error)
func (c *ManagedconfigurationsfordeviceListCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceListCall
func (c *ManagedconfigurationsfordeviceListCall) Header() http.Header
func (c *ManagedconfigurationsfordeviceListCall) IfNoneMatch(entityTag string) *ManagedconfigurationsfordeviceListCall
type ManagedconfigurationsfordeviceService
func NewManagedconfigurationsfordeviceService(s *Service) *ManagedconfigurationsfordeviceService
func (r *ManagedconfigurationsfordeviceService) Delete(enterpriseId string, userId string, deviceId string, ...) *ManagedconfigurationsfordeviceDeleteCall
func (r *ManagedconfigurationsfordeviceService) Get(enterpriseId string, userId string, deviceId string, ...) *ManagedconfigurationsfordeviceGetCall
func (r *ManagedconfigurationsfordeviceService) List(enterpriseId string, userId string, deviceId string) *ManagedconfigurationsfordeviceListCall
func (r *ManagedconfigurationsfordeviceService) Update(enterpriseId string, userId string, deviceId string, ...) *ManagedconfigurationsfordeviceUpdateCall
type ManagedconfigurationsfordeviceUpdateCall
func (c *ManagedconfigurationsfordeviceUpdateCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceUpdateCall
func (c *ManagedconfigurationsfordeviceUpdateCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)
func (c *ManagedconfigurationsfordeviceUpdateCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceUpdateCall
func (c *ManagedconfigurationsfordeviceUpdateCall) Header() http.Header
type ManagedconfigurationsforuserDeleteCall
func (c *ManagedconfigurationsforuserDeleteCall) Context(ctx context.Context) *ManagedconfigurationsforuserDeleteCall
func (c *ManagedconfigurationsforuserDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagedconfigurationsforuserDeleteCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserDeleteCall
func (c *ManagedconfigurationsforuserDeleteCall) Header() http.Header
type ManagedconfigurationsforuserGetCall
func (c *ManagedconfigurationsforuserGetCall) Context(ctx context.Context) *ManagedconfigurationsforuserGetCall
func (c *ManagedconfigurationsforuserGetCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)
func (c *ManagedconfigurationsforuserGetCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserGetCall
func (c *ManagedconfigurationsforuserGetCall) Header() http.Header
func (c *ManagedconfigurationsforuserGetCall) IfNoneMatch(entityTag string) *ManagedconfigurationsforuserGetCall
type ManagedconfigurationsforuserListCall
func (c *ManagedconfigurationsforuserListCall) Context(ctx context.Context) *ManagedconfigurationsforuserListCall
func (c *ManagedconfigurationsforuserListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsForUserListResponse, error)
func (c *ManagedconfigurationsforuserListCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserListCall
func (c *ManagedconfigurationsforuserListCall) Header() http.Header
func (c *ManagedconfigurationsforuserListCall) IfNoneMatch(entityTag string) *ManagedconfigurationsforuserListCall
type ManagedconfigurationsforuserService
func NewManagedconfigurationsforuserService(s *Service) *ManagedconfigurationsforuserService
func (r *ManagedconfigurationsforuserService) Delete(enterpriseId string, userId string, managedConfigurationForUserId string) *ManagedconfigurationsforuserDeleteCall
func (r *ManagedconfigurationsforuserService) Get(enterpriseId string, userId string, managedConfigurationForUserId string) *ManagedconfigurationsforuserGetCall
func (r *ManagedconfigurationsforuserService) List(enterpriseId string, userId string) *ManagedconfigurationsforuserListCall
func (r *ManagedconfigurationsforuserService) Update(enterpriseId string, userId string, managedConfigurationForUserId string, ...) *ManagedconfigurationsforuserUpdateCall
type ManagedconfigurationsforuserUpdateCall
func (c *ManagedconfigurationsforuserUpdateCall) Context(ctx context.Context) *ManagedconfigurationsforuserUpdateCall
func (c *ManagedconfigurationsforuserUpdateCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)
func (c *ManagedconfigurationsforuserUpdateCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserUpdateCall
func (c *ManagedconfigurationsforuserUpdateCall) Header() http.Header
type ManagedconfigurationssettingsListCall
func (c *ManagedconfigurationssettingsListCall) Context(ctx context.Context) *ManagedconfigurationssettingsListCall
func (c *ManagedconfigurationssettingsListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsSettingsListResponse, error)
func (c *ManagedconfigurationssettingsListCall) Fields(s ...googleapi.Field) *ManagedconfigurationssettingsListCall
func (c *ManagedconfigurationssettingsListCall) Header() http.Header
func (c *ManagedconfigurationssettingsListCall) IfNoneMatch(entityTag string) *ManagedconfigurationssettingsListCall
type ManagedconfigurationssettingsService
func NewManagedconfigurationssettingsService(s *Service) *ManagedconfigurationssettingsService
func (r *ManagedconfigurationssettingsService) List(enterpriseId string, productId string) *ManagedconfigurationssettingsListCall
type NewDeviceEvent
func (s NewDeviceEvent) MarshalJSON() ([]byte, error)
type NewPermissionsEvent
func (s NewPermissionsEvent) MarshalJSON() ([]byte, error)
type Notification
func (s Notification) MarshalJSON() ([]byte, error)
type NotificationSet
func (s NotificationSet) MarshalJSON() ([]byte, error)
type PageInfo
func (s PageInfo) MarshalJSON() ([]byte, error)
type Permission
func (s Permission) MarshalJSON() ([]byte, error)
type PermissionsGetCall
func (c *PermissionsGetCall) Context(ctx context.Context) *PermissionsGetCall
func (c *PermissionsGetCall) Do(opts ...googleapi.CallOption) (*Permission, error)
func (c *PermissionsGetCall) Fields(s ...googleapi.Field) *PermissionsGetCall
func (c *PermissionsGetCall) Header() http.Header
func (c *PermissionsGetCall) IfNoneMatch(entityTag string) *PermissionsGetCall
func (c *PermissionsGetCall) Language(language string) *PermissionsGetCall
type PermissionsService
func NewPermissionsService(s *Service) *PermissionsService
func (r *PermissionsService) Get(permissionId string) *PermissionsGetCall
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type Product
func (s Product) MarshalJSON() ([]byte, error)
type ProductApprovalEvent
func (s ProductApprovalEvent) MarshalJSON() ([]byte, error)
type ProductAvailabilityChangeEvent
func (s ProductAvailabilityChangeEvent) MarshalJSON() ([]byte, error)
type ProductPermission
func (s ProductPermission) MarshalJSON() ([]byte, error)
type ProductPermissions
func (s ProductPermissions) MarshalJSON() ([]byte, error)
type ProductPolicy
func (s ProductPolicy) MarshalJSON() ([]byte, error)
type ProductSet
func (s ProductSet) MarshalJSON() ([]byte, error)
type ProductSigningCertificate
func (s ProductSigningCertificate) MarshalJSON() ([]byte, error)
type ProductVisibility
func (s ProductVisibility) MarshalJSON() ([]byte, error)
type ProductsApproveCall
func (c *ProductsApproveCall) Context(ctx context.Context) *ProductsApproveCall
func (c *ProductsApproveCall) Do(opts ...googleapi.CallOption) error
func (c *ProductsApproveCall) Fields(s ...googleapi.Field) *ProductsApproveCall
func (c *ProductsApproveCall) Header() http.Header
type ProductsApproveRequest
func (s ProductsApproveRequest) MarshalJSON() ([]byte, error)
type ProductsGenerateApprovalUrlCall
func (c *ProductsGenerateApprovalUrlCall) Context(ctx context.Context) *ProductsGenerateApprovalUrlCall
func (c *ProductsGenerateApprovalUrlCall) Do(opts ...googleapi.CallOption) (*ProductsGenerateApprovalUrlResponse, error)
func (c *ProductsGenerateApprovalUrlCall) Fields(s ...googleapi.Field) *ProductsGenerateApprovalUrlCall
func (c *ProductsGenerateApprovalUrlCall) Header() http.Header
func (c *ProductsGenerateApprovalUrlCall) LanguageCode(languageCode string) *ProductsGenerateApprovalUrlCall
type ProductsGenerateApprovalUrlResponse
func (s ProductsGenerateApprovalUrlResponse) MarshalJSON() ([]byte, error)
type ProductsGetAppRestrictionsSchemaCall
func (c *ProductsGetAppRestrictionsSchemaCall) Context(ctx context.Context) *ProductsGetAppRestrictionsSchemaCall
func (c *ProductsGetAppRestrictionsSchemaCall) Do(opts ...googleapi.CallOption) (*AppRestrictionsSchema, error)
func (c *ProductsGetAppRestrictionsSchemaCall) Fields(s ...googleapi.Field) *ProductsGetAppRestrictionsSchemaCall
func (c *ProductsGetAppRestrictionsSchemaCall) Header() http.Header
func (c *ProductsGetAppRestrictionsSchemaCall) IfNoneMatch(entityTag string) *ProductsGetAppRestrictionsSchemaCall
func (c *ProductsGetAppRestrictionsSchemaCall) Language(language string) *ProductsGetAppRestrictionsSchemaCall
type ProductsGetCall
func (c *ProductsGetCall) Context(ctx context.Context) *ProductsGetCall
func (c *ProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)
func (c *ProductsGetCall) Fields(s ...googleapi.Field) *ProductsGetCall
func (c *ProductsGetCall) Header() http.Header
func (c *ProductsGetCall) IfNoneMatch(entityTag string) *ProductsGetCall
func (c *ProductsGetCall) Language(language string) *ProductsGetCall
type ProductsGetPermissionsCall
func (c *ProductsGetPermissionsCall) Context(ctx context.Context) *ProductsGetPermissionsCall
func (c *ProductsGetPermissionsCall) Do(opts ...googleapi.CallOption) (*ProductPermissions, error)
func (c *ProductsGetPermissionsCall) Fields(s ...googleapi.Field) *ProductsGetPermissionsCall
func (c *ProductsGetPermissionsCall) Header() http.Header
func (c *ProductsGetPermissionsCall) IfNoneMatch(entityTag string) *ProductsGetPermissionsCall
type ProductsListCall
func (c *ProductsListCall) Approved(approved bool) *ProductsListCall
func (c *ProductsListCall) Context(ctx context.Context) *ProductsListCall
func (c *ProductsListCall) Do(opts ...googleapi.CallOption) (*ProductsListResponse, error)
func (c *ProductsListCall) Fields(s ...googleapi.Field) *ProductsListCall
func (c *ProductsListCall) Header() http.Header
func (c *ProductsListCall) IfNoneMatch(entityTag string) *ProductsListCall
func (c *ProductsListCall) Language(language string) *ProductsListCall
func (c *ProductsListCall) MaxResults(maxResults int64) *ProductsListCall
func (c *ProductsListCall) Query(query string) *ProductsListCall
func (c *ProductsListCall) Token(token string) *ProductsListCall
type ProductsListResponse
func (s ProductsListResponse) MarshalJSON() ([]byte, error)
type ProductsService
func NewProductsService(s *Service) *ProductsService
func (r *ProductsService) Approve(enterpriseId string, productId string, ...) *ProductsApproveCall
func (r *ProductsService) GenerateApprovalUrl(enterpriseId string, productId string) *ProductsGenerateApprovalUrlCall
func (r *ProductsService) Get(enterpriseId string, productId string) *ProductsGetCall
func (r *ProductsService) GetAppRestrictionsSchema(enterpriseId string, productId string) *ProductsGetAppRestrictionsSchemaCall
func (r *ProductsService) GetPermissions(enterpriseId string, productId string) *ProductsGetPermissionsCall
func (r *ProductsService) List(enterpriseId string) *ProductsListCall
func (r *ProductsService) Unapprove(enterpriseId string, productId string) *ProductsUnapproveCall
type ProductsUnapproveCall
func (c *ProductsUnapproveCall) Context(ctx context.Context) *ProductsUnapproveCall
func (c *ProductsUnapproveCall) Do(opts ...googleapi.CallOption) error
func (c *ProductsUnapproveCall) Fields(s ...googleapi.Field) *ProductsUnapproveCall
func (c *ProductsUnapproveCall) Header() http.Header
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type ServiceAccount
func (s ServiceAccount) MarshalJSON() ([]byte, error)
type ServiceAccountKey
func (s ServiceAccountKey) MarshalJSON() ([]byte, error)
type ServiceAccountKeysListResponse
func (s ServiceAccountKeysListResponse) MarshalJSON() ([]byte, error)
type ServiceaccountkeysDeleteCall
func (c *ServiceaccountkeysDeleteCall) Context(ctx context.Context) *ServiceaccountkeysDeleteCall
func (c *ServiceaccountkeysDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ServiceaccountkeysDeleteCall) Fields(s ...googleapi.Field) *ServiceaccountkeysDeleteCall
func (c *ServiceaccountkeysDeleteCall) Header() http.Header
type ServiceaccountkeysInsertCall
func (c *ServiceaccountkeysInsertCall) Context(ctx context.Context) *ServiceaccountkeysInsertCall
func (c *ServiceaccountkeysInsertCall) Do(opts ...googleapi.CallOption) (*ServiceAccountKey, error)
func (c *ServiceaccountkeysInsertCall) Fields(s ...googleapi.Field) *ServiceaccountkeysInsertCall
func (c *ServiceaccountkeysInsertCall) Header() http.Header
type ServiceaccountkeysListCall
func (c *ServiceaccountkeysListCall) Context(ctx context.Context) *ServiceaccountkeysListCall
func (c *ServiceaccountkeysListCall) Do(opts ...googleapi.CallOption) (*ServiceAccountKeysListResponse, error)
func (c *ServiceaccountkeysListCall) Fields(s ...googleapi.Field) *ServiceaccountkeysListCall
func (c *ServiceaccountkeysListCall) Header() http.Header
func (c *ServiceaccountkeysListCall) IfNoneMatch(entityTag string) *ServiceaccountkeysListCall
type ServiceaccountkeysService
func NewServiceaccountkeysService(s *Service) *ServiceaccountkeysService
func (r *ServiceaccountkeysService) Delete(enterpriseId string, keyId string) *ServiceaccountkeysDeleteCall
func (r *ServiceaccountkeysService) Insert(enterpriseId string, serviceaccountkey *ServiceAccountKey) *ServiceaccountkeysInsertCall
func (r *ServiceaccountkeysService) List(enterpriseId string) *ServiceaccountkeysListCall
type SignupInfo
func (s SignupInfo) MarshalJSON() ([]byte, error)
type StoreCluster
func (s StoreCluster) MarshalJSON() ([]byte, error)
type StoreLayout
func (s StoreLayout) MarshalJSON() ([]byte, error)
type StoreLayoutClustersListResponse
func (s StoreLayoutClustersListResponse) MarshalJSON() ([]byte, error)
type StoreLayoutPagesListResponse
func (s StoreLayoutPagesListResponse) MarshalJSON() ([]byte, error)
type StorePage
func (s StorePage) MarshalJSON() ([]byte, error)
type StorelayoutclustersDeleteCall
func (c *StorelayoutclustersDeleteCall) Context(ctx context.Context) *StorelayoutclustersDeleteCall
func (c *StorelayoutclustersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *StorelayoutclustersDeleteCall) Fields(s ...googleapi.Field) *StorelayoutclustersDeleteCall
func (c *StorelayoutclustersDeleteCall) Header() http.Header
type StorelayoutclustersGetCall
func (c *StorelayoutclustersGetCall) Context(ctx context.Context) *StorelayoutclustersGetCall
func (c *StorelayoutclustersGetCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)
func (c *StorelayoutclustersGetCall) Fields(s ...googleapi.Field) *StorelayoutclustersGetCall
func (c *StorelayoutclustersGetCall) Header() http.Header
func (c *StorelayoutclustersGetCall) IfNoneMatch(entityTag string) *StorelayoutclustersGetCall
type StorelayoutclustersInsertCall
func (c *StorelayoutclustersInsertCall) Context(ctx context.Context) *StorelayoutclustersInsertCall
func (c *StorelayoutclustersInsertCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)
func (c *StorelayoutclustersInsertCall) Fields(s ...googleapi.Field) *StorelayoutclustersInsertCall
func (c *StorelayoutclustersInsertCall) Header() http.Header
type StorelayoutclustersListCall
func (c *StorelayoutclustersListCall) Context(ctx context.Context) *StorelayoutclustersListCall
func (c *StorelayoutclustersListCall) Do(opts ...googleapi.CallOption) (*StoreLayoutClustersListResponse, error)
func (c *StorelayoutclustersListCall) Fields(s ...googleapi.Field) *StorelayoutclustersListCall
func (c *StorelayoutclustersListCall) Header() http.Header
func (c *StorelayoutclustersListCall) IfNoneMatch(entityTag string) *StorelayoutclustersListCall
type StorelayoutclustersService
func NewStorelayoutclustersService(s *Service) *StorelayoutclustersService
func (r *StorelayoutclustersService) Delete(enterpriseId string, pageId string, clusterId string) *StorelayoutclustersDeleteCall
func (r *StorelayoutclustersService) Get(enterpriseId string, pageId string, clusterId string) *StorelayoutclustersGetCall
func (r *StorelayoutclustersService) Insert(enterpriseId string, pageId string, storecluster *StoreCluster) *StorelayoutclustersInsertCall
func (r *StorelayoutclustersService) List(enterpriseId string, pageId string) *StorelayoutclustersListCall
func (r *StorelayoutclustersService) Update(enterpriseId string, pageId string, clusterId string, ...) *StorelayoutclustersUpdateCall
type StorelayoutclustersUpdateCall
func (c *StorelayoutclustersUpdateCall) Context(ctx context.Context) *StorelayoutclustersUpdateCall
func (c *StorelayoutclustersUpdateCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)
func (c *StorelayoutclustersUpdateCall) Fields(s ...googleapi.Field) *StorelayoutclustersUpdateCall
func (c *StorelayoutclustersUpdateCall) Header() http.Header
type StorelayoutpagesDeleteCall
func (c *StorelayoutpagesDeleteCall) Context(ctx context.Context) *StorelayoutpagesDeleteCall
func (c *StorelayoutpagesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *StorelayoutpagesDeleteCall) Fields(s ...googleapi.Field) *StorelayoutpagesDeleteCall
func (c *StorelayoutpagesDeleteCall) Header() http.Header
type StorelayoutpagesGetCall
func (c *StorelayoutpagesGetCall) Context(ctx context.Context) *StorelayoutpagesGetCall
func (c *StorelayoutpagesGetCall) Do(opts ...googleapi.CallOption) (*StorePage, error)
func (c *StorelayoutpagesGetCall) Fields(s ...googleapi.Field) *StorelayoutpagesGetCall
func (c *StorelayoutpagesGetCall) Header() http.Header
func (c *StorelayoutpagesGetCall) IfNoneMatch(entityTag string) *StorelayoutpagesGetCall
type StorelayoutpagesInsertCall
func (c *StorelayoutpagesInsertCall) Context(ctx context.Context) *StorelayoutpagesInsertCall
func (c *StorelayoutpagesInsertCall) Do(opts ...googleapi.CallOption) (*StorePage, error)
func (c *StorelayoutpagesInsertCall) Fields(s ...googleapi.Field) *StorelayoutpagesInsertCall
func (c *StorelayoutpagesInsertCall) Header() http.Header
type StorelayoutpagesListCall
func (c *StorelayoutpagesListCall) Context(ctx context.Context) *StorelayoutpagesListCall
func (c *StorelayoutpagesListCall) Do(opts ...googleapi.CallOption) (*StoreLayoutPagesListResponse, error)
func (c *StorelayoutpagesListCall) Fields(s ...googleapi.Field) *StorelayoutpagesListCall
func (c *StorelayoutpagesListCall) Header() http.Header
func (c *StorelayoutpagesListCall) IfNoneMatch(entityTag string) *StorelayoutpagesListCall
type StorelayoutpagesService
func NewStorelayoutpagesService(s *Service) *StorelayoutpagesService
func (r *StorelayoutpagesService) Delete(enterpriseId string, pageId string) *StorelayoutpagesDeleteCall
func (r *StorelayoutpagesService) Get(enterpriseId string, pageId string) *StorelayoutpagesGetCall
func (r *StorelayoutpagesService) Insert(enterpriseId string, storepage *StorePage) *StorelayoutpagesInsertCall
func (r *StorelayoutpagesService) List(enterpriseId string) *StorelayoutpagesListCall
func (r *StorelayoutpagesService) Update(enterpriseId string, pageId string, storepage *StorePage) *StorelayoutpagesUpdateCall
type StorelayoutpagesUpdateCall
func (c *StorelayoutpagesUpdateCall) Context(ctx context.Context) *StorelayoutpagesUpdateCall
func (c *StorelayoutpagesUpdateCall) Do(opts ...googleapi.CallOption) (*StorePage, error)
func (c *StorelayoutpagesUpdateCall) Fields(s ...googleapi.Field) *StorelayoutpagesUpdateCall
func (c *StorelayoutpagesUpdateCall) Header() http.Header
type TokenPagination
func (s TokenPagination) MarshalJSON() ([]byte, error)
type TrackInfo
func (s TrackInfo) MarshalJSON() ([]byte, error)
type User
func (s User) MarshalJSON() ([]byte, error)
type UsersDeleteCall
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall
func (c *UsersDeleteCall) Header() http.Header
type UsersGenerateAuthenticationTokenCall
func (c *UsersGenerateAuthenticationTokenCall) Context(ctx context.Context) *UsersGenerateAuthenticationTokenCall
func (c *UsersGenerateAuthenticationTokenCall) Do(opts ...googleapi.CallOption) (*AuthenticationToken, error)
func (c *UsersGenerateAuthenticationTokenCall) Fields(s ...googleapi.Field) *UsersGenerateAuthenticationTokenCall
func (c *UsersGenerateAuthenticationTokenCall) Header() http.Header
type UsersGetAvailableProductSetCall
func (c *UsersGetAvailableProductSetCall) Context(ctx context.Context) *UsersGetAvailableProductSetCall
func (c *UsersGetAvailableProductSetCall) Do(opts ...googleapi.CallOption) (*ProductSet, error)
func (c *UsersGetAvailableProductSetCall) Fields(s ...googleapi.Field) *UsersGetAvailableProductSetCall
func (c *UsersGetAvailableProductSetCall) Header() http.Header
func (c *UsersGetAvailableProductSetCall) IfNoneMatch(entityTag string) *UsersGetAvailableProductSetCall
type UsersGetCall
func (c *UsersGetCall) Context(ctx context.Context) *UsersGetCall
func (c *UsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersGetCall) Fields(s ...googleapi.Field) *UsersGetCall
func (c *UsersGetCall) Header() http.Header
func (c *UsersGetCall) IfNoneMatch(entityTag string) *UsersGetCall
type UsersInsertCall
func (c *UsersInsertCall) Context(ctx context.Context) *UsersInsertCall
func (c *UsersInsertCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersInsertCall) Fields(s ...googleapi.Field) *UsersInsertCall
func (c *UsersInsertCall) Header() http.Header
type UsersListCall
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*UsersListResponse, error)
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall
func (c *UsersListCall) Header() http.Header
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall
type UsersListResponse
func (s UsersListResponse) MarshalJSON() ([]byte, error)
type UsersRevokeDeviceAccessCall
func (c *UsersRevokeDeviceAccessCall) Context(ctx context.Context) *UsersRevokeDeviceAccessCall
func (c *UsersRevokeDeviceAccessCall) Do(opts ...googleapi.CallOption) error
func (c *UsersRevokeDeviceAccessCall) Fields(s ...googleapi.Field) *UsersRevokeDeviceAccessCall
func (c *UsersRevokeDeviceAccessCall) Header() http.Header
type UsersService
func NewUsersService(s *Service) *UsersService
func (r *UsersService) Delete(enterpriseId string, userId string) *UsersDeleteCall
func (r *UsersService) GenerateAuthenticationToken(enterpriseId string, userId string) *UsersGenerateAuthenticationTokenCall
func (r *UsersService) Get(enterpriseId string, userId string) *UsersGetCall
func (r *UsersService) GetAvailableProductSet(enterpriseId string, userId string) *UsersGetAvailableProductSetCall
func (r *UsersService) Insert(enterpriseId string, user *User) *UsersInsertCall
func (r *UsersService) List(enterpriseId string, email string) *UsersListCall
func (r *UsersService) RevokeDeviceAccess(enterpriseId string, userId string) *UsersRevokeDeviceAccessCall
func (r *UsersService) SetAvailableProductSet(enterpriseId string, userId string, productset *ProductSet) *UsersSetAvailableProductSetCall
func (r *UsersService) Update(enterpriseId string, userId string, user *User) *UsersUpdateCall
type UsersSetAvailableProductSetCall
func (c *UsersSetAvailableProductSetCall) Context(ctx context.Context) *UsersSetAvailableProductSetCall
func (c *UsersSetAvailableProductSetCall) Do(opts ...googleapi.CallOption) (*ProductSet, error)
func (c *UsersSetAvailableProductSetCall) Fields(s ...googleapi.Field) *UsersSetAvailableProductSetCall
func (c *UsersSetAvailableProductSetCall) Header() http.Header
type UsersUpdateCall
func (c *UsersUpdateCall) Context(ctx context.Context) *UsersUpdateCall
func (c *UsersUpdateCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersUpdateCall) Fields(s ...googleapi.Field) *UsersUpdateCall
func (c *UsersUpdateCall) Header() http.Header
type VariableSet
func (s VariableSet) MarshalJSON() ([]byte, error)
type WebApp
func (s WebApp) MarshalJSON() ([]byte, error)
type WebAppIcon
func (s WebAppIcon) MarshalJSON() ([]byte, error)
type WebAppsListResponse
func (s WebAppsListResponse) MarshalJSON() ([]byte, error)
type WebappsDeleteCall
func (c *WebappsDeleteCall) Context(ctx context.Context) *WebappsDeleteCall
func (c *WebappsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *WebappsDeleteCall) Fields(s ...googleapi.Field) *WebappsDeleteCall
func (c *WebappsDeleteCall) Header() http.Header
type WebappsGetCall
func (c *WebappsGetCall) Context(ctx context.Context) *WebappsGetCall
func (c *WebappsGetCall) Do(opts ...googleapi.CallOption) (*WebApp, error)
func (c *WebappsGetCall) Fields(s ...googleapi.Field) *WebappsGetCall
func (c *WebappsGetCall) Header() http.Header
func (c *WebappsGetCall) IfNoneMatch(entityTag string) *WebappsGetCall
type WebappsInsertCall
func (c *WebappsInsertCall) Context(ctx context.Context) *WebappsInsertCall
func (c *WebappsInsertCall) Do(opts ...googleapi.CallOption) (*WebApp, error)
func (c *WebappsInsertCall) Fields(s ...googleapi.Field) *WebappsInsertCall
func (c *WebappsInsertCall) Header() http.Header
type WebappsListCall
func (c *WebappsListCall) Context(ctx context.Context) *WebappsListCall
func (c *WebappsListCall) Do(opts ...googleapi.CallOption) (*WebAppsListResponse, error)
func (c *WebappsListCall) Fields(s ...googleapi.Field) *WebappsListCall
func (c *WebappsListCall) Header() http.Header
func (c *WebappsListCall) IfNoneMatch(entityTag string) *WebappsListCall
type WebappsService
func NewWebappsService(s *Service) *WebappsService
func (r *WebappsService) Delete(enterpriseId string, webAppId string) *WebappsDeleteCall
func (r *WebappsService) Get(enterpriseId string, webAppId string) *WebappsGetCall
func (r *WebappsService) Insert(enterpriseId string, webapp *WebApp) *WebappsInsertCall
func (r *WebappsService) List(enterpriseId string) *WebappsListCall
func (r *WebappsService) Update(enterpriseId string, webAppId string, webapp *WebApp) *WebappsUpdateCall
type WebappsUpdateCall
func (c *WebappsUpdateCall) Context(ctx context.Context) *WebappsUpdateCall
func (c *WebappsUpdateCall) Do(opts ...googleapi.CallOption) (*WebApp, error)
func (c *WebappsUpdateCall) Fields(s ...googleapi.Field) *WebappsUpdateCall
func (c *WebappsUpdateCall) Header() http.Header
Constants ¶
View Source
const (
	// Manage corporate Android devices
	AndroidenterpriseScope = "https://www.googleapis.com/auth/androidenterprise"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Administrator ¶
type Administrator struct {
	// Email: The admin's email address.
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

Administrator: This represents an enterprise admin who can manage the enterprise in the managed Google Play store.

func (Administrator) MarshalJSON ¶
func (s Administrator) MarshalJSON() ([]byte, error)
type AdministratorWebToken ¶
type AdministratorWebToken struct {
	// Token: An opaque token to be passed to the Play front-end to generate an
	// iframe.
	Token string `json:"token,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Token") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Token") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdministratorWebToken: A token authorizing an admin to access an iframe.

func (AdministratorWebToken) MarshalJSON ¶
func (s AdministratorWebToken) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpec ¶
type AdministratorWebTokenSpec struct {
	// ManagedConfigurations: Options for displaying the Managed Configuration
	// page.
	ManagedConfigurations *AdministratorWebTokenSpecManagedConfigurations `json:"managedConfigurations,omitempty"`
	// Parent: The URI of the parent frame hosting the iframe. To prevent XSS, the
	// iframe may not be hosted at other URIs. This URI must be https. Use
	// whitespaces to separate multiple parent URIs.
	Parent string `json:"parent,omitempty"`
	// Permission: Deprecated. Use PlaySearch.approveApps.
	//
	// Possible values:
	//   "unknown" - Unknown permission.
	//   "approveApps" - Permission to approve and unapprove apps.
	//   "manageMcm" - Permission to manage app restrictions.
	Permission []string `json:"permission,omitempty"`
	// PlaySearch: Options for displaying the managed Play Search apps page.
	PlaySearch *AdministratorWebTokenSpecPlaySearch `json:"playSearch,omitempty"`
	// PrivateApps: Options for displaying the Private Apps page.
	PrivateApps *AdministratorWebTokenSpecPrivateApps `json:"privateApps,omitempty"`
	// StoreBuilder: Options for displaying the Organize apps page.
	StoreBuilder *AdministratorWebTokenSpecStoreBuilder `json:"storeBuilder,omitempty"`
	// WebApps: Options for displaying the Web Apps page.
	WebApps *AdministratorWebTokenSpecWebApps `json:"webApps,omitempty"`
	// ZeroTouch: Options for displaying the Zero Touch page.
	ZeroTouch *AdministratorWebTokenSpecZeroTouch `json:"zeroTouch,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ManagedConfigurations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagedConfigurations") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdministratorWebTokenSpec: Specification for a token used to generate iframes. The token specifies what data the admin is allowed to modify and the URI the iframe is allowed to communiate with.

func (AdministratorWebTokenSpec) MarshalJSON ¶
func (s AdministratorWebTokenSpec) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecManagedConfigurations ¶
added in v0.2.0
type AdministratorWebTokenSpecManagedConfigurations struct {
	// Enabled: Whether the Managed Configuration page is displayed. Default is
	// true.
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
func (AdministratorWebTokenSpecManagedConfigurations) MarshalJSON ¶
added in v0.2.0
func (s AdministratorWebTokenSpecManagedConfigurations) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecPlaySearch ¶
type AdministratorWebTokenSpecPlaySearch struct {
	// ApproveApps: Allow access to the iframe in approve mode. Default is false.
	ApproveApps bool `json:"approveApps,omitempty"`
	// Enabled: Whether the managed Play Search apps page is displayed. Default is
	// true.
	Enabled bool `json:"enabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApproveApps") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApproveApps") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (AdministratorWebTokenSpecPlaySearch) MarshalJSON ¶
func (s AdministratorWebTokenSpecPlaySearch) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecPrivateApps ¶
type AdministratorWebTokenSpecPrivateApps struct {
	// Enabled: Whether the Private Apps page is displayed. Default is true.
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
func (AdministratorWebTokenSpecPrivateApps) MarshalJSON ¶
func (s AdministratorWebTokenSpecPrivateApps) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecStoreBuilder ¶
type AdministratorWebTokenSpecStoreBuilder struct {
	// Enabled: Whether the Organize apps page is displayed. Default is true.
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
func (AdministratorWebTokenSpecStoreBuilder) MarshalJSON ¶
func (s AdministratorWebTokenSpecStoreBuilder) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecWebApps ¶
type AdministratorWebTokenSpecWebApps struct {
	// Enabled: Whether the Web Apps page is displayed. Default is true.
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
func (AdministratorWebTokenSpecWebApps) MarshalJSON ¶
func (s AdministratorWebTokenSpecWebApps) MarshalJSON() ([]byte, error)
type AdministratorWebTokenSpecZeroTouch ¶
added in v0.46.0
type AdministratorWebTokenSpecZeroTouch struct {
	// Enabled: Whether zero-touch embedded UI is usable with this token. If
	// enabled, the admin can link zero-touch customers to this enterprise.
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
func (AdministratorWebTokenSpecZeroTouch) MarshalJSON ¶
added in v0.46.0
func (s AdministratorWebTokenSpecZeroTouch) MarshalJSON() ([]byte, error)
type AppRestrictionsSchema ¶
type AppRestrictionsSchema struct {
	// Kind: Deprecated.
	Kind string `json:"kind,omitempty"`
	// Restrictions: The set of restrictions that make up this schema.
	Restrictions []*AppRestrictionsSchemaRestriction `json:"restrictions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Kind") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Kind") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppRestrictionsSchema: Represents the list of app restrictions available to be pre-configured for the product.

func (AppRestrictionsSchema) MarshalJSON ¶
func (s AppRestrictionsSchema) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaChangeEvent ¶
type AppRestrictionsSchemaChangeEvent struct {
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") for
	// which the app restriction schema changed. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProductId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppRestrictionsSchemaChangeEvent: An event generated when a new app version is uploaded to Google Play and its app restrictions schema changed. To fetch the app restrictions schema for an app, use Products.getAppRestrictionsSchema on the EMM API.

func (AppRestrictionsSchemaChangeEvent) MarshalJSON ¶
func (s AppRestrictionsSchemaChangeEvent) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaRestriction ¶
type AppRestrictionsSchemaRestriction struct {
	// DefaultValue: The default value of the restriction. bundle and bundleArray
	// restrictions never have a default value.
	DefaultValue *AppRestrictionsSchemaRestrictionRestrictionValue `json:"defaultValue,omitempty"`
	// Description: A longer description of the restriction, giving more detail of
	// what it affects.
	Description string `json:"description,omitempty"`
	// Entry: For choice or multiselect restrictions, the list of possible entries'
	// human-readable names.
	Entry []string `json:"entry,omitempty"`
	// EntryValue: For choice or multiselect restrictions, the list of possible
	// entries' machine-readable values. These values should be used in the
	// configuration, either as a single string value for a choice restriction or
	// in a stringArray for a multiselect restriction.
	EntryValue []string `json:"entryValue,omitempty"`
	// Key: The unique key that the product uses to identify the restriction, e.g.
	// "com.google.android.gm.fieldname".
	Key string `json:"key,omitempty"`
	// NestedRestriction: For bundle or bundleArray restrictions, the list of
	// nested restrictions. A bundle restriction is always nested within a
	// bundleArray restriction, and a bundleArray restriction is at most two levels
	// deep.
	NestedRestriction []*AppRestrictionsSchemaRestriction `json:"nestedRestriction,omitempty"`
	// RestrictionType: The type of the restriction.
	//
	// Possible values:
	//   "bool" - A restriction of boolean type.
	//   "string" - A restriction of string type.
	//   "integer" - A restriction of integer type.
	//   "choice" - A choice of one item from a set.
	//   "multiselect" - A choice of multiple items from a set.
	//   "hidden" - A hidden restriction of string type (the default value can be
	// used to pass along information that cannot be modified, such as a version
	// code).
	//   "bundle" - [M+ devices only] A bundle of restrictions
	//   "bundleArray" - [M+ devices only] An array of restriction bundles
	RestrictionType string `json:"restrictionType,omitempty"`
	// Title: The name of the restriction.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DefaultValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DefaultValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppRestrictionsSchemaRestriction: A restriction in the App Restriction Schema represents a piece of configuration that may be pre-applied.

func (AppRestrictionsSchemaRestriction) MarshalJSON ¶
func (s AppRestrictionsSchemaRestriction) MarshalJSON() ([]byte, error)
type AppRestrictionsSchemaRestrictionRestrictionValue ¶
type AppRestrictionsSchemaRestrictionRestrictionValue struct {
	// Type: The type of the value being provided.
	//
	// Possible values:
	//   "bool" - A restriction of boolean type.
	//   "string" - A restriction of string type.
	//   "integer" - A restriction of integer type.
	//   "choice" - A choice of one item from a set.
	//   "multiselect" - A choice of multiple items from a set.
	//   "hidden" - A hidden restriction of string type (the default value can be
	// used to pass along information that cannot be modified, such as a version
	// code).
	//   "bundle" - [M+ devices only] A bundle of restrictions
	//   "bundleArray" - [M+ devices only] An array of restriction bundles
	Type string `json:"type,omitempty"`
	// ValueBool: The boolean value - this will only be present if type is bool.
	ValueBool bool `json:"valueBool,omitempty"`
	// ValueInteger: The integer value - this will only be present if type is
	// integer.
	ValueInteger int64 `json:"valueInteger,omitempty"`
	// ValueMultiselect: The list of string values - this will only be present if
	// type is multiselect.
	ValueMultiselect []string `json:"valueMultiselect,omitempty"`
	// ValueString: The string value - this will be present for types string,
	// choice and hidden.
	ValueString string `json:"valueString,omitempty"`
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

AppRestrictionsSchemaRestrictionRestrictionValue: A typed value for the restriction.

func (AppRestrictionsSchemaRestrictionRestrictionValue) MarshalJSON ¶
func (s AppRestrictionsSchemaRestrictionRestrictionValue) MarshalJSON() ([]byte, error)
type AppState ¶
added in v0.7.0
type AppState struct {
	// KeyedAppState: List of keyed app states. This field will always be present.
	KeyedAppState []*KeyedAppState `json:"keyedAppState,omitempty"`
	// PackageName: The package name of the app. This field will always be present.
	PackageName string `json:"packageName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "KeyedAppState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KeyedAppState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppState: List of states set by the app.

func (AppState) MarshalJSON ¶
added in v0.7.0
func (s AppState) MarshalJSON() ([]byte, error)
type AppUpdateEvent ¶
type AppUpdateEvent struct {
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") that was
	// updated. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProductId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppUpdateEvent: An event generated when a new version of an app is uploaded to Google Play. Notifications are sent for new public versions only: alpha, beta, or canary versions do not generate this event. To fetch up-to-date version history for an app, use Products.Get on the EMM API.

func (AppUpdateEvent) MarshalJSON ¶
func (s AppUpdateEvent) MarshalJSON() ([]byte, error)
type AppVersion ¶
type AppVersion struct {
	// IsProduction: True if this version is a production APK.
	IsProduction bool `json:"isProduction,omitempty"`
	// TargetSdkVersion: The SDK version this app targets, as specified in the
	// manifest of the APK. See
	// http://developer.android.com/guide/topics/manifest/uses-sdk-element.html
	TargetSdkVersion int64 `json:"targetSdkVersion,omitempty"`
	// Track: Deprecated, use trackId instead.
	//
	// Possible values:
	//   "appTrackUnspecified"
	//   "production"
	//   "beta"
	//   "alpha"
	Track string `json:"track,omitempty"`
	// TrackId: Track ids that the app version is published in. Replaces the track
	// field (deprecated), but doesn't include the production track (see
	// isProduction instead).
	TrackId []string `json:"trackId,omitempty"`
	// VersionCode: Unique increasing identifier for the app version.
	VersionCode int64 `json:"versionCode,omitempty"`
	// VersionString: The string used in the Play store by the app developer to
	// identify the version. The string is not necessarily unique or localized (for
	// example, the string could be "1.4").
	VersionString string `json:"versionString,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IsProduction") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsProduction") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppVersion: This represents a single version of the app.

func (AppVersion) MarshalJSON ¶
func (s AppVersion) MarshalJSON() ([]byte, error)
type ApprovalUrlInfo ¶
type ApprovalUrlInfo struct {
	// ApprovalUrl: A URL that displays a product's permissions and that can also
	// be used to approve the product with the Products.approve call.
	ApprovalUrl string `json:"approvalUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApprovalUrl") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApprovalUrl") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApprovalUrlInfo: Information on an approval URL.

func (ApprovalUrlInfo) MarshalJSON ¶
func (s ApprovalUrlInfo) MarshalJSON() ([]byte, error)
type AuthenticationToken ¶
type AuthenticationToken struct {
	// Token: The authentication token to be passed to the device policy client on
	// the device where it can be used to provision the account for which this
	// token was generated.
	Token string `json:"token,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Token") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Token") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuthenticationToken: An AuthenticationToken is used by the EMM's device policy client on a device to provision the given EMM-managed user on that device.

func (AuthenticationToken) MarshalJSON ¶
func (s AuthenticationToken) MarshalJSON() ([]byte, error)
type AutoInstallConstraint ¶
type AutoInstallConstraint struct {
	// ChargingStateConstraint: Charging state constraint.
	//
	// Possible values:
	//   "chargingStateConstraintUnspecified"
	//   "chargingNotRequired" - Device doesn't have to be charging.
	//   "chargingRequired" - Device has to be charging.
	ChargingStateConstraint string `json:"chargingStateConstraint,omitempty"`
	// DeviceIdleStateConstraint: Device idle state constraint.
	//
	// Possible values:
	//   "deviceIdleStateConstraintUnspecified"
	//   "deviceIdleNotRequired" - Device doesn't have to be idle, app can be
	// installed while the user is interacting with the device.
	//   "deviceIdleRequired" - Device has to be idle.
	DeviceIdleStateConstraint string `json:"deviceIdleStateConstraint,omitempty"`
	// NetworkTypeConstraint: Network type constraint.
	//
	// Possible values:
	//   "networkTypeConstraintUnspecified"
	//   "anyNetwork" - Any active networks (Wi-Fi, cellular, etc.).
	//   "unmeteredNetwork" - Any unmetered network (e.g. Wi-FI).
	NetworkTypeConstraint string `json:"networkTypeConstraint,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ChargingStateConstraint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChargingStateConstraint") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutoInstallConstraint: The auto-install constraint. Defines a set of restrictions for installation. At least one of the fields must be set.

func (AutoInstallConstraint) MarshalJSON ¶
func (s AutoInstallConstraint) MarshalJSON() ([]byte, error)
type AutoInstallPolicy ¶
type AutoInstallPolicy struct {
	// AutoInstallConstraint: The constraints for auto-installing the app. You can
	// specify a maximum of one constraint.
	AutoInstallConstraint []*AutoInstallConstraint `json:"autoInstallConstraint,omitempty"`
	// AutoInstallMode: The auto-install mode. If unset, defaults to
	// "doNotAutoInstall". An app is automatically installed regardless of a set
	// maintenance window.
	//
	// Possible values:
	//   "autoInstallModeUnspecified"
	//   "doNotAutoInstall" - The product is not installed automatically, the user
	// needs to install it from the Play Store.
	//   "autoInstallOnce" - The product is automatically installed once, if the
	// user uninstalls the product it will not be installed again.
	//   "forceAutoInstall" - The product is automatically installed, if the user
	// uninstalls the product it will be installed again. On managed devices the
	// DPC should block uninstall.
	AutoInstallMode string `json:"autoInstallMode,omitempty"`
	// AutoInstallPriority: The priority of the install, as an unsigned integer. A
	// lower number means higher priority.
	AutoInstallPriority int64 `json:"autoInstallPriority,omitempty"`
	// MinimumVersionCode: The minimum version of the app. If a lower version of
	// the app is installed, then the app will be auto-updated according to the
	// auto-install constraints, instead of waiting for the regular auto-update.
	// You can set a minimum version code for at most 20 apps per device.
	MinimumVersionCode int64 `json:"minimumVersionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoInstallConstraint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoInstallConstraint") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (AutoInstallPolicy) MarshalJSON ¶
func (s AutoInstallPolicy) MarshalJSON() ([]byte, error)
type ConfigurationVariables ¶
type ConfigurationVariables struct {
	// McmId: The ID of the managed configurations settings.
	McmId string `json:"mcmId,omitempty"`
	// VariableSet: The variable set that is attributed to the user.
	VariableSet []*VariableSet `json:"variableSet,omitempty"`
	// ForceSendFields is a list of field names (e.g. "McmId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "McmId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConfigurationVariables: A configuration variables resource contains the managed configuration settings ID to be applied to a single user, as well as the variable set that is attributed to the user. The variable set will be used to replace placeholders in the managed configuration settings.

func (ConfigurationVariables) MarshalJSON ¶
func (s ConfigurationVariables) MarshalJSON() ([]byte, error)
type Device ¶
type Device struct {
	// AndroidId: The Google Play Services Android ID for the device encoded as a
	// lowercase hex string. For example, "123456789abcdef0".
	AndroidId string `json:"androidId,omitempty"`
	// Device: The internal hardware codename of the device. This comes from
	// android.os.Build.DEVICE. (field named "device" per
	// logs/wireless/android/android_checkin.proto)
	Device string `json:"device,omitempty"`
	// LatestBuildFingerprint: The build fingerprint of the device if known.
	LatestBuildFingerprint string `json:"latestBuildFingerprint,omitempty"`
	// Maker: The manufacturer of the device. This comes from
	// android.os.Build.MANUFACTURER.
	Maker string `json:"maker,omitempty"`
	// ManagementType: Identifies the extent to which the device is controlled by a
	// managed Google Play EMM in various deployment configurations. Possible
	// values include: - "managedDevice", a device that has the EMM's device policy
	// controller (DPC) as the device owner. - "managedProfile", a device that has
	// a profile managed by the DPC (DPC is profile owner) in addition to a
	// separate, personal profile that is unavailable to the DPC. - "containerApp",
	// no longer used (deprecated). - "unmanagedProfile", a device that has been
	// allowed (by the domain's admin, using the Admin Console to enable the
	// privilege) to use managed Google Play, but the profile is itself not owned
	// by a DPC.
	//
	// Possible values:
	//   "managedDevice"
	//   "managedProfile"
	//   "containerApp"
	//   "unmanagedProfile"
	ManagementType string `json:"managementType,omitempty"`
	// Model: The model name of the device. This comes from android.os.Build.MODEL.
	Model string `json:"model,omitempty"`
	// Policy: The policy enforced on the device.
	Policy *Policy `json:"policy,omitempty"`
	// Product: The product name of the device. This comes from
	// android.os.Build.PRODUCT.
	Product string `json:"product,omitempty"`
	// Report: The device report updated with the latest app states.
	Report *DeviceReport `json:"report,omitempty"`
	// RetailBrand: Retail brand for the device, if set. See android.os.Build.BRAND
	RetailBrand string `json:"retailBrand,omitempty"`
	// SdkVersion: API compatibility version.
	SdkVersion int64 `json:"sdkVersion,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AndroidId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndroidId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Device: A Devices resource represents a mobile device managed by the EMM and belonging to a specific enterprise user.

func (Device) MarshalJSON ¶
func (s Device) MarshalJSON() ([]byte, error)
type DeviceReport ¶
added in v0.7.0
type DeviceReport struct {
	// AppState: List of app states set by managed apps on the device. App states
	// are defined by the app's developers. This field will always be present.
	AppState []*AppState `json:"appState,omitempty"`
	// LastUpdatedTimestampMillis: The timestamp of the last report update in
	// milliseconds since epoch. This field will always be present.
	LastUpdatedTimestampMillis int64 `json:"lastUpdatedTimestampMillis,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "AppState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceReport: Device report updated with the latest app states for managed apps on the device.

func (DeviceReport) MarshalJSON ¶
added in v0.7.0
func (s DeviceReport) MarshalJSON() ([]byte, error)
type DeviceReportUpdateEvent ¶
added in v0.7.0
type DeviceReportUpdateEvent struct {
	// DeviceId: The Android ID of the device. This field will always be present.
	DeviceId string `json:"deviceId,omitempty"`
	// Report: The device report updated with the latest app states. This field
	// will always be present.
	Report *DeviceReport `json:"report,omitempty"`
	// UserId: The ID of the user. This field will always be present.
	UserId string `json:"userId,omitempty"`
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

DeviceReportUpdateEvent: An event generated when an updated device report is available.

func (DeviceReportUpdateEvent) MarshalJSON ¶
added in v0.7.0
func (s DeviceReportUpdateEvent) MarshalJSON() ([]byte, error)
type DeviceState ¶
type DeviceState struct {
	// AccountState: The state of the Google account on the device. "enabled"
	// indicates that the Google account on the device can be used to access Google
	// services (including Google Play), while "disabled" means that it cannot. A
	// new device is initially in the "disabled" state.
	//
	// Possible values:
	//   "enabled"
	//   "disabled"
	AccountState string `json:"accountState,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceState: The state of a user's device, as accessed by the getState and setState methods on device resources.

func (DeviceState) MarshalJSON ¶
func (s DeviceState) MarshalJSON() ([]byte, error)
type DevicesForceReportUploadCall ¶
added in v0.7.0
type DevicesForceReportUploadCall struct {
	// contains filtered or unexported fields
}
func (*DevicesForceReportUploadCall) Context ¶
added in v0.7.0
func (c *DevicesForceReportUploadCall) Context(ctx context.Context) *DevicesForceReportUploadCall

Context sets the context to be used in this call's Do method.

func (*DevicesForceReportUploadCall) Do ¶
added in v0.7.0
func (c *DevicesForceReportUploadCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.devices.forceReportUpload" call.

func (*DevicesForceReportUploadCall) Fields ¶
added in v0.7.0
func (c *DevicesForceReportUploadCall) Fields(s ...googleapi.Field) *DevicesForceReportUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesForceReportUploadCall) Header ¶
added in v0.7.0
func (c *DevicesForceReportUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DevicesGetCall ¶
type DevicesGetCall struct {
	// contains filtered or unexported fields
}
func (*DevicesGetCall) Context ¶
func (c *DevicesGetCall) Context(ctx context.Context) *DevicesGetCall

Context sets the context to be used in this call's Do method.

func (*DevicesGetCall) Do ¶
func (c *DevicesGetCall) Do(opts ...googleapi.CallOption) (*Device, error)

Do executes the "androidenterprise.devices.get" call. Any non-2xx status code is an error. Response headers are in either *Device.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DevicesGetCall) Fields ¶
func (c *DevicesGetCall) Fields(s ...googleapi.Field) *DevicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesGetCall) Header ¶
func (c *DevicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DevicesGetCall) IfNoneMatch ¶
func (c *DevicesGetCall) IfNoneMatch(entityTag string) *DevicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DevicesGetStateCall ¶
type DevicesGetStateCall struct {
	// contains filtered or unexported fields
}
func (*DevicesGetStateCall) Context ¶
func (c *DevicesGetStateCall) Context(ctx context.Context) *DevicesGetStateCall

Context sets the context to be used in this call's Do method.

func (*DevicesGetStateCall) Do ¶
func (c *DevicesGetStateCall) Do(opts ...googleapi.CallOption) (*DeviceState, error)

Do executes the "androidenterprise.devices.getState" call. Any non-2xx status code is an error. Response headers are in either *DeviceState.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DevicesGetStateCall) Fields ¶
func (c *DevicesGetStateCall) Fields(s ...googleapi.Field) *DevicesGetStateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesGetStateCall) Header ¶
func (c *DevicesGetStateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DevicesGetStateCall) IfNoneMatch ¶
func (c *DevicesGetStateCall) IfNoneMatch(entityTag string) *DevicesGetStateCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DevicesListCall ¶
type DevicesListCall struct {
	// contains filtered or unexported fields
}
func (*DevicesListCall) Context ¶
func (c *DevicesListCall) Context(ctx context.Context) *DevicesListCall

Context sets the context to be used in this call's Do method.

func (*DevicesListCall) Do ¶
func (c *DevicesListCall) Do(opts ...googleapi.CallOption) (*DevicesListResponse, error)

Do executes the "androidenterprise.devices.list" call. Any non-2xx status code is an error. Response headers are in either *DevicesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DevicesListCall) Fields ¶
func (c *DevicesListCall) Fields(s ...googleapi.Field) *DevicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesListCall) Header ¶
func (c *DevicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DevicesListCall) IfNoneMatch ¶
func (c *DevicesListCall) IfNoneMatch(entityTag string) *DevicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type DevicesListResponse ¶
type DevicesListResponse struct {
	// Device: A managed device.
	Device []*Device `json:"device,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Device") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Device") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (DevicesListResponse) MarshalJSON ¶
func (s DevicesListResponse) MarshalJSON() ([]byte, error)
type DevicesService ¶
type DevicesService struct {
	// contains filtered or unexported fields
}
func NewDevicesService ¶
func NewDevicesService(s *Service) *DevicesService
func (*DevicesService) ForceReportUpload ¶
added in v0.7.0
func (r *DevicesService) ForceReportUpload(enterpriseId string, userId string, deviceId string) *DevicesForceReportUploadCall

ForceReportUpload: Uploads a report containing any changes in app states on the device since the last report was generated. You can call this method up to 3 times every 24 hours for a given device. If you exceed the quota, then the Google Play EMM API returns HTTP 429 Too Many Requests.

- deviceId: The ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*DevicesService) Get ¶
func (r *DevicesService) Get(enterpriseId string, userId string, deviceId string) *DevicesGetCall

Get: Retrieves the details of a device.

- deviceId: The ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*DevicesService) GetState ¶
func (r *DevicesService) GetState(enterpriseId string, userId string, deviceId string) *DevicesGetStateCall

GetState: Retrieves whether a device's access to Google services is enabled or disabled. The device state takes effect only if enforcing EMM policies on Android devices is enabled in the Google Admin Console. Otherwise, the device state is ignored and all devices are allowed access to Google services. This is only supported for Google-managed users.

- deviceId: The ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*DevicesService) List ¶
func (r *DevicesService) List(enterpriseId string, userId string) *DevicesListCall

List: Retrieves the IDs of all of a user's devices.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*DevicesService) SetState ¶
func (r *DevicesService) SetState(enterpriseId string, userId string, deviceId string, devicestate *DeviceState) *DevicesSetStateCall

SetState: Sets whether a device's access to Google services is enabled or disabled. The device state takes effect only if enforcing EMM policies on Android devices is enabled in the Google Admin Console. Otherwise, the device state is ignored and all devices are allowed access to Google services. This is only supported for Google-managed users.

- deviceId: The ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*DevicesService) Update ¶
func (r *DevicesService) Update(enterpriseId string, userId string, deviceId string, device *Device) *DevicesUpdateCall

Update: Updates the device policy. To ensure the policy is properly enforced, you need to prevent unmanaged accounts from accessing Google Play by setting the allowed_accounts in the managed configuration for the Google Play package. See restrict accounts in Google Play. When provisioning a new device, you should set the device policy using this method before adding the managed Google Play Account to the device, otherwise the policy will not be applied for a short period of time after adding the account to the device.

- deviceId: The ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

type DevicesSetStateCall ¶
type DevicesSetStateCall struct {
	// contains filtered or unexported fields
}
func (*DevicesSetStateCall) Context ¶
func (c *DevicesSetStateCall) Context(ctx context.Context) *DevicesSetStateCall

Context sets the context to be used in this call's Do method.

func (*DevicesSetStateCall) Do ¶
func (c *DevicesSetStateCall) Do(opts ...googleapi.CallOption) (*DeviceState, error)

Do executes the "androidenterprise.devices.setState" call. Any non-2xx status code is an error. Response headers are in either *DeviceState.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DevicesSetStateCall) Fields ¶
func (c *DevicesSetStateCall) Fields(s ...googleapi.Field) *DevicesSetStateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesSetStateCall) Header ¶
func (c *DevicesSetStateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type DevicesUpdateCall ¶
type DevicesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*DevicesUpdateCall) Context ¶
func (c *DevicesUpdateCall) Context(ctx context.Context) *DevicesUpdateCall

Context sets the context to be used in this call's Do method.

func (*DevicesUpdateCall) Do ¶
func (c *DevicesUpdateCall) Do(opts ...googleapi.CallOption) (*Device, error)

Do executes the "androidenterprise.devices.update" call. Any non-2xx status code is an error. Response headers are in either *Device.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DevicesUpdateCall) Fields ¶
func (c *DevicesUpdateCall) Fields(s ...googleapi.Field) *DevicesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DevicesUpdateCall) Header ¶
func (c *DevicesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DevicesUpdateCall) UpdateMask ¶
func (c *DevicesUpdateCall) UpdateMask(updateMask string) *DevicesUpdateCall

UpdateMask sets the optional parameter "updateMask": Mask that identifies which fields to update. If not set, all modifiable fields will be modified. When set in a query parameter, this field should be specified as updateMask=<field1>,<field2>,...

type EnrollmentToken ¶
added in v0.207.0
type EnrollmentToken struct {
	// Duration: [Optional] The length of time the enrollment token is valid,
	// ranging from 1 minute to `Durations.MAX_VALUE`
	// (https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/Durations.html#MAX_VALUE),
	// approximately 10,000 years. If not specified, the default duration is 1
	// hour.
	Duration string `json:"duration,omitempty"`
	// EnrollmentTokenType: [Required] The type of the enrollment token.
	//
	// Possible values:
	//   "enrollmentTokenTypeUnspecified" - The value is unused.
	//   "userlessDevice" - The enrollment token is for a userless device.
	//   "userDevice" - The enrollment token is for a user device.
	EnrollmentTokenType string `json:"enrollmentTokenType,omitempty"`
	// GoogleAuthenticationOptions: [Optional] Provides options related to Google
	// authentication during the enrollment.
	GoogleAuthenticationOptions *EnrollmentTokenGoogleAuthenticationOptions `json:"googleAuthenticationOptions,omitempty"`
	// Token: The token value that's passed to the device and authorizes the device
	// to enroll. This is a read-only field generated by the server.
	Token string `json:"token,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Duration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Duration") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EnrollmentToken: A token used to enroll a device.

func (EnrollmentToken) MarshalJSON ¶
added in v0.207.0
func (s EnrollmentToken) MarshalJSON() ([]byte, error)
type EnrollmentTokenGoogleAuthenticationOptions ¶
added in v0.244.0
type EnrollmentTokenGoogleAuthenticationOptions struct {
	// AuthenticationRequirement: [Optional] Specifies whether user should
	// authenticate with Google during enrollment. This setting, if
	// specified,`GoogleAuthenticationSettings` specified for the enterprise
	// resource is ignored for devices enrolled with this token.
	//
	// Possible values:
	//   "authenticationRequirementUnspecified" - The value is unused.
	//   "optional" - Google authentication is optional for the user. This means
	// the user can choose to skip Google authentication during enrollment.
	//   "required" - Google authentication is required for the user. This means
	// the user must authenticate with a Google account to proceed.
	AuthenticationRequirement string `json:"authenticationRequirement,omitempty"`
	// RequiredAccountEmail: [Optional] Specifies the managed Google account that
	// the user must use during enrollment.`AuthenticationRequirement` must be set
	// to`REQUIRED` if this field is set.
	RequiredAccountEmail string `json:"requiredAccountEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuthenticationRequirement")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthenticationRequirement") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EnrollmentTokenGoogleAuthenticationOptions: Options for Google authentication during the enrollment.

func (EnrollmentTokenGoogleAuthenticationOptions) MarshalJSON ¶
added in v0.244.0
func (s EnrollmentTokenGoogleAuthenticationOptions) MarshalJSON() ([]byte, error)
type EnrollmentTokensCreateCall ¶
added in v0.218.0
type EnrollmentTokensCreateCall struct {
	// contains filtered or unexported fields
}
func (*EnrollmentTokensCreateCall) Context ¶
added in v0.218.0
func (c *EnrollmentTokensCreateCall) Context(ctx context.Context) *EnrollmentTokensCreateCall

Context sets the context to be used in this call's Do method.

func (*EnrollmentTokensCreateCall) Do ¶
added in v0.218.0
func (c *EnrollmentTokensCreateCall) Do(opts ...googleapi.CallOption) (*EnrollmentToken, error)

Do executes the "androidenterprise.enrollmentTokens.create" call. Any non-2xx status code is an error. Response headers are in either *EnrollmentToken.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnrollmentTokensCreateCall) Fields ¶
added in v0.218.0
func (c *EnrollmentTokensCreateCall) Fields(s ...googleapi.Field) *EnrollmentTokensCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnrollmentTokensCreateCall) Header ¶
added in v0.218.0
func (c *EnrollmentTokensCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnrollmentTokensService ¶
added in v0.218.0
type EnrollmentTokensService struct {
	// contains filtered or unexported fields
}
func NewEnrollmentTokensService ¶
added in v0.218.0
func NewEnrollmentTokensService(s *Service) *EnrollmentTokensService
func (*EnrollmentTokensService) Create ¶
added in v0.218.0
func (r *EnrollmentTokensService) Create(enterpriseId string, enrollmenttoken *EnrollmentToken) *EnrollmentTokensCreateCall

Create: Returns a token for device enrollment. The DPC can encode this token within the QR/NFC/zero-touch enrollment payload or fetch it before calling the on-device API to authenticate the user. The token can be generated for each device or reused across multiple devices.

- enterpriseId: The ID of the enterprise.

type Enterprise ¶
type Enterprise struct {
	// Administrator: Admins of the enterprise. This is only supported for
	// enterprises created via the EMM-initiated flow.
	Administrator []*Administrator `json:"administrator,omitempty"`
	// EnterpriseType: The type of the enterprise.
	//
	// Possible values:
	//   "enterpriseTypeUnspecified" - This value is not used.
	//   "managedGoogleDomain" - The enterprise belongs to a managed Google domain.
	//   "managedGooglePlayAccountsEnterprise" - The enterprise is a managed Google
	// Play Accounts enterprise.
	EnterpriseType string `json:"enterpriseType,omitempty"`
	// GoogleAuthenticationSettings: Output only. Settings for Google-provided user
	// authentication.
	GoogleAuthenticationSettings *GoogleAuthenticationSettings `json:"googleAuthenticationSettings,omitempty"`
	// Id: The unique ID for the enterprise.
	Id string `json:"id,omitempty"`
	// ManagedGoogleDomainType: The type of managed Google domain
	//
	// Possible values:
	//   "managedGoogleDomainTypeUnspecified" - The managed Google domain type is
	// not specified.
	//   "typeTeam" - The managed Google domain is an email-verified team.
	//   "typeDomain" - The managed Google domain is domain-verified.
	ManagedGoogleDomainType string `json:"managedGoogleDomainType,omitempty"`
	// Name: The name of the enterprise, for example, "Example, Inc".
	Name string `json:"name,omitempty"`
	// PrimaryDomain: The enterprise's primary domain, such as "example.com".
	PrimaryDomain string `json:"primaryDomain,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Administrator") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Administrator") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Enterprise: An Enterprises resource represents the binding between an EMM and a specific organization. That binding can be instantiated in one of two different ways using this API as follows: - For Google managed domain customers, the process involves using Enterprises.enroll and Enterprises.setAccount (in conjunction with artifacts obtained from the Admin console and the Google API Console) and submitted to the EMM through a more-or-less manual process. - For managed Google Play Accounts customers, the process involves using Enterprises.generateSignupUrl and Enterprises.completeSignup in conjunction with the managed Google Play sign-up UI (Google-provided mechanism) to create the binding without manual steps. As an EMM, you can support either or both approaches in your EMM console. See Create an Enterprise for details.

func (Enterprise) MarshalJSON ¶
func (s Enterprise) MarshalJSON() ([]byte, error)
type EnterpriseAccount ¶
type EnterpriseAccount struct {
	// AccountEmail: The email address of the service account.
	AccountEmail string `json:"accountEmail,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountEmail") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountEmail") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EnterpriseAccount: A service account that can be used to authenticate as the enterprise to API calls that require such authentication.

func (EnterpriseAccount) MarshalJSON ¶
func (s EnterpriseAccount) MarshalJSON() ([]byte, error)
type EnterpriseAuthenticationAppLinkConfig ¶
added in v0.75.0
type EnterpriseAuthenticationAppLinkConfig struct {
	// Uri: An authentication url.
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

EnterpriseAuthenticationAppLinkConfig: An authentication URL configuration for the authenticator app of an identity provider.

func (EnterpriseAuthenticationAppLinkConfig) MarshalJSON ¶
added in v0.75.0
func (s EnterpriseAuthenticationAppLinkConfig) MarshalJSON() ([]byte, error)
type EnterpriseUpgradeEvent ¶
added in v0.224.0
type EnterpriseUpgradeEvent struct {
	// UpgradeState: The upgrade state.
	//
	// Possible values:
	//   "upgradeStateUnspecified" - Unspecified. This value is not used.
	//   "upgradeStateSucceeded" - The upgrade has succeeded.
	UpgradeState string `json:"upgradeState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "UpgradeState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "UpgradeState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EnterpriseUpgradeEvent: An event generated when an enterprise is upgraded.

func (EnterpriseUpgradeEvent) MarshalJSON ¶
added in v0.224.0
func (s EnterpriseUpgradeEvent) MarshalJSON() ([]byte, error)
type EnterprisesAcknowledgeNotificationSetCall ¶
type EnterprisesAcknowledgeNotificationSetCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesAcknowledgeNotificationSetCall) Context ¶
func (c *EnterprisesAcknowledgeNotificationSetCall) Context(ctx context.Context) *EnterprisesAcknowledgeNotificationSetCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesAcknowledgeNotificationSetCall) Do ¶
func (c *EnterprisesAcknowledgeNotificationSetCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.enterprises.acknowledgeNotificationSet" call.

func (*EnterprisesAcknowledgeNotificationSetCall) Fields ¶
func (c *EnterprisesAcknowledgeNotificationSetCall) Fields(s ...googleapi.Field) *EnterprisesAcknowledgeNotificationSetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesAcknowledgeNotificationSetCall) Header ¶
func (c *EnterprisesAcknowledgeNotificationSetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesAcknowledgeNotificationSetCall) NotificationSetId ¶
func (c *EnterprisesAcknowledgeNotificationSetCall) NotificationSetId(notificationSetId string) *EnterprisesAcknowledgeNotificationSetCall

NotificationSetId sets the optional parameter "notificationSetId": The notification set ID as returned by Enterprises.PullNotificationSet. This must be provided.

type EnterprisesCompleteSignupCall ¶
type EnterprisesCompleteSignupCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesCompleteSignupCall) CompletionToken ¶
func (c *EnterprisesCompleteSignupCall) CompletionToken(completionToken string) *EnterprisesCompleteSignupCall

CompletionToken sets the optional parameter "completionToken": The Completion token initially returned by GenerateSignupUrl.

func (*EnterprisesCompleteSignupCall) Context ¶
func (c *EnterprisesCompleteSignupCall) Context(ctx context.Context) *EnterprisesCompleteSignupCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesCompleteSignupCall) Do ¶
func (c *EnterprisesCompleteSignupCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)

Do executes the "androidenterprise.enterprises.completeSignup" call. Any non-2xx status code is an error. Response headers are in either *Enterprise.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesCompleteSignupCall) EnterpriseToken ¶
func (c *EnterprisesCompleteSignupCall) EnterpriseToken(enterpriseToken string) *EnterprisesCompleteSignupCall

EnterpriseToken sets the optional parameter "enterpriseToken": The Enterprise token appended to the Callback URL.

func (*EnterprisesCompleteSignupCall) Fields ¶
func (c *EnterprisesCompleteSignupCall) Fields(s ...googleapi.Field) *EnterprisesCompleteSignupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesCompleteSignupCall) Header ¶
func (c *EnterprisesCompleteSignupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesCreateWebTokenCall ¶
type EnterprisesCreateWebTokenCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesCreateWebTokenCall) Context ¶
func (c *EnterprisesCreateWebTokenCall) Context(ctx context.Context) *EnterprisesCreateWebTokenCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesCreateWebTokenCall) Do ¶
func (c *EnterprisesCreateWebTokenCall) Do(opts ...googleapi.CallOption) (*AdministratorWebToken, error)

Do executes the "androidenterprise.enterprises.createWebToken" call. Any non-2xx status code is an error. Response headers are in either *AdministratorWebToken.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesCreateWebTokenCall) Fields ¶
func (c *EnterprisesCreateWebTokenCall) Fields(s ...googleapi.Field) *EnterprisesCreateWebTokenCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesCreateWebTokenCall) Header ¶
func (c *EnterprisesCreateWebTokenCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesEnrollCall ¶
type EnterprisesEnrollCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesEnrollCall) Context ¶
func (c *EnterprisesEnrollCall) Context(ctx context.Context) *EnterprisesEnrollCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesEnrollCall) Do ¶
func (c *EnterprisesEnrollCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)

Do executes the "androidenterprise.enterprises.enroll" call. Any non-2xx status code is an error. Response headers are in either *Enterprise.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesEnrollCall) Fields ¶
func (c *EnterprisesEnrollCall) Fields(s ...googleapi.Field) *EnterprisesEnrollCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesEnrollCall) Header ¶
func (c *EnterprisesEnrollCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesGenerateEnterpriseUpgradeUrlCall ¶
added in v0.224.0
type EnterprisesGenerateEnterpriseUpgradeUrlCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) AdminEmail ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) AdminEmail(adminEmail string) *EnterprisesGenerateEnterpriseUpgradeUrlCall

AdminEmail sets the optional parameter "adminEmail": Email address used to prefill the admin field of the enterprise signup form as part of the upgrade process. This value is a hint only and can be altered by the user. Personal email addresses are not allowed. If `allowedDomains` is non-empty then this must belong to one of the `allowedDomains`.

func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) AllowedDomains ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) AllowedDomains(allowedDomains ...string) *EnterprisesGenerateEnterpriseUpgradeUrlCall

AllowedDomains sets the optional parameter "allowedDomains": A list of domains that are permitted for the admin email. The IT admin cannot enter an email address with a domain name that is not in this list. Subdomains of domains in this list are not allowed but can be allowed by adding a second entry which has `*.` prefixed to the domain name (e.g. *.example.com). If the field is not present or is an empty list then the IT admin is free to use any valid domain name. Personal email domains are not allowed.

func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) Context ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Context(ctx context.Context) *EnterprisesGenerateEnterpriseUpgradeUrlCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) Do ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Do(opts ...googleapi.CallOption) (*GenerateEnterpriseUpgradeUrlResponse, error)

Do executes the "androidenterprise.enterprises.generateEnterpriseUpgradeUrl" call. Any non-2xx status code is an error. Response headers are in either *GenerateEnterpriseUpgradeUrlResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) Fields ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Fields(s ...googleapi.Field) *EnterprisesGenerateEnterpriseUpgradeUrlCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesGenerateEnterpriseUpgradeUrlCall) Header ¶
added in v0.224.0
func (c *EnterprisesGenerateEnterpriseUpgradeUrlCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesGenerateSignupUrlCall ¶
type EnterprisesGenerateSignupUrlCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesGenerateSignupUrlCall) AdminEmail ¶
added in v0.188.0
func (c *EnterprisesGenerateSignupUrlCall) AdminEmail(adminEmail string) *EnterprisesGenerateSignupUrlCall

AdminEmail sets the optional parameter "adminEmail": Email address used to prefill the admin field of the enterprise signup form. This value is a hint only and can be altered by the user. If `allowedDomains` is non-empty then this must belong to one of the `allowedDomains`.

func (*EnterprisesGenerateSignupUrlCall) AllowedDomains ¶
added in v0.217.0
func (c *EnterprisesGenerateSignupUrlCall) AllowedDomains(allowedDomains ...string) *EnterprisesGenerateSignupUrlCall

AllowedDomains sets the optional parameter "allowedDomains": A list of domains that are permitted for the admin email. The IT admin cannot enter an email address with a domain name that is not in this list. Subdomains of domains in this list are not allowed but can be allowed by adding a second entry which has `*.` prefixed to the domain name (e.g. *.example.com). If the field is not present or is an empty list then the IT admin is free to use any valid domain name. Personal email domains are always allowed, but will result in the creation of a managed Google Play Accounts enterprise.

func (*EnterprisesGenerateSignupUrlCall) CallbackUrl ¶
func (c *EnterprisesGenerateSignupUrlCall) CallbackUrl(callbackUrl string) *EnterprisesGenerateSignupUrlCall

CallbackUrl sets the optional parameter "callbackUrl": The callback URL to which the Admin will be redirected after successfully creating an enterprise. Before redirecting there the system will add a single query parameter to this URL named "enterpriseToken" which will contain an opaque token to be used for the CompleteSignup request. Beware that this means that the URL will be parsed, the parameter added and then a new URL formatted, i.e. there may be some minor formatting changes and, more importantly, the URL must be well-formed so that it can be parsed.

func (*EnterprisesGenerateSignupUrlCall) Context ¶
func (c *EnterprisesGenerateSignupUrlCall) Context(ctx context.Context) *EnterprisesGenerateSignupUrlCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesGenerateSignupUrlCall) Do ¶
func (c *EnterprisesGenerateSignupUrlCall) Do(opts ...googleapi.CallOption) (*SignupInfo, error)

Do executes the "androidenterprise.enterprises.generateSignupUrl" call. Any non-2xx status code is an error. Response headers are in either *SignupInfo.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesGenerateSignupUrlCall) Fields ¶
func (c *EnterprisesGenerateSignupUrlCall) Fields(s ...googleapi.Field) *EnterprisesGenerateSignupUrlCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesGenerateSignupUrlCall) Header ¶
func (c *EnterprisesGenerateSignupUrlCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesGetCall ¶
type EnterprisesGetCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesGetCall) Context ¶
func (c *EnterprisesGetCall) Context(ctx context.Context) *EnterprisesGetCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesGetCall) Do ¶
func (c *EnterprisesGetCall) Do(opts ...googleapi.CallOption) (*Enterprise, error)

Do executes the "androidenterprise.enterprises.get" call. Any non-2xx status code is an error. Response headers are in either *Enterprise.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesGetCall) Fields ¶
func (c *EnterprisesGetCall) Fields(s ...googleapi.Field) *EnterprisesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesGetCall) Header ¶
func (c *EnterprisesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesGetCall) IfNoneMatch ¶
func (c *EnterprisesGetCall) IfNoneMatch(entityTag string) *EnterprisesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EnterprisesGetServiceAccountCall ¶
type EnterprisesGetServiceAccountCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesGetServiceAccountCall) Context ¶
func (c *EnterprisesGetServiceAccountCall) Context(ctx context.Context) *EnterprisesGetServiceAccountCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesGetServiceAccountCall) Do ¶
func (c *EnterprisesGetServiceAccountCall) Do(opts ...googleapi.CallOption) (*ServiceAccount, error)

Do executes the "androidenterprise.enterprises.getServiceAccount" call. Any non-2xx status code is an error. Response headers are in either *ServiceAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesGetServiceAccountCall) Fields ¶
func (c *EnterprisesGetServiceAccountCall) Fields(s ...googleapi.Field) *EnterprisesGetServiceAccountCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesGetServiceAccountCall) Header ¶
func (c *EnterprisesGetServiceAccountCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesGetServiceAccountCall) IfNoneMatch ¶
func (c *EnterprisesGetServiceAccountCall) IfNoneMatch(entityTag string) *EnterprisesGetServiceAccountCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*EnterprisesGetServiceAccountCall) KeyType ¶
func (c *EnterprisesGetServiceAccountCall) KeyType(keyType string) *EnterprisesGetServiceAccountCall

KeyType sets the optional parameter "keyType": The type of credential to return with the service account. Required.

Possible values:

"googleCredentials" - Google Credentials File format.
"pkcs12" - PKCS12 format. The password for the PKCS12 file is


'notasecret'. For more information, see https://tools.ietf.org/html/rfc7292. The data for keys of this type are base64 encoded according to RFC 4648 Section 4. See http://tools.ietf.org/html/rfc4648#section-4.

type EnterprisesGetStoreLayoutCall ¶
type EnterprisesGetStoreLayoutCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesGetStoreLayoutCall) Context ¶
func (c *EnterprisesGetStoreLayoutCall) Context(ctx context.Context) *EnterprisesGetStoreLayoutCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesGetStoreLayoutCall) Do ¶
func (c *EnterprisesGetStoreLayoutCall) Do(opts ...googleapi.CallOption) (*StoreLayout, error)

Do executes the "androidenterprise.enterprises.getStoreLayout" call. Any non-2xx status code is an error. Response headers are in either *StoreLayout.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesGetStoreLayoutCall) Fields ¶
func (c *EnterprisesGetStoreLayoutCall) Fields(s ...googleapi.Field) *EnterprisesGetStoreLayoutCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesGetStoreLayoutCall) Header ¶
func (c *EnterprisesGetStoreLayoutCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesGetStoreLayoutCall) IfNoneMatch ¶
func (c *EnterprisesGetStoreLayoutCall) IfNoneMatch(entityTag string) *EnterprisesGetStoreLayoutCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EnterprisesListCall ¶
type EnterprisesListCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesListCall) Context ¶
func (c *EnterprisesListCall) Context(ctx context.Context) *EnterprisesListCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesListCall) Do ¶
func (c *EnterprisesListCall) Do(opts ...googleapi.CallOption) (*EnterprisesListResponse, error)

Do executes the "androidenterprise.enterprises.list" call. Any non-2xx status code is an error. Response headers are in either *EnterprisesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesListCall) Fields ¶
func (c *EnterprisesListCall) Fields(s ...googleapi.Field) *EnterprisesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesListCall) Header ¶
func (c *EnterprisesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesListCall) IfNoneMatch ¶
func (c *EnterprisesListCall) IfNoneMatch(entityTag string) *EnterprisesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EnterprisesListResponse ¶
type EnterprisesListResponse struct {
	// Enterprise: An enterprise.
	Enterprise []*Enterprise `json:"enterprise,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Enterprise") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Enterprise") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (EnterprisesListResponse) MarshalJSON ¶
func (s EnterprisesListResponse) MarshalJSON() ([]byte, error)
type EnterprisesPullNotificationSetCall ¶
type EnterprisesPullNotificationSetCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesPullNotificationSetCall) Context ¶
func (c *EnterprisesPullNotificationSetCall) Context(ctx context.Context) *EnterprisesPullNotificationSetCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesPullNotificationSetCall) Do ¶
func (c *EnterprisesPullNotificationSetCall) Do(opts ...googleapi.CallOption) (*NotificationSet, error)

Do executes the "androidenterprise.enterprises.pullNotificationSet" call. Any non-2xx status code is an error. Response headers are in either *NotificationSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesPullNotificationSetCall) Fields ¶
func (c *EnterprisesPullNotificationSetCall) Fields(s ...googleapi.Field) *EnterprisesPullNotificationSetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesPullNotificationSetCall) Header ¶
func (c *EnterprisesPullNotificationSetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EnterprisesPullNotificationSetCall) RequestMode ¶
func (c *EnterprisesPullNotificationSetCall) RequestMode(requestMode string) *EnterprisesPullNotificationSetCall

RequestMode sets the optional parameter "requestMode": The request mode for pulling notifications. Specifying waitForNotifications will cause the request to block and wait until one or more notifications are present, or return an empty notification list if no notifications are present after some time. Specifying returnImmediately will cause the request to immediately return the pending notifications, or an empty list if no notifications are present. If omitted, defaults to waitForNotifications.

Possible values:

"waitForNotifications" - Wait until one or more notifications are present.
"returnImmediately" - Returns immediately whether notifications are


present or not.

type EnterprisesSendTestPushNotificationCall ¶
type EnterprisesSendTestPushNotificationCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesSendTestPushNotificationCall) Context ¶
func (c *EnterprisesSendTestPushNotificationCall) Context(ctx context.Context) *EnterprisesSendTestPushNotificationCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesSendTestPushNotificationCall) Do ¶
func (c *EnterprisesSendTestPushNotificationCall) Do(opts ...googleapi.CallOption) (*EnterprisesSendTestPushNotificationResponse, error)

Do executes the "androidenterprise.enterprises.sendTestPushNotification" call. Any non-2xx status code is an error. Response headers are in either *EnterprisesSendTestPushNotificationResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesSendTestPushNotificationCall) Fields ¶
func (c *EnterprisesSendTestPushNotificationCall) Fields(s ...googleapi.Field) *EnterprisesSendTestPushNotificationCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesSendTestPushNotificationCall) Header ¶
func (c *EnterprisesSendTestPushNotificationCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesSendTestPushNotificationResponse ¶
type EnterprisesSendTestPushNotificationResponse struct {
	// MessageId: The message ID of the test push notification that was sent.
	MessageId string `json:"messageId,omitempty"`
	// TopicName: The name of the Cloud Pub/Sub topic to which notifications for
	// this enterprise's enrolled account will be sent.
	TopicName string `json:"topicName,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "MessageId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MessageId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (EnterprisesSendTestPushNotificationResponse) MarshalJSON ¶
func (s EnterprisesSendTestPushNotificationResponse) MarshalJSON() ([]byte, error)
type EnterprisesService ¶
type EnterprisesService struct {
	// contains filtered or unexported fields
}
func NewEnterprisesService ¶
func NewEnterprisesService(s *Service) *EnterprisesService
func (*EnterprisesService) AcknowledgeNotificationSet ¶
func (r *EnterprisesService) AcknowledgeNotificationSet() *EnterprisesAcknowledgeNotificationSetCall

AcknowledgeNotificationSet: Acknowledges notifications that were received from Enterprises.PullNotificationSet to prevent subsequent calls from returning the same notifications.

func (*EnterprisesService) CompleteSignup ¶
func (r *EnterprisesService) CompleteSignup() *EnterprisesCompleteSignupCall

CompleteSignup: Completes the signup flow, by specifying the Completion token and Enterprise token. This request must not be called multiple times for a given Enterprise Token.

func (*EnterprisesService) CreateWebToken ¶
func (r *EnterprisesService) CreateWebToken(enterpriseId string, administratorwebtokenspec *AdministratorWebTokenSpec) *EnterprisesCreateWebTokenCall

CreateWebToken: Returns a unique token to access an embeddable UI. To generate a web UI, pass the generated token into the managed Google Play javascript API. Each token may only be used to start one UI session. See the JavaScript API documentation for further information.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) Enroll ¶
func (r *EnterprisesService) Enroll(token string, enterprise *Enterprise) *EnterprisesEnrollCall

Enroll: Enrolls an enterprise with the calling EMM.

- token: The token provided by the enterprise to register the EMM.

func (*EnterprisesService) GenerateEnterpriseUpgradeUrl ¶
added in v0.224.0
func (r *EnterprisesService) GenerateEnterpriseUpgradeUrl(enterpriseId string) *EnterprisesGenerateEnterpriseUpgradeUrlCall

GenerateEnterpriseUpgradeUrl: Generates an enterprise upgrade URL to upgrade an existing managed Google Play Accounts enterprise to a managed Google domain. See the guide to upgrading an enterprise for more details.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) GenerateSignupUrl ¶
func (r *EnterprisesService) GenerateSignupUrl() *EnterprisesGenerateSignupUrlCall

GenerateSignupUrl: Generates a sign-up URL.

func (*EnterprisesService) Get ¶
func (r *EnterprisesService) Get(enterpriseId string) *EnterprisesGetCall

Get: Retrieves the name and domain of an enterprise.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) GetServiceAccount ¶
func (r *EnterprisesService) GetServiceAccount(enterpriseId string) *EnterprisesGetServiceAccountCall

GetServiceAccount: Returns a service account and credentials. The service account can be bound to the enterprise by calling setAccount. The service account is unique to this enterprise and EMM, and will be deleted if the enterprise is unbound. The credentials contain private key data and are not stored server-side. This method can only be called after calling Enterprises.Enroll or Enterprises.CompleteSignup, and before Enterprises.SetAccount; at other times it will return an error. Subsequent calls after the first will generate a new, unique set of credentials, and invalidate the previously generated credentials. Once the service account is bound to the enterprise, it can be managed using the serviceAccountKeys resource. *Note:* After you create a key, you might need to wait for 60 seconds or more before you perform another operation with the key. If you try to perform an operation with the key immediately after you create the key, and you receive an error, you can retry the request with exponential backoff .

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) GetStoreLayout ¶
func (r *EnterprisesService) GetStoreLayout(enterpriseId string) *EnterprisesGetStoreLayoutCall

GetStoreLayout: Returns the store layout for the enterprise. If the store layout has not been set, returns "basic" as the store layout type and no homepage.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) List ¶
func (r *EnterprisesService) List(domain string) *EnterprisesListCall

List: Looks up an enterprise by domain name. This is only supported for enterprises created via the Google-initiated creation flow. Lookup of the id is not needed for enterprises created via the EMM-initiated flow since the EMM learns the enterprise ID in the callback specified in the Enterprises.generateSignupUrl call.

- domain: The exact primary domain name of the enterprise to look up.

func (*EnterprisesService) PullNotificationSet ¶
func (r *EnterprisesService) PullNotificationSet() *EnterprisesPullNotificationSetCall

PullNotificationSet: Pulls and returns a notification set for the enterprises associated with the service account authenticated for the request. The notification set may be empty if no notification are pending. A notification set returned needs to be acknowledged within 20 seconds by calling Enterprises.AcknowledgeNotificationSet, unless the notification set is empty. Notifications that are not acknowledged within the 20 seconds will eventually be included again in the response to another PullNotificationSet request, and those that are never acknowledged will ultimately be deleted according to the Google Cloud Platform Pub/Sub system policy. Multiple requests might be performed concurrently to retrieve notifications, in which case the pending notifications (if any) will be split among each caller, if any are pending. If no notifications are present, an empty notification list is returned. Subsequent requests may return more notifications once they become available.

func (*EnterprisesService) SendTestPushNotification ¶
func (r *EnterprisesService) SendTestPushNotification(enterpriseId string) *EnterprisesSendTestPushNotificationCall

SendTestPushNotification: Sends a test notification to validate the EMM integration with the Google Cloud Pub/Sub service for this enterprise.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) SetAccount ¶
func (r *EnterprisesService) SetAccount(enterpriseId string, enterpriseaccount *EnterpriseAccount) *EnterprisesSetAccountCall

SetAccount: Sets the account that will be used to authenticate to the API as the enterprise.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) SetStoreLayout ¶
func (r *EnterprisesService) SetStoreLayout(enterpriseId string, storelayout *StoreLayout) *EnterprisesSetStoreLayoutCall

SetStoreLayout: Sets the store layout for the enterprise. By default, storeLayoutType is set to "basic" and the basic store layout is enabled. The basic layout only contains apps approved by the admin, and that have been added to the available product set for a user (using the setAvailableProductSet call). Apps on the page are sorted in order of their product ID value. If you create a custom store layout (by setting storeLayoutType = "custom" and setting a homepage), the basic store layout is disabled.

- enterpriseId: The ID of the enterprise.

func (*EnterprisesService) Unenroll ¶
func (r *EnterprisesService) Unenroll(enterpriseId string) *EnterprisesUnenrollCall

Unenroll: Unenrolls an enterprise from the calling EMM.

- enterpriseId: The ID of the enterprise.

type EnterprisesSetAccountCall ¶
type EnterprisesSetAccountCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesSetAccountCall) Context ¶
func (c *EnterprisesSetAccountCall) Context(ctx context.Context) *EnterprisesSetAccountCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesSetAccountCall) Do ¶
func (c *EnterprisesSetAccountCall) Do(opts ...googleapi.CallOption) (*EnterpriseAccount, error)

Do executes the "androidenterprise.enterprises.setAccount" call. Any non-2xx status code is an error. Response headers are in either *EnterpriseAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesSetAccountCall) Fields ¶
func (c *EnterprisesSetAccountCall) Fields(s ...googleapi.Field) *EnterprisesSetAccountCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesSetAccountCall) Header ¶
func (c *EnterprisesSetAccountCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesSetStoreLayoutCall ¶
type EnterprisesSetStoreLayoutCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesSetStoreLayoutCall) Context ¶
func (c *EnterprisesSetStoreLayoutCall) Context(ctx context.Context) *EnterprisesSetStoreLayoutCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesSetStoreLayoutCall) Do ¶
func (c *EnterprisesSetStoreLayoutCall) Do(opts ...googleapi.CallOption) (*StoreLayout, error)

Do executes the "androidenterprise.enterprises.setStoreLayout" call. Any non-2xx status code is an error. Response headers are in either *StoreLayout.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EnterprisesSetStoreLayoutCall) Fields ¶
func (c *EnterprisesSetStoreLayoutCall) Fields(s ...googleapi.Field) *EnterprisesSetStoreLayoutCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesSetStoreLayoutCall) Header ¶
func (c *EnterprisesSetStoreLayoutCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EnterprisesUnenrollCall ¶
type EnterprisesUnenrollCall struct {
	// contains filtered or unexported fields
}
func (*EnterprisesUnenrollCall) Context ¶
func (c *EnterprisesUnenrollCall) Context(ctx context.Context) *EnterprisesUnenrollCall

Context sets the context to be used in this call's Do method.

func (*EnterprisesUnenrollCall) Do ¶
func (c *EnterprisesUnenrollCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.enterprises.unenroll" call.

func (*EnterprisesUnenrollCall) Fields ¶
func (c *EnterprisesUnenrollCall) Fields(s ...googleapi.Field) *EnterprisesUnenrollCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EnterprisesUnenrollCall) Header ¶
func (c *EnterprisesUnenrollCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type Entitlement ¶
type Entitlement struct {
	// ProductId: The ID of the product that the entitlement is for. For example,
	// "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`
	// Reason: The reason for the entitlement. For example, "free" for free apps.
	// This property is temporary: it will be replaced by the acquisition kind
	// field of group licenses.
	//
	// Possible values:
	//   "free"
	//   "groupLicense"
	//   "userPurchase"
	Reason string `json:"reason,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ProductId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Entitlement: *Deprecated:* New integrations cannot use this method and can refer to our new recommendations.

func (Entitlement) MarshalJSON ¶
func (s Entitlement) MarshalJSON() ([]byte, error)
type EntitlementsDeleteCall ¶
type EntitlementsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*EntitlementsDeleteCall) Context ¶
func (c *EntitlementsDeleteCall) Context(ctx context.Context) *EntitlementsDeleteCall

Context sets the context to be used in this call's Do method.

func (*EntitlementsDeleteCall) Do ¶
func (c *EntitlementsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.entitlements.delete" call.

func (*EntitlementsDeleteCall) Fields ¶
func (c *EntitlementsDeleteCall) Fields(s ...googleapi.Field) *EntitlementsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EntitlementsDeleteCall) Header ¶
func (c *EntitlementsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EntitlementsGetCall ¶
type EntitlementsGetCall struct {
	// contains filtered or unexported fields
}
func (*EntitlementsGetCall) Context ¶
func (c *EntitlementsGetCall) Context(ctx context.Context) *EntitlementsGetCall

Context sets the context to be used in this call's Do method.

func (*EntitlementsGetCall) Do ¶
func (c *EntitlementsGetCall) Do(opts ...googleapi.CallOption) (*Entitlement, error)

Do executes the "androidenterprise.entitlements.get" call. Any non-2xx status code is an error. Response headers are in either *Entitlement.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EntitlementsGetCall) Fields ¶
func (c *EntitlementsGetCall) Fields(s ...googleapi.Field) *EntitlementsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EntitlementsGetCall) Header ¶
func (c *EntitlementsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EntitlementsGetCall) IfNoneMatch ¶
func (c *EntitlementsGetCall) IfNoneMatch(entityTag string) *EntitlementsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EntitlementsListCall ¶
type EntitlementsListCall struct {
	// contains filtered or unexported fields
}
func (*EntitlementsListCall) Context ¶
func (c *EntitlementsListCall) Context(ctx context.Context) *EntitlementsListCall

Context sets the context to be used in this call's Do method.

func (*EntitlementsListCall) Do ¶
func (c *EntitlementsListCall) Do(opts ...googleapi.CallOption) (*EntitlementsListResponse, error)

Do executes the "androidenterprise.entitlements.list" call. Any non-2xx status code is an error. Response headers are in either *EntitlementsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EntitlementsListCall) Fields ¶
func (c *EntitlementsListCall) Fields(s ...googleapi.Field) *EntitlementsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EntitlementsListCall) Header ¶
func (c *EntitlementsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EntitlementsListCall) IfNoneMatch ¶
func (c *EntitlementsListCall) IfNoneMatch(entityTag string) *EntitlementsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EntitlementsListResponse ¶
type EntitlementsListResponse struct {
	// Entitlement: An entitlement of a user to a product (e.g. an app). For
	// example, a free app that they have installed, or a paid app that they have
	// been allocated a license to.
	Entitlement []*Entitlement `json:"entitlement,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Entitlement") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Entitlement") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (EntitlementsListResponse) MarshalJSON ¶
func (s EntitlementsListResponse) MarshalJSON() ([]byte, error)
type EntitlementsService ¶
type EntitlementsService struct {
	// contains filtered or unexported fields
}
func NewEntitlementsService ¶
func NewEntitlementsService(s *Service) *EntitlementsService
func (*EntitlementsService) Delete ¶
func (r *EntitlementsService) Delete(enterpriseId string, userId string, entitlementId string) *EntitlementsDeleteCall

Delete: Removes an entitlement to an app for a user. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

enterpriseId: The ID of the enterprise.
entitlementId: The ID of the entitlement (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*EntitlementsService) Get ¶
func (r *EntitlementsService) Get(enterpriseId string, userId string, entitlementId string) *EntitlementsGetCall

Get: Retrieves details of an entitlement. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

enterpriseId: The ID of the enterprise.
entitlementId: The ID of the entitlement (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*EntitlementsService) List ¶
func (r *EntitlementsService) List(enterpriseId string, userId string) *EntitlementsListCall

List: Lists all entitlements for the specified user. Only the ID is set. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*EntitlementsService) Update ¶
func (r *EntitlementsService) Update(enterpriseId string, userId string, entitlementId string, entitlement *Entitlement) *EntitlementsUpdateCall

Update: Adds or updates an entitlement to an app for a user. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

enterpriseId: The ID of the enterprise.
entitlementId: The ID of the entitlement (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
type EntitlementsUpdateCall ¶
type EntitlementsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EntitlementsUpdateCall) Context ¶
func (c *EntitlementsUpdateCall) Context(ctx context.Context) *EntitlementsUpdateCall

Context sets the context to be used in this call's Do method.

func (*EntitlementsUpdateCall) Do ¶
func (c *EntitlementsUpdateCall) Do(opts ...googleapi.CallOption) (*Entitlement, error)

Do executes the "androidenterprise.entitlements.update" call. Any non-2xx status code is an error. Response headers are in either *Entitlement.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EntitlementsUpdateCall) Fields ¶
func (c *EntitlementsUpdateCall) Fields(s ...googleapi.Field) *EntitlementsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EntitlementsUpdateCall) Header ¶
func (c *EntitlementsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EntitlementsUpdateCall) Install ¶
func (c *EntitlementsUpdateCall) Install(install bool) *EntitlementsUpdateCall

Install sets the optional parameter "install": Set to true to also install the product on all the user's devices where possible. Failure to install on one or more devices will not prevent this operation from returning successfully, as long as the entitlement was successfully assigned to the user.

type GenerateEnterpriseUpgradeUrlResponse ¶
added in v0.224.0
type GenerateEnterpriseUpgradeUrlResponse struct {
	// Url: A URL for an enterprise admin to upgrade their enterprise. The page
	// can't be rendered in an iframe.
	Url string `json:"url,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Url") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Url") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GenerateEnterpriseUpgradeUrlResponse: Response message for generating a URL to upgrade an existing managed Google Play Accounts enterprise to a managed Google domain.

func (GenerateEnterpriseUpgradeUrlResponse) MarshalJSON ¶
added in v0.224.0
func (s GenerateEnterpriseUpgradeUrlResponse) MarshalJSON() ([]byte, error)
type GoogleAuthenticationSettings ¶
added in v0.108.0
type GoogleAuthenticationSettings struct {
	// DedicatedDevicesAllowed: Whether dedicated devices are allowed.
	//
	// Possible values:
	//   "dedicatedDevicesAllowedUnspecified" - This value is unused.
	//   "disallowed" - Dedicated devices are not allowed.
	//   "allowed" - Dedicated devices are allowed.
	DedicatedDevicesAllowed string `json:"dedicatedDevicesAllowed,omitempty"`
	// GoogleAuthenticationRequired: Whether Google authentication is required.
	//
	// Possible values:
	//   "googleAuthenticationRequiredUnspecified" - This value is unused.
	//   "notRequired" - Google authentication is not required.
	//   "required" - User is required to be successfully authenticated by Google.
	GoogleAuthenticationRequired string `json:"googleAuthenticationRequired,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DedicatedDevicesAllowed") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DedicatedDevicesAllowed") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAuthenticationSettings: Contains settings for Google-provided user authentication.

func (GoogleAuthenticationSettings) MarshalJSON ¶
added in v0.108.0
func (s GoogleAuthenticationSettings) MarshalJSON() ([]byte, error)
type GroupLicense ¶
type GroupLicense struct {
	// AcquisitionKind: How this group license was acquired. "bulkPurchase" means
	// that this Grouplicenses resource was created because the enterprise
	// purchased licenses for this product; otherwise, the value is "free" (for
	// free products).
	//
	// Possible values:
	//   "free"
	//   "bulkPurchase"
	AcquisitionKind string `json:"acquisitionKind,omitempty"`
	// Approval: Whether the product to which this group license relates is
	// currently approved by the enterprise. Products are approved when a group
	// license is first created, but this approval may be revoked by an enterprise
	// admin via Google Play. Unapproved products will not be visible to end users
	// in collections, and new entitlements to them should not normally be created.
	//
	// Possible values:
	//   "approved"
	//   "unapproved"
	Approval string `json:"approval,omitempty"`
	// NumProvisioned: The total number of provisioned licenses for this product.
	// Returned by read operations, but ignored in write operations.
	NumProvisioned int64 `json:"numProvisioned,omitempty"`
	// NumPurchased: The number of purchased licenses (possibly in multiple
	// purchases). If this field is omitted, then there is no limit on the number
	// of licenses that can be provisioned (for example, if the acquisition kind is
	// "free").
	NumPurchased int64 `json:"numPurchased,omitempty"`
	// Permissions: The permission approval status of the product. This field is
	// only set if the product is approved. Possible states are: -
	// "currentApproved", the current set of permissions is approved, but
	// additional permissions will require the administrator to reapprove the
	// product (If the product was approved without specifying the approved
	// permissions setting, then this is the default behavior.), -
	// "needsReapproval", the product has unapproved permissions. No additional
	// product licenses can be assigned until the product is reapproved, -
	// "allCurrentAndFutureApproved", the current permissions are approved and any
	// future permission updates will be automatically approved without
	// administrator review.
	//
	// Possible values:
	//   "currentApproved"
	//   "needsReapproval"
	//   "allCurrentAndFutureApproved"
	Permissions string `json:"permissions,omitempty"`
	// ProductId: The ID of the product that the license is for. For example,
	// "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AcquisitionKind") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcquisitionKind") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GroupLicense: *Deprecated:* New integrations cannot use this method and can refer to our new recommendations

func (GroupLicense) MarshalJSON ¶
func (s GroupLicense) MarshalJSON() ([]byte, error)
type GroupLicenseUsersListResponse ¶
type GroupLicenseUsersListResponse struct {
	// User: A user of an enterprise.
	User []*User `json:"user,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "User") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "User") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GroupLicenseUsersListResponse) MarshalJSON ¶
func (s GroupLicenseUsersListResponse) MarshalJSON() ([]byte, error)
type GroupLicensesListResponse ¶
type GroupLicensesListResponse struct {
	// GroupLicense: A group license for a product approved for use in the
	// enterprise.
	GroupLicense []*GroupLicense `json:"groupLicense,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GroupLicense") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GroupLicense") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GroupLicensesListResponse) MarshalJSON ¶
func (s GroupLicensesListResponse) MarshalJSON() ([]byte, error)
type GrouplicensesGetCall ¶
type GrouplicensesGetCall struct {
	// contains filtered or unexported fields
}
func (*GrouplicensesGetCall) Context ¶
func (c *GrouplicensesGetCall) Context(ctx context.Context) *GrouplicensesGetCall

Context sets the context to be used in this call's Do method.

func (*GrouplicensesGetCall) Do ¶
func (c *GrouplicensesGetCall) Do(opts ...googleapi.CallOption) (*GroupLicense, error)

Do executes the "androidenterprise.grouplicenses.get" call. Any non-2xx status code is an error. Response headers are in either *GroupLicense.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GrouplicensesGetCall) Fields ¶
func (c *GrouplicensesGetCall) Fields(s ...googleapi.Field) *GrouplicensesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrouplicensesGetCall) Header ¶
func (c *GrouplicensesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GrouplicensesGetCall) IfNoneMatch ¶
func (c *GrouplicensesGetCall) IfNoneMatch(entityTag string) *GrouplicensesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GrouplicensesListCall ¶
type GrouplicensesListCall struct {
	// contains filtered or unexported fields
}
func (*GrouplicensesListCall) Context ¶
func (c *GrouplicensesListCall) Context(ctx context.Context) *GrouplicensesListCall

Context sets the context to be used in this call's Do method.

func (*GrouplicensesListCall) Do ¶
func (c *GrouplicensesListCall) Do(opts ...googleapi.CallOption) (*GroupLicensesListResponse, error)

Do executes the "androidenterprise.grouplicenses.list" call. Any non-2xx status code is an error. Response headers are in either *GroupLicensesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GrouplicensesListCall) Fields ¶
func (c *GrouplicensesListCall) Fields(s ...googleapi.Field) *GrouplicensesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrouplicensesListCall) Header ¶
func (c *GrouplicensesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GrouplicensesListCall) IfNoneMatch ¶
func (c *GrouplicensesListCall) IfNoneMatch(entityTag string) *GrouplicensesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GrouplicensesService ¶
type GrouplicensesService struct {
	// contains filtered or unexported fields
}
func NewGrouplicensesService ¶
func NewGrouplicensesService(s *Service) *GrouplicensesService
func (*GrouplicensesService) Get ¶
func (r *GrouplicensesService) Get(enterpriseId string, groupLicenseId string) *GrouplicensesGetCall

Get: Retrieves details of an enterprise's group license for a product. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

enterpriseId: The ID of the enterprise.
groupLicenseId: The ID of the product the group license is for, e.g. "app:com.google.android.gm".
func (*GrouplicensesService) List ¶
func (r *GrouplicensesService) List(enterpriseId string) *GrouplicensesListCall

List: Retrieves IDs of all products for which the enterprise has a group license. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise.

type GrouplicenseusersListCall ¶
type GrouplicenseusersListCall struct {
	// contains filtered or unexported fields
}
func (*GrouplicenseusersListCall) Context ¶
func (c *GrouplicenseusersListCall) Context(ctx context.Context) *GrouplicenseusersListCall

Context sets the context to be used in this call's Do method.

func (*GrouplicenseusersListCall) Do ¶
func (c *GrouplicenseusersListCall) Do(opts ...googleapi.CallOption) (*GroupLicenseUsersListResponse, error)

Do executes the "androidenterprise.grouplicenseusers.list" call. Any non-2xx status code is an error. Response headers are in either *GroupLicenseUsersListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GrouplicenseusersListCall) Fields ¶
func (c *GrouplicenseusersListCall) Fields(s ...googleapi.Field) *GrouplicenseusersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrouplicenseusersListCall) Header ¶
func (c *GrouplicenseusersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GrouplicenseusersListCall) IfNoneMatch ¶
func (c *GrouplicenseusersListCall) IfNoneMatch(entityTag string) *GrouplicenseusersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GrouplicenseusersService ¶
type GrouplicenseusersService struct {
	// contains filtered or unexported fields
}
func NewGrouplicenseusersService ¶
func NewGrouplicenseusersService(s *Service) *GrouplicenseusersService
func (*GrouplicenseusersService) List ¶
func (r *GrouplicenseusersService) List(enterpriseId string, groupLicenseId string) *GrouplicenseusersListCall

List: Retrieves the IDs of the users who have been granted entitlements under the license. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

enterpriseId: The ID of the enterprise.
groupLicenseId: The ID of the product the group license is for, e.g. "app:com.google.android.gm".
type Install ¶
type Install struct {
	// InstallState: Install state. The state "installPending" means that an
	// install request has recently been made and download to the device is in
	// progress. The state "installed" means that the app has been installed. This
	// field is read-only.
	//
	// Possible values:
	//   "installed"
	//   "installPending"
	InstallState string `json:"installState,omitempty"`
	// ProductId: The ID of the product that the install is for. For example,
	// "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`
	// VersionCode: The version of the installed product. Guaranteed to be set only
	// if the install state is "installed".
	VersionCode int64 `json:"versionCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "InstallState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstallState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Install: The existence of an Installs resource indicates that an app is installed on a particular device (or that an install is pending). The API can be used to create an install resource using the update method. This triggers the actual install of the app on the device. If the user does not already have an entitlement for the app, then an attempt is made to create one. If this fails (for example, because the app is not free and there is no available license), then the creation of the install fails. The API can also be used to update an installed app. If the update method is used on an existing install, then the app will be updated to the latest available version. Note that it is not possible to force the installation of a specific version of an app: the version code is read-only. If a user installs an app themselves (as permitted by the enterprise), then again an install resource and possibly an entitlement resource are automatically created. The API can also be used to delete an install resource, which triggers the removal of the app from the device. Note that deleting an install does not automatically remove the corresponding entitlement, even if there are no remaining installs. The install resource will also be deleted if the user uninstalls the app themselves.

func (Install) MarshalJSON ¶
func (s Install) MarshalJSON() ([]byte, error)
type InstallFailureEvent ¶
type InstallFailureEvent struct {
	// DeviceId: The Android ID of the device. This field will always be present.
	DeviceId string `json:"deviceId,omitempty"`
	// FailureDetails: Additional details on the failure if applicable.
	FailureDetails string `json:"failureDetails,omitempty"`
	// FailureReason: The reason for the installation failure. This field will
	// always be present.
	//
	// Possible values:
	//   "unknown" - Used whenever no better reason for failure can be provided.
	//   "timeout" - Used when the installation timed out. This can cover a number
	// of situations, for example when the device did not have connectivity at any
	// point during the retry period, or if the device is OOM.
	FailureReason string `json:"failureReason,omitempty"`
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") for
	// which the install failure event occured. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// UserId: The ID of the user. This field will always be present.
	UserId string `json:"userId,omitempty"`
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

InstallFailureEvent: An event generated when an app installation failed on a device

func (InstallFailureEvent) MarshalJSON ¶
func (s InstallFailureEvent) MarshalJSON() ([]byte, error)
type InstallsDeleteCall ¶
type InstallsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*InstallsDeleteCall) Context ¶
func (c *InstallsDeleteCall) Context(ctx context.Context) *InstallsDeleteCall

Context sets the context to be used in this call's Do method.

func (*InstallsDeleteCall) Do ¶
func (c *InstallsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.installs.delete" call.

func (*InstallsDeleteCall) Fields ¶
func (c *InstallsDeleteCall) Fields(s ...googleapi.Field) *InstallsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InstallsDeleteCall) Header ¶
func (c *InstallsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type InstallsGetCall ¶
type InstallsGetCall struct {
	// contains filtered or unexported fields
}
func (*InstallsGetCall) Context ¶
func (c *InstallsGetCall) Context(ctx context.Context) *InstallsGetCall

Context sets the context to be used in this call's Do method.

func (*InstallsGetCall) Do ¶
func (c *InstallsGetCall) Do(opts ...googleapi.CallOption) (*Install, error)

Do executes the "androidenterprise.installs.get" call. Any non-2xx status code is an error. Response headers are in either *Install.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InstallsGetCall) Fields ¶
func (c *InstallsGetCall) Fields(s ...googleapi.Field) *InstallsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InstallsGetCall) Header ¶
func (c *InstallsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InstallsGetCall) IfNoneMatch ¶
func (c *InstallsGetCall) IfNoneMatch(entityTag string) *InstallsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type InstallsListCall ¶
type InstallsListCall struct {
	// contains filtered or unexported fields
}
func (*InstallsListCall) Context ¶
func (c *InstallsListCall) Context(ctx context.Context) *InstallsListCall

Context sets the context to be used in this call's Do method.

func (*InstallsListCall) Do ¶
func (c *InstallsListCall) Do(opts ...googleapi.CallOption) (*InstallsListResponse, error)

Do executes the "androidenterprise.installs.list" call. Any non-2xx status code is an error. Response headers are in either *InstallsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InstallsListCall) Fields ¶
func (c *InstallsListCall) Fields(s ...googleapi.Field) *InstallsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InstallsListCall) Header ¶
func (c *InstallsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InstallsListCall) IfNoneMatch ¶
func (c *InstallsListCall) IfNoneMatch(entityTag string) *InstallsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type InstallsListResponse ¶
type InstallsListResponse struct {
	// Install: An installation of an app for a user on a specific device. The
	// existence of an install implies that the user must have an entitlement to
	// the app.
	Install []*Install `json:"install,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Install") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Install") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (InstallsListResponse) MarshalJSON ¶
func (s InstallsListResponse) MarshalJSON() ([]byte, error)
type InstallsService ¶
type InstallsService struct {
	// contains filtered or unexported fields
}
func NewInstallsService ¶
func NewInstallsService(s *Service) *InstallsService
func (*InstallsService) Delete ¶
func (r *InstallsService) Delete(enterpriseId string, userId string, deviceId string, installId string) *InstallsDeleteCall

Delete: Requests to remove an app from a device. A call to get or list will still show the app as installed on the device until it is actually removed. A successful response indicates that a removal request has been sent to the device. The call will be considered successful even if the app is not present on the device (e.g. it was never installed, or was removed by the user).

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
installId: The ID of the product represented by the install, e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*InstallsService) Get ¶
func (r *InstallsService) Get(enterpriseId string, userId string, deviceId string, installId string) *InstallsGetCall

Get: Retrieves details of an installation of an app on a device.

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
installId: The ID of the product represented by the install, e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*InstallsService) List ¶
func (r *InstallsService) List(enterpriseId string, userId string, deviceId string) *InstallsListCall

List: Retrieves the details of all apps installed on the specified device.

- deviceId: The Android ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*InstallsService) Update ¶
func (r *InstallsService) Update(enterpriseId string, userId string, deviceId string, installId string, install *Install) *InstallsUpdateCall

Update: Requests to install the latest version of an app to a device. If the app is already installed, then it is updated to the latest version if necessary.

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
installId: The ID of the product represented by the install, e.g. "app:com.google.android.gm".
userId: The ID of the user.
type InstallsUpdateCall ¶
type InstallsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*InstallsUpdateCall) Context ¶
func (c *InstallsUpdateCall) Context(ctx context.Context) *InstallsUpdateCall

Context sets the context to be used in this call's Do method.

func (*InstallsUpdateCall) Do ¶
func (c *InstallsUpdateCall) Do(opts ...googleapi.CallOption) (*Install, error)

Do executes the "androidenterprise.installs.update" call. Any non-2xx status code is an error. Response headers are in either *Install.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InstallsUpdateCall) Fields ¶
func (c *InstallsUpdateCall) Fields(s ...googleapi.Field) *InstallsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InstallsUpdateCall) Header ¶
func (c *InstallsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type KeyedAppState ¶
added in v0.7.0
type KeyedAppState struct {
	// Data: Additional field intended for machine-readable data. For example, a
	// number or JSON object. To prevent XSS, we recommend removing any HTML from
	// the data before displaying it.
	Data string `json:"data,omitempty"`
	// Key: Key indicating what the app is providing a state for. The content of
	// the key is set by the app's developer. To prevent XSS, we recommend removing
	// any HTML from the key before displaying it. This field will always be
	// present.
	Key string `json:"key,omitempty"`
	// Message: Free-form, human-readable message describing the app state. For
	// example, an error message. To prevent XSS, we recommend removing any HTML
	// from the message before displaying it.
	Message string `json:"message,omitempty"`
	// Severity: Severity of the app state. This field will always be present.
	//
	// Possible values:
	//   "severityUnknown"
	//   "severityInfo"
	//   "severityError"
	Severity string `json:"severity,omitempty"`
	// StateTimestampMillis: Timestamp of when the app set the state in
	// milliseconds since epoch. This field will always be present.
	StateTimestampMillis int64 `json:"stateTimestampMillis,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "Data") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Data") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

KeyedAppState: Represents a keyed app state containing a key, timestamp, severity level, optional description, and optional data.

func (KeyedAppState) MarshalJSON ¶
added in v0.7.0
func (s KeyedAppState) MarshalJSON() ([]byte, error)
type LocalizedText ¶
type LocalizedText struct {
	// Locale: The BCP47 tag for a locale. (e.g. "en-US", "de").
	Locale string `json:"locale,omitempty"`
	// Text: The text localized in the associated locale.
	Text string `json:"text,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Locale") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Locale") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LocalizedText: A localized string with its locale.

func (LocalizedText) MarshalJSON ¶
func (s LocalizedText) MarshalJSON() ([]byte, error)
type MaintenanceWindow ¶
type MaintenanceWindow struct {
	// DurationMs: Duration of the maintenance window, in milliseconds. The
	// duration must be between 30 minutes and 24 hours (inclusive).
	DurationMs int64 `json:"durationMs,omitempty,string"`
	// StartTimeAfterMidnightMs: Start time of the maintenance window, in
	// milliseconds after midnight on the device. Windows can span midnight.
	StartTimeAfterMidnightMs int64 `json:"startTimeAfterMidnightMs,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "DurationMs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DurationMs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MaintenanceWindow: Maintenance window for managed Google Play Accounts. This allows Play store to update the apps on the foreground in the designated window.

func (MaintenanceWindow) MarshalJSON ¶
func (s MaintenanceWindow) MarshalJSON() ([]byte, error)
type ManagedConfiguration ¶
type ManagedConfiguration struct {
	// ConfigurationVariables: Contains the ID of the managed configuration profile
	// and the set of configuration variables (if any) defined for the user.
	ConfigurationVariables *ConfigurationVariables `json:"configurationVariables,omitempty"`
	// Kind: Deprecated.
	Kind string `json:"kind,omitempty"`
	// ManagedProperty: The set of managed properties for this configuration.
	ManagedProperty []*ManagedProperty `json:"managedProperty,omitempty"`
	// ProductId: The ID of the product that the managed configuration is for, e.g.
	// "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ConfigurationVariables") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConfigurationVariables") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagedConfiguration: *Deprecated:* New integrations cannot use this method and can refer to our new recommendations

func (ManagedConfiguration) MarshalJSON ¶
func (s ManagedConfiguration) MarshalJSON() ([]byte, error)
type ManagedConfigurationsForDeviceListResponse ¶
type ManagedConfigurationsForDeviceListResponse struct {
	// ManagedConfigurationForDevice: A managed configuration for an app on a
	// specific device.
	ManagedConfigurationForDevice []*ManagedConfiguration `json:"managedConfigurationForDevice,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "ManagedConfigurationForDevice") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagedConfigurationForDevice")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ManagedConfigurationsForDeviceListResponse) MarshalJSON ¶
func (s ManagedConfigurationsForDeviceListResponse) MarshalJSON() ([]byte, error)
type ManagedConfigurationsForUserListResponse ¶
type ManagedConfigurationsForUserListResponse struct {
	// ManagedConfigurationForUser: A managed configuration for an app for a
	// specific user.
	ManagedConfigurationForUser []*ManagedConfiguration `json:"managedConfigurationForUser,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "ManagedConfigurationForUser") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagedConfigurationForUser") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ManagedConfigurationsForUserListResponse) MarshalJSON ¶
func (s ManagedConfigurationsForUserListResponse) MarshalJSON() ([]byte, error)
type ManagedConfigurationsSettings ¶
type ManagedConfigurationsSettings struct {
	// LastUpdatedTimestampMillis: The last updated time of the managed
	// configuration settings in milliseconds since 1970-01-01T00:00:00Z.
	LastUpdatedTimestampMillis int64 `json:"lastUpdatedTimestampMillis,omitempty,string"`
	// McmId: The ID of the managed configurations settings.
	McmId string `json:"mcmId,omitempty"`
	// Name: The name of the managed configurations settings.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastUpdatedTimestampMillis")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastUpdatedTimestampMillis") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagedConfigurationsSettings: A managed configurations settings resource contains the set of managed properties that have been configured for an Android app to be applied to a set of users. The app's developer would have defined configurable properties in the managed configurations schema.

func (ManagedConfigurationsSettings) MarshalJSON ¶
func (s ManagedConfigurationsSettings) MarshalJSON() ([]byte, error)
type ManagedConfigurationsSettingsListResponse ¶
type ManagedConfigurationsSettingsListResponse struct {
	// ManagedConfigurationsSettings: A managed configurations settings for an app
	// that may be assigned to a group of users in an enterprise.
	ManagedConfigurationsSettings []*ManagedConfigurationsSettings `json:"managedConfigurationsSettings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "ManagedConfigurationsSettings") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagedConfigurationsSettings")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ManagedConfigurationsSettingsListResponse) MarshalJSON ¶
func (s ManagedConfigurationsSettingsListResponse) MarshalJSON() ([]byte, error)
type ManagedProperty ¶
type ManagedProperty struct {
	// Key: The unique key that identifies the property.
	Key string `json:"key,omitempty"`
	// ValueBool: The boolean value - this will only be present if type of the
	// property is bool.
	ValueBool bool `json:"valueBool,omitempty"`
	// ValueBundle: The bundle of managed properties - this will only be present if
	// type of the property is bundle.
	ValueBundle *ManagedPropertyBundle `json:"valueBundle,omitempty"`
	// ValueBundleArray: The list of bundles of properties - this will only be
	// present if type of the property is bundle_array.
	ValueBundleArray []*ManagedPropertyBundle `json:"valueBundleArray,omitempty"`
	// ValueInteger: The integer value - this will only be present if type of the
	// property is integer.
	ValueInteger int64 `json:"valueInteger,omitempty"`
	// ValueString: The string value - this will only be present if type of the
	// property is string, choice or hidden.
	ValueString string `json:"valueString,omitempty"`
	// ValueStringArray: The list of string values - this will only be present if
	// type of the property is multiselect.
	ValueStringArray []string `json:"valueStringArray,omitempty"`
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

ManagedProperty: A managed property of a managed configuration. The property must match one of the properties in the app restrictions schema of the product. Exactly one of the value fields must be populated, and it must match the property's type in the app restrictions schema.

func (ManagedProperty) MarshalJSON ¶
func (s ManagedProperty) MarshalJSON() ([]byte, error)
type ManagedPropertyBundle ¶
type ManagedPropertyBundle struct {
	// ManagedProperty: The list of managed properties.
	ManagedProperty []*ManagedProperty `json:"managedProperty,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ManagedProperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ManagedProperty") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagedPropertyBundle: A bundle of managed properties.

func (ManagedPropertyBundle) MarshalJSON ¶
func (s ManagedPropertyBundle) MarshalJSON() ([]byte, error)
type ManagedconfigurationsfordeviceDeleteCall ¶
type ManagedconfigurationsfordeviceDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsfordeviceDeleteCall) Context ¶
func (c *ManagedconfigurationsfordeviceDeleteCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsfordeviceDeleteCall) Do ¶
func (c *ManagedconfigurationsfordeviceDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.managedconfigurationsfordevice.delete" call.

func (*ManagedconfigurationsfordeviceDeleteCall) Fields ¶
func (c *ManagedconfigurationsfordeviceDeleteCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsfordeviceDeleteCall) Header ¶
func (c *ManagedconfigurationsfordeviceDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagedconfigurationsfordeviceGetCall ¶
type ManagedconfigurationsfordeviceGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsfordeviceGetCall) Context ¶
func (c *ManagedconfigurationsfordeviceGetCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceGetCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsfordeviceGetCall) Do ¶
func (c *ManagedconfigurationsfordeviceGetCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)

Do executes the "androidenterprise.managedconfigurationsfordevice.get" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfiguration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsfordeviceGetCall) Fields ¶
func (c *ManagedconfigurationsfordeviceGetCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsfordeviceGetCall) Header ¶
func (c *ManagedconfigurationsfordeviceGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagedconfigurationsfordeviceGetCall) IfNoneMatch ¶
func (c *ManagedconfigurationsfordeviceGetCall) IfNoneMatch(entityTag string) *ManagedconfigurationsfordeviceGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagedconfigurationsfordeviceListCall ¶
type ManagedconfigurationsfordeviceListCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsfordeviceListCall) Context ¶
func (c *ManagedconfigurationsfordeviceListCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceListCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsfordeviceListCall) Do ¶
func (c *ManagedconfigurationsfordeviceListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsForDeviceListResponse, error)

Do executes the "androidenterprise.managedconfigurationsfordevice.list" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfigurationsForDeviceListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsfordeviceListCall) Fields ¶
func (c *ManagedconfigurationsfordeviceListCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsfordeviceListCall) Header ¶
func (c *ManagedconfigurationsfordeviceListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagedconfigurationsfordeviceListCall) IfNoneMatch ¶
func (c *ManagedconfigurationsfordeviceListCall) IfNoneMatch(entityTag string) *ManagedconfigurationsfordeviceListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagedconfigurationsfordeviceService ¶
type ManagedconfigurationsfordeviceService struct {
	// contains filtered or unexported fields
}
func NewManagedconfigurationsfordeviceService ¶
func NewManagedconfigurationsfordeviceService(s *Service) *ManagedconfigurationsfordeviceService
func (*ManagedconfigurationsfordeviceService) Delete ¶
func (r *ManagedconfigurationsfordeviceService) Delete(enterpriseId string, userId string, deviceId string, managedConfigurationForDeviceId string) *ManagedconfigurationsfordeviceDeleteCall

Delete: Removes a per-device managed configuration for an app for the specified device.

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
managedConfigurationForDeviceId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*ManagedconfigurationsfordeviceService) Get ¶
func (r *ManagedconfigurationsfordeviceService) Get(enterpriseId string, userId string, deviceId string, managedConfigurationForDeviceId string) *ManagedconfigurationsfordeviceGetCall

Get: Retrieves details of a per-device managed configuration.

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
managedConfigurationForDeviceId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*ManagedconfigurationsfordeviceService) List ¶
func (r *ManagedconfigurationsfordeviceService) List(enterpriseId string, userId string, deviceId string) *ManagedconfigurationsfordeviceListCall

List: Lists all the per-device managed configurations for the specified device. Only the ID is set.

- deviceId: The Android ID of the device. - enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*ManagedconfigurationsfordeviceService) Update ¶
func (r *ManagedconfigurationsfordeviceService) Update(enterpriseId string, userId string, deviceId string, managedConfigurationForDeviceId string, managedconfiguration *ManagedConfiguration) *ManagedconfigurationsfordeviceUpdateCall

Update: Adds or updates a per-device managed configuration for an app for the specified device.

deviceId: The Android ID of the device.
enterpriseId: The ID of the enterprise.
managedConfigurationForDeviceId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
type ManagedconfigurationsfordeviceUpdateCall ¶
type ManagedconfigurationsfordeviceUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsfordeviceUpdateCall) Context ¶
func (c *ManagedconfigurationsfordeviceUpdateCall) Context(ctx context.Context) *ManagedconfigurationsfordeviceUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsfordeviceUpdateCall) Do ¶
func (c *ManagedconfigurationsfordeviceUpdateCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)

Do executes the "androidenterprise.managedconfigurationsfordevice.update" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfiguration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsfordeviceUpdateCall) Fields ¶
func (c *ManagedconfigurationsfordeviceUpdateCall) Fields(s ...googleapi.Field) *ManagedconfigurationsfordeviceUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsfordeviceUpdateCall) Header ¶
func (c *ManagedconfigurationsfordeviceUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagedconfigurationsforuserDeleteCall ¶
type ManagedconfigurationsforuserDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsforuserDeleteCall) Context ¶
func (c *ManagedconfigurationsforuserDeleteCall) Context(ctx context.Context) *ManagedconfigurationsforuserDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsforuserDeleteCall) Do ¶
func (c *ManagedconfigurationsforuserDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.managedconfigurationsforuser.delete" call.

func (*ManagedconfigurationsforuserDeleteCall) Fields ¶
func (c *ManagedconfigurationsforuserDeleteCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsforuserDeleteCall) Header ¶
func (c *ManagedconfigurationsforuserDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagedconfigurationsforuserGetCall ¶
type ManagedconfigurationsforuserGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsforuserGetCall) Context ¶
func (c *ManagedconfigurationsforuserGetCall) Context(ctx context.Context) *ManagedconfigurationsforuserGetCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsforuserGetCall) Do ¶
func (c *ManagedconfigurationsforuserGetCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)

Do executes the "androidenterprise.managedconfigurationsforuser.get" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfiguration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsforuserGetCall) Fields ¶
func (c *ManagedconfigurationsforuserGetCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsforuserGetCall) Header ¶
func (c *ManagedconfigurationsforuserGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagedconfigurationsforuserGetCall) IfNoneMatch ¶
func (c *ManagedconfigurationsforuserGetCall) IfNoneMatch(entityTag string) *ManagedconfigurationsforuserGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagedconfigurationsforuserListCall ¶
type ManagedconfigurationsforuserListCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsforuserListCall) Context ¶
func (c *ManagedconfigurationsforuserListCall) Context(ctx context.Context) *ManagedconfigurationsforuserListCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsforuserListCall) Do ¶
func (c *ManagedconfigurationsforuserListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsForUserListResponse, error)

Do executes the "androidenterprise.managedconfigurationsforuser.list" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfigurationsForUserListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsforuserListCall) Fields ¶
func (c *ManagedconfigurationsforuserListCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsforuserListCall) Header ¶
func (c *ManagedconfigurationsforuserListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagedconfigurationsforuserListCall) IfNoneMatch ¶
func (c *ManagedconfigurationsforuserListCall) IfNoneMatch(entityTag string) *ManagedconfigurationsforuserListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagedconfigurationsforuserService ¶
type ManagedconfigurationsforuserService struct {
	// contains filtered or unexported fields
}
func NewManagedconfigurationsforuserService ¶
func NewManagedconfigurationsforuserService(s *Service) *ManagedconfigurationsforuserService
func (*ManagedconfigurationsforuserService) Delete ¶
func (r *ManagedconfigurationsforuserService) Delete(enterpriseId string, userId string, managedConfigurationForUserId string) *ManagedconfigurationsforuserDeleteCall

Delete: Removes a per-user managed configuration for an app for the specified user.

enterpriseId: The ID of the enterprise.
managedConfigurationForUserId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*ManagedconfigurationsforuserService) Get ¶
func (r *ManagedconfigurationsforuserService) Get(enterpriseId string, userId string, managedConfigurationForUserId string) *ManagedconfigurationsforuserGetCall

Get: Retrieves details of a per-user managed configuration for an app for the specified user.

enterpriseId: The ID of the enterprise.
managedConfigurationForUserId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
func (*ManagedconfigurationsforuserService) List ¶
func (r *ManagedconfigurationsforuserService) List(enterpriseId string, userId string) *ManagedconfigurationsforuserListCall

List: Lists all the per-user managed configurations for the specified user. Only the ID is set.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*ManagedconfigurationsforuserService) Update ¶
func (r *ManagedconfigurationsforuserService) Update(enterpriseId string, userId string, managedConfigurationForUserId string, managedconfiguration *ManagedConfiguration) *ManagedconfigurationsforuserUpdateCall

Update: Adds or updates the managed configuration settings for an app for the specified user. If you support the Managed configurations iframe, you can apply managed configurations to a user by specifying an mcmId and its associated configuration variables (if any) in the request. Alternatively, all EMMs can apply managed configurations by passing a list of managed properties.

enterpriseId: The ID of the enterprise.
managedConfigurationForUserId: The ID of the managed configuration (a product ID), e.g. "app:com.google.android.gm".
userId: The ID of the user.
type ManagedconfigurationsforuserUpdateCall ¶
type ManagedconfigurationsforuserUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationsforuserUpdateCall) Context ¶
func (c *ManagedconfigurationsforuserUpdateCall) Context(ctx context.Context) *ManagedconfigurationsforuserUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationsforuserUpdateCall) Do ¶
func (c *ManagedconfigurationsforuserUpdateCall) Do(opts ...googleapi.CallOption) (*ManagedConfiguration, error)

Do executes the "androidenterprise.managedconfigurationsforuser.update" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfiguration.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationsforuserUpdateCall) Fields ¶
func (c *ManagedconfigurationsforuserUpdateCall) Fields(s ...googleapi.Field) *ManagedconfigurationsforuserUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationsforuserUpdateCall) Header ¶
func (c *ManagedconfigurationsforuserUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagedconfigurationssettingsListCall ¶
type ManagedconfigurationssettingsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagedconfigurationssettingsListCall) Context ¶
func (c *ManagedconfigurationssettingsListCall) Context(ctx context.Context) *ManagedconfigurationssettingsListCall

Context sets the context to be used in this call's Do method.

func (*ManagedconfigurationssettingsListCall) Do ¶
func (c *ManagedconfigurationssettingsListCall) Do(opts ...googleapi.CallOption) (*ManagedConfigurationsSettingsListResponse, error)

Do executes the "androidenterprise.managedconfigurationssettings.list" call. Any non-2xx status code is an error. Response headers are in either *ManagedConfigurationsSettingsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagedconfigurationssettingsListCall) Fields ¶
func (c *ManagedconfigurationssettingsListCall) Fields(s ...googleapi.Field) *ManagedconfigurationssettingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagedconfigurationssettingsListCall) Header ¶
func (c *ManagedconfigurationssettingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagedconfigurationssettingsListCall) IfNoneMatch ¶
func (c *ManagedconfigurationssettingsListCall) IfNoneMatch(entityTag string) *ManagedconfigurationssettingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagedconfigurationssettingsService ¶
type ManagedconfigurationssettingsService struct {
	// contains filtered or unexported fields
}
func NewManagedconfigurationssettingsService ¶
func NewManagedconfigurationssettingsService(s *Service) *ManagedconfigurationssettingsService
func (*ManagedconfigurationssettingsService) List ¶
func (r *ManagedconfigurationssettingsService) List(enterpriseId string, productId string) *ManagedconfigurationssettingsListCall

List: Lists all the managed configurations settings for the specified app.

enterpriseId: The ID of the enterprise.
productId: The ID of the product for which the managed configurations settings applies to.
type NewDeviceEvent ¶
type NewDeviceEvent struct {
	// DeviceId: The Android ID of the device. This field will always be present.
	DeviceId string `json:"deviceId,omitempty"`
	// DpcPackageName: Policy app on the device.
	DpcPackageName string `json:"dpcPackageName,omitempty"`
	// ManagementType: Identifies the extent to which the device is controlled by
	// an Android EMM in various deployment configurations. Possible values
	// include: - "managedDevice", a device where the DPC is set as device owner, -
	// "managedProfile", a device where the DPC is set as profile owner.
	//
	// Possible values:
	//   "managedDevice"
	//   "managedProfile"
	ManagementType string `json:"managementType,omitempty"`
	// UserId: The ID of the user. This field will always be present.
	UserId string `json:"userId,omitempty"`
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

NewDeviceEvent: An event generated when a new device is ready to be managed.

func (NewDeviceEvent) MarshalJSON ¶
func (s NewDeviceEvent) MarshalJSON() ([]byte, error)
type NewPermissionsEvent ¶
type NewPermissionsEvent struct {
	// ApprovedPermissions: The set of permissions that the enterprise admin has
	// already approved for this application. Use Permissions.Get on the EMM API to
	// retrieve details about these permissions.
	ApprovedPermissions []string `json:"approvedPermissions,omitempty"`
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") for
	// which new permissions were added. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// RequestedPermissions: The set of permissions that the app is currently
	// requesting. Use Permissions.Get on the EMM API to retrieve details about
	// these permissions.
	RequestedPermissions []string `json:"requestedPermissions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApprovedPermissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApprovedPermissions") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NewPermissionsEvent: An event generated when new permissions are added to an app.

func (NewPermissionsEvent) MarshalJSON ¶
func (s NewPermissionsEvent) MarshalJSON() ([]byte, error)
type Notification ¶
type Notification struct {
	// AppRestrictionsSchemaChangeEvent: Notifications about new app restrictions
	// schema changes.
	AppRestrictionsSchemaChangeEvent *AppRestrictionsSchemaChangeEvent `json:"appRestrictionsSchemaChangeEvent,omitempty"`
	// AppUpdateEvent: Notifications about app updates.
	AppUpdateEvent *AppUpdateEvent `json:"appUpdateEvent,omitempty"`
	// DeviceReportUpdateEvent: Notifications about device report updates.
	DeviceReportUpdateEvent *DeviceReportUpdateEvent `json:"deviceReportUpdateEvent,omitempty"`
	// EnterpriseId: The ID of the enterprise for which the notification is sent.
	// This will always be present.
	EnterpriseId string `json:"enterpriseId,omitempty"`
	// EnterpriseUpgradeEvent: Notifications about enterprise upgrade.
	EnterpriseUpgradeEvent *EnterpriseUpgradeEvent `json:"enterpriseUpgradeEvent,omitempty"`
	// InstallFailureEvent: Notifications about an app installation failure.
	InstallFailureEvent *InstallFailureEvent `json:"installFailureEvent,omitempty"`
	// NewDeviceEvent: Notifications about new devices.
	NewDeviceEvent *NewDeviceEvent `json:"newDeviceEvent,omitempty"`
	// NewPermissionsEvent: Notifications about new app permissions.
	NewPermissionsEvent *NewPermissionsEvent `json:"newPermissionsEvent,omitempty"`
	// NotificationType: Type of the notification.
	//
	// Possible values:
	//   "unknown"
	//   "testNotification" - A test push notification.
	//   "productApproval" - Notification about change to a product's approval
	// status.
	//   "installFailure" - Notification about an app installation failure.
	//   "appUpdate" - Notification about app update.
	//   "newPermissions" - Notification about new app permissions.
	//   "appRestricionsSchemaChange" - Notification about new app restrictions
	// schema change.
	//   "productAvailabilityChange" - Notification about product availability
	// change.
	//   "newDevice" - Notification about a new device.
	//   "deviceReportUpdate" - Notification about an updated device report.
	//   "enterpriseUpgrade" - Notification about an enterprise upgrade.
	NotificationType string `json:"notificationType,omitempty"`
	// ProductApprovalEvent: Notifications about changes to a product's approval
	// status.
	ProductApprovalEvent *ProductApprovalEvent `json:"productApprovalEvent,omitempty"`
	// ProductAvailabilityChangeEvent: Notifications about product availability
	// changes.
	ProductAvailabilityChangeEvent *ProductAvailabilityChangeEvent `json:"productAvailabilityChangeEvent,omitempty"`
	// TimestampMillis: The time when the notification was published in
	// milliseconds since 1970-01-01T00:00:00Z. This will always be present.
	TimestampMillis int64 `json:"timestampMillis,omitempty,string"`
	// ForceSendFields is a list of field names (e.g.
	// "AppRestrictionsSchemaChangeEvent") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AppRestrictionsSchemaChangeEvent") to include in API requests with the JSON
	// null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

Notification: A notification of one event relating to an enterprise.

func (Notification) MarshalJSON ¶
func (s Notification) MarshalJSON() ([]byte, error)
type NotificationSet ¶
type NotificationSet struct {
	// Notification: The notifications received, or empty if no notifications are
	// present.
	Notification []*Notification `json:"notification,omitempty"`
	// NotificationSetId: The notification set ID, required to mark the
	// notification as received with the Enterprises.AcknowledgeNotification API.
	// This will be omitted if no notifications are present.
	NotificationSetId string `json:"notificationSetId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Notification") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Notification") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NotificationSet: A resource returned by the PullNotificationSet API, which contains a collection of notifications for enterprises associated with the service account authenticated for the request.

func (NotificationSet) MarshalJSON ¶
func (s NotificationSet) MarshalJSON() ([]byte, error)
type PageInfo ¶
type PageInfo struct {
	// ResultPerPage: Maximum number of results returned in one page. ! The number
	// of results included in the API response.
	ResultPerPage int64 `json:"resultPerPage,omitempty"`
	// StartIndex: Index of the first result returned in the current page.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: Total number of results available on the backend ! The total
	// number of results in the result set.
	TotalResults int64 `json:"totalResults,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ResultPerPage") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ResultPerPage") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PageInfo: Information about the current page. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned.

func (PageInfo) MarshalJSON ¶
func (s PageInfo) MarshalJSON() ([]byte, error)
type Permission ¶
type Permission struct {
	// Description: A longer description of the Permissions resource, giving more
	// details of what it affects.
	Description string `json:"description,omitempty"`
	// Name: The name of the permission.
	Name string `json:"name,omitempty"`
	// PermissionId: An opaque string uniquely identifying the permission.
	PermissionId string `json:"permissionId,omitempty"`

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

Permission: A Permissions resource represents some extra capability, to be granted to an Android app, which requires explicit consent. An enterprise admin must consent to these permissions on behalf of their users before an entitlement for the app can be created. The permissions collection is read-only. The information provided for each permission (localized name and description) is intended to be used in the MDM user interface when obtaining consent from the enterprise.

func (Permission) MarshalJSON ¶
func (s Permission) MarshalJSON() ([]byte, error)
type PermissionsGetCall ¶
type PermissionsGetCall struct {
	// contains filtered or unexported fields
}
func (*PermissionsGetCall) Context ¶
func (c *PermissionsGetCall) Context(ctx context.Context) *PermissionsGetCall

Context sets the context to be used in this call's Do method.

func (*PermissionsGetCall) Do ¶
func (c *PermissionsGetCall) Do(opts ...googleapi.CallOption) (*Permission, error)

Do executes the "androidenterprise.permissions.get" call. Any non-2xx status code is an error. Response headers are in either *Permission.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PermissionsGetCall) Fields ¶
func (c *PermissionsGetCall) Fields(s ...googleapi.Field) *PermissionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PermissionsGetCall) Header ¶
func (c *PermissionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PermissionsGetCall) IfNoneMatch ¶
func (c *PermissionsGetCall) IfNoneMatch(entityTag string) *PermissionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PermissionsGetCall) Language ¶
func (c *PermissionsGetCall) Language(language string) *PermissionsGetCall

Language sets the optional parameter "language": The BCP47 tag for the user's preferred language (e.g. "en-US", "de")

type PermissionsService ¶
type PermissionsService struct {
	// contains filtered or unexported fields
}
func NewPermissionsService ¶
func NewPermissionsService(s *Service) *PermissionsService
func (*PermissionsService) Get ¶
func (r *PermissionsService) Get(permissionId string) *PermissionsGetCall

Get: Retrieves details of an Android app permission for display to an enterprise admin.

- permissionId: The ID of the permission.

type Policy ¶
type Policy struct {
	// AutoUpdatePolicy: Controls when automatic app updates on the device can be
	// applied. Recommended alternative: autoUpdateMode which is set per app,
	// provides greater flexibility around update frequency. When autoUpdateMode is
	// set to AUTO_UPDATE_POSTPONED or AUTO_UPDATE_HIGH_PRIORITY, autoUpdatePolicy
	// has no effect. - choiceToTheUser allows the device's user to configure the
	// app update policy. - always enables auto updates. - never disables auto
	// updates. - wifiOnly enables auto updates only when the device is connected
	// to wifi. *Important:* Changes to app update policies don't affect updates
	// that are in progress. Any policy changes will apply to subsequent app
	// updates.
	//
	// Possible values:
	//   "autoUpdatePolicyUnspecified" - The auto update policy is not set.
	//   "choiceToTheUser" - The user can control auto-updates.
	//   "never" - Apps are never auto-updated.
	//   "wifiOnly" - Apps are auto-updated over WiFi only.
	//   "always" - Apps are auto-updated at any time. Data charges may apply.
	AutoUpdatePolicy string `json:"autoUpdatePolicy,omitempty"`
	// DeviceReportPolicy: Whether the device reports app states to the EMM. The
	// default value is "deviceReportDisabled".
	//
	// Possible values:
	//   "deviceReportPolicyUnspecified" - The device report policy is not set.
	//   "deviceReportDisabled" - Device reports are disabled.
	//   "deviceReportEnabled" - Device reports are enabled.
	DeviceReportPolicy string `json:"deviceReportPolicy,omitempty"`
	// MaintenanceWindow: The maintenance window defining when apps running in the
	// foreground should be updated.
	MaintenanceWindow *MaintenanceWindow `json:"maintenanceWindow,omitempty"`
	// PolicyId: An identifier for the policy that will be passed with the app
	// install feedback sent from the Play Store.
	PolicyId string `json:"policyId,omitempty"`
	// ProductAvailabilityPolicy: The availability granted to the device for the
	// specified products. "all" gives the device access to all products,
	// regardless of approval status. "all" does not enable automatic visibility of
	// "alpha" or "beta" tracks. "whitelist" grants the device access the products
	// specified in productPolicy[]. Only products that are approved or products
	// that were previously approved (products with revoked approval) by the
	// enterprise can be whitelisted. If no value is provided, the availability set
	// at the user level is applied by default.
	//
	// Possible values:
	//   "productAvailabilityPolicyUnspecified" - Unspecified, applies the user
	// available product set by default.
	//   "whitelist" - The approved products with product availability set to
	// AVAILABLE in the product policy are available.
	//   "all" - All products are available except those explicitly marked as
	// unavailable in the product availability policy.
	ProductAvailabilityPolicy string `json:"productAvailabilityPolicy,omitempty"`
	// ProductPolicy: The list of product policies. The productAvailabilityPolicy
	// needs to be set to WHITELIST or ALL for the product policies to be applied.
	ProductPolicy []*ProductPolicy `json:"productPolicy,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoUpdatePolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoUpdatePolicy") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Policy: The device policy for a given managed device.

func (Policy) MarshalJSON ¶
func (s Policy) MarshalJSON() ([]byte, error)
type Product ¶
type Product struct {
	// AppRestrictionsSchema: The app restriction schema
	AppRestrictionsSchema *AppRestrictionsSchema `json:"appRestrictionsSchema,omitempty"`
	// AppTracks: The tracks visible to the enterprise.
	AppTracks []*TrackInfo `json:"appTracks,omitempty"`
	// AppVersion: App versions currently available for this product.
	AppVersion []*AppVersion `json:"appVersion,omitempty"`
	// AuthorName: The name of the author of the product (for example, the app
	// developer).
	AuthorName string `json:"authorName,omitempty"`
	// AvailableCountries: The countries which this app is available in.
	AvailableCountries []string `json:"availableCountries,omitempty"`
	// AvailableTracks: Deprecated, use appTracks instead.
	//
	// Possible values:
	//   "appTrackUnspecified"
	//   "production"
	//   "beta"
	//   "alpha"
	AvailableTracks []string `json:"availableTracks,omitempty"`
	// Category: The app category (e.g. RACING, SOCIAL, etc.)
	Category string `json:"category,omitempty"`
	// ContentRating: The content rating for this app.
	//
	// Possible values:
	//   "ratingUnknown"
	//   "all"
	//   "preTeen"
	//   "teen"
	//   "mature"
	ContentRating string `json:"contentRating,omitempty"`
	// Description: The localized promotional description, if available.
	Description string `json:"description,omitempty"`
	// DetailsUrl: A link to the (consumer) Google Play details page for the
	// product.
	DetailsUrl string `json:"detailsUrl,omitempty"`
	// DistributionChannel: How and to whom the package is made available. The
	// value publicGoogleHosted means that the package is available through the
	// Play store and not restricted to a specific enterprise. The value
	// privateGoogleHosted means that the package is a private app (restricted to
	// an enterprise) but hosted by Google. The value privateSelfHosted means that
	// the package is a private app (restricted to an enterprise) and is privately
	// hosted.
	//
	// Possible values:
	//   "publicGoogleHosted"
	//   "privateGoogleHosted"
	//   "privateSelfHosted"
	DistributionChannel string `json:"distributionChannel,omitempty"`
	// Features: Noteworthy features (if any) of this product.
	//
	// Possible values:
	//   "featureUnknown"
	//   "vpnApp" - The app is a VPN.
	Features []string `json:"features,omitempty"`
	// FullDescription: The localized full app store description, if available.
	FullDescription string `json:"fullDescription,omitempty"`
	// IconUrl: A link to an image that can be used as an icon for the product.
	// This image is suitable for use at up to 512px x 512px.
	IconUrl string `json:"iconUrl,omitempty"`
	// LastUpdatedTimestampMillis: The approximate time (within 7 days) the app was
	// last published, expressed in milliseconds since epoch.
	LastUpdatedTimestampMillis int64 `json:"lastUpdatedTimestampMillis,omitempty,string"`
	// MinAndroidSdkVersion: The minimum Android SDK necessary to run the app.
	MinAndroidSdkVersion int64 `json:"minAndroidSdkVersion,omitempty"`
	// Permissions: A list of permissions required by the app.
	Permissions []*ProductPermission `json:"permissions,omitempty"`
	// ProductId: A string of the form *app:<package name>*. For example,
	// app:com.google.android.gm represents the Gmail app.
	ProductId string `json:"productId,omitempty"`
	// ProductPricing: Whether this product is free, free with in-app purchases, or
	// paid. If the pricing is unknown, this means the product is not generally
	// available anymore (even though it might still be available to people who own
	// it).
	//
	// Possible values:
	//   "unknown" - Unknown pricing, used to denote an approved product that is
	// not generally available.
	//   "free" - The product is free.
	//   "freeWithInAppPurchase" - The product is free, but offers in-app
	// purchases.
	//   "paid" - The product is paid.
	ProductPricing string `json:"productPricing,omitempty"`
	// RecentChanges: A description of the recent changes made to the app.
	RecentChanges string `json:"recentChanges,omitempty"`
	// RequiresContainerApp: Deprecated.
	RequiresContainerApp bool `json:"requiresContainerApp,omitempty"`
	// ScreenshotUrls: A list of screenshot links representing the app.
	ScreenshotUrls []string `json:"screenshotUrls,omitempty"`
	// SigningCertificate: The certificate used to sign this product.
	SigningCertificate *ProductSigningCertificate `json:"signingCertificate,omitempty"`
	// SmallIconUrl: A link to a smaller image that can be used as an icon for the
	// product. This image is suitable for use at up to 128px x 128px.
	SmallIconUrl string `json:"smallIconUrl,omitempty"`
	// Title: The name of the product.
	Title string `json:"title,omitempty"`
	// WorkDetailsUrl: A link to the managed Google Play details page for the
	// product, for use by an Enterprise admin.
	WorkDetailsUrl string `json:"workDetailsUrl,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppRestrictionsSchema") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppRestrictionsSchema") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Product: A Products resource represents an app in the Google Play store that is available to at least some users in the enterprise. (Some apps are restricted to a single enterprise, and no information about them is made available outside that enterprise.) The information provided for each product (localized name, icon, link to the full Google Play details page) is intended to allow a basic representation of the product within an EMM user interface.

func (Product) MarshalJSON ¶
func (s Product) MarshalJSON() ([]byte, error)
type ProductApprovalEvent ¶
type ProductApprovalEvent struct {
	// Approved: Whether the product was approved or unapproved. This field will
	// always be present.
	//
	// Possible values:
	//   "unknown" - Conveys no information.
	//   "approved" - The product was approved.
	//   "unapproved" - The product was unapproved.
	Approved string `json:"approved,omitempty"`
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") for
	// which the approval status has changed. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Approved") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Approved") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductApprovalEvent: An event generated when a product's approval status is changed.

func (ProductApprovalEvent) MarshalJSON ¶
func (s ProductApprovalEvent) MarshalJSON() ([]byte, error)
type ProductAvailabilityChangeEvent ¶
type ProductAvailabilityChangeEvent struct {
	// AvailabilityStatus: The new state of the product. This field will always be
	// present.
	//
	// Possible values:
	//   "unknown" - Conveys no information.
	//   "available" - The previously unavailable product is again available on
	// Google Play.
	//   "removed" - The product was removed from Google Play.
	//   "unpublished" - The product was unpublished by the developer.
	AvailabilityStatus string `json:"availabilityStatus,omitempty"`
	// ProductId: The id of the product (e.g. "app:com.google.android.gm") for
	// which the product availability changed. This field will always be present.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AvailabilityStatus") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailabilityStatus") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductAvailabilityChangeEvent: An event generated whenever a product's availability changes.

func (ProductAvailabilityChangeEvent) MarshalJSON ¶
func (s ProductAvailabilityChangeEvent) MarshalJSON() ([]byte, error)
type ProductPermission ¶
type ProductPermission struct {
	// PermissionId: An opaque string uniquely identifying the permission.
	PermissionId string `json:"permissionId,omitempty"`
	// State: Whether the permission has been accepted or not.
	//
	// Possible values:
	//   "required" - The permission is required by the app but has not yet been
	// accepted by the enterprise.
	//   "accepted" - The permission has been accepted by the enterprise.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PermissionId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PermissionId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPermission: A product permissions resource represents the set of permissions required by a specific app and whether or not they have been accepted by an enterprise admin. The API can be used to read the set of permissions, and also to update the set to indicate that permissions have been accepted.

func (ProductPermission) MarshalJSON ¶
func (s ProductPermission) MarshalJSON() ([]byte, error)
type ProductPermissions ¶
type ProductPermissions struct {
	// Permission: The permissions required by the app.
	Permission []*ProductPermission `json:"permission,omitempty"`
	// ProductId: The ID of the app that the permissions relate to, e.g.
	// "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Permission") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Permission") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPermissions: Information about the permissions required by a specific app and whether they have been accepted by the enterprise.

func (ProductPermissions) MarshalJSON ¶
func (s ProductPermissions) MarshalJSON() ([]byte, error)
type ProductPolicy ¶
type ProductPolicy struct {
	// AutoInstallPolicy: The auto-install policy for the product.
	AutoInstallPolicy *AutoInstallPolicy `json:"autoInstallPolicy,omitempty"`
	// AutoUpdateMode: The auto-update mode for the product. When autoUpdateMode is
	// used, it always takes precedence over the user's choice. So when a user
	// makes changes to the device settings manually, these changes are ignored.
	//
	// Possible values:
	//   "autoUpdateModeUnspecified" - Unspecified. Defaults to
	// AUTO_UPDATE_DEFAULT.
	//   "autoUpdateDefault" - The app is automatically updated with low priority
	// to minimize the impact on the user. The app is updated when the following
	// constraints are met: * The device is not actively used * The device is
	// connected to an unmetered network * The device is charging The device is
	// notified about a new update within 24 hours after it is published by the
	// developer, after which the app is updated the next time the constraints
	// above are met.
	//   "autoUpdatePostponed" - The app is not automatically updated for a maximum
	// of 90 days after the app becomes out of date. 90 days after the app becomes
	// out of date, the latest available version is installed automatically with
	// low priority (see AUTO_UPDATE_DEFAULT). After the app is updated it is not
	// automatically updated again until 90 days after it becomes out of date
	// again. The user can still manually update the app from the Play Store at any
	// time.
	//   "autoUpdateHighPriority" - The app is updated as soon as possible. No
	// constraints are applied. The device is notified as soon as possible about a
	// new app update after it is published by the developer.
	AutoUpdateMode string `json:"autoUpdateMode,omitempty"`
	// EnterpriseAuthenticationAppLinkConfigs: An authentication URL configuration
	// for the authenticator app of an identity provider. This helps to launch the
	// identity provider's authenticator app during the authentication happening in
	// a private app using Android WebView. Authenticator app should already be the
	// default handler for the authentication url on the device.
	EnterpriseAuthenticationAppLinkConfigs []*EnterpriseAuthenticationAppLinkConfig `json:"enterpriseAuthenticationAppLinkConfigs,omitempty"`
	// ManagedConfiguration: The managed configuration for the product.
	ManagedConfiguration *ManagedConfiguration `json:"managedConfiguration,omitempty"`
	// ProductId: The ID of the product. For example, "app:com.google.android.gm".
	ProductId string `json:"productId,omitempty"`
	// TrackIds: Grants the device visibility to the specified product release
	// track(s), identified by trackIds. The list of release tracks of a product
	// can be obtained by calling Products.Get.
	TrackIds []string `json:"trackIds,omitempty"`
	// Tracks: Deprecated. Use trackIds instead.
	//
	// Possible values:
	//   "appTrackUnspecified"
	//   "production"
	//   "beta"
	//   "alpha"
	Tracks []string `json:"tracks,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoInstallPolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoInstallPolicy") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPolicy: The policy for a product.

func (ProductPolicy) MarshalJSON ¶
func (s ProductPolicy) MarshalJSON() ([]byte, error)
type ProductSet ¶
type ProductSet struct {
	// ProductId: The list of product IDs making up the set of products.
	ProductId []string `json:"productId,omitempty"`
	// ProductSetBehavior: The interpretation of this product set. "unknown" should
	// never be sent and is ignored if received. "whitelist" means that the user is
	// entitled to access the product set. "includeAll" means that all products are
	// accessible, including products that are approved, products with revoked
	// approval, and products that have never been approved. "allApproved" means
	// that the user is entitled to access all products that are approved for the
	// enterprise. If the value is "allApproved" or "includeAll", the productId
	// field is ignored. If no value is provided, it is interpreted as "whitelist"
	// for backwards compatibility. Further "allApproved" or "includeAll" does not
	// enable automatic visibility of "alpha" or "beta" tracks for Android app. Use
	// ProductVisibility to enable "alpha" or "beta" tracks per user.
	//
	// Possible values:
	//   "unknown" - This value should never be sent and ignored if received.
	//   "whitelist" - This product set constitutes a whitelist.
	//   "includeAll" - This product set represents all products. For Android app
	// it represents only "production" track. (The value of the productId field is
	// therefore ignored).
	//   "allApproved" - This product set represents all approved products. For
	// Android app it represents only "production" track. (The value of the
	// product_id field is therefore ignored).
	ProductSetBehavior string `json:"productSetBehavior,omitempty"`
	// ProductVisibility: Additional list of product IDs making up the product set.
	// Unlike the productID array, in this list It's possible to specify which
	// tracks (alpha, beta, production) of a product are visible to the user. See
	// ProductVisibility and its fields for more information. Specifying the same
	// product ID both here and in the productId array is not allowed and it will
	// result in an error.
	ProductVisibility []*ProductVisibility `json:"productVisibility,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ProductId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductSet: A set of products.

func (ProductSet) MarshalJSON ¶
func (s ProductSet) MarshalJSON() ([]byte, error)
type ProductSigningCertificate ¶
type ProductSigningCertificate struct {
	// CertificateHashSha1: The base64 urlsafe encoded SHA1 hash of the
	// certificate. (This field is deprecated in favor of SHA2-256. It should not
	// be used and may be removed at any time.)
	CertificateHashSha1 string `json:"certificateHashSha1,omitempty"`
	// CertificateHashSha256: The base64 urlsafe encoded SHA2-256 hash of the
	// certificate.
	CertificateHashSha256 string `json:"certificateHashSha256,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CertificateHashSha1") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CertificateHashSha1") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ProductSigningCertificate) MarshalJSON ¶
func (s ProductSigningCertificate) MarshalJSON() ([]byte, error)
type ProductVisibility ¶
type ProductVisibility struct {
	// ProductId: The product ID to make visible to the user. Required for each
	// item in the productVisibility list.
	ProductId string `json:"productId,omitempty"`
	// TrackIds: Grants the user visibility to the specified product track(s),
	// identified by trackIds.
	TrackIds []string `json:"trackIds,omitempty"`
	// Tracks: Deprecated. Use trackIds instead.
	//
	// Possible values:
	//   "appTrackUnspecified"
	//   "production"
	//   "beta"
	//   "alpha"
	Tracks []string `json:"tracks,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProductId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductVisibility: A product to be made visible to a user.

func (ProductVisibility) MarshalJSON ¶
func (s ProductVisibility) MarshalJSON() ([]byte, error)
type ProductsApproveCall ¶
type ProductsApproveCall struct {
	// contains filtered or unexported fields
}
func (*ProductsApproveCall) Context ¶
func (c *ProductsApproveCall) Context(ctx context.Context) *ProductsApproveCall

Context sets the context to be used in this call's Do method.

func (*ProductsApproveCall) Do ¶
func (c *ProductsApproveCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.products.approve" call.

func (*ProductsApproveCall) Fields ¶
func (c *ProductsApproveCall) Fields(s ...googleapi.Field) *ProductsApproveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsApproveCall) Header ¶
func (c *ProductsApproveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProductsApproveRequest ¶
type ProductsApproveRequest struct {
	// ApprovalUrlInfo: The approval URL that was shown to the user. Only the
	// permissions shown to the user with that URL will be accepted, which may not
	// be the product's entire set of permissions. For example, the URL may only
	// display new permissions from an update after the product was approved, or
	// not include new permissions if the product was updated since the URL was
	// generated.
	ApprovalUrlInfo *ApprovalUrlInfo `json:"approvalUrlInfo,omitempty"`
	// ApprovedPermissions: Sets how new permission requests for the product are
	// handled. "allPermissions" automatically approves all current and future
	// permissions for the product. "currentPermissionsOnly" approves the current
	// set of permissions for the product, but any future permissions added through
	// updates will require manual reapproval. If not specified, only the current
	// set of permissions will be approved.
	//
	// Possible values:
	//   "currentPermissionsOnly" - Approve only the permissions the product
	// requires at approval time. If an update requires additional permissions, the
	// app will not be updated on devices associated with enterprise users until
	// the additional permissions are approved.
	//   "allPermissions" - All current and future permissions the app requires are
	// automatically approved.
	ApprovedPermissions string `json:"approvedPermissions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApprovalUrlInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApprovalUrlInfo") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ProductsApproveRequest) MarshalJSON ¶
func (s ProductsApproveRequest) MarshalJSON() ([]byte, error)
type ProductsGenerateApprovalUrlCall ¶
type ProductsGenerateApprovalUrlCall struct {
	// contains filtered or unexported fields
}
func (*ProductsGenerateApprovalUrlCall) Context ¶
func (c *ProductsGenerateApprovalUrlCall) Context(ctx context.Context) *ProductsGenerateApprovalUrlCall

Context sets the context to be used in this call's Do method.

func (*ProductsGenerateApprovalUrlCall) Do ¶
func (c *ProductsGenerateApprovalUrlCall) Do(opts ...googleapi.CallOption) (*ProductsGenerateApprovalUrlResponse, error)

Do executes the "androidenterprise.products.generateApprovalUrl" call. Any non-2xx status code is an error. Response headers are in either *ProductsGenerateApprovalUrlResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsGenerateApprovalUrlCall) Fields ¶
func (c *ProductsGenerateApprovalUrlCall) Fields(s ...googleapi.Field) *ProductsGenerateApprovalUrlCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsGenerateApprovalUrlCall) Header ¶
func (c *ProductsGenerateApprovalUrlCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProductsGenerateApprovalUrlCall) LanguageCode ¶
func (c *ProductsGenerateApprovalUrlCall) LanguageCode(languageCode string) *ProductsGenerateApprovalUrlCall

LanguageCode sets the optional parameter "languageCode": The BCP 47 language code used for permission names and descriptions in the returned iframe, for instance "en-US".

type ProductsGenerateApprovalUrlResponse ¶
type ProductsGenerateApprovalUrlResponse struct {
	// Url: A URL that can be rendered in an iframe to display the permissions (if
	// any) of a product. This URL can be used to approve the product only once and
	// only within 24 hours of being generated, using the Products.approve call. If
	// the product is currently unapproved and has no permissions, this URL will
	// point to an empty page. If the product is currently approved, a URL will
	// only be generated if that product has added permissions since it was last
	// approved, and the URL will only display those new permissions that have not
	// yet been accepted.
	Url string `json:"url,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Url") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Url") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ProductsGenerateApprovalUrlResponse) MarshalJSON ¶
func (s ProductsGenerateApprovalUrlResponse) MarshalJSON() ([]byte, error)
type ProductsGetAppRestrictionsSchemaCall ¶
type ProductsGetAppRestrictionsSchemaCall struct {
	// contains filtered or unexported fields
}
func (*ProductsGetAppRestrictionsSchemaCall) Context ¶
func (c *ProductsGetAppRestrictionsSchemaCall) Context(ctx context.Context) *ProductsGetAppRestrictionsSchemaCall

Context sets the context to be used in this call's Do method.

func (*ProductsGetAppRestrictionsSchemaCall) Do ¶
func (c *ProductsGetAppRestrictionsSchemaCall) Do(opts ...googleapi.CallOption) (*AppRestrictionsSchema, error)

Do executes the "androidenterprise.products.getAppRestrictionsSchema" call. Any non-2xx status code is an error. Response headers are in either *AppRestrictionsSchema.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsGetAppRestrictionsSchemaCall) Fields ¶
func (c *ProductsGetAppRestrictionsSchemaCall) Fields(s ...googleapi.Field) *ProductsGetAppRestrictionsSchemaCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsGetAppRestrictionsSchemaCall) Header ¶
func (c *ProductsGetAppRestrictionsSchemaCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProductsGetAppRestrictionsSchemaCall) IfNoneMatch ¶
func (c *ProductsGetAppRestrictionsSchemaCall) IfNoneMatch(entityTag string) *ProductsGetAppRestrictionsSchemaCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProductsGetAppRestrictionsSchemaCall) Language ¶
func (c *ProductsGetAppRestrictionsSchemaCall) Language(language string) *ProductsGetAppRestrictionsSchemaCall

Language sets the optional parameter "language": The BCP47 tag for the user's preferred language (e.g. "en-US", "de").

type ProductsGetCall ¶
type ProductsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProductsGetCall) Context ¶
func (c *ProductsGetCall) Context(ctx context.Context) *ProductsGetCall

Context sets the context to be used in this call's Do method.

func (*ProductsGetCall) Do ¶
func (c *ProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)

Do executes the "androidenterprise.products.get" call. Any non-2xx status code is an error. Response headers are in either *Product.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsGetCall) Fields ¶
func (c *ProductsGetCall) Fields(s ...googleapi.Field) *ProductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsGetCall) Header ¶
func (c *ProductsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProductsGetCall) IfNoneMatch ¶
func (c *ProductsGetCall) IfNoneMatch(entityTag string) *ProductsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProductsGetCall) Language ¶
func (c *ProductsGetCall) Language(language string) *ProductsGetCall

Language sets the optional parameter "language": The BCP47 tag for the user's preferred language (e.g. "en-US", "de").

type ProductsGetPermissionsCall ¶
type ProductsGetPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProductsGetPermissionsCall) Context ¶
func (c *ProductsGetPermissionsCall) Context(ctx context.Context) *ProductsGetPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProductsGetPermissionsCall) Do ¶
func (c *ProductsGetPermissionsCall) Do(opts ...googleapi.CallOption) (*ProductPermissions, error)

Do executes the "androidenterprise.products.getPermissions" call. Any non-2xx status code is an error. Response headers are in either *ProductPermissions.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsGetPermissionsCall) Fields ¶
func (c *ProductsGetPermissionsCall) Fields(s ...googleapi.Field) *ProductsGetPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsGetPermissionsCall) Header ¶
func (c *ProductsGetPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProductsGetPermissionsCall) IfNoneMatch ¶
func (c *ProductsGetPermissionsCall) IfNoneMatch(entityTag string) *ProductsGetPermissionsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProductsListCall ¶
type ProductsListCall struct {
	// contains filtered or unexported fields
}
func (*ProductsListCall) Approved ¶
func (c *ProductsListCall) Approved(approved bool) *ProductsListCall

Approved sets the optional parameter "approved": Specifies whether to search among all products (false) or among only products that have been approved (true). Only "true" is supported, and should be specified.

func (*ProductsListCall) Context ¶
func (c *ProductsListCall) Context(ctx context.Context) *ProductsListCall

Context sets the context to be used in this call's Do method.

func (*ProductsListCall) Do ¶
func (c *ProductsListCall) Do(opts ...googleapi.CallOption) (*ProductsListResponse, error)

Do executes the "androidenterprise.products.list" call. Any non-2xx status code is an error. Response headers are in either *ProductsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsListCall) Fields ¶
func (c *ProductsListCall) Fields(s ...googleapi.Field) *ProductsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsListCall) Header ¶
func (c *ProductsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProductsListCall) IfNoneMatch ¶
func (c *ProductsListCall) IfNoneMatch(entityTag string) *ProductsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProductsListCall) Language ¶
func (c *ProductsListCall) Language(language string) *ProductsListCall

Language sets the optional parameter "language": The BCP47 tag for the user's preferred language (e.g. "en-US", "de"). Results are returned in the language best matching the preferred language.

func (*ProductsListCall) MaxResults ¶
func (c *ProductsListCall) MaxResults(maxResults int64) *ProductsListCall

MaxResults sets the optional parameter "maxResults": Defines how many results the list operation should return. The default number depends on the resource collection.

func (*ProductsListCall) Query ¶
func (c *ProductsListCall) Query(query string) *ProductsListCall

Query sets the optional parameter "query": The search query as typed in the Google Play store search box. If omitted, all approved apps will be returned (using the pagination parameters), including apps that are not available in the store (e.g. unpublished apps).

func (*ProductsListCall) Token ¶
func (c *ProductsListCall) Token(token string) *ProductsListCall

Token sets the optional parameter "token": Defines the token of the page to return, usually taken from TokenPagination. This can only be used if token paging is enabled.

type ProductsListResponse ¶
type ProductsListResponse struct {
	// PageInfo: General pagination information.
	PageInfo *PageInfo `json:"pageInfo,omitempty"`
	// Product: Information about a product (e.g. an app) in the Google Play store,
	// for display to an enterprise admin.
	Product []*Product `json:"product,omitempty"`
	// TokenPagination: Pagination information for token pagination.
	TokenPagination *TokenPagination `json:"tokenPagination,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "PageInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PageInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ProductsListResponse) MarshalJSON ¶
func (s ProductsListResponse) MarshalJSON() ([]byte, error)
type ProductsService ¶
type ProductsService struct {
	// contains filtered or unexported fields
}
func NewProductsService ¶
func NewProductsService(s *Service) *ProductsService
func (*ProductsService) Approve ¶
func (r *ProductsService) Approve(enterpriseId string, productId string, productsapproverequest *ProductsApproveRequest) *ProductsApproveCall

Approve: Approves the specified product and the relevant app permissions, if any. The maximum number of products that you can approve per enterprise customer is 1,000. To learn how to use managed Google Play to design and create a store layout to display approved products to your users, see Store Layout Design. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product.

func (*ProductsService) GenerateApprovalUrl ¶
func (r *ProductsService) GenerateApprovalUrl(enterpriseId string, productId string) *ProductsGenerateApprovalUrlCall

GenerateApprovalUrl: Generates a URL that can be rendered in an iframe to display the permissions (if any) of a product. An enterprise admin must view these permissions and accept them on behalf of their organization in order to approve that product. Admins should accept the displayed permissions by interacting with a separate UI element in the EMM console, which in turn should trigger the use of this URL as the approvalUrlInfo.approvalUrl property in a Products.approve call to approve the product. This URL can only be used to display permissions for up to 1 day. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product.

func (*ProductsService) Get ¶
func (r *ProductsService) Get(enterpriseId string, productId string) *ProductsGetCall

Get: Retrieves details of a product for display to an enterprise admin.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product, e.g. "app:com.google.android.gm".

func (*ProductsService) GetAppRestrictionsSchema ¶
func (r *ProductsService) GetAppRestrictionsSchema(enterpriseId string, productId string) *ProductsGetAppRestrictionsSchemaCall

GetAppRestrictionsSchema: Retrieves the schema that defines the configurable properties for this product. All products have a schema, but this schema may be empty if no managed configurations have been defined. This schema can be used to populate a UI that allows an admin to configure the product. To apply a managed configuration based on the schema obtained using this API, see Managed Configurations through Play.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product.

func (*ProductsService) GetPermissions ¶
func (r *ProductsService) GetPermissions(enterpriseId string, productId string) *ProductsGetPermissionsCall

GetPermissions: Retrieves the Android app permissions required by this app.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product.

func (*ProductsService) List ¶
func (r *ProductsService) List(enterpriseId string) *ProductsListCall

List: Finds approved products that match a query, or all approved products if there is no query. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise.

func (*ProductsService) Unapprove ¶
func (r *ProductsService) Unapprove(enterpriseId string, productId string) *ProductsUnapproveCall

Unapprove: Unapproves the specified product (and the relevant app permissions, if any) **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - productId: The ID of the product.

type ProductsUnapproveCall ¶
type ProductsUnapproveCall struct {
	// contains filtered or unexported fields
}
func (*ProductsUnapproveCall) Context ¶
func (c *ProductsUnapproveCall) Context(ctx context.Context) *ProductsUnapproveCall

Context sets the context to be used in this call's Do method.

func (*ProductsUnapproveCall) Do ¶
func (c *ProductsUnapproveCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.products.unapprove" call.

func (*ProductsUnapproveCall) Fields ¶
func (c *ProductsUnapproveCall) Fields(s ...googleapi.Field) *ProductsUnapproveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProductsUnapproveCall) Header ¶
func (c *ProductsUnapproveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Devices *DevicesService

	EnrollmentTokens *EnrollmentTokensService

	Enterprises *EnterprisesService

	Entitlements *EntitlementsService

	Grouplicenses *GrouplicensesService

	Grouplicenseusers *GrouplicenseusersService

	Installs *InstallsService

	Managedconfigurationsfordevice *ManagedconfigurationsfordeviceService

	Managedconfigurationsforuser *ManagedconfigurationsforuserService

	Managedconfigurationssettings *ManagedconfigurationssettingsService

	Permissions *PermissionsService

	Products *ProductsService

	Serviceaccountkeys *ServiceaccountkeysService

	Storelayoutclusters *StorelayoutclustersService

	Storelayoutpages *StorelayoutpagesService

	Users *UsersService

	Webapps *WebappsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type ServiceAccount ¶
type ServiceAccount struct {
	// Key: Credentials that can be used to authenticate as this ServiceAccount.
	Key *ServiceAccountKey `json:"key,omitempty"`
	// Name: The account name of the service account, in the form of an email
	// address. Assigned by the server.
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

ServiceAccount: A service account identity, including the name and credentials that can be used to authenticate as the service account.

func (ServiceAccount) MarshalJSON ¶
func (s ServiceAccount) MarshalJSON() ([]byte, error)
type ServiceAccountKey ¶
type ServiceAccountKey struct {
	// Data: The body of the private key credentials file, in string format. This
	// is only populated when the ServiceAccountKey is created, and is not stored
	// by Google.
	Data string `json:"data,omitempty"`
	// Id: An opaque, unique identifier for this ServiceAccountKey. Assigned by the
	// server.
	Id string `json:"id,omitempty"`
	// PublicData: Public key data for the credentials file. This is an X.509 cert.
	// If you are using the googleCredentials key type, this is identical to the
	// cert that can be retrieved by using the X.509 cert url inside of the
	// credentials file.
	PublicData string `json:"publicData,omitempty"`
	// Type: The file format of the generated key data.
	//
	// Possible values:
	//   "googleCredentials" - Google Credentials File format.
	//   "pkcs12" - PKCS12 format. The password for the PKCS12 file is
	// 'notasecret'. For more information, see https://tools.ietf.org/html/rfc7292.
	// The data for keys of this type are base64 encoded according to RFC 4648
	// Section 4. See http://tools.ietf.org/html/rfc4648#section-4.
	Type string `json:"type,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Data") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Data") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServiceAccountKey: *Deprecated:* New integrations cannot use this method and can refer to our new recommendations

func (ServiceAccountKey) MarshalJSON ¶
func (s ServiceAccountKey) MarshalJSON() ([]byte, error)
type ServiceAccountKeysListResponse ¶
type ServiceAccountKeysListResponse struct {
	// ServiceAccountKey: The service account credentials.
	ServiceAccountKey []*ServiceAccountKey `json:"serviceAccountKey,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ServiceAccountKey") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServiceAccountKey") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ServiceAccountKeysListResponse) MarshalJSON ¶
func (s ServiceAccountKeysListResponse) MarshalJSON() ([]byte, error)
type ServiceaccountkeysDeleteCall ¶
type ServiceaccountkeysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ServiceaccountkeysDeleteCall) Context ¶
func (c *ServiceaccountkeysDeleteCall) Context(ctx context.Context) *ServiceaccountkeysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ServiceaccountkeysDeleteCall) Do ¶
func (c *ServiceaccountkeysDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.serviceaccountkeys.delete" call.

func (*ServiceaccountkeysDeleteCall) Fields ¶
func (c *ServiceaccountkeysDeleteCall) Fields(s ...googleapi.Field) *ServiceaccountkeysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ServiceaccountkeysDeleteCall) Header ¶
func (c *ServiceaccountkeysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ServiceaccountkeysInsertCall ¶
type ServiceaccountkeysInsertCall struct {
	// contains filtered or unexported fields
}
func (*ServiceaccountkeysInsertCall) Context ¶
func (c *ServiceaccountkeysInsertCall) Context(ctx context.Context) *ServiceaccountkeysInsertCall

Context sets the context to be used in this call's Do method.

func (*ServiceaccountkeysInsertCall) Do ¶
func (c *ServiceaccountkeysInsertCall) Do(opts ...googleapi.CallOption) (*ServiceAccountKey, error)

Do executes the "androidenterprise.serviceaccountkeys.insert" call. Any non-2xx status code is an error. Response headers are in either *ServiceAccountKey.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ServiceaccountkeysInsertCall) Fields ¶
func (c *ServiceaccountkeysInsertCall) Fields(s ...googleapi.Field) *ServiceaccountkeysInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ServiceaccountkeysInsertCall) Header ¶
func (c *ServiceaccountkeysInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ServiceaccountkeysListCall ¶
type ServiceaccountkeysListCall struct {
	// contains filtered or unexported fields
}
func (*ServiceaccountkeysListCall) Context ¶
func (c *ServiceaccountkeysListCall) Context(ctx context.Context) *ServiceaccountkeysListCall

Context sets the context to be used in this call's Do method.

func (*ServiceaccountkeysListCall) Do ¶
func (c *ServiceaccountkeysListCall) Do(opts ...googleapi.CallOption) (*ServiceAccountKeysListResponse, error)

Do executes the "androidenterprise.serviceaccountkeys.list" call. Any non-2xx status code is an error. Response headers are in either *ServiceAccountKeysListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ServiceaccountkeysListCall) Fields ¶
func (c *ServiceaccountkeysListCall) Fields(s ...googleapi.Field) *ServiceaccountkeysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ServiceaccountkeysListCall) Header ¶
func (c *ServiceaccountkeysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ServiceaccountkeysListCall) IfNoneMatch ¶
func (c *ServiceaccountkeysListCall) IfNoneMatch(entityTag string) *ServiceaccountkeysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ServiceaccountkeysService ¶
type ServiceaccountkeysService struct {
	// contains filtered or unexported fields
}
func NewServiceaccountkeysService ¶
func NewServiceaccountkeysService(s *Service) *ServiceaccountkeysService
func (*ServiceaccountkeysService) Delete ¶
func (r *ServiceaccountkeysService) Delete(enterpriseId string, keyId string) *ServiceaccountkeysDeleteCall

Delete: Removes and invalidates the specified credentials for the service account associated with this enterprise. The calling service account must have been retrieved by calling Enterprises.GetServiceAccount and must have been set as the enterprise service account by calling Enterprises.SetAccount.

- enterpriseId: The ID of the enterprise. - keyId: The ID of the key.

func (*ServiceaccountkeysService) Insert ¶
func (r *ServiceaccountkeysService) Insert(enterpriseId string, serviceaccountkey *ServiceAccountKey) *ServiceaccountkeysInsertCall

Insert: Generates new credentials for the service account associated with this enterprise. The calling service account must have been retrieved by calling Enterprises.GetServiceAccount and must have been set as the enterprise service account by calling Enterprises.SetAccount. Only the type of the key should be populated in the resource to be inserted.

- enterpriseId: The ID of the enterprise.

func (*ServiceaccountkeysService) List ¶
func (r *ServiceaccountkeysService) List(enterpriseId string) *ServiceaccountkeysListCall

List: Lists all active credentials for the service account associated with this enterprise. Only the ID and key type are returned. The calling service account must have been retrieved by calling Enterprises.GetServiceAccount and must have been set as the enterprise service account by calling Enterprises.SetAccount.

- enterpriseId: The ID of the enterprise.

type SignupInfo ¶
type SignupInfo struct {
	// CompletionToken: An opaque token that will be required, along with the
	// Enterprise Token, for obtaining the enterprise resource from CompleteSignup.
	CompletionToken string `json:"completionToken,omitempty"`
	// Kind: Deprecated.
	Kind string `json:"kind,omitempty"`
	// Url: A URL under which the Admin can sign up for an enterprise. The page
	// pointed to cannot be rendered in an iframe.
	Url string `json:"url,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CompletionToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CompletionToken") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SignupInfo: A resource returned by the GenerateSignupUrl API, which contains the Signup URL and Completion Token.

func (SignupInfo) MarshalJSON ¶
func (s SignupInfo) MarshalJSON() ([]byte, error)
type StoreCluster ¶
type StoreCluster struct {
	// Id: Unique ID of this cluster. Assigned by the server. Immutable once
	// assigned.
	Id string `json:"id,omitempty"`
	// Name: Ordered list of localized strings giving the name of this page. The
	// text displayed is the one that best matches the user locale, or the first
	// entry if there is no good match. There needs to be at least one entry.
	Name []*LocalizedText `json:"name,omitempty"`
	// OrderInPage: String (US-ASCII only) used to determine order of this cluster
	// within the parent page's elements. Page elements are sorted in lexicographic
	// order of this field. Duplicated values are allowed, but ordering between
	// elements with duplicate order is undefined. The value of this field is never
	// visible to a user, it is used solely for the purpose of defining an
	// ordering. Maximum length is 256 characters.
	OrderInPage string `json:"orderInPage,omitempty"`
	// ProductId: List of products in the order they are displayed in the cluster.
	// There should not be duplicates within a cluster.
	ProductId []string `json:"productId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

StoreCluster: Definition of a managed Google Play store cluster, a list of products displayed as part of a store page.

func (StoreCluster) MarshalJSON ¶
func (s StoreCluster) MarshalJSON() ([]byte, error)
type StoreLayout ¶
type StoreLayout struct {
	// HomepageId: The ID of the store page to be used as the homepage. The
	// homepage is the first page shown in the managed Google Play Store. Not
	// specifying a homepage is equivalent to setting the store layout type to
	// "basic".
	HomepageId string `json:"homepageId,omitempty"`
	// StoreLayoutType: The store layout type. By default, this value is set to
	// "basic" if the homepageId field is not set, and to "custom" otherwise. If
	// set to "basic", the layout will consist of all approved apps that have been
	// whitelisted for the user.
	//
	// Possible values:
	//   "unknown"
	//   "basic"
	//   "custom"
	StoreLayoutType string `json:"storeLayoutType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "HomepageId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "HomepageId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StoreLayout: General setting for the managed Google Play store layout, currently only specifying the page to display the first time the store is opened.

func (StoreLayout) MarshalJSON ¶
func (s StoreLayout) MarshalJSON() ([]byte, error)
type StoreLayoutClustersListResponse ¶
type StoreLayoutClustersListResponse struct {
	// Cluster: A store cluster of an enterprise.
	Cluster []*StoreCluster `json:"cluster,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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
func (StoreLayoutClustersListResponse) MarshalJSON ¶
func (s StoreLayoutClustersListResponse) MarshalJSON() ([]byte, error)
type StoreLayoutPagesListResponse ¶
type StoreLayoutPagesListResponse struct {
	// Page: A store page of an enterprise.
	Page []*StorePage `json:"page,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Page") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Page") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (StoreLayoutPagesListResponse) MarshalJSON ¶
func (s StoreLayoutPagesListResponse) MarshalJSON() ([]byte, error)
type StorePage ¶
type StorePage struct {
	// Id: Unique ID of this page. Assigned by the server. Immutable once assigned.
	Id string `json:"id,omitempty"`
	// Link: Ordered list of pages a user should be able to reach from this page.
	// The list can't include this page. It is recommended that the basic pages are
	// created first, before adding the links between pages. The API doesn't verify
	// that the pages exist or the pages are reachable.
	Link []string `json:"link,omitempty"`
	// Name: Ordered list of localized strings giving the name of this page. The
	// text displayed is the one that best matches the user locale, or the first
	// entry if there is no good match. There needs to be at least one entry.
	Name []*LocalizedText `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

StorePage: Definition of a managed Google Play store page, made of a localized name and links to other pages. A page also contains clusters defined as a subcollection.

func (StorePage) MarshalJSON ¶
func (s StorePage) MarshalJSON() ([]byte, error)
type StorelayoutclustersDeleteCall ¶
type StorelayoutclustersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutclustersDeleteCall) Context ¶
func (c *StorelayoutclustersDeleteCall) Context(ctx context.Context) *StorelayoutclustersDeleteCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutclustersDeleteCall) Do ¶
func (c *StorelayoutclustersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.storelayoutclusters.delete" call.

func (*StorelayoutclustersDeleteCall) Fields ¶
func (c *StorelayoutclustersDeleteCall) Fields(s ...googleapi.Field) *StorelayoutclustersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutclustersDeleteCall) Header ¶
func (c *StorelayoutclustersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type StorelayoutclustersGetCall ¶
type StorelayoutclustersGetCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutclustersGetCall) Context ¶
func (c *StorelayoutclustersGetCall) Context(ctx context.Context) *StorelayoutclustersGetCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutclustersGetCall) Do ¶
func (c *StorelayoutclustersGetCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)

Do executes the "androidenterprise.storelayoutclusters.get" call. Any non-2xx status code is an error. Response headers are in either *StoreCluster.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutclustersGetCall) Fields ¶
func (c *StorelayoutclustersGetCall) Fields(s ...googleapi.Field) *StorelayoutclustersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutclustersGetCall) Header ¶
func (c *StorelayoutclustersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*StorelayoutclustersGetCall) IfNoneMatch ¶
func (c *StorelayoutclustersGetCall) IfNoneMatch(entityTag string) *StorelayoutclustersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type StorelayoutclustersInsertCall ¶
type StorelayoutclustersInsertCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutclustersInsertCall) Context ¶
func (c *StorelayoutclustersInsertCall) Context(ctx context.Context) *StorelayoutclustersInsertCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutclustersInsertCall) Do ¶
func (c *StorelayoutclustersInsertCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)

Do executes the "androidenterprise.storelayoutclusters.insert" call. Any non-2xx status code is an error. Response headers are in either *StoreCluster.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutclustersInsertCall) Fields ¶
func (c *StorelayoutclustersInsertCall) Fields(s ...googleapi.Field) *StorelayoutclustersInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutclustersInsertCall) Header ¶
func (c *StorelayoutclustersInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type StorelayoutclustersListCall ¶
type StorelayoutclustersListCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutclustersListCall) Context ¶
func (c *StorelayoutclustersListCall) Context(ctx context.Context) *StorelayoutclustersListCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutclustersListCall) Do ¶
func (c *StorelayoutclustersListCall) Do(opts ...googleapi.CallOption) (*StoreLayoutClustersListResponse, error)

Do executes the "androidenterprise.storelayoutclusters.list" call. Any non-2xx status code is an error. Response headers are in either *StoreLayoutClustersListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutclustersListCall) Fields ¶
func (c *StorelayoutclustersListCall) Fields(s ...googleapi.Field) *StorelayoutclustersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutclustersListCall) Header ¶
func (c *StorelayoutclustersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*StorelayoutclustersListCall) IfNoneMatch ¶
func (c *StorelayoutclustersListCall) IfNoneMatch(entityTag string) *StorelayoutclustersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type StorelayoutclustersService ¶
type StorelayoutclustersService struct {
	// contains filtered or unexported fields
}
func NewStorelayoutclustersService ¶
func NewStorelayoutclustersService(s *Service) *StorelayoutclustersService
func (*StorelayoutclustersService) Delete ¶
func (r *StorelayoutclustersService) Delete(enterpriseId string, pageId string, clusterId string) *StorelayoutclustersDeleteCall

Delete: Deletes a cluster.

- clusterId: The ID of the cluster. - enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutclustersService) Get ¶
func (r *StorelayoutclustersService) Get(enterpriseId string, pageId string, clusterId string) *StorelayoutclustersGetCall

Get: Retrieves details of a cluster.

- clusterId: The ID of the cluster. - enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutclustersService) Insert ¶
func (r *StorelayoutclustersService) Insert(enterpriseId string, pageId string, storecluster *StoreCluster) *StorelayoutclustersInsertCall

Insert: Inserts a new cluster in a page.

- enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutclustersService) List ¶
func (r *StorelayoutclustersService) List(enterpriseId string, pageId string) *StorelayoutclustersListCall

List: Retrieves the details of all clusters on the specified page.

- enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutclustersService) Update ¶
func (r *StorelayoutclustersService) Update(enterpriseId string, pageId string, clusterId string, storecluster *StoreCluster) *StorelayoutclustersUpdateCall

Update: Updates a cluster.

- clusterId: The ID of the cluster. - enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

type StorelayoutclustersUpdateCall ¶
type StorelayoutclustersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutclustersUpdateCall) Context ¶
func (c *StorelayoutclustersUpdateCall) Context(ctx context.Context) *StorelayoutclustersUpdateCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutclustersUpdateCall) Do ¶
func (c *StorelayoutclustersUpdateCall) Do(opts ...googleapi.CallOption) (*StoreCluster, error)

Do executes the "androidenterprise.storelayoutclusters.update" call. Any non-2xx status code is an error. Response headers are in either *StoreCluster.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutclustersUpdateCall) Fields ¶
func (c *StorelayoutclustersUpdateCall) Fields(s ...googleapi.Field) *StorelayoutclustersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutclustersUpdateCall) Header ¶
func (c *StorelayoutclustersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type StorelayoutpagesDeleteCall ¶
type StorelayoutpagesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutpagesDeleteCall) Context ¶
func (c *StorelayoutpagesDeleteCall) Context(ctx context.Context) *StorelayoutpagesDeleteCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutpagesDeleteCall) Do ¶
func (c *StorelayoutpagesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.storelayoutpages.delete" call.

func (*StorelayoutpagesDeleteCall) Fields ¶
func (c *StorelayoutpagesDeleteCall) Fields(s ...googleapi.Field) *StorelayoutpagesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutpagesDeleteCall) Header ¶
func (c *StorelayoutpagesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type StorelayoutpagesGetCall ¶
type StorelayoutpagesGetCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutpagesGetCall) Context ¶
func (c *StorelayoutpagesGetCall) Context(ctx context.Context) *StorelayoutpagesGetCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutpagesGetCall) Do ¶
func (c *StorelayoutpagesGetCall) Do(opts ...googleapi.CallOption) (*StorePage, error)

Do executes the "androidenterprise.storelayoutpages.get" call. Any non-2xx status code is an error. Response headers are in either *StorePage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutpagesGetCall) Fields ¶
func (c *StorelayoutpagesGetCall) Fields(s ...googleapi.Field) *StorelayoutpagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutpagesGetCall) Header ¶
func (c *StorelayoutpagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*StorelayoutpagesGetCall) IfNoneMatch ¶
func (c *StorelayoutpagesGetCall) IfNoneMatch(entityTag string) *StorelayoutpagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type StorelayoutpagesInsertCall ¶
type StorelayoutpagesInsertCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutpagesInsertCall) Context ¶
func (c *StorelayoutpagesInsertCall) Context(ctx context.Context) *StorelayoutpagesInsertCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutpagesInsertCall) Do ¶
func (c *StorelayoutpagesInsertCall) Do(opts ...googleapi.CallOption) (*StorePage, error)

Do executes the "androidenterprise.storelayoutpages.insert" call. Any non-2xx status code is an error. Response headers are in either *StorePage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutpagesInsertCall) Fields ¶
func (c *StorelayoutpagesInsertCall) Fields(s ...googleapi.Field) *StorelayoutpagesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutpagesInsertCall) Header ¶
func (c *StorelayoutpagesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type StorelayoutpagesListCall ¶
type StorelayoutpagesListCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutpagesListCall) Context ¶
func (c *StorelayoutpagesListCall) Context(ctx context.Context) *StorelayoutpagesListCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutpagesListCall) Do ¶
func (c *StorelayoutpagesListCall) Do(opts ...googleapi.CallOption) (*StoreLayoutPagesListResponse, error)

Do executes the "androidenterprise.storelayoutpages.list" call. Any non-2xx status code is an error. Response headers are in either *StoreLayoutPagesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutpagesListCall) Fields ¶
func (c *StorelayoutpagesListCall) Fields(s ...googleapi.Field) *StorelayoutpagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutpagesListCall) Header ¶
func (c *StorelayoutpagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*StorelayoutpagesListCall) IfNoneMatch ¶
func (c *StorelayoutpagesListCall) IfNoneMatch(entityTag string) *StorelayoutpagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type StorelayoutpagesService ¶
type StorelayoutpagesService struct {
	// contains filtered or unexported fields
}
func NewStorelayoutpagesService ¶
func NewStorelayoutpagesService(s *Service) *StorelayoutpagesService
func (*StorelayoutpagesService) Delete ¶
func (r *StorelayoutpagesService) Delete(enterpriseId string, pageId string) *StorelayoutpagesDeleteCall

Delete: Deletes a store page.

- enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutpagesService) Get ¶
func (r *StorelayoutpagesService) Get(enterpriseId string, pageId string) *StorelayoutpagesGetCall

Get: Retrieves details of a store page.

- enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

func (*StorelayoutpagesService) Insert ¶
func (r *StorelayoutpagesService) Insert(enterpriseId string, storepage *StorePage) *StorelayoutpagesInsertCall

Insert: Inserts a new store page.

- enterpriseId: The ID of the enterprise.

func (*StorelayoutpagesService) List ¶
func (r *StorelayoutpagesService) List(enterpriseId string) *StorelayoutpagesListCall

List: Retrieves the details of all pages in the store.

- enterpriseId: The ID of the enterprise.

func (*StorelayoutpagesService) Update ¶
func (r *StorelayoutpagesService) Update(enterpriseId string, pageId string, storepage *StorePage) *StorelayoutpagesUpdateCall

Update: Updates the content of a store page.

- enterpriseId: The ID of the enterprise. - pageId: The ID of the page.

type StorelayoutpagesUpdateCall ¶
type StorelayoutpagesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*StorelayoutpagesUpdateCall) Context ¶
func (c *StorelayoutpagesUpdateCall) Context(ctx context.Context) *StorelayoutpagesUpdateCall

Context sets the context to be used in this call's Do method.

func (*StorelayoutpagesUpdateCall) Do ¶
func (c *StorelayoutpagesUpdateCall) Do(opts ...googleapi.CallOption) (*StorePage, error)

Do executes the "androidenterprise.storelayoutpages.update" call. Any non-2xx status code is an error. Response headers are in either *StorePage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*StorelayoutpagesUpdateCall) Fields ¶
func (c *StorelayoutpagesUpdateCall) Fields(s ...googleapi.Field) *StorelayoutpagesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*StorelayoutpagesUpdateCall) Header ¶
func (c *StorelayoutpagesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type TokenPagination ¶
type TokenPagination struct {
	// NextPageToken: Tokens to pass to the standard list field 'page_token'.
	// Whenever available, tokens are preferred over manipulating start_index.
	NextPageToken     string `json:"nextPageToken,omitempty"`
	PreviousPageToken string `json:"previousPageToken,omitempty"`
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

TokenPagination: Pagination information returned by a List operation when token pagination is enabled. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned. When using token pagination, clients should use the next/previous token to get another page of the result. The presence or absence of next/previous token indicates whether a next/previous page is available and provides a mean of accessing this page. ListRequest.page_token should be set to either next_page_token or previous_page_token to access another page.

func (TokenPagination) MarshalJSON ¶
func (s TokenPagination) MarshalJSON() ([]byte, error)
type TrackInfo ¶
type TrackInfo struct {
	// TrackAlias: A modifiable name for a track. This is the visible name in the
	// play developer console.
	TrackAlias string `json:"trackAlias,omitempty"`
	// TrackId: Unmodifiable, unique track identifier. This identifier is the
	// releaseTrackId in the url of the play developer console page that displays
	// the track information.
	TrackId string `json:"trackId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TrackAlias") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TrackAlias") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrackInfo: Id to name association of a track.

func (TrackInfo) MarshalJSON ¶
func (s TrackInfo) MarshalJSON() ([]byte, error)
type User ¶
type User struct {
	// AccountIdentifier: A unique identifier you create for this user, such as
	// "user342" or "asset#44418". Do not use personally identifiable information
	// (PII) for this property. Must always be set for EMM-managed users. Not set
	// for Google-managed users.
	AccountIdentifier string `json:"accountIdentifier,omitempty"`
	// AccountType: The type of account that this user represents. A userAccount
	// can be installed on multiple devices, but a deviceAccount is specific to a
	// single device. An EMM-managed user (emmManaged) can be either type
	// (userAccount, deviceAccount), but a Google-managed user (googleManaged) is
	// always a userAccount.
	//
	// Possible values:
	//   "deviceAccount"
	//   "userAccount"
	AccountType string `json:"accountType,omitempty"`
	// DisplayName: The name that will appear in user interfaces. Setting this
	// property is optional when creating EMM-managed users. If you do set this
	// property, use something generic about the organization (such as "Example,
	// Inc.") or your name (as EMM). Not used for Google-managed user accounts.
	// @mutable androidenterprise.users.update
	DisplayName string `json:"displayName,omitempty"`
	// Id: The unique ID for the user.
	Id string `json:"id,omitempty"`
	// ManagementType: The entity that manages the user. With googleManaged users,
	// the source of truth is Google so EMMs have to make sure a Google Account
	// exists for the user. With emmManaged users, the EMM is in charge.
	//
	// Possible values:
	//   "googleManaged"
	//   "emmManaged"
	ManagementType string `json:"managementType,omitempty"`
	// PrimaryEmail: The user's primary email address, for example,
	// "jsmith@example.com". Will always be set for Google managed users and not
	// set for EMM managed users.
	PrimaryEmail string `json:"primaryEmail,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountIdentifier") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountIdentifier") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

User: A Users resource represents an account associated with an enterprise. The account may be specific to a device or to an individual user (who can then use the account across multiple devices). The account may provide access to managed Google Play only, or to other Google services, depending on the identity model: - The Google managed domain identity model requires synchronization to Google account sources (via primaryEmail). - The managed Google Play Accounts identity model provides a dynamic means for enterprises to create user or device accounts as needed. These accounts provide access to managed Google Play.

func (User) MarshalJSON ¶
func (s User) MarshalJSON() ([]byte, error)
type UsersDeleteCall ¶
type UsersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersDeleteCall) Context ¶
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersDeleteCall) Do ¶
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.users.delete" call.

func (*UsersDeleteCall) Fields ¶
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersDeleteCall) Header ¶
func (c *UsersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersGenerateAuthenticationTokenCall ¶
type UsersGenerateAuthenticationTokenCall struct {
	// contains filtered or unexported fields
}
func (*UsersGenerateAuthenticationTokenCall) Context ¶
func (c *UsersGenerateAuthenticationTokenCall) Context(ctx context.Context) *UsersGenerateAuthenticationTokenCall

Context sets the context to be used in this call's Do method.

func (*UsersGenerateAuthenticationTokenCall) Do ¶
func (c *UsersGenerateAuthenticationTokenCall) Do(opts ...googleapi.CallOption) (*AuthenticationToken, error)

Do executes the "androidenterprise.users.generateAuthenticationToken" call. Any non-2xx status code is an error. Response headers are in either *AuthenticationToken.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersGenerateAuthenticationTokenCall) Fields ¶
func (c *UsersGenerateAuthenticationTokenCall) Fields(s ...googleapi.Field) *UsersGenerateAuthenticationTokenCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersGenerateAuthenticationTokenCall) Header ¶
func (c *UsersGenerateAuthenticationTokenCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersGetAvailableProductSetCall ¶
type UsersGetAvailableProductSetCall struct {
	// contains filtered or unexported fields
}
func (*UsersGetAvailableProductSetCall) Context ¶
func (c *UsersGetAvailableProductSetCall) Context(ctx context.Context) *UsersGetAvailableProductSetCall

Context sets the context to be used in this call's Do method.

func (*UsersGetAvailableProductSetCall) Do ¶
func (c *UsersGetAvailableProductSetCall) Do(opts ...googleapi.CallOption) (*ProductSet, error)

Do executes the "androidenterprise.users.getAvailableProductSet" call. Any non-2xx status code is an error. Response headers are in either *ProductSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersGetAvailableProductSetCall) Fields ¶
func (c *UsersGetAvailableProductSetCall) Fields(s ...googleapi.Field) *UsersGetAvailableProductSetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersGetAvailableProductSetCall) Header ¶
func (c *UsersGetAvailableProductSetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersGetAvailableProductSetCall) IfNoneMatch ¶
func (c *UsersGetAvailableProductSetCall) IfNoneMatch(entityTag string) *UsersGetAvailableProductSetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type UsersGetCall ¶
type UsersGetCall struct {
	// contains filtered or unexported fields
}
func (*UsersGetCall) Context ¶
func (c *UsersGetCall) Context(ctx context.Context) *UsersGetCall

Context sets the context to be used in this call's Do method.

func (*UsersGetCall) Do ¶
func (c *UsersGetCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "androidenterprise.users.get" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersGetCall) Fields ¶
func (c *UsersGetCall) Fields(s ...googleapi.Field) *UsersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersGetCall) Header ¶
func (c *UsersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersGetCall) IfNoneMatch ¶
func (c *UsersGetCall) IfNoneMatch(entityTag string) *UsersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type UsersInsertCall ¶
type UsersInsertCall struct {
	// contains filtered or unexported fields
}
func (*UsersInsertCall) Context ¶
func (c *UsersInsertCall) Context(ctx context.Context) *UsersInsertCall

Context sets the context to be used in this call's Do method.

func (*UsersInsertCall) Do ¶
func (c *UsersInsertCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "androidenterprise.users.insert" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersInsertCall) Fields ¶
func (c *UsersInsertCall) Fields(s ...googleapi.Field) *UsersInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersInsertCall) Header ¶
func (c *UsersInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersListCall ¶
type UsersListCall struct {
	// contains filtered or unexported fields
}
func (*UsersListCall) Context ¶
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall

Context sets the context to be used in this call's Do method.

func (*UsersListCall) Do ¶
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*UsersListResponse, error)

Do executes the "androidenterprise.users.list" call. Any non-2xx status code is an error. Response headers are in either *UsersListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersListCall) Fields ¶
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersListCall) Header ¶
func (c *UsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersListCall) IfNoneMatch ¶
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type UsersListResponse ¶
type UsersListResponse struct {
	// User: A user of an enterprise.
	User []*User `json:"user,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "User") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "User") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (UsersListResponse) MarshalJSON ¶
func (s UsersListResponse) MarshalJSON() ([]byte, error)
type UsersRevokeDeviceAccessCall ¶
type UsersRevokeDeviceAccessCall struct {
	// contains filtered or unexported fields
}
func (*UsersRevokeDeviceAccessCall) Context ¶
func (c *UsersRevokeDeviceAccessCall) Context(ctx context.Context) *UsersRevokeDeviceAccessCall

Context sets the context to be used in this call's Do method.

func (*UsersRevokeDeviceAccessCall) Do ¶
func (c *UsersRevokeDeviceAccessCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.users.revokeDeviceAccess" call.

func (*UsersRevokeDeviceAccessCall) Fields ¶
func (c *UsersRevokeDeviceAccessCall) Fields(s ...googleapi.Field) *UsersRevokeDeviceAccessCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersRevokeDeviceAccessCall) Header ¶
func (c *UsersRevokeDeviceAccessCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersService ¶
type UsersService struct {
	// contains filtered or unexported fields
}
func NewUsersService ¶
func NewUsersService(s *Service) *UsersService
func (*UsersService) Delete ¶
func (r *UsersService) Delete(enterpriseId string, userId string) *UsersDeleteCall

Delete: Deleted an EMM-managed user.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) GenerateAuthenticationToken ¶
func (r *UsersService) GenerateAuthenticationToken(enterpriseId string, userId string) *UsersGenerateAuthenticationTokenCall

GenerateAuthenticationToken: Generates an authentication token which the device policy client can use to provision the given EMM-managed user account on a device. The generated token is single-use and expires after a few minutes. You can provision a maximum of 10 devices per user. This call only works with EMM-managed accounts.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) Get ¶
func (r *UsersService) Get(enterpriseId string, userId string) *UsersGetCall

Get: Retrieves a user's details.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) GetAvailableProductSet ¶
func (r *UsersService) GetAvailableProductSet(enterpriseId string, userId string) *UsersGetAvailableProductSetCall

GetAvailableProductSet: Retrieves the set of products a user is entitled to access. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) Insert ¶
func (r *UsersService) Insert(enterpriseId string, user *User) *UsersInsertCall

Insert: Creates a new EMM-managed user. The Users resource passed in the body of the request should include an accountIdentifier and an accountType. If a corresponding user already exists with the same account identifier, the user will be updated with the resource. In this case only the displayName field can be changed.

- enterpriseId: The ID of the enterprise.

func (*UsersService) List ¶
func (r *UsersService) List(enterpriseId string, email string) *UsersListCall

List: Looks up a user by primary email address. This is only supported for Google-managed users. Lookup of the id is not needed for EMM-managed users because the id is already returned in the result of the Users.insert call.

- email: The exact primary email address of the user to look up. - enterpriseId: The ID of the enterprise.

func (*UsersService) RevokeDeviceAccess ¶
func (r *UsersService) RevokeDeviceAccess(enterpriseId string, userId string) *UsersRevokeDeviceAccessCall

RevokeDeviceAccess: Revokes access to all devices currently provisioned to the user. The user will no longer be able to use the managed Play store on any of their managed devices. This call only works with EMM-managed accounts.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) SetAvailableProductSet ¶
func (r *UsersService) SetAvailableProductSet(enterpriseId string, userId string, productset *ProductSet) *UsersSetAvailableProductSetCall

SetAvailableProductSet: Modifies the set of products that a user is entitled to access (referred to as *whitelisted* products). Only products that are approved or products that were previously approved (products with revoked approval) can be whitelisted. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

func (*UsersService) Update ¶
func (r *UsersService) Update(enterpriseId string, userId string, user *User) *UsersUpdateCall

Update: Updates the details of an EMM-managed user. Can be used with EMM-managed users only (not Google managed users). Pass the new details in the Users resource in the request body. Only the displayName field can be changed. Other fields must either be unset or have the currently active value.

- enterpriseId: The ID of the enterprise. - userId: The ID of the user.

type UsersSetAvailableProductSetCall ¶
type UsersSetAvailableProductSetCall struct {
	// contains filtered or unexported fields
}
func (*UsersSetAvailableProductSetCall) Context ¶
func (c *UsersSetAvailableProductSetCall) Context(ctx context.Context) *UsersSetAvailableProductSetCall

Context sets the context to be used in this call's Do method.

func (*UsersSetAvailableProductSetCall) Do ¶
func (c *UsersSetAvailableProductSetCall) Do(opts ...googleapi.CallOption) (*ProductSet, error)

Do executes the "androidenterprise.users.setAvailableProductSet" call. Any non-2xx status code is an error. Response headers are in either *ProductSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersSetAvailableProductSetCall) Fields ¶
func (c *UsersSetAvailableProductSetCall) Fields(s ...googleapi.Field) *UsersSetAvailableProductSetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersSetAvailableProductSetCall) Header ¶
func (c *UsersSetAvailableProductSetCall) Header() http.Header

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

Do executes the "androidenterprise.users.update" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersUpdateCall) Fields ¶
func (c *UsersUpdateCall) Fields(s ...googleapi.Field) *UsersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersUpdateCall) Header ¶
func (c *UsersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type VariableSet ¶
type VariableSet struct {
	// Placeholder: The placeholder string; defined by EMM.
	Placeholder string `json:"placeholder,omitempty"`
	// UserValue: The value of the placeholder, specific to the user.
	UserValue string `json:"userValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Placeholder") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Placeholder") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VariableSet: A variable set is a key-value pair of EMM-provided placeholders and its corresponding value, which is attributed to a user. For example, $FIRSTNAME could be a placeholder, and its value could be Alice. Placeholders should start with a '$' sign and should be alphanumeric only.

func (VariableSet) MarshalJSON ¶
func (s VariableSet) MarshalJSON() ([]byte, error)
type WebApp ¶
type WebApp struct {
	// DisplayMode: The display mode of the web app. Possible values include: -
	// "minimalUi", the device's status bar, navigation bar, the app's URL, and a
	// refresh button are visible when the app is open. For HTTP URLs, you can only
	// select this option. - "standalone", the device's status bar and navigation
	// bar are visible when the app is open. - "fullScreen", the app opens in full
	// screen mode, hiding the device's status and navigation bars. All browser UI
	// elements, page URL, system status bar and back button are not visible, and
	// the web app takes up the entirety of the available display area.
	//
	// Possible values:
	//   "displayModeUnspecified"
	//   "minimalUi" - Opens the web app with a minimal set of browser UI elements
	// for controlling navigation and viewing the page URL.
	//   "standalone" - Opens the web app to look and feel like a standalone native
	// application. The browser UI elements and page URL are not visible, however
	// the system status bar and back button are visible.
	//   "fullScreen" - Opens the web app in full screen without any visible
	// controls. The browser UI elements, page URL, system status bar and back
	// button are not visible, and the web app takes up the entirety of the
	// available display area.
	DisplayMode string `json:"displayMode,omitempty"`
	// Icons: A list of icons representing this website. If absent, a default icon
	// (for create) or the current icon (for update) will be used.
	Icons []*WebAppIcon `json:"icons,omitempty"`
	// IsPublished: A flag whether the app has been published to the Play store
	// yet.
	IsPublished bool `json:"isPublished,omitempty"`
	// StartUrl: The start URL, i.e. the URL that should load when the user opens
	// the application.
	StartUrl string `json:"startUrl,omitempty"`
	// Title: The title of the web app as displayed to the user (e.g., amongst a
	// list of other applications, or as a label for an icon).
	Title string `json:"title,omitempty"`
	// VersionCode: The current version of the app. Note that the version can
	// automatically increase during the lifetime of the web app, while Google does
	// internal housekeeping to keep the web app up-to-date.
	VersionCode int64 `json:"versionCode,omitempty,string"`
	// WebAppId: The ID of the application. A string of the form "app:<package
	// name>" where the package name always starts with the prefix
	// "com.google.enterprise.webapp." followed by a random id.
	WebAppId string `json:"webAppId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DisplayMode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayMode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebApp: A WebApps resource represents a web app created for an enterprise. Web apps are published to managed Google Play and can be distributed like other Android apps. On a user's device, a web app opens its specified URL.

func (WebApp) MarshalJSON ¶
func (s WebApp) MarshalJSON() ([]byte, error)
type WebAppIcon ¶
type WebAppIcon struct {
	// ImageData: The actual bytes of the image in a base64url encoded string (c.f.
	// RFC4648, section 5 "Base 64 Encoding with URL and Filename Safe Alphabet").
	// - The image type can be png or jpg. - The image should ideally be square. -
	// The image should ideally have a size of 512x512.
	ImageData string `json:"imageData,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ImageData") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ImageData") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebAppIcon: Icon for a web app.

func (WebAppIcon) MarshalJSON ¶
func (s WebAppIcon) MarshalJSON() ([]byte, error)
type WebAppsListResponse ¶
type WebAppsListResponse struct {
	// WebApp: The manifest describing a web app.
	WebApp []*WebApp `json:"webApp,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "WebApp") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "WebApp") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (WebAppsListResponse) MarshalJSON ¶
func (s WebAppsListResponse) MarshalJSON() ([]byte, error)
type WebappsDeleteCall ¶
type WebappsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*WebappsDeleteCall) Context ¶
func (c *WebappsDeleteCall) Context(ctx context.Context) *WebappsDeleteCall

Context sets the context to be used in this call's Do method.

func (*WebappsDeleteCall) Do ¶
func (c *WebappsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidenterprise.webapps.delete" call.

func (*WebappsDeleteCall) Fields ¶
func (c *WebappsDeleteCall) Fields(s ...googleapi.Field) *WebappsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*WebappsDeleteCall) Header ¶
func (c *WebappsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type WebappsGetCall ¶
type WebappsGetCall struct {
	// contains filtered or unexported fields
}
func (*WebappsGetCall) Context ¶
func (c *WebappsGetCall) Context(ctx context.Context) *WebappsGetCall

Context sets the context to be used in this call's Do method.

func (*WebappsGetCall) Do ¶
func (c *WebappsGetCall) Do(opts ...googleapi.CallOption) (*WebApp, error)

Do executes the "androidenterprise.webapps.get" call. Any non-2xx status code is an error. Response headers are in either *WebApp.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*WebappsGetCall) Fields ¶
func (c *WebappsGetCall) Fields(s ...googleapi.Field) *WebappsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*WebappsGetCall) Header ¶
func (c *WebappsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*WebappsGetCall) IfNoneMatch ¶
func (c *WebappsGetCall) IfNoneMatch(entityTag string) *WebappsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type WebappsInsertCall ¶
type WebappsInsertCall struct {
	// contains filtered or unexported fields
}
func (*WebappsInsertCall) Context ¶
func (c *WebappsInsertCall) Context(ctx context.Context) *WebappsInsertCall

Context sets the context to be used in this call's Do method.

func (*WebappsInsertCall) Do ¶
func (c *WebappsInsertCall) Do(opts ...googleapi.CallOption) (*WebApp, error)

Do executes the "androidenterprise.webapps.insert" call. Any non-2xx status code is an error. Response headers are in either *WebApp.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*WebappsInsertCall) Fields ¶
func (c *WebappsInsertCall) Fields(s ...googleapi.Field) *WebappsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*WebappsInsertCall) Header ¶
func (c *WebappsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type WebappsListCall ¶
type WebappsListCall struct {
	// contains filtered or unexported fields
}
func (*WebappsListCall) Context ¶
func (c *WebappsListCall) Context(ctx context.Context) *WebappsListCall

Context sets the context to be used in this call's Do method.

func (*WebappsListCall) Do ¶
func (c *WebappsListCall) Do(opts ...googleapi.CallOption) (*WebAppsListResponse, error)

Do executes the "androidenterprise.webapps.list" call. Any non-2xx status code is an error. Response headers are in either *WebAppsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*WebappsListCall) Fields ¶
func (c *WebappsListCall) Fields(s ...googleapi.Field) *WebappsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*WebappsListCall) Header ¶
func (c *WebappsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*WebappsListCall) IfNoneMatch ¶
func (c *WebappsListCall) IfNoneMatch(entityTag string) *WebappsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type WebappsService ¶
type WebappsService struct {
	// contains filtered or unexported fields
}
func NewWebappsService ¶
func NewWebappsService(s *Service) *WebappsService
func (*WebappsService) Delete ¶
func (r *WebappsService) Delete(enterpriseId string, webAppId string) *WebappsDeleteCall

Delete: Deletes an existing web app.

- enterpriseId: The ID of the enterprise. - webAppId: The ID of the web app.

func (*WebappsService) Get ¶
func (r *WebappsService) Get(enterpriseId string, webAppId string) *WebappsGetCall

Get: Gets an existing web app.

- enterpriseId: The ID of the enterprise. - webAppId: The ID of the web app.

func (*WebappsService) Insert ¶
func (r *WebappsService) Insert(enterpriseId string, webapp *WebApp) *WebappsInsertCall

Insert: Creates a new web app for the enterprise.

- enterpriseId: The ID of the enterprise.

func (*WebappsService) List ¶
func (r *WebappsService) List(enterpriseId string) *WebappsListCall

List: Retrieves the details of all web apps for a given enterprise.

- enterpriseId: The ID of the enterprise.

func (*WebappsService) Update ¶
func (r *WebappsService) Update(enterpriseId string, webAppId string, webapp *WebApp) *WebappsUpdateCall

Update: Updates an existing web app.

- enterpriseId: The ID of the enterprise. - webAppId: The ID of the web app.

type WebappsUpdateCall ¶
type WebappsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*WebappsUpdateCall) Context ¶
func (c *WebappsUpdateCall) Context(ctx context.Context) *WebappsUpdateCall

Context sets the context to be used in this call's Do method.

func (*WebappsUpdateCall) Do ¶
func (c *WebappsUpdateCall) Do(opts ...googleapi.CallOption) (*WebApp, error)

Do executes the "androidenterprise.webapps.update" call. Any non-2xx status code is an error. Response headers are in either *WebApp.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*WebappsUpdateCall) Fields ¶
func (c *WebappsUpdateCall) Fields(s ...googleapi.Field) *WebappsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*WebappsUpdateCall) Header ¶
func (c *WebappsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

 Source Files ¶
View all Source files
androidenterprise-gen.go
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
