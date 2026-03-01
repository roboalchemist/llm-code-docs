# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/androidpublisher/v3

Title: androidpublisher package - google.golang.org/api/androidpublisher/v3 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/androidpublisher/v3

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
androidpublisher
 
v3
androidpublisher
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 81
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

Package androidpublisher provides access to the Google Play Android Developer API.

For product documentation, see: https://developers.google.com/android-publisher

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/androidpublisher/v3"
...
ctx := context.Background()
androidpublisherService, err := androidpublisher.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

androidpublisherService, err := androidpublisher.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
androidpublisherService, err := androidpublisher.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Abi
func (s Abi) MarshalJSON() ([]byte, error)
type AbiTargeting
func (s AbiTargeting) MarshalJSON() ([]byte, error)
type AcquisitionTargetingRule
func (s AcquisitionTargetingRule) MarshalJSON() ([]byte, error)
type ActivateBasePlanRequest
func (s ActivateBasePlanRequest) MarshalJSON() ([]byte, error)
type ActivateOneTimeProductOfferRequest
func (s ActivateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type ActivatePurchaseOptionRequest
func (s ActivatePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type ActivateSubscriptionOfferRequest
func (s ActivateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type AddTargetingRequest
func (s AddTargetingRequest) MarshalJSON() ([]byte, error)
type AddTargetingResponse
type AllUsers
func (s AllUsers) MarshalJSON() ([]byte, error)
type AndroidSdks
func (s AndroidSdks) MarshalJSON() ([]byte, error)
type Apk
func (s Apk) MarshalJSON() ([]byte, error)
type ApkBinary
func (s ApkBinary) MarshalJSON() ([]byte, error)
type ApkDescription
func (s ApkDescription) MarshalJSON() ([]byte, error)
type ApkSet
func (s ApkSet) MarshalJSON() ([]byte, error)
type ApkTargeting
func (s ApkTargeting) MarshalJSON() ([]byte, error)
type ApksAddExternallyHostedRequest
func (s ApksAddExternallyHostedRequest) MarshalJSON() ([]byte, error)
type ApksAddExternallyHostedResponse
func (s ApksAddExternallyHostedResponse) MarshalJSON() ([]byte, error)
type ApksListResponse
func (s ApksListResponse) MarshalJSON() ([]byte, error)
type AppDetails
func (s AppDetails) MarshalJSON() ([]byte, error)
type AppEdit
func (s AppEdit) MarshalJSON() ([]byte, error)
type AppRecoveryAction
func (s AppRecoveryAction) MarshalJSON() ([]byte, error)
type AppVersionList
func (s AppVersionList) MarshalJSON() ([]byte, error)
type AppVersionRange
func (s AppVersionRange) MarshalJSON() ([]byte, error)
type ApplicationsDataSafetyCall
func (c *ApplicationsDataSafetyCall) Context(ctx context.Context) *ApplicationsDataSafetyCall
func (c *ApplicationsDataSafetyCall) Do(opts ...googleapi.CallOption) (*SafetyLabelsUpdateResponse, error)
func (c *ApplicationsDataSafetyCall) Fields(s ...googleapi.Field) *ApplicationsDataSafetyCall
func (c *ApplicationsDataSafetyCall) Header() http.Header
type ApplicationsDeviceTierConfigsCreateCall
func (c *ApplicationsDeviceTierConfigsCreateCall) AllowUnknownDevices(allowUnknownDevices bool) *ApplicationsDeviceTierConfigsCreateCall
func (c *ApplicationsDeviceTierConfigsCreateCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsCreateCall
func (c *ApplicationsDeviceTierConfigsCreateCall) Do(opts ...googleapi.CallOption) (*DeviceTierConfig, error)
func (c *ApplicationsDeviceTierConfigsCreateCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsCreateCall
func (c *ApplicationsDeviceTierConfigsCreateCall) Header() http.Header
type ApplicationsDeviceTierConfigsGetCall
func (c *ApplicationsDeviceTierConfigsGetCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsGetCall
func (c *ApplicationsDeviceTierConfigsGetCall) Do(opts ...googleapi.CallOption) (*DeviceTierConfig, error)
func (c *ApplicationsDeviceTierConfigsGetCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsGetCall
func (c *ApplicationsDeviceTierConfigsGetCall) Header() http.Header
func (c *ApplicationsDeviceTierConfigsGetCall) IfNoneMatch(entityTag string) *ApplicationsDeviceTierConfigsGetCall
type ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) Do(opts ...googleapi.CallOption) (*ListDeviceTierConfigsResponse, error)
func (c *ApplicationsDeviceTierConfigsListCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) Header() http.Header
func (c *ApplicationsDeviceTierConfigsListCall) IfNoneMatch(entityTag string) *ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) PageSize(pageSize int64) *ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) PageToken(pageToken string) *ApplicationsDeviceTierConfigsListCall
func (c *ApplicationsDeviceTierConfigsListCall) Pages(ctx context.Context, f func(*ListDeviceTierConfigsResponse) error) error
type ApplicationsDeviceTierConfigsService
func NewApplicationsDeviceTierConfigsService(s *Service) *ApplicationsDeviceTierConfigsService
func (r *ApplicationsDeviceTierConfigsService) Create(packageName string, devicetierconfig *DeviceTierConfig) *ApplicationsDeviceTierConfigsCreateCall
func (r *ApplicationsDeviceTierConfigsService) Get(packageName string, deviceTierConfigId int64) *ApplicationsDeviceTierConfigsGetCall
func (r *ApplicationsDeviceTierConfigsService) List(packageName string) *ApplicationsDeviceTierConfigsListCall
type ApplicationsService
func NewApplicationsService(s *Service) *ApplicationsService
func (r *ApplicationsService) DataSafety(packageName string, safetylabelsupdaterequest *SafetyLabelsUpdateRequest) *ApplicationsDataSafetyCall
type ApprecoveryAddTargetingCall
func (c *ApprecoveryAddTargetingCall) Context(ctx context.Context) *ApprecoveryAddTargetingCall
func (c *ApprecoveryAddTargetingCall) Do(opts ...googleapi.CallOption) (*AddTargetingResponse, error)
func (c *ApprecoveryAddTargetingCall) Fields(s ...googleapi.Field) *ApprecoveryAddTargetingCall
func (c *ApprecoveryAddTargetingCall) Header() http.Header
type ApprecoveryCancelCall
func (c *ApprecoveryCancelCall) Context(ctx context.Context) *ApprecoveryCancelCall
func (c *ApprecoveryCancelCall) Do(opts ...googleapi.CallOption) (*CancelAppRecoveryResponse, error)
func (c *ApprecoveryCancelCall) Fields(s ...googleapi.Field) *ApprecoveryCancelCall
func (c *ApprecoveryCancelCall) Header() http.Header
type ApprecoveryCreateCall
func (c *ApprecoveryCreateCall) Context(ctx context.Context) *ApprecoveryCreateCall
func (c *ApprecoveryCreateCall) Do(opts ...googleapi.CallOption) (*AppRecoveryAction, error)
func (c *ApprecoveryCreateCall) Fields(s ...googleapi.Field) *ApprecoveryCreateCall
func (c *ApprecoveryCreateCall) Header() http.Header
type ApprecoveryDeployCall
func (c *ApprecoveryDeployCall) Context(ctx context.Context) *ApprecoveryDeployCall
func (c *ApprecoveryDeployCall) Do(opts ...googleapi.CallOption) (*DeployAppRecoveryResponse, error)
func (c *ApprecoveryDeployCall) Fields(s ...googleapi.Field) *ApprecoveryDeployCall
func (c *ApprecoveryDeployCall) Header() http.Header
type ApprecoveryListCall
func (c *ApprecoveryListCall) Context(ctx context.Context) *ApprecoveryListCall
func (c *ApprecoveryListCall) Do(opts ...googleapi.CallOption) (*ListAppRecoveriesResponse, error)
func (c *ApprecoveryListCall) Fields(s ...googleapi.Field) *ApprecoveryListCall
func (c *ApprecoveryListCall) Header() http.Header
func (c *ApprecoveryListCall) IfNoneMatch(entityTag string) *ApprecoveryListCall
func (c *ApprecoveryListCall) VersionCode(versionCode int64) *ApprecoveryListCall
type ApprecoveryService
func NewApprecoveryService(s *Service) *ApprecoveryService
func (r *ApprecoveryService) AddTargeting(packageName string, appRecoveryId int64, ...) *ApprecoveryAddTargetingCall
func (r *ApprecoveryService) Cancel(packageName string, appRecoveryId int64, ...) *ApprecoveryCancelCall
func (r *ApprecoveryService) Create(packageName string, ...) *ApprecoveryCreateCall
func (r *ApprecoveryService) Deploy(packageName string, appRecoveryId int64, ...) *ApprecoveryDeployCall
func (r *ApprecoveryService) List(packageName string) *ApprecoveryListCall
type ArchiveSubscriptionRequest
type AssetModuleMetadata
func (s AssetModuleMetadata) MarshalJSON() ([]byte, error)
type AssetSliceSet
func (s AssetSliceSet) MarshalJSON() ([]byte, error)
type AutoRenewingBasePlanType
func (s AutoRenewingBasePlanType) MarshalJSON() ([]byte, error)
type AutoRenewingPlan
func (s AutoRenewingPlan) MarshalJSON() ([]byte, error)
type BaseDetails
type BasePlan
func (s BasePlan) MarshalJSON() ([]byte, error)
type BasePriceOfferPhase
type BatchDeleteOneTimeProductOffersRequest
func (s BatchDeleteOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchDeleteOneTimeProductsRequest
func (s BatchDeleteOneTimeProductsRequest) MarshalJSON() ([]byte, error)
type BatchDeletePurchaseOptionsRequest
func (s BatchDeletePurchaseOptionsRequest) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductOffersRequest
func (s BatchGetOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductOffersResponse
func (s BatchGetOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductsResponse
func (s BatchGetOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type BatchGetOrdersResponse
func (s BatchGetOrdersResponse) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionOffersRequest
func (s BatchGetSubscriptionOffersRequest) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionOffersResponse
func (s BatchGetSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionsResponse
func (s BatchGetSubscriptionsResponse) MarshalJSON() ([]byte, error)
type BatchMigrateBasePlanPricesRequest
func (s BatchMigrateBasePlanPricesRequest) MarshalJSON() ([]byte, error)
type BatchMigrateBasePlanPricesResponse
func (s BatchMigrateBasePlanPricesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateBasePlanStatesRequest
func (s BatchUpdateBasePlanStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateBasePlanStatesResponse
func (s BatchUpdateBasePlanStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOfferStatesRequest
func (s BatchUpdateOneTimeProductOfferStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOfferStatesResponse
func (s BatchUpdateOneTimeProductOfferStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOffersRequest
func (s BatchUpdateOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOffersResponse
func (s BatchUpdateOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductsRequest
func (s BatchUpdateOneTimeProductsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductsResponse
func (s BatchUpdateOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type BatchUpdatePurchaseOptionStatesRequest
func (s BatchUpdatePurchaseOptionStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdatePurchaseOptionStatesResponse
func (s BatchUpdatePurchaseOptionStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOfferStatesRequest
func (s BatchUpdateSubscriptionOfferStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOfferStatesResponse
func (s BatchUpdateSubscriptionOfferStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOffersRequest
func (s BatchUpdateSubscriptionOffersRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOffersResponse
func (s BatchUpdateSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionsRequest
func (s BatchUpdateSubscriptionsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionsResponse
func (s BatchUpdateSubscriptionsResponse) MarshalJSON() ([]byte, error)
type Bundle
func (s Bundle) MarshalJSON() ([]byte, error)
type BundlesListResponse
func (s BundlesListResponse) MarshalJSON() ([]byte, error)
type BuyerAddress
func (s BuyerAddress) MarshalJSON() ([]byte, error)
type CancelAppRecoveryRequest
type CancelAppRecoveryResponse
type CancelOneTimeProductOfferRequest
func (s CancelOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type CancelSubscriptionPurchaseRequest
func (s CancelSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type CancelSubscriptionPurchaseResponse
type CancelSurveyResult
func (s CancelSurveyResult) MarshalJSON() ([]byte, error)
type CanceledStateContext
func (s CanceledStateContext) MarshalJSON() ([]byte, error)
type CancellationContext
func (s CancellationContext) MarshalJSON() ([]byte, error)
type CancellationEvent
func (s CancellationEvent) MarshalJSON() ([]byte, error)
type Comment
func (s Comment) MarshalJSON() ([]byte, error)
type ConvertRegionPricesRequest
func (s ConvertRegionPricesRequest) MarshalJSON() ([]byte, error)
type ConvertRegionPricesResponse
func (s ConvertRegionPricesResponse) MarshalJSON() ([]byte, error)
type ConvertedOtherRegionsPrice
func (s ConvertedOtherRegionsPrice) MarshalJSON() ([]byte, error)
type ConvertedRegionPrice
func (s ConvertedRegionPrice) MarshalJSON() ([]byte, error)
type CountryTargeting
func (s CountryTargeting) MarshalJSON() ([]byte, error)
type CreateDraftAppRecoveryRequest
func (s CreateDraftAppRecoveryRequest) MarshalJSON() ([]byte, error)
type DeactivateBasePlanRequest
func (s DeactivateBasePlanRequest) MarshalJSON() ([]byte, error)
type DeactivateOneTimeProductOfferRequest
func (s DeactivateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type DeactivatePurchaseOptionRequest
func (s DeactivatePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type DeactivateSubscriptionOfferRequest
func (s DeactivateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type DeferSubscriptionPurchaseRequest
func (s DeferSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type DeferSubscriptionPurchaseResponse
func (s DeferSubscriptionPurchaseResponse) MarshalJSON() ([]byte, error)
type DeferralContext
func (s DeferralContext) MarshalJSON() ([]byte, error)
type DeferredItemRemoval
type DeferredItemReplacement
func (s DeferredItemReplacement) MarshalJSON() ([]byte, error)
type DeleteOneTimeProductOfferRequest
func (s DeleteOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type DeleteOneTimeProductRequest
func (s DeleteOneTimeProductRequest) MarshalJSON() ([]byte, error)
type DeletePurchaseOptionRequest
func (s DeletePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type DeobfuscationFile
func (s DeobfuscationFile) MarshalJSON() ([]byte, error)
type DeobfuscationFilesUploadResponse
func (s DeobfuscationFilesUploadResponse) MarshalJSON() ([]byte, error)
type DeployAppRecoveryRequest
type DeployAppRecoveryResponse
type DeveloperComment
func (s DeveloperComment) MarshalJSON() ([]byte, error)
type DeveloperInitiatedCancellation
type DeviceFeature
func (s DeviceFeature) MarshalJSON() ([]byte, error)
type DeviceFeatureTargeting
func (s DeviceFeatureTargeting) MarshalJSON() ([]byte, error)
type DeviceGroup
func (s DeviceGroup) MarshalJSON() ([]byte, error)
type DeviceId
func (s DeviceId) MarshalJSON() ([]byte, error)
type DeviceMetadata
func (s DeviceMetadata) MarshalJSON() ([]byte, error)
type DeviceRam
func (s DeviceRam) MarshalJSON() ([]byte, error)
type DeviceSelector
func (s DeviceSelector) MarshalJSON() ([]byte, error)
type DeviceSpec
func (s DeviceSpec) MarshalJSON() ([]byte, error)
type DeviceTier
func (s DeviceTier) MarshalJSON() ([]byte, error)
type DeviceTierConfig
func (s DeviceTierConfig) MarshalJSON() ([]byte, error)
type DeviceTierSet
func (s DeviceTierSet) MarshalJSON() ([]byte, error)
type EditsApksAddexternallyhostedCall
func (c *EditsApksAddexternallyhostedCall) Context(ctx context.Context) *EditsApksAddexternallyhostedCall
func (c *EditsApksAddexternallyhostedCall) Do(opts ...googleapi.CallOption) (*ApksAddExternallyHostedResponse, error)
func (c *EditsApksAddexternallyhostedCall) Fields(s ...googleapi.Field) *EditsApksAddexternallyhostedCall
func (c *EditsApksAddexternallyhostedCall) Header() http.Header
type EditsApksListCall
func (c *EditsApksListCall) Context(ctx context.Context) *EditsApksListCall
func (c *EditsApksListCall) Do(opts ...googleapi.CallOption) (*ApksListResponse, error)
func (c *EditsApksListCall) Fields(s ...googleapi.Field) *EditsApksListCall
func (c *EditsApksListCall) Header() http.Header
func (c *EditsApksListCall) IfNoneMatch(entityTag string) *EditsApksListCall
type EditsApksService
func NewEditsApksService(s *Service) *EditsApksService
func (r *EditsApksService) Addexternallyhosted(packageName string, editId string, ...) *EditsApksAddexternallyhostedCall
func (r *EditsApksService) List(packageName string, editId string) *EditsApksListCall
func (r *EditsApksService) Upload(packageName string, editId string) *EditsApksUploadCall
type EditsApksUploadCall
func (c *EditsApksUploadCall) Context(ctx context.Context) *EditsApksUploadCall
func (c *EditsApksUploadCall) Do(opts ...googleapi.CallOption) (*Apk, error)
func (c *EditsApksUploadCall) Fields(s ...googleapi.Field) *EditsApksUploadCall
func (c *EditsApksUploadCall) Header() http.Header
func (c *EditsApksUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsApksUploadCall
func (c *EditsApksUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsApksUploadCall
func (c *EditsApksUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *EditsApksUploadCallDEPRECATED
type EditsBundlesListCall
func (c *EditsBundlesListCall) Context(ctx context.Context) *EditsBundlesListCall
func (c *EditsBundlesListCall) Do(opts ...googleapi.CallOption) (*BundlesListResponse, error)
func (c *EditsBundlesListCall) Fields(s ...googleapi.Field) *EditsBundlesListCall
func (c *EditsBundlesListCall) Header() http.Header
func (c *EditsBundlesListCall) IfNoneMatch(entityTag string) *EditsBundlesListCall
type EditsBundlesService
func NewEditsBundlesService(s *Service) *EditsBundlesService
func (r *EditsBundlesService) List(packageName string, editId string) *EditsBundlesListCall
func (r *EditsBundlesService) Upload(packageName string, editId string) *EditsBundlesUploadCall
type EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) AckBundleInstallationWarning(ackBundleInstallationWarning bool) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) Context(ctx context.Context) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) DeviceTierConfigId(deviceTierConfigId string) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) Do(opts ...googleapi.CallOption) (*Bundle, error)
func (c *EditsBundlesUploadCall) Fields(s ...googleapi.Field) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) Header() http.Header
func (c *EditsBundlesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsBundlesUploadCall
func (c *EditsBundlesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *EditsBundlesUploadCallDEPRECATED
type EditsCommitCall
func (c *EditsCommitCall) ChangesNotSentForReview(changesNotSentForReview bool) *EditsCommitCall
func (c *EditsCommitCall) Context(ctx context.Context) *EditsCommitCall
func (c *EditsCommitCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)
func (c *EditsCommitCall) Fields(s ...googleapi.Field) *EditsCommitCall
func (c *EditsCommitCall) Header() http.Header
type EditsCountryavailabilityGetCall
func (c *EditsCountryavailabilityGetCall) Context(ctx context.Context) *EditsCountryavailabilityGetCall
func (c *EditsCountryavailabilityGetCall) Do(opts ...googleapi.CallOption) (*TrackCountryAvailability, error)
func (c *EditsCountryavailabilityGetCall) Fields(s ...googleapi.Field) *EditsCountryavailabilityGetCall
func (c *EditsCountryavailabilityGetCall) Header() http.Header
func (c *EditsCountryavailabilityGetCall) IfNoneMatch(entityTag string) *EditsCountryavailabilityGetCall
type EditsCountryavailabilityService
func NewEditsCountryavailabilityService(s *Service) *EditsCountryavailabilityService
func (r *EditsCountryavailabilityService) Get(packageName string, editId string, track string) *EditsCountryavailabilityGetCall
type EditsDeleteCall
func (c *EditsDeleteCall) Context(ctx context.Context) *EditsDeleteCall
func (c *EditsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *EditsDeleteCall) Fields(s ...googleapi.Field) *EditsDeleteCall
func (c *EditsDeleteCall) Header() http.Header
type EditsDeobfuscationfilesService
func NewEditsDeobfuscationfilesService(s *Service) *EditsDeobfuscationfilesService
func (r *EditsDeobfuscationfilesService) Upload(packageNameid string, editId string, apkVersionCode int64, ...) *EditsDeobfuscationfilesUploadCall
type EditsDeobfuscationfilesUploadCall
func (c *EditsDeobfuscationfilesUploadCall) Context(ctx context.Context) *EditsDeobfuscationfilesUploadCall
func (c *EditsDeobfuscationfilesUploadCall) Do(opts ...googleapi.CallOption) (*DeobfuscationFilesUploadResponse, error)
func (c *EditsDeobfuscationfilesUploadCall) Fields(s ...googleapi.Field) *EditsDeobfuscationfilesUploadCall
func (c *EditsDeobfuscationfilesUploadCall) Header() http.Header
func (c *EditsDeobfuscationfilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsDeobfuscationfilesUploadCall
func (c *EditsDeobfuscationfilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsDeobfuscationfilesUploadCall
func (c *EditsDeobfuscationfilesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *EditsDeobfuscationfilesUploadCallDEPRECATED
type EditsDetailsGetCall
func (c *EditsDetailsGetCall) Context(ctx context.Context) *EditsDetailsGetCall
func (c *EditsDetailsGetCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)
func (c *EditsDetailsGetCall) Fields(s ...googleapi.Field) *EditsDetailsGetCall
func (c *EditsDetailsGetCall) Header() http.Header
func (c *EditsDetailsGetCall) IfNoneMatch(entityTag string) *EditsDetailsGetCall
type EditsDetailsPatchCall
func (c *EditsDetailsPatchCall) Context(ctx context.Context) *EditsDetailsPatchCall
func (c *EditsDetailsPatchCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)
func (c *EditsDetailsPatchCall) Fields(s ...googleapi.Field) *EditsDetailsPatchCall
func (c *EditsDetailsPatchCall) Header() http.Header
type EditsDetailsService
func NewEditsDetailsService(s *Service) *EditsDetailsService
func (r *EditsDetailsService) Get(packageName string, editId string) *EditsDetailsGetCall
func (r *EditsDetailsService) Patch(packageName string, editId string, appdetails *AppDetails) *EditsDetailsPatchCall
func (r *EditsDetailsService) Update(packageName string, editId string, appdetails *AppDetails) *EditsDetailsUpdateCall
type EditsDetailsUpdateCall
func (c *EditsDetailsUpdateCall) Context(ctx context.Context) *EditsDetailsUpdateCall
func (c *EditsDetailsUpdateCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)
func (c *EditsDetailsUpdateCall) Fields(s ...googleapi.Field) *EditsDetailsUpdateCall
func (c *EditsDetailsUpdateCall) Header() http.Header
type EditsExpansionfilesGetCall
func (c *EditsExpansionfilesGetCall) Context(ctx context.Context) *EditsExpansionfilesGetCall
func (c *EditsExpansionfilesGetCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)
func (c *EditsExpansionfilesGetCall) Fields(s ...googleapi.Field) *EditsExpansionfilesGetCall
func (c *EditsExpansionfilesGetCall) Header() http.Header
func (c *EditsExpansionfilesGetCall) IfNoneMatch(entityTag string) *EditsExpansionfilesGetCall
type EditsExpansionfilesPatchCall
func (c *EditsExpansionfilesPatchCall) Context(ctx context.Context) *EditsExpansionfilesPatchCall
func (c *EditsExpansionfilesPatchCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)
func (c *EditsExpansionfilesPatchCall) Fields(s ...googleapi.Field) *EditsExpansionfilesPatchCall
func (c *EditsExpansionfilesPatchCall) Header() http.Header
type EditsExpansionfilesService
func NewEditsExpansionfilesService(s *Service) *EditsExpansionfilesService
func (r *EditsExpansionfilesService) Get(packageName string, editId string, apkVersionCode int64, ...) *EditsExpansionfilesGetCall
func (r *EditsExpansionfilesService) Patch(packageName string, editId string, apkVersionCode int64, ...) *EditsExpansionfilesPatchCall
func (r *EditsExpansionfilesService) Update(packageName string, editId string, apkVersionCode int64, ...) *EditsExpansionfilesUpdateCall
func (r *EditsExpansionfilesService) Upload(packageName string, editId string, apkVersionCode int64, ...) *EditsExpansionfilesUploadCall
type EditsExpansionfilesUpdateCall
func (c *EditsExpansionfilesUpdateCall) Context(ctx context.Context) *EditsExpansionfilesUpdateCall
func (c *EditsExpansionfilesUpdateCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)
func (c *EditsExpansionfilesUpdateCall) Fields(s ...googleapi.Field) *EditsExpansionfilesUpdateCall
func (c *EditsExpansionfilesUpdateCall) Header() http.Header
type EditsExpansionfilesUploadCall
func (c *EditsExpansionfilesUploadCall) Context(ctx context.Context) *EditsExpansionfilesUploadCall
func (c *EditsExpansionfilesUploadCall) Do(opts ...googleapi.CallOption) (*ExpansionFilesUploadResponse, error)
func (c *EditsExpansionfilesUploadCall) Fields(s ...googleapi.Field) *EditsExpansionfilesUploadCall
func (c *EditsExpansionfilesUploadCall) Header() http.Header
func (c *EditsExpansionfilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsExpansionfilesUploadCall
func (c *EditsExpansionfilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsExpansionfilesUploadCall
func (c *EditsExpansionfilesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *EditsExpansionfilesUploadCallDEPRECATED
type EditsGetCall
func (c *EditsGetCall) Context(ctx context.Context) *EditsGetCall
func (c *EditsGetCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)
func (c *EditsGetCall) Fields(s ...googleapi.Field) *EditsGetCall
func (c *EditsGetCall) Header() http.Header
func (c *EditsGetCall) IfNoneMatch(entityTag string) *EditsGetCall
type EditsImagesDeleteCall
func (c *EditsImagesDeleteCall) Context(ctx context.Context) *EditsImagesDeleteCall
func (c *EditsImagesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *EditsImagesDeleteCall) Fields(s ...googleapi.Field) *EditsImagesDeleteCall
func (c *EditsImagesDeleteCall) Header() http.Header
type EditsImagesDeleteallCall
func (c *EditsImagesDeleteallCall) Context(ctx context.Context) *EditsImagesDeleteallCall
func (c *EditsImagesDeleteallCall) Do(opts ...googleapi.CallOption) (*ImagesDeleteAllResponse, error)
func (c *EditsImagesDeleteallCall) Fields(s ...googleapi.Field) *EditsImagesDeleteallCall
func (c *EditsImagesDeleteallCall) Header() http.Header
type EditsImagesListCall
func (c *EditsImagesListCall) Context(ctx context.Context) *EditsImagesListCall
func (c *EditsImagesListCall) Do(opts ...googleapi.CallOption) (*ImagesListResponse, error)
func (c *EditsImagesListCall) Fields(s ...googleapi.Field) *EditsImagesListCall
func (c *EditsImagesListCall) Header() http.Header
func (c *EditsImagesListCall) IfNoneMatch(entityTag string) *EditsImagesListCall
type EditsImagesService
func NewEditsImagesService(s *Service) *EditsImagesService
func (r *EditsImagesService) Delete(packageName string, editId string, language string, imageType string, ...) *EditsImagesDeleteCall
func (r *EditsImagesService) Deleteall(packageName string, editId string, language string, imageType string) *EditsImagesDeleteallCall
func (r *EditsImagesService) List(packageName string, editId string, language string, imageType string) *EditsImagesListCall
func (r *EditsImagesService) Upload(packageName string, editId string, language string, imageType string) *EditsImagesUploadCall
type EditsImagesUploadCall
func (c *EditsImagesUploadCall) Context(ctx context.Context) *EditsImagesUploadCall
func (c *EditsImagesUploadCall) Do(opts ...googleapi.CallOption) (*ImagesUploadResponse, error)
func (c *EditsImagesUploadCall) Fields(s ...googleapi.Field) *EditsImagesUploadCall
func (c *EditsImagesUploadCall) Header() http.Header
func (c *EditsImagesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsImagesUploadCall
func (c *EditsImagesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsImagesUploadCall
func (c *EditsImagesUploadCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *EditsImagesUploadCallDEPRECATED
type EditsInsertCall
func (c *EditsInsertCall) Context(ctx context.Context) *EditsInsertCall
func (c *EditsInsertCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)
func (c *EditsInsertCall) Fields(s ...googleapi.Field) *EditsInsertCall
func (c *EditsInsertCall) Header() http.Header
type EditsListingsDeleteCall
func (c *EditsListingsDeleteCall) Context(ctx context.Context) *EditsListingsDeleteCall
func (c *EditsListingsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *EditsListingsDeleteCall) Fields(s ...googleapi.Field) *EditsListingsDeleteCall
func (c *EditsListingsDeleteCall) Header() http.Header
type EditsListingsDeleteallCall
func (c *EditsListingsDeleteallCall) Context(ctx context.Context) *EditsListingsDeleteallCall
func (c *EditsListingsDeleteallCall) Do(opts ...googleapi.CallOption) error
func (c *EditsListingsDeleteallCall) Fields(s ...googleapi.Field) *EditsListingsDeleteallCall
func (c *EditsListingsDeleteallCall) Header() http.Header
type EditsListingsGetCall
func (c *EditsListingsGetCall) Context(ctx context.Context) *EditsListingsGetCall
func (c *EditsListingsGetCall) Do(opts ...googleapi.CallOption) (*Listing, error)
func (c *EditsListingsGetCall) Fields(s ...googleapi.Field) *EditsListingsGetCall
func (c *EditsListingsGetCall) Header() http.Header
func (c *EditsListingsGetCall) IfNoneMatch(entityTag string) *EditsListingsGetCall
type EditsListingsListCall
func (c *EditsListingsListCall) Context(ctx context.Context) *EditsListingsListCall
func (c *EditsListingsListCall) Do(opts ...googleapi.CallOption) (*ListingsListResponse, error)
func (c *EditsListingsListCall) Fields(s ...googleapi.Field) *EditsListingsListCall
func (c *EditsListingsListCall) Header() http.Header
func (c *EditsListingsListCall) IfNoneMatch(entityTag string) *EditsListingsListCall
type EditsListingsPatchCall
func (c *EditsListingsPatchCall) Context(ctx context.Context) *EditsListingsPatchCall
func (c *EditsListingsPatchCall) Do(opts ...googleapi.CallOption) (*Listing, error)
func (c *EditsListingsPatchCall) Fields(s ...googleapi.Field) *EditsListingsPatchCall
func (c *EditsListingsPatchCall) Header() http.Header
type EditsListingsService
func NewEditsListingsService(s *Service) *EditsListingsService
func (r *EditsListingsService) Delete(packageName string, editId string, language string) *EditsListingsDeleteCall
func (r *EditsListingsService) Deleteall(packageName string, editId string) *EditsListingsDeleteallCall
func (r *EditsListingsService) Get(packageName string, editId string, language string) *EditsListingsGetCall
func (r *EditsListingsService) List(packageName string, editId string) *EditsListingsListCall
func (r *EditsListingsService) Patch(packageName string, editId string, language string, listing *Listing) *EditsListingsPatchCall
func (r *EditsListingsService) Update(packageName string, editId string, language string, listing *Listing) *EditsListingsUpdateCall
type EditsListingsUpdateCall
func (c *EditsListingsUpdateCall) Context(ctx context.Context) *EditsListingsUpdateCall
func (c *EditsListingsUpdateCall) Do(opts ...googleapi.CallOption) (*Listing, error)
func (c *EditsListingsUpdateCall) Fields(s ...googleapi.Field) *EditsListingsUpdateCall
func (c *EditsListingsUpdateCall) Header() http.Header
type EditsService
func NewEditsService(s *Service) *EditsService
func (r *EditsService) Commit(packageName string, editId string) *EditsCommitCall
func (r *EditsService) Delete(packageName string, editId string) *EditsDeleteCall
func (r *EditsService) Get(packageName string, editId string) *EditsGetCall
func (r *EditsService) Insert(packageName string, appedit *AppEdit) *EditsInsertCall
func (r *EditsService) Validate(packageName string, editId string) *EditsValidateCall
type EditsTestersGetCall
func (c *EditsTestersGetCall) Context(ctx context.Context) *EditsTestersGetCall
func (c *EditsTestersGetCall) Do(opts ...googleapi.CallOption) (*Testers, error)
func (c *EditsTestersGetCall) Fields(s ...googleapi.Field) *EditsTestersGetCall
func (c *EditsTestersGetCall) Header() http.Header
func (c *EditsTestersGetCall) IfNoneMatch(entityTag string) *EditsTestersGetCall
type EditsTestersPatchCall
func (c *EditsTestersPatchCall) Context(ctx context.Context) *EditsTestersPatchCall
func (c *EditsTestersPatchCall) Do(opts ...googleapi.CallOption) (*Testers, error)
func (c *EditsTestersPatchCall) Fields(s ...googleapi.Field) *EditsTestersPatchCall
func (c *EditsTestersPatchCall) Header() http.Header
type EditsTestersService
func NewEditsTestersService(s *Service) *EditsTestersService
func (r *EditsTestersService) Get(packageName string, editId string, track string) *EditsTestersGetCall
func (r *EditsTestersService) Patch(packageName string, editId string, track string, testers *Testers) *EditsTestersPatchCall
func (r *EditsTestersService) Update(packageName string, editId string, track string, testers *Testers) *EditsTestersUpdateCall
type EditsTestersUpdateCall
func (c *EditsTestersUpdateCall) Context(ctx context.Context) *EditsTestersUpdateCall
func (c *EditsTestersUpdateCall) Do(opts ...googleapi.CallOption) (*Testers, error)
func (c *EditsTestersUpdateCall) Fields(s ...googleapi.Field) *EditsTestersUpdateCall
func (c *EditsTestersUpdateCall) Header() http.Header
type EditsTracksCreateCall
func (c *EditsTracksCreateCall) Context(ctx context.Context) *EditsTracksCreateCall
func (c *EditsTracksCreateCall) Do(opts ...googleapi.CallOption) (*Track, error)
func (c *EditsTracksCreateCall) Fields(s ...googleapi.Field) *EditsTracksCreateCall
func (c *EditsTracksCreateCall) Header() http.Header
type EditsTracksGetCall
func (c *EditsTracksGetCall) Context(ctx context.Context) *EditsTracksGetCall
func (c *EditsTracksGetCall) Do(opts ...googleapi.CallOption) (*Track, error)
func (c *EditsTracksGetCall) Fields(s ...googleapi.Field) *EditsTracksGetCall
func (c *EditsTracksGetCall) Header() http.Header
func (c *EditsTracksGetCall) IfNoneMatch(entityTag string) *EditsTracksGetCall
type EditsTracksListCall
func (c *EditsTracksListCall) Context(ctx context.Context) *EditsTracksListCall
func (c *EditsTracksListCall) Do(opts ...googleapi.CallOption) (*TracksListResponse, error)
func (c *EditsTracksListCall) Fields(s ...googleapi.Field) *EditsTracksListCall
func (c *EditsTracksListCall) Header() http.Header
func (c *EditsTracksListCall) IfNoneMatch(entityTag string) *EditsTracksListCall
type EditsTracksPatchCall
func (c *EditsTracksPatchCall) Context(ctx context.Context) *EditsTracksPatchCall
func (c *EditsTracksPatchCall) Do(opts ...googleapi.CallOption) (*Track, error)
func (c *EditsTracksPatchCall) Fields(s ...googleapi.Field) *EditsTracksPatchCall
func (c *EditsTracksPatchCall) Header() http.Header
type EditsTracksService
func NewEditsTracksService(s *Service) *EditsTracksService
func (r *EditsTracksService) Create(packageName string, editId string, trackconfig *TrackConfig) *EditsTracksCreateCall
func (r *EditsTracksService) Get(packageName string, editId string, track string) *EditsTracksGetCall
func (r *EditsTracksService) List(packageName string, editId string) *EditsTracksListCall
func (r *EditsTracksService) Patch(packageName string, editId string, track string, track2 *Track) *EditsTracksPatchCall
func (r *EditsTracksService) Update(packageName string, editId string, track string, track2 *Track) *EditsTracksUpdateCall
type EditsTracksUpdateCall
func (c *EditsTracksUpdateCall) Context(ctx context.Context) *EditsTracksUpdateCall
func (c *EditsTracksUpdateCall) Do(opts ...googleapi.CallOption) (*Track, error)
func (c *EditsTracksUpdateCall) Fields(s ...googleapi.Field) *EditsTracksUpdateCall
func (c *EditsTracksUpdateCall) Header() http.Header
type EditsValidateCall
func (c *EditsValidateCall) Context(ctx context.Context) *EditsValidateCall
func (c *EditsValidateCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)
func (c *EditsValidateCall) Fields(s ...googleapi.Field) *EditsValidateCall
func (c *EditsValidateCall) Header() http.Header
type ExpansionFile
func (s ExpansionFile) MarshalJSON() ([]byte, error)
type ExpansionFilesUploadResponse
func (s ExpansionFilesUploadResponse) MarshalJSON() ([]byte, error)
type ExternalAccountIdentifiers
func (s ExternalAccountIdentifiers) MarshalJSON() ([]byte, error)
type ExternalAccountIds
func (s ExternalAccountIds) MarshalJSON() ([]byte, error)
type ExternalOfferDetails
func (s ExternalOfferDetails) MarshalJSON() ([]byte, error)
type ExternalSubscription
func (s ExternalSubscription) MarshalJSON() ([]byte, error)
type ExternalTransaction
func (s ExternalTransaction) MarshalJSON() ([]byte, error)
type ExternalTransactionAddress
func (s ExternalTransactionAddress) MarshalJSON() ([]byte, error)
type ExternalTransactionTestPurchase
type ExternallyHostedApk
func (s ExternallyHostedApk) MarshalJSON() ([]byte, error)
type ExternaltransactionsCreateexternaltransactionCall
func (c *ExternaltransactionsCreateexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsCreateexternaltransactionCall
func (c *ExternaltransactionsCreateexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)
func (c *ExternaltransactionsCreateexternaltransactionCall) ExternalTransactionId(externalTransactionId string) *ExternaltransactionsCreateexternaltransactionCall
func (c *ExternaltransactionsCreateexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsCreateexternaltransactionCall
func (c *ExternaltransactionsCreateexternaltransactionCall) Header() http.Header
type ExternaltransactionsGetexternaltransactionCall
func (c *ExternaltransactionsGetexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsGetexternaltransactionCall
func (c *ExternaltransactionsGetexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)
func (c *ExternaltransactionsGetexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsGetexternaltransactionCall
func (c *ExternaltransactionsGetexternaltransactionCall) Header() http.Header
func (c *ExternaltransactionsGetexternaltransactionCall) IfNoneMatch(entityTag string) *ExternaltransactionsGetexternaltransactionCall
type ExternaltransactionsRefundexternaltransactionCall
func (c *ExternaltransactionsRefundexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsRefundexternaltransactionCall
func (c *ExternaltransactionsRefundexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)
func (c *ExternaltransactionsRefundexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsRefundexternaltransactionCall
func (c *ExternaltransactionsRefundexternaltransactionCall) Header() http.Header
type ExternaltransactionsService
func NewExternaltransactionsService(s *Service) *ExternaltransactionsService
func (r *ExternaltransactionsService) Createexternaltransaction(parent string, externaltransaction *ExternalTransaction) *ExternaltransactionsCreateexternaltransactionCall
func (r *ExternaltransactionsService) Getexternaltransaction(name string) *ExternaltransactionsGetexternaltransactionCall
func (r *ExternaltransactionsService) Refundexternaltransaction(name string, ...) *ExternaltransactionsRefundexternaltransactionCall
type FreeTrialDetails
type FreeTrialOfferPhase
type FullRefund
type GeneratedApksListResponse
func (s GeneratedApksListResponse) MarshalJSON() ([]byte, error)
type GeneratedApksPerSigningKey
func (s GeneratedApksPerSigningKey) MarshalJSON() ([]byte, error)
type GeneratedAssetPackSlice
func (s GeneratedAssetPackSlice) MarshalJSON() ([]byte, error)
type GeneratedRecoveryApk
func (s GeneratedRecoveryApk) MarshalJSON() ([]byte, error)
type GeneratedSplitApk
func (s GeneratedSplitApk) MarshalJSON() ([]byte, error)
type GeneratedStandaloneApk
func (s GeneratedStandaloneApk) MarshalJSON() ([]byte, error)
type GeneratedUniversalApk
func (s GeneratedUniversalApk) MarshalJSON() ([]byte, error)
type GeneratedapksDownloadCall
func (c *GeneratedapksDownloadCall) Context(ctx context.Context) *GeneratedapksDownloadCall
func (c *GeneratedapksDownloadCall) Do(opts ...googleapi.CallOption) error
func (c *GeneratedapksDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)
func (c *GeneratedapksDownloadCall) Fields(s ...googleapi.Field) *GeneratedapksDownloadCall
func (c *GeneratedapksDownloadCall) Header() http.Header
func (c *GeneratedapksDownloadCall) IfNoneMatch(entityTag string) *GeneratedapksDownloadCall
type GeneratedapksListCall
func (c *GeneratedapksListCall) Context(ctx context.Context) *GeneratedapksListCall
func (c *GeneratedapksListCall) Do(opts ...googleapi.CallOption) (*GeneratedApksListResponse, error)
func (c *GeneratedapksListCall) Fields(s ...googleapi.Field) *GeneratedapksListCall
func (c *GeneratedapksListCall) Header() http.Header
func (c *GeneratedapksListCall) IfNoneMatch(entityTag string) *GeneratedapksListCall
type GeneratedapksService
func NewGeneratedapksService(s *Service) *GeneratedapksService
func (r *GeneratedapksService) Download(packageName string, versionCode int64, downloadId string) *GeneratedapksDownloadCall
func (r *GeneratedapksService) List(packageName string, versionCode int64) *GeneratedapksListCall
type GetOneTimeProductOfferRequest
func (s GetOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type GetSubscriptionOfferRequest
func (s GetSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type Grant
func (s Grant) MarshalJSON() ([]byte, error)
type GrantsCreateCall
func (c *GrantsCreateCall) Context(ctx context.Context) *GrantsCreateCall
func (c *GrantsCreateCall) Do(opts ...googleapi.CallOption) (*Grant, error)
func (c *GrantsCreateCall) Fields(s ...googleapi.Field) *GrantsCreateCall
func (c *GrantsCreateCall) Header() http.Header
type GrantsDeleteCall
func (c *GrantsDeleteCall) Context(ctx context.Context) *GrantsDeleteCall
func (c *GrantsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *GrantsDeleteCall) Fields(s ...googleapi.Field) *GrantsDeleteCall
func (c *GrantsDeleteCall) Header() http.Header
type GrantsPatchCall
func (c *GrantsPatchCall) Context(ctx context.Context) *GrantsPatchCall
func (c *GrantsPatchCall) Do(opts ...googleapi.CallOption) (*Grant, error)
func (c *GrantsPatchCall) Fields(s ...googleapi.Field) *GrantsPatchCall
func (c *GrantsPatchCall) Header() http.Header
func (c *GrantsPatchCall) UpdateMask(updateMask string) *GrantsPatchCall
type GrantsService
func NewGrantsService(s *Service) *GrantsService
func (r *GrantsService) Create(parent string, grant *Grant) *GrantsCreateCall
func (r *GrantsService) Delete(name string) *GrantsDeleteCall
func (r *GrantsService) Patch(name string, grant *Grant) *GrantsPatchCall
type Image
func (s Image) MarshalJSON() ([]byte, error)
type ImagesDeleteAllResponse
func (s ImagesDeleteAllResponse) MarshalJSON() ([]byte, error)
type ImagesListResponse
func (s ImagesListResponse) MarshalJSON() ([]byte, error)
type ImagesUploadResponse
func (s ImagesUploadResponse) MarshalJSON() ([]byte, error)
type InAppProduct
func (s InAppProduct) MarshalJSON() ([]byte, error)
type InAppProductListing
func (s InAppProductListing) MarshalJSON() ([]byte, error)
type InappproductsBatchDeleteCall
func (c *InappproductsBatchDeleteCall) Context(ctx context.Context) *InappproductsBatchDeleteCall
func (c *InappproductsBatchDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *InappproductsBatchDeleteCall) Fields(s ...googleapi.Field) *InappproductsBatchDeleteCall
func (c *InappproductsBatchDeleteCall) Header() http.Header
type InappproductsBatchDeleteRequest
func (s InappproductsBatchDeleteRequest) MarshalJSON() ([]byte, error)
type InappproductsBatchGetCall
func (c *InappproductsBatchGetCall) Context(ctx context.Context) *InappproductsBatchGetCall
func (c *InappproductsBatchGetCall) Do(opts ...googleapi.CallOption) (*InappproductsBatchGetResponse, error)
func (c *InappproductsBatchGetCall) Fields(s ...googleapi.Field) *InappproductsBatchGetCall
func (c *InappproductsBatchGetCall) Header() http.Header
func (c *InappproductsBatchGetCall) IfNoneMatch(entityTag string) *InappproductsBatchGetCall
func (c *InappproductsBatchGetCall) Sku(sku ...string) *InappproductsBatchGetCall
type InappproductsBatchGetResponse
func (s InappproductsBatchGetResponse) MarshalJSON() ([]byte, error)
type InappproductsBatchUpdateCall
func (c *InappproductsBatchUpdateCall) Context(ctx context.Context) *InappproductsBatchUpdateCall
func (c *InappproductsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*InappproductsBatchUpdateResponse, error)
func (c *InappproductsBatchUpdateCall) Fields(s ...googleapi.Field) *InappproductsBatchUpdateCall
func (c *InappproductsBatchUpdateCall) Header() http.Header
type InappproductsBatchUpdateRequest
func (s InappproductsBatchUpdateRequest) MarshalJSON() ([]byte, error)
type InappproductsBatchUpdateResponse
func (s InappproductsBatchUpdateResponse) MarshalJSON() ([]byte, error)
type InappproductsDeleteCall
func (c *InappproductsDeleteCall) Context(ctx context.Context) *InappproductsDeleteCall
func (c *InappproductsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *InappproductsDeleteCall) Fields(s ...googleapi.Field) *InappproductsDeleteCall
func (c *InappproductsDeleteCall) Header() http.Header
func (c *InappproductsDeleteCall) LatencyTolerance(latencyTolerance string) *InappproductsDeleteCall
type InappproductsDeleteRequest
func (s InappproductsDeleteRequest) MarshalJSON() ([]byte, error)
type InappproductsGetCall
func (c *InappproductsGetCall) Context(ctx context.Context) *InappproductsGetCall
func (c *InappproductsGetCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)
func (c *InappproductsGetCall) Fields(s ...googleapi.Field) *InappproductsGetCall
func (c *InappproductsGetCall) Header() http.Header
func (c *InappproductsGetCall) IfNoneMatch(entityTag string) *InappproductsGetCall
type InappproductsInsertCall
func (c *InappproductsInsertCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsInsertCall
func (c *InappproductsInsertCall) Context(ctx context.Context) *InappproductsInsertCall
func (c *InappproductsInsertCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)
func (c *InappproductsInsertCall) Fields(s ...googleapi.Field) *InappproductsInsertCall
func (c *InappproductsInsertCall) Header() http.Header
type InappproductsListCall
func (c *InappproductsListCall) Context(ctx context.Context) *InappproductsListCall
func (c *InappproductsListCall) Do(opts ...googleapi.CallOption) (*InappproductsListResponse, error)
func (c *InappproductsListCall) Fields(s ...googleapi.Field) *InappproductsListCall
func (c *InappproductsListCall) Header() http.Header
func (c *InappproductsListCall) IfNoneMatch(entityTag string) *InappproductsListCall
func (c *InappproductsListCall) MaxResults(maxResults int64) *InappproductsListCall
func (c *InappproductsListCall) StartIndex(startIndex int64) *InappproductsListCall
func (c *InappproductsListCall) Token(token string) *InappproductsListCall
type InappproductsListResponse
func (s InappproductsListResponse) MarshalJSON() ([]byte, error)
type InappproductsPatchCall
func (c *InappproductsPatchCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsPatchCall
func (c *InappproductsPatchCall) Context(ctx context.Context) *InappproductsPatchCall
func (c *InappproductsPatchCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)
func (c *InappproductsPatchCall) Fields(s ...googleapi.Field) *InappproductsPatchCall
func (c *InappproductsPatchCall) Header() http.Header
func (c *InappproductsPatchCall) LatencyTolerance(latencyTolerance string) *InappproductsPatchCall
type InappproductsService
func NewInappproductsService(s *Service) *InappproductsService
func (r *InappproductsService) BatchDelete(packageName string, ...) *InappproductsBatchDeleteCall
func (r *InappproductsService) BatchGet(packageName string) *InappproductsBatchGetCall
func (r *InappproductsService) BatchUpdate(packageName string, ...) *InappproductsBatchUpdateCall
func (r *InappproductsService) Delete(packageName string, skuid string) *InappproductsDeleteCall
func (r *InappproductsService) Get(packageName string, skuid string) *InappproductsGetCall
func (r *InappproductsService) Insert(packageName string, inappproduct *InAppProduct) *InappproductsInsertCall
func (r *InappproductsService) List(packageName string) *InappproductsListCall
func (r *InappproductsService) Patch(packageName string, skuid string, inappproduct *InAppProduct) *InappproductsPatchCall
func (r *InappproductsService) Update(packageName string, skuid string, inappproduct *InAppProduct) *InappproductsUpdateCall
type InappproductsUpdateCall
func (c *InappproductsUpdateCall) AllowMissing(allowMissing bool) *InappproductsUpdateCall
func (c *InappproductsUpdateCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsUpdateCall
func (c *InappproductsUpdateCall) Context(ctx context.Context) *InappproductsUpdateCall
func (c *InappproductsUpdateCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)
func (c *InappproductsUpdateCall) Fields(s ...googleapi.Field) *InappproductsUpdateCall
func (c *InappproductsUpdateCall) Header() http.Header
func (c *InappproductsUpdateCall) LatencyTolerance(latencyTolerance string) *InappproductsUpdateCall
type InappproductsUpdateRequest
func (s InappproductsUpdateRequest) MarshalJSON() ([]byte, error)
type InstallmentPlan
func (s InstallmentPlan) MarshalJSON() ([]byte, error)
type InstallmentsBasePlanType
func (s InstallmentsBasePlanType) MarshalJSON() ([]byte, error)
type InternalAppSharingArtifact
func (s InternalAppSharingArtifact) MarshalJSON() ([]byte, error)
type InternalappsharingartifactsService
func NewInternalappsharingartifactsService(s *Service) *InternalappsharingartifactsService
func (r *InternalappsharingartifactsService) Uploadapk(packageName string) *InternalappsharingartifactsUploadapkCall
func (r *InternalappsharingartifactsService) Uploadbundle(packageName string) *InternalappsharingartifactsUploadbundleCall
type InternalappsharingartifactsUploadapkCall
func (c *InternalappsharingartifactsUploadapkCall) Context(ctx context.Context) *InternalappsharingartifactsUploadapkCall
func (c *InternalappsharingartifactsUploadapkCall) Do(opts ...googleapi.CallOption) (*InternalAppSharingArtifact, error)
func (c *InternalappsharingartifactsUploadapkCall) Fields(s ...googleapi.Field) *InternalappsharingartifactsUploadapkCall
func (c *InternalappsharingartifactsUploadapkCall) Header() http.Header
func (c *InternalappsharingartifactsUploadapkCall) Media(r io.Reader, options ...googleapi.MediaOption) *InternalappsharingartifactsUploadapkCall
func (c *InternalappsharingartifactsUploadapkCall) ProgressUpdater(pu googleapi.ProgressUpdater) *InternalappsharingartifactsUploadapkCall
func (c *InternalappsharingartifactsUploadapkCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *InternalappsharingartifactsUploadapkCallDEPRECATED
type InternalappsharingartifactsUploadbundleCall
func (c *InternalappsharingartifactsUploadbundleCall) Context(ctx context.Context) *InternalappsharingartifactsUploadbundleCall
func (c *InternalappsharingartifactsUploadbundleCall) Do(opts ...googleapi.CallOption) (*InternalAppSharingArtifact, error)
func (c *InternalappsharingartifactsUploadbundleCall) Fields(s ...googleapi.Field) *InternalappsharingartifactsUploadbundleCall
func (c *InternalappsharingartifactsUploadbundleCall) Header() http.Header
func (c *InternalappsharingartifactsUploadbundleCall) Media(r io.Reader, options ...googleapi.MediaOption) *InternalappsharingartifactsUploadbundleCall
func (c *InternalappsharingartifactsUploadbundleCall) ProgressUpdater(pu googleapi.ProgressUpdater) *InternalappsharingartifactsUploadbundleCall
func (c *InternalappsharingartifactsUploadbundleCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *InternalappsharingartifactsUploadbundleCallDEPRECATED
type IntroductoryPriceDetails
type IntroductoryPriceInfo
func (s IntroductoryPriceInfo) MarshalJSON() ([]byte, error)
type IntroductoryPriceOfferPhase
type ItemExpiryTimeDetails
func (s ItemExpiryTimeDetails) MarshalJSON() ([]byte, error)
type ItemReplacement
func (s ItemReplacement) MarshalJSON() ([]byte, error)
type LanguageTargeting
func (s LanguageTargeting) MarshalJSON() ([]byte, error)
type LineItem
func (s LineItem) MarshalJSON() ([]byte, error)
type ListAppRecoveriesResponse
func (s ListAppRecoveriesResponse) MarshalJSON() ([]byte, error)
type ListDeviceTierConfigsResponse
func (s ListDeviceTierConfigsResponse) MarshalJSON() ([]byte, error)
type ListOneTimeProductOffersResponse
func (s ListOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type ListOneTimeProductsResponse
func (s ListOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type ListSubscriptionOffersResponse
func (s ListSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type ListSubscriptionsResponse
func (s ListSubscriptionsResponse) MarshalJSON() ([]byte, error)
type ListUsersResponse
func (s ListUsersResponse) MarshalJSON() ([]byte, error)
type Listing
func (s Listing) MarshalJSON() ([]byte, error)
type ListingsListResponse
func (s ListingsListResponse) MarshalJSON() ([]byte, error)
type LocalizedText
func (s LocalizedText) MarshalJSON() ([]byte, error)
type ManagedProductTaxAndComplianceSettings
func (s ManagedProductTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type MigrateBasePlanPricesRequest
func (s MigrateBasePlanPricesRequest) MarshalJSON() ([]byte, error)
type MigrateBasePlanPricesResponse
type ModuleMetadata
func (s ModuleMetadata) MarshalJSON() ([]byte, error)
type ModuleTargeting
func (s ModuleTargeting) MarshalJSON() ([]byte, error)
type MonetizationConvertRegionPricesCall
func (c *MonetizationConvertRegionPricesCall) Context(ctx context.Context) *MonetizationConvertRegionPricesCall
func (c *MonetizationConvertRegionPricesCall) Do(opts ...googleapi.CallOption) (*ConvertRegionPricesResponse, error)
func (c *MonetizationConvertRegionPricesCall) Fields(s ...googleapi.Field) *MonetizationConvertRegionPricesCall
func (c *MonetizationConvertRegionPricesCall) Header() http.Header
type MonetizationOnetimeproductsBatchDeleteCall
func (c *MonetizationOnetimeproductsBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchDeleteCall
func (c *MonetizationOnetimeproductsBatchDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationOnetimeproductsBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchDeleteCall
func (c *MonetizationOnetimeproductsBatchDeleteCall) Header() http.Header
type MonetizationOnetimeproductsBatchGetCall
func (c *MonetizationOnetimeproductsBatchGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchGetCall
func (c *MonetizationOnetimeproductsBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetOneTimeProductsResponse, error)
func (c *MonetizationOnetimeproductsBatchGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchGetCall
func (c *MonetizationOnetimeproductsBatchGetCall) Header() http.Header
func (c *MonetizationOnetimeproductsBatchGetCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsBatchGetCall
func (c *MonetizationOnetimeproductsBatchGetCall) ProductIds(productIds ...string) *MonetizationOnetimeproductsBatchGetCall
type MonetizationOnetimeproductsBatchUpdateCall
func (c *MonetizationOnetimeproductsBatchUpdateCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchUpdateCall
func (c *MonetizationOnetimeproductsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductsResponse, error)
func (c *MonetizationOnetimeproductsBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchUpdateCall
func (c *MonetizationOnetimeproductsBatchUpdateCall) Header() http.Header
type MonetizationOnetimeproductsDeleteCall
func (c *MonetizationOnetimeproductsDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsDeleteCall
func (c *MonetizationOnetimeproductsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationOnetimeproductsDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsDeleteCall
func (c *MonetizationOnetimeproductsDeleteCall) Header() http.Header
func (c *MonetizationOnetimeproductsDeleteCall) LatencyTolerance(latencyTolerance string) *MonetizationOnetimeproductsDeleteCall
type MonetizationOnetimeproductsGetCall
func (c *MonetizationOnetimeproductsGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsGetCall
func (c *MonetizationOnetimeproductsGetCall) Do(opts ...googleapi.CallOption) (*OneTimeProduct, error)
func (c *MonetizationOnetimeproductsGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsGetCall
func (c *MonetizationOnetimeproductsGetCall) Header() http.Header
func (c *MonetizationOnetimeproductsGetCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsGetCall
type MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) Context(ctx context.Context) *MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) Do(opts ...googleapi.CallOption) (*ListOneTimeProductsResponse, error)
func (c *MonetizationOnetimeproductsListCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) Header() http.Header
func (c *MonetizationOnetimeproductsListCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) PageSize(pageSize int64) *MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) PageToken(pageToken string) *MonetizationOnetimeproductsListCall
func (c *MonetizationOnetimeproductsListCall) Pages(ctx context.Context, f func(*ListOneTimeProductsResponse) error) error
type MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) AllowMissing(allowMissing bool) *MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) Context(ctx context.Context) *MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) Do(opts ...googleapi.CallOption) (*OneTimeProduct, error)
func (c *MonetizationOnetimeproductsPatchCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) Header() http.Header
func (c *MonetizationOnetimeproductsPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationOnetimeproductsPatchCall
func (c *MonetizationOnetimeproductsPatchCall) UpdateMask(updateMask string) *MonetizationOnetimeproductsPatchCall
type MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdatePurchaseOptionStatesResponse, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetOneTimeProductOffersResponse, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductOffersResponse, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductOfferStatesResponse, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Header() http.Header
type MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Do(opts ...googleapi.CallOption) (*ListOneTimeProductOffersResponse, error)
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Header() http.Header
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageSize(pageSize int64) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageToken(pageToken string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Pages(ctx context.Context, f func(*ListOneTimeProductOffersResponse) error) error
type MonetizationOnetimeproductsPurchaseOptionsOffersService
func NewMonetizationOnetimeproductsPurchaseOptionsOffersService(s *Service) *MonetizationOnetimeproductsPurchaseOptionsOffersService
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Activate(packageName string, productId string, purchaseOptionId string, offerId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchDelete(packageName string, productId string, purchaseOptionId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchGet(packageName string, productId string, purchaseOptionId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdate(packageName string, productId string, purchaseOptionId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdateStates(packageName string, productId string, purchaseOptionId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Cancel(packageName string, productId string, purchaseOptionId string, offerId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Deactivate(packageName string, productId string, purchaseOptionId string, offerId string, ...) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) List(packageName string, productId string, purchaseOptionId string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall
type MonetizationOnetimeproductsPurchaseOptionsService
func NewMonetizationOnetimeproductsPurchaseOptionsService(s *Service) *MonetizationOnetimeproductsPurchaseOptionsService
func (r *MonetizationOnetimeproductsPurchaseOptionsService) BatchDelete(packageName string, productId string, ...) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall
func (r *MonetizationOnetimeproductsPurchaseOptionsService) BatchUpdateStates(packageName string, productId string, ...) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall
type MonetizationOnetimeproductsService
func NewMonetizationOnetimeproductsService(s *Service) *MonetizationOnetimeproductsService
func (r *MonetizationOnetimeproductsService) BatchDelete(packageName string, ...) *MonetizationOnetimeproductsBatchDeleteCall
func (r *MonetizationOnetimeproductsService) BatchGet(packageName string) *MonetizationOnetimeproductsBatchGetCall
func (r *MonetizationOnetimeproductsService) BatchUpdate(packageName string, ...) *MonetizationOnetimeproductsBatchUpdateCall
func (r *MonetizationOnetimeproductsService) Delete(packageName string, productId string) *MonetizationOnetimeproductsDeleteCall
func (r *MonetizationOnetimeproductsService) Get(packageName string, productId string) *MonetizationOnetimeproductsGetCall
func (r *MonetizationOnetimeproductsService) List(packageName string) *MonetizationOnetimeproductsListCall
func (r *MonetizationOnetimeproductsService) Patch(packageName string, productId string, onetimeproduct *OneTimeProduct) *MonetizationOnetimeproductsPatchCall
type MonetizationService
func NewMonetizationService(s *Service) *MonetizationService
func (r *MonetizationService) ConvertRegionPrices(packageName string, convertregionpricesrequest *ConvertRegionPricesRequest) *MonetizationConvertRegionPricesCall
type MonetizationSubscriptionsArchiveCall
func (c *MonetizationSubscriptionsArchiveCall) Context(ctx context.Context) *MonetizationSubscriptionsArchiveCall
func (c *MonetizationSubscriptionsArchiveCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsArchiveCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsArchiveCall
func (c *MonetizationSubscriptionsArchiveCall) Header() http.Header
type MonetizationSubscriptionsBasePlansActivateCall
func (c *MonetizationSubscriptionsBasePlansActivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansActivateCall
func (c *MonetizationSubscriptionsBasePlansActivateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsBasePlansActivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansActivateCall
func (c *MonetizationSubscriptionsBasePlansActivateCall) Header() http.Header
type MonetizationSubscriptionsBasePlansBatchMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Do(opts ...googleapi.CallOption) (*BatchMigrateBasePlanPricesResponse, error)
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Header() http.Header
type MonetizationSubscriptionsBasePlansBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateBasePlanStatesResponse, error)
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Header() http.Header
type MonetizationSubscriptionsBasePlansDeactivateCall
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansDeactivateCall
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansDeactivateCall
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Header() http.Header
type MonetizationSubscriptionsBasePlansDeleteCall
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansDeleteCall
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansDeleteCall
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Header() http.Header
type MonetizationSubscriptionsBasePlansMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Do(opts ...googleapi.CallOption) (*MigrateBasePlanPricesResponse, error)
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansMigratePricesCall
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersActivateCall
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersActivateCall
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersActivateCall
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersBatchGetCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchGetCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetSubscriptionOffersResponse, error)
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchGetCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersBatchUpdateCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionOffersResponse, error)
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionOfferStatesResponse, error)
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersCreateCall
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersCreateCall
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersCreateCall
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Header() http.Header
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) OfferId(offerId string) *MonetizationSubscriptionsBasePlansOffersCreateCall
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsBasePlansOffersCreateCall
type MonetizationSubscriptionsBasePlansOffersDeactivateCall
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersDeactivateCall
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersDeactivateCall
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersDeleteCall
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersDeleteCall
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersDeleteCall
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Header() http.Header
type MonetizationSubscriptionsBasePlansOffersGetCall
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersGetCall
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersGetCall
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Header() http.Header
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBasePlansOffersGetCall
type MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Do(opts ...googleapi.CallOption) (*ListSubscriptionOffersResponse, error)
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Header() http.Header
func (c *MonetizationSubscriptionsBasePlansOffersListCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) PageSize(pageSize int64) *MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) PageToken(pageToken string) *MonetizationSubscriptionsBasePlansOffersListCall
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Pages(ctx context.Context, f func(*ListSubscriptionOffersResponse) error) error
type MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) AllowMissing(allowMissing bool) *MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Header() http.Header
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsBasePlansOffersPatchCall
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) UpdateMask(updateMask string) *MonetizationSubscriptionsBasePlansOffersPatchCall
type MonetizationSubscriptionsBasePlansOffersService
func NewMonetizationSubscriptionsBasePlansOffersService(s *Service) *MonetizationSubscriptionsBasePlansOffersService
func (r *MonetizationSubscriptionsBasePlansOffersService) Activate(packageName string, productId string, basePlanId string, offerId string, ...) *MonetizationSubscriptionsBasePlansOffersActivateCall
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchGet(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansOffersBatchGetCall
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchUpdate(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchUpdateStates(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall
func (r *MonetizationSubscriptionsBasePlansOffersService) Create(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansOffersCreateCall
func (r *MonetizationSubscriptionsBasePlansOffersService) Deactivate(packageName string, productId string, basePlanId string, offerId string, ...) *MonetizationSubscriptionsBasePlansOffersDeactivateCall
func (r *MonetizationSubscriptionsBasePlansOffersService) Delete(packageName string, productId string, basePlanId string, offerId string) *MonetizationSubscriptionsBasePlansOffersDeleteCall
func (r *MonetizationSubscriptionsBasePlansOffersService) Get(packageName string, productId string, basePlanId string, offerId string) *MonetizationSubscriptionsBasePlansOffersGetCall
func (r *MonetizationSubscriptionsBasePlansOffersService) List(packageName string, productId string, basePlanId string) *MonetizationSubscriptionsBasePlansOffersListCall
func (r *MonetizationSubscriptionsBasePlansOffersService) Patch(packageName string, productId string, basePlanId string, offerId string, ...) *MonetizationSubscriptionsBasePlansOffersPatchCall
type MonetizationSubscriptionsBasePlansService
func NewMonetizationSubscriptionsBasePlansService(s *Service) *MonetizationSubscriptionsBasePlansService
func (r *MonetizationSubscriptionsBasePlansService) Activate(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansActivateCall
func (r *MonetizationSubscriptionsBasePlansService) BatchMigratePrices(packageName string, productId string, ...) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall
func (r *MonetizationSubscriptionsBasePlansService) BatchUpdateStates(packageName string, productId string, ...) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall
func (r *MonetizationSubscriptionsBasePlansService) Deactivate(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansDeactivateCall
func (r *MonetizationSubscriptionsBasePlansService) Delete(packageName string, productId string, basePlanId string) *MonetizationSubscriptionsBasePlansDeleteCall
func (r *MonetizationSubscriptionsBasePlansService) MigratePrices(packageName string, productId string, basePlanId string, ...) *MonetizationSubscriptionsBasePlansMigratePricesCall
type MonetizationSubscriptionsBatchGetCall
func (c *MonetizationSubscriptionsBatchGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBatchGetCall
func (c *MonetizationSubscriptionsBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetSubscriptionsResponse, error)
func (c *MonetizationSubscriptionsBatchGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBatchGetCall
func (c *MonetizationSubscriptionsBatchGetCall) Header() http.Header
func (c *MonetizationSubscriptionsBatchGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBatchGetCall
func (c *MonetizationSubscriptionsBatchGetCall) ProductIds(productIds ...string) *MonetizationSubscriptionsBatchGetCall
type MonetizationSubscriptionsBatchUpdateCall
func (c *MonetizationSubscriptionsBatchUpdateCall) Context(ctx context.Context) *MonetizationSubscriptionsBatchUpdateCall
func (c *MonetizationSubscriptionsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionsResponse, error)
func (c *MonetizationSubscriptionsBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBatchUpdateCall
func (c *MonetizationSubscriptionsBatchUpdateCall) Header() http.Header
type MonetizationSubscriptionsCreateCall
func (c *MonetizationSubscriptionsCreateCall) Context(ctx context.Context) *MonetizationSubscriptionsCreateCall
func (c *MonetizationSubscriptionsCreateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsCreateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsCreateCall
func (c *MonetizationSubscriptionsCreateCall) Header() http.Header
func (c *MonetizationSubscriptionsCreateCall) ProductId(productId string) *MonetizationSubscriptionsCreateCall
func (c *MonetizationSubscriptionsCreateCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsCreateCall
type MonetizationSubscriptionsDeleteCall
func (c *MonetizationSubscriptionsDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsDeleteCall
func (c *MonetizationSubscriptionsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *MonetizationSubscriptionsDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsDeleteCall
func (c *MonetizationSubscriptionsDeleteCall) Header() http.Header
type MonetizationSubscriptionsGetCall
func (c *MonetizationSubscriptionsGetCall) Context(ctx context.Context) *MonetizationSubscriptionsGetCall
func (c *MonetizationSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsGetCall
func (c *MonetizationSubscriptionsGetCall) Header() http.Header
func (c *MonetizationSubscriptionsGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsGetCall
type MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) Context(ctx context.Context) *MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) Do(opts ...googleapi.CallOption) (*ListSubscriptionsResponse, error)
func (c *MonetizationSubscriptionsListCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) Header() http.Header
func (c *MonetizationSubscriptionsListCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) PageSize(pageSize int64) *MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) PageToken(pageToken string) *MonetizationSubscriptionsListCall
func (c *MonetizationSubscriptionsListCall) Pages(ctx context.Context, f func(*ListSubscriptionsResponse) error) error
func (c *MonetizationSubscriptionsListCall) ShowArchived(showArchived bool) *MonetizationSubscriptionsListCall
type MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) AllowMissing(allowMissing bool) *MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) Context(ctx context.Context) *MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) Do(opts ...googleapi.CallOption) (*Subscription, error)
func (c *MonetizationSubscriptionsPatchCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) Header() http.Header
func (c *MonetizationSubscriptionsPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsPatchCall
func (c *MonetizationSubscriptionsPatchCall) UpdateMask(updateMask string) *MonetizationSubscriptionsPatchCall
type MonetizationSubscriptionsService
func NewMonetizationSubscriptionsService(s *Service) *MonetizationSubscriptionsService
func (r *MonetizationSubscriptionsService) Archive(packageName string, productId string, ...) *MonetizationSubscriptionsArchiveCall
func (r *MonetizationSubscriptionsService) BatchGet(packageName string) *MonetizationSubscriptionsBatchGetCall
func (r *MonetizationSubscriptionsService) BatchUpdate(packageName string, ...) *MonetizationSubscriptionsBatchUpdateCall
func (r *MonetizationSubscriptionsService) Create(packageName string, subscription *Subscription) *MonetizationSubscriptionsCreateCall
func (r *MonetizationSubscriptionsService) Delete(packageName string, productId string) *MonetizationSubscriptionsDeleteCall
func (r *MonetizationSubscriptionsService) Get(packageName string, productId string) *MonetizationSubscriptionsGetCall
func (r *MonetizationSubscriptionsService) List(packageName string) *MonetizationSubscriptionsListCall
func (r *MonetizationSubscriptionsService) Patch(packageName string, productId string, subscription *Subscription) *MonetizationSubscriptionsPatchCall
type Money
func (s Money) MarshalJSON() ([]byte, error)
type MultiAbi
func (s MultiAbi) MarshalJSON() ([]byte, error)
type MultiAbiTargeting
func (s MultiAbiTargeting) MarshalJSON() ([]byte, error)
type OfferDetails
func (s OfferDetails) MarshalJSON() ([]byte, error)
type OfferPhase
func (s OfferPhase) MarshalJSON() ([]byte, error)
type OfferPhaseDetails
func (s OfferPhaseDetails) MarshalJSON() ([]byte, error)
type OfferTag
func (s OfferTag) MarshalJSON() ([]byte, error)
type OneTimeCode
type OneTimeExternalTransaction
func (s OneTimeExternalTransaction) MarshalJSON() ([]byte, error)
type OneTimeProduct
func (s OneTimeProduct) MarshalJSON() ([]byte, error)
type OneTimeProductBuyPurchaseOption
func (s OneTimeProductBuyPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductDiscountedOffer
func (s OneTimeProductDiscountedOffer) MarshalJSON() ([]byte, error)
type OneTimeProductListing
func (s OneTimeProductListing) MarshalJSON() ([]byte, error)
type OneTimeProductOffer
func (s OneTimeProductOffer) MarshalJSON() ([]byte, error)
type OneTimeProductOfferNoPriceOverrideOptions
type OneTimeProductOfferRegionalPricingAndAvailabilityConfig
func (s OneTimeProductOfferRegionalPricingAndAvailabilityConfig) MarshalJSON() ([]byte, error)
func (s *OneTimeProductOfferRegionalPricingAndAvailabilityConfig) UnmarshalJSON(data []byte) error
type OneTimeProductPreOrderOffer
func (s OneTimeProductPreOrderOffer) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOption
func (s OneTimeProductPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOptionNewRegionsConfig
func (s OneTimeProductPurchaseOptionNewRegionsConfig) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig
func (s OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig) MarshalJSON() ([]byte, error)
type OneTimeProductRentPurchaseOption
func (s OneTimeProductRentPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductTaxAndComplianceSettings
func (s OneTimeProductTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type OneTimePurchaseDetails
func (s OneTimePurchaseDetails) MarshalJSON() ([]byte, error)
type Order
func (s Order) MarshalJSON() ([]byte, error)
type OrderDetails
func (s OrderDetails) MarshalJSON() ([]byte, error)
type OrderHistory
func (s OrderHistory) MarshalJSON() ([]byte, error)
type OrdersBatchgetCall
func (c *OrdersBatchgetCall) Context(ctx context.Context) *OrdersBatchgetCall
func (c *OrdersBatchgetCall) Do(opts ...googleapi.CallOption) (*BatchGetOrdersResponse, error)
func (c *OrdersBatchgetCall) Fields(s ...googleapi.Field) *OrdersBatchgetCall
func (c *OrdersBatchgetCall) Header() http.Header
func (c *OrdersBatchgetCall) IfNoneMatch(entityTag string) *OrdersBatchgetCall
func (c *OrdersBatchgetCall) OrderIds(orderIds ...string) *OrdersBatchgetCall
type OrdersGetCall
func (c *OrdersGetCall) Context(ctx context.Context) *OrdersGetCall
func (c *OrdersGetCall) Do(opts ...googleapi.CallOption) (*Order, error)
func (c *OrdersGetCall) Fields(s ...googleapi.Field) *OrdersGetCall
func (c *OrdersGetCall) Header() http.Header
func (c *OrdersGetCall) IfNoneMatch(entityTag string) *OrdersGetCall
type OrdersRefundCall
func (c *OrdersRefundCall) Context(ctx context.Context) *OrdersRefundCall
func (c *OrdersRefundCall) Do(opts ...googleapi.CallOption) error
func (c *OrdersRefundCall) Fields(s ...googleapi.Field) *OrdersRefundCall
func (c *OrdersRefundCall) Header() http.Header
func (c *OrdersRefundCall) Revoke(revoke bool) *OrdersRefundCall
type OrdersService
func NewOrdersService(s *Service) *OrdersService
func (r *OrdersService) Batchget(packageName string) *OrdersBatchgetCall
func (r *OrdersService) Get(packageName string, orderId string) *OrdersGetCall
func (r *OrdersService) Refund(packageName string, orderId string) *OrdersRefundCall
type OtherRecurringProduct
type OtherRegionsBasePlanConfig
func (s OtherRegionsBasePlanConfig) MarshalJSON() ([]byte, error)
type OtherRegionsSubscriptionOfferConfig
func (s OtherRegionsSubscriptionOfferConfig) MarshalJSON() ([]byte, error)
type OtherRegionsSubscriptionOfferPhaseConfig
func (s OtherRegionsSubscriptionOfferPhaseConfig) MarshalJSON() ([]byte, error)
func (s *OtherRegionsSubscriptionOfferPhaseConfig) UnmarshalJSON(data []byte) error
type OtherRegionsSubscriptionOfferPhaseFreePriceOverride
type OtherRegionsSubscriptionOfferPhasePrices
func (s OtherRegionsSubscriptionOfferPhasePrices) MarshalJSON() ([]byte, error)
type OutOfAppPurchaseContext
func (s OutOfAppPurchaseContext) MarshalJSON() ([]byte, error)
type PageInfo
func (s PageInfo) MarshalJSON() ([]byte, error)
type PaidAppDetails
type PartialRefund
func (s PartialRefund) MarshalJSON() ([]byte, error)
type PartialRefundEvent
func (s PartialRefundEvent) MarshalJSON() ([]byte, error)
type PausedStateContext
func (s PausedStateContext) MarshalJSON() ([]byte, error)
type PendingCancellation
type PointsDetails
func (s PointsDetails) MarshalJSON() ([]byte, error)
type PreorderDetails
type PreorderOfferDetails
func (s PreorderOfferDetails) MarshalJSON() ([]byte, error)
type PrepaidBasePlanType
func (s PrepaidBasePlanType) MarshalJSON() ([]byte, error)
type PrepaidPlan
func (s PrepaidPlan) MarshalJSON() ([]byte, error)
type Price
func (s Price) MarshalJSON() ([]byte, error)
type PriceStepUpConsentDetails
func (s PriceStepUpConsentDetails) MarshalJSON() ([]byte, error)
type ProcessedEvent
func (s ProcessedEvent) MarshalJSON() ([]byte, error)
type ProductLineItem
func (s ProductLineItem) MarshalJSON() ([]byte, error)
type ProductOfferDetails
func (s ProductOfferDetails) MarshalJSON() ([]byte, error)
type ProductPurchase
func (s ProductPurchase) MarshalJSON() ([]byte, error)
type ProductPurchaseV2
func (s ProductPurchaseV2) MarshalJSON() ([]byte, error)
type ProductPurchasesAcknowledgeRequest
func (s ProductPurchasesAcknowledgeRequest) MarshalJSON() ([]byte, error)
type ProrationPeriodDetails
func (s ProrationPeriodDetails) MarshalJSON() ([]byte, error)
type ProrationPeriodOfferPhase
func (s ProrationPeriodOfferPhase) MarshalJSON() ([]byte, error)
type PurchaseOptionTaxAndComplianceSettings
func (s PurchaseOptionTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type PurchaseStateContext
func (s PurchaseStateContext) MarshalJSON() ([]byte, error)
type PurchasesProductsAcknowledgeCall
func (c *PurchasesProductsAcknowledgeCall) Context(ctx context.Context) *PurchasesProductsAcknowledgeCall
func (c *PurchasesProductsAcknowledgeCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesProductsAcknowledgeCall) Fields(s ...googleapi.Field) *PurchasesProductsAcknowledgeCall
func (c *PurchasesProductsAcknowledgeCall) Header() http.Header
type PurchasesProductsConsumeCall
func (c *PurchasesProductsConsumeCall) Context(ctx context.Context) *PurchasesProductsConsumeCall
func (c *PurchasesProductsConsumeCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesProductsConsumeCall) Fields(s ...googleapi.Field) *PurchasesProductsConsumeCall
func (c *PurchasesProductsConsumeCall) Header() http.Header
type PurchasesProductsGetCall
func (c *PurchasesProductsGetCall) Context(ctx context.Context) *PurchasesProductsGetCall
func (c *PurchasesProductsGetCall) Do(opts ...googleapi.CallOption) (*ProductPurchase, error)
func (c *PurchasesProductsGetCall) Fields(s ...googleapi.Field) *PurchasesProductsGetCall
func (c *PurchasesProductsGetCall) Header() http.Header
func (c *PurchasesProductsGetCall) IfNoneMatch(entityTag string) *PurchasesProductsGetCall
type PurchasesProductsService
func NewPurchasesProductsService(s *Service) *PurchasesProductsService
func (r *PurchasesProductsService) Acknowledge(packageName string, productId string, token string, ...) *PurchasesProductsAcknowledgeCall
func (r *PurchasesProductsService) Consume(packageName string, productId string, token string) *PurchasesProductsConsumeCall
func (r *PurchasesProductsService) Get(packageName string, productId string, token string) *PurchasesProductsGetCall
type PurchasesProductsv2Getproductpurchasev2Call
func (c *PurchasesProductsv2Getproductpurchasev2Call) Context(ctx context.Context) *PurchasesProductsv2Getproductpurchasev2Call
func (c *PurchasesProductsv2Getproductpurchasev2Call) Do(opts ...googleapi.CallOption) (*ProductPurchaseV2, error)
func (c *PurchasesProductsv2Getproductpurchasev2Call) Fields(s ...googleapi.Field) *PurchasesProductsv2Getproductpurchasev2Call
func (c *PurchasesProductsv2Getproductpurchasev2Call) Header() http.Header
func (c *PurchasesProductsv2Getproductpurchasev2Call) IfNoneMatch(entityTag string) *PurchasesProductsv2Getproductpurchasev2Call
type PurchasesProductsv2Service
func NewPurchasesProductsv2Service(s *Service) *PurchasesProductsv2Service
func (r *PurchasesProductsv2Service) Getproductpurchasev2(packageName string, token string) *PurchasesProductsv2Getproductpurchasev2Call
type PurchasesService
func NewPurchasesService(s *Service) *PurchasesService
type PurchasesSubscriptionsAcknowledgeCall
func (c *PurchasesSubscriptionsAcknowledgeCall) Context(ctx context.Context) *PurchasesSubscriptionsAcknowledgeCall
func (c *PurchasesSubscriptionsAcknowledgeCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesSubscriptionsAcknowledgeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsAcknowledgeCall
func (c *PurchasesSubscriptionsAcknowledgeCall) Header() http.Header
type PurchasesSubscriptionsCancelCall
func (c *PurchasesSubscriptionsCancelCall) Context(ctx context.Context) *PurchasesSubscriptionsCancelCall
func (c *PurchasesSubscriptionsCancelCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesSubscriptionsCancelCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsCancelCall
func (c *PurchasesSubscriptionsCancelCall) Header() http.Header
type PurchasesSubscriptionsDeferCall
func (c *PurchasesSubscriptionsDeferCall) Context(ctx context.Context) *PurchasesSubscriptionsDeferCall
func (c *PurchasesSubscriptionsDeferCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchasesDeferResponse, error)
func (c *PurchasesSubscriptionsDeferCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsDeferCall
func (c *PurchasesSubscriptionsDeferCall) Header() http.Header
type PurchasesSubscriptionsGetCall
func (c *PurchasesSubscriptionsGetCall) Context(ctx context.Context) *PurchasesSubscriptionsGetCall
func (c *PurchasesSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchase, error)
func (c *PurchasesSubscriptionsGetCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsGetCall
func (c *PurchasesSubscriptionsGetCall) Header() http.Header
func (c *PurchasesSubscriptionsGetCall) IfNoneMatch(entityTag string) *PurchasesSubscriptionsGetCall
type PurchasesSubscriptionsRefundCall
func (c *PurchasesSubscriptionsRefundCall) Context(ctx context.Context) *PurchasesSubscriptionsRefundCall
func (c *PurchasesSubscriptionsRefundCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesSubscriptionsRefundCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsRefundCall
func (c *PurchasesSubscriptionsRefundCall) Header() http.Header
type PurchasesSubscriptionsRevokeCall
func (c *PurchasesSubscriptionsRevokeCall) Context(ctx context.Context) *PurchasesSubscriptionsRevokeCall
func (c *PurchasesSubscriptionsRevokeCall) Do(opts ...googleapi.CallOption) error
func (c *PurchasesSubscriptionsRevokeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsRevokeCall
func (c *PurchasesSubscriptionsRevokeCall) Header() http.Header
type PurchasesSubscriptionsService
func NewPurchasesSubscriptionsService(s *Service) *PurchasesSubscriptionsService
func (r *PurchasesSubscriptionsService) Acknowledge(packageName string, subscriptionId string, token string, ...) *PurchasesSubscriptionsAcknowledgeCall
func (r *PurchasesSubscriptionsService) Cancel(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsCancelCall
func (r *PurchasesSubscriptionsService) Defer(packageName string, subscriptionId string, token string, ...) *PurchasesSubscriptionsDeferCall
func (r *PurchasesSubscriptionsService) Get(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsGetCall
func (r *PurchasesSubscriptionsService) Refund(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsRefundCall
func (r *PurchasesSubscriptionsService) Revoke(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsRevokeCall
type PurchasesSubscriptionsv2CancelCall
func (c *PurchasesSubscriptionsv2CancelCall) Context(ctx context.Context) *PurchasesSubscriptionsv2CancelCall
func (c *PurchasesSubscriptionsv2CancelCall) Do(opts ...googleapi.CallOption) (*CancelSubscriptionPurchaseResponse, error)
func (c *PurchasesSubscriptionsv2CancelCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2CancelCall
func (c *PurchasesSubscriptionsv2CancelCall) Header() http.Header
type PurchasesSubscriptionsv2DeferCall
func (c *PurchasesSubscriptionsv2DeferCall) Context(ctx context.Context) *PurchasesSubscriptionsv2DeferCall
func (c *PurchasesSubscriptionsv2DeferCall) Do(opts ...googleapi.CallOption) (*DeferSubscriptionPurchaseResponse, error)
func (c *PurchasesSubscriptionsv2DeferCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2DeferCall
func (c *PurchasesSubscriptionsv2DeferCall) Header() http.Header
type PurchasesSubscriptionsv2GetCall
func (c *PurchasesSubscriptionsv2GetCall) Context(ctx context.Context) *PurchasesSubscriptionsv2GetCall
func (c *PurchasesSubscriptionsv2GetCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchaseV2, error)
func (c *PurchasesSubscriptionsv2GetCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2GetCall
func (c *PurchasesSubscriptionsv2GetCall) Header() http.Header
func (c *PurchasesSubscriptionsv2GetCall) IfNoneMatch(entityTag string) *PurchasesSubscriptionsv2GetCall
type PurchasesSubscriptionsv2RevokeCall
func (c *PurchasesSubscriptionsv2RevokeCall) Context(ctx context.Context) *PurchasesSubscriptionsv2RevokeCall
func (c *PurchasesSubscriptionsv2RevokeCall) Do(opts ...googleapi.CallOption) (*RevokeSubscriptionPurchaseResponse, error)
func (c *PurchasesSubscriptionsv2RevokeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2RevokeCall
func (c *PurchasesSubscriptionsv2RevokeCall) Header() http.Header
type PurchasesSubscriptionsv2Service
func NewPurchasesSubscriptionsv2Service(s *Service) *PurchasesSubscriptionsv2Service
func (r *PurchasesSubscriptionsv2Service) Cancel(packageName string, token string, ...) *PurchasesSubscriptionsv2CancelCall
func (r *PurchasesSubscriptionsv2Service) Defer(packageName string, token string, ...) *PurchasesSubscriptionsv2DeferCall
func (r *PurchasesSubscriptionsv2Service) Get(packageName string, token string) *PurchasesSubscriptionsv2GetCall
func (r *PurchasesSubscriptionsv2Service) Revoke(packageName string, token string, ...) *PurchasesSubscriptionsv2RevokeCall
type PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Context(ctx context.Context) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Do(opts ...googleapi.CallOption) (*VoidedPurchasesListResponse, error)
func (c *PurchasesVoidedpurchasesListCall) EndTime(endTime int64) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Fields(s ...googleapi.Field) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Header() http.Header
func (c *PurchasesVoidedpurchasesListCall) IfNoneMatch(entityTag string) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) IncludeQuantityBasedPartialRefund(includeQuantityBasedPartialRefund bool) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) MaxResults(maxResults int64) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) StartIndex(startIndex int64) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) StartTime(startTime int64) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Token(token string) *PurchasesVoidedpurchasesListCall
func (c *PurchasesVoidedpurchasesListCall) Type(type_ int64) *PurchasesVoidedpurchasesListCall
type PurchasesVoidedpurchasesService
func NewPurchasesVoidedpurchasesService(s *Service) *PurchasesVoidedpurchasesService
func (r *PurchasesVoidedpurchasesService) List(packageName string) *PurchasesVoidedpurchasesListCall
type RecurringExternalTransaction
func (s RecurringExternalTransaction) MarshalJSON() ([]byte, error)
type RefundDetails
func (s RefundDetails) MarshalJSON() ([]byte, error)
type RefundEvent
func (s RefundEvent) MarshalJSON() ([]byte, error)
type RefundExternalTransactionRequest
func (s RefundExternalTransactionRequest) MarshalJSON() ([]byte, error)
type RegionalBasePlanConfig
func (s RegionalBasePlanConfig) MarshalJSON() ([]byte, error)
type RegionalPriceMigrationConfig
func (s RegionalPriceMigrationConfig) MarshalJSON() ([]byte, error)
type RegionalProductAgeRatingInfo
func (s RegionalProductAgeRatingInfo) MarshalJSON() ([]byte, error)
type RegionalSubscriptionOfferConfig
func (s RegionalSubscriptionOfferConfig) MarshalJSON() ([]byte, error)
type RegionalSubscriptionOfferPhaseConfig
func (s RegionalSubscriptionOfferPhaseConfig) MarshalJSON() ([]byte, error)
func (s *RegionalSubscriptionOfferPhaseConfig) UnmarshalJSON(data []byte) error
type RegionalSubscriptionOfferPhaseFreePriceOverride
type RegionalTaxConfig
func (s RegionalTaxConfig) MarshalJSON() ([]byte, error)
type RegionalTaxRateInfo
func (s RegionalTaxRateInfo) MarshalJSON() ([]byte, error)
type Regions
func (s Regions) MarshalJSON() ([]byte, error)
type RegionsVersion
func (s RegionsVersion) MarshalJSON() ([]byte, error)
type RemoteInAppUpdate
func (s RemoteInAppUpdate) MarshalJSON() ([]byte, error)
type RemoteInAppUpdateData
func (s RemoteInAppUpdateData) MarshalJSON() ([]byte, error)
type RemoteInAppUpdateDataPerBundle
func (s RemoteInAppUpdateDataPerBundle) MarshalJSON() ([]byte, error)
type RentOfferDetails
type RentalDetails
type ReplacementCancellation
type RestrictedPaymentCountries
func (s RestrictedPaymentCountries) MarshalJSON() ([]byte, error)
type Review
func (s Review) MarshalJSON() ([]byte, error)
type ReviewReplyResult
func (s ReviewReplyResult) MarshalJSON() ([]byte, error)
type ReviewsGetCall
func (c *ReviewsGetCall) Context(ctx context.Context) *ReviewsGetCall
func (c *ReviewsGetCall) Do(opts ...googleapi.CallOption) (*Review, error)
func (c *ReviewsGetCall) Fields(s ...googleapi.Field) *ReviewsGetCall
func (c *ReviewsGetCall) Header() http.Header
func (c *ReviewsGetCall) IfNoneMatch(entityTag string) *ReviewsGetCall
func (c *ReviewsGetCall) TranslationLanguage(translationLanguage string) *ReviewsGetCall
type ReviewsListCall
func (c *ReviewsListCall) Context(ctx context.Context) *ReviewsListCall
func (c *ReviewsListCall) Do(opts ...googleapi.CallOption) (*ReviewsListResponse, error)
func (c *ReviewsListCall) Fields(s ...googleapi.Field) *ReviewsListCall
func (c *ReviewsListCall) Header() http.Header
func (c *ReviewsListCall) IfNoneMatch(entityTag string) *ReviewsListCall
func (c *ReviewsListCall) MaxResults(maxResults int64) *ReviewsListCall
func (c *ReviewsListCall) StartIndex(startIndex int64) *ReviewsListCall
func (c *ReviewsListCall) Token(token string) *ReviewsListCall
func (c *ReviewsListCall) TranslationLanguage(translationLanguage string) *ReviewsListCall
type ReviewsListResponse
func (s ReviewsListResponse) MarshalJSON() ([]byte, error)
type ReviewsReplyCall
func (c *ReviewsReplyCall) Context(ctx context.Context) *ReviewsReplyCall
func (c *ReviewsReplyCall) Do(opts ...googleapi.CallOption) (*ReviewsReplyResponse, error)
func (c *ReviewsReplyCall) Fields(s ...googleapi.Field) *ReviewsReplyCall
func (c *ReviewsReplyCall) Header() http.Header
type ReviewsReplyRequest
func (s ReviewsReplyRequest) MarshalJSON() ([]byte, error)
type ReviewsReplyResponse
func (s ReviewsReplyResponse) MarshalJSON() ([]byte, error)
type ReviewsService
func NewReviewsService(s *Service) *ReviewsService
func (r *ReviewsService) Get(packageName string, reviewId string) *ReviewsGetCall
func (r *ReviewsService) List(packageName string) *ReviewsListCall
func (r *ReviewsService) Reply(packageName string, reviewId string, reviewsreplyrequest *ReviewsReplyRequest) *ReviewsReplyCall
type RevocationContext
func (s RevocationContext) MarshalJSON() ([]byte, error)
type RevocationContextFullRefund
type RevocationContextItemBasedRefund
func (s RevocationContextItemBasedRefund) MarshalJSON() ([]byte, error)
type RevocationContextProratedRefund
type RevokeSubscriptionPurchaseRequest
func (s RevokeSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type RevokeSubscriptionPurchaseResponse
type SafetyLabelsUpdateRequest
func (s SafetyLabelsUpdateRequest) MarshalJSON() ([]byte, error)
type SafetyLabelsUpdateResponse
type ScreenDensity
func (s ScreenDensity) MarshalJSON() ([]byte, error)
type ScreenDensityTargeting
func (s ScreenDensityTargeting) MarshalJSON() ([]byte, error)
type SdkVersion
func (s SdkVersion) MarshalJSON() ([]byte, error)
type SdkVersionTargeting
func (s SdkVersionTargeting) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SignupPromotion
func (s SignupPromotion) MarshalJSON() ([]byte, error)
type SplitApkMetadata
func (s SplitApkMetadata) MarshalJSON() ([]byte, error)
type SplitApkVariant
func (s SplitApkVariant) MarshalJSON() ([]byte, error)
type StandaloneApkMetadata
func (s StandaloneApkMetadata) MarshalJSON() ([]byte, error)
type SubscribeWithGoogleInfo
func (s SubscribeWithGoogleInfo) MarshalJSON() ([]byte, error)
type Subscription
func (s Subscription) MarshalJSON() ([]byte, error)
type SubscriptionCancelSurveyResult
func (s SubscriptionCancelSurveyResult) MarshalJSON() ([]byte, error)
type SubscriptionDeferralInfo
func (s SubscriptionDeferralInfo) MarshalJSON() ([]byte, error)
type SubscriptionDetails
func (s SubscriptionDetails) MarshalJSON() ([]byte, error)
type SubscriptionItemPriceChangeDetails
func (s SubscriptionItemPriceChangeDetails) MarshalJSON() ([]byte, error)
type SubscriptionListing
func (s SubscriptionListing) MarshalJSON() ([]byte, error)
type SubscriptionOffer
func (s SubscriptionOffer) MarshalJSON() ([]byte, error)
type SubscriptionOfferPhase
func (s SubscriptionOfferPhase) MarshalJSON() ([]byte, error)
type SubscriptionOfferTargeting
func (s SubscriptionOfferTargeting) MarshalJSON() ([]byte, error)
type SubscriptionPriceChange
func (s SubscriptionPriceChange) MarshalJSON() ([]byte, error)
type SubscriptionPurchase
func (s SubscriptionPurchase) MarshalJSON() ([]byte, error)
type SubscriptionPurchaseLineItem
func (s SubscriptionPurchaseLineItem) MarshalJSON() ([]byte, error)
type SubscriptionPurchaseV2
func (s SubscriptionPurchaseV2) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesAcknowledgeRequest
func (s SubscriptionPurchasesAcknowledgeRequest) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesDeferRequest
func (s SubscriptionPurchasesDeferRequest) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesDeferResponse
func (s SubscriptionPurchasesDeferResponse) MarshalJSON() ([]byte, error)
type SubscriptionTaxAndComplianceSettings
func (s SubscriptionTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type SystemApkOptions
func (s SystemApkOptions) MarshalJSON() ([]byte, error)
type SystemApksListResponse
func (s SystemApksListResponse) MarshalJSON() ([]byte, error)
type SystemFeature
func (s SystemFeature) MarshalJSON() ([]byte, error)
type SystemInitiatedCancellation
type SystemOnChip
func (s SystemOnChip) MarshalJSON() ([]byte, error)
type SystemapksService
func NewSystemapksService(s *Service) *SystemapksService
type SystemapksVariantsCreateCall
func (c *SystemapksVariantsCreateCall) Context(ctx context.Context) *SystemapksVariantsCreateCall
func (c *SystemapksVariantsCreateCall) Do(opts ...googleapi.CallOption) (*Variant, error)
func (c *SystemapksVariantsCreateCall) Fields(s ...googleapi.Field) *SystemapksVariantsCreateCall
func (c *SystemapksVariantsCreateCall) Header() http.Header
type SystemapksVariantsDownloadCall
func (c *SystemapksVariantsDownloadCall) Context(ctx context.Context) *SystemapksVariantsDownloadCall
func (c *SystemapksVariantsDownloadCall) Do(opts ...googleapi.CallOption) error
func (c *SystemapksVariantsDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)
func (c *SystemapksVariantsDownloadCall) Fields(s ...googleapi.Field) *SystemapksVariantsDownloadCall
func (c *SystemapksVariantsDownloadCall) Header() http.Header
func (c *SystemapksVariantsDownloadCall) IfNoneMatch(entityTag string) *SystemapksVariantsDownloadCall
type SystemapksVariantsGetCall
func (c *SystemapksVariantsGetCall) Context(ctx context.Context) *SystemapksVariantsGetCall
func (c *SystemapksVariantsGetCall) Do(opts ...googleapi.CallOption) (*Variant, error)
func (c *SystemapksVariantsGetCall) Fields(s ...googleapi.Field) *SystemapksVariantsGetCall
func (c *SystemapksVariantsGetCall) Header() http.Header
func (c *SystemapksVariantsGetCall) IfNoneMatch(entityTag string) *SystemapksVariantsGetCall
type SystemapksVariantsListCall
func (c *SystemapksVariantsListCall) Context(ctx context.Context) *SystemapksVariantsListCall
func (c *SystemapksVariantsListCall) Do(opts ...googleapi.CallOption) (*SystemApksListResponse, error)
func (c *SystemapksVariantsListCall) Fields(s ...googleapi.Field) *SystemapksVariantsListCall
func (c *SystemapksVariantsListCall) Header() http.Header
func (c *SystemapksVariantsListCall) IfNoneMatch(entityTag string) *SystemapksVariantsListCall
type SystemapksVariantsService
func NewSystemapksVariantsService(s *Service) *SystemapksVariantsService
func (r *SystemapksVariantsService) Create(packageName string, versionCode int64, variant *Variant) *SystemapksVariantsCreateCall
func (r *SystemapksVariantsService) Download(packageName string, versionCode int64, variantId int64) *SystemapksVariantsDownloadCall
func (r *SystemapksVariantsService) Get(packageName string, versionCode int64, variantId int64) *SystemapksVariantsGetCall
func (r *SystemapksVariantsService) List(packageName string, versionCode int64) *SystemapksVariantsListCall
type Targeting
func (s Targeting) MarshalJSON() ([]byte, error)
type TargetingInfo
func (s TargetingInfo) MarshalJSON() ([]byte, error)
type TargetingRuleScope
func (s TargetingRuleScope) MarshalJSON() ([]byte, error)
type TargetingRuleScopeAnySubscriptionInApp
type TargetingRuleScopeThisSubscription
type TargetingUpdate
func (s TargetingUpdate) MarshalJSON() ([]byte, error)
type TestPurchase
type TestPurchaseContext
func (s TestPurchaseContext) MarshalJSON() ([]byte, error)
type Testers
func (s Testers) MarshalJSON() ([]byte, error)
type TextureCompressionFormat
func (s TextureCompressionFormat) MarshalJSON() ([]byte, error)
type TextureCompressionFormatTargeting
func (s TextureCompressionFormatTargeting) MarshalJSON() ([]byte, error)
type Timestamp
func (s Timestamp) MarshalJSON() ([]byte, error)
type TokenPagination
func (s TokenPagination) MarshalJSON() ([]byte, error)
type Track
func (s Track) MarshalJSON() ([]byte, error)
type TrackConfig
func (s TrackConfig) MarshalJSON() ([]byte, error)
type TrackCountryAvailability
func (s TrackCountryAvailability) MarshalJSON() ([]byte, error)
type TrackRelease
func (s TrackRelease) MarshalJSON() ([]byte, error)
func (s *TrackRelease) UnmarshalJSON(data []byte) error
type TrackTargetedCountry
func (s TrackTargetedCountry) MarshalJSON() ([]byte, error)
type TracksListResponse
func (s TracksListResponse) MarshalJSON() ([]byte, error)
type UpdateBasePlanStateRequest
func (s UpdateBasePlanStateRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductOfferRequest
func (s UpdateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductOfferStateRequest
func (s UpdateOneTimeProductOfferStateRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductRequest
func (s UpdateOneTimeProductRequest) MarshalJSON() ([]byte, error)
type UpdatePurchaseOptionStateRequest
func (s UpdatePurchaseOptionStateRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionOfferRequest
func (s UpdateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionOfferStateRequest
func (s UpdateSubscriptionOfferStateRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionRequest
func (s UpdateSubscriptionRequest) MarshalJSON() ([]byte, error)
type UpgradeTargetingRule
func (s UpgradeTargetingRule) MarshalJSON() ([]byte, error)
type User
func (s User) MarshalJSON() ([]byte, error)
type UserComment
func (s UserComment) MarshalJSON() ([]byte, error)
type UserCountriesTargeting
func (s UserCountriesTargeting) MarshalJSON() ([]byte, error)
type UserCountrySet
func (s UserCountrySet) MarshalJSON() ([]byte, error)
type UserInitiatedCancellation
func (s UserInitiatedCancellation) MarshalJSON() ([]byte, error)
type UsersCreateCall
func (c *UsersCreateCall) Context(ctx context.Context) *UsersCreateCall
func (c *UsersCreateCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersCreateCall) Fields(s ...googleapi.Field) *UsersCreateCall
func (c *UsersCreateCall) Header() http.Header
type UsersDeleteCall
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall
func (c *UsersDeleteCall) Header() http.Header
type UsersListCall
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*ListUsersResponse, error)
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall
func (c *UsersListCall) Header() http.Header
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall
func (c *UsersListCall) PageSize(pageSize int64) *UsersListCall
func (c *UsersListCall) PageToken(pageToken string) *UsersListCall
func (c *UsersListCall) Pages(ctx context.Context, f func(*ListUsersResponse) error) error
type UsersPatchCall
func (c *UsersPatchCall) Context(ctx context.Context) *UsersPatchCall
func (c *UsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)
func (c *UsersPatchCall) Fields(s ...googleapi.Field) *UsersPatchCall
func (c *UsersPatchCall) Header() http.Header
func (c *UsersPatchCall) UpdateMask(updateMask string) *UsersPatchCall
type UsersService
func NewUsersService(s *Service) *UsersService
func (r *UsersService) Create(parent string, user *User) *UsersCreateCall
func (r *UsersService) Delete(name string) *UsersDeleteCall
func (r *UsersService) List(parent string) *UsersListCall
func (r *UsersService) Patch(name string, user *User) *UsersPatchCall
type UsesPermission
func (s UsesPermission) MarshalJSON() ([]byte, error)
type VanityCode
func (s VanityCode) MarshalJSON() ([]byte, error)
type Variant
func (s Variant) MarshalJSON() ([]byte, error)
type VariantTargeting
func (s VariantTargeting) MarshalJSON() ([]byte, error)
type VoidedPurchase
func (s VoidedPurchase) MarshalJSON() ([]byte, error)
type VoidedPurchasesListResponse
func (s VoidedPurchasesListResponse) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// View and manage your Google Play Developer account
	AndroidpublisherScope = "https://www.googleapis.com/auth/androidpublisher"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Abi ¶
added in v0.130.0
type Abi struct {
	// Alias: Alias for an abi.
	//
	// Possible values:
	//   "UNSPECIFIED_CPU_ARCHITECTURE" - Unspecified abi.
	//   "ARMEABI" - ARMEABI abi.
	//   "ARMEABI_V7A" - ARMEABI_V7A abi.
	//   "ARM64_V8A" - ARM64_V8A abi.
	//   "X86" - X86 abi.
	//   "X86_64" - X86_64 abi.
	//   "RISCV64" - RISCV64 abi.
	Alias string `json:"alias,omitempty"`
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

Abi: Represents an Abi.

func (Abi) MarshalJSON ¶
added in v0.130.0
func (s Abi) MarshalJSON() ([]byte, error)
type AbiTargeting ¶
added in v0.130.0
type AbiTargeting struct {
	// Alternatives: Targeting of other sibling directories that were in the
	// Bundle. For main splits this is targeting of other main splits.
	Alternatives []*Abi `json:"alternatives,omitempty"`
	// Value: Value of an abi.
	Value []*Abi `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AbiTargeting: Targeting based on Abi.

func (AbiTargeting) MarshalJSON ¶
added in v0.130.0
func (s AbiTargeting) MarshalJSON() ([]byte, error)
type AcquisitionTargetingRule ¶
added in v0.80.0
type AcquisitionTargetingRule struct {
	// Scope: Required. The scope of subscriptions this rule considers. Only allows
	// "this subscription" and "any subscription in app".
	Scope *TargetingRuleScope `json:"scope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Scope") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Scope") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AcquisitionTargetingRule: Represents a targeting rule of the form: User never had {scope} before.

func (AcquisitionTargetingRule) MarshalJSON ¶
added in v0.80.0
func (s AcquisitionTargetingRule) MarshalJSON() ([]byte, error)
type ActivateBasePlanRequest ¶
added in v0.80.0
type ActivateBasePlanRequest struct {
	// BasePlanId: Required. The unique base plan ID of the base plan to activate.
	BasePlanId string `json:"basePlanId,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the base plan to
	// activate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent subscription (ID) of the base plan to
	// activate.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ActivateBasePlanRequest: Request message for ActivateBasePlan.

func (ActivateBasePlanRequest) MarshalJSON ¶
added in v0.154.0
func (s ActivateBasePlanRequest) MarshalJSON() ([]byte, error)
type ActivateOneTimeProductOfferRequest ¶
added in v0.244.0
type ActivateOneTimeProductOfferRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The offer ID of the offer to activate.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to
	// activate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the offer to
	// activate.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The parent purchase option (ID) of the offer to
	// activate.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ActivateOneTimeProductOfferRequest: Request message for ActivateOneTimeProductOffer.

func (ActivateOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s ActivateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type ActivatePurchaseOptionRequest ¶
added in v0.244.0
type ActivatePurchaseOptionRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the purchase option
	// to activate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the purchase option
	// to activate.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The purchase option ID of the purchase option to
	// activate.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ActivatePurchaseOptionRequest: Request message for UpdatePurchaseOptionState.

func (ActivatePurchaseOptionRequest) MarshalJSON ¶
added in v0.244.0
func (s ActivatePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type ActivateSubscriptionOfferRequest ¶
added in v0.80.0
type ActivateSubscriptionOfferRequest struct {
	// BasePlanId: Required. The parent base plan (ID) of the offer to activate.
	BasePlanId string `json:"basePlanId,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The unique offer ID of the offer to activate.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to
	// activate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent subscription (ID) of the offer to activate.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ActivateSubscriptionOfferRequest: Request message for ActivateSubscriptionOffer.

func (ActivateSubscriptionOfferRequest) MarshalJSON ¶
added in v0.154.0
func (s ActivateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type AddTargetingRequest ¶
added in v0.156.0
type AddTargetingRequest struct {
	// TargetingUpdate: Specifies targeting updates such as regions, android sdk
	// versions etc.
	TargetingUpdate *TargetingUpdate `json:"targetingUpdate,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TargetingUpdate") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TargetingUpdate") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AddTargetingRequest: Request message for AddTargeting.

func (AddTargetingRequest) MarshalJSON ¶
added in v0.156.0
func (s AddTargetingRequest) MarshalJSON() ([]byte, error)
type AddTargetingResponse ¶
added in v0.156.0
type AddTargetingResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

AddTargetingResponse: Response message for AddTargeting.

type AllUsers ¶
added in v0.156.0
type AllUsers struct {
	// IsAllUsersRequested: Required. Set to true if all set of users are needed.
	IsAllUsersRequested bool `json:"isAllUsersRequested,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IsAllUsersRequested") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsAllUsersRequested") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AllUsers: Object representation to describe all set of users.

func (AllUsers) MarshalJSON ¶
added in v0.156.0
func (s AllUsers) MarshalJSON() ([]byte, error)
type AndroidSdks ¶
added in v0.156.0
type AndroidSdks struct {
	// SdkLevels: Android api levels of devices targeted by recovery action. See
	// https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels
	// for different api levels in android.
	SdkLevels googleapi.Int64s `json:"sdkLevels,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SdkLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SdkLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AndroidSdks: Android api level targeting data for app recovery action targeting.

func (AndroidSdks) MarshalJSON ¶
added in v0.156.0
func (s AndroidSdks) MarshalJSON() ([]byte, error)
type Apk ¶
type Apk struct {
	// Binary: Information about the binary payload of this APK.
	Binary *ApkBinary `json:"binary,omitempty"`
	// VersionCode: The version code of the APK, as specified in the manifest file.
	VersionCode int64 `json:"versionCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Binary") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Binary") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Apk: Information about an APK. The resource for ApksService.

func (Apk) MarshalJSON ¶
func (s Apk) MarshalJSON() ([]byte, error)
type ApkBinary ¶
type ApkBinary struct {
	// Sha1: A sha1 hash of the APK payload, encoded as a hex string and matching
	// the output of the sha1sum command.
	Sha1 string `json:"sha1,omitempty"`
	// Sha256: A sha256 hash of the APK payload, encoded as a hex string and
	// matching the output of the sha256sum command.
	Sha256 string `json:"sha256,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Sha1") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Sha1") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApkBinary: Represents the binary payload of an APK.

func (ApkBinary) MarshalJSON ¶
func (s ApkBinary) MarshalJSON() ([]byte, error)
type ApkDescription ¶
added in v0.130.0
type ApkDescription struct {
	// AssetSliceMetadata: Set only for asset slices.
	AssetSliceMetadata *SplitApkMetadata `json:"assetSliceMetadata,omitempty"`
	// InstantApkMetadata: Set only for Instant split APKs.
	InstantApkMetadata *SplitApkMetadata `json:"instantApkMetadata,omitempty"`
	// Path: Path of the Apk, will be in the following format: .apk where
	// DownloadId is the ID used to download the apk using GeneratedApks.Download
	// API.
	Path string `json:"path,omitempty"`
	// SplitApkMetadata: Set only for Split APKs.
	SplitApkMetadata *SplitApkMetadata `json:"splitApkMetadata,omitempty"`
	// StandaloneApkMetadata: Set only for standalone APKs.
	StandaloneApkMetadata *StandaloneApkMetadata `json:"standaloneApkMetadata,omitempty"`
	// Targeting: Apk-level targeting.
	Targeting *ApkTargeting `json:"targeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AssetSliceMetadata") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssetSliceMetadata") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApkDescription: Description of the created apks.

func (ApkDescription) MarshalJSON ¶
added in v0.130.0
func (s ApkDescription) MarshalJSON() ([]byte, error)
type ApkSet ¶
added in v0.130.0
type ApkSet struct {
	// ApkDescription: Description of the generated apks.
	ApkDescription []*ApkDescription `json:"apkDescription,omitempty"`
	// ModuleMetadata: Metadata about the module represented by this ApkSet
	ModuleMetadata *ModuleMetadata `json:"moduleMetadata,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApkDescription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApkDescription") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApkSet: A set of apks representing a module.

func (ApkSet) MarshalJSON ¶
added in v0.130.0
func (s ApkSet) MarshalJSON() ([]byte, error)
type ApkTargeting ¶
added in v0.130.0
type ApkTargeting struct {
	// AbiTargeting: The abi that the apk targets
	AbiTargeting *AbiTargeting `json:"abiTargeting,omitempty"`
	// LanguageTargeting: The language that the apk targets
	LanguageTargeting *LanguageTargeting `json:"languageTargeting,omitempty"`
	// MultiAbiTargeting: Multi-api-level targeting.
	MultiAbiTargeting *MultiAbiTargeting `json:"multiAbiTargeting,omitempty"`
	// ScreenDensityTargeting: The screen density that this apk supports.
	ScreenDensityTargeting *ScreenDensityTargeting `json:"screenDensityTargeting,omitempty"`
	// SdkVersionTargeting: The sdk version that the apk targets
	SdkVersionTargeting *SdkVersionTargeting `json:"sdkVersionTargeting,omitempty"`
	// TextureCompressionFormatTargeting: Texture-compression-format-level
	// targeting
	TextureCompressionFormatTargeting *TextureCompressionFormatTargeting `json:"textureCompressionFormatTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AbiTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbiTargeting") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApkTargeting: Represents a set of apk-level targetings.

func (ApkTargeting) MarshalJSON ¶
added in v0.130.0
func (s ApkTargeting) MarshalJSON() ([]byte, error)
type ApksAddExternallyHostedRequest ¶
type ApksAddExternallyHostedRequest struct {
	// ExternallyHostedApk: The definition of the externally-hosted APK and where
	// it is located.
	ExternallyHostedApk *ExternallyHostedApk `json:"externallyHostedApk,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternallyHostedApk") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternallyHostedApk") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApksAddExternallyHostedRequest: Request to create a new externally hosted APK.

func (ApksAddExternallyHostedRequest) MarshalJSON ¶
func (s ApksAddExternallyHostedRequest) MarshalJSON() ([]byte, error)
type ApksAddExternallyHostedResponse ¶
type ApksAddExternallyHostedResponse struct {
	// ExternallyHostedApk: The definition of the externally-hosted APK and where
	// it is located.
	ExternallyHostedApk *ExternallyHostedApk `json:"externallyHostedApk,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExternallyHostedApk") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternallyHostedApk") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApksAddExternallyHostedResponse: Response for creating a new externally hosted APK.

func (ApksAddExternallyHostedResponse) MarshalJSON ¶
func (s ApksAddExternallyHostedResponse) MarshalJSON() ([]byte, error)
type ApksListResponse ¶
type ApksListResponse struct {
	// Apks: All APKs.
	Apks []*Apk `json:"apks,omitempty"`
	// Kind: The kind of this response ("androidpublisher#apksListResponse").
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Apks") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Apks") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApksListResponse: Response listing all APKs.

func (ApksListResponse) MarshalJSON ¶
func (s ApksListResponse) MarshalJSON() ([]byte, error)
type AppDetails ¶
type AppDetails struct {
	// ContactEmail: The user-visible support email for this app.
	ContactEmail string `json:"contactEmail,omitempty"`
	// ContactPhone: The user-visible support telephone number for this app.
	ContactPhone string `json:"contactPhone,omitempty"`
	// ContactWebsite: The user-visible website for this app.
	ContactWebsite string `json:"contactWebsite,omitempty"`
	// DefaultLanguage: Default language code, in BCP 47 format (eg "en-US").
	DefaultLanguage string `json:"defaultLanguage,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ContactEmail") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ContactEmail") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppDetails: The app details. The resource for DetailsService.

func (AppDetails) MarshalJSON ¶
func (s AppDetails) MarshalJSON() ([]byte, error)
type AppEdit ¶
type AppEdit struct {
	// ExpiryTimeSeconds: Output only. The time (as seconds since Epoch) at which
	// the edit will expire and will be no longer valid for use.
	ExpiryTimeSeconds string `json:"expiryTimeSeconds,omitempty"`
	// Id: Output only. Identifier of the edit. Can be used in subsequent API
	// calls.
	Id string `json:"id,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExpiryTimeSeconds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpiryTimeSeconds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppEdit: An app edit. The resource for EditsService.

func (AppEdit) MarshalJSON ¶
func (s AppEdit) MarshalJSON() ([]byte, error)
type AppRecoveryAction ¶
added in v0.156.0
type AppRecoveryAction struct {
	// AppRecoveryId: ID corresponding to the app recovery action.
	AppRecoveryId int64 `json:"appRecoveryId,omitempty,string"`
	// CancelTime: Timestamp of when the app recovery action is canceled by the
	// developer. Only set if the recovery action has been canceled.
	CancelTime string `json:"cancelTime,omitempty"`
	// CreateTime: Timestamp of when the app recovery action is created by the
	// developer. It is always set after creation of the recovery action.
	CreateTime string `json:"createTime,omitempty"`
	// DeployTime: Timestamp of when the app recovery action is deployed to the
	// users. Only set if the recovery action has been deployed.
	DeployTime string `json:"deployTime,omitempty"`
	// LastUpdateTime: Timestamp of when the developer last updated recovery
	// action. In case the action is cancelled, it corresponds to cancellation
	// time. It is always set after creation of the recovery action.
	LastUpdateTime string `json:"lastUpdateTime,omitempty"`
	// RemoteInAppUpdateData: Data about the remote in-app update action such as
	// such as recovered user base, recoverable user base etc. Set only if the
	// recovery action type is Remote In-App Update.
	RemoteInAppUpdateData *RemoteInAppUpdateData `json:"remoteInAppUpdateData,omitempty"`
	// Status: The status of the recovery action.
	//
	// Possible values:
	//   "RECOVERY_STATUS_UNSPECIFIED" - RecoveryStatus is unspecified.
	//   "RECOVERY_STATUS_ACTIVE" - The app recovery action has not been canceled
	// since it has been created.
	//   "RECOVERY_STATUS_CANCELED" - The recovery action has been canceled. The
	// action cannot be resumed.
	//   "RECOVERY_STATUS_DRAFT" - The recovery action is in the draft state and
	// has not yet been deployed to users.
	//   "RECOVERY_STATUS_GENERATION_IN_PROGRESS" - The recovery action is
	// generating recovery apks.
	//   "RECOVERY_STATUS_GENERATION_FAILED" - The app recovery action generation
	// has failed.
	Status string `json:"status,omitempty"`
	// Targeting: Specifies targeting criteria for the recovery action such as
	// regions, android sdk versions, app versions etc.
	Targeting *Targeting `json:"targeting,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppRecoveryId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppRecoveryId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppRecoveryAction: Information about an app recovery action.

func (AppRecoveryAction) MarshalJSON ¶
added in v0.156.0
func (s AppRecoveryAction) MarshalJSON() ([]byte, error)
type AppVersionList ¶
added in v0.156.0
type AppVersionList struct {
	// VersionCodes: List of app version codes.
	VersionCodes googleapi.Int64s `json:"versionCodes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "VersionCodes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "VersionCodes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppVersionList: Data format for a list of app versions.

func (AppVersionList) MarshalJSON ¶
added in v0.156.0
func (s AppVersionList) MarshalJSON() ([]byte, error)
type AppVersionRange ¶
added in v0.156.0
type AppVersionRange struct {
	// VersionCodeEnd: Highest app version in the range, inclusive.
	VersionCodeEnd int64 `json:"versionCodeEnd,omitempty,string"`
	// VersionCodeStart: Lowest app version in the range, inclusive.
	VersionCodeStart int64 `json:"versionCodeStart,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "VersionCodeEnd") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "VersionCodeEnd") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppVersionRange: Data format for a continuous range of app versions.

func (AppVersionRange) MarshalJSON ¶
added in v0.156.0
func (s AppVersionRange) MarshalJSON() ([]byte, error)
type ApplicationsDataSafetyCall ¶
added in v0.160.0
type ApplicationsDataSafetyCall struct {
	// contains filtered or unexported fields
}
func (*ApplicationsDataSafetyCall) Context ¶
added in v0.160.0
func (c *ApplicationsDataSafetyCall) Context(ctx context.Context) *ApplicationsDataSafetyCall

Context sets the context to be used in this call's Do method.

func (*ApplicationsDataSafetyCall) Do ¶
added in v0.160.0
func (c *ApplicationsDataSafetyCall) Do(opts ...googleapi.CallOption) (*SafetyLabelsUpdateResponse, error)

Do executes the "androidpublisher.applications.dataSafety" call. Any non-2xx status code is an error. Response headers are in either *SafetyLabelsUpdateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApplicationsDataSafetyCall) Fields ¶
added in v0.160.0
func (c *ApplicationsDataSafetyCall) Fields(s ...googleapi.Field) *ApplicationsDataSafetyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApplicationsDataSafetyCall) Header ¶
added in v0.160.0
func (c *ApplicationsDataSafetyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApplicationsDeviceTierConfigsCreateCall ¶
added in v0.74.0
type ApplicationsDeviceTierConfigsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ApplicationsDeviceTierConfigsCreateCall) AllowUnknownDevices ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsCreateCall) AllowUnknownDevices(allowUnknownDevices bool) *ApplicationsDeviceTierConfigsCreateCall

AllowUnknownDevices sets the optional parameter "allowUnknownDevices": Whether the service should accept device IDs that are unknown to Play's device catalog.

func (*ApplicationsDeviceTierConfigsCreateCall) Context ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsCreateCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsCreateCall

Context sets the context to be used in this call's Do method.

func (*ApplicationsDeviceTierConfigsCreateCall) Do ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsCreateCall) Do(opts ...googleapi.CallOption) (*DeviceTierConfig, error)

Do executes the "androidpublisher.applications.deviceTierConfigs.create" call. Any non-2xx status code is an error. Response headers are in either *DeviceTierConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApplicationsDeviceTierConfigsCreateCall) Fields ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsCreateCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApplicationsDeviceTierConfigsCreateCall) Header ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApplicationsDeviceTierConfigsGetCall ¶
added in v0.74.0
type ApplicationsDeviceTierConfigsGetCall struct {
	// contains filtered or unexported fields
}
func (*ApplicationsDeviceTierConfigsGetCall) Context ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsGetCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsGetCall

Context sets the context to be used in this call's Do method.

func (*ApplicationsDeviceTierConfigsGetCall) Do ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsGetCall) Do(opts ...googleapi.CallOption) (*DeviceTierConfig, error)

Do executes the "androidpublisher.applications.deviceTierConfigs.get" call. Any non-2xx status code is an error. Response headers are in either *DeviceTierConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApplicationsDeviceTierConfigsGetCall) Fields ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsGetCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApplicationsDeviceTierConfigsGetCall) Header ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ApplicationsDeviceTierConfigsGetCall) IfNoneMatch ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsGetCall) IfNoneMatch(entityTag string) *ApplicationsDeviceTierConfigsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ApplicationsDeviceTierConfigsListCall ¶
added in v0.74.0
type ApplicationsDeviceTierConfigsListCall struct {
	// contains filtered or unexported fields
}
func (*ApplicationsDeviceTierConfigsListCall) Context ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) Context(ctx context.Context) *ApplicationsDeviceTierConfigsListCall

Context sets the context to be used in this call's Do method.

func (*ApplicationsDeviceTierConfigsListCall) Do ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) Do(opts ...googleapi.CallOption) (*ListDeviceTierConfigsResponse, error)

Do executes the "androidpublisher.applications.deviceTierConfigs.list" call. Any non-2xx status code is an error. Response headers are in either *ListDeviceTierConfigsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApplicationsDeviceTierConfigsListCall) Fields ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) Fields(s ...googleapi.Field) *ApplicationsDeviceTierConfigsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApplicationsDeviceTierConfigsListCall) Header ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ApplicationsDeviceTierConfigsListCall) IfNoneMatch ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) IfNoneMatch(entityTag string) *ApplicationsDeviceTierConfigsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ApplicationsDeviceTierConfigsListCall) PageSize ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) PageSize(pageSize int64) *ApplicationsDeviceTierConfigsListCall

PageSize sets the optional parameter "pageSize": The maximum number of device tier configs to return. The service may return fewer than this value. If unspecified, at most 10 device tier configs will be returned. The maximum value for this field is 100; values above 100 will be coerced to 100. Device tier configs will be ordered by descending creation time.

func (*ApplicationsDeviceTierConfigsListCall) PageToken ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) PageToken(pageToken string) *ApplicationsDeviceTierConfigsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDeviceTierConfigs` call. Provide this to retrieve the subsequent page.

func (*ApplicationsDeviceTierConfigsListCall) Pages ¶
added in v0.74.0
func (c *ApplicationsDeviceTierConfigsListCall) Pages(ctx context.Context, f func(*ListDeviceTierConfigsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ApplicationsDeviceTierConfigsService ¶
added in v0.74.0
type ApplicationsDeviceTierConfigsService struct {
	// contains filtered or unexported fields
}
func NewApplicationsDeviceTierConfigsService ¶
added in v0.74.0
func NewApplicationsDeviceTierConfigsService(s *Service) *ApplicationsDeviceTierConfigsService
func (*ApplicationsDeviceTierConfigsService) Create ¶
added in v0.74.0
func (r *ApplicationsDeviceTierConfigsService) Create(packageName string, devicetierconfig *DeviceTierConfig) *ApplicationsDeviceTierConfigsCreateCall

Create: Creates a new device tier config for an app.

- packageName: Package name of the app.

func (*ApplicationsDeviceTierConfigsService) Get ¶
added in v0.74.0
func (r *ApplicationsDeviceTierConfigsService) Get(packageName string, deviceTierConfigId int64) *ApplicationsDeviceTierConfigsGetCall

Get: Returns a particular device tier config.

- deviceTierConfigId: Id of an existing device tier config. - packageName: Package name of the app.

func (*ApplicationsDeviceTierConfigsService) List ¶
added in v0.74.0
func (r *ApplicationsDeviceTierConfigsService) List(packageName string) *ApplicationsDeviceTierConfigsListCall

List: Returns created device tier configs, ordered by descending creation time.

- packageName: Package name of the app.

type ApplicationsService ¶
added in v0.74.0
type ApplicationsService struct {
	DeviceTierConfigs *ApplicationsDeviceTierConfigsService
	// contains filtered or unexported fields
}
func NewApplicationsService ¶
added in v0.74.0
func NewApplicationsService(s *Service) *ApplicationsService
func (*ApplicationsService) DataSafety ¶
added in v0.160.0
func (r *ApplicationsService) DataSafety(packageName string, safetylabelsupdaterequest *SafetyLabelsUpdateRequest) *ApplicationsDataSafetyCall

DataSafety: Writes the Safety Labels declaration of an app.

- packageName: Package name of the app.

type ApprecoveryAddTargetingCall ¶
added in v0.156.0
type ApprecoveryAddTargetingCall struct {
	// contains filtered or unexported fields
}
func (*ApprecoveryAddTargetingCall) Context ¶
added in v0.156.0
func (c *ApprecoveryAddTargetingCall) Context(ctx context.Context) *ApprecoveryAddTargetingCall

Context sets the context to be used in this call's Do method.

func (*ApprecoveryAddTargetingCall) Do ¶
added in v0.156.0
func (c *ApprecoveryAddTargetingCall) Do(opts ...googleapi.CallOption) (*AddTargetingResponse, error)

Do executes the "androidpublisher.apprecovery.addTargeting" call. Any non-2xx status code is an error. Response headers are in either *AddTargetingResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApprecoveryAddTargetingCall) Fields ¶
added in v0.156.0
func (c *ApprecoveryAddTargetingCall) Fields(s ...googleapi.Field) *ApprecoveryAddTargetingCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApprecoveryAddTargetingCall) Header ¶
added in v0.156.0
func (c *ApprecoveryAddTargetingCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApprecoveryCancelCall ¶
added in v0.156.0
type ApprecoveryCancelCall struct {
	// contains filtered or unexported fields
}
func (*ApprecoveryCancelCall) Context ¶
added in v0.156.0
func (c *ApprecoveryCancelCall) Context(ctx context.Context) *ApprecoveryCancelCall

Context sets the context to be used in this call's Do method.

func (*ApprecoveryCancelCall) Do ¶
added in v0.156.0
func (c *ApprecoveryCancelCall) Do(opts ...googleapi.CallOption) (*CancelAppRecoveryResponse, error)

Do executes the "androidpublisher.apprecovery.cancel" call. Any non-2xx status code is an error. Response headers are in either *CancelAppRecoveryResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApprecoveryCancelCall) Fields ¶
added in v0.156.0
func (c *ApprecoveryCancelCall) Fields(s ...googleapi.Field) *ApprecoveryCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApprecoveryCancelCall) Header ¶
added in v0.156.0
func (c *ApprecoveryCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApprecoveryCreateCall ¶
added in v0.156.0
type ApprecoveryCreateCall struct {
	// contains filtered or unexported fields
}
func (*ApprecoveryCreateCall) Context ¶
added in v0.156.0
func (c *ApprecoveryCreateCall) Context(ctx context.Context) *ApprecoveryCreateCall

Context sets the context to be used in this call's Do method.

func (*ApprecoveryCreateCall) Do ¶
added in v0.156.0
func (c *ApprecoveryCreateCall) Do(opts ...googleapi.CallOption) (*AppRecoveryAction, error)

Do executes the "androidpublisher.apprecovery.create" call. Any non-2xx status code is an error. Response headers are in either *AppRecoveryAction.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApprecoveryCreateCall) Fields ¶
added in v0.156.0
func (c *ApprecoveryCreateCall) Fields(s ...googleapi.Field) *ApprecoveryCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApprecoveryCreateCall) Header ¶
added in v0.156.0
func (c *ApprecoveryCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApprecoveryDeployCall ¶
added in v0.156.0
type ApprecoveryDeployCall struct {
	// contains filtered or unexported fields
}
func (*ApprecoveryDeployCall) Context ¶
added in v0.156.0
func (c *ApprecoveryDeployCall) Context(ctx context.Context) *ApprecoveryDeployCall

Context sets the context to be used in this call's Do method.

func (*ApprecoveryDeployCall) Do ¶
added in v0.156.0
func (c *ApprecoveryDeployCall) Do(opts ...googleapi.CallOption) (*DeployAppRecoveryResponse, error)

Do executes the "androidpublisher.apprecovery.deploy" call. Any non-2xx status code is an error. Response headers are in either *DeployAppRecoveryResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApprecoveryDeployCall) Fields ¶
added in v0.156.0
func (c *ApprecoveryDeployCall) Fields(s ...googleapi.Field) *ApprecoveryDeployCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApprecoveryDeployCall) Header ¶
added in v0.156.0
func (c *ApprecoveryDeployCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ApprecoveryListCall ¶
added in v0.189.0
type ApprecoveryListCall struct {
	// contains filtered or unexported fields
}
func (*ApprecoveryListCall) Context ¶
added in v0.189.0
func (c *ApprecoveryListCall) Context(ctx context.Context) *ApprecoveryListCall

Context sets the context to be used in this call's Do method.

func (*ApprecoveryListCall) Do ¶
added in v0.189.0
func (c *ApprecoveryListCall) Do(opts ...googleapi.CallOption) (*ListAppRecoveriesResponse, error)

Do executes the "androidpublisher.apprecovery.list" call. Any non-2xx status code is an error. Response headers are in either *ListAppRecoveriesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ApprecoveryListCall) Fields ¶
added in v0.189.0
func (c *ApprecoveryListCall) Fields(s ...googleapi.Field) *ApprecoveryListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ApprecoveryListCall) Header ¶
added in v0.189.0
func (c *ApprecoveryListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ApprecoveryListCall) IfNoneMatch ¶
added in v0.189.0
func (c *ApprecoveryListCall) IfNoneMatch(entityTag string) *ApprecoveryListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ApprecoveryListCall) VersionCode ¶
added in v0.189.0
func (c *ApprecoveryListCall) VersionCode(versionCode int64) *ApprecoveryListCall

VersionCode sets the optional parameter "versionCode": Required. Version code targeted by the list of recovery actions.

type ApprecoveryService ¶
added in v0.156.0
type ApprecoveryService struct {
	// contains filtered or unexported fields
}
func NewApprecoveryService ¶
added in v0.156.0
func NewApprecoveryService(s *Service) *ApprecoveryService
func (*ApprecoveryService) AddTargeting ¶
added in v0.156.0
func (r *ApprecoveryService) AddTargeting(packageName string, appRecoveryId int64, addtargetingrequest *AddTargetingRequest) *ApprecoveryAddTargetingCall

AddTargeting: Incrementally update targeting for a recovery action. Note that only the criteria selected during the creation of recovery action can be expanded.

appRecoveryId: ID corresponding to the app recovery action.
packageName: Package name of the app for which recovery action is to be updated.
func (*ApprecoveryService) Cancel ¶
added in v0.156.0
func (r *ApprecoveryService) Cancel(packageName string, appRecoveryId int64, cancelapprecoveryrequest *CancelAppRecoveryRequest) *ApprecoveryCancelCall

Cancel: Cancel an already executing app recovery action. Note that this action changes status of the recovery action to CANCELED.

appRecoveryId: ID corresponding to the app recovery action.
packageName: Package name of the app for which recovery action cancellation is requested.
func (*ApprecoveryService) Create ¶
added in v0.156.0
func (r *ApprecoveryService) Create(packageName string, createdraftapprecoveryrequest *CreateDraftAppRecoveryRequest) *ApprecoveryCreateCall

Create: Create an app recovery action with recovery status as DRAFT. Note that this action does not execute the recovery action.

packageName: Package name of the app on which recovery action is performed.
func (*ApprecoveryService) Deploy ¶
added in v0.156.0
func (r *ApprecoveryService) Deploy(packageName string, appRecoveryId int64, deployapprecoveryrequest *DeployAppRecoveryRequest) *ApprecoveryDeployCall

Deploy: Deploy an already created app recovery action with recovery status DRAFT. Note that this action activates the recovery action for all targeted users and changes its status to ACTIVE.

appRecoveryId: ID corresponding to the app recovery action to deploy.
packageName: Package name of the app for which recovery action is deployed.
func (*ApprecoveryService) List ¶
added in v0.189.0
func (r *ApprecoveryService) List(packageName string) *ApprecoveryListCall

List: List all app recovery action resources associated with a particular package name and app version.

packageName: Package name of the app for which list of recovery actions is requested.
type ArchiveSubscriptionRequest ¶
added in v0.80.0
type ArchiveSubscriptionRequest struct {
}

ArchiveSubscriptionRequest: Deprecated: subscription archiving is not supported.

type AssetModuleMetadata ¶
added in v0.130.0
type AssetModuleMetadata struct {
	// DeliveryType: Indicates the delivery type for persistent install.
	//
	// Possible values:
	//   "UNKNOWN_DELIVERY_TYPE" - Unspecified delivery type.
	//   "INSTALL_TIME" - This module will always be downloaded as part of the
	// initial install of the app.
	//   "ON_DEMAND" - This module is requested on-demand, which means it will not
	// be part of the initial install, and will only be sent when requested by the
	// client.
	//   "FAST_FOLLOW" - This module will be downloaded immediately after initial
	// install finishes. The app can be opened before these modules are downloaded.
	DeliveryType string `json:"deliveryType,omitempty"`
	// Name: Module name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeliveryType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeliveryType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AssetModuleMetadata: Metadata of an asset module.

func (AssetModuleMetadata) MarshalJSON ¶
added in v0.130.0
func (s AssetModuleMetadata) MarshalJSON() ([]byte, error)
type AssetSliceSet ¶
added in v0.130.0
type AssetSliceSet struct {
	// ApkDescription: Asset slices.
	ApkDescription []*ApkDescription `json:"apkDescription,omitempty"`
	// AssetModuleMetadata: Module level metadata.
	AssetModuleMetadata *AssetModuleMetadata `json:"assetModuleMetadata,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApkDescription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApkDescription") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AssetSliceSet: Set of asset slices belonging to a single asset module.

func (AssetSliceSet) MarshalJSON ¶
added in v0.130.0
func (s AssetSliceSet) MarshalJSON() ([]byte, error)
type AutoRenewingBasePlanType ¶
added in v0.80.0
type AutoRenewingBasePlanType struct {
	// AccountHoldDuration: Optional. Custom account hold period of the
	// subscription, specified in ISO 8601 format. Acceptable values must be in
	// days and between P0D and P60D. An empty field represents a recommended
	// account hold, calculated as 60 days minus grace period. The sum of
	// gracePeriodDuration and accountHoldDuration must be between P30D and P60D
	// days, inclusive.
	AccountHoldDuration string `json:"accountHoldDuration,omitempty"`
	// BillingPeriodDuration: Required. Immutable. Subscription period, specified
	// in ISO 8601 format. For a list of acceptable billing periods, refer to the
	// help center. The duration is immutable after the base plan is created.
	BillingPeriodDuration string `json:"billingPeriodDuration,omitempty"`
	// GracePeriodDuration: Grace period of the subscription, specified in ISO 8601
	// format. Acceptable values must be in days and between P0D and the lesser of
	// 30D and base plan billing period. If not specified, a default value will be
	// used based on the billing period. The sum of gracePeriodDuration and
	// accountHoldDuration must be between P30D and P60D days, inclusive.
	GracePeriodDuration string `json:"gracePeriodDuration,omitempty"`
	// LegacyCompatible: Whether the renewing base plan is backward compatible. The
	// backward compatible base plan is returned by the Google Play Billing Library
	// deprecated method querySkuDetailsAsync(). Only one renewing base plan can be
	// marked as legacy compatible for a given subscription.
	LegacyCompatible bool `json:"legacyCompatible,omitempty"`
	// LegacyCompatibleSubscriptionOfferId: Subscription offer id which is legacy
	// compatible. The backward compatible subscription offer is returned by the
	// Google Play Billing Library deprecated method querySkuDetailsAsync(). Only
	// one subscription offer can be marked as legacy compatible for a given
	// renewing base plan. To have no Subscription offer as legacy compatible set
	// this field as empty string.
	LegacyCompatibleSubscriptionOfferId string `json:"legacyCompatibleSubscriptionOfferId,omitempty"`
	// ProrationMode: The proration mode for the base plan determines what happens
	// when a user switches to this plan from another base plan. If unspecified,
	// defaults to CHARGE_ON_NEXT_BILLING_DATE.
	//
	// Possible values:
	//   "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED" - Unspecified mode.
	//   "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE" - Users will be
	// charged for their new base plan at the end of their current billing period.
	//   "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY" - Users will
	// be charged for their new base plan immediately and in full. Any remaining
	// period of their existing subscription will be used to extend the duration of
	// the new billing plan.
	ProrationMode string `json:"prorationMode,omitempty"`
	// ResubscribeState: Whether users should be able to resubscribe to this base
	// plan in Google Play surfaces. Defaults to RESUBSCRIBE_STATE_ACTIVE if not
	// specified.
	//
	// Possible values:
	//   "RESUBSCRIBE_STATE_UNSPECIFIED" - Unspecified state.
	//   "RESUBSCRIBE_STATE_ACTIVE" - Resubscribe is active.
	//   "RESUBSCRIBE_STATE_INACTIVE" - Resubscribe is inactive.
	ResubscribeState string `json:"resubscribeState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountHoldDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountHoldDuration") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AutoRenewingBasePlanType: Represents a base plan that automatically renews at the end of its subscription period.

func (AutoRenewingBasePlanType) MarshalJSON ¶
added in v0.80.0
func (s AutoRenewingBasePlanType) MarshalJSON() ([]byte, error)
type AutoRenewingPlan ¶
added in v0.80.0
type AutoRenewingPlan struct {
	// AutoRenewEnabled: If the subscription is currently set to auto-renew, e.g.
	// the user has not canceled the subscription
	AutoRenewEnabled bool `json:"autoRenewEnabled,omitempty"`
	// InstallmentDetails: The installment plan commitment and state related info
	// for the auto renewing plan.
	InstallmentDetails *InstallmentPlan `json:"installmentDetails,omitempty"`
	// PriceChangeDetails: The information of the last price change for the item
	// since subscription signup.
	PriceChangeDetails *SubscriptionItemPriceChangeDetails `json:"priceChangeDetails,omitempty"`
	// PriceStepUpConsentDetails: The information of the latest price step-up
	// consent.
	PriceStepUpConsentDetails *PriceStepUpConsentDetails `json:"priceStepUpConsentDetails,omitempty"`
	// RecurringPrice: The current recurring price of the auto renewing plan. Note
	// that the price does not take into account discounts and does not include
	// taxes for tax-exclusive pricing, please call orders.get API instead if
	// transaction details are needed.
	RecurringPrice *Money `json:"recurringPrice,omitempty"`
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

AutoRenewingPlan: Information related to an auto renewing plan.

func (AutoRenewingPlan) MarshalJSON ¶
added in v0.80.0
func (s AutoRenewingPlan) MarshalJSON() ([]byte, error)
type BaseDetails ¶
added in v0.257.0
type BaseDetails struct {
}

BaseDetails: Details of a base price pricing phase.

type BasePlan ¶
added in v0.80.0
type BasePlan struct {
	// AutoRenewingBasePlanType: Set when the base plan automatically renews at a
	// regular interval.
	AutoRenewingBasePlanType *AutoRenewingBasePlanType `json:"autoRenewingBasePlanType,omitempty"`
	// BasePlanId: Required. Immutable. The unique identifier of this base plan.
	// Must be unique within the subscription, and conform with RFC-1034. That is,
	// this ID can only contain lower-case letters (a-z), numbers (0-9), and
	// hyphens (-), and be at most 63 characters.
	BasePlanId string `json:"basePlanId,omitempty"`
	// InstallmentsBasePlanType: Set for installments base plans where a user is
	// committed to a specified number of payments.
	InstallmentsBasePlanType *InstallmentsBasePlanType `json:"installmentsBasePlanType,omitempty"`
	// OfferTags: List of up to 20 custom tags specified for this base plan, and
	// returned to the app through the billing library. Subscription offers for
	// this base plan will also receive these offer tags in the billing library.
	OfferTags []*OfferTag `json:"offerTags,omitempty"`
	// OtherRegionsConfig: Pricing information for any new locations Play may
	// launch in the future. If omitted, the BasePlan will not be automatically
	// available any new locations Play may launch in the future.
	OtherRegionsConfig *OtherRegionsBasePlanConfig `json:"otherRegionsConfig,omitempty"`
	// PrepaidBasePlanType: Set when the base plan does not automatically renew at
	// the end of the billing period.
	PrepaidBasePlanType *PrepaidBasePlanType `json:"prepaidBasePlanType,omitempty"`
	// RegionalConfigs: Region-specific information for this base plan.
	RegionalConfigs []*RegionalBasePlanConfig `json:"regionalConfigs,omitempty"`
	// State: Output only. The state of the base plan, i.e. whether it's active.
	// Draft and inactive base plans can be activated or deleted. Active base plans
	// can be made inactive. Inactive base plans can be canceled. This field cannot
	// be changed by updating the resource. Use the dedicated endpoints instead.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified state.
	//   "DRAFT" - The base plan is currently in a draft state, and hasn't been
	// activated. It can be safely deleted at this point.
	//   "ACTIVE" - The base plan is active and available for new subscribers.
	//   "INACTIVE" - The base plan is inactive and only available for existing
	// subscribers.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoRenewingBasePlanType")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoRenewingBasePlanType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BasePlan: A single base plan for a subscription.

func (BasePlan) MarshalJSON ¶
added in v0.80.0
func (s BasePlan) MarshalJSON() ([]byte, error)
type BasePriceOfferPhase ¶
added in v0.265.0
type BasePriceOfferPhase struct {
}

BasePriceOfferPhase: Details about base price offer phase.

type BatchDeleteOneTimeProductOffersRequest ¶
added in v0.244.0
type BatchDeleteOneTimeProductOffersRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must correspond to different offers.
	Requests []*DeleteOneTimeProductOfferRequest `json:"requests,omitempty"`
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

BatchDeleteOneTimeProductOffersRequest: Request message for BatchDeleteOneTimeProductOffers.

func (BatchDeleteOneTimeProductOffersRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchDeleteOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchDeleteOneTimeProductsRequest ¶
added in v0.244.0
type BatchDeleteOneTimeProductsRequest struct {
	// Requests: Required. A list of delete requests of up to 100 elements. All
	// requests must delete different one-time products.
	Requests []*DeleteOneTimeProductRequest `json:"requests,omitempty"`
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

BatchDeleteOneTimeProductsRequest: Request message for BatchDeleteOneTimeProduct.

func (BatchDeleteOneTimeProductsRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchDeleteOneTimeProductsRequest) MarshalJSON() ([]byte, error)
type BatchDeletePurchaseOptionsRequest ¶
added in v0.244.0
type BatchDeletePurchaseOptionsRequest struct {
	// Requests: Required. A list of delete requests of up to 100 elements. All
	// requests must delete purchase options from different one-time products.
	Requests []*DeletePurchaseOptionRequest `json:"requests,omitempty"`
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

BatchDeletePurchaseOptionsRequest: Request message for BatchDeletePurchaseOption.

func (BatchDeletePurchaseOptionsRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchDeletePurchaseOptionsRequest) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductOffersRequest ¶
added in v0.244.0
type BatchGetOneTimeProductOffersRequest struct {
	// Requests: Required. A list of get requests of up to 100 elements. All
	// requests must retrieve different offers.
	Requests []*GetOneTimeProductOfferRequest `json:"requests,omitempty"`
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

BatchGetOneTimeProductOffersRequest: Request message for the BatchGetOneTimeProductOffers endpoint.

func (BatchGetOneTimeProductOffersRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchGetOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductOffersResponse ¶
added in v0.244.0
type BatchGetOneTimeProductOffersResponse struct {
	// OneTimeProductOffers: The list of updated one-time product offers, in the
	// same order as the request.
	OneTimeProductOffers []*OneTimeProductOffer `json:"oneTimeProductOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProductOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProductOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchGetOneTimeProductOffersResponse: Response message for the BatchGetOneTimeProductOffers endpoint.

func (BatchGetOneTimeProductOffersResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchGetOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type BatchGetOneTimeProductsResponse ¶
added in v0.244.0
type BatchGetOneTimeProductsResponse struct {
	// OneTimeProducts: The list of requested one-time products, in the same order
	// as the request.
	OneTimeProducts []*OneTimeProduct `json:"oneTimeProducts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProducts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProducts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchGetOneTimeProductsResponse: Response message for the BatchGetOneTimeProducts endpoint.

func (BatchGetOneTimeProductsResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchGetOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type BatchGetOrdersResponse ¶
added in v0.234.0
type BatchGetOrdersResponse struct {
	// Orders: Details for the requested order IDs.
	Orders []*Order `json:"orders,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Orders") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Orders") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchGetOrdersResponse: Response for the orders.batchGet API.

func (BatchGetOrdersResponse) MarshalJSON ¶
added in v0.234.0
func (s BatchGetOrdersResponse) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionOffersRequest ¶
added in v0.154.0
type BatchGetSubscriptionOffersRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must update different subscriptions.
	Requests []*GetSubscriptionOfferRequest `json:"requests,omitempty"`
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

BatchGetSubscriptionOffersRequest: Request message for BatchGetSubscriptionOffers endpoint.

func (BatchGetSubscriptionOffersRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchGetSubscriptionOffersRequest) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionOffersResponse ¶
added in v0.154.0
type BatchGetSubscriptionOffersResponse struct {
	SubscriptionOffers []*SubscriptionOffer `json:"subscriptionOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "SubscriptionOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SubscriptionOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchGetSubscriptionOffersResponse: Response message for BatchGetSubscriptionOffers endpoint.

func (BatchGetSubscriptionOffersResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchGetSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type BatchGetSubscriptionsResponse ¶
added in v0.154.0
type BatchGetSubscriptionsResponse struct {
	// Subscriptions: The list of requested subscriptions, in the same order as the
	// request.
	Subscriptions []*Subscription `json:"subscriptions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Subscriptions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Subscriptions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchGetSubscriptionsResponse: Response message for BatchGetSubscriptions endpoint.

func (BatchGetSubscriptionsResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchGetSubscriptionsResponse) MarshalJSON() ([]byte, error)
type BatchMigrateBasePlanPricesRequest ¶
added in v0.154.0
type BatchMigrateBasePlanPricesRequest struct {
	// Requests: Required. Up to 100 price migration requests. All requests must
	// update different base plans.
	Requests []*MigrateBasePlanPricesRequest `json:"requests,omitempty"`
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

BatchMigrateBasePlanPricesRequest: Request message for BatchMigrateBasePlanPrices.

func (BatchMigrateBasePlanPricesRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchMigrateBasePlanPricesRequest) MarshalJSON() ([]byte, error)
type BatchMigrateBasePlanPricesResponse ¶
added in v0.154.0
type BatchMigrateBasePlanPricesResponse struct {
	// Responses: Contains one response per requested price migration, in the same
	// order as the request.
	Responses []*MigrateBasePlanPricesResponse `json:"responses,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Responses") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Responses") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchMigrateBasePlanPricesResponse: Response message for BatchMigrateBasePlanPrices.

func (BatchMigrateBasePlanPricesResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchMigrateBasePlanPricesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateBasePlanStatesRequest ¶
added in v0.154.0
type BatchUpdateBasePlanStatesRequest struct {
	// Requests: Required. The update request list of up to 100 elements. All
	// requests must update different base plans.
	Requests []*UpdateBasePlanStateRequest `json:"requests,omitempty"`
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

BatchUpdateBasePlanStatesRequest: Request message for BatchUpdateBasePlanStates.

func (BatchUpdateBasePlanStatesRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateBasePlanStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateBasePlanStatesResponse ¶
added in v0.154.0
type BatchUpdateBasePlanStatesResponse struct {
	// Subscriptions: The list of updated subscriptions. This list will match the
	// requests one to one, in the same order.
	Subscriptions []*Subscription `json:"subscriptions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Subscriptions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Subscriptions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateBasePlanStatesResponse: Response message for BatchUpdateBasePlanStates.

func (BatchUpdateBasePlanStatesResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateBasePlanStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOfferStatesRequest ¶
added in v0.244.0
type BatchUpdateOneTimeProductOfferStatesRequest struct {
	// Requests: Required. The update request list of up to 100 elements. All
	// requests must update different offers.
	Requests []*UpdateOneTimeProductOfferStateRequest `json:"requests,omitempty"`
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

BatchUpdateOneTimeProductOfferStatesRequest: Request message for BatchUpdateOneTimeProductOfferStates.

func (BatchUpdateOneTimeProductOfferStatesRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductOfferStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOfferStatesResponse ¶
added in v0.244.0
type BatchUpdateOneTimeProductOfferStatesResponse struct {
	// OneTimeProductOffers: The updated one-time product offers list, in the same
	// order as the request.
	OneTimeProductOffers []*OneTimeProductOffer `json:"oneTimeProductOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProductOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProductOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateOneTimeProductOfferStatesResponse: Response message for BatchUpdateOneTimeProductOfferStates.

func (BatchUpdateOneTimeProductOfferStatesResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductOfferStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOffersRequest ¶
added in v0.244.0
type BatchUpdateOneTimeProductOffersRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must update different offers.
	Requests []*UpdateOneTimeProductOfferRequest `json:"requests,omitempty"`
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

BatchUpdateOneTimeProductOffersRequest: Request message for BatchUpdateOneTimeProductOffers.

func (BatchUpdateOneTimeProductOffersRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductOffersRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductOffersResponse ¶
added in v0.244.0
type BatchUpdateOneTimeProductOffersResponse struct {
	// OneTimeProductOffers: The list of updated one-time product offers, in the
	// same order as the request.
	OneTimeProductOffers []*OneTimeProductOffer `json:"oneTimeProductOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProductOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProductOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateOneTimeProductOffersResponse: Response message for BatchUpdateOneTimeProductOffers.

func (BatchUpdateOneTimeProductOffersResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductsRequest ¶
added in v0.244.0
type BatchUpdateOneTimeProductsRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must update different one-time products.
	Requests []*UpdateOneTimeProductRequest `json:"requests,omitempty"`
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

BatchUpdateOneTimeProductsRequest: Request message for BatchUpdateOneTimeProduct.

func (BatchUpdateOneTimeProductsRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateOneTimeProductsResponse ¶
added in v0.244.0
type BatchUpdateOneTimeProductsResponse struct {
	// OneTimeProducts: The list of updated one-time products list, in the same
	// order as the request.
	OneTimeProducts []*OneTimeProduct `json:"oneTimeProducts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProducts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProducts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateOneTimeProductsResponse: Response message for BatchUpdateOneTimeProduct.

func (BatchUpdateOneTimeProductsResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdateOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type BatchUpdatePurchaseOptionStatesRequest ¶
added in v0.244.0
type BatchUpdatePurchaseOptionStatesRequest struct {
	// Requests: Required. The update request list of up to 100 elements. All
	// requests must update different purchase options.
	Requests []*UpdatePurchaseOptionStateRequest `json:"requests,omitempty"`
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

BatchUpdatePurchaseOptionStatesRequest: Request message for BatchUpdatePurchaseOptionStates.

func (BatchUpdatePurchaseOptionStatesRequest) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdatePurchaseOptionStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdatePurchaseOptionStatesResponse ¶
added in v0.244.0
type BatchUpdatePurchaseOptionStatesResponse struct {
	// OneTimeProducts: The list of updated one-time products. This list will match
	// the requests one to one, in the same order.
	OneTimeProducts []*OneTimeProduct `json:"oneTimeProducts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "OneTimeProducts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeProducts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdatePurchaseOptionStatesResponse: Response message for BatchUpdatePurchaseOptionStates.

func (BatchUpdatePurchaseOptionStatesResponse) MarshalJSON ¶
added in v0.244.0
func (s BatchUpdatePurchaseOptionStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOfferStatesRequest ¶
added in v0.154.0
type BatchUpdateSubscriptionOfferStatesRequest struct {
	// Requests: Required. The update request list of up to 100 elements. All
	// requests must update different offers.
	Requests []*UpdateSubscriptionOfferStateRequest `json:"requests,omitempty"`
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

BatchUpdateSubscriptionOfferStatesRequest: Request message for BatchUpdateSubscriptionOfferStates.

func (BatchUpdateSubscriptionOfferStatesRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionOfferStatesRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOfferStatesResponse ¶
added in v0.154.0
type BatchUpdateSubscriptionOfferStatesResponse struct {
	// SubscriptionOffers: The updated subscription offers list.
	SubscriptionOffers []*SubscriptionOffer `json:"subscriptionOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "SubscriptionOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SubscriptionOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateSubscriptionOfferStatesResponse: Response message for BatchUpdateSubscriptionOfferStates.

func (BatchUpdateSubscriptionOfferStatesResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionOfferStatesResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOffersRequest ¶
added in v0.154.0
type BatchUpdateSubscriptionOffersRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must update different subscription offers.
	Requests []*UpdateSubscriptionOfferRequest `json:"requests,omitempty"`
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

BatchUpdateSubscriptionOffersRequest: Request message for BatchUpdateSubscriptionOffers.

func (BatchUpdateSubscriptionOffersRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionOffersRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionOffersResponse ¶
added in v0.154.0
type BatchUpdateSubscriptionOffersResponse struct {
	// SubscriptionOffers: The updated subscription offers list.
	SubscriptionOffers []*SubscriptionOffer `json:"subscriptionOffers,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "SubscriptionOffers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SubscriptionOffers") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateSubscriptionOffersResponse: Response message for BatchUpdateSubscriptionOffers.

func (BatchUpdateSubscriptionOffersResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionsRequest ¶
added in v0.154.0
type BatchUpdateSubscriptionsRequest struct {
	// Requests: Required. A list of update requests of up to 100 elements. All
	// requests must update different subscriptions.
	Requests []*UpdateSubscriptionRequest `json:"requests,omitempty"`
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

BatchUpdateSubscriptionsRequest: Request message for BatchUpdateSubscription.

func (BatchUpdateSubscriptionsRequest) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateSubscriptionsResponse ¶
added in v0.154.0
type BatchUpdateSubscriptionsResponse struct {
	// Subscriptions: The updated subscriptions list.
	Subscriptions []*Subscription `json:"subscriptions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Subscriptions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Subscriptions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateSubscriptionsResponse: Response message for BatchUpdateSubscription.

func (BatchUpdateSubscriptionsResponse) MarshalJSON ¶
added in v0.154.0
func (s BatchUpdateSubscriptionsResponse) MarshalJSON() ([]byte, error)
type Bundle ¶
type Bundle struct {
	// Sha1: A sha1 hash of the upload payload, encoded as a hex string and
	// matching the output of the sha1sum command.
	Sha1 string `json:"sha1,omitempty"`
	// Sha256: A sha256 hash of the upload payload, encoded as a hex string and
	// matching the output of the sha256sum command.
	Sha256 string `json:"sha256,omitempty"`
	// VersionCode: The version code of the Android App Bundle, as specified in the
	// Android App Bundle's base module APK manifest file.
	VersionCode int64 `json:"versionCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Sha1") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Sha1") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Bundle: Information about an app bundle. The resource for BundlesService.

func (Bundle) MarshalJSON ¶
func (s Bundle) MarshalJSON() ([]byte, error)
type BundlesListResponse ¶
type BundlesListResponse struct {
	// Bundles: All app bundles.
	Bundles []*Bundle `json:"bundles,omitempty"`
	// Kind: The kind of this response ("androidpublisher#bundlesListResponse").
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Bundles") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Bundles") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BundlesListResponse: Response listing all app bundles.

func (BundlesListResponse) MarshalJSON ¶
func (s BundlesListResponse) MarshalJSON() ([]byte, error)
type BuyerAddress ¶
added in v0.234.0
type BuyerAddress struct {
	// BuyerCountry: Two letter country code based on ISO-3166-1 Alpha-2 (UN
	// country codes).
	BuyerCountry string `json:"buyerCountry,omitempty"`
	// BuyerPostcode: Postal code of an address. When Google is the Merchant of
	// Record for the order, this information is not included.
	BuyerPostcode string `json:"buyerPostcode,omitempty"`
	// BuyerState: Top-level administrative subdivision of the buyer address
	// country. When Google is the Merchant of Record for the order, this
	// information is not included.
	BuyerState string `json:"buyerState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BuyerCountry") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuyerCountry") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BuyerAddress: Address information for the customer, for use in tax computation.

func (BuyerAddress) MarshalJSON ¶
added in v0.234.0
func (s BuyerAddress) MarshalJSON() ([]byte, error)
type CancelAppRecoveryRequest ¶
added in v0.156.0
type CancelAppRecoveryRequest struct {
}

CancelAppRecoveryRequest: Request message for CancelAppRecovery.

type CancelAppRecoveryResponse ¶
added in v0.156.0
type CancelAppRecoveryResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

CancelAppRecoveryResponse: Response message for CancelAppRecovery.

type CancelOneTimeProductOfferRequest ¶
added in v0.244.0
type CancelOneTimeProductOfferRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The offer ID of the offer to cancel.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to cancel.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the offer to
	// cancel.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The parent purchase option (ID) of the offer to
	// cancel.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CancelOneTimeProductOfferRequest: Request message for CancelOneTimeProductOffer.

func (CancelOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s CancelOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type CancelSubscriptionPurchaseRequest ¶
added in v0.249.0
type CancelSubscriptionPurchaseRequest struct {
	// CancellationContext: Required. Additional details around the subscription
	// revocation.
	CancellationContext *CancellationContext `json:"cancellationContext,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CancellationContext") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CancellationContext") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CancelSubscriptionPurchaseRequest: Request for the purchases.subscriptionsv2.cancel API.

func (CancelSubscriptionPurchaseRequest) MarshalJSON ¶
added in v0.249.0
func (s CancelSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type CancelSubscriptionPurchaseResponse ¶
added in v0.249.0
type CancelSubscriptionPurchaseResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

CancelSubscriptionPurchaseResponse: Response for the purchases.subscriptionsv2.cancel API.

type CancelSurveyResult ¶
added in v0.80.0
type CancelSurveyResult struct {
	// Reason: The reason the user selected in the cancel survey.
	//
	// Possible values:
	//   "CANCEL_SURVEY_REASON_UNSPECIFIED" - Unspecified cancel survey reason.
	//   "CANCEL_SURVEY_REASON_NOT_ENOUGH_USAGE" - Not enough usage of the
	// subscription.
	//   "CANCEL_SURVEY_REASON_TECHNICAL_ISSUES" - Technical issues while using the
	// app.
	//   "CANCEL_SURVEY_REASON_COST_RELATED" - Cost related issues.
	//   "CANCEL_SURVEY_REASON_FOUND_BETTER_APP" - The user found a better app.
	//   "CANCEL_SURVEY_REASON_OTHERS" - Other reasons.
	Reason string `json:"reason,omitempty"`
	// ReasonUserInput: Only set for CANCEL_SURVEY_REASON_OTHERS. This is the
	// user's freeform response to the survey.
	ReasonUserInput string `json:"reasonUserInput,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Reason") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Reason") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CancelSurveyResult: Result of the cancel survey when the subscription was canceled by the user.

func (CancelSurveyResult) MarshalJSON ¶
added in v0.80.0
func (s CancelSurveyResult) MarshalJSON() ([]byte, error)
type CanceledStateContext ¶
added in v0.80.0
type CanceledStateContext struct {
	// DeveloperInitiatedCancellation: Subscription was canceled by the developer.
	DeveloperInitiatedCancellation *DeveloperInitiatedCancellation `json:"developerInitiatedCancellation,omitempty"`
	// ReplacementCancellation: Subscription was replaced by a new subscription.
	ReplacementCancellation *ReplacementCancellation `json:"replacementCancellation,omitempty"`
	// SystemInitiatedCancellation: Subscription was canceled by the system, for
	// example because of a billing problem.
	SystemInitiatedCancellation *SystemInitiatedCancellation `json:"systemInitiatedCancellation,omitempty"`
	// UserInitiatedCancellation: Subscription was canceled by user.
	UserInitiatedCancellation *UserInitiatedCancellation `json:"userInitiatedCancellation,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "DeveloperInitiatedCancellation") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeveloperInitiatedCancellation")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CanceledStateContext: Information specific to a subscription in the SUBSCRIPTION_STATE_CANCELED or SUBSCRIPTION_STATE_EXPIRED state.

func (CanceledStateContext) MarshalJSON ¶
added in v0.80.0
func (s CanceledStateContext) MarshalJSON() ([]byte, error)
type CancellationContext ¶
added in v0.249.0
type CancellationContext struct {
	// CancellationType: Required. The type of cancellation for the purchased
	// subscription.
	//
	// Possible values:
	//   "CANCELLATION_TYPE_UNSPECIFIED" - Cancellation type unspecified.
	//   "USER_REQUESTED_STOP_RENEWALS" - Cancellation requested by the user, and
	// the subscription can be restored. It only stops the subscription's next
	// renewal. For an installment subscription, users still need to finish the
	// commitment period. For more details on renewals and payments, see
	// https://developer.android.com/google/play/billing/subscriptions#installments
	//   "DEVELOPER_REQUESTED_STOP_PAYMENTS" - Cancellation requested by the
	// developer, and the subscription cannot be restored. It stops the
	// subscription's next payment. For an installment subscription, users will not
	// need to pay the next payment and finish the commitment period. For more
	// details on renewals and payments, see
	// https://developer.android.com/google/play/billing/subscriptions#installments
	CancellationType string `json:"cancellationType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CancellationType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CancellationType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CancellationContext: Cancellation context of the purchases.subscriptionsv2.cancel API.

func (CancellationContext) MarshalJSON ¶
added in v0.249.0
func (s CancellationContext) MarshalJSON() ([]byte, error)
type CancellationEvent ¶
added in v0.234.0
type CancellationEvent struct {
	// EventTime: The time when the order was canceled.
	EventTime string `json:"eventTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CancellationEvent: Details of when the order was canceled.

func (CancellationEvent) MarshalJSON ¶
added in v0.234.0
func (s CancellationEvent) MarshalJSON() ([]byte, error)
type Comment ¶
type Comment struct {
	// DeveloperComment: A comment from a developer.
	DeveloperComment *DeveloperComment `json:"developerComment,omitempty"`
	// UserComment: A comment from a user.
	UserComment *UserComment `json:"userComment,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeveloperComment") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeveloperComment") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Comment: An entry of conversation between user and developer.

func (Comment) MarshalJSON ¶
func (s Comment) MarshalJSON() ([]byte, error)
type ConvertRegionPricesRequest ¶
added in v0.59.0
type ConvertRegionPricesRequest struct {
	// Price: The intital price to convert other regions from. Tax exclusive.
	Price *Money `json:"price,omitempty"`
	// ProductTaxCategoryCode: Optional. Product tax category code in context.
	// Product tax category determines the transaction tax rates applied to the
	// product that will be factored into the price calculation. If not set, tax
	// rates for the default product tax category will be used. Refer to the Help
	// Center article
	// (https://support.google.com/googleplay/android-developer/answer/16408159)
	// for more information.
	ProductTaxCategoryCode string `json:"productTaxCategoryCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Price") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Price") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConvertRegionPricesRequest: Request message for ConvertRegionPrices.

func (ConvertRegionPricesRequest) MarshalJSON ¶
added in v0.59.0
func (s ConvertRegionPricesRequest) MarshalJSON() ([]byte, error)
type ConvertRegionPricesResponse ¶
added in v0.59.0
type ConvertRegionPricesResponse struct {
	// ConvertedOtherRegionsPrice: Converted other regions prices in USD and EUR,
	// to use for countries where Play doesn't support a country's local currency.
	ConvertedOtherRegionsPrice *ConvertedOtherRegionsPrice `json:"convertedOtherRegionsPrice,omitempty"`
	// ConvertedRegionPrices: Map from region code to converted region price.
	ConvertedRegionPrices map[string]ConvertedRegionPrice `json:"convertedRegionPrices,omitempty"`
	// RegionVersion: The region version at which the prices were generated.
	RegionVersion *RegionsVersion `json:"regionVersion,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ConvertedOtherRegionsPrice")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConvertedOtherRegionsPrice") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConvertRegionPricesResponse: Response message for ConvertRegionPrices.

func (ConvertRegionPricesResponse) MarshalJSON ¶
added in v0.59.0
func (s ConvertRegionPricesResponse) MarshalJSON() ([]byte, error)
type ConvertedOtherRegionsPrice ¶
added in v0.59.0
type ConvertedOtherRegionsPrice struct {
	// EurPrice: Price in EUR to use for the "Other regions" location exclusive of
	// taxes.
	EurPrice *Money `json:"eurPrice,omitempty"`
	// UsdPrice: Price in USD to use for the "Other regions" location exclusive of
	// taxes.
	UsdPrice *Money `json:"usdPrice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EurPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EurPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConvertedOtherRegionsPrice: Converted other regions prices.

func (ConvertedOtherRegionsPrice) MarshalJSON ¶
added in v0.59.0
func (s ConvertedOtherRegionsPrice) MarshalJSON() ([]byte, error)
type ConvertedRegionPrice ¶
added in v0.59.0
type ConvertedRegionPrice struct {
	// Price: The converted price tax inclusive.
	Price *Money `json:"price,omitempty"`
	// RegionCode: The region code of the region.
	RegionCode string `json:"regionCode,omitempty"`
	// TaxAmount: The tax amount of the converted price.
	TaxAmount *Money `json:"taxAmount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Price") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Price") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ConvertedRegionPrice: A converted region price.

func (ConvertedRegionPrice) MarshalJSON ¶
added in v0.59.0
func (s ConvertedRegionPrice) MarshalJSON() ([]byte, error)
type CountryTargeting ¶
added in v0.3.1
type CountryTargeting struct {
	// Countries: Countries to target, specified as two letter CLDR codes
	// (https://unicode.org/cldr/charts/latest/supplemental/territory_containment_un_m_49.html).
	Countries []string `json:"countries,omitempty"`
	// IncludeRestOfWorld: Include "rest of world" as well as explicitly targeted
	// countries.
	IncludeRestOfWorld bool `json:"includeRestOfWorld,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Countries") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Countries") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CountryTargeting: Country targeting specification.

func (CountryTargeting) MarshalJSON ¶
added in v0.3.1
func (s CountryTargeting) MarshalJSON() ([]byte, error)
type CreateDraftAppRecoveryRequest ¶
added in v0.156.0
type CreateDraftAppRecoveryRequest struct {
	// RemoteInAppUpdate: Action type is remote in-app update. As a consequence of
	// this action, a downloadable recovery module is also created for testing
	// purposes.
	RemoteInAppUpdate *RemoteInAppUpdate `json:"remoteInAppUpdate,omitempty"`
	// Targeting: Specifies targeting criteria for the recovery action such as
	// regions, android sdk versions, app versions etc.
	Targeting *Targeting `json:"targeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RemoteInAppUpdate") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RemoteInAppUpdate") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreateDraftAppRecoveryRequest: Request message for CreateDraftAppRecovery.

func (CreateDraftAppRecoveryRequest) MarshalJSON ¶
added in v0.156.0
func (s CreateDraftAppRecoveryRequest) MarshalJSON() ([]byte, error)
type DeactivateBasePlanRequest ¶
added in v0.80.0
type DeactivateBasePlanRequest struct {
	// BasePlanId: Required. The unique base plan ID of the base plan to
	// deactivate.
	BasePlanId string `json:"basePlanId,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the base plan to
	// deactivate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent subscription (ID) of the base plan to
	// deactivate.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeactivateBasePlanRequest: Request message for DeactivateBasePlan.

func (DeactivateBasePlanRequest) MarshalJSON ¶
added in v0.154.0
func (s DeactivateBasePlanRequest) MarshalJSON() ([]byte, error)
type DeactivateOneTimeProductOfferRequest ¶
added in v0.244.0
type DeactivateOneTimeProductOfferRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The offer ID of the offer to deactivate.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to
	// deactivate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the offer to
	// deactivate.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The parent purchase option (ID) of the offer to
	// deactivate.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeactivateOneTimeProductOfferRequest: Request message for DeactivateOneTimeProductOffer.

func (DeactivateOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s DeactivateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type DeactivatePurchaseOptionRequest ¶
added in v0.244.0
type DeactivatePurchaseOptionRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the purchase option
	// to deactivate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the purchase option
	// to deactivate.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The purchase option ID of the purchase option to
	// deactivate.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeactivatePurchaseOptionRequest: Request message for UpdatePurchaseOptionState.

func (DeactivatePurchaseOptionRequest) MarshalJSON ¶
added in v0.244.0
func (s DeactivatePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type DeactivateSubscriptionOfferRequest ¶
added in v0.80.0
type DeactivateSubscriptionOfferRequest struct {
	// BasePlanId: Required. The parent base plan (ID) of the offer to deactivate.
	BasePlanId string `json:"basePlanId,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The unique offer ID of the offer to deactivate.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to
	// deactivate.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent subscription (ID) of the offer to
	// deactivate.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeactivateSubscriptionOfferRequest: Request message for DeactivateSubscriptionOffer.

func (DeactivateSubscriptionOfferRequest) MarshalJSON ¶
added in v0.154.0
func (s DeactivateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type DeferSubscriptionPurchaseRequest ¶
added in v0.265.0
type DeferSubscriptionPurchaseRequest struct {
	// DeferralContext: Required. Details about the subscription deferral.
	DeferralContext *DeferralContext `json:"deferralContext,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeferralContext") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeferralContext") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeferSubscriptionPurchaseRequest: Request for the v2 purchases.subscriptions.defer API.

func (DeferSubscriptionPurchaseRequest) MarshalJSON ¶
added in v0.265.0
func (s DeferSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type DeferSubscriptionPurchaseResponse ¶
added in v0.265.0
type DeferSubscriptionPurchaseResponse struct {
	// ItemExpiryTimeDetails: The new expiry time for each subscription items.
	ItemExpiryTimeDetails []*ItemExpiryTimeDetails `json:"itemExpiryTimeDetails,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ItemExpiryTimeDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ItemExpiryTimeDetails") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeferSubscriptionPurchaseResponse: Response for the v2 purchases.subscriptions.defer API.

func (DeferSubscriptionPurchaseResponse) MarshalJSON ¶
added in v0.265.0
func (s DeferSubscriptionPurchaseResponse) MarshalJSON() ([]byte, error)
type DeferralContext ¶
added in v0.265.0
type DeferralContext struct {
	// DeferDuration: Required. The duration by which all subscription items should
	// be deferred.
	DeferDuration string `json:"deferDuration,omitempty"`
	// Etag: Required. The API will fail if the etag does not match the latest etag
	// for this subscription. The etag is retrieved from
	// purchases.subscriptionsv2.get:
	// https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get
	Etag string `json:"etag,omitempty"`
	// ValidateOnly: If set to "true", the request is a dry run to validate the
	// effect of Defer, the subscription would not be impacted.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeferDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeferDuration") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeferralContext: Deferral context of the purchases.subscriptionsv2.defer API.

func (DeferralContext) MarshalJSON ¶
added in v0.265.0
func (s DeferralContext) MarshalJSON() ([]byte, error)
type DeferredItemRemoval ¶
added in v0.247.0
type DeferredItemRemoval struct {
}

DeferredItemRemoval: Information related to deferred item replacement.

type DeferredItemReplacement ¶
added in v0.127.0
type DeferredItemReplacement struct {
	// ProductId: The product_id going to replace the existing product_id.
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

DeferredItemReplacement: Information related to deferred item replacement.

func (DeferredItemReplacement) MarshalJSON ¶
added in v0.127.0
func (s DeferredItemReplacement) MarshalJSON() ([]byte, error)
type DeleteOneTimeProductOfferRequest ¶
added in v0.244.0
type DeleteOneTimeProductOfferRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OfferId: Required. The unique offer ID of the offer to delete.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to delete.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the offer to
	// delete.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The parent purchase option (ID) of the offer to
	// delete.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeleteOneTimeProductOfferRequest: Request message for deleting an one-time product offer.

func (DeleteOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s DeleteOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type DeleteOneTimeProductRequest ¶
added in v0.244.0
type DeleteOneTimeProductRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the one-time product
	// to delete.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The one-time product ID of the one-time product to
	// delete.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeleteOneTimeProductRequest: Request message for deleting a one-time product.

func (DeleteOneTimeProductRequest) MarshalJSON ¶
added in v0.244.0
func (s DeleteOneTimeProductRequest) MarshalJSON() ([]byte, error)
type DeletePurchaseOptionRequest ¶
added in v0.244.0
type DeletePurchaseOptionRequest struct {
	// Force: Optional. This field has no effect for purchase options with no
	// offers under them. For purchase options with associated offers: * If `force`
	// is set to false (default), an error will be returned. * If `force` is set to
	// true, any associated offers under the purchase option will be deleted.
	Force bool `json:"force,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. The parent app (package name) of the purchase option
	// to delete.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the purchase option
	// to delete.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The purchase option ID of the purchase option to
	// delete.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Force") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Force") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeletePurchaseOptionRequest: Request message for deleting a purchase option.

func (DeletePurchaseOptionRequest) MarshalJSON ¶
added in v0.244.0
func (s DeletePurchaseOptionRequest) MarshalJSON() ([]byte, error)
type DeobfuscationFile ¶
type DeobfuscationFile struct {
	// SymbolType: The type of the deobfuscation file.
	//
	// Possible values:
	//   "deobfuscationFileTypeUnspecified" - Unspecified deobfuscation file type.
	//   "proguard" - Proguard deobfuscation file type.
	//   "nativeCode" - Native debugging symbols file type.
	SymbolType string `json:"symbolType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SymbolType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SymbolType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeobfuscationFile: Represents a deobfuscation file.

func (DeobfuscationFile) MarshalJSON ¶
func (s DeobfuscationFile) MarshalJSON() ([]byte, error)
type DeobfuscationFilesUploadResponse ¶
type DeobfuscationFilesUploadResponse struct {
	// DeobfuscationFile: The uploaded Deobfuscation File configuration.
	DeobfuscationFile *DeobfuscationFile `json:"deobfuscationFile,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeobfuscationFile") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeobfuscationFile") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeobfuscationFilesUploadResponse: Responses for the upload.

func (DeobfuscationFilesUploadResponse) MarshalJSON ¶
func (s DeobfuscationFilesUploadResponse) MarshalJSON() ([]byte, error)
type DeployAppRecoveryRequest ¶
added in v0.156.0
type DeployAppRecoveryRequest struct {
}

DeployAppRecoveryRequest: Request message for DeployAppRecovery.

type DeployAppRecoveryResponse ¶
added in v0.156.0
type DeployAppRecoveryResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

DeployAppRecoveryResponse: Response message for DeployAppRecovery.

type DeveloperComment ¶
type DeveloperComment struct {
	// LastModified: The last time at which this comment was updated.
	LastModified *Timestamp `json:"lastModified,omitempty"`
	// Text: The content of the comment, i.e. reply body.
	Text string `json:"text,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastModified") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastModified") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeveloperComment: Developer entry from conversation between user and developer.

func (DeveloperComment) MarshalJSON ¶
func (s DeveloperComment) MarshalJSON() ([]byte, error)
type DeveloperInitiatedCancellation ¶
added in v0.80.0
type DeveloperInitiatedCancellation struct {
}

DeveloperInitiatedCancellation: Information specific to cancellations initiated by developers.

type DeviceFeature ¶
added in v0.130.0
type DeviceFeature struct {
	// FeatureName: Name of the feature.
	FeatureName string `json:"featureName,omitempty"`
	// FeatureVersion: The feature version specified by android:glEsVersion or
	// android:version in in the AndroidManifest.
	FeatureVersion int64 `json:"featureVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FeatureName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FeatureName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceFeature: Represents a device feature.

func (DeviceFeature) MarshalJSON ¶
added in v0.130.0
func (s DeviceFeature) MarshalJSON() ([]byte, error)
type DeviceFeatureTargeting ¶
added in v0.130.0
type DeviceFeatureTargeting struct {
	// RequiredFeature: Feature of the device.
	RequiredFeature *DeviceFeature `json:"requiredFeature,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RequiredFeature") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RequiredFeature") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceFeatureTargeting: Targeting for a device feature.

func (DeviceFeatureTargeting) MarshalJSON ¶
added in v0.130.0
func (s DeviceFeatureTargeting) MarshalJSON() ([]byte, error)
type DeviceGroup ¶
added in v0.74.0
type DeviceGroup struct {
	// DeviceSelectors: Device selectors for this group. A device matching any of
	// the selectors is included in this group.
	DeviceSelectors []*DeviceSelector `json:"deviceSelectors,omitempty"`
	// Name: The name of the group.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceSelectors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceSelectors") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceGroup: A group of devices. A group is defined by a set of device selectors. A device belongs to the group if it matches any selector (logical OR).

func (DeviceGroup) MarshalJSON ¶
added in v0.74.0
func (s DeviceGroup) MarshalJSON() ([]byte, error)
type DeviceId ¶
added in v0.74.0
type DeviceId struct {
	// BuildBrand: Value of Build.BRAND.
	BuildBrand string `json:"buildBrand,omitempty"`
	// BuildDevice: Value of Build.DEVICE.
	BuildDevice string `json:"buildDevice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BuildBrand") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuildBrand") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceId: Identifier of a device.

func (DeviceId) MarshalJSON ¶
added in v0.74.0
func (s DeviceId) MarshalJSON() ([]byte, error)
type DeviceMetadata ¶
type DeviceMetadata struct {
	// CpuMake: Device CPU make, e.g. "Qualcomm"
	CpuMake string `json:"cpuMake,omitempty"`
	// CpuModel: Device CPU model, e.g. "MSM8974"
	CpuModel string `json:"cpuModel,omitempty"`
	// DeviceClass: Device class (e.g. tablet)
	DeviceClass string `json:"deviceClass,omitempty"`
	// GlEsVersion: OpenGL version
	GlEsVersion int64 `json:"glEsVersion,omitempty"`
	// Manufacturer: Device manufacturer (e.g. Motorola)
	Manufacturer string `json:"manufacturer,omitempty"`
	// NativePlatform: Comma separated list of native platforms (e.g. "arm",
	// "arm7")
	NativePlatform string `json:"nativePlatform,omitempty"`
	// ProductName: Device model name (e.g. Droid)
	ProductName string `json:"productName,omitempty"`
	// RamMb: Device RAM in Megabytes, e.g. "2048"
	RamMb int64 `json:"ramMb,omitempty"`
	// ScreenDensityDpi: Screen density in DPI
	ScreenDensityDpi int64 `json:"screenDensityDpi,omitempty"`
	// ScreenHeightPx: Screen height in pixels
	ScreenHeightPx int64 `json:"screenHeightPx,omitempty"`
	// ScreenWidthPx: Screen width in pixels
	ScreenWidthPx int64 `json:"screenWidthPx,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CpuMake") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CpuMake") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceMetadata: Characteristics of the user's device.

func (DeviceMetadata) MarshalJSON ¶
func (s DeviceMetadata) MarshalJSON() ([]byte, error)
type DeviceRam ¶
added in v0.74.0
type DeviceRam struct {
	// MaxBytes: Maximum RAM in bytes (bound excluded).
	MaxBytes int64 `json:"maxBytes,omitempty,string"`
	// MinBytes: Minimum RAM in bytes (bound included).
	MinBytes int64 `json:"minBytes,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "MaxBytes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxBytes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceRam: Conditions about a device's RAM capabilities.

func (DeviceRam) MarshalJSON ¶
added in v0.74.0
func (s DeviceRam) MarshalJSON() ([]byte, error)
type DeviceSelector ¶
added in v0.74.0
type DeviceSelector struct {
	// DeviceRam: Conditions on the device's RAM.
	DeviceRam *DeviceRam `json:"deviceRam,omitempty"`
	// ExcludedDeviceIds: Device models excluded by this selector, even if they
	// match all other conditions.
	ExcludedDeviceIds []*DeviceId `json:"excludedDeviceIds,omitempty"`
	// ForbiddenSystemFeatures: A device that has any of these system features is
	// excluded by this selector, even if it matches all other conditions.
	ForbiddenSystemFeatures []*SystemFeature `json:"forbiddenSystemFeatures,omitempty"`
	// IncludedDeviceIds: Device models included by this selector.
	IncludedDeviceIds []*DeviceId `json:"includedDeviceIds,omitempty"`
	// RequiredSystemFeatures: A device needs to have all these system features to
	// be included by the selector.
	RequiredSystemFeatures []*SystemFeature `json:"requiredSystemFeatures,omitempty"`
	// SystemOnChips: Optional. The SoCs included by this selector. Only works for
	// Android S+ devices.
	SystemOnChips []*SystemOnChip `json:"systemOnChips,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceRam") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceRam") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceSelector: Selector for a device group. A selector consists of a set of conditions on the device that should all match (logical AND) to determine a device group eligibility. For instance, if a selector specifies RAM conditions, device model inclusion and device model exclusion, a device is considered to match if: device matches RAM conditions AND device matches one of the included device models AND device doesn't match excluded device models

func (DeviceSelector) MarshalJSON ¶
added in v0.74.0
func (s DeviceSelector) MarshalJSON() ([]byte, error)
type DeviceSpec ¶
added in v0.16.0
type DeviceSpec struct {
	// ScreenDensity: Screen dpi.
	ScreenDensity int64 `json:"screenDensity,omitempty"`
	// SupportedAbis: Supported ABI architectures in the order of preference. The
	// values should be the string as reported by the platform, e.g. "armeabi-v7a",
	// "x86_64".
	SupportedAbis []string `json:"supportedAbis,omitempty"`
	// SupportedLocales: All installed locales represented as BCP-47 strings, e.g.
	// "en-US".
	SupportedLocales []string `json:"supportedLocales,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ScreenDensity") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ScreenDensity") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceSpec: The device spec used to generate a system APK.

func (DeviceSpec) MarshalJSON ¶
added in v0.16.0
func (s DeviceSpec) MarshalJSON() ([]byte, error)
type DeviceTier ¶
added in v0.74.0
type DeviceTier struct {
	// DeviceGroupNames: Groups of devices included in this tier. These groups must
	// be defined explicitly under device_groups in this configuration.
	DeviceGroupNames []string `json:"deviceGroupNames,omitempty"`
	// Level: The priority level of the tier. Tiers are evaluated in descending
	// order of level: the highest level tier has the highest priority. The highest
	// tier matching a given device is selected for that device. You should use a
	// contiguous range of levels for your tiers in a tier set; tier levels in a
	// tier set must be unique. For instance, if your tier set has 4 tiers
	// (including the global fallback), you should define tiers 1, 2 and 3 in this
	// configuration. Note: tier 0 is implicitly defined as a global fallback and
	// selected for devices that don't match any of the tiers explicitly defined
	// here. You mustn't define level 0 explicitly in this configuration.
	Level int64 `json:"level,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceGroupNames") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceGroupNames") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceTier: A single device tier. Devices matching any of the device groups in device_group_names are considered to match the tier.

func (DeviceTier) MarshalJSON ¶
added in v0.74.0
func (s DeviceTier) MarshalJSON() ([]byte, error)
type DeviceTierConfig ¶
added in v0.74.0
type DeviceTierConfig struct {
	// DeviceGroups: Definition of device groups for the app.
	DeviceGroups []*DeviceGroup `json:"deviceGroups,omitempty"`
	// DeviceTierConfigId: Output only. The device tier config ID.
	DeviceTierConfigId int64 `json:"deviceTierConfigId,omitempty,string"`
	// DeviceTierSet: Definition of the set of device tiers for the app.
	DeviceTierSet *DeviceTierSet `json:"deviceTierSet,omitempty"`
	// UserCountrySets: Definition of user country sets for the app.
	UserCountrySets []*UserCountrySet `json:"userCountrySets,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeviceGroups") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceGroups") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceTierConfig: Configuration describing device targeting criteria for the content of an app.

func (DeviceTierConfig) MarshalJSON ¶
added in v0.74.0
func (s DeviceTierConfig) MarshalJSON() ([]byte, error)
type DeviceTierSet ¶
added in v0.74.0
type DeviceTierSet struct {
	// DeviceTiers: Device tiers belonging to the set.
	DeviceTiers []*DeviceTier `json:"deviceTiers,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceTiers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceTiers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeviceTierSet: A set of device tiers. A tier set determines what variation of app content gets served to a specific device, for device-targeted content. You should assign a priority level to each tier, which determines the ordering by which they are evaluated by Play. See the documentation of DeviceTier.level for more details.

func (DeviceTierSet) MarshalJSON ¶
added in v0.74.0
func (s DeviceTierSet) MarshalJSON() ([]byte, error)
type EditsApksAddexternallyhostedCall ¶
type EditsApksAddexternallyhostedCall struct {
	// contains filtered or unexported fields
}
func (*EditsApksAddexternallyhostedCall) Context ¶
func (c *EditsApksAddexternallyhostedCall) Context(ctx context.Context) *EditsApksAddexternallyhostedCall

Context sets the context to be used in this call's Do method.

func (*EditsApksAddexternallyhostedCall) Do ¶
func (c *EditsApksAddexternallyhostedCall) Do(opts ...googleapi.CallOption) (*ApksAddExternallyHostedResponse, error)

Do executes the "androidpublisher.edits.apks.addexternallyhosted" call. Any non-2xx status code is an error. Response headers are in either *ApksAddExternallyHostedResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsApksAddexternallyhostedCall) Fields ¶
func (c *EditsApksAddexternallyhostedCall) Fields(s ...googleapi.Field) *EditsApksAddexternallyhostedCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsApksAddexternallyhostedCall) Header ¶
func (c *EditsApksAddexternallyhostedCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsApksListCall ¶
type EditsApksListCall struct {
	// contains filtered or unexported fields
}
func (*EditsApksListCall) Context ¶
func (c *EditsApksListCall) Context(ctx context.Context) *EditsApksListCall

Context sets the context to be used in this call's Do method.

func (*EditsApksListCall) Do ¶
func (c *EditsApksListCall) Do(opts ...googleapi.CallOption) (*ApksListResponse, error)

Do executes the "androidpublisher.edits.apks.list" call. Any non-2xx status code is an error. Response headers are in either *ApksListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsApksListCall) Fields ¶
func (c *EditsApksListCall) Fields(s ...googleapi.Field) *EditsApksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsApksListCall) Header ¶
func (c *EditsApksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsApksListCall) IfNoneMatch ¶
func (c *EditsApksListCall) IfNoneMatch(entityTag string) *EditsApksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsApksService ¶
type EditsApksService struct {
	// contains filtered or unexported fields
}
func NewEditsApksService ¶
func NewEditsApksService(s *Service) *EditsApksService
func (*EditsApksService) Addexternallyhosted ¶
func (r *EditsApksService) Addexternallyhosted(packageName string, editId string, apksaddexternallyhostedrequest *ApksAddExternallyHostedRequest) *EditsApksAddexternallyhostedCall

Addexternallyhosted: Creates a new APK without uploading the APK itself to Google Play, instead hosting the APK at a specified URL. This function is only available to organizations using Managed Play whose application is configured to restrict distribution to the organizations.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsApksService) List ¶
func (r *EditsApksService) List(packageName string, editId string) *EditsApksListCall

List: Lists all current APKs of the app and edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsApksService) Upload ¶
func (r *EditsApksService) Upload(packageName string, editId string) *EditsApksUploadCall

Upload: Uploads an APK and adds to the current edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

type EditsApksUploadCall ¶
type EditsApksUploadCall struct {
	// contains filtered or unexported fields
}
func (*EditsApksUploadCall) Context ¶
func (c *EditsApksUploadCall) Context(ctx context.Context) *EditsApksUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*EditsApksUploadCall) Do ¶
func (c *EditsApksUploadCall) Do(opts ...googleapi.CallOption) (*Apk, error)

Do executes the "androidpublisher.edits.apks.upload" call. Any non-2xx status code is an error. Response headers are in either *Apk.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsApksUploadCall) Fields ¶
func (c *EditsApksUploadCall) Fields(s ...googleapi.Field) *EditsApksUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsApksUploadCall) Header ¶
func (c *EditsApksUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsApksUploadCall) Media ¶
func (c *EditsApksUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsApksUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*EditsApksUploadCall) ProgressUpdater ¶
func (c *EditsApksUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsApksUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*EditsApksUploadCall)
ResumableMedia
DEPRECATED
type EditsBundlesListCall ¶
type EditsBundlesListCall struct {
	// contains filtered or unexported fields
}
func (*EditsBundlesListCall) Context ¶
func (c *EditsBundlesListCall) Context(ctx context.Context) *EditsBundlesListCall

Context sets the context to be used in this call's Do method.

func (*EditsBundlesListCall) Do ¶
func (c *EditsBundlesListCall) Do(opts ...googleapi.CallOption) (*BundlesListResponse, error)

Do executes the "androidpublisher.edits.bundles.list" call. Any non-2xx status code is an error. Response headers are in either *BundlesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsBundlesListCall) Fields ¶
func (c *EditsBundlesListCall) Fields(s ...googleapi.Field) *EditsBundlesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsBundlesListCall) Header ¶
func (c *EditsBundlesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsBundlesListCall) IfNoneMatch ¶
func (c *EditsBundlesListCall) IfNoneMatch(entityTag string) *EditsBundlesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsBundlesService ¶
type EditsBundlesService struct {
	// contains filtered or unexported fields
}
func NewEditsBundlesService ¶
func NewEditsBundlesService(s *Service) *EditsBundlesService
func (*EditsBundlesService) List ¶
func (r *EditsBundlesService) List(packageName string, editId string) *EditsBundlesListCall

List: Lists all current Android App Bundles of the app and edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsBundlesService) Upload ¶
func (r *EditsBundlesService) Upload(packageName string, editId string) *EditsBundlesUploadCall

Upload: Uploads a new Android App Bundle to this edit. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See Timeouts and Errors (https://developers.google.com/api-client-library/java/google-api-java-client/errors) for an example in java.

- editId: Identifier of the edit. - packageName: Package name of the app.

type EditsBundlesUploadCall ¶
type EditsBundlesUploadCall struct {
	// contains filtered or unexported fields
}
func (*EditsBundlesUploadCall) AckBundleInstallationWarning ¶
func (c *EditsBundlesUploadCall) AckBundleInstallationWarning(ackBundleInstallationWarning bool) *EditsBundlesUploadCall

AckBundleInstallationWarning sets the optional parameter "ackBundleInstallationWarning": Deprecated. The installation warning has been removed, it's not necessary to set this field anymore.

func (*EditsBundlesUploadCall) Context ¶
func (c *EditsBundlesUploadCall) Context(ctx context.Context) *EditsBundlesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*EditsBundlesUploadCall) DeviceTierConfigId ¶
added in v0.96.0
func (c *EditsBundlesUploadCall) DeviceTierConfigId(deviceTierConfigId string) *EditsBundlesUploadCall

DeviceTierConfigId sets the optional parameter "deviceTierConfigId": Device tier config (DTC) to be used for generating deliverables (APKs). Contains id of the DTC or "LATEST" for last uploaded DTC.

func (*EditsBundlesUploadCall) Do ¶
func (c *EditsBundlesUploadCall) Do(opts ...googleapi.CallOption) (*Bundle, error)

Do executes the "androidpublisher.edits.bundles.upload" call. Any non-2xx status code is an error. Response headers are in either *Bundle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsBundlesUploadCall) Fields ¶
func (c *EditsBundlesUploadCall) Fields(s ...googleapi.Field) *EditsBundlesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsBundlesUploadCall) Header ¶
func (c *EditsBundlesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsBundlesUploadCall) Media ¶
func (c *EditsBundlesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsBundlesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*EditsBundlesUploadCall) ProgressUpdater ¶
func (c *EditsBundlesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsBundlesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*EditsBundlesUploadCall)
ResumableMedia
DEPRECATED
type EditsCommitCall ¶
type EditsCommitCall struct {
	// contains filtered or unexported fields
}
func (*EditsCommitCall) ChangesNotSentForReview ¶
added in v0.46.0
func (c *EditsCommitCall) ChangesNotSentForReview(changesNotSentForReview bool) *EditsCommitCall

ChangesNotSentForReview sets the optional parameter "changesNotSentForReview": When a rejection happens, the parameter will make sure that the changes in this edit won't be reviewed until they are explicitly sent for review from within the Google Play Console UI. These changes will be added to any other changes that are not yet sent for review.

func (*EditsCommitCall) Context ¶
func (c *EditsCommitCall) Context(ctx context.Context) *EditsCommitCall

Context sets the context to be used in this call's Do method.

func (*EditsCommitCall) Do ¶
func (c *EditsCommitCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)

Do executes the "androidpublisher.edits.commit" call. Any non-2xx status code is an error. Response headers are in either *AppEdit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsCommitCall) Fields ¶
func (c *EditsCommitCall) Fields(s ...googleapi.Field) *EditsCommitCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsCommitCall) Header ¶
func (c *EditsCommitCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsCountryavailabilityGetCall ¶
added in v0.61.0
type EditsCountryavailabilityGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsCountryavailabilityGetCall) Context ¶
added in v0.61.0
func (c *EditsCountryavailabilityGetCall) Context(ctx context.Context) *EditsCountryavailabilityGetCall

Context sets the context to be used in this call's Do method.

func (*EditsCountryavailabilityGetCall) Do ¶
added in v0.61.0
func (c *EditsCountryavailabilityGetCall) Do(opts ...googleapi.CallOption) (*TrackCountryAvailability, error)

Do executes the "androidpublisher.edits.countryavailability.get" call. Any non-2xx status code is an error. Response headers are in either *TrackCountryAvailability.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsCountryavailabilityGetCall) Fields ¶
added in v0.61.0
func (c *EditsCountryavailabilityGetCall) Fields(s ...googleapi.Field) *EditsCountryavailabilityGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsCountryavailabilityGetCall) Header ¶
added in v0.61.0
func (c *EditsCountryavailabilityGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsCountryavailabilityGetCall) IfNoneMatch ¶
added in v0.61.0
func (c *EditsCountryavailabilityGetCall) IfNoneMatch(entityTag string) *EditsCountryavailabilityGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsCountryavailabilityService ¶
added in v0.61.0
type EditsCountryavailabilityService struct {
	// contains filtered or unexported fields
}
func NewEditsCountryavailabilityService ¶
added in v0.61.0
func NewEditsCountryavailabilityService(s *Service) *EditsCountryavailabilityService
func (*EditsCountryavailabilityService) Get ¶
added in v0.61.0
func (r *EditsCountryavailabilityService) Get(packageName string, editId string, track string) *EditsCountryavailabilityGetCall

Get: Gets country availability.

- editId: Identifier of the edit. - packageName: Package name of the app. - track: The track to read from.

type EditsDeleteCall ¶
type EditsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*EditsDeleteCall) Context ¶
func (c *EditsDeleteCall) Context(ctx context.Context) *EditsDeleteCall

Context sets the context to be used in this call's Do method.

func (*EditsDeleteCall) Do ¶
func (c *EditsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.edits.delete" call.

func (*EditsDeleteCall) Fields ¶
func (c *EditsDeleteCall) Fields(s ...googleapi.Field) *EditsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsDeleteCall) Header ¶
func (c *EditsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsDeobfuscationfilesService ¶
type EditsDeobfuscationfilesService struct {
	// contains filtered or unexported fields
}
func NewEditsDeobfuscationfilesService ¶
func NewEditsDeobfuscationfilesService(s *Service) *EditsDeobfuscationfilesService
func (*EditsDeobfuscationfilesService) Upload ¶
func (r *EditsDeobfuscationfilesService) Upload(packageNameid string, editId string, apkVersionCode int64, deobfuscationFileType string) *EditsDeobfuscationfilesUploadCall

Upload: Uploads a new deobfuscation file and attaches to the specified APK.

apkVersionCode: The version code of the APK whose Deobfuscation File is being uploaded.
deobfuscationFileType: The type of the deobfuscation file.
editId: Unique identifier for this edit.
packageName: Unique identifier for the Android app.
type EditsDeobfuscationfilesUploadCall ¶
type EditsDeobfuscationfilesUploadCall struct {
	// contains filtered or unexported fields
}
func (*EditsDeobfuscationfilesUploadCall) Context ¶
func (c *EditsDeobfuscationfilesUploadCall) Context(ctx context.Context) *EditsDeobfuscationfilesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*EditsDeobfuscationfilesUploadCall) Do ¶
func (c *EditsDeobfuscationfilesUploadCall) Do(opts ...googleapi.CallOption) (*DeobfuscationFilesUploadResponse, error)

Do executes the "androidpublisher.edits.deobfuscationfiles.upload" call. Any non-2xx status code is an error. Response headers are in either *DeobfuscationFilesUploadResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsDeobfuscationfilesUploadCall) Fields ¶
func (c *EditsDeobfuscationfilesUploadCall) Fields(s ...googleapi.Field) *EditsDeobfuscationfilesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsDeobfuscationfilesUploadCall) Header ¶
func (c *EditsDeobfuscationfilesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsDeobfuscationfilesUploadCall) Media ¶
func (c *EditsDeobfuscationfilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsDeobfuscationfilesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*EditsDeobfuscationfilesUploadCall) ProgressUpdater ¶
func (c *EditsDeobfuscationfilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsDeobfuscationfilesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*EditsDeobfuscationfilesUploadCall)
ResumableMedia
DEPRECATED
type EditsDetailsGetCall ¶
type EditsDetailsGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsDetailsGetCall) Context ¶
func (c *EditsDetailsGetCall) Context(ctx context.Context) *EditsDetailsGetCall

Context sets the context to be used in this call's Do method.

func (*EditsDetailsGetCall) Do ¶
func (c *EditsDetailsGetCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)

Do executes the "androidpublisher.edits.details.get" call. Any non-2xx status code is an error. Response headers are in either *AppDetails.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsDetailsGetCall) Fields ¶
func (c *EditsDetailsGetCall) Fields(s ...googleapi.Field) *EditsDetailsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsDetailsGetCall) Header ¶
func (c *EditsDetailsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsDetailsGetCall) IfNoneMatch ¶
func (c *EditsDetailsGetCall) IfNoneMatch(entityTag string) *EditsDetailsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsDetailsPatchCall ¶
type EditsDetailsPatchCall struct {
	// contains filtered or unexported fields
}
func (*EditsDetailsPatchCall) Context ¶
func (c *EditsDetailsPatchCall) Context(ctx context.Context) *EditsDetailsPatchCall

Context sets the context to be used in this call's Do method.

func (*EditsDetailsPatchCall) Do ¶
func (c *EditsDetailsPatchCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)

Do executes the "androidpublisher.edits.details.patch" call. Any non-2xx status code is an error. Response headers are in either *AppDetails.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsDetailsPatchCall) Fields ¶
func (c *EditsDetailsPatchCall) Fields(s ...googleapi.Field) *EditsDetailsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsDetailsPatchCall) Header ¶
func (c *EditsDetailsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsDetailsService ¶
type EditsDetailsService struct {
	// contains filtered or unexported fields
}
func NewEditsDetailsService ¶
func NewEditsDetailsService(s *Service) *EditsDetailsService
func (*EditsDetailsService) Get ¶
func (r *EditsDetailsService) Get(packageName string, editId string) *EditsDetailsGetCall

Get: Gets details of an app.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsDetailsService) Patch ¶
func (r *EditsDetailsService) Patch(packageName string, editId string, appdetails *AppDetails) *EditsDetailsPatchCall

Patch: Patches details of an app.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsDetailsService) Update ¶
func (r *EditsDetailsService) Update(packageName string, editId string, appdetails *AppDetails) *EditsDetailsUpdateCall

Update: Updates details of an app.

- editId: Identifier of the edit. - packageName: Package name of the app.

type EditsDetailsUpdateCall ¶
type EditsDetailsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EditsDetailsUpdateCall) Context ¶
func (c *EditsDetailsUpdateCall) Context(ctx context.Context) *EditsDetailsUpdateCall

Context sets the context to be used in this call's Do method.

func (*EditsDetailsUpdateCall) Do ¶
func (c *EditsDetailsUpdateCall) Do(opts ...googleapi.CallOption) (*AppDetails, error)

Do executes the "androidpublisher.edits.details.update" call. Any non-2xx status code is an error. Response headers are in either *AppDetails.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsDetailsUpdateCall) Fields ¶
func (c *EditsDetailsUpdateCall) Fields(s ...googleapi.Field) *EditsDetailsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsDetailsUpdateCall) Header ¶
func (c *EditsDetailsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsExpansionfilesGetCall ¶
type EditsExpansionfilesGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsExpansionfilesGetCall) Context ¶
func (c *EditsExpansionfilesGetCall) Context(ctx context.Context) *EditsExpansionfilesGetCall

Context sets the context to be used in this call's Do method.

func (*EditsExpansionfilesGetCall) Do ¶
func (c *EditsExpansionfilesGetCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)

Do executes the "androidpublisher.edits.expansionfiles.get" call. Any non-2xx status code is an error. Response headers are in either *ExpansionFile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsExpansionfilesGetCall) Fields ¶
func (c *EditsExpansionfilesGetCall) Fields(s ...googleapi.Field) *EditsExpansionfilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsExpansionfilesGetCall) Header ¶
func (c *EditsExpansionfilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsExpansionfilesGetCall) IfNoneMatch ¶
func (c *EditsExpansionfilesGetCall) IfNoneMatch(entityTag string) *EditsExpansionfilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsExpansionfilesPatchCall ¶
type EditsExpansionfilesPatchCall struct {
	// contains filtered or unexported fields
}
func (*EditsExpansionfilesPatchCall) Context ¶
func (c *EditsExpansionfilesPatchCall) Context(ctx context.Context) *EditsExpansionfilesPatchCall

Context sets the context to be used in this call's Do method.

func (*EditsExpansionfilesPatchCall) Do ¶
func (c *EditsExpansionfilesPatchCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)

Do executes the "androidpublisher.edits.expansionfiles.patch" call. Any non-2xx status code is an error. Response headers are in either *ExpansionFile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsExpansionfilesPatchCall) Fields ¶
func (c *EditsExpansionfilesPatchCall) Fields(s ...googleapi.Field) *EditsExpansionfilesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsExpansionfilesPatchCall) Header ¶
func (c *EditsExpansionfilesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsExpansionfilesService ¶
type EditsExpansionfilesService struct {
	// contains filtered or unexported fields
}
func NewEditsExpansionfilesService ¶
func NewEditsExpansionfilesService(s *Service) *EditsExpansionfilesService
func (*EditsExpansionfilesService) Get ¶
func (r *EditsExpansionfilesService) Get(packageName string, editId string, apkVersionCode int64, expansionFileType string) *EditsExpansionfilesGetCall

Get: Fetches the expansion file configuration for the specified APK.

apkVersionCode: The version code of the APK whose expansion file configuration is being read or modified.
editId: Identifier of the edit.
expansionFileType: The file type of the file configuration which is being read or modified.
packageName: Package name of the app.
func (*EditsExpansionfilesService) Patch ¶
func (r *EditsExpansionfilesService) Patch(packageName string, editId string, apkVersionCode int64, expansionFileType string, expansionfile *ExpansionFile) *EditsExpansionfilesPatchCall

Patch: Patches the APK's expansion file configuration to reference another APK's expansion file. To add a new expansion file use the Upload method.

apkVersionCode: The version code of the APK whose expansion file configuration is being read or modified.
editId: Identifier of the edit.
expansionFileType: The file type of the expansion file configuration which is being updated.
packageName: Package name of the app.
func (*EditsExpansionfilesService) Update ¶
func (r *EditsExpansionfilesService) Update(packageName string, editId string, apkVersionCode int64, expansionFileType string, expansionfile *ExpansionFile) *EditsExpansionfilesUpdateCall

Update: Updates the APK's expansion file configuration to reference another APK's expansion file. To add a new expansion file use the Upload method.

apkVersionCode: The version code of the APK whose expansion file configuration is being read or modified.
editId: Identifier of the edit.
expansionFileType: The file type of the file configuration which is being read or modified.
packageName: Package name of the app.
func (*EditsExpansionfilesService) Upload ¶
func (r *EditsExpansionfilesService) Upload(packageName string, editId string, apkVersionCode int64, expansionFileType string) *EditsExpansionfilesUploadCall

Upload: Uploads a new expansion file and attaches to the specified APK.

apkVersionCode: The version code of the APK whose expansion file configuration is being read or modified.
editId: Identifier of the edit.
expansionFileType: The file type of the expansion file configuration which is being updated.
packageName: Package name of the app.
type EditsExpansionfilesUpdateCall ¶
type EditsExpansionfilesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EditsExpansionfilesUpdateCall) Context ¶
func (c *EditsExpansionfilesUpdateCall) Context(ctx context.Context) *EditsExpansionfilesUpdateCall

Context sets the context to be used in this call's Do method.

func (*EditsExpansionfilesUpdateCall) Do ¶
func (c *EditsExpansionfilesUpdateCall) Do(opts ...googleapi.CallOption) (*ExpansionFile, error)

Do executes the "androidpublisher.edits.expansionfiles.update" call. Any non-2xx status code is an error. Response headers are in either *ExpansionFile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsExpansionfilesUpdateCall) Fields ¶
func (c *EditsExpansionfilesUpdateCall) Fields(s ...googleapi.Field) *EditsExpansionfilesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsExpansionfilesUpdateCall) Header ¶
func (c *EditsExpansionfilesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsExpansionfilesUploadCall ¶
type EditsExpansionfilesUploadCall struct {
	// contains filtered or unexported fields
}
func (*EditsExpansionfilesUploadCall) Context ¶
func (c *EditsExpansionfilesUploadCall) Context(ctx context.Context) *EditsExpansionfilesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*EditsExpansionfilesUploadCall) Do ¶
func (c *EditsExpansionfilesUploadCall) Do(opts ...googleapi.CallOption) (*ExpansionFilesUploadResponse, error)

Do executes the "androidpublisher.edits.expansionfiles.upload" call. Any non-2xx status code is an error. Response headers are in either *ExpansionFilesUploadResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsExpansionfilesUploadCall) Fields ¶
func (c *EditsExpansionfilesUploadCall) Fields(s ...googleapi.Field) *EditsExpansionfilesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsExpansionfilesUploadCall) Header ¶
func (c *EditsExpansionfilesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsExpansionfilesUploadCall) Media ¶
func (c *EditsExpansionfilesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsExpansionfilesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*EditsExpansionfilesUploadCall) ProgressUpdater ¶
func (c *EditsExpansionfilesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsExpansionfilesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*EditsExpansionfilesUploadCall)
ResumableMedia
DEPRECATED
type EditsGetCall ¶
type EditsGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsGetCall) Context ¶
func (c *EditsGetCall) Context(ctx context.Context) *EditsGetCall

Context sets the context to be used in this call's Do method.

func (*EditsGetCall) Do ¶
func (c *EditsGetCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)

Do executes the "androidpublisher.edits.get" call. Any non-2xx status code is an error. Response headers are in either *AppEdit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsGetCall) Fields ¶
func (c *EditsGetCall) Fields(s ...googleapi.Field) *EditsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsGetCall) Header ¶
func (c *EditsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsGetCall) IfNoneMatch ¶
func (c *EditsGetCall) IfNoneMatch(entityTag string) *EditsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsImagesDeleteCall ¶
type EditsImagesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*EditsImagesDeleteCall) Context ¶
func (c *EditsImagesDeleteCall) Context(ctx context.Context) *EditsImagesDeleteCall

Context sets the context to be used in this call's Do method.

func (*EditsImagesDeleteCall) Do ¶
func (c *EditsImagesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.edits.images.delete" call.

func (*EditsImagesDeleteCall) Fields ¶
func (c *EditsImagesDeleteCall) Fields(s ...googleapi.Field) *EditsImagesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsImagesDeleteCall) Header ¶
func (c *EditsImagesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsImagesDeleteallCall ¶
type EditsImagesDeleteallCall struct {
	// contains filtered or unexported fields
}
func (*EditsImagesDeleteallCall) Context ¶
func (c *EditsImagesDeleteallCall) Context(ctx context.Context) *EditsImagesDeleteallCall

Context sets the context to be used in this call's Do method.

func (*EditsImagesDeleteallCall) Do ¶
func (c *EditsImagesDeleteallCall) Do(opts ...googleapi.CallOption) (*ImagesDeleteAllResponse, error)

Do executes the "androidpublisher.edits.images.deleteall" call. Any non-2xx status code is an error. Response headers are in either *ImagesDeleteAllResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsImagesDeleteallCall) Fields ¶
func (c *EditsImagesDeleteallCall) Fields(s ...googleapi.Field) *EditsImagesDeleteallCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsImagesDeleteallCall) Header ¶
func (c *EditsImagesDeleteallCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsImagesListCall ¶
type EditsImagesListCall struct {
	// contains filtered or unexported fields
}
func (*EditsImagesListCall) Context ¶
func (c *EditsImagesListCall) Context(ctx context.Context) *EditsImagesListCall

Context sets the context to be used in this call's Do method.

func (*EditsImagesListCall) Do ¶
func (c *EditsImagesListCall) Do(opts ...googleapi.CallOption) (*ImagesListResponse, error)

Do executes the "androidpublisher.edits.images.list" call. Any non-2xx status code is an error. Response headers are in either *ImagesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsImagesListCall) Fields ¶
func (c *EditsImagesListCall) Fields(s ...googleapi.Field) *EditsImagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsImagesListCall) Header ¶
func (c *EditsImagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsImagesListCall) IfNoneMatch ¶
func (c *EditsImagesListCall) IfNoneMatch(entityTag string) *EditsImagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsImagesService ¶
type EditsImagesService struct {
	// contains filtered or unexported fields
}
func NewEditsImagesService ¶
func NewEditsImagesService(s *Service) *EditsImagesService
func (*EditsImagesService) Delete ¶
func (r *EditsImagesService) Delete(packageName string, editId string, language string, imageType string, imageId string) *EditsImagesDeleteCall

Delete: Deletes the image (specified by id) from the edit.

editId: Identifier of the edit.
imageId: Unique identifier an image within the set of images attached to this edit.
imageType: Type of the Image.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German).
packageName: Package name of the app.
func (*EditsImagesService) Deleteall ¶
func (r *EditsImagesService) Deleteall(packageName string, editId string, language string, imageType string) *EditsImagesDeleteallCall

Deleteall: Deletes all images for the specified language and image type. Returns an empty response if no images are found.

editId: Identifier of the edit.
imageType: Type of the Image. Providing an image type that refers to no images is a no-op.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German). Providing a language that is not supported by the App is a no-op.
packageName: Package name of the app.
func (*EditsImagesService) List ¶
func (r *EditsImagesService) List(packageName string, editId string, language string, imageType string) *EditsImagesListCall

List: Lists all images. The response may be empty.

editId: Identifier of the edit.
imageType: Type of the Image. Providing an image type that refers to no images will return an empty response.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German). There must be a store listing for the specified language.
packageName: Package name of the app.
func (*EditsImagesService) Upload ¶
func (r *EditsImagesService) Upload(packageName string, editId string, language string, imageType string) *EditsImagesUploadCall

Upload: Uploads an image of the specified language and image type, and adds to the edit.

editId: Identifier of the edit.
imageType: Type of the Image.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German). Providing a language that is not supported by the App is a no-op.
packageName: Package name of the app.
type EditsImagesUploadCall ¶
type EditsImagesUploadCall struct {
	// contains filtered or unexported fields
}
func (*EditsImagesUploadCall) Context ¶
func (c *EditsImagesUploadCall) Context(ctx context.Context) *EditsImagesUploadCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*EditsImagesUploadCall) Do ¶
func (c *EditsImagesUploadCall) Do(opts ...googleapi.CallOption) (*ImagesUploadResponse, error)

Do executes the "androidpublisher.edits.images.upload" call. Any non-2xx status code is an error. Response headers are in either *ImagesUploadResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsImagesUploadCall) Fields ¶
func (c *EditsImagesUploadCall) Fields(s ...googleapi.Field) *EditsImagesUploadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsImagesUploadCall) Header ¶
func (c *EditsImagesUploadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsImagesUploadCall) Media ¶
func (c *EditsImagesUploadCall) Media(r io.Reader, options ...googleapi.MediaOption) *EditsImagesUploadCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*EditsImagesUploadCall) ProgressUpdater ¶
func (c *EditsImagesUploadCall) ProgressUpdater(pu googleapi.ProgressUpdater) *EditsImagesUploadCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*EditsImagesUploadCall)
ResumableMedia
DEPRECATED
type EditsInsertCall ¶
type EditsInsertCall struct {
	// contains filtered or unexported fields
}
func (*EditsInsertCall) Context ¶
func (c *EditsInsertCall) Context(ctx context.Context) *EditsInsertCall

Context sets the context to be used in this call's Do method.

func (*EditsInsertCall) Do ¶
func (c *EditsInsertCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)

Do executes the "androidpublisher.edits.insert" call. Any non-2xx status code is an error. Response headers are in either *AppEdit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsInsertCall) Fields ¶
func (c *EditsInsertCall) Fields(s ...googleapi.Field) *EditsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsInsertCall) Header ¶
func (c *EditsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsListingsDeleteCall ¶
type EditsListingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsDeleteCall) Context ¶
func (c *EditsListingsDeleteCall) Context(ctx context.Context) *EditsListingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsDeleteCall) Do ¶
func (c *EditsListingsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.edits.listings.delete" call.

func (*EditsListingsDeleteCall) Fields ¶
func (c *EditsListingsDeleteCall) Fields(s ...googleapi.Field) *EditsListingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsDeleteCall) Header ¶
func (c *EditsListingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsListingsDeleteallCall ¶
type EditsListingsDeleteallCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsDeleteallCall) Context ¶
func (c *EditsListingsDeleteallCall) Context(ctx context.Context) *EditsListingsDeleteallCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsDeleteallCall) Do ¶
func (c *EditsListingsDeleteallCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.edits.listings.deleteall" call.

func (*EditsListingsDeleteallCall) Fields ¶
func (c *EditsListingsDeleteallCall) Fields(s ...googleapi.Field) *EditsListingsDeleteallCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsDeleteallCall) Header ¶
func (c *EditsListingsDeleteallCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsListingsGetCall ¶
type EditsListingsGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsGetCall) Context ¶
func (c *EditsListingsGetCall) Context(ctx context.Context) *EditsListingsGetCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsGetCall) Do ¶
func (c *EditsListingsGetCall) Do(opts ...googleapi.CallOption) (*Listing, error)

Do executes the "androidpublisher.edits.listings.get" call. Any non-2xx status code is an error. Response headers are in either *Listing.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsListingsGetCall) Fields ¶
func (c *EditsListingsGetCall) Fields(s ...googleapi.Field) *EditsListingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsGetCall) Header ¶
func (c *EditsListingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsListingsGetCall) IfNoneMatch ¶
func (c *EditsListingsGetCall) IfNoneMatch(entityTag string) *EditsListingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsListingsListCall ¶
type EditsListingsListCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsListCall) Context ¶
func (c *EditsListingsListCall) Context(ctx context.Context) *EditsListingsListCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsListCall) Do ¶
func (c *EditsListingsListCall) Do(opts ...googleapi.CallOption) (*ListingsListResponse, error)

Do executes the "androidpublisher.edits.listings.list" call. Any non-2xx status code is an error. Response headers are in either *ListingsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsListingsListCall) Fields ¶
func (c *EditsListingsListCall) Fields(s ...googleapi.Field) *EditsListingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsListCall) Header ¶
func (c *EditsListingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsListingsListCall) IfNoneMatch ¶
func (c *EditsListingsListCall) IfNoneMatch(entityTag string) *EditsListingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsListingsPatchCall ¶
type EditsListingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsPatchCall) Context ¶
func (c *EditsListingsPatchCall) Context(ctx context.Context) *EditsListingsPatchCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsPatchCall) Do ¶
func (c *EditsListingsPatchCall) Do(opts ...googleapi.CallOption) (*Listing, error)

Do executes the "androidpublisher.edits.listings.patch" call. Any non-2xx status code is an error. Response headers are in either *Listing.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsListingsPatchCall) Fields ¶
func (c *EditsListingsPatchCall) Fields(s ...googleapi.Field) *EditsListingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsPatchCall) Header ¶
func (c *EditsListingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsListingsService ¶
type EditsListingsService struct {
	// contains filtered or unexported fields
}
func NewEditsListingsService ¶
func NewEditsListingsService(s *Service) *EditsListingsService
func (*EditsListingsService) Delete ¶
func (r *EditsListingsService) Delete(packageName string, editId string, language string) *EditsListingsDeleteCall

Delete: Deletes a localized store listing.

editId: Identifier of the edit.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German).
packageName: Package name of the app.
func (*EditsListingsService) Deleteall ¶
func (r *EditsListingsService) Deleteall(packageName string, editId string) *EditsListingsDeleteallCall

Deleteall: Deletes all store listings.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsListingsService) Get ¶
func (r *EditsListingsService) Get(packageName string, editId string, language string) *EditsListingsGetCall

Get: Gets a localized store listing.

editId: Identifier of the edit.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German).
packageName: Package name of the app.
func (*EditsListingsService) List ¶
func (r *EditsListingsService) List(packageName string, editId string) *EditsListingsListCall

List: Lists all localized store listings.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsListingsService) Patch ¶
func (r *EditsListingsService) Patch(packageName string, editId string, language string, listing *Listing) *EditsListingsPatchCall

Patch: Patches a localized store listing.

editId: Identifier of the edit.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German).
packageName: Package name of the app.
func (*EditsListingsService) Update ¶
func (r *EditsListingsService) Update(packageName string, editId string, language string, listing *Listing) *EditsListingsUpdateCall

Update: Creates or updates a localized store listing.

editId: Identifier of the edit.
language: Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German).
packageName: Package name of the app.
type EditsListingsUpdateCall ¶
type EditsListingsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EditsListingsUpdateCall) Context ¶
func (c *EditsListingsUpdateCall) Context(ctx context.Context) *EditsListingsUpdateCall

Context sets the context to be used in this call's Do method.

func (*EditsListingsUpdateCall) Do ¶
func (c *EditsListingsUpdateCall) Do(opts ...googleapi.CallOption) (*Listing, error)

Do executes the "androidpublisher.edits.listings.update" call. Any non-2xx status code is an error. Response headers are in either *Listing.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsListingsUpdateCall) Fields ¶
func (c *EditsListingsUpdateCall) Fields(s ...googleapi.Field) *EditsListingsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsListingsUpdateCall) Header ¶
func (c *EditsListingsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsService ¶
type EditsService struct {
	Apks *EditsApksService

	Bundles *EditsBundlesService

	Countryavailability *EditsCountryavailabilityService

	Deobfuscationfiles *EditsDeobfuscationfilesService

	Details *EditsDetailsService

	Expansionfiles *EditsExpansionfilesService

	Images *EditsImagesService

	Listings *EditsListingsService

	Testers *EditsTestersService

	Tracks *EditsTracksService
	// contains filtered or unexported fields
}
func NewEditsService ¶
func NewEditsService(s *Service) *EditsService
func (*EditsService) Commit ¶
func (r *EditsService) Commit(packageName string, editId string) *EditsCommitCall

Commit: Commits an app edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsService) Delete ¶
func (r *EditsService) Delete(packageName string, editId string) *EditsDeleteCall

Delete: Deletes an app edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsService) Get ¶
func (r *EditsService) Get(packageName string, editId string) *EditsGetCall

Get: Gets an app edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsService) Insert ¶
func (r *EditsService) Insert(packageName string, appedit *AppEdit) *EditsInsertCall

Insert: Creates a new edit for an app.

- packageName: Package name of the app.

func (*EditsService) Validate ¶
func (r *EditsService) Validate(packageName string, editId string) *EditsValidateCall

Validate: Validates an app edit.

- editId: Identifier of the edit. - packageName: Package name of the app.

type EditsTestersGetCall ¶
type EditsTestersGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsTestersGetCall) Context ¶
func (c *EditsTestersGetCall) Context(ctx context.Context) *EditsTestersGetCall

Context sets the context to be used in this call's Do method.

func (*EditsTestersGetCall) Do ¶
func (c *EditsTestersGetCall) Do(opts ...googleapi.CallOption) (*Testers, error)

Do executes the "androidpublisher.edits.testers.get" call. Any non-2xx status code is an error. Response headers are in either *Testers.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTestersGetCall) Fields ¶
func (c *EditsTestersGetCall) Fields(s ...googleapi.Field) *EditsTestersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTestersGetCall) Header ¶
func (c *EditsTestersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsTestersGetCall) IfNoneMatch ¶
func (c *EditsTestersGetCall) IfNoneMatch(entityTag string) *EditsTestersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsTestersPatchCall ¶
type EditsTestersPatchCall struct {
	// contains filtered or unexported fields
}
func (*EditsTestersPatchCall) Context ¶
func (c *EditsTestersPatchCall) Context(ctx context.Context) *EditsTestersPatchCall

Context sets the context to be used in this call's Do method.

func (*EditsTestersPatchCall) Do ¶
func (c *EditsTestersPatchCall) Do(opts ...googleapi.CallOption) (*Testers, error)

Do executes the "androidpublisher.edits.testers.patch" call. Any non-2xx status code is an error. Response headers are in either *Testers.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTestersPatchCall) Fields ¶
func (c *EditsTestersPatchCall) Fields(s ...googleapi.Field) *EditsTestersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTestersPatchCall) Header ¶
func (c *EditsTestersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsTestersService ¶
type EditsTestersService struct {
	// contains filtered or unexported fields
}
func NewEditsTestersService ¶
func NewEditsTestersService(s *Service) *EditsTestersService
func (*EditsTestersService) Get ¶
func (r *EditsTestersService) Get(packageName string, editId string, track string) *EditsTestersGetCall

Get: Gets testers. Note: Testers resource does not support email lists.

- editId: Identifier of the edit. - packageName: Package name of the app. - track: The track to read from.

func (*EditsTestersService) Patch ¶
func (r *EditsTestersService) Patch(packageName string, editId string, track string, testers *Testers) *EditsTestersPatchCall

Patch: Patches testers. Note: Testers resource does not support email lists.

- editId: Identifier of the edit. - packageName: Package name of the app. - track: The track to update.

func (*EditsTestersService) Update ¶
func (r *EditsTestersService) Update(packageName string, editId string, track string, testers *Testers) *EditsTestersUpdateCall

Update: Updates testers. Note: Testers resource does not support email lists.

- editId: Identifier of the edit. - packageName: Package name of the app. - track: The track to update.

type EditsTestersUpdateCall ¶
type EditsTestersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EditsTestersUpdateCall) Context ¶
func (c *EditsTestersUpdateCall) Context(ctx context.Context) *EditsTestersUpdateCall

Context sets the context to be used in this call's Do method.

func (*EditsTestersUpdateCall) Do ¶
func (c *EditsTestersUpdateCall) Do(opts ...googleapi.CallOption) (*Testers, error)

Do executes the "androidpublisher.edits.testers.update" call. Any non-2xx status code is an error. Response headers are in either *Testers.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTestersUpdateCall) Fields ¶
func (c *EditsTestersUpdateCall) Fields(s ...googleapi.Field) *EditsTestersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTestersUpdateCall) Header ¶
func (c *EditsTestersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsTracksCreateCall ¶
added in v0.151.0
type EditsTracksCreateCall struct {
	// contains filtered or unexported fields
}
func (*EditsTracksCreateCall) Context ¶
added in v0.151.0
func (c *EditsTracksCreateCall) Context(ctx context.Context) *EditsTracksCreateCall

Context sets the context to be used in this call's Do method.

func (*EditsTracksCreateCall) Do ¶
added in v0.151.0
func (c *EditsTracksCreateCall) Do(opts ...googleapi.CallOption) (*Track, error)

Do executes the "androidpublisher.edits.tracks.create" call. Any non-2xx status code is an error. Response headers are in either *Track.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTracksCreateCall) Fields ¶
added in v0.151.0
func (c *EditsTracksCreateCall) Fields(s ...googleapi.Field) *EditsTracksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTracksCreateCall) Header ¶
added in v0.151.0
func (c *EditsTracksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsTracksGetCall ¶
type EditsTracksGetCall struct {
	// contains filtered or unexported fields
}
func (*EditsTracksGetCall) Context ¶
func (c *EditsTracksGetCall) Context(ctx context.Context) *EditsTracksGetCall

Context sets the context to be used in this call's Do method.

func (*EditsTracksGetCall) Do ¶
func (c *EditsTracksGetCall) Do(opts ...googleapi.CallOption) (*Track, error)

Do executes the "androidpublisher.edits.tracks.get" call. Any non-2xx status code is an error. Response headers are in either *Track.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTracksGetCall) Fields ¶
func (c *EditsTracksGetCall) Fields(s ...googleapi.Field) *EditsTracksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTracksGetCall) Header ¶
func (c *EditsTracksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsTracksGetCall) IfNoneMatch ¶
func (c *EditsTracksGetCall) IfNoneMatch(entityTag string) *EditsTracksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsTracksListCall ¶
type EditsTracksListCall struct {
	// contains filtered or unexported fields
}
func (*EditsTracksListCall) Context ¶
func (c *EditsTracksListCall) Context(ctx context.Context) *EditsTracksListCall

Context sets the context to be used in this call's Do method.

func (*EditsTracksListCall) Do ¶
func (c *EditsTracksListCall) Do(opts ...googleapi.CallOption) (*TracksListResponse, error)

Do executes the "androidpublisher.edits.tracks.list" call. Any non-2xx status code is an error. Response headers are in either *TracksListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTracksListCall) Fields ¶
func (c *EditsTracksListCall) Fields(s ...googleapi.Field) *EditsTracksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTracksListCall) Header ¶
func (c *EditsTracksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*EditsTracksListCall) IfNoneMatch ¶
func (c *EditsTracksListCall) IfNoneMatch(entityTag string) *EditsTracksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type EditsTracksPatchCall ¶
type EditsTracksPatchCall struct {
	// contains filtered or unexported fields
}
func (*EditsTracksPatchCall) Context ¶
func (c *EditsTracksPatchCall) Context(ctx context.Context) *EditsTracksPatchCall

Context sets the context to be used in this call's Do method.

func (*EditsTracksPatchCall) Do ¶
func (c *EditsTracksPatchCall) Do(opts ...googleapi.CallOption) (*Track, error)

Do executes the "androidpublisher.edits.tracks.patch" call. Any non-2xx status code is an error. Response headers are in either *Track.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTracksPatchCall) Fields ¶
func (c *EditsTracksPatchCall) Fields(s ...googleapi.Field) *EditsTracksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTracksPatchCall) Header ¶
func (c *EditsTracksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsTracksService ¶
type EditsTracksService struct {
	// contains filtered or unexported fields
}
func NewEditsTracksService ¶
func NewEditsTracksService(s *Service) *EditsTracksService
func (*EditsTracksService) Create ¶
added in v0.151.0
func (r *EditsTracksService) Create(packageName string, editId string, trackconfig *TrackConfig) *EditsTracksCreateCall

Create: Creates a new track.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsTracksService) Get ¶
func (r *EditsTracksService) Get(packageName string, editId string, track string) *EditsTracksGetCall

Get: Gets a track.

editId: Identifier of the edit.
packageName: Package name of the app.
track: Identifier of the track. More on track name (https://developers.google.com/android-publisher/tracks#ff-track-name).
func (*EditsTracksService) List ¶
func (r *EditsTracksService) List(packageName string, editId string) *EditsTracksListCall

List: Lists all tracks.

- editId: Identifier of the edit. - packageName: Package name of the app.

func (*EditsTracksService) Patch ¶
func (r *EditsTracksService) Patch(packageName string, editId string, track string, track2 *Track) *EditsTracksPatchCall

Patch: Patches a track.

editId: Identifier of the edit.
packageName: Package name of the app.
track: Identifier of the track. More on track name (https://developers.google.com/android-publisher/tracks#ff-track-name).
func (*EditsTracksService) Update ¶
func (r *EditsTracksService) Update(packageName string, editId string, track string, track2 *Track) *EditsTracksUpdateCall

Update: Updates a track.

editId: Identifier of the edit.
packageName: Package name of the app.
track: Identifier of the track. More on track name (https://developers.google.com/android-publisher/tracks#ff-track-name).
type EditsTracksUpdateCall ¶
type EditsTracksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*EditsTracksUpdateCall) Context ¶
func (c *EditsTracksUpdateCall) Context(ctx context.Context) *EditsTracksUpdateCall

Context sets the context to be used in this call's Do method.

func (*EditsTracksUpdateCall) Do ¶
func (c *EditsTracksUpdateCall) Do(opts ...googleapi.CallOption) (*Track, error)

Do executes the "androidpublisher.edits.tracks.update" call. Any non-2xx status code is an error. Response headers are in either *Track.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsTracksUpdateCall) Fields ¶
func (c *EditsTracksUpdateCall) Fields(s ...googleapi.Field) *EditsTracksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsTracksUpdateCall) Header ¶
func (c *EditsTracksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type EditsValidateCall ¶
type EditsValidateCall struct {
	// contains filtered or unexported fields
}
func (*EditsValidateCall) Context ¶
func (c *EditsValidateCall) Context(ctx context.Context) *EditsValidateCall

Context sets the context to be used in this call's Do method.

func (*EditsValidateCall) Do ¶
func (c *EditsValidateCall) Do(opts ...googleapi.CallOption) (*AppEdit, error)

Do executes the "androidpublisher.edits.validate" call. Any non-2xx status code is an error. Response headers are in either *AppEdit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*EditsValidateCall) Fields ¶
func (c *EditsValidateCall) Fields(s ...googleapi.Field) *EditsValidateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*EditsValidateCall) Header ¶
func (c *EditsValidateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ExpansionFile ¶
type ExpansionFile struct {
	// FileSize: If set, this field indicates that this APK has an expansion file
	// uploaded to it: this APK does not reference another APK's expansion file.
	// The field's value is the size of the uploaded expansion file in bytes.
	FileSize int64 `json:"fileSize,omitempty,string"`
	// ReferencesVersion: If set, this APK's expansion file references another
	// APK's expansion file. The file_size field will not be set.
	ReferencesVersion int64 `json:"referencesVersion,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FileSize") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FileSize") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExpansionFile: An expansion file. The resource for ExpansionFilesService.

func (ExpansionFile) MarshalJSON ¶
func (s ExpansionFile) MarshalJSON() ([]byte, error)
type ExpansionFilesUploadResponse ¶
type ExpansionFilesUploadResponse struct {
	// ExpansionFile: The uploaded expansion file configuration.
	ExpansionFile *ExpansionFile `json:"expansionFile,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExpansionFile") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpansionFile") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExpansionFilesUploadResponse: Response for uploading an expansion file.

func (ExpansionFilesUploadResponse) MarshalJSON ¶
func (s ExpansionFilesUploadResponse) MarshalJSON() ([]byte, error)
type ExternalAccountIdentifiers ¶
added in v0.80.0
type ExternalAccountIdentifiers struct {
	// ExternalAccountId: User account identifier in the third-party service. Only
	// present if account linking happened as part of the subscription purchase
	// flow.
	ExternalAccountId string `json:"externalAccountId,omitempty"`
	// ObfuscatedExternalAccountId: An obfuscated version of the id that is
	// uniquely associated with the user's account in your app. Present for the
	// following purchases: * If account linking happened as part of the
	// subscription purchase flow. * It was specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid
	// when the purchase was made.
	ObfuscatedExternalAccountId string `json:"obfuscatedExternalAccountId,omitempty"`
	// ObfuscatedExternalProfileId: An obfuscated version of the id that is
	// uniquely associated with the user's profile in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid
	// when the purchase was made.
	ObfuscatedExternalProfileId string `json:"obfuscatedExternalProfileId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalAccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalAccountId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExternalAccountIdentifiers: User account identifier in the third-party service.

func (ExternalAccountIdentifiers) MarshalJSON ¶
added in v0.80.0
func (s ExternalAccountIdentifiers) MarshalJSON() ([]byte, error)
type ExternalAccountIds ¶
added in v0.257.0
type ExternalAccountIds struct {
	// ObfuscatedAccountId: Optional. Specifies an optional obfuscated string that
	// is uniquely associated with the purchaser's user account in your app. If you
	// pass this value, Google Play can use it to detect irregular activity. Do not
	// use this field to store any Personally Identifiable Information (PII) such
	// as emails in cleartext. Attempting to store PII in this field will result in
	// purchases being blocked. Google Play recommends that you use either
	// encryption or a one-way hash to generate an obfuscated identifier to send to
	// Google Play. This identifier is limited to 64 characters. This field can
	// only be set for resubscription purchases. See
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid
	// to set this field for purchases made using the standard in-app billing flow.
	ObfuscatedAccountId string `json:"obfuscatedAccountId,omitempty"`
	// ObfuscatedProfileId: Optional. Specifies an optional obfuscated string that
	// is uniquely associated with the purchaser's user profile in your app. If you
	// pass this value, Google Play can use it to detect irregular activity. Do not
	// use this field to store any Personally Identifiable Information (PII) such
	// as emails in cleartext. Attempting to store PII in this field will result in
	// purchases being blocked. Google Play recommends that you use either
	// encryption or a one-way hash to generate an obfuscated identifier to send to
	// Google Play. This identifier is limited to 64 characters. This field can
	// only be set for resubscription purchases. See
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid
	// to set this field for purchases made using the standard in-app billing flow.
	ObfuscatedProfileId string `json:"obfuscatedProfileId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ObfuscatedAccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ObfuscatedAccountId") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExternalAccountIds: User account identifier in your app.

func (ExternalAccountIds) MarshalJSON ¶
added in v0.257.0
func (s ExternalAccountIds) MarshalJSON() ([]byte, error)
type ExternalOfferDetails ¶
added in v0.258.0
type ExternalOfferDetails struct {
	// AppDownloadEventExternalTransactionId: Optional. The external transaction id
	// associated with the app download event through an external link. Required
	// when reporting transactions made in externally installed apps.
	AppDownloadEventExternalTransactionId string `json:"appDownloadEventExternalTransactionId,omitempty"`
	// InstalledAppCategory: Optional. The category of the downloaded app though
	// this transaction. This must match the category provided in Play Console
	// during the external app verification process. Only required for app
	// downloads.
	//
	// Possible values:
	//   "EXTERNAL_OFFER_APP_CATEGORY_UNSPECIFIED" - Unspecified, do not use.
	//   "APP" - The app is classified under the app category.
	//   "GAME" - The app is classified under the game category.
	InstalledAppCategory string `json:"installedAppCategory,omitempty"`
	// InstalledAppPackage: Optional. The package name of the app downloaded
	// through this transaction. Required when link_type is LINK_TO_APP_DOWNLOAD.
	InstalledAppPackage string `json:"installedAppPackage,omitempty"`
	// LinkType: Optional. The type of content being reported by this transaction.
	// Required when reporting app downloads or purchased digital content offers
	// made in app installed through Google Play.
	//
	// Possible values:
	//   "EXTERNAL_OFFER_LINK_TYPE_UNSPECIFIED" - Unspecified, do not use.
	//   "LINK_TO_DIGITAL_CONTENT_OFFER" - An offer to purchase digital content.
	//   "LINK_TO_APP_DOWNLOAD" - An app install.
	LinkType string `json:"linkType,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AppDownloadEventExternalTransactionId") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AppDownloadEventExternalTransactionId") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

ExternalOfferDetails: Reporting details unique to the external offers program.

func (ExternalOfferDetails) MarshalJSON ¶
added in v0.258.0
func (s ExternalOfferDetails) MarshalJSON() ([]byte, error)
type ExternalSubscription ¶
added in v0.117.0
type ExternalSubscription struct {
	// SubscriptionType: Required. The type of the external subscription.
	//
	// Possible values:
	//   "SUBSCRIPTION_TYPE_UNSPECIFIED" - Unspecified, do not use.
	//   "RECURRING" - This is a recurring subscription where the user is charged
	// every billing cycle.
	//   "PREPAID" - This is a prepaid subscription where the user pays up front.
	SubscriptionType string `json:"subscriptionType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SubscriptionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SubscriptionType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExternalSubscription: Details of an external subscription.

func (ExternalSubscription) MarshalJSON ¶
added in v0.117.0
func (s ExternalSubscription) MarshalJSON() ([]byte, error)
type ExternalTransaction ¶
added in v0.117.0
type ExternalTransaction struct {
	// CreateTime: Output only. The time when this transaction was created. This is
	// the time when Google was notified of the transaction.
	CreateTime string `json:"createTime,omitempty"`
	// CurrentPreTaxAmount: Output only. The current transaction amount before tax.
	// This represents the current pre-tax amount including any refunds that may
	// have been applied to this transaction.
	CurrentPreTaxAmount *Price `json:"currentPreTaxAmount,omitempty"`
	// CurrentTaxAmount: Output only. The current tax amount. This represents the
	// current tax amount including any refunds that may have been applied to this
	// transaction.
	CurrentTaxAmount *Price `json:"currentTaxAmount,omitempty"`
	// ExternalOfferDetails: Optional. Details necessary to accurately report
	// external offers transactions.
	ExternalOfferDetails *ExternalOfferDetails `json:"externalOfferDetails,omitempty"`
	// ExternalTransactionId: Output only. The id of this transaction. All
	// transaction ids under the same package name must be unique. Set when
	// creating the external transaction.
	ExternalTransactionId string `json:"externalTransactionId,omitempty"`
	// OneTimeTransaction: This is a one-time transaction and not part of a
	// subscription.
	OneTimeTransaction *OneTimeExternalTransaction `json:"oneTimeTransaction,omitempty"`
	// OriginalPreTaxAmount: Required. The original transaction amount before
	// taxes. This represents the pre-tax amount originally notified to Google
	// before any refunds were applied.
	OriginalPreTaxAmount *Price `json:"originalPreTaxAmount,omitempty"`
	// OriginalTaxAmount: Required. The original tax amount. This represents the
	// tax amount originally notified to Google before any refunds were applied.
	OriginalTaxAmount *Price `json:"originalTaxAmount,omitempty"`
	// PackageName: Output only. The resource name of the external transaction. The
	// package name of the application the inapp products were sold (for example,
	// 'com.some.app').
	PackageName string `json:"packageName,omitempty"`
	// RecurringTransaction: This transaction is part of a recurring series of
	// transactions.
	RecurringTransaction *RecurringExternalTransaction `json:"recurringTransaction,omitempty"`
	// TestPurchase: Output only. If set, this transaction was a test purchase.
	// Google will not charge for a test transaction.
	TestPurchase *ExternalTransactionTestPurchase `json:"testPurchase,omitempty"`
	// TransactionProgramCode: Optional. The transaction program code, used to help
	// determine service fee for eligible apps participating in partner programs.
	// Developers participating in the Play Media Experience Program
	// (https://play.google.com/console/about/programs/mediaprogram/) must provide
	// the program code when reporting alternative billing transactions. If you are
	// an eligible developer, please contact your BDM for more information on how
	// to set this field. Note: this field can not be used for external offers
	// transactions.
	TransactionProgramCode int64 `json:"transactionProgramCode,omitempty"`
	// TransactionState: Output only. The current state of the transaction.
	//
	// Possible values:
	//   "TRANSACTION_STATE_UNSPECIFIED" - Unspecified transaction state. Not used.
	//   "TRANSACTION_REPORTED" - The transaction has been successfully reported to
	// Google.
	//   "TRANSACTION_CANCELED" - The transaction has been fully refunded.
	TransactionState string `json:"transactionState,omitempty"`
	// TransactionTime: Required. The time when the transaction was completed.
	TransactionTime string `json:"transactionTime,omitempty"`
	// UserTaxAddress: Required. User address for tax computation.
	UserTaxAddress *ExternalTransactionAddress `json:"userTaxAddress,omitempty"`

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

ExternalTransaction: The details of an external transaction.

func (ExternalTransaction) MarshalJSON ¶
added in v0.117.0
func (s ExternalTransaction) MarshalJSON() ([]byte, error)
type ExternalTransactionAddress ¶
added in v0.117.0
type ExternalTransactionAddress struct {
	// AdministrativeArea: Optional. Top-level administrative subdivision of the
	// country/region. Only required for transactions in India. Valid values are
	// "ANDAMAN AND NICOBAR ISLANDS", "ANDHRA PRADESH", "ARUNACHAL PRADESH",
	// "ASSAM", "BIHAR", "CHANDIGARH", "CHHATTISGARH", "DADRA AND NAGAR HAVELI",
	// "DADRA AND NAGAR HAVELI AND DAMAN AND DIU", "DAMAN AND DIU", "DELHI", "GOA",
	// "GUJARAT", "HARYANA", "HIMACHAL PRADESH", "JAMMU AND KASHMIR", "JHARKHAND",
	// "KARNATAKA", "KERALA", "LADAKH", "LAKSHADWEEP", "MADHYA PRADESH",
	// "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA",
	// "PUDUCHERRY", "PUNJAB", "RAJASTHAN", "SIKKIM", "TAMIL NADU", "TELANGANA",
	// "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", and "WEST BENGAL".
	AdministrativeArea string `json:"administrativeArea,omitempty"`
	// RegionCode: Required. Two letter region code based on ISO-3166-1 Alpha-2 (UN
	// region codes).
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdministrativeArea") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdministrativeArea") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExternalTransactionAddress: User's address for the external transaction.

func (ExternalTransactionAddress) MarshalJSON ¶
added in v0.117.0
func (s ExternalTransactionAddress) MarshalJSON() ([]byte, error)
type ExternalTransactionTestPurchase ¶
added in v0.117.0
type ExternalTransactionTestPurchase struct {
}

ExternalTransactionTestPurchase: Represents a transaction performed using a test account. These transactions will not be charged by Google.

type ExternallyHostedApk ¶
type ExternallyHostedApk struct {
	// ApplicationLabel: The application label.
	ApplicationLabel string `json:"applicationLabel,omitempty"`
	// CertificateBase64s: A certificate (or array of certificates if a
	// certificate-chain is used) used to sign this APK, represented as a base64
	// encoded byte array.
	CertificateBase64s []string `json:"certificateBase64s,omitempty"`
	// ExternallyHostedUrl: The URL at which the APK is hosted. This must be an
	// https URL.
	ExternallyHostedUrl string `json:"externallyHostedUrl,omitempty"`
	// FileSha1Base64: The sha1 checksum of this APK, represented as a base64
	// encoded byte array.
	FileSha1Base64 string `json:"fileSha1Base64,omitempty"`
	// FileSha256Base64: The sha256 checksum of this APK, represented as a base64
	// encoded byte array.
	FileSha256Base64 string `json:"fileSha256Base64,omitempty"`
	// FileSize: The file size in bytes of this APK.
	FileSize int64 `json:"fileSize,omitempty,string"`
	// IconBase64: The icon image from the APK, as a base64 encoded byte array.
	IconBase64 string `json:"iconBase64,omitempty"`
	// MaximumSdk: The maximum SDK supported by this APK (optional).
	MaximumSdk int64 `json:"maximumSdk,omitempty"`
	// MinimumSdk: The minimum SDK targeted by this APK.
	MinimumSdk int64 `json:"minimumSdk,omitempty"`
	// NativeCodes: The native code environments supported by this APK (optional).
	NativeCodes []string `json:"nativeCodes,omitempty"`
	// PackageName: The package name.
	PackageName string `json:"packageName,omitempty"`
	// UsesFeatures: The features required by this APK (optional).
	UsesFeatures []string `json:"usesFeatures,omitempty"`
	// UsesPermissions: The permissions requested by this APK.
	UsesPermissions []*UsesPermission `json:"usesPermissions,omitempty"`
	// VersionCode: The version code of this APK.
	VersionCode int64 `json:"versionCode,omitempty"`
	// VersionName: The version name of this APK.
	VersionName string `json:"versionName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicationLabel") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicationLabel") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExternallyHostedApk: Defines an APK available for this application that is hosted externally and not uploaded to Google Play. This function is only available to organizations using Managed Play whose application is configured to restrict distribution to the organizations.

func (ExternallyHostedApk) MarshalJSON ¶
func (s ExternallyHostedApk) MarshalJSON() ([]byte, error)
type ExternaltransactionsCreateexternaltransactionCall ¶
added in v0.117.0
type ExternaltransactionsCreateexternaltransactionCall struct {
	// contains filtered or unexported fields
}
func (*ExternaltransactionsCreateexternaltransactionCall) Context ¶
added in v0.117.0
func (c *ExternaltransactionsCreateexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsCreateexternaltransactionCall

Context sets the context to be used in this call's Do method.

func (*ExternaltransactionsCreateexternaltransactionCall) Do ¶
added in v0.117.0
func (c *ExternaltransactionsCreateexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)

Do executes the "androidpublisher.externaltransactions.createexternaltransaction" call. Any non-2xx status code is an error. Response headers are in either *ExternalTransaction.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ExternaltransactionsCreateexternaltransactionCall) ExternalTransactionId ¶
added in v0.117.0
func (c *ExternaltransactionsCreateexternaltransactionCall) ExternalTransactionId(externalTransactionId string) *ExternaltransactionsCreateexternaltransactionCall

ExternalTransactionId sets the optional parameter "externalTransactionId": Required. The id to use for the external transaction. Must be unique across all other transactions for the app. This value should be 1-63 characters and valid characters are /a-zA-Z0-9_-/. Do not use this field to store any Personally Identifiable Information (PII) such as emails. Attempting to store PII in this field may result in requests being blocked.

func (*ExternaltransactionsCreateexternaltransactionCall) Fields ¶
added in v0.117.0
func (c *ExternaltransactionsCreateexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsCreateexternaltransactionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ExternaltransactionsCreateexternaltransactionCall) Header ¶
added in v0.117.0
func (c *ExternaltransactionsCreateexternaltransactionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ExternaltransactionsGetexternaltransactionCall ¶
added in v0.117.0
type ExternaltransactionsGetexternaltransactionCall struct {
	// contains filtered or unexported fields
}
func (*ExternaltransactionsGetexternaltransactionCall) Context ¶
added in v0.117.0
func (c *ExternaltransactionsGetexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsGetexternaltransactionCall

Context sets the context to be used in this call's Do method.

func (*ExternaltransactionsGetexternaltransactionCall) Do ¶
added in v0.117.0
func (c *ExternaltransactionsGetexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)

Do executes the "androidpublisher.externaltransactions.getexternaltransaction" call. Any non-2xx status code is an error. Response headers are in either *ExternalTransaction.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ExternaltransactionsGetexternaltransactionCall) Fields ¶
added in v0.117.0
func (c *ExternaltransactionsGetexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsGetexternaltransactionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ExternaltransactionsGetexternaltransactionCall) Header ¶
added in v0.117.0
func (c *ExternaltransactionsGetexternaltransactionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ExternaltransactionsGetexternaltransactionCall) IfNoneMatch ¶
added in v0.117.0
func (c *ExternaltransactionsGetexternaltransactionCall) IfNoneMatch(entityTag string) *ExternaltransactionsGetexternaltransactionCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ExternaltransactionsRefundexternaltransactionCall ¶
added in v0.117.0
type ExternaltransactionsRefundexternaltransactionCall struct {
	// contains filtered or unexported fields
}
func (*ExternaltransactionsRefundexternaltransactionCall) Context ¶
added in v0.117.0
func (c *ExternaltransactionsRefundexternaltransactionCall) Context(ctx context.Context) *ExternaltransactionsRefundexternaltransactionCall

Context sets the context to be used in this call's Do method.

func (*ExternaltransactionsRefundexternaltransactionCall) Do ¶
added in v0.117.0
func (c *ExternaltransactionsRefundexternaltransactionCall) Do(opts ...googleapi.CallOption) (*ExternalTransaction, error)

Do executes the "androidpublisher.externaltransactions.refundexternaltransaction" call. Any non-2xx status code is an error. Response headers are in either *ExternalTransaction.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ExternaltransactionsRefundexternaltransactionCall) Fields ¶
added in v0.117.0
func (c *ExternaltransactionsRefundexternaltransactionCall) Fields(s ...googleapi.Field) *ExternaltransactionsRefundexternaltransactionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ExternaltransactionsRefundexternaltransactionCall) Header ¶
added in v0.117.0
func (c *ExternaltransactionsRefundexternaltransactionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ExternaltransactionsService ¶
added in v0.117.0
type ExternaltransactionsService struct {
	// contains filtered or unexported fields
}
func NewExternaltransactionsService ¶
added in v0.117.0
func NewExternaltransactionsService(s *Service) *ExternaltransactionsService
func (*ExternaltransactionsService) Createexternaltransaction ¶
added in v0.117.0
func (r *ExternaltransactionsService) Createexternaltransaction(parent string, externaltransaction *ExternalTransaction) *ExternaltransactionsCreateexternaltransactionCall

Createexternaltransaction: Creates a new external transaction.

parent: The parent resource where this external transaction will be created. Format: applications/{package_name}.
func (*ExternaltransactionsService) Getexternaltransaction ¶
added in v0.117.0
func (r *ExternaltransactionsService) Getexternaltransaction(name string) *ExternaltransactionsGetexternaltransactionCall

Getexternaltransaction: Gets an existing external transaction.

name: The name of the external transaction to retrieve. Format: applications/{package_name}/externalTransactions/{external_transaction}.
func (*ExternaltransactionsService) Refundexternaltransaction ¶
added in v0.117.0
func (r *ExternaltransactionsService) Refundexternaltransaction(name string, refundexternaltransactionrequest *RefundExternalTransactionRequest) *ExternaltransactionsRefundexternaltransactionCall

Refundexternaltransaction: Refunds or partially refunds an existing external transaction.

name: The name of the external transaction that will be refunded. Format: applications/{package_name}/externalTransactions/{external_transaction}.
type FreeTrialDetails ¶
added in v0.257.0
type FreeTrialDetails struct {
}

FreeTrialDetails: Details of a free trial pricing phase.

type FreeTrialOfferPhase ¶
added in v0.265.0
type FreeTrialOfferPhase struct {
}

FreeTrialOfferPhase: Details about free trial offer phase.

type FullRefund ¶
added in v0.117.0
type FullRefund struct {
}

FullRefund: A full refund of the remaining amount of a transaction.

type GeneratedApksListResponse ¶
added in v0.61.0
type GeneratedApksListResponse struct {
	// GeneratedApks: All generated APKs, grouped by the APK signing key.
	GeneratedApks []*GeneratedApksPerSigningKey `json:"generatedApks,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GeneratedApks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GeneratedApks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedApksListResponse: Response to list generated APKs.

func (GeneratedApksListResponse) MarshalJSON ¶
added in v0.61.0
func (s GeneratedApksListResponse) MarshalJSON() ([]byte, error)
type GeneratedApksPerSigningKey ¶
added in v0.61.0
type GeneratedApksPerSigningKey struct {
	// CertificateSha256Hash: SHA256 hash of the APK signing public key
	// certificate.
	CertificateSha256Hash string `json:"certificateSha256Hash,omitempty"`
	// GeneratedAssetPackSlices: List of asset pack slices which will be served for
	// this app bundle, signed with a key corresponding to certificate_sha256_hash.
	GeneratedAssetPackSlices []*GeneratedAssetPackSlice `json:"generatedAssetPackSlices,omitempty"`
	// GeneratedRecoveryModules: Generated recovery apks for recovery actions
	// signed with a key corresponding to certificate_sha256_hash. This includes
	// all generated recovery APKs, also those in draft or cancelled state. This
	// field is not set if no recovery actions were created for this signing key.
	GeneratedRecoveryModules []*GeneratedRecoveryApk `json:"generatedRecoveryModules,omitempty"`
	// GeneratedSplitApks: List of generated split APKs, signed with a key
	// corresponding to certificate_sha256_hash.
	GeneratedSplitApks []*GeneratedSplitApk `json:"generatedSplitApks,omitempty"`
	// GeneratedStandaloneApks: List of generated standalone APKs, signed with a
	// key corresponding to certificate_sha256_hash.
	GeneratedStandaloneApks []*GeneratedStandaloneApk `json:"generatedStandaloneApks,omitempty"`
	// GeneratedUniversalApk: Generated universal APK, signed with a key
	// corresponding to certificate_sha256_hash. This field is not set if no
	// universal APK was generated for this signing key.
	GeneratedUniversalApk *GeneratedUniversalApk `json:"generatedUniversalApk,omitempty"`
	// TargetingInfo: Contains targeting information about the generated apks.
	TargetingInfo *TargetingInfo `json:"targetingInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CertificateSha256Hash") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CertificateSha256Hash") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedApksPerSigningKey: Download metadata for split, standalone and universal APKs, as well as asset pack slices, signed with a given key.

func (GeneratedApksPerSigningKey) MarshalJSON ¶
added in v0.61.0
func (s GeneratedApksPerSigningKey) MarshalJSON() ([]byte, error)
type GeneratedAssetPackSlice ¶
added in v0.61.0
type GeneratedAssetPackSlice struct {
	// DownloadId: Download ID, which uniquely identifies the APK to download.
	// Should be supplied to `generatedapks.download` method.
	DownloadId string `json:"downloadId,omitempty"`
	// ModuleName: Name of the module that this asset slice belongs to.
	ModuleName string `json:"moduleName,omitempty"`
	// SliceId: Asset slice ID.
	SliceId string `json:"sliceId,omitempty"`
	// Version: Asset module version.
	Version int64 `json:"version,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "DownloadId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DownloadId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedAssetPackSlice: Download metadata for an asset pack slice.

func (GeneratedAssetPackSlice) MarshalJSON ¶
added in v0.61.0
func (s GeneratedAssetPackSlice) MarshalJSON() ([]byte, error)
type GeneratedRecoveryApk ¶
added in v0.156.0
type GeneratedRecoveryApk struct {
	// DownloadId: Download ID, which uniquely identifies the APK to download.
	// Should be supplied to `generatedapks.download` method.
	DownloadId string `json:"downloadId,omitempty"`
	// ModuleName: Name of the module which recovery apk belongs to.
	ModuleName string `json:"moduleName,omitempty"`
	// RecoveryId: ID of the recovery action.
	RecoveryId int64 `json:"recoveryId,omitempty,string"`
	// RecoveryStatus: The status of the recovery action corresponding to the
	// recovery apk.
	//
	// Possible values:
	//   "RECOVERY_STATUS_UNSPECIFIED" - RecoveryStatus is unspecified.
	//   "RECOVERY_STATUS_ACTIVE" - The app recovery action has not been canceled
	// since it has been created.
	//   "RECOVERY_STATUS_CANCELED" - The recovery action has been canceled. The
	// action cannot be resumed.
	//   "RECOVERY_STATUS_DRAFT" - The recovery action is in the draft state and
	// has not yet been deployed to users.
	//   "RECOVERY_STATUS_GENERATION_IN_PROGRESS" - The recovery action is
	// generating recovery apks.
	//   "RECOVERY_STATUS_GENERATION_FAILED" - The app recovery action generation
	// has failed.
	RecoveryStatus string `json:"recoveryStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DownloadId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DownloadId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedRecoveryApk: Download metadata for an app recovery module.

func (GeneratedRecoveryApk) MarshalJSON ¶
added in v0.156.0
func (s GeneratedRecoveryApk) MarshalJSON() ([]byte, error)
type GeneratedSplitApk ¶
added in v0.61.0
type GeneratedSplitApk struct {
	// DownloadId: Download ID, which uniquely identifies the APK to download.
	// Should be supplied to `generatedapks.download` method.
	DownloadId string `json:"downloadId,omitempty"`
	// ModuleName: Name of the module that this APK belongs to.
	ModuleName string `json:"moduleName,omitempty"`
	// SplitId: Split ID. Empty for the main split of the base module.
	SplitId string `json:"splitId,omitempty"`
	// VariantId: ID of the generated variant.
	VariantId int64 `json:"variantId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DownloadId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DownloadId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedSplitApk: Download metadata for a split APK.

func (GeneratedSplitApk) MarshalJSON ¶
added in v0.61.0
func (s GeneratedSplitApk) MarshalJSON() ([]byte, error)
type GeneratedStandaloneApk ¶
added in v0.61.0
type GeneratedStandaloneApk struct {
	// DownloadId: Download ID, which uniquely identifies the APK to download.
	// Should be supplied to `generatedapks.download` method.
	DownloadId string `json:"downloadId,omitempty"`
	// VariantId: ID of the generated variant.
	VariantId int64 `json:"variantId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DownloadId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DownloadId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedStandaloneApk: Download metadata for a standalone APK.

func (GeneratedStandaloneApk) MarshalJSON ¶
added in v0.61.0
func (s GeneratedStandaloneApk) MarshalJSON() ([]byte, error)
type GeneratedUniversalApk ¶
added in v0.61.0
type GeneratedUniversalApk struct {
	// DownloadId: Download ID, which uniquely identifies the APK to download.
	// Should be supplied to `generatedapks.download` method.
	DownloadId string `json:"downloadId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DownloadId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DownloadId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GeneratedUniversalApk: Download metadata for a universal APK.

func (GeneratedUniversalApk) MarshalJSON ¶
added in v0.61.0
func (s GeneratedUniversalApk) MarshalJSON() ([]byte, error)
type GeneratedapksDownloadCall ¶
added in v0.61.0
type GeneratedapksDownloadCall struct {
	// contains filtered or unexported fields
}
func (*GeneratedapksDownloadCall) Context ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) Context(ctx context.Context) *GeneratedapksDownloadCall

Context sets the context to be used in this call's Do and Download methods.

func (*GeneratedapksDownloadCall) Do ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.generatedapks.download" call.

func (*GeneratedapksDownloadCall) Download ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

func (*GeneratedapksDownloadCall) Fields ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) Fields(s ...googleapi.Field) *GeneratedapksDownloadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GeneratedapksDownloadCall) Header ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GeneratedapksDownloadCall) IfNoneMatch ¶
added in v0.61.0
func (c *GeneratedapksDownloadCall) IfNoneMatch(entityTag string) *GeneratedapksDownloadCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GeneratedapksListCall ¶
added in v0.61.0
type GeneratedapksListCall struct {
	// contains filtered or unexported fields
}
func (*GeneratedapksListCall) Context ¶
added in v0.61.0
func (c *GeneratedapksListCall) Context(ctx context.Context) *GeneratedapksListCall

Context sets the context to be used in this call's Do method.

func (*GeneratedapksListCall) Do ¶
added in v0.61.0
func (c *GeneratedapksListCall) Do(opts ...googleapi.CallOption) (*GeneratedApksListResponse, error)

Do executes the "androidpublisher.generatedapks.list" call. Any non-2xx status code is an error. Response headers are in either *GeneratedApksListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GeneratedapksListCall) Fields ¶
added in v0.61.0
func (c *GeneratedapksListCall) Fields(s ...googleapi.Field) *GeneratedapksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GeneratedapksListCall) Header ¶
added in v0.61.0
func (c *GeneratedapksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GeneratedapksListCall) IfNoneMatch ¶
added in v0.61.0
func (c *GeneratedapksListCall) IfNoneMatch(entityTag string) *GeneratedapksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type GeneratedapksService ¶
added in v0.61.0
type GeneratedapksService struct {
	// contains filtered or unexported fields
}
func NewGeneratedapksService ¶
added in v0.61.0
func NewGeneratedapksService(s *Service) *GeneratedapksService
func (*GeneratedapksService) Download ¶
added in v0.61.0
func (r *GeneratedapksService) Download(packageName string, versionCode int64, downloadId string) *GeneratedapksDownloadCall

Download: Downloads a single signed APK generated from an app bundle.

downloadId: Download ID, which uniquely identifies the APK to download. Can be obtained from the response of `generatedapks.list` method.
packageName: Package name of the app.
versionCode: Version code of the app bundle.
func (*GeneratedapksService) List ¶
added in v0.61.0
func (r *GeneratedapksService) List(packageName string, versionCode int64) *GeneratedapksListCall

List: Returns download metadata for all APKs that were generated from a given app bundle.

- packageName: Package name of the app. - versionCode: Version code of the app bundle.

type GetOneTimeProductOfferRequest ¶
added in v0.244.0
type GetOneTimeProductOfferRequest struct {
	// OfferId: Required. The unique offer ID of the offer to get.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to get.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent one-time product (ID) of the offer to get.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. The parent purchase option (ID) of the offer to
	// get.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OfferId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OfferId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GetOneTimeProductOfferRequest: Request message for GetOneTimeProductOffers.

func (GetOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s GetOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type GetSubscriptionOfferRequest ¶
added in v0.154.0
type GetSubscriptionOfferRequest struct {
	// BasePlanId: Required. The parent base plan (ID) of the offer to get.
	BasePlanId string `json:"basePlanId,omitempty"`
	// OfferId: Required. The unique offer ID of the offer to get.
	OfferId string `json:"offerId,omitempty"`
	// PackageName: Required. The parent app (package name) of the offer to get.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The parent subscription (ID) of the offer to get.
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GetSubscriptionOfferRequest: Request message for GetSubscriptionOffer.

func (GetSubscriptionOfferRequest) MarshalJSON ¶
added in v0.154.0
func (s GetSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type Grant ¶
added in v0.59.0
type Grant struct {
	// AppLevelPermissions: The permissions granted to the user for this app.
	//
	// Possible values:
	//   "APP_LEVEL_PERMISSION_UNSPECIFIED" - Unknown or unspecified permission.
	//   "CAN_ACCESS_APP" - View app information (read-only). Deprecated: Try
	// defining a more granular capability. Otherwise, check
	// AppLevelPermission.CAN_VIEW_NON_FINANCIAL_DATA.
	//   "CAN_VIEW_FINANCIAL_DATA" - View financial data.
	//   "CAN_MANAGE_PERMISSIONS" - Admin (all permissions).
	//   "CAN_REPLY_TO_REVIEWS" - Reply to reviews.
	//   "CAN_MANAGE_PUBLIC_APKS" - Release to production, exclude devices, and use
	// app signing by Google Play.
	//   "CAN_MANAGE_TRACK_APKS" - Release to testing tracks.
	//   "CAN_MANAGE_TRACK_USERS" - Manage testing tracks and edit tester lists.
	//   "CAN_MANAGE_PUBLIC_LISTING" - Manage store presence.
	//   "CAN_MANAGE_DRAFT_APPS" - Edit and delete draft apps.
	//   "CAN_MANAGE_ORDERS" - Manage orders and subscriptions.
	//   "CAN_MANAGE_APP_CONTENT" - Manage policy related pages.
	//   "CAN_VIEW_NON_FINANCIAL_DATA" - View app information (read-only).
	//   "CAN_VIEW_APP_QUALITY" - View app quality data such as Vitals, Crashes
	// etc.
	//   "CAN_MANAGE_DEEPLINKS" - Manage the deep links setup of an app.
	AppLevelPermissions []string `json:"appLevelPermissions,omitempty"`
	// Name: Required. Resource name for this grant, following the pattern
	// "developers/{developer}/users/{email}/grants/{package_name}". If this grant
	// is for a draft app, the app ID will be used in this resource name instead of
	// the package name.
	Name string `json:"name,omitempty"`
	// PackageName: Immutable. The package name of the app. This will be empty for
	// draft apps.
	PackageName string `json:"packageName,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppLevelPermissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppLevelPermissions") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Grant: An access grant resource.

func (Grant) MarshalJSON ¶
added in v0.59.0
func (s Grant) MarshalJSON() ([]byte, error)
type GrantsCreateCall ¶
added in v0.59.0
type GrantsCreateCall struct {
	// contains filtered or unexported fields
}
func (*GrantsCreateCall) Context ¶
added in v0.59.0
func (c *GrantsCreateCall) Context(ctx context.Context) *GrantsCreateCall

Context sets the context to be used in this call's Do method.

func (*GrantsCreateCall) Do ¶
added in v0.59.0
func (c *GrantsCreateCall) Do(opts ...googleapi.CallOption) (*Grant, error)

Do executes the "androidpublisher.grants.create" call. Any non-2xx status code is an error. Response headers are in either *Grant.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GrantsCreateCall) Fields ¶
added in v0.59.0
func (c *GrantsCreateCall) Fields(s ...googleapi.Field) *GrantsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrantsCreateCall) Header ¶
added in v0.59.0
func (c *GrantsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GrantsDeleteCall ¶
added in v0.59.0
type GrantsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*GrantsDeleteCall) Context ¶
added in v0.59.0
func (c *GrantsDeleteCall) Context(ctx context.Context) *GrantsDeleteCall

Context sets the context to be used in this call's Do method.

func (*GrantsDeleteCall) Do ¶
added in v0.59.0
func (c *GrantsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.grants.delete" call.

func (*GrantsDeleteCall) Fields ¶
added in v0.59.0
func (c *GrantsDeleteCall) Fields(s ...googleapi.Field) *GrantsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrantsDeleteCall) Header ¶
added in v0.59.0
func (c *GrantsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type GrantsPatchCall ¶
added in v0.59.0
type GrantsPatchCall struct {
	// contains filtered or unexported fields
}
func (*GrantsPatchCall) Context ¶
added in v0.59.0
func (c *GrantsPatchCall) Context(ctx context.Context) *GrantsPatchCall

Context sets the context to be used in this call's Do method.

func (*GrantsPatchCall) Do ¶
added in v0.59.0
func (c *GrantsPatchCall) Do(opts ...googleapi.CallOption) (*Grant, error)

Do executes the "androidpublisher.grants.patch" call. Any non-2xx status code is an error. Response headers are in either *Grant.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*GrantsPatchCall) Fields ¶
added in v0.59.0
func (c *GrantsPatchCall) Fields(s ...googleapi.Field) *GrantsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*GrantsPatchCall) Header ¶
added in v0.59.0
func (c *GrantsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*GrantsPatchCall) UpdateMask ¶
added in v0.59.0
func (c *GrantsPatchCall) UpdateMask(updateMask string) *GrantsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated.

type GrantsService ¶
added in v0.59.0
type GrantsService struct {
	// contains filtered or unexported fields
}
func NewGrantsService ¶
added in v0.59.0
func NewGrantsService(s *Service) *GrantsService
func (*GrantsService) Create ¶
added in v0.59.0
func (r *GrantsService) Create(parent string, grant *Grant) *GrantsCreateCall

Create: Grant access for a user to the given package.

parent: The user which needs permission. Format: developers/{developer}/users/{user}.
func (*GrantsService) Delete ¶
added in v0.59.0
func (r *GrantsService) Delete(name string) *GrantsDeleteCall

Delete: Removes all access for the user to the given package or developer account.

name: The name of the grant to delete. Format: developers/{developer}/users/{email}/grants/{package_name}.
func (*GrantsService) Patch ¶
added in v0.59.0
func (r *GrantsService) Patch(name string, grant *Grant) *GrantsPatchCall

Patch: Updates access for the user to the given package.

name: Resource name for this grant, following the pattern "developers/{developer}/users/{email}/grants/{package_name}". If this grant is for a draft app, the app ID will be used in this resource name instead of the package name.
type Image ¶
type Image struct {
	// Id: A unique id representing this image.
	Id string `json:"id,omitempty"`
	// Sha1: A sha1 hash of the image.
	Sha1 string `json:"sha1,omitempty"`
	// Sha256: A sha256 hash of the image.
	Sha256 string `json:"sha256,omitempty"`
	// Url: A URL that will serve a preview of the image.
	Url string `json:"url,omitempty"`
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

Image: An uploaded image. The resource for ImagesService.

func (Image) MarshalJSON ¶
func (s Image) MarshalJSON() ([]byte, error)
type ImagesDeleteAllResponse ¶
type ImagesDeleteAllResponse struct {
	// Deleted: The deleted images.
	Deleted []*Image `json:"deleted,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Deleted") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deleted") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImagesDeleteAllResponse: Response for deleting all images.

func (ImagesDeleteAllResponse) MarshalJSON ¶
func (s ImagesDeleteAllResponse) MarshalJSON() ([]byte, error)
type ImagesListResponse ¶
type ImagesListResponse struct {
	// Images: All listed Images.
	Images []*Image `json:"images,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Images") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Images") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImagesListResponse: Response listing all images.

func (ImagesListResponse) MarshalJSON ¶
func (s ImagesListResponse) MarshalJSON() ([]byte, error)
type ImagesUploadResponse ¶
type ImagesUploadResponse struct {
	// Image: The uploaded image.
	Image *Image `json:"image,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Image") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Image") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImagesUploadResponse: Response for uploading an image.

func (ImagesUploadResponse) MarshalJSON ¶
func (s ImagesUploadResponse) MarshalJSON() ([]byte, error)
type InAppProduct ¶
type InAppProduct struct {
	// DefaultLanguage: Default language of the localized data, as defined by
	// BCP-47. e.g. "en-US".
	DefaultLanguage string `json:"defaultLanguage,omitempty"`
	// DefaultPrice: Default price. Cannot be zero, as in-app products are never
	// free. Always in the developer's Checkout merchant currency.
	DefaultPrice *Price `json:"defaultPrice,omitempty"`
	// GracePeriod: Grace period of the subscription, specified in ISO 8601 format.
	// Allows developers to give their subscribers a grace period when the payment
	// for the new recurrence period is declined. Acceptable values are P0D (zero
	// days), P3D (three days), P7D (seven days), P14D (14 days), and P30D (30
	// days).
	GracePeriod string `json:"gracePeriod,omitempty"`
	// Listings: List of localized title and description data. Map key is the
	// language of the localized data, as defined by BCP-47, e.g. "en-US".
	Listings map[string]InAppProductListing `json:"listings,omitempty"`
	// ManagedProductTaxesAndComplianceSettings: Details about taxes and legal
	// compliance. Only applicable to managed products.
	ManagedProductTaxesAndComplianceSettings *ManagedProductTaxAndComplianceSettings `json:"managedProductTaxesAndComplianceSettings,omitempty"`
	// PackageName: Package name of the parent app.
	PackageName string `json:"packageName,omitempty"`
	// Prices: Prices per buyer region. None of these can be zero, as in-app
	// products are never free. Map key is region code, as defined by ISO 3166-2.
	Prices map[string]Price `json:"prices,omitempty"`
	// PurchaseType: The type of the product, e.g. a recurring subscription.
	//
	// Possible values:
	//   "purchaseTypeUnspecified" - Unspecified purchase type.
	//   "managedUser" - The default product type - one time purchase.
	//   "subscription" - In-app product with a recurring period.
	PurchaseType string `json:"purchaseType,omitempty"`
	// Sku: Stock-keeping-unit (SKU) of the product, unique within an app.
	Sku string `json:"sku,omitempty"`
	// Status: The status of the product, e.g. whether it's active.
	//
	// Possible values:
	//   "statusUnspecified" - Unspecified status.
	//   "active" - The product is published and active in the store.
	//   "inactive" - The product is not published and therefore inactive in the
	// store.
	Status string `json:"status,omitempty"`
	// SubscriptionPeriod: Subscription period, specified in ISO 8601 format.
	// Acceptable values are P1W (one week), P1M (one month), P3M (three months),
	// P6M (six months), and P1Y (one year).
	SubscriptionPeriod string `json:"subscriptionPeriod,omitempty"`
	// SubscriptionTaxesAndComplianceSettings: Details about taxes and legal
	// compliance. Only applicable to subscription products.
	SubscriptionTaxesAndComplianceSettings *SubscriptionTaxAndComplianceSettings `json:"subscriptionTaxesAndComplianceSettings,omitempty"`
	// TrialPeriod: Trial period, specified in ISO 8601 format. Acceptable values
	// are anything between P7D (seven days) and P999D (999 days).
	TrialPeriod string `json:"trialPeriod,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DefaultLanguage") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DefaultLanguage") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InAppProduct: An in-app product. The resource for InappproductsService.

func (InAppProduct) MarshalJSON ¶
func (s InAppProduct) MarshalJSON() ([]byte, error)
type InAppProductListing ¶
type InAppProductListing struct {
	// Benefits: Localized entitlement benefits for a subscription.
	Benefits []string `json:"benefits,omitempty"`
	// Description: Description for the store listing.
	Description string `json:"description,omitempty"`
	// Title: Title for the store listing.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Benefits") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Benefits") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InAppProductListing: Store listing of a single in-app product.

func (InAppProductListing) MarshalJSON ¶
func (s InAppProductListing) MarshalJSON() ([]byte, error)
type InappproductsBatchDeleteCall ¶
added in v0.154.0
type InappproductsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsBatchDeleteCall) Context ¶
added in v0.154.0
func (c *InappproductsBatchDeleteCall) Context(ctx context.Context) *InappproductsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*InappproductsBatchDeleteCall) Do ¶
added in v0.154.0
func (c *InappproductsBatchDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.inappproducts.batchDelete" call.

func (*InappproductsBatchDeleteCall) Fields ¶
added in v0.154.0
func (c *InappproductsBatchDeleteCall) Fields(s ...googleapi.Field) *InappproductsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsBatchDeleteCall) Header ¶
added in v0.154.0
func (c *InappproductsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type InappproductsBatchDeleteRequest ¶
added in v0.154.0
type InappproductsBatchDeleteRequest struct {
	// Requests: Individual delete requests. At least one request is required. Can
	// contain up to 100 requests. All requests must correspond to different in-app
	// products.
	Requests []*InappproductsDeleteRequest `json:"requests,omitempty"`
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

InappproductsBatchDeleteRequest: Request to delete multiple in-app products.

func (InappproductsBatchDeleteRequest) MarshalJSON ¶
added in v0.154.0
func (s InappproductsBatchDeleteRequest) MarshalJSON() ([]byte, error)
type InappproductsBatchGetCall ¶
added in v0.154.0
type InappproductsBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsBatchGetCall) Context ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) Context(ctx context.Context) *InappproductsBatchGetCall

Context sets the context to be used in this call's Do method.

func (*InappproductsBatchGetCall) Do ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) Do(opts ...googleapi.CallOption) (*InappproductsBatchGetResponse, error)

Do executes the "androidpublisher.inappproducts.batchGet" call. Any non-2xx status code is an error. Response headers are in either *InappproductsBatchGetResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsBatchGetCall) Fields ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) Fields(s ...googleapi.Field) *InappproductsBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsBatchGetCall) Header ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsBatchGetCall) IfNoneMatch ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) IfNoneMatch(entityTag string) *InappproductsBatchGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*InappproductsBatchGetCall) Sku ¶
added in v0.154.0
func (c *InappproductsBatchGetCall) Sku(sku ...string) *InappproductsBatchGetCall

Sku sets the optional parameter "sku": Unique identifier for the in-app products.

type InappproductsBatchGetResponse ¶
added in v0.154.0
type InappproductsBatchGetResponse struct {
	// Inappproduct: The list of requested in-app products, in the same order as
	// the request.
	Inappproduct []*InAppProduct `json:"inappproduct,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Inappproduct") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Inappproduct") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InappproductsBatchGetResponse: Response message for BatchGetSubscriptions endpoint.

func (InappproductsBatchGetResponse) MarshalJSON ¶
added in v0.154.0
func (s InappproductsBatchGetResponse) MarshalJSON() ([]byte, error)
type InappproductsBatchUpdateCall ¶
added in v0.154.0
type InappproductsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsBatchUpdateCall) Context ¶
added in v0.154.0
func (c *InappproductsBatchUpdateCall) Context(ctx context.Context) *InappproductsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*InappproductsBatchUpdateCall) Do ¶
added in v0.154.0
func (c *InappproductsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*InappproductsBatchUpdateResponse, error)

Do executes the "androidpublisher.inappproducts.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *InappproductsBatchUpdateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsBatchUpdateCall) Fields ¶
added in v0.154.0
func (c *InappproductsBatchUpdateCall) Fields(s ...googleapi.Field) *InappproductsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsBatchUpdateCall) Header ¶
added in v0.154.0
func (c *InappproductsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type InappproductsBatchUpdateRequest ¶
added in v0.154.0
type InappproductsBatchUpdateRequest struct {
	// Requests: Required. Individual update requests. At least one request is
	// required. Can contain up to 100 requests. All requests must correspond to
	// different in-app products.
	Requests []*InappproductsUpdateRequest `json:"requests,omitempty"`
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

InappproductsBatchUpdateRequest: Request to update or insert one or more in-app products.

func (InappproductsBatchUpdateRequest) MarshalJSON ¶
added in v0.154.0
func (s InappproductsBatchUpdateRequest) MarshalJSON() ([]byte, error)
type InappproductsBatchUpdateResponse ¶
added in v0.154.0
type InappproductsBatchUpdateResponse struct {
	// Inappproducts: The updated or inserted in-app products.
	Inappproducts []*InAppProduct `json:"inappproducts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Inappproducts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Inappproducts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InappproductsBatchUpdateResponse: Response for a batch in-app product update.

func (InappproductsBatchUpdateResponse) MarshalJSON ¶
added in v0.154.0
func (s InappproductsBatchUpdateResponse) MarshalJSON() ([]byte, error)
type InappproductsDeleteCall ¶
type InappproductsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsDeleteCall) Context ¶
func (c *InappproductsDeleteCall) Context(ctx context.Context) *InappproductsDeleteCall

Context sets the context to be used in this call's Do method.

func (*InappproductsDeleteCall) Do ¶
func (c *InappproductsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.inappproducts.delete" call.

func (*InappproductsDeleteCall) Fields ¶
func (c *InappproductsDeleteCall) Fields(s ...googleapi.Field) *InappproductsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsDeleteCall) Header ¶
func (c *InappproductsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsDeleteCall) LatencyTolerance ¶
added in v0.154.0
func (c *InappproductsDeleteCall) LatencyTolerance(latencyTolerance string) *InappproductsDeleteCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

type InappproductsDeleteRequest ¶
added in v0.154.0
type InappproductsDeleteRequest struct {
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Package name of the app.
	PackageName string `json:"packageName,omitempty"`
	// Sku: Unique identifier for the in-app product.
	Sku string `json:"sku,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LatencyTolerance") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LatencyTolerance") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InappproductsDeleteRequest: Request to delete an in-app product.

func (InappproductsDeleteRequest) MarshalJSON ¶
added in v0.154.0
func (s InappproductsDeleteRequest) MarshalJSON() ([]byte, error)
type InappproductsGetCall ¶
type InappproductsGetCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsGetCall) Context ¶
func (c *InappproductsGetCall) Context(ctx context.Context) *InappproductsGetCall

Context sets the context to be used in this call's Do method.

func (*InappproductsGetCall) Do ¶
func (c *InappproductsGetCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)

Do executes the "androidpublisher.inappproducts.get" call. Any non-2xx status code is an error. Response headers are in either *InAppProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsGetCall) Fields ¶
func (c *InappproductsGetCall) Fields(s ...googleapi.Field) *InappproductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsGetCall) Header ¶
func (c *InappproductsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsGetCall) IfNoneMatch ¶
func (c *InappproductsGetCall) IfNoneMatch(entityTag string) *InappproductsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type InappproductsInsertCall ¶
type InappproductsInsertCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsInsertCall) AutoConvertMissingPrices ¶
func (c *InappproductsInsertCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsInsertCall

AutoConvertMissingPrices sets the optional parameter "autoConvertMissingPrices": If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.

func (*InappproductsInsertCall) Context ¶
func (c *InappproductsInsertCall) Context(ctx context.Context) *InappproductsInsertCall

Context sets the context to be used in this call's Do method.

func (*InappproductsInsertCall) Do ¶
func (c *InappproductsInsertCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)

Do executes the "androidpublisher.inappproducts.insert" call. Any non-2xx status code is an error. Response headers are in either *InAppProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsInsertCall) Fields ¶
func (c *InappproductsInsertCall) Fields(s ...googleapi.Field) *InappproductsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsInsertCall) Header ¶
func (c *InappproductsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type InappproductsListCall ¶
type InappproductsListCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsListCall) Context ¶
func (c *InappproductsListCall) Context(ctx context.Context) *InappproductsListCall

Context sets the context to be used in this call's Do method.

func (*InappproductsListCall) Do ¶
func (c *InappproductsListCall) Do(opts ...googleapi.CallOption) (*InappproductsListResponse, error)

Do executes the "androidpublisher.inappproducts.list" call. Any non-2xx status code is an error. Response headers are in either *InappproductsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsListCall) Fields ¶
func (c *InappproductsListCall) Fields(s ...googleapi.Field) *InappproductsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsListCall) Header ¶
func (c *InappproductsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsListCall) IfNoneMatch ¶
func (c *InappproductsListCall) IfNoneMatch(entityTag string) *InappproductsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*InappproductsListCall) MaxResults ¶
func (c *InappproductsListCall) MaxResults(maxResults int64) *InappproductsListCall

MaxResults sets the optional parameter "maxResults": Deprecated and ignored. The page size is determined by the server.

func (*InappproductsListCall) StartIndex ¶
func (c *InappproductsListCall) StartIndex(startIndex int64) *InappproductsListCall

StartIndex sets the optional parameter "startIndex": Deprecated and ignored. Set the `token` parameter to retrieve the next page.

func (*InappproductsListCall) Token ¶
func (c *InappproductsListCall) Token(token string) *InappproductsListCall

Token sets the optional parameter "token": Pagination token. If empty, list starts at the first product.

type InappproductsListResponse ¶
type InappproductsListResponse struct {
	// Inappproduct: All in-app products.
	Inappproduct []*InAppProduct `json:"inappproduct,omitempty"`
	// Kind: The kind of this response
	// ("androidpublisher#inappproductsListResponse").
	Kind string `json:"kind,omitempty"`
	// PageInfo: Deprecated and unset.
	PageInfo *PageInfo `json:"pageInfo,omitempty"`
	// TokenPagination: Pagination token, to handle a number of products that is
	// over one page.
	TokenPagination *TokenPagination `json:"tokenPagination,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Inappproduct") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Inappproduct") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InappproductsListResponse: Response listing all in-app products.

func (InappproductsListResponse) MarshalJSON ¶
func (s InappproductsListResponse) MarshalJSON() ([]byte, error)
type InappproductsPatchCall ¶
type InappproductsPatchCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsPatchCall) AutoConvertMissingPrices ¶
func (c *InappproductsPatchCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsPatchCall

AutoConvertMissingPrices sets the optional parameter "autoConvertMissingPrices": If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.

func (*InappproductsPatchCall) Context ¶
func (c *InappproductsPatchCall) Context(ctx context.Context) *InappproductsPatchCall

Context sets the context to be used in this call's Do method.

func (*InappproductsPatchCall) Do ¶
func (c *InappproductsPatchCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)

Do executes the "androidpublisher.inappproducts.patch" call. Any non-2xx status code is an error. Response headers are in either *InAppProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsPatchCall) Fields ¶
func (c *InappproductsPatchCall) Fields(s ...googleapi.Field) *InappproductsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsPatchCall) Header ¶
func (c *InappproductsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsPatchCall) LatencyTolerance ¶
added in v0.154.0
func (c *InappproductsPatchCall) LatencyTolerance(latencyTolerance string) *InappproductsPatchCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

type InappproductsService ¶
type InappproductsService struct {
	// contains filtered or unexported fields
}
func NewInappproductsService ¶
func NewInappproductsService(s *Service) *InappproductsService
func (*InappproductsService) BatchDelete ¶
added in v0.154.0
func (r *InappproductsService) BatchDelete(packageName string, inappproductsbatchdeleterequest *InappproductsBatchDeleteRequest) *InappproductsBatchDeleteCall

BatchDelete: Deletes in-app products (managed products or subscriptions). Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput. This method should not be used to delete subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app.

func (*InappproductsService) BatchGet ¶
added in v0.154.0
func (r *InappproductsService) BatchGet(packageName string) *InappproductsBatchGetCall

BatchGet: Reads multiple in-app products, which can be managed products or subscriptions. This method should not be used to retrieve subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app.

func (*InappproductsService) BatchUpdate ¶
added in v0.154.0
func (r *InappproductsService) BatchUpdate(packageName string, inappproductsbatchupdaterequest *InappproductsBatchUpdateRequest) *InappproductsBatchUpdateCall

BatchUpdate: Updates or inserts one or more in-app products (managed products or subscriptions). Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput. This method should no longer be used to update subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app.

func (*InappproductsService) Delete ¶
func (r *InappproductsService) Delete(packageName string, skuid string) *InappproductsDeleteCall

Delete: Deletes an in-app product (a managed product or a subscription). This method should no longer be used to delete subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app. - sku: Unique identifier for the in-app product.

func (*InappproductsService) Get ¶
func (r *InappproductsService) Get(packageName string, skuid string) *InappproductsGetCall

Get: Gets an in-app product, which can be a managed product or a subscription. This method should no longer be used to retrieve subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app. - sku: Unique identifier for the in-app product.

func (*InappproductsService) Insert ¶
func (r *InappproductsService) Insert(packageName string, inappproduct *InAppProduct) *InappproductsInsertCall

Insert: Creates an in-app product (a managed product or a subscription). This method should no longer be used to create subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app.

func (*InappproductsService) List ¶
func (r *InappproductsService) List(packageName string) *InappproductsListCall

List: Lists all in-app products - both managed products and subscriptions. If an app has a large number of in-app products, the response may be paginated. In this case the response field `tokenPagination.nextPageToken` will be set and the caller should provide its value as a `token` request parameter to retrieve the next page. This method should no longer be used to retrieve subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app.

func (*InappproductsService) Patch ¶
func (r *InappproductsService) Patch(packageName string, skuid string, inappproduct *InAppProduct) *InappproductsPatchCall

Patch: Patches an in-app product (a managed product or a subscription). This method should no longer be used to update subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app. - sku: Unique identifier for the in-app product.

func (*InappproductsService) Update ¶
func (r *InappproductsService) Update(packageName string, skuid string, inappproduct *InAppProduct) *InappproductsUpdateCall

Update: Updates an in-app product (a managed product or a subscription). This method should no longer be used to update subscriptions. See this article (https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.html) for more information.

- packageName: Package name of the app. - sku: Unique identifier for the in-app product.

type InappproductsUpdateCall ¶
type InappproductsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*InappproductsUpdateCall) AllowMissing ¶
added in v0.52.0
func (c *InappproductsUpdateCall) AllowMissing(allowMissing bool) *InappproductsUpdateCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the in-app product with the given package_name and sku doesn't exist, the in-app product will be created.

func (*InappproductsUpdateCall) AutoConvertMissingPrices ¶
func (c *InappproductsUpdateCall) AutoConvertMissingPrices(autoConvertMissingPrices bool) *InappproductsUpdateCall

AutoConvertMissingPrices sets the optional parameter "autoConvertMissingPrices": If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.

func (*InappproductsUpdateCall) Context ¶
func (c *InappproductsUpdateCall) Context(ctx context.Context) *InappproductsUpdateCall

Context sets the context to be used in this call's Do method.

func (*InappproductsUpdateCall) Do ¶
func (c *InappproductsUpdateCall) Do(opts ...googleapi.CallOption) (*InAppProduct, error)

Do executes the "androidpublisher.inappproducts.update" call. Any non-2xx status code is an error. Response headers are in either *InAppProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InappproductsUpdateCall) Fields ¶
func (c *InappproductsUpdateCall) Fields(s ...googleapi.Field) *InappproductsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InappproductsUpdateCall) Header ¶
func (c *InappproductsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InappproductsUpdateCall) LatencyTolerance ¶
added in v0.154.0
func (c *InappproductsUpdateCall) LatencyTolerance(latencyTolerance string) *InappproductsUpdateCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

type InappproductsUpdateRequest ¶
added in v0.154.0
type InappproductsUpdateRequest struct {
	// AllowMissing: If set to true, and the in-app product with the given
	// package_name and sku doesn't exist, the in-app product will be created.
	AllowMissing bool `json:"allowMissing,omitempty"`
	// AutoConvertMissingPrices: If true the prices for all regions targeted by the
	// parent app that don't have a price specified for this in-app product will be
	// auto converted to the target currency based on the default price. Defaults
	// to false.
	AutoConvertMissingPrices bool `json:"autoConvertMissingPrices,omitempty"`
	// Inappproduct: The new in-app product.
	Inappproduct *InAppProduct `json:"inappproduct,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Package name of the app.
	PackageName string `json:"packageName,omitempty"`
	// Sku: Unique identifier for the in-app product.
	Sku string `json:"sku,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowMissing") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowMissing") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InappproductsUpdateRequest: Request to update an in-app product.

func (InappproductsUpdateRequest) MarshalJSON ¶
added in v0.154.0
func (s InappproductsUpdateRequest) MarshalJSON() ([]byte, error)
type InstallmentPlan ¶
added in v0.181.0
type InstallmentPlan struct {
	// InitialCommittedPaymentsCount: Total number of payments the user is
	// initially committed for.
	InitialCommittedPaymentsCount int64 `json:"initialCommittedPaymentsCount,omitempty"`
	// PendingCancellation: If present, this installment plan is pending to be
	// canceled. The cancellation will happen only after the user finished all
	// committed payments.
	PendingCancellation *PendingCancellation `json:"pendingCancellation,omitempty"`
	// RemainingCommittedPaymentsCount: Total number of committed payments
	// remaining to be paid for in this renewal cycle.
	RemainingCommittedPaymentsCount int64 `json:"remainingCommittedPaymentsCount,omitempty"`
	// SubsequentCommittedPaymentsCount: Total number of payments the user will be
	// committed for after each commitment period. Empty means the installment plan
	// will fall back to a normal auto-renew subscription after initial commitment.
	SubsequentCommittedPaymentsCount int64 `json:"subsequentCommittedPaymentsCount,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "InitialCommittedPaymentsCount") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InitialCommittedPaymentsCount")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstallmentPlan: Information to a installment plan.

func (InstallmentPlan) MarshalJSON ¶
added in v0.181.0
func (s InstallmentPlan) MarshalJSON() ([]byte, error)
type InstallmentsBasePlanType ¶
added in v0.181.0
type InstallmentsBasePlanType struct {
	// AccountHoldDuration: Optional. Custom account hold period of the
	// subscription, specified in ISO 8601 format. Acceptable values must be in
	// days and between P0D and P60D. An empty field represents a recommended
	// account hold, calculated as 60 days minus grace period. The sum of
	// gracePeriodDuration and accountHoldDuration must be between P30D and P60D
	// days, inclusive.
	AccountHoldDuration string `json:"accountHoldDuration,omitempty"`
	// BillingPeriodDuration: Required. Immutable. Subscription period, specified
	// in ISO 8601 format. For a list of acceptable billing periods, refer to the
	// help center. The duration is immutable after the base plan is created.
	BillingPeriodDuration string `json:"billingPeriodDuration,omitempty"`
	// CommittedPaymentsCount: Required. Immutable. The number of payments the user
	// is committed to. It is immutable after the base plan is created.
	CommittedPaymentsCount int64 `json:"committedPaymentsCount,omitempty"`
	// GracePeriodDuration: Grace period of the subscription, specified in ISO 8601
	// format. Acceptable values must be in days and between P0D and the lesser of
	// 30D and base plan billing period. If not specified, a default value will be
	// used based on the billing period. The sum of gracePeriodDuration and
	// accountHoldDuration must be between P30D and P60D days, inclusive.
	GracePeriodDuration string `json:"gracePeriodDuration,omitempty"`
	// ProrationMode: The proration mode for the base plan determines what happens
	// when a user switches to this plan from another base plan. If unspecified,
	// defaults to CHARGE_ON_NEXT_BILLING_DATE.
	//
	// Possible values:
	//   "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED" - Unspecified mode.
	//   "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE" - Users will be
	// charged for their new base plan at the end of their current billing period.
	//   "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY" - Users will
	// be charged for their new base plan immediately and in full. Any remaining
	// period of their existing subscription will be used to extend the duration of
	// the new billing plan.
	ProrationMode string `json:"prorationMode,omitempty"`
	// RenewalType: Required. Immutable. Installments base plan renewal type.
	// Determines the behavior at the end of the initial commitment. The renewal
	// type is immutable after the base plan is created.
	//
	// Possible values:
	//   "RENEWAL_TYPE_UNSPECIFIED" - Unspecified state.
	//   "RENEWAL_TYPE_RENEWS_WITHOUT_COMMITMENT" - Renews periodically for the
	// billing period duration without commitment.
	//   "RENEWAL_TYPE_RENEWS_WITH_COMMITMENT" - Renews with the commitment of the
	// same duration as the initial one.
	RenewalType string `json:"renewalType,omitempty"`
	// ResubscribeState: Whether users should be able to resubscribe to this base
	// plan in Google Play surfaces. Defaults to RESUBSCRIBE_STATE_ACTIVE if not
	// specified.
	//
	// Possible values:
	//   "RESUBSCRIBE_STATE_UNSPECIFIED" - Unspecified state.
	//   "RESUBSCRIBE_STATE_ACTIVE" - Resubscribe is active.
	//   "RESUBSCRIBE_STATE_INACTIVE" - Resubscribe is inactive.
	ResubscribeState string `json:"resubscribeState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountHoldDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountHoldDuration") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InstallmentsBasePlanType: Represents an installments base plan where a user commits to a specified number of payments.

func (InstallmentsBasePlanType) MarshalJSON ¶
added in v0.181.0
func (s InstallmentsBasePlanType) MarshalJSON() ([]byte, error)
type InternalAppSharingArtifact ¶
added in v0.5.0
type InternalAppSharingArtifact struct {
	// CertificateFingerprint: The sha256 fingerprint of the certificate used to
	// sign the generated artifact.
	CertificateFingerprint string `json:"certificateFingerprint,omitempty"`
	// DownloadUrl: The download URL generated for the uploaded artifact. Users
	// that are authorized to download can follow the link to the Play Store app to
	// install it.
	DownloadUrl string `json:"downloadUrl,omitempty"`
	// Sha256: The sha256 hash of the artifact represented as a lowercase
	// hexadecimal number, matching the output of the sha256sum command.
	Sha256 string `json:"sha256,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CertificateFingerprint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CertificateFingerprint") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InternalAppSharingArtifact: An artifact resource which gets created when uploading an APK or Android App Bundle through internal app sharing.

func (InternalAppSharingArtifact) MarshalJSON ¶
added in v0.5.0
func (s InternalAppSharingArtifact) MarshalJSON() ([]byte, error)
type InternalappsharingartifactsService ¶
added in v0.5.0
type InternalappsharingartifactsService struct {
	// contains filtered or unexported fields
}
func NewInternalappsharingartifactsService ¶
added in v0.5.0
func NewInternalappsharingartifactsService(s *Service) *InternalappsharingartifactsService
func (*InternalappsharingartifactsService) Uploadapk ¶
added in v0.5.0
func (r *InternalappsharingartifactsService) Uploadapk(packageName string) *InternalappsharingartifactsUploadapkCall

Uploadapk: Uploads an APK to internal app sharing. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See Timeouts and Errors (https://developers.google.com/api-client-library/java/google-api-java-client/errors) for an example in java.

- packageName: Package name of the app.

func (*InternalappsharingartifactsService) Uploadbundle ¶
added in v0.5.0
func (r *InternalappsharingartifactsService) Uploadbundle(packageName string) *InternalappsharingartifactsUploadbundleCall

Uploadbundle: Uploads an app bundle to internal app sharing. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See Timeouts and Errors (https://developers.google.com/api-client-library/java/google-api-java-client/errors) for an example in java.

- packageName: Package name of the app.

type InternalappsharingartifactsUploadapkCall ¶
added in v0.5.0
type InternalappsharingartifactsUploadapkCall struct {
	// contains filtered or unexported fields
}
func (*InternalappsharingartifactsUploadapkCall) Context ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) Context(ctx context.Context) *InternalappsharingartifactsUploadapkCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*InternalappsharingartifactsUploadapkCall) Do ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) Do(opts ...googleapi.CallOption) (*InternalAppSharingArtifact, error)

Do executes the "androidpublisher.internalappsharingartifacts.uploadapk" call. Any non-2xx status code is an error. Response headers are in either *InternalAppSharingArtifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InternalappsharingartifactsUploadapkCall) Fields ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) Fields(s ...googleapi.Field) *InternalappsharingartifactsUploadapkCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InternalappsharingartifactsUploadapkCall) Header ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InternalappsharingartifactsUploadapkCall) Media ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) Media(r io.Reader, options ...googleapi.MediaOption) *InternalappsharingartifactsUploadapkCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*InternalappsharingartifactsUploadapkCall) ProgressUpdater ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadapkCall) ProgressUpdater(pu googleapi.ProgressUpdater) *InternalappsharingartifactsUploadapkCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*InternalappsharingartifactsUploadapkCall)
ResumableMedia
DEPRECATED
added in v0.5.0
type InternalappsharingartifactsUploadbundleCall ¶
added in v0.5.0
type InternalappsharingartifactsUploadbundleCall struct {
	// contains filtered or unexported fields
}
func (*InternalappsharingartifactsUploadbundleCall) Context ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) Context(ctx context.Context) *InternalappsharingartifactsUploadbundleCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*InternalappsharingartifactsUploadbundleCall) Do ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) Do(opts ...googleapi.CallOption) (*InternalAppSharingArtifact, error)

Do executes the "androidpublisher.internalappsharingartifacts.uploadbundle" call. Any non-2xx status code is an error. Response headers are in either *InternalAppSharingArtifact.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*InternalappsharingartifactsUploadbundleCall) Fields ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) Fields(s ...googleapi.Field) *InternalappsharingartifactsUploadbundleCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*InternalappsharingartifactsUploadbundleCall) Header ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*InternalappsharingartifactsUploadbundleCall) Media ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) Media(r io.Reader, options ...googleapi.MediaOption) *InternalappsharingartifactsUploadbundleCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*InternalappsharingartifactsUploadbundleCall) ProgressUpdater ¶
added in v0.5.0
func (c *InternalappsharingartifactsUploadbundleCall) ProgressUpdater(pu googleapi.ProgressUpdater) *InternalappsharingartifactsUploadbundleCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*InternalappsharingartifactsUploadbundleCall)
ResumableMedia
DEPRECATED
added in v0.5.0
type IntroductoryPriceDetails ¶
added in v0.257.0
type IntroductoryPriceDetails struct {
}

IntroductoryPriceDetails: Details of an introductory price pricing phase.

type IntroductoryPriceInfo ¶
added in v0.8.0
type IntroductoryPriceInfo struct {
	// IntroductoryPriceAmountMicros: Introductory price of the subscription, not
	// including tax. The currency is the same as price_currency_code. Price is
	// expressed in micro-units, where 1,000,000 micro-units represents one unit of
	// the currency. For example, if the subscription price is €1.99,
	// price_amount_micros is 1990000.
	IntroductoryPriceAmountMicros int64 `json:"introductoryPriceAmountMicros,omitempty,string"`
	// IntroductoryPriceCurrencyCode: ISO 4217 currency code for the introductory
	// subscription price. For example, if the price is specified in British pounds
	// sterling, price_currency_code is "GBP".
	IntroductoryPriceCurrencyCode string `json:"introductoryPriceCurrencyCode,omitempty"`
	// IntroductoryPriceCycles: The number of billing period to offer introductory
	// pricing.
	IntroductoryPriceCycles int64 `json:"introductoryPriceCycles,omitempty"`
	// IntroductoryPricePeriod: Introductory price period, specified in ISO 8601
	// format. Common values are (but not limited to) "P1W" (one week), "P1M" (one
	// month), "P3M" (three months), "P6M" (six months), and "P1Y" (one year).
	IntroductoryPricePeriod string `json:"introductoryPricePeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "IntroductoryPriceAmountMicros") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IntroductoryPriceAmountMicros")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IntroductoryPriceInfo: Contains the introductory price information for a subscription.

func (IntroductoryPriceInfo) MarshalJSON ¶
added in v0.8.0
func (s IntroductoryPriceInfo) MarshalJSON() ([]byte, error)
type IntroductoryPriceOfferPhase ¶
added in v0.265.0
type IntroductoryPriceOfferPhase struct {
}

IntroductoryPriceOfferPhase: Details about introductory price offer phase.

type ItemExpiryTimeDetails ¶
added in v0.265.0
type ItemExpiryTimeDetails struct {
	// ExpiryTime: The new expiry time for this subscription item.
	ExpiryTime string `json:"expiryTime,omitempty"`
	// ProductId: The product ID of the subscription item (for example,
	// 'premium_plan').
	ProductId string `json:"productId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExpiryTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpiryTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ItemExpiryTimeDetails: Expiry time details of a subscription item.

func (ItemExpiryTimeDetails) MarshalJSON ¶
added in v0.265.0
func (s ItemExpiryTimeDetails) MarshalJSON() ([]byte, error)
type ItemReplacement ¶
added in v0.257.0
type ItemReplacement struct {
	// BasePlanId: The base plan ID of the subscription line item being replaced.
	BasePlanId string `json:"basePlanId,omitempty"`
	// OfferId: The offer ID of the subscription line item being replaced, if
	// applicable.
	OfferId string `json:"offerId,omitempty"`
	// ProductId: The product ID of the subscription line item being replaced.
	ProductId string `json:"productId,omitempty"`
	// ReplacementMode: The replacement mode applied during the purchase.
	//
	// Possible values:
	//   "REPLACEMENT_MODE_UNSPECIFIED" - Unspecified replacement mode.
	//   "WITH_TIME_PRORATION" - The new plan will be prorated and credited from
	// the old plan.
	//   "CHARGE_PRORATED_PRICE" - The user will be charged a prorated price for
	// the new plan.
	//   "WITHOUT_PRORATION" - The new plan will replace the old one without
	// prorating the time.
	//   "CHARGE_FULL_PRICE" - The user will be charged the full price for the new
	// plan.
	//   "DEFERRED" - The old plan will be cancelled and the new plan will be
	// effective after the old one expires.
	//   "KEEP_EXISTING" - The plan will remain unchanged with this replacement.
	ReplacementMode string `json:"replacementMode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ItemReplacement: Details about a subscription line item that is being replaced.

func (ItemReplacement) MarshalJSON ¶
added in v0.257.0
func (s ItemReplacement) MarshalJSON() ([]byte, error)
type LanguageTargeting ¶
added in v0.130.0
type LanguageTargeting struct {
	// Alternatives: Alternative languages.
	Alternatives []string `json:"alternatives,omitempty"`
	// Value: ISO-639: 2 or 3 letter language code.
	Value []string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LanguageTargeting: Targeting based on language.

func (LanguageTargeting) MarshalJSON ¶
added in v0.130.0
func (s LanguageTargeting) MarshalJSON() ([]byte, error)
type LineItem ¶
added in v0.234.0
type LineItem struct {
	// ListingPrice: Item's listed price on Play Store, this may or may not include
	// tax. Excludes Google-funded discounts only.
	ListingPrice *Money `json:"listingPrice,omitempty"`
	// OneTimePurchaseDetails: Details of a one-time purchase.
	OneTimePurchaseDetails *OneTimePurchaseDetails `json:"oneTimePurchaseDetails,omitempty"`
	// PaidAppDetails: Details of a paid app purchase.
	PaidAppDetails *PaidAppDetails `json:"paidAppDetails,omitempty"`
	// ProductId: The purchased product ID or in-app SKU (for example, 'monthly001'
	// or 'com.some.thing.inapp1').
	ProductId string `json:"productId,omitempty"`
	// ProductTitle: Developer-specified name of the product. Displayed in buyer's
	// locale. Example: coins, monthly subscription, etc.
	ProductTitle string `json:"productTitle,omitempty"`
	// SubscriptionDetails: Details of a subscription purchase.
	SubscriptionDetails *SubscriptionDetails `json:"subscriptionDetails,omitempty"`
	// Tax: The tax paid for this line item.
	Tax *Money `json:"tax,omitempty"`
	// Total: The total amount paid by the user for this line item, taking into
	// account discounts and tax.
	Total *Money `json:"total,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ListingPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ListingPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LineItem: Details of a line item.

func (LineItem) MarshalJSON ¶
added in v0.234.0
func (s LineItem) MarshalJSON() ([]byte, error)
type ListAppRecoveriesResponse ¶
added in v0.156.0
type ListAppRecoveriesResponse struct {
	// RecoveryActions: List of recovery actions associated with the requested
	// package name.
	RecoveryActions []*AppRecoveryAction `json:"recoveryActions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "RecoveryActions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RecoveryActions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAppRecoveriesResponse: Response message for ListAppRecoveries. -- api-linter: core::0158::response-next-page-token-field=disabled

func (ListAppRecoveriesResponse) MarshalJSON ¶
added in v0.156.0
func (s ListAppRecoveriesResponse) MarshalJSON() ([]byte, error)
type ListDeviceTierConfigsResponse ¶
added in v0.74.0
type ListDeviceTierConfigsResponse struct {
	// DeviceTierConfigs: Device tier configs created by the developer.
	DeviceTierConfigs []*DeviceTierConfig `json:"deviceTierConfigs,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeviceTierConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceTierConfigs") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDeviceTierConfigsResponse: Response listing existing device tier configs.

func (ListDeviceTierConfigsResponse) MarshalJSON ¶
added in v0.74.0
func (s ListDeviceTierConfigsResponse) MarshalJSON() ([]byte, error)
type ListOneTimeProductOffersResponse ¶
added in v0.244.0
type ListOneTimeProductOffersResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// OneTimeProductOffers: The one_time_product offers from the specified
	// request.
	OneTimeProductOffers []*OneTimeProductOffer `json:"oneTimeProductOffers,omitempty"`

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

ListOneTimeProductOffersResponse: Response message for ListOneTimeProductOffers.

func (ListOneTimeProductOffersResponse) MarshalJSON ¶
added in v0.244.0
func (s ListOneTimeProductOffersResponse) MarshalJSON() ([]byte, error)
type ListOneTimeProductsResponse ¶
added in v0.244.0
type ListOneTimeProductsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// OneTimeProducts: The one-time products from the specified app.
	OneTimeProducts []*OneTimeProduct `json:"oneTimeProducts,omitempty"`

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

ListOneTimeProductsResponse: Response message for ListOneTimeProducts.

func (ListOneTimeProductsResponse) MarshalJSON ¶
added in v0.244.0
func (s ListOneTimeProductsResponse) MarshalJSON() ([]byte, error)
type ListSubscriptionOffersResponse ¶
added in v0.80.0
type ListSubscriptionOffersResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SubscriptionOffers: The subscription offers from the specified subscription.
	SubscriptionOffers []*SubscriptionOffer `json:"subscriptionOffers,omitempty"`

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

ListSubscriptionOffersResponse: Response message for ListSubscriptionOffers.

func (ListSubscriptionOffersResponse) MarshalJSON ¶
added in v0.80.0
func (s ListSubscriptionOffersResponse) MarshalJSON() ([]byte, error)
type ListSubscriptionsResponse ¶
added in v0.80.0
type ListSubscriptionsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Subscriptions: The subscriptions from the specified app.
	Subscriptions []*Subscription `json:"subscriptions,omitempty"`

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

ListSubscriptionsResponse: Response message for ListSubscriptions.

func (ListSubscriptionsResponse) MarshalJSON ¶
added in v0.80.0
func (s ListSubscriptionsResponse) MarshalJSON() ([]byte, error)
type ListUsersResponse ¶
added in v0.59.0
type ListUsersResponse struct {
	// NextPageToken: A token to pass to subsequent calls in order to retrieve
	// subsequent results. This will not be set if there are no more results to
	// return.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Users: The resulting users.
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

ListUsersResponse: A response containing one or more users with access to an account.

func (ListUsersResponse) MarshalJSON ¶
added in v0.59.0
func (s ListUsersResponse) MarshalJSON() ([]byte, error)
type Listing ¶
type Listing struct {
	// FullDescription: Full description of the app.
	FullDescription string `json:"fullDescription,omitempty"`
	// Language: Language localization code (a BCP-47 language tag; for example,
	// "de-AT" for Austrian German).
	Language string `json:"language,omitempty"`
	// ShortDescription: Short description of the app.
	ShortDescription string `json:"shortDescription,omitempty"`
	// Title: Localized title of the app.
	Title string `json:"title,omitempty"`
	// Video: URL of a promotional YouTube video for the app.
	Video string `json:"video,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FullDescription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FullDescription") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Listing: A localized store listing. The resource for ListingsService.

func (Listing) MarshalJSON ¶
func (s Listing) MarshalJSON() ([]byte, error)
type ListingsListResponse ¶
type ListingsListResponse struct {
	// Kind: The kind of this response ("androidpublisher#listingsListResponse").
	Kind string `json:"kind,omitempty"`
	// Listings: All localized listings.
	Listings []*Listing `json:"listings,omitempty"`

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

ListingsListResponse: Response listing all localized listings.

func (ListingsListResponse) MarshalJSON ¶
func (s ListingsListResponse) MarshalJSON() ([]byte, error)
type LocalizedText ¶
type LocalizedText struct {
	// Language: Language localization code (a BCP-47 language tag; for example,
	// "de-AT" for Austrian German).
	Language string `json:"language,omitempty"`
	// Text: The text in the given language.
	Text string `json:"text,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Language") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Language") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LocalizedText: Localized text in given language.

func (LocalizedText) MarshalJSON ¶
func (s LocalizedText) MarshalJSON() ([]byte, error)
type ManagedProductTaxAndComplianceSettings ¶
added in v0.60.0
type ManagedProductTaxAndComplianceSettings struct {
	// EeaWithdrawalRightType: Digital content or service classification for
	// products distributed to users in the European Economic Area (EEA). The
	// withdrawal regime under EEA consumer laws depends on this classification.
	// Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/10463498)
	// for more information.
	//
	// Possible values:
	//   "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"
	//   "WITHDRAWAL_RIGHT_DIGITAL_CONTENT"
	//   "WITHDRAWAL_RIGHT_SERVICE"
	EeaWithdrawalRightType string `json:"eeaWithdrawalRightType,omitempty"`
	// IsTokenizedDigitalAsset: Whether this in-app product is declared as a
	// product representing a tokenized digital asset.
	IsTokenizedDigitalAsset bool `json:"isTokenizedDigitalAsset,omitempty"`
	// ProductTaxCategoryCode: Product tax category code to assign to the in-app
	// product. Product tax category determines the transaction tax rates applied
	// to the product. Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/16408159)
	// for more information.
	ProductTaxCategoryCode string `json:"productTaxCategoryCode,omitempty"`
	// RegionalProductAgeRatingInfos: Regional age rating information. Currently
	// this field is only supported for region code `US`.
	RegionalProductAgeRatingInfos []*RegionalProductAgeRatingInfo `json:"regionalProductAgeRatingInfos,omitempty"`
	// TaxRateInfoByRegionCode: A mapping from region code to tax rate details. The
	// keys are region codes as defined by Unicode's "CLDR".
	TaxRateInfoByRegionCode map[string]RegionalTaxRateInfo `json:"taxRateInfoByRegionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EeaWithdrawalRightType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EeaWithdrawalRightType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ManagedProductTaxAndComplianceSettings: Details about taxation and legal compliance for managed products.

func (ManagedProductTaxAndComplianceSettings) MarshalJSON ¶
added in v0.60.0
func (s ManagedProductTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type MigrateBasePlanPricesRequest ¶
added in v0.80.0
type MigrateBasePlanPricesRequest struct {
	// BasePlanId: Required. The unique base plan ID of the base plan to update
	// prices on.
	BasePlanId string `json:"basePlanId,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// PackageName: Required. Package name of the parent app. Must be equal to the
	// package_name field on the Subscription resource.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. The ID of the subscription to update. Must be equal to
	// the product_id field on the Subscription resource.
	ProductId string `json:"productId,omitempty"`
	// RegionalPriceMigrations: Required. The regional prices to update.
	RegionalPriceMigrations []*RegionalPriceMigrationConfig `json:"regionalPriceMigrations,omitempty"`
	// RegionsVersion: Required. The version of the available regions being used
	// for the regional_price_migrations.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MigrateBasePlanPricesRequest: Request message for MigrateBasePlanPrices.

func (MigrateBasePlanPricesRequest) MarshalJSON ¶
added in v0.80.0
func (s MigrateBasePlanPricesRequest) MarshalJSON() ([]byte, error)
type MigrateBasePlanPricesResponse ¶
added in v0.80.0
type MigrateBasePlanPricesResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

MigrateBasePlanPricesResponse: Response message for MigrateBasePlanPrices.

type ModuleMetadata ¶
added in v0.130.0
type ModuleMetadata struct {
	// DeliveryType: Indicates the delivery type (e.g. on-demand) of the module.
	//
	// Possible values:
	//   "UNKNOWN_DELIVERY_TYPE" - Unspecified delivery type.
	//   "INSTALL_TIME" - This module will always be downloaded as part of the
	// initial install of the app.
	//   "ON_DEMAND" - This module is requested on-demand, which means it will not
	// be part of the initial install, and will only be sent when requested by the
	// client.
	//   "FAST_FOLLOW" - This module will be downloaded immediately after initial
	// install finishes. The app can be opened before these modules are downloaded.
	DeliveryType string `json:"deliveryType,omitempty"`
	// Dependencies: Names of the modules that this module directly depends on.
	// Each module implicitly depends on the base module.
	Dependencies []string `json:"dependencies,omitempty"`
	// ModuleType: Indicates the type of this feature module.
	//
	// Possible values:
	//   "UNKNOWN_MODULE_TYPE" - Unknown feature module.
	//   "FEATURE_MODULE" - Regular feature module.
	ModuleType string `json:"moduleType,omitempty"`
	// Name: Module name.
	Name string `json:"name,omitempty"`
	// Targeting: The targeting that makes a conditional module installed. Relevant
	// only for Split APKs.
	Targeting *ModuleTargeting `json:"targeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeliveryType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeliveryType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ModuleMetadata: Metadata of a module.

func (ModuleMetadata) MarshalJSON ¶
added in v0.130.0
func (s ModuleMetadata) MarshalJSON() ([]byte, error)
type ModuleTargeting ¶
added in v0.130.0
type ModuleTargeting struct {
	// DeviceFeatureTargeting: Targeting for device features.
	DeviceFeatureTargeting []*DeviceFeatureTargeting `json:"deviceFeatureTargeting,omitempty"`
	// SdkVersionTargeting: The sdk version that the variant targets
	SdkVersionTargeting *SdkVersionTargeting `json:"sdkVersionTargeting,omitempty"`
	// UserCountriesTargeting: Countries-level targeting
	UserCountriesTargeting *UserCountriesTargeting `json:"userCountriesTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceFeatureTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceFeatureTargeting") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ModuleTargeting: Targeting on the module level.

func (ModuleTargeting) MarshalJSON ¶
added in v0.130.0
func (s ModuleTargeting) MarshalJSON() ([]byte, error)
type MonetizationConvertRegionPricesCall ¶
added in v0.59.0
type MonetizationConvertRegionPricesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationConvertRegionPricesCall) Context ¶
added in v0.59.0
func (c *MonetizationConvertRegionPricesCall) Context(ctx context.Context) *MonetizationConvertRegionPricesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationConvertRegionPricesCall) Do ¶
added in v0.59.0
func (c *MonetizationConvertRegionPricesCall) Do(opts ...googleapi.CallOption) (*ConvertRegionPricesResponse, error)

Do executes the "androidpublisher.monetization.convertRegionPrices" call. Any non-2xx status code is an error. Response headers are in either *ConvertRegionPricesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationConvertRegionPricesCall) Fields ¶
added in v0.59.0
func (c *MonetizationConvertRegionPricesCall) Fields(s ...googleapi.Field) *MonetizationConvertRegionPricesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationConvertRegionPricesCall) Header ¶
added in v0.59.0
func (c *MonetizationConvertRegionPricesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsBatchDeleteCall ¶
added in v0.244.0
type MonetizationOnetimeproductsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsBatchDeleteCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsBatchDeleteCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.onetimeproducts.batchDelete" call.

func (*MonetizationOnetimeproductsBatchDeleteCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsBatchDeleteCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsBatchGetCall ¶
added in v0.244.0
type MonetizationOnetimeproductsBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsBatchGetCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsBatchGetCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetOneTimeProductsResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.batchGet" call. Any non-2xx status code is an error. Response headers are in either *BatchGetOneTimeProductsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsBatchGetCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsBatchGetCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsBatchGetCall) IfNoneMatch ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsBatchGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationOnetimeproductsBatchGetCall) ProductIds ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchGetCall) ProductIds(productIds ...string) *MonetizationOnetimeproductsBatchGetCall

ProductIds sets the optional parameter "productIds": Required. A list of up to 100 product IDs to retrieve. All IDs must be different.

type MonetizationOnetimeproductsBatchUpdateCall ¶
added in v0.244.0
type MonetizationOnetimeproductsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsBatchUpdateCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchUpdateCall) Context(ctx context.Context) *MonetizationOnetimeproductsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsBatchUpdateCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductsResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateOneTimeProductsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsBatchUpdateCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsBatchUpdateCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsDeleteCall ¶
added in v0.244.0
type MonetizationOnetimeproductsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsDeleteCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsDeleteCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.onetimeproducts.delete" call.

func (*MonetizationOnetimeproductsDeleteCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsDeleteCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsDeleteCall) LatencyTolerance ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsDeleteCall) LatencyTolerance(latencyTolerance string) *MonetizationOnetimeproductsDeleteCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

type MonetizationOnetimeproductsGetCall ¶
added in v0.244.0
type MonetizationOnetimeproductsGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsGetCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsGetCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsGetCall) Do(opts ...googleapi.CallOption) (*OneTimeProduct, error)

Do executes the "androidpublisher.monetization.onetimeproducts.get" call. Any non-2xx status code is an error. Response headers are in either *OneTimeProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsGetCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsGetCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsGetCall) IfNoneMatch ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsGetCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MonetizationOnetimeproductsListCall ¶
added in v0.244.0
type MonetizationOnetimeproductsListCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsListCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) Context(ctx context.Context) *MonetizationOnetimeproductsListCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsListCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) Do(opts ...googleapi.CallOption) (*ListOneTimeProductsResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.list" call. Any non-2xx status code is an error. Response headers are in either *ListOneTimeProductsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsListCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsListCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsListCall) IfNoneMatch ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationOnetimeproductsListCall) PageSize ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) PageSize(pageSize int64) *MonetizationOnetimeproductsListCall

PageSize sets the optional parameter "pageSize": The maximum number of one-time product to return. The service may return fewer than this value. If unspecified, at most 50 one-time products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*MonetizationOnetimeproductsListCall) PageToken ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) PageToken(pageToken string) *MonetizationOnetimeproductsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListOneTimeProducts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListOneTimeProducts` must match the call that provided the page token.

func (*MonetizationOnetimeproductsListCall) Pages ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsListCall) Pages(ctx context.Context, f func(*ListOneTimeProductsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type MonetizationOnetimeproductsPatchCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPatchCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPatchCall) AllowMissing ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) AllowMissing(allowMissing bool) *MonetizationOnetimeproductsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the one-time product with the given package_name and product_id doesn't exist, the one-time product will be created. If a new one-time product is created, update_mask is ignored.

func (*MonetizationOnetimeproductsPatchCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) Context(ctx context.Context) *MonetizationOnetimeproductsPatchCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPatchCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) Do(opts ...googleapi.CallOption) (*OneTimeProduct, error)

Do executes the "androidpublisher.monetization.onetimeproducts.patch" call. Any non-2xx status code is an error. Response headers are in either *OneTimeProduct.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPatchCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPatchCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsPatchCall) LatencyTolerance ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationOnetimeproductsPatchCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product upsert. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

func (*MonetizationOnetimeproductsPatchCall) RegionsVersionVersion ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationOnetimeproductsPatchCall

RegionsVersionVersion sets the optional parameter "regionsVersion.version": Required. A string representing the version of available regions being used for the specified resource. Regional prices and latest supported version for the resource have to be specified according to the information published in this article (https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available.

func (*MonetizationOnetimeproductsPatchCall) UpdateMask ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPatchCall) UpdateMask(updateMask string) *MonetizationOnetimeproductsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated.

type MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.batchDelete" call.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdatePurchaseOptionStatesResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.batchUpdateStates" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdatePurchaseOptionStatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.activate" call. Any non-2xx status code is an error. Response headers are in either *OneTimeProductOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.batchDelete" call.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetOneTimeProductOffersResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.batchGet" call. Any non-2xx status code is an error. Response headers are in either *BatchGetOneTimeProductOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductOffersResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateOneTimeProductOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateOneTimeProductOfferStatesResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.batchUpdateStates" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateOneTimeProductOfferStatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.cancel" call. Any non-2xx status code is an error. Response headers are in either *OneTimeProductOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Do(opts ...googleapi.CallOption) (*OneTimeProductOffer, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.deactivate" call. Any non-2xx status code is an error. Response headers are in either *OneTimeProductOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationOnetimeproductsPurchaseOptionsOffersListCall ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersListCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Context ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Context(ctx context.Context) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

Context sets the context to be used in this call's Do method.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Do ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Do(opts ...googleapi.CallOption) (*ListOneTimeProductOffersResponse, error)

Do executes the "androidpublisher.monetization.onetimeproducts.purchaseOptions.offers.list" call. Any non-2xx status code is an error. Response headers are in either *ListOneTimeProductOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Fields ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Fields(s ...googleapi.Field) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Header ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) IfNoneMatch ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) IfNoneMatch(entityTag string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageSize ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageSize(pageSize int64) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

PageSize sets the optional parameter "pageSize": The maximum number of offers to return. The service may return fewer than this value. If unspecified, at most 50 offers will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageToken ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) PageToken(pageToken string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListOneTimeProductsOffers` call. Provide this to retrieve the subsequent page. When paginating, product_id, package_name and purchase_option_id provided to `ListOneTimeProductsOffersRequest` must match the call that provided the page token.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Pages ¶
added in v0.244.0
func (c *MonetizationOnetimeproductsPurchaseOptionsOffersListCall) Pages(ctx context.Context, f func(*ListOneTimeProductOffersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type MonetizationOnetimeproductsPurchaseOptionsOffersService ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsOffersService struct {
	// contains filtered or unexported fields
}
func NewMonetizationOnetimeproductsPurchaseOptionsOffersService ¶
added in v0.244.0
func NewMonetizationOnetimeproductsPurchaseOptionsOffersService(s *Service) *MonetizationOnetimeproductsPurchaseOptionsOffersService
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) Activate ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Activate(packageName string, productId string, purchaseOptionId string, offerId string, activateonetimeproductofferrequest *ActivateOneTimeProductOfferRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersActivateCall

Activate: Activates a one-time product offer.

offerId: The offer ID of the offer to activate.
packageName: The parent app (package name) of the offer to activate.
productId: The parent one-time product (ID) of the offer to activate.
purchaseOptionId: The parent purchase option (ID) of the offer to activate.
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchDelete ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchDelete(packageName string, productId string, purchaseOptionId string, batchdeleteonetimeproductoffersrequest *BatchDeleteOneTimeProductOffersRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchDeleteCall

BatchDelete: Deletes one or more one-time product offers.

packageName: The parent app (package name) of the offers to delete. Must be equal to the package_name field on all the OneTimeProductOffer resources.
productId: The product ID of the parent one-time product, if all offers to delete belong to the same product. If this request spans multiple one-time products, set this field to "-".
purchaseOptionId: The parent purchase option (ID) for which the offers should be deleted. May be specified as '-' to update offers from multiple purchase options.
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchGet ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchGet(packageName string, productId string, purchaseOptionId string, batchgetonetimeproductoffersrequest *BatchGetOneTimeProductOffersRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchGetCall

BatchGet: Reads one or more one-time product offers.

packageName: The parent app (package name) of the updated offers. Must be equal to the package_name field on all the updated OneTimeProductOffer resources.
productId: The product ID of the parent one-time product, if all updated offers belong to the same product. If this request spans multiple one-time products, set this field to "-".
purchaseOptionId: The parent purchase option (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple purchase options.
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdate ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdate(packageName string, productId string, purchaseOptionId string, batchupdateonetimeproductoffersrequest *BatchUpdateOneTimeProductOffersRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateCall

BatchUpdate: Creates or updates one or more one-time product offers.

packageName: The parent app (package name) of the updated offers. Must be equal to the package_name field on all the updated OneTimeProductOffer resources.
productId: The product ID of the parent one-time product, if all updated offers belong to the same product. If this request spans multiple one-time products, set this field to "-".
purchaseOptionId: The parent purchase option (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple purchase options.
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdateStates ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) BatchUpdateStates(packageName string, productId string, purchaseOptionId string, batchupdateonetimeproductofferstatesrequest *BatchUpdateOneTimeProductOfferStatesRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersBatchUpdateStatesCall

BatchUpdateStates: Updates a batch of one-time product offer states.

packageName: The parent app (package name) of the updated one-time product offers.
productId: The product ID of the parent one-time product, if all updated offers belong to the same one-time product. If this batch update spans multiple one-time products, set this field to "-".
purchaseOptionId: The purchase option ID of the parent purchase option, if all updated offers belong to the same purchase option. If this batch update spans multiple purchase options, set this field to "-".
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) Cancel ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Cancel(packageName string, productId string, purchaseOptionId string, offerId string, cancelonetimeproductofferrequest *CancelOneTimeProductOfferRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersCancelCall

Cancel: Cancels a one-time product offer.

- offerId: The offer ID of the offer to cancel. - packageName: The parent app (package name) of the offer to cancel. - productId: The parent one-time product (ID) of the offer to cancel. - purchaseOptionId: The parent purchase option (ID) of the offer to cancel.

func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) Deactivate ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) Deactivate(packageName string, productId string, purchaseOptionId string, offerId string, deactivateonetimeproductofferrequest *DeactivateOneTimeProductOfferRequest) *MonetizationOnetimeproductsPurchaseOptionsOffersDeactivateCall

Deactivate: Deactivates a one-time product offer.

offerId: The offer ID of the offer to deactivate.
packageName: The parent app (package name) of the offer to deactivate.
productId: The parent one-time product (ID) of the offer to deactivate.
purchaseOptionId: The parent purchase option (ID) of the offer to deactivate.
func (*MonetizationOnetimeproductsPurchaseOptionsOffersService) List ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsOffersService) List(packageName string, productId string, purchaseOptionId string) *MonetizationOnetimeproductsPurchaseOptionsOffersListCall

List: Lists all offers under a given app, product, or purchase option.

packageName: The parent app (package name) for which the offers should be read.
productId: The parent one-time product (ID) for which the offers should be read. May be specified as '-' to read all offers under an app.
purchaseOptionId: The parent purchase option (ID) for which the offers should be read. May be specified as '-' to read all offers under a one-time product or an app. Must be specified as '-' if product_id is specified as '-'.
type MonetizationOnetimeproductsPurchaseOptionsService ¶
added in v0.244.0
type MonetizationOnetimeproductsPurchaseOptionsService struct {
	Offers *MonetizationOnetimeproductsPurchaseOptionsOffersService
	// contains filtered or unexported fields
}
func NewMonetizationOnetimeproductsPurchaseOptionsService ¶
added in v0.244.0
func NewMonetizationOnetimeproductsPurchaseOptionsService(s *Service) *MonetizationOnetimeproductsPurchaseOptionsService
func (*MonetizationOnetimeproductsPurchaseOptionsService) BatchDelete ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsService) BatchDelete(packageName string, productId string, batchdeletepurchaseoptionsrequest *BatchDeletePurchaseOptionsRequest) *MonetizationOnetimeproductsPurchaseOptionsBatchDeleteCall

BatchDelete: Deletes purchase options across one or multiple one-time products. By default this operation will fail if there are any existing offers under the deleted purchase options. Use the force parameter to override the default behavior.

packageName: The parent app (package name) of the purchase options to delete.
productId: The product ID of the parent one-time product, if all purchase options to delete belong to the same one-time product. If this batch delete spans multiple one-time products, set this field to "-".
func (*MonetizationOnetimeproductsPurchaseOptionsService) BatchUpdateStates ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsPurchaseOptionsService) BatchUpdateStates(packageName string, productId string, batchupdatepurchaseoptionstatesrequest *BatchUpdatePurchaseOptionStatesRequest) *MonetizationOnetimeproductsPurchaseOptionsBatchUpdateStatesCall

BatchUpdateStates: Activates or deactivates purchase options across one or multiple one-time products.

packageName: The parent app (package name) of the updated purchase options.
productId: The product ID of the parent one-time product, if all updated purchase options belong to the same one-time product. If this batch update spans multiple one-time products, set this field to "-".
type MonetizationOnetimeproductsService ¶
added in v0.244.0
type MonetizationOnetimeproductsService struct {
	PurchaseOptions *MonetizationOnetimeproductsPurchaseOptionsService
	// contains filtered or unexported fields
}
func NewMonetizationOnetimeproductsService ¶
added in v0.244.0
func NewMonetizationOnetimeproductsService(s *Service) *MonetizationOnetimeproductsService
func (*MonetizationOnetimeproductsService) BatchDelete ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) BatchDelete(packageName string, batchdeleteonetimeproductsrequest *BatchDeleteOneTimeProductsRequest) *MonetizationOnetimeproductsBatchDeleteCall

BatchDelete: Deletes one or more one-time products.

packageName: The parent app (package name) for which the one-time products should be deleted. Must be equal to the package_name field on all the OneTimeProduct resources.
func (*MonetizationOnetimeproductsService) BatchGet ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) BatchGet(packageName string) *MonetizationOnetimeproductsBatchGetCall

BatchGet: Reads one or more one-time products.

packageName: The parent app (package name) for which the products should be retrieved. Must be equal to the package_name field on all requests.
func (*MonetizationOnetimeproductsService) BatchUpdate ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) BatchUpdate(packageName string, batchupdateonetimeproductsrequest *BatchUpdateOneTimeProductsRequest) *MonetizationOnetimeproductsBatchUpdateCall

BatchUpdate: Creates or updates one or more one-time products.

packageName: The parent app (package name) for which the one-time products should be updated. Must be equal to the package_name field on all the OneTimeProduct resources.
func (*MonetizationOnetimeproductsService) Delete ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) Delete(packageName string, productId string) *MonetizationOnetimeproductsDeleteCall

Delete: Deletes a one-time product.

packageName: The parent app (package name) of the one-time product to delete.
productId: The one-time product ID of the one-time product to delete.
func (*MonetizationOnetimeproductsService) Get ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) Get(packageName string, productId string) *MonetizationOnetimeproductsGetCall

Get: Reads a single one-time product.

- packageName: The parent app (package name) of the product to retrieve. - productId: The product ID of the product to retrieve.

func (*MonetizationOnetimeproductsService) List ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) List(packageName string) *MonetizationOnetimeproductsListCall

List: Lists all one-time products under a given app.

packageName: The parent app (package name) for which the one-time product should be read.
func (*MonetizationOnetimeproductsService) Patch ¶
added in v0.244.0
func (r *MonetizationOnetimeproductsService) Patch(packageName string, productId string, onetimeproduct *OneTimeProduct) *MonetizationOnetimeproductsPatchCall

Patch: Creates or updates a one-time product.

packageName: Immutable. Package name of the parent app.
productId: Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must start with a number or lowercase letter, and can contain numbers (0-9), lowercase letters (a-z), underscores (_), and periods (.).
type MonetizationService ¶
added in v0.59.0
type MonetizationService struct {
	Onetimeproducts *MonetizationOnetimeproductsService

	Subscriptions *MonetizationSubscriptionsService
	// contains filtered or unexported fields
}
func NewMonetizationService ¶
added in v0.59.0
func NewMonetizationService(s *Service) *MonetizationService
func (*MonetizationService) ConvertRegionPrices ¶
added in v0.59.0
func (r *MonetizationService) ConvertRegionPrices(packageName string, convertregionpricesrequest *ConvertRegionPricesRequest) *MonetizationConvertRegionPricesCall

ConvertRegionPrices: Calculates the region prices, using today's exchange rate and country-specific pricing patterns, based on the price in the request for a set of regions.

- packageName: The app package name.

type MonetizationSubscriptionsArchiveCall ¶
added in v0.80.0
type MonetizationSubscriptionsArchiveCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsArchiveCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsArchiveCall) Context(ctx context.Context) *MonetizationSubscriptionsArchiveCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsArchiveCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsArchiveCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.archive" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsArchiveCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsArchiveCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsArchiveCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansActivateCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansActivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansActivateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansActivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansActivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansActivateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansActivateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.activate" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansActivateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansActivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansActivateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansBatchMigratePricesCall ¶
added in v0.154.0
type MonetizationSubscriptionsBasePlansBatchMigratePricesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Do(opts ...googleapi.CallOption) (*BatchMigrateBasePlanPricesResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.batchMigratePrices" call. Any non-2xx status code is an error. Response headers are in either *BatchMigrateBasePlanPricesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchMigratePricesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansBatchUpdateStatesCall ¶
added in v0.154.0
type MonetizationSubscriptionsBasePlansBatchUpdateStatesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateBasePlanStatesResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.batchUpdateStates" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateBasePlanStatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansDeactivateCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansDeactivateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansDeactivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansDeactivateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.deactivate" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansDeactivateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansDeactivateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansDeleteCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansDeleteCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansDeleteCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.subscriptions.basePlans.delete" call.

func (*MonetizationSubscriptionsBasePlansDeleteCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansDeleteCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansMigratePricesCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansMigratePricesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansMigratePricesCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansMigratePricesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansMigratePricesCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Do(opts ...googleapi.CallOption) (*MigrateBasePlanPricesResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.migratePrices" call. Any non-2xx status code is an error. Response headers are in either *MigrateBasePlanPricesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansMigratePricesCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansMigratePricesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansMigratePricesCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansMigratePricesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersActivateCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersActivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersActivateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersActivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersActivateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.activate" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersActivateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersActivateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersBatchGetCall ¶
added in v0.154.0
type MonetizationSubscriptionsBasePlansOffersBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersBatchGetCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersBatchGetCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetSubscriptionOffersResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.batchGet" call. Any non-2xx status code is an error. Response headers are in either *BatchGetSubscriptionOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersBatchGetCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersBatchGetCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersBatchUpdateCall ¶
added in v0.154.0
type MonetizationSubscriptionsBasePlansOffersBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionOffersResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateSubscriptionOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall ¶
added in v0.154.0
type MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionOfferStatesResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.batchUpdateStates" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateSubscriptionOfferStatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersCreateCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersCreateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersCreateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersCreateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersCreateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.create" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersCreateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersCreateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsBasePlansOffersCreateCall) OfferId ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) OfferId(offerId string) *MonetizationSubscriptionsBasePlansOffersCreateCall

OfferId sets the optional parameter "offerId": Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource.

func (*MonetizationSubscriptionsBasePlansOffersCreateCall) RegionsVersionVersion ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersCreateCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsBasePlansOffersCreateCall

RegionsVersionVersion sets the optional parameter "regionsVersion.version": Required. A string representing the version of available regions being used for the specified resource. Regional prices and latest supported version for the resource have to be specified according to the information published in this article (https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available.

type MonetizationSubscriptionsBasePlansOffersDeactivateCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersDeactivateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersDeactivateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersDeactivateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.deactivate" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersDeactivateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersDeactivateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersDeleteCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersDeleteCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersDeleteCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.delete" call.

func (*MonetizationSubscriptionsBasePlansOffersDeleteCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersDeleteCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsBasePlansOffersGetCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersGetCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersGetCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.get" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersGetCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersGetCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsBasePlansOffersGetCall) IfNoneMatch ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBasePlansOffersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MonetizationSubscriptionsBasePlansOffersListCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersListCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersListCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersListCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersListCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Do(opts ...googleapi.CallOption) (*ListSubscriptionOffersResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.list" call. Any non-2xx status code is an error. Response headers are in either *ListSubscriptionOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersListCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersListCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsBasePlansOffersListCall) IfNoneMatch ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBasePlansOffersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationSubscriptionsBasePlansOffersListCall) PageSize ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) PageSize(pageSize int64) *MonetizationSubscriptionsBasePlansOffersListCall

PageSize sets the optional parameter "pageSize": The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*MonetizationSubscriptionsBasePlansOffersListCall) PageToken ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) PageToken(pageToken string) *MonetizationSubscriptionsBasePlansOffersListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSubscriptionsOffers` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptionOffers` must match the call that provided the page token.

func (*MonetizationSubscriptionsBasePlansOffersListCall) Pages ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersListCall) Pages(ctx context.Context, f func(*ListSubscriptionOffersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type MonetizationSubscriptionsBasePlansOffersPatchCall ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersPatchCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBasePlansOffersPatchCall) AllowMissing ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) AllowMissing(allowMissing bool) *MonetizationSubscriptionsBasePlansOffersPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn't exist, an offer will be created. If a new offer is created, update_mask is ignored.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Context(ctx context.Context) *MonetizationSubscriptionsBasePlansOffersPatchCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Do(opts ...googleapi.CallOption) (*SubscriptionOffer, error)

Do executes the "androidpublisher.monetization.subscriptions.basePlans.offers.patch" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionOffer.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBasePlansOffersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) LatencyTolerance ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationSubscriptionsBasePlansOffersPatchCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) RegionsVersionVersion ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsBasePlansOffersPatchCall

RegionsVersionVersion sets the optional parameter "regionsVersion.version": Required. A string representing the version of available regions being used for the specified resource. Regional prices and latest supported version for the resource have to be specified according to the information published in this article (https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available.

func (*MonetizationSubscriptionsBasePlansOffersPatchCall) UpdateMask ¶
added in v0.80.0
func (c *MonetizationSubscriptionsBasePlansOffersPatchCall) UpdateMask(updateMask string) *MonetizationSubscriptionsBasePlansOffersPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated.

type MonetizationSubscriptionsBasePlansOffersService ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansOffersService struct {
	// contains filtered or unexported fields
}
func NewMonetizationSubscriptionsBasePlansOffersService ¶
added in v0.80.0
func NewMonetizationSubscriptionsBasePlansOffersService(s *Service) *MonetizationSubscriptionsBasePlansOffersService
func (*MonetizationSubscriptionsBasePlansOffersService) Activate ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Activate(packageName string, productId string, basePlanId string, offerId string, activatesubscriptionofferrequest *ActivateSubscriptionOfferRequest) *MonetizationSubscriptionsBasePlansOffersActivateCall

Activate: Activates a subscription offer. Once activated, subscription offers will be available to new subscribers.

- basePlanId: The parent base plan (ID) of the offer to activate. - offerId: The unique offer ID of the offer to activate. - packageName: The parent app (package name) of the offer to activate. - productId: The parent subscription (ID) of the offer to activate.

func (*MonetizationSubscriptionsBasePlansOffersService) BatchGet ¶
added in v0.154.0
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchGet(packageName string, productId string, basePlanId string, batchgetsubscriptionoffersrequest *BatchGetSubscriptionOffersRequest) *MonetizationSubscriptionsBasePlansOffersBatchGetCall

BatchGet: Reads one or more subscription offers.

basePlanId: The parent base plan (ID) for which the offers should be read. May be specified as '-' to read offers from multiple base plans.
packageName: The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests.
productId: The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to "-". Must be set.
func (*MonetizationSubscriptionsBasePlansOffersService) BatchUpdate ¶
added in v0.154.0
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchUpdate(packageName string, productId string, basePlanId string, batchupdatesubscriptionoffersrequest *BatchUpdateSubscriptionOffersRequest) *MonetizationSubscriptionsBasePlansOffersBatchUpdateCall

BatchUpdate: Updates a batch of subscription offers. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

basePlanId: The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
packageName: The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
productId: The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to "-". Must be set.
func (*MonetizationSubscriptionsBasePlansOffersService) BatchUpdateStates ¶
added in v0.154.0
func (r *MonetizationSubscriptionsBasePlansOffersService) BatchUpdateStates(packageName string, productId string, basePlanId string, batchupdatesubscriptionofferstatesrequest *BatchUpdateSubscriptionOfferStatesRequest) *MonetizationSubscriptionsBasePlansOffersBatchUpdateStatesCall

BatchUpdateStates: Updates a batch of subscription offer states. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

basePlanId: The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
packageName: The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
productId: The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to "-". Must be set.
func (*MonetizationSubscriptionsBasePlansOffersService) Create ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Create(packageName string, productId string, basePlanId string, subscriptionoffer *SubscriptionOffer) *MonetizationSubscriptionsBasePlansOffersCreateCall

Create: Creates a new subscription offer. Only auto-renewing base plans can have subscription offers. The offer state will be DRAFT until it is activated.

basePlanId: The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource.
packageName: The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource.
productId: The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource.
func (*MonetizationSubscriptionsBasePlansOffersService) Deactivate ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Deactivate(packageName string, productId string, basePlanId string, offerId string, deactivatesubscriptionofferrequest *DeactivateSubscriptionOfferRequest) *MonetizationSubscriptionsBasePlansOffersDeactivateCall

Deactivate: Deactivates a subscription offer. Once deactivated, existing subscribers will maintain their subscription, but the offer will become unavailable to new subscribers.

- basePlanId: The parent base plan (ID) of the offer to deactivate. - offerId: The unique offer ID of the offer to deactivate. - packageName: The parent app (package name) of the offer to deactivate. - productId: The parent subscription (ID) of the offer to deactivate.

func (*MonetizationSubscriptionsBasePlansOffersService) Delete ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Delete(packageName string, productId string, basePlanId string, offerId string) *MonetizationSubscriptionsBasePlansOffersDeleteCall

Delete: Deletes a subscription offer. Can only be done for draft offers. This action is irreversible.

- basePlanId: The parent base plan (ID) of the offer to delete. - offerId: The unique offer ID of the offer to delete. - packageName: The parent app (package name) of the offer to delete. - productId: The parent subscription (ID) of the offer to delete.

func (*MonetizationSubscriptionsBasePlansOffersService) Get ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Get(packageName string, productId string, basePlanId string, offerId string) *MonetizationSubscriptionsBasePlansOffersGetCall

Get: Reads a single offer

- basePlanId: The parent base plan (ID) of the offer to get. - offerId: The unique offer ID of the offer to get. - packageName: The parent app (package name) of the offer to get. - productId: The parent subscription (ID) of the offer to get.

func (*MonetizationSubscriptionsBasePlansOffersService) List ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) List(packageName string, productId string, basePlanId string) *MonetizationSubscriptionsBasePlansOffersListCall

List: Lists all offers under a given subscription.

basePlanId: The parent base plan (ID) for which the offers should be read. May be specified as '-' to read all offers under a subscription or an app. Must be specified as '-' if product_id is specified as '-'.
packageName: The parent app (package name) for which the subscriptions should be read.
productId: The parent subscription (ID) for which the offers should be read. May be specified as '-' to read all offers under an app.
func (*MonetizationSubscriptionsBasePlansOffersService) Patch ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansOffersService) Patch(packageName string, productId string, basePlanId string, offerId string, subscriptionoffer *SubscriptionOffer) *MonetizationSubscriptionsBasePlansOffersPatchCall

Patch: Updates an existing subscription offer.

basePlanId: Immutable. The ID of the base plan to which this offer is an extension.
offerId: Immutable. Unique ID of this subscription offer. Must be unique within the base plan.
packageName: Immutable. The package name of the app the parent subscription belongs to.
productId: Immutable. The ID of the parent subscription this offer belongs to.
type MonetizationSubscriptionsBasePlansService ¶
added in v0.80.0
type MonetizationSubscriptionsBasePlansService struct {
	Offers *MonetizationSubscriptionsBasePlansOffersService
	// contains filtered or unexported fields
}
func NewMonetizationSubscriptionsBasePlansService ¶
added in v0.80.0
func NewMonetizationSubscriptionsBasePlansService(s *Service) *MonetizationSubscriptionsBasePlansService
func (*MonetizationSubscriptionsBasePlansService) Activate ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansService) Activate(packageName string, productId string, basePlanId string, activatebaseplanrequest *ActivateBasePlanRequest) *MonetizationSubscriptionsBasePlansActivateCall

Activate: Activates a base plan. Once activated, base plans will be available to new subscribers.

- basePlanId: The unique base plan ID of the base plan to activate. - packageName: The parent app (package name) of the base plan to activate. - productId: The parent subscription (ID) of the base plan to activate.

func (*MonetizationSubscriptionsBasePlansService) BatchMigratePrices ¶
added in v0.154.0
func (r *MonetizationSubscriptionsBasePlansService) BatchMigratePrices(packageName string, productId string, batchmigratebaseplanpricesrequest *BatchMigrateBasePlanPricesRequest) *MonetizationSubscriptionsBasePlansBatchMigratePricesCall

BatchMigratePrices: Batch variant of the MigrateBasePlanPrices endpoint. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

packageName: The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources.
productId: The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to "-". Must be set.
func (*MonetizationSubscriptionsBasePlansService) BatchUpdateStates ¶
added in v0.154.0
func (r *MonetizationSubscriptionsBasePlansService) BatchUpdateStates(packageName string, productId string, batchupdatebaseplanstatesrequest *BatchUpdateBasePlanStatesRequest) *MonetizationSubscriptionsBasePlansBatchUpdateStatesCall

BatchUpdateStates: Activates or deactivates base plans across one or multiple subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

packageName: The parent app (package name) of the updated base plans.
productId: The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to "-". Must be set.
func (*MonetizationSubscriptionsBasePlansService) Deactivate ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansService) Deactivate(packageName string, productId string, basePlanId string, deactivatebaseplanrequest *DeactivateBasePlanRequest) *MonetizationSubscriptionsBasePlansDeactivateCall

Deactivate: Deactivates a base plan. Once deactivated, the base plan will become unavailable to new subscribers, but existing subscribers will maintain their subscription

- basePlanId: The unique base plan ID of the base plan to deactivate. - packageName: The parent app (package name) of the base plan to deactivate. - productId: The parent subscription (ID) of the base plan to deactivate.

func (*MonetizationSubscriptionsBasePlansService) Delete ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansService) Delete(packageName string, productId string, basePlanId string) *MonetizationSubscriptionsBasePlansDeleteCall

Delete: Deletes a base plan. Can only be done for draft base plans. This action is irreversible.

- basePlanId: The unique offer ID of the base plan to delete. - packageName: The parent app (package name) of the base plan to delete. - productId: The parent subscription (ID) of the base plan to delete.

func (*MonetizationSubscriptionsBasePlansService) MigratePrices ¶
added in v0.80.0
func (r *MonetizationSubscriptionsBasePlansService) MigratePrices(packageName string, productId string, basePlanId string, migratebaseplanpricesrequest *MigrateBasePlanPricesRequest) *MonetizationSubscriptionsBasePlansMigratePricesCall

MigratePrices: Migrates subscribers from one or more legacy price cohorts to the current price. Requests result in Google Play notifying affected subscribers. Only up to 250 simultaneous legacy price cohorts are supported.

basePlanId: The unique base plan ID of the base plan to update prices on.
packageName: Package name of the parent app. Must be equal to the package_name field on the Subscription resource.
productId: The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource.
type MonetizationSubscriptionsBatchGetCall ¶
added in v0.154.0
type MonetizationSubscriptionsBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBatchGetCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) Context(ctx context.Context) *MonetizationSubscriptionsBatchGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBatchGetCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) Do(opts ...googleapi.CallOption) (*BatchGetSubscriptionsResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.batchGet" call. Any non-2xx status code is an error. Response headers are in either *BatchGetSubscriptionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBatchGetCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBatchGetCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsBatchGetCall) IfNoneMatch ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsBatchGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationSubscriptionsBatchGetCall) ProductIds ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchGetCall) ProductIds(productIds ...string) *MonetizationSubscriptionsBatchGetCall

ProductIds sets the optional parameter "productIds": Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different.

type MonetizationSubscriptionsBatchUpdateCall ¶
added in v0.154.0
type MonetizationSubscriptionsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsBatchUpdateCall) Context ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchUpdateCall) Context(ctx context.Context) *MonetizationSubscriptionsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsBatchUpdateCall) Do ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateSubscriptionsResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateSubscriptionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsBatchUpdateCall) Fields ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchUpdateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsBatchUpdateCall) Header ¶
added in v0.154.0
func (c *MonetizationSubscriptionsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsCreateCall ¶
added in v0.80.0
type MonetizationSubscriptionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsCreateCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) Context(ctx context.Context) *MonetizationSubscriptionsCreateCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsCreateCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.create" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsCreateCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsCreateCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsCreateCall) ProductId ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) ProductId(productId string) *MonetizationSubscriptionsCreateCall

ProductId sets the optional parameter "productId": Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource.

func (*MonetizationSubscriptionsCreateCall) RegionsVersionVersion ¶
added in v0.80.0
func (c *MonetizationSubscriptionsCreateCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsCreateCall

RegionsVersionVersion sets the optional parameter "regionsVersion.version": Required. A string representing the version of available regions being used for the specified resource. Regional prices and latest supported version for the resource have to be specified according to the information published in this article (https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available.

type MonetizationSubscriptionsDeleteCall ¶
added in v0.80.0
type MonetizationSubscriptionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsDeleteCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsDeleteCall) Context(ctx context.Context) *MonetizationSubscriptionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsDeleteCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.monetization.subscriptions.delete" call.

func (*MonetizationSubscriptionsDeleteCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsDeleteCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsDeleteCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type MonetizationSubscriptionsGetCall ¶
added in v0.80.0
type MonetizationSubscriptionsGetCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsGetCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsGetCall) Context(ctx context.Context) *MonetizationSubscriptionsGetCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsGetCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.get" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsGetCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsGetCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsGetCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsGetCall) IfNoneMatch ¶
added in v0.80.0
func (c *MonetizationSubscriptionsGetCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MonetizationSubscriptionsListCall ¶
added in v0.80.0
type MonetizationSubscriptionsListCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsListCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) Context(ctx context.Context) *MonetizationSubscriptionsListCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsListCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) Do(opts ...googleapi.CallOption) (*ListSubscriptionsResponse, error)

Do executes the "androidpublisher.monetization.subscriptions.list" call. Any non-2xx status code is an error. Response headers are in either *ListSubscriptionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsListCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsListCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsListCall) IfNoneMatch ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) IfNoneMatch(entityTag string) *MonetizationSubscriptionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MonetizationSubscriptionsListCall) PageSize ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) PageSize(pageSize int64) *MonetizationSubscriptionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

func (*MonetizationSubscriptionsListCall) PageToken ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) PageToken(pageToken string) *MonetizationSubscriptionsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSubscriptions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptions` must match the call that provided the page token.

func (*MonetizationSubscriptionsListCall) Pages ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) Pages(ctx context.Context, f func(*ListSubscriptionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*MonetizationSubscriptionsListCall) ShowArchived ¶
added in v0.80.0
func (c *MonetizationSubscriptionsListCall) ShowArchived(showArchived bool) *MonetizationSubscriptionsListCall

ShowArchived sets the optional parameter "showArchived": Deprecated: subscription archiving is not supported.

type MonetizationSubscriptionsPatchCall ¶
added in v0.80.0
type MonetizationSubscriptionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*MonetizationSubscriptionsPatchCall) AllowMissing ¶
added in v0.154.0
func (c *MonetizationSubscriptionsPatchCall) AllowMissing(allowMissing bool) *MonetizationSubscriptionsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set to true, and the subscription with the given package_name and product_id doesn't exist, the subscription will be created. If a new subscription is created, update_mask is ignored.

func (*MonetizationSubscriptionsPatchCall) Context ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) Context(ctx context.Context) *MonetizationSubscriptionsPatchCall

Context sets the context to be used in this call's Do method.

func (*MonetizationSubscriptionsPatchCall) Do ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) Do(opts ...googleapi.CallOption) (*Subscription, error)

Do executes the "androidpublisher.monetization.subscriptions.patch" call. Any non-2xx status code is an error. Response headers are in either *Subscription.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MonetizationSubscriptionsPatchCall) Fields ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) Fields(s ...googleapi.Field) *MonetizationSubscriptionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MonetizationSubscriptionsPatchCall) Header ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MonetizationSubscriptionsPatchCall) LatencyTolerance ¶
added in v0.154.0
func (c *MonetizationSubscriptionsPatchCall) LatencyTolerance(latencyTolerance string) *MonetizationSubscriptionsPatchCall

LatencyTolerance sets the optional parameter "latencyTolerance": The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.

Possible values:

"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to


PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will


propagate to clients within several minutes on average and up to a few hours in rare cases. Throughput is limited to 7,200 updates per app per hour.

"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will


propagate to clients within 24 hours. Supports high throughput of up to 720,000 updates per app per hour using batch modification methods.

func (*MonetizationSubscriptionsPatchCall) RegionsVersionVersion ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) RegionsVersionVersion(regionsVersionVersion string) *MonetizationSubscriptionsPatchCall

RegionsVersionVersion sets the optional parameter "regionsVersion.version": Required. A string representing the version of available regions being used for the specified resource. Regional prices and latest supported version for the resource have to be specified according to the information published in this article (https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available.

func (*MonetizationSubscriptionsPatchCall) UpdateMask ¶
added in v0.80.0
func (c *MonetizationSubscriptionsPatchCall) UpdateMask(updateMask string) *MonetizationSubscriptionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated.

type MonetizationSubscriptionsService ¶
added in v0.80.0
type MonetizationSubscriptionsService struct {
	BasePlans *MonetizationSubscriptionsBasePlansService
	// contains filtered or unexported fields
}
func NewMonetizationSubscriptionsService ¶
added in v0.80.0
func NewMonetizationSubscriptionsService(s *Service) *MonetizationSubscriptionsService
func (*MonetizationSubscriptionsService) Archive ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) Archive(packageName string, productId string, archivesubscriptionrequest *ArchiveSubscriptionRequest) *MonetizationSubscriptionsArchiveCall

Archive: Deprecated: subscription archiving is not supported.

packageName: The parent app (package name) of the app of the subscription to delete.
productId: The unique product ID of the subscription to delete.
func (*MonetizationSubscriptionsService) BatchGet ¶
added in v0.154.0
func (r *MonetizationSubscriptionsService) BatchGet(packageName string) *MonetizationSubscriptionsBatchGetCall

BatchGet: Reads one or more subscriptions.

packageName: The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests.
func (*MonetizationSubscriptionsService) BatchUpdate ¶
added in v0.154.0
func (r *MonetizationSubscriptionsService) BatchUpdate(packageName string, batchupdatesubscriptionsrequest *BatchUpdateSubscriptionsRequest) *MonetizationSubscriptionsBatchUpdateCall

BatchUpdate: Updates a batch of subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

packageName: The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources.
func (*MonetizationSubscriptionsService) Create ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) Create(packageName string, subscription *Subscription) *MonetizationSubscriptionsCreateCall

Create: Creates a new subscription. Newly added base plans will remain in draft state until activated.

packageName: The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource.
func (*MonetizationSubscriptionsService) Delete ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) Delete(packageName string, productId string) *MonetizationSubscriptionsDeleteCall

Delete: Deletes a subscription. A subscription can only be deleted if it has never had a base plan published.

packageName: The parent app (package name) of the app of the subscription to delete.
productId: The unique product ID of the subscription to delete.
func (*MonetizationSubscriptionsService) Get ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) Get(packageName string, productId string) *MonetizationSubscriptionsGetCall

Get: Reads a single subscription.

- packageName: The parent app (package name) of the subscription to get. - productId: The unique product ID of the subscription to get.

func (*MonetizationSubscriptionsService) List ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) List(packageName string) *MonetizationSubscriptionsListCall

List: Lists all subscriptions under a given app.

packageName: The parent app (package name) for which the subscriptions should be read.
func (*MonetizationSubscriptionsService) Patch ¶
added in v0.80.0
func (r *MonetizationSubscriptionsService) Patch(packageName string, productId string, subscription *Subscription) *MonetizationSubscriptionsPatchCall

Patch: Updates an existing subscription.

packageName: Immutable. Package name of the parent app.
productId: Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length.
type Money ¶
added in v0.59.0
type Money struct {
	// CurrencyCode: The three-letter currency code defined in ISO 4217.
	CurrencyCode string `json:"currencyCode,omitempty"`
	// Nanos: Number of nano (10^-9) units of the amount. The value must be between
	// -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos`
	// must be positive or zero. If `units` is zero, `nanos` can be positive, zero,
	// or negative. If `units` is negative, `nanos` must be negative or zero. For
	// example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
	Nanos int64 `json:"nanos,omitempty"`
	// Units: The whole units of the amount. For example if `currencyCode` is
	// "USD", then 1 unit is one US dollar.
	Units int64 `json:"units,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "CurrencyCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrencyCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Money: Represents an amount of money with its currency type.

func (Money) MarshalJSON ¶
added in v0.59.0
func (s Money) MarshalJSON() ([]byte, error)
type MultiAbi ¶
added in v0.130.0
type MultiAbi struct {
	// Abi: A list of targeted ABIs, as represented by the Android Platform
	Abi []*Abi `json:"abi,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Abi") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Abi") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MultiAbi: Represents a list of ABIs.

func (MultiAbi) MarshalJSON ¶
added in v0.130.0
func (s MultiAbi) MarshalJSON() ([]byte, error)
type MultiAbiTargeting ¶
added in v0.130.0
type MultiAbiTargeting struct {
	// Alternatives: Targeting of other sibling directories that were in the
	// Bundle. For main splits this is targeting of other main splits.
	Alternatives []*MultiAbi `json:"alternatives,omitempty"`
	// Value: Value of a multi abi.
	Value []*MultiAbi `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MultiAbiTargeting: Targeting based on multiple abis.

func (MultiAbiTargeting) MarshalJSON ¶
added in v0.130.0
func (s MultiAbiTargeting) MarshalJSON() ([]byte, error)
type OfferDetails ¶
added in v0.104.0
type OfferDetails struct {
	// BasePlanId: The base plan ID. Present for all base plan and offers.
	BasePlanId string `json:"basePlanId,omitempty"`
	// OfferId: The offer ID. Only present for discounted offers.
	OfferId string `json:"offerId,omitempty"`
	// OfferTags: The latest offer tags associated with the offer. It includes tags
	// inherited from the base plan.
	OfferTags []string `json:"offerTags,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OfferDetails: Offer details information related to a purchase line item.

func (OfferDetails) MarshalJSON ¶
added in v0.104.0
func (s OfferDetails) MarshalJSON() ([]byte, error)
type OfferPhase ¶
added in v0.265.0
type OfferPhase struct {
	// BasePrice: Set when the offer phase is a base plan pricing phase.
	BasePrice *BasePriceOfferPhase `json:"basePrice,omitempty"`
	// FreeTrial: Set when the offer phase is a free trial.
	FreeTrial *FreeTrialOfferPhase `json:"freeTrial,omitempty"`
	// IntroductoryPrice: Set when the offer phase is an introductory price offer
	// phase.
	IntroductoryPrice *IntroductoryPriceOfferPhase `json:"introductoryPrice,omitempty"`
	// ProrationPeriod: Set when the offer phase is a proration period.
	ProrationPeriod *ProrationPeriodOfferPhase `json:"prorationPeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OfferPhase: Offer phase details.

func (OfferPhase) MarshalJSON ¶
added in v0.265.0
func (s OfferPhase) MarshalJSON() ([]byte, error)
type OfferPhaseDetails ¶
added in v0.257.0
type OfferPhaseDetails struct {
	// BaseDetails: The order funds a base price period.
	BaseDetails *BaseDetails `json:"baseDetails,omitempty"`
	// FreeTrialDetails: The order funds a free trial period.
	FreeTrialDetails *FreeTrialDetails `json:"freeTrialDetails,omitempty"`
	// IntroductoryPriceDetails: The order funds an introductory pricing period.
	IntroductoryPriceDetails *IntroductoryPriceDetails `json:"introductoryPriceDetails,omitempty"`
	// ProrationPeriodDetails: The order funds a proration period.
	ProrationPeriodDetails *ProrationPeriodDetails `json:"prorationPeriodDetails,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BaseDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BaseDetails") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OfferPhaseDetails: Details of a pricing phase for the entitlement period funded by this order.

func (OfferPhaseDetails) MarshalJSON ¶
added in v0.257.0
func (s OfferPhaseDetails) MarshalJSON() ([]byte, error)
type OfferTag ¶
added in v0.80.0
type OfferTag struct {
	// Tag: Must conform with RFC-1034. That is, this string can only contain
	// lower-case letters (a-z), numbers (0-9), and hyphens (-), and be at most 20
	// characters.
	Tag string `json:"tag,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Tag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Tag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OfferTag: Represents a custom tag specified for a product offer.

func (OfferTag) MarshalJSON ¶
added in v0.80.0
func (s OfferTag) MarshalJSON() ([]byte, error)
type OneTimeCode ¶
added in v0.210.0
type OneTimeCode struct {
}

OneTimeCode: A single use promotion code.

type OneTimeExternalTransaction ¶
added in v0.117.0
type OneTimeExternalTransaction struct {
	// ExternalTransactionToken: Input only. Provided during the call to Create.
	// Retrieved from the client when the alternative billing flow is launched.
	ExternalTransactionToken string `json:"externalTransactionToken,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalTransactionToken")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalTransactionToken") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeExternalTransaction: Represents a one-time transaction.

func (OneTimeExternalTransaction) MarshalJSON ¶
added in v0.117.0
func (s OneTimeExternalTransaction) MarshalJSON() ([]byte, error)
type OneTimeProduct ¶
added in v0.244.0
type OneTimeProduct struct {
	// Listings: Required. Set of localized title and description data. Must not
	// have duplicate entries with the same language_code.
	Listings []*OneTimeProductListing `json:"listings,omitempty"`
	// OfferTags: Optional. List of up to 20 custom tags specified for this
	// one-time product, and returned to the app through the billing library.
	// Purchase options and offers for this product will also receive these tags in
	// the billing library.
	OfferTags []*OfferTag `json:"offerTags,omitempty"`
	// PackageName: Required. Immutable. Package name of the parent app.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Required. Immutable. Unique product ID of the product. Unique
	// within the parent app. Product IDs must start with a number or lowercase
	// letter, and can contain numbers (0-9), lowercase letters (a-z), underscores
	// (_), and periods (.).
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptions: Required. The set of purchase options for this one-time
	// product.
	PurchaseOptions []*OneTimeProductPurchaseOption `json:"purchaseOptions,omitempty"`
	// RegionsVersion: Output only. The version of the regions configuration that
	// was used to generate the one-time product.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// RestrictedPaymentCountries: Optional. Countries where the purchase of this
	// one-time product is restricted to payment methods registered in the same
	// country. If empty, no payment location restrictions are imposed.
	RestrictedPaymentCountries *RestrictedPaymentCountries `json:"restrictedPaymentCountries,omitempty"`
	// TaxAndComplianceSettings: Details about taxes and legal compliance.
	TaxAndComplianceSettings *OneTimeProductTaxAndComplianceSettings `json:"taxAndComplianceSettings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Listings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Listings") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProduct: A single one-time product for an app.

func (OneTimeProduct) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProduct) MarshalJSON() ([]byte, error)
type OneTimeProductBuyPurchaseOption ¶
added in v0.244.0
type OneTimeProductBuyPurchaseOption struct {
	// LegacyCompatible: Optional. Whether this purchase option will be available
	// in legacy PBL flows that do not support one-time products model. Up to one
	// "buy" purchase option can be marked as backwards compatible.
	LegacyCompatible bool `json:"legacyCompatible,omitempty"`
	// MultiQuantityEnabled: Optional. Whether this purchase option allows
	// multi-quantity. Multi-quantity allows buyer to purchase more than one item
	// in a single checkout.
	MultiQuantityEnabled bool `json:"multiQuantityEnabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LegacyCompatible") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LegacyCompatible") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductBuyPurchaseOption: A purchase option that can be bought.

func (OneTimeProductBuyPurchaseOption) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductBuyPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductDiscountedOffer ¶
added in v0.244.0
type OneTimeProductDiscountedOffer struct {
	// EndTime: Time when the offer will stop being available.
	EndTime string `json:"endTime,omitempty"`
	// RedemptionLimit: Optional. The number of times this offer can be redeemed.
	// If unset or set to 0, allows for unlimited offer redemptions. Otherwise must
	// be a number between 1 and 50 inclusive.
	RedemptionLimit int64 `json:"redemptionLimit,omitempty,string"`
	// StartTime: Time when the offer will start being available.
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

OneTimeProductDiscountedOffer: Configuration specific to discounted offers.

func (OneTimeProductDiscountedOffer) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductDiscountedOffer) MarshalJSON() ([]byte, error)
type OneTimeProductListing ¶
added in v0.244.0
type OneTimeProductListing struct {
	// Description: Required. The description of this product in the language of
	// this listing. The maximum length is 200 characters.
	Description string `json:"description,omitempty"`
	// LanguageCode: Required. The language of this listing, as defined by BCP-47,
	// e.g., "en-US".
	LanguageCode string `json:"languageCode,omitempty"`
	// Title: Required. The title of this product in the language of this listing.
	// The maximum length is 55 characters.
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

OneTimeProductListing: Regional store listing for a one-time product.

func (OneTimeProductListing) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductListing) MarshalJSON() ([]byte, error)
type OneTimeProductOffer ¶
added in v0.244.0
type OneTimeProductOffer struct {
	// DiscountedOffer: A discounted offer.
	DiscountedOffer *OneTimeProductDiscountedOffer `json:"discountedOffer,omitempty"`
	// OfferId: Required. Immutable. The ID of this product offer. Must be unique
	// within the purchase option. It must start with a number or lower-case
	// letter, and can only contain lower-case letters (a-z), numbers (0-9), and
	// hyphens (-). The maximum length is 63 characters.
	OfferId string `json:"offerId,omitempty"`
	// OfferTags: Optional. List of up to 20 custom tags specified for this offer,
	// and returned to the app through the billing library.
	OfferTags []*OfferTag `json:"offerTags,omitempty"`
	// PackageName: Required. Immutable. The package name of the app the parent
	// product belongs to.
	PackageName string `json:"packageName,omitempty"`
	// PreOrderOffer: A pre-order offer.
	PreOrderOffer *OneTimeProductPreOrderOffer `json:"preOrderOffer,omitempty"`
	// ProductId: Required. Immutable. The ID of the parent product this offer
	// belongs to.
	ProductId string `json:"productId,omitempty"`
	// PurchaseOptionId: Required. Immutable. The ID of the purchase option to
	// which this offer is an extension.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// RegionalPricingAndAvailabilityConfigs: Set of regional pricing and
	// availability information for this offer. Must not have duplicate entries
	// with the same region_code.
	RegionalPricingAndAvailabilityConfigs []*OneTimeProductOfferRegionalPricingAndAvailabilityConfig `json:"regionalPricingAndAvailabilityConfigs,omitempty"`
	// RegionsVersion: Output only. The version of the regions configuration that
	// was used to generate the one-time product offer.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// State: Output only. The current state of this offer. This field cannot be
	// changed by updating the resource. Use the dedicated endpoints instead.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value, should never be used.
	//   "DRAFT" - The offer is not and has never been available to users.
	//   "ACTIVE" - The offer is available to users, as long as its conditions are
	// met.
	//   "CANCELLED" - This state is specific to pre-orders. The offer is cancelled
	// and not available to users. All pending orders related to this offer were
	// cancelled.
	//   "INACTIVE" - This state is specific to discounted offers. The offer is no
	// longer available to users.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DiscountedOffer") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DiscountedOffer") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductOffer: A single offer for a one-time product.

func (OneTimeProductOffer) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductOffer) MarshalJSON() ([]byte, error)
type OneTimeProductOfferNoPriceOverrideOptions ¶
added in v0.244.0
type OneTimeProductOfferNoPriceOverrideOptions struct {
}

OneTimeProductOfferNoPriceOverrideOptions: Options for one-time product offers without a regional price override.

type OneTimeProductOfferRegionalPricingAndAvailabilityConfig ¶
added in v0.244.0
type OneTimeProductOfferRegionalPricingAndAvailabilityConfig struct {
	// AbsoluteDiscount: The absolute value of the discount that is subtracted from
	// the purchase option price. It should be between 0 and the purchase option
	// price.
	AbsoluteDiscount *Money `json:"absoluteDiscount,omitempty"`
	// Availability: Required. The availability for this region.
	//
	// Possible values:
	//   "AVAILABILITY_UNSPECIFIED" - Unspecified availability. Must not be used.
	//   "AVAILABLE" - The offer is available to users.
	//   "NO_LONGER_AVAILABLE" - The offer is no longer available to users. This
	// value can only be used if the availability was previously set as AVAILABLE.
	Availability string `json:"availability,omitempty"`
	// NoOverride: The price defined in the purchase option for this region will be
	// used.
	NoOverride *OneTimeProductOfferNoPriceOverrideOptions `json:"noOverride,omitempty"`
	// RegionCode: Required. Region code this configuration applies to, as defined
	// by ISO 3166-2, e.g., "US".
	RegionCode string `json:"regionCode,omitempty"`
	// RelativeDiscount: The fraction of the purchase option price that the user
	// pays for this offer. For example, if the purchase option price for this
	// region is $12, then a 50% discount would correspond to a price of $6. The
	// discount must be specified as a fraction strictly larger than 0 and strictly
	// smaller than 1. The resulting price will be rounded to the nearest billable
	// unit (e.g. cents for USD). The relative discount is considered invalid if
	// the discounted price ends up being smaller than the minimum price allowed in
	// this region.
	RelativeDiscount float64 `json:"relativeDiscount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AbsoluteDiscount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbsoluteDiscount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductOfferRegionalPricingAndAvailabilityConfig: Regional pricing and availability configuration for a one-time product offer.

func (OneTimeProductOfferRegionalPricingAndAvailabilityConfig) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductOfferRegionalPricingAndAvailabilityConfig) MarshalJSON() ([]byte, error)
func (*OneTimeProductOfferRegionalPricingAndAvailabilityConfig) UnmarshalJSON ¶
added in v0.244.0
func (s *OneTimeProductOfferRegionalPricingAndAvailabilityConfig) UnmarshalJSON(data []byte) error
type OneTimeProductPreOrderOffer ¶
added in v0.244.0
type OneTimeProductPreOrderOffer struct {
	// EndTime: Required. Time when the pre-order will stop being available.
	EndTime string `json:"endTime,omitempty"`
	// PriceChangeBehavior: Required. Immutable. Specifies how price changes affect
	// pre-existing pre-orders.
	//
	// Possible values:
	//   "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_UNSPECIFIED" - Unspecified price change
	// behavior. Must not be used.
	//   "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_TWO_POINT_LOWEST" - The buyer gets
	// charged the minimum between the initial price at the time of pre-order and
	// the final offer price on the release date.
	//   "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_NEW_ORDERS_ONLY" - The buyer gets the
	// same price as the one they pre-ordered, regardless of any price changes that
	// may have happened after the pre-order.
	PriceChangeBehavior string `json:"priceChangeBehavior,omitempty"`
	// ReleaseTime: Required. Time on which the product associated with the
	// pre-order will be released and the pre-order orders fulfilled.
	ReleaseTime string `json:"releaseTime,omitempty"`
	// StartTime: Required. Time when the pre-order will start being available.
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

OneTimeProductPreOrderOffer: Configuration specific to pre-order offers.

func (OneTimeProductPreOrderOffer) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductPreOrderOffer) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOption ¶
added in v0.244.0
type OneTimeProductPurchaseOption struct {
	// BuyOption: A purchase option that can be bought.
	BuyOption *OneTimeProductBuyPurchaseOption `json:"buyOption,omitempty"`
	// NewRegionsConfig: Pricing information for any new locations Play may launch
	// in the future. If omitted, the purchase option will not be automatically
	// available in any new locations Play may launch in the future.
	NewRegionsConfig *OneTimeProductPurchaseOptionNewRegionsConfig `json:"newRegionsConfig,omitempty"`
	// OfferTags: Optional. List of up to 20 custom tags specified for this
	// purchase option, and returned to the app through the billing library. Offers
	// for this purchase option will also receive these tags in the billing
	// library.
	OfferTags []*OfferTag `json:"offerTags,omitempty"`
	// PurchaseOptionId: Required. Immutable. The unique identifier of this
	// purchase option. Must be unique within the one-time product. It must start
	// with a number or lower-case letter, and can only contain lower-case letters
	// (a-z), numbers (0-9), and hyphens (-). The maximum length is 63 characters.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// RegionalPricingAndAvailabilityConfigs: Regional pricing and availability
	// information for this purchase option.
	RegionalPricingAndAvailabilityConfigs []*OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig `json:"regionalPricingAndAvailabilityConfigs,omitempty"`
	// RentOption: A purchase option that can be rented.
	RentOption *OneTimeProductRentPurchaseOption `json:"rentOption,omitempty"`
	// State: Output only. The state of the purchase option, i.e., whether it's
	// active. This field cannot be changed by updating the resource. Use the
	// dedicated endpoints instead.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value, should never be used.
	//   "DRAFT" - The purchase option is not and has never been available to
	// users.
	//   "ACTIVE" - The purchase option is available to users.
	//   "INACTIVE" - The purchase option is not available to users anymore.
	//   "INACTIVE_PUBLISHED" - The purchase option is not available for purchase
	// anymore, but we continue to expose its offer via the Play Billing Library
	// for backwards compatibility. Only automatically migrated purchase options
	// can be in this state.
	State string `json:"state,omitempty"`
	// TaxAndComplianceSettings: Optional. Details about taxes and legal
	// compliance.
	TaxAndComplianceSettings *PurchaseOptionTaxAndComplianceSettings `json:"taxAndComplianceSettings,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BuyOption") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuyOption") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductPurchaseOption: A single purchase option for a one-time product.

func (OneTimeProductPurchaseOption) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOptionNewRegionsConfig ¶
added in v0.244.0
type OneTimeProductPurchaseOptionNewRegionsConfig struct {
	// Availability: Required. The regional availability for the new regions
	// config. When set to AVAILABLE, the pricing information will be used for any
	// new regions Play may launch in the future.
	//
	// Possible values:
	//   "AVAILABILITY_UNSPECIFIED" - Unspecified availability. Must not be used.
	//   "AVAILABLE" - The config will be used for any new regions Play may launch
	// in the future.
	//   "NO_LONGER_AVAILABLE" - The config is not available anymore and will not
	// be used for any new regions Play may launch in the future. This value can
	// only be used if the availability was previously set as AVAILABLE.
	Availability string `json:"availability,omitempty"`
	// EurPrice: Required. Price in EUR to use for any new regions Play may launch
	// in.
	EurPrice *Money `json:"eurPrice,omitempty"`
	// UsdPrice: Required. Price in USD to use for any new regions Play may launch
	// in.
	UsdPrice *Money `json:"usdPrice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Availability") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Availability") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductPurchaseOptionNewRegionsConfig: Pricing information for any new regions Play may launch in the future.

func (OneTimeProductPurchaseOptionNewRegionsConfig) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductPurchaseOptionNewRegionsConfig) MarshalJSON() ([]byte, error)
type OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig ¶
added in v0.244.0
type OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig struct {
	// Availability: The availability of the purchase option.
	//
	// Possible values:
	//   "AVAILABILITY_UNSPECIFIED" - Unspecified availability. Must not be used.
	//   "AVAILABLE" - The purchase option is available to users.
	//   "NO_LONGER_AVAILABLE" - The purchase option is no longer available to
	// users. This value can only be used if the availability was previously set as
	// AVAILABLE.
	//   "AVAILABLE_IF_RELEASED" - The purchase option is initially unavailable,
	// but made available via a released pre-order offer.
	//   "AVAILABLE_FOR_OFFERS_ONLY" - The purchase option is unavailable but
	// offers linked to it (i.e. Play Points offer) are available.
	Availability string `json:"availability,omitempty"`
	// Price: The price of the purchase option in the specified region. Must be set
	// in the currency that is linked to the specified region.
	Price *Money `json:"price,omitempty"`
	// RegionCode: Required. Region code this configuration applies to, as defined
	// by ISO 3166-2, e.g., "US".
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Availability") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Availability") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig: Regional pricing and availability configuration for a purchase option.

func (OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig) MarshalJSON() ([]byte, error)
type OneTimeProductRentPurchaseOption ¶
added in v0.244.0
type OneTimeProductRentPurchaseOption struct {
	// ExpirationPeriod: Optional. The amount of time the user has after starting
	// consuming the entitlement before it is revoked. Specified in ISO 8601
	// format.
	ExpirationPeriod string `json:"expirationPeriod,omitempty"`
	// RentalPeriod: Required. The amount of time a user has the entitlement for.
	// Starts at purchase flow completion. Specified in ISO 8601 format.
	RentalPeriod string `json:"rentalPeriod,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExpirationPeriod") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpirationPeriod") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductRentPurchaseOption: A purchase option that can be rented.

func (OneTimeProductRentPurchaseOption) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductRentPurchaseOption) MarshalJSON() ([]byte, error)
type OneTimeProductTaxAndComplianceSettings ¶
added in v0.244.0
type OneTimeProductTaxAndComplianceSettings struct {
	// IsTokenizedDigitalAsset: Whether this one-time product is declared as a
	// product representing a tokenized digital asset.
	IsTokenizedDigitalAsset bool `json:"isTokenizedDigitalAsset,omitempty"`
	// ProductTaxCategoryCode: Product tax category code to assign to the one-time
	// product. Product tax category determines the transaction tax rates applied
	// to the product. Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/16408159)
	// for more information.
	ProductTaxCategoryCode string `json:"productTaxCategoryCode,omitempty"`
	// RegionalProductAgeRatingInfos: Regional age rating information. Currently
	// this field is only supported for region code `US`.
	RegionalProductAgeRatingInfos []*RegionalProductAgeRatingInfo `json:"regionalProductAgeRatingInfos,omitempty"`
	// RegionalTaxConfigs: Regional tax configuration.
	RegionalTaxConfigs []*RegionalTaxConfig `json:"regionalTaxConfigs,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IsTokenizedDigitalAsset") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsTokenizedDigitalAsset") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimeProductTaxAndComplianceSettings: Details about taxation, Google Play policy and legal compliance for one-time products.

func (OneTimeProductTaxAndComplianceSettings) MarshalJSON ¶
added in v0.244.0
func (s OneTimeProductTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type OneTimePurchaseDetails ¶
added in v0.234.0
type OneTimePurchaseDetails struct {
	// OfferId: The offer ID of the one-time purchase offer.
	OfferId string `json:"offerId,omitempty"`
	// PreorderDetails: The details of a pre-order purchase. Only set if it is a
	// pre-order purchase. Note that this field will be set even after pre-order is
	// fulfilled.
	PreorderDetails *PreorderDetails `json:"preorderDetails,omitempty"`
	// PurchaseOptionId: ID of the purchase option. This field is set for both
	// purchase options and variant offers. For purchase options, this ID
	// identifies the purchase option itself. For variant offers, this ID refers to
	// the associated purchase option, and in conjunction with offer_id it
	// identifies the variant offer.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// Quantity: The number of items purchased (for multi-quantity item purchases).
	Quantity int64 `json:"quantity,omitempty"`
	// RentalDetails: The details of a rent purchase. Only set if it is a rent
	// purchase.
	RentalDetails *RentalDetails `json:"rentalDetails,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OfferId") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OfferId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OneTimePurchaseDetails: Details of a one-time purchase.

func (OneTimePurchaseDetails) MarshalJSON ¶
added in v0.234.0
func (s OneTimePurchaseDetails) MarshalJSON() ([]byte, error)
type Order ¶
added in v0.234.0
type Order struct {
	// BuyerAddress: Address information for the customer, for use in tax
	// computation. When Google is the Merchant of Record for the order, only
	// country is shown.
	BuyerAddress *BuyerAddress `json:"buyerAddress,omitempty"`
	// CreateTime: The time when the order was created.
	CreateTime string `json:"createTime,omitempty"`
	// DeveloperRevenueInBuyerCurrency: Your revenue for this order in the buyer's
	// currency, including deductions of partial refunds, taxes and fees. Google
	// deducts standard transaction and third party fees from each sale, including
	// VAT in some regions.
	DeveloperRevenueInBuyerCurrency *Money `json:"developerRevenueInBuyerCurrency,omitempty"`
	// LastEventTime: The time of the last event that occurred on the order.
	LastEventTime string `json:"lastEventTime,omitempty"`
	// LineItems: The individual line items making up this order.
	LineItems []*LineItem `json:"lineItems,omitempty"`
	// OrderDetails: Detailed information about the order at creation time.
	OrderDetails *OrderDetails `json:"orderDetails,omitempty"`
	// OrderHistory: Details about events which modified the order.
	OrderHistory *OrderHistory `json:"orderHistory,omitempty"`
	// OrderId: The order ID.
	OrderId string `json:"orderId,omitempty"`
	// PointsDetails: Play points applied to the order, including offer
	// information, discount rate and point values.
	PointsDetails *PointsDetails `json:"pointsDetails,omitempty"`
	// PurchaseToken: The token provided to the user's device when the subscription
	// or item was purchased.
	PurchaseToken string `json:"purchaseToken,omitempty"`
	// SalesChannel: The originating sales channel of the order.
	//
	// Possible values:
	//   "SALES_CHANNEL_UNSPECIFIED" - Sales channel unspecified. This value is not
	// used.
	//   "IN_APP" - Standard orders that initiated from in-app.
	//   "PC_EMULATOR" - Orders initiated from a PC emulator for in-app purchases.
	//   "NATIVE_PC" - Orders initiated from a native PC app for in-app purchases.
	//   "PLAY_STORE" - Orders initiated from the Google Play store.
	//   "OUTSIDE_PLAY_STORE" - Orders initiated outside the Google Play store.
	SalesChannel string `json:"salesChannel,omitempty"`
	// State: The state of the order.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State unspecified. This value is not used.
	//   "PENDING" - Order has been created and is waiting to be processed.
	//   "PROCESSED" - Order has been successfully processed.
	//   "CANCELED" - Order was canceled before being processed.
	//   "PENDING_REFUND" - Requested refund is waiting to be processed.
	//   "PARTIALLY_REFUNDED" - Part of the order amount was refunded.
	//   "REFUNDED" - The full order amount was refunded.
	State string `json:"state,omitempty"`
	// Tax: The total tax paid as a part of this order.
	Tax *Money `json:"tax,omitempty"`
	// Total: The final amount paid by the customer, taking into account discounts
	// and taxes.
	Total *Money `json:"total,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BuyerAddress") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuyerAddress") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Order: The Order resource encapsulates comprehensive information about a transaction made on Google Play. It includes a variety of attributes that provide details about the order itself, the products purchased, and the history of events related to the order. The Orders APIs provide real-time access to your order data within the Google Play ecosystem. You can retrieve detailed information and metadata for both one-time and recurring orders, including transaction details like charges, taxes, and refunds, as well as metadata such as pricing phases for subscriptions. The Orders APIs let you automate tasks related to order management, reducing the need for manual checks via the Play Developer Console. The following are some of the use cases for this API: + Real-time order data retrieval - Get order details and metadata immediately after a purchase using an order ID. + Order update synchronization - Periodically sync order updates to maintain an up-to-date record of order information. Note: + The Orders API calls count towards your Play Developer API quota, which defaults to 200K daily, and may be insufficient to sync extensive order histories. + A maximum of 1000 orders can be retrieved per call. Using larger page sizes is recommended to minimize quota usage. Check your quota in the Cloud Console and request more if required.

func (Order) MarshalJSON ¶
added in v0.234.0
func (s Order) MarshalJSON() ([]byte, error)
type OrderDetails ¶
added in v0.234.0
type OrderDetails struct {
	// TaxInclusive: Indicates whether the listed price was tax inclusive or not.
	TaxInclusive bool `json:"taxInclusive,omitempty"`
	// ForceSendFields is a list of field names (e.g. "TaxInclusive") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "TaxInclusive") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OrderDetails: Detailed information about the order at creation time.

func (OrderDetails) MarshalJSON ¶
added in v0.234.0
func (s OrderDetails) MarshalJSON() ([]byte, error)
type OrderHistory ¶
added in v0.234.0
type OrderHistory struct {
	// CancellationEvent: Details of when the order was canceled.
	CancellationEvent *CancellationEvent `json:"cancellationEvent,omitempty"`
	// PartialRefundEvents: Details of the partial refund events for this order.
	PartialRefundEvents []*PartialRefundEvent `json:"partialRefundEvents,omitempty"`
	// ProcessedEvent: Details of when the order was processed.
	ProcessedEvent *ProcessedEvent `json:"processedEvent,omitempty"`
	// RefundEvent: Details of when the order was fully refunded.
	RefundEvent *RefundEvent `json:"refundEvent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CancellationEvent") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CancellationEvent") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OrderHistory: Details about events which modified the order.

func (OrderHistory) MarshalJSON ¶
added in v0.234.0
func (s OrderHistory) MarshalJSON() ([]byte, error)
type OrdersBatchgetCall ¶
added in v0.234.0
type OrdersBatchgetCall struct {
	// contains filtered or unexported fields
}
func (*OrdersBatchgetCall) Context ¶
added in v0.234.0
func (c *OrdersBatchgetCall) Context(ctx context.Context) *OrdersBatchgetCall

Context sets the context to be used in this call's Do method.

func (*OrdersBatchgetCall) Do ¶
added in v0.234.0
func (c *OrdersBatchgetCall) Do(opts ...googleapi.CallOption) (*BatchGetOrdersResponse, error)

Do executes the "androidpublisher.orders.batchget" call. Any non-2xx status code is an error. Response headers are in either *BatchGetOrdersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrdersBatchgetCall) Fields ¶
added in v0.234.0
func (c *OrdersBatchgetCall) Fields(s ...googleapi.Field) *OrdersBatchgetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrdersBatchgetCall) Header ¶
added in v0.234.0
func (c *OrdersBatchgetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrdersBatchgetCall) IfNoneMatch ¶
added in v0.234.0
func (c *OrdersBatchgetCall) IfNoneMatch(entityTag string) *OrdersBatchgetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrdersBatchgetCall) OrderIds ¶
added in v0.234.0
func (c *OrdersBatchgetCall) OrderIds(orderIds ...string) *OrdersBatchgetCall

OrderIds sets the optional parameter "orderIds": Required. The list of order IDs to retrieve order details for. There must be between 1 and 1000 (inclusive) order IDs per request. If any order ID is not found or does not match the provided package, the entire request will fail with an error. The order IDs must be distinct.

type OrdersGetCall ¶
added in v0.234.0
type OrdersGetCall struct {
	// contains filtered or unexported fields
}
func (*OrdersGetCall) Context ¶
added in v0.234.0
func (c *OrdersGetCall) Context(ctx context.Context) *OrdersGetCall

Context sets the context to be used in this call's Do method.

func (*OrdersGetCall) Do ¶
added in v0.234.0
func (c *OrdersGetCall) Do(opts ...googleapi.CallOption) (*Order, error)

Do executes the "androidpublisher.orders.get" call. Any non-2xx status code is an error. Response headers are in either *Order.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrdersGetCall) Fields ¶
added in v0.234.0
func (c *OrdersGetCall) Fields(s ...googleapi.Field) *OrdersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrdersGetCall) Header ¶
added in v0.234.0
func (c *OrdersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrdersGetCall) IfNoneMatch ¶
added in v0.234.0
func (c *OrdersGetCall) IfNoneMatch(entityTag string) *OrdersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrdersRefundCall ¶
type OrdersRefundCall struct {
	// contains filtered or unexported fields
}
func (*OrdersRefundCall) Context ¶
func (c *OrdersRefundCall) Context(ctx context.Context) *OrdersRefundCall

Context sets the context to be used in this call's Do method.

func (*OrdersRefundCall) Do ¶
func (c *OrdersRefundCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.orders.refund" call.

func (*OrdersRefundCall) Fields ¶
func (c *OrdersRefundCall) Fields(s ...googleapi.Field) *OrdersRefundCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrdersRefundCall) Header ¶
func (c *OrdersRefundCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrdersRefundCall) Revoke ¶
func (c *OrdersRefundCall) Revoke(revoke bool) *OrdersRefundCall

Revoke sets the optional parameter "revoke": Whether to revoke the purchased item. If set to true, access to the subscription or in-app item will be terminated immediately. If the item is a recurring subscription, all future payments will also be terminated. Consumed in-app items need to be handled by developer's app. (optional).

type OrdersService ¶
type OrdersService struct {
	// contains filtered or unexported fields
}
func NewOrdersService ¶
func NewOrdersService(s *Service) *OrdersService
func (*OrdersService) Batchget ¶
added in v0.234.0
func (r *OrdersService) Batchget(packageName string) *OrdersBatchgetCall

Batchget: Get order details for a list of orders.

packageName: The package name of the application for which this subscription or in-app item was purchased (for example, 'com.some.thing').
func (*OrdersService) Get ¶
added in v0.234.0
func (r *OrdersService) Get(packageName string, orderId string) *OrdersGetCall

Get: Get order details for a single order.

orderId: The order ID provided to the user when the subscription or in-app order was purchased.
packageName: The package name of the application for which this subscription or in-app item was purchased (for example, 'com.some.thing').
func (*OrdersService) Refund ¶
func (r *OrdersService) Refund(packageName string, orderId string) *OrdersRefundCall

Refund: Refunds a user's subscription or in-app purchase order. Orders older than 3 years cannot be refunded.

orderId: The order ID provided to the user when the subscription or in-app order was purchased.
packageName: The package name of the application for which this subscription or in-app item was purchased (for example, 'com.some.thing').
type OtherRecurringProduct ¶
added in v0.175.0
type OtherRecurringProduct struct {
}

OtherRecurringProduct: Details of a recurring external transaction product which doesn't belong to any other more specific category.

type OtherRegionsBasePlanConfig ¶
added in v0.80.0
type OtherRegionsBasePlanConfig struct {
	// EurPrice: Required. Price in EUR to use for any new locations Play may
	// launch in.
	EurPrice *Money `json:"eurPrice,omitempty"`
	// NewSubscriberAvailability: Whether the base plan is available for new
	// subscribers in any new locations Play may launch in. If not specified, this
	// will default to false.
	NewSubscriberAvailability bool `json:"newSubscriberAvailability,omitempty"`
	// UsdPrice: Required. Price in USD to use for any new locations Play may
	// launch in.
	UsdPrice *Money `json:"usdPrice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EurPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EurPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OtherRegionsBasePlanConfig: Pricing information for any new locations Play may launch in.

func (OtherRegionsBasePlanConfig) MarshalJSON ¶
added in v0.80.0
func (s OtherRegionsBasePlanConfig) MarshalJSON() ([]byte, error)
type OtherRegionsSubscriptionOfferConfig ¶
added in v0.80.0
type OtherRegionsSubscriptionOfferConfig struct {
	// OtherRegionsNewSubscriberAvailability: Whether the subscription offer in any
	// new locations Play may launch in the future. If not specified, this will
	// default to false.
	OtherRegionsNewSubscriberAvailability bool `json:"otherRegionsNewSubscriberAvailability,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "OtherRegionsNewSubscriberAvailability") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "OtherRegionsNewSubscriberAvailability") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

OtherRegionsSubscriptionOfferConfig: Configuration for any new locations Play may launch in specified on a subscription offer.

func (OtherRegionsSubscriptionOfferConfig) MarshalJSON ¶
added in v0.80.0
func (s OtherRegionsSubscriptionOfferConfig) MarshalJSON() ([]byte, error)
type OtherRegionsSubscriptionOfferPhaseConfig ¶
added in v0.80.0
type OtherRegionsSubscriptionOfferPhaseConfig struct {
	// AbsoluteDiscounts: The absolute amount of money subtracted from the base
	// plan price prorated over the phase duration that the user pays for this
	// offer phase. For example, if the base plan price for this region is $12 for
	// a period of 1 year, then a $1 absolute discount for a phase of a duration of
	// 3 months would correspond to a price of $2. The resulting price may not be
	// smaller than the minimum price allowed for any new locations Play may launch
	// in.
	AbsoluteDiscounts *OtherRegionsSubscriptionOfferPhasePrices `json:"absoluteDiscounts,omitempty"`
	// Free: Set to specify this offer is free to obtain.
	Free *OtherRegionsSubscriptionOfferPhaseFreePriceOverride `json:"free,omitempty"`
	// OtherRegionsPrices: The absolute price the user pays for this offer phase.
	// The price must not be smaller than the minimum price allowed for any new
	// locations Play may launch in.
	OtherRegionsPrices *OtherRegionsSubscriptionOfferPhasePrices `json:"otherRegionsPrices,omitempty"`
	// RelativeDiscount: The fraction of the base plan price prorated over the
	// phase duration that the user pays for this offer phase. For example, if the
	// base plan price for this region is $12 for a period of 1 year, then a 50%
	// discount for a phase of a duration of 3 months would correspond to a price
	// of $1.50. The discount must be specified as a fraction strictly larger than
	// 0 and strictly smaller than 1. The resulting price will be rounded to the
	// nearest billable unit (e.g. cents for USD). The relative discount is
	// considered invalid if the discounted price ends up being smaller than the
	// minimum price allowed in any new locations Play may launch in.
	RelativeDiscount float64 `json:"relativeDiscount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AbsoluteDiscounts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbsoluteDiscounts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OtherRegionsSubscriptionOfferPhaseConfig: Configuration for any new locations Play may launch in for a single offer phase.

func (OtherRegionsSubscriptionOfferPhaseConfig) MarshalJSON ¶
added in v0.80.0
func (s OtherRegionsSubscriptionOfferPhaseConfig) MarshalJSON() ([]byte, error)
func (*OtherRegionsSubscriptionOfferPhaseConfig) UnmarshalJSON ¶
added in v0.80.0
func (s *OtherRegionsSubscriptionOfferPhaseConfig) UnmarshalJSON(data []byte) error
type OtherRegionsSubscriptionOfferPhaseFreePriceOverride ¶
added in v0.175.0
type OtherRegionsSubscriptionOfferPhaseFreePriceOverride struct {
}

OtherRegionsSubscriptionOfferPhaseFreePriceOverride: Represents the free price override configuration for any new locations Play may launch for a single offer phase.

type OtherRegionsSubscriptionOfferPhasePrices ¶
added in v0.80.0
type OtherRegionsSubscriptionOfferPhasePrices struct {
	// EurPrice: Required. Price in EUR to use for any new locations Play may
	// launch in.
	EurPrice *Money `json:"eurPrice,omitempty"`
	// UsdPrice: Required. Price in USD to use for any new locations Play may
	// launch in.
	UsdPrice *Money `json:"usdPrice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EurPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EurPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OtherRegionsSubscriptionOfferPhasePrices: Pricing information for any new locations Play may launch in.

func (OtherRegionsSubscriptionOfferPhasePrices) MarshalJSON ¶
added in v0.80.0
func (s OtherRegionsSubscriptionOfferPhasePrices) MarshalJSON() ([]byte, error)
type OutOfAppPurchaseContext ¶
added in v0.257.0
type OutOfAppPurchaseContext struct {
	// ExpiredExternalAccountIdentifiers: User account identifier from the last
	// expired subscription for this SKU.
	ExpiredExternalAccountIdentifiers *ExternalAccountIdentifiers `json:"expiredExternalAccountIdentifiers,omitempty"`
	// ExpiredPurchaseToken: The purchase token of the last expired subscription.
	// This purchase token must only be used to help identify the user if the link
	// between the purchaseToken and user is stored in your database. This cannot
	// be used to call the Google Developer API if it has been more than 60 days
	// since expiry.
	ExpiredPurchaseToken string `json:"expiredPurchaseToken,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ExpiredExternalAccountIdentifiers") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ExpiredExternalAccountIdentifiers") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

OutOfAppPurchaseContext: Information specific to an out of app purchase.

func (OutOfAppPurchaseContext) MarshalJSON ¶
added in v0.257.0
func (s OutOfAppPurchaseContext) MarshalJSON() ([]byte, error)
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
type PaidAppDetails ¶
added in v0.234.0
type PaidAppDetails struct {
}

PaidAppDetails: Details of a paid app purchase.

type PartialRefund ¶
added in v0.117.0
type PartialRefund struct {
	// RefundId: Required. A unique id distinguishing this partial refund. If the
	// refund is successful, subsequent refunds with the same id will fail. Must be
	// unique across refunds for one individual transaction.
	RefundId string `json:"refundId,omitempty"`
	// RefundPreTaxAmount: Required. The pre-tax amount of the partial refund.
	// Should be less than the remaining pre-tax amount of the transaction.
	RefundPreTaxAmount *Price `json:"refundPreTaxAmount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RefundId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RefundId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PartialRefund: A partial refund of a transaction.

func (PartialRefund) MarshalJSON ¶
added in v0.117.0
func (s PartialRefund) MarshalJSON() ([]byte, error)
type PartialRefundEvent ¶
added in v0.234.0
type PartialRefundEvent struct {
	// CreateTime: The time when the partial refund was created.
	CreateTime string `json:"createTime,omitempty"`
	// ProcessTime: The time when the partial refund was processed.
	ProcessTime string `json:"processTime,omitempty"`
	// RefundDetails: Details for the partial refund.
	RefundDetails *RefundDetails `json:"refundDetails,omitempty"`
	// State: The state of the partial refund.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - State unspecified. This value is not used.
	//   "PENDING" - The partial refund has been created, but not yet processed.
	//   "PROCESSED_SUCCESSFULLY" - The partial refund was processed successfully.
	State string `json:"state,omitempty"`
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

PartialRefundEvent: Details of the partial refund events for this order.

func (PartialRefundEvent) MarshalJSON ¶
added in v0.234.0
func (s PartialRefundEvent) MarshalJSON() ([]byte, error)
type PausedStateContext ¶
added in v0.80.0
type PausedStateContext struct {
	// AutoResumeTime: Time at which the subscription will be automatically
	// resumed.
	AutoResumeTime string `json:"autoResumeTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoResumeTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoResumeTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PausedStateContext: Information specific to a subscription in paused state.

func (PausedStateContext) MarshalJSON ¶
added in v0.80.0
func (s PausedStateContext) MarshalJSON() ([]byte, error)
type PendingCancellation ¶
added in v0.181.0
type PendingCancellation struct {
}

PendingCancellation: This is an indicator of whether there is a pending cancellation on the virtual installment plan. The cancellation will happen only after the user finished all committed payments.

type PointsDetails ¶
added in v0.234.0
type PointsDetails struct {
	// PointsCouponValue: The monetary value of a Play Points coupon. This is the
	// discount the coupon provides, which may not be the total amount. Only set
	// when Play Points coupons have been used. E.g. for a 100 points for $2
	// coupon, this is $2.
	PointsCouponValue *Money `json:"pointsCouponValue,omitempty"`
	// PointsDiscountRateMicros: The percentage rate which the Play Points
	// promotion reduces the cost by. E.g. for a 100 points for $2 coupon, this is
	// 500,000. Since $2 has an estimate of 200 points, but the actual Points
	// required, 100, is 50% of this, and 50% in micros is 500,000. Between 0 and
	// 1,000,000.
	PointsDiscountRateMicros int64 `json:"pointsDiscountRateMicros,omitempty,string"`
	// PointsOfferId: ID unique to the play points offer in use for this order.
	PointsOfferId string `json:"pointsOfferId,omitempty"`
	// PointsSpent: The number of Play Points applied in this order. E.g. for a 100
	// points for $2 coupon, this is 100. For coupon stacked with base offer, this
	// is the total points spent across both.
	PointsSpent int64 `json:"pointsSpent,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "PointsCouponValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PointsCouponValue") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PointsDetails: Details relating to any Play Points applied to an order.

func (PointsDetails) MarshalJSON ¶
added in v0.234.0
func (s PointsDetails) MarshalJSON() ([]byte, error)
type PreorderDetails ¶
added in v0.255.0
type PreorderDetails struct {
}

PreorderDetails: Details of a pre-order purchase.

type PreorderOfferDetails ¶
added in v0.255.0
type PreorderOfferDetails struct {
	// PreorderReleaseTime: The time when a preordered item is released for a
	// preorder purchase.
	PreorderReleaseTime string `json:"preorderReleaseTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PreorderReleaseTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PreorderReleaseTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PreorderOfferDetails: Offer details information related to a preorder line item.

func (PreorderOfferDetails) MarshalJSON ¶
added in v0.255.0
func (s PreorderOfferDetails) MarshalJSON() ([]byte, error)
type PrepaidBasePlanType ¶
added in v0.80.0
type PrepaidBasePlanType struct {
	// BillingPeriodDuration: Required. Immutable. Subscription period, specified
	// in ISO 8601 format. For a list of acceptable billing periods, refer to the
	// help center. The duration is immutable after the base plan is created.
	BillingPeriodDuration string `json:"billingPeriodDuration,omitempty"`
	// TimeExtension: Whether users should be able to extend this prepaid base plan
	// in Google Play surfaces. Defaults to TIME_EXTENSION_ACTIVE if not specified.
	//
	// Possible values:
	//   "TIME_EXTENSION_UNSPECIFIED" - Unspecified state.
	//   "TIME_EXTENSION_ACTIVE" - Time extension is active. Users are allowed to
	// top-up or extend their prepaid plan.
	//   "TIME_EXTENSION_INACTIVE" - Time extension is inactive. Users cannot
	// top-up or extend their prepaid plan.
	TimeExtension string `json:"timeExtension,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BillingPeriodDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BillingPeriodDuration") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrepaidBasePlanType: Represents a base plan that does not automatically renew at the end of the base plan, and must be manually renewed by the user.

func (PrepaidBasePlanType) MarshalJSON ¶
added in v0.80.0
func (s PrepaidBasePlanType) MarshalJSON() ([]byte, error)
type PrepaidPlan ¶
added in v0.80.0
type PrepaidPlan struct {
	// AllowExtendAfterTime: If present, this is the time after which top up
	// purchases are allowed for the prepaid plan. Will not be present for expired
	// prepaid plans.
	AllowExtendAfterTime string `json:"allowExtendAfterTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowExtendAfterTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowExtendAfterTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrepaidPlan: Information related to a prepaid plan.

func (PrepaidPlan) MarshalJSON ¶
added in v0.80.0
func (s PrepaidPlan) MarshalJSON() ([]byte, error)
type Price ¶
type Price struct {
	// Currency: 3 letter Currency code, as defined by ISO 4217. See
	// java/com/google/common/money/CurrencyCode.java
	Currency string `json:"currency,omitempty"`
	// PriceMicros: Price in 1/million of the currency base unit, represented as a
	// string.
	PriceMicros string `json:"priceMicros,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Currency") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Currency") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Price: Definition of a price, i.e. currency and units.

func (Price) MarshalJSON ¶
func (s Price) MarshalJSON() ([]byte, error)
type PriceStepUpConsentDetails ¶
added in v0.249.0
type PriceStepUpConsentDetails struct {
	// ConsentDeadlineTime: The deadline by which the user must provide consent. If
	// consent is not provided by this time, the subscription will be canceled.
	ConsentDeadlineTime string `json:"consentDeadlineTime,omitempty"`
	// NewPrice: The new price which requires user consent.
	NewPrice *Money `json:"newPrice,omitempty"`
	// State: Output only. The state of the price step-up consent.
	//
	// Possible values:
	//   "CONSENT_STATE_UNSPECIFIED" - Unspecified consent state.
	//   "PENDING" - The user has not yet provided consent.
	//   "CONFIRMED" - The user has consented, and the new price is waiting to take
	// effect.
	//   "COMPLETED" - The user has consented, and the new price has taken effect.
	State string `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConsentDeadlineTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsentDeadlineTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PriceStepUpConsentDetails: Information related to a price step-up that requires user consent.

func (PriceStepUpConsentDetails) MarshalJSON ¶
added in v0.249.0
func (s PriceStepUpConsentDetails) MarshalJSON() ([]byte, error)
type ProcessedEvent ¶
added in v0.234.0
type ProcessedEvent struct {
	// EventTime: The time when the order was processed.
	EventTime string `json:"eventTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProcessedEvent: Details of when the order was processed.

func (ProcessedEvent) MarshalJSON ¶
added in v0.234.0
func (s ProcessedEvent) MarshalJSON() ([]byte, error)
type ProductLineItem ¶
added in v0.240.0
type ProductLineItem struct {
	// ProductId: The purchased product ID (for example, 'monthly001').
	ProductId string `json:"productId,omitempty"`
	// ProductOfferDetails: The offer details for this item.
	ProductOfferDetails *ProductOfferDetails `json:"productOfferDetails,omitempty"`
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

ProductLineItem: Contains item-level info for a ProductPurchaseV2.

func (ProductLineItem) MarshalJSON ¶
added in v0.240.0
func (s ProductLineItem) MarshalJSON() ([]byte, error)
type ProductOfferDetails ¶
added in v0.240.0
type ProductOfferDetails struct {
	// ConsumptionState: Output only. The consumption state of the purchase.
	//
	// Possible values:
	//   "CONSUMPTION_STATE_UNSPECIFIED" - Consumption state unspecified. This
	// value should never be set.
	//   "CONSUMPTION_STATE_YET_TO_BE_CONSUMED" - Yet to be consumed.
	//   "CONSUMPTION_STATE_CONSUMED" - Consumed already.
	ConsumptionState string `json:"consumptionState,omitempty"`
	// OfferId: The offer ID. Only present for offers.
	OfferId string `json:"offerId,omitempty"`
	// OfferTags: The latest offer tags associated with the offer. It includes tags
	// inherited from the purchase option.
	OfferTags []string `json:"offerTags,omitempty"`
	// OfferToken: The per-transaction offer token used to make this purchase line
	// item.
	OfferToken string `json:"offerToken,omitempty"`
	// PreorderOfferDetails: Offer details for a preorder offer. This will only be
	// set for preorders.
	PreorderOfferDetails *PreorderOfferDetails `json:"preorderOfferDetails,omitempty"`
	// PurchaseOptionId: The purchase option ID.
	PurchaseOptionId string `json:"purchaseOptionId,omitempty"`
	// Quantity: The quantity associated with the purchase of the inapp product.
	Quantity int64 `json:"quantity,omitempty"`
	// RefundableQuantity: The quantity eligible for refund, i.e. quantity that
	// hasn't been refunded. The value reflects quantity-based partial refunds and
	// full refunds.
	RefundableQuantity int64 `json:"refundableQuantity,omitempty"`
	// RentOfferDetails: Offer details about rent offers. This will only be set for
	// rental line items.
	RentOfferDetails *RentOfferDetails `json:"rentOfferDetails,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConsumptionState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConsumptionState") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductOfferDetails: Offer details information related to a purchase line item.

func (ProductOfferDetails) MarshalJSON ¶
added in v0.240.0
func (s ProductOfferDetails) MarshalJSON() ([]byte, error)
type ProductPurchase ¶
type ProductPurchase struct {
	// AcknowledgementState: The acknowledgement state of the inapp product.
	// Possible values are: 0. Yet to be acknowledged 1. Acknowledged
	AcknowledgementState int64 `json:"acknowledgementState,omitempty"`
	// ConsumptionState: The consumption state of the inapp product. Possible
	// values are: 0. Yet to be consumed 1. Consumed
	ConsumptionState int64 `json:"consumptionState,omitempty"`
	// DeveloperPayload: A developer-specified string that contains supplemental
	// information about an order.
	DeveloperPayload string `json:"developerPayload,omitempty"`
	// Kind: This kind represents an inappPurchase object in the androidpublisher
	// service.
	Kind string `json:"kind,omitempty"`
	// ObfuscatedExternalAccountId: An obfuscated version of the id that is
	// uniquely associated with the user's account in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid
	// when the purchase was made.
	ObfuscatedExternalAccountId string `json:"obfuscatedExternalAccountId,omitempty"`
	// ObfuscatedExternalProfileId: An obfuscated version of the id that is
	// uniquely associated with the user's profile in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid
	// when the purchase was made.
	ObfuscatedExternalProfileId string `json:"obfuscatedExternalProfileId,omitempty"`
	// OrderId: The order id associated with the purchase of the inapp product.
	OrderId string `json:"orderId,omitempty"`
	// ProductId: The inapp product SKU. May not be present.
	ProductId string `json:"productId,omitempty"`
	// PurchaseState: The purchase state of the order. Possible values are: 0.
	// Purchased 1. Canceled 2. Pending
	PurchaseState int64 `json:"purchaseState,omitempty"`
	// PurchaseTimeMillis: The time the product was purchased, in milliseconds
	// since the epoch (Jan 1, 1970).
	PurchaseTimeMillis int64 `json:"purchaseTimeMillis,omitempty,string"`
	// PurchaseToken: The purchase token generated to identify this purchase. May
	// not be present.
	PurchaseToken string `json:"purchaseToken,omitempty"`
	// PurchaseType: The type of purchase of the inapp product. This field is only
	// set if this purchase was not made using the standard in-app billing flow.
	// Possible values are: 0. Test (i.e. purchased from a license testing account)
	// 1. Promo (i.e. purchased using a promo code). Does not include Play Points
	// purchases. 2. Rewarded (i.e. from watching a video ad instead of paying)
	PurchaseType *int64 `json:"purchaseType,omitempty"`
	// Quantity: The quantity associated with the purchase of the inapp product. If
	// not present, the quantity is 1.
	Quantity int64 `json:"quantity,omitempty"`
	// RefundableQuantity: The quantity eligible for refund, i.e. quantity that
	// hasn't been refunded. The value reflects quantity-based partial refunds and
	// full refunds.
	RefundableQuantity int64 `json:"refundableQuantity,omitempty"`
	// RegionCode: ISO 3166-1 alpha-2 billing region code of the user at the time
	// the product was granted.
	RegionCode string `json:"regionCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AcknowledgementState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcknowledgementState") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPurchase: A ProductPurchase resource indicates the status of a user's inapp product purchase.

func (ProductPurchase) MarshalJSON ¶
func (s ProductPurchase) MarshalJSON() ([]byte, error)
type ProductPurchaseV2 ¶
added in v0.240.0
type ProductPurchaseV2 struct {
	// AcknowledgementState: Output only. The acknowledgement state of the
	// purchase.
	//
	// Possible values:
	//   "ACKNOWLEDGEMENT_STATE_UNSPECIFIED" - Unspecified acknowledgement state.
	//   "ACKNOWLEDGEMENT_STATE_PENDING" - The purchase is not acknowledged yet.
	//   "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED" - The purchase is acknowledged.
	AcknowledgementState string `json:"acknowledgementState,omitempty"`
	// Kind: This kind represents a ProductPurchaseV2 object in the
	// androidpublisher service.
	Kind string `json:"kind,omitempty"`
	// ObfuscatedExternalAccountId: An obfuscated version of the id that is
	// uniquely associated with the user's account in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid
	// when the purchase was made.
	ObfuscatedExternalAccountId string `json:"obfuscatedExternalAccountId,omitempty"`
	// ObfuscatedExternalProfileId: An obfuscated version of the id that is
	// uniquely associated with the user's profile in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid
	// when the purchase was made.
	ObfuscatedExternalProfileId string `json:"obfuscatedExternalProfileId,omitempty"`
	// OrderId: The order id associated with the purchase of the inapp product. May
	// not be set if there is no order associated with the purchase.
	OrderId string `json:"orderId,omitempty"`
	// ProductLineItem: Contains item-level info for a ProductPurchaseV2.
	ProductLineItem []*ProductLineItem `json:"productLineItem,omitempty"`
	// PurchaseCompletionTime: The time when the purchase was successful, i.e.,
	// when the PurchaseState has changed to PURCHASED. This field will not be
	// present until the payment is complete. For example, if the user initiated a
	// pending transaction
	// (https://developer.android.com/google/play/billing/integrate#pending), this
	// field will not be populated until the user successfully completes the steps
	// required to complete the transaction.
	PurchaseCompletionTime string `json:"purchaseCompletionTime,omitempty"`
	// PurchaseStateContext: Information about the purchase state of the purchase.
	PurchaseStateContext *PurchaseStateContext `json:"purchaseStateContext,omitempty"`
	// RegionCode: ISO 3166-1 alpha-2 billing region code of the user at the time
	// the product was granted.
	RegionCode string `json:"regionCode,omitempty"`
	// TestPurchaseContext: Information related to test purchases. This will only
	// be set for test purchases.
	TestPurchaseContext *TestPurchaseContext `json:"testPurchaseContext,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AcknowledgementState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcknowledgementState") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPurchaseV2: A ProductPurchaseV2 resource indicates the status of a user's inapp product purchase.

func (ProductPurchaseV2) MarshalJSON ¶
added in v0.240.0
func (s ProductPurchaseV2) MarshalJSON() ([]byte, error)
type ProductPurchasesAcknowledgeRequest ¶
added in v0.6.0
type ProductPurchasesAcknowledgeRequest struct {
	// DeveloperPayload: Payload to attach to the purchase.
	DeveloperPayload string `json:"developerPayload,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeveloperPayload") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeveloperPayload") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProductPurchasesAcknowledgeRequest: Request for the product.purchases.acknowledge API.

func (ProductPurchasesAcknowledgeRequest) MarshalJSON ¶
added in v0.6.0
func (s ProductPurchasesAcknowledgeRequest) MarshalJSON() ([]byte, error)
type ProrationPeriodDetails ¶
added in v0.257.0
type ProrationPeriodDetails struct {
	// OriginalOfferPhase: Represent the original offer phase from the purchased
	// the line item if the proration period contains any of them. For example, a
	// proration period from CHARGE_FULL_PRICE plan change may merge the 1st offer
	// phase of the subscription offer of the new product user purchased. In this
	// case, the original offer phase will be set here.
	//
	// Possible values:
	//   "OFFER_PHASE_UNSPECIFIED" - Offer phase unspecified. This value is not
	// used.
	//   "BASE" - The order funds a base price period.
	//   "INTRODUCTORY" - The order funds an introductory pricing period.
	//   "FREE_TRIAL" - The order funds a free trial period.
	OriginalOfferPhase string `json:"originalOfferPhase,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OriginalOfferPhase") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OriginalOfferPhase") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProrationPeriodDetails: Details of a proration period. A proration period can be a period calculated during a plan change to cover existing entitlements (For more information, see Allow users to upgrade, downgrade, or change their subscription (https://developer.android.com/google/play/billing/subscriptions#allow-users-change), or a prorated period to align add-on renewal dates with the base (For more information, see Rules applicable for items in the purchase (https://developer.android.com/google/play/billing/subscription-with-addons#rules-base-addons)).

func (ProrationPeriodDetails) MarshalJSON ¶
added in v0.257.0
func (s ProrationPeriodDetails) MarshalJSON() ([]byte, error)
type ProrationPeriodOfferPhase ¶
added in v0.265.0
type ProrationPeriodOfferPhase struct {
	// OriginalOfferPhaseType: The original offer phase type before the proration
	// period. Only set when the proration period is updated from an existing offer
	// phase.
	//
	// Possible values:
	//   "ORIGINAL_OFFER_PHASE_TYPE_UNSPECIFIED" - Unspecified original offer phase
	// type.
	//   "BASE" - The subscription is in the base pricing phase (e.g. full price).
	//   "INTRODUCTORY" - The subscription is in an introductory pricing phase.
	//   "FREE_TRIAL" - The subscription is in a free trial.
	OriginalOfferPhaseType string `json:"originalOfferPhaseType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OriginalOfferPhaseType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OriginalOfferPhaseType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProrationPeriodOfferPhase: Details about proration period offer phase.

func (ProrationPeriodOfferPhase) MarshalJSON ¶
added in v0.265.0
func (s ProrationPeriodOfferPhase) MarshalJSON() ([]byte, error)
type PurchaseOptionTaxAndComplianceSettings ¶
added in v0.244.0
type PurchaseOptionTaxAndComplianceSettings struct {
	// WithdrawalRightType: Optional. Digital content or service classification for
	// products distributed to users in eligible regions. If unset, it defaults to
	// `WITHDRAWAL_RIGHT_DIGITAL_CONTENT`. Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/10463498)
	// for more information.
	//
	// Possible values:
	//   "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"
	//   "WITHDRAWAL_RIGHT_DIGITAL_CONTENT"
	//   "WITHDRAWAL_RIGHT_SERVICE"
	WithdrawalRightType string `json:"withdrawalRightType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "WithdrawalRightType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "WithdrawalRightType") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PurchaseOptionTaxAndComplianceSettings: Details about taxation, Google Play policy and legal compliance for one-time product purchase options.

func (PurchaseOptionTaxAndComplianceSettings) MarshalJSON ¶
added in v0.244.0
func (s PurchaseOptionTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type PurchaseStateContext ¶
added in v0.240.0
type PurchaseStateContext struct {
	// PurchaseState: Output only. The purchase state of the purchase.
	//
	// Possible values:
	//   "PURCHASE_STATE_UNSPECIFIED" - Purchase state unspecified. This value
	// should never be set.
	//   "PURCHASED" - Purchased successfully.
	//   "CANCELLED" - Purchase canceled.
	//   "PENDING" - The purchase is in a pending state and has not yet been
	// completed. For more information on handling pending purchases, see
	// https://developer.android.com/google/play/billing/integrate#pending.
	PurchaseState string `json:"purchaseState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PurchaseState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PurchaseState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PurchaseStateContext: Context about the purchase state.

func (PurchaseStateContext) MarshalJSON ¶
added in v0.240.0
func (s PurchaseStateContext) MarshalJSON() ([]byte, error)
type PurchasesProductsAcknowledgeCall ¶
added in v0.6.0
type PurchasesProductsAcknowledgeCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesProductsAcknowledgeCall) Context ¶
added in v0.6.0
func (c *PurchasesProductsAcknowledgeCall) Context(ctx context.Context) *PurchasesProductsAcknowledgeCall

Context sets the context to be used in this call's Do method.

func (*PurchasesProductsAcknowledgeCall) Do ¶
added in v0.6.0
func (c *PurchasesProductsAcknowledgeCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.products.acknowledge" call.

func (*PurchasesProductsAcknowledgeCall) Fields ¶
added in v0.6.0
func (c *PurchasesProductsAcknowledgeCall) Fields(s ...googleapi.Field) *PurchasesProductsAcknowledgeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesProductsAcknowledgeCall) Header ¶
added in v0.6.0
func (c *PurchasesProductsAcknowledgeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesProductsConsumeCall ¶
added in v0.114.0
type PurchasesProductsConsumeCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesProductsConsumeCall) Context ¶
added in v0.114.0
func (c *PurchasesProductsConsumeCall) Context(ctx context.Context) *PurchasesProductsConsumeCall

Context sets the context to be used in this call's Do method.

func (*PurchasesProductsConsumeCall) Do ¶
added in v0.114.0
func (c *PurchasesProductsConsumeCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.products.consume" call.

func (*PurchasesProductsConsumeCall) Fields ¶
added in v0.114.0
func (c *PurchasesProductsConsumeCall) Fields(s ...googleapi.Field) *PurchasesProductsConsumeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesProductsConsumeCall) Header ¶
added in v0.114.0
func (c *PurchasesProductsConsumeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesProductsGetCall ¶
type PurchasesProductsGetCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesProductsGetCall) Context ¶
func (c *PurchasesProductsGetCall) Context(ctx context.Context) *PurchasesProductsGetCall

Context sets the context to be used in this call's Do method.

func (*PurchasesProductsGetCall) Do ¶
func (c *PurchasesProductsGetCall) Do(opts ...googleapi.CallOption) (*ProductPurchase, error)

Do executes the "androidpublisher.purchases.products.get" call. Any non-2xx status code is an error. Response headers are in either *ProductPurchase.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesProductsGetCall) Fields ¶
func (c *PurchasesProductsGetCall) Fields(s ...googleapi.Field) *PurchasesProductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesProductsGetCall) Header ¶
func (c *PurchasesProductsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PurchasesProductsGetCall) IfNoneMatch ¶
func (c *PurchasesProductsGetCall) IfNoneMatch(entityTag string) *PurchasesProductsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PurchasesProductsService ¶
type PurchasesProductsService struct {
	// contains filtered or unexported fields
}
func NewPurchasesProductsService ¶
func NewPurchasesProductsService(s *Service) *PurchasesProductsService
func (*PurchasesProductsService) Acknowledge ¶
added in v0.6.0
func (r *PurchasesProductsService) Acknowledge(packageName string, productId string, token string, productpurchasesacknowledgerequest *ProductPurchasesAcknowledgeRequest) *PurchasesProductsAcknowledgeCall

Acknowledge: Acknowledges a purchase of an inapp item.

packageName: The package name of the application the inapp product was sold in (for example, 'com.some.thing').
productId: The inapp product SKU (for example, 'com.some.thing.inapp1').
token: The token provided to the user's device when the inapp product was purchased.
func (*PurchasesProductsService) Consume ¶
added in v0.114.0
func (r *PurchasesProductsService) Consume(packageName string, productId string, token string) *PurchasesProductsConsumeCall

Consume: Consumes a purchase for an inapp item.

packageName: The package name of the application the inapp product was sold in (for example, 'com.some.thing').
productId: The inapp product SKU (for example, 'com.some.thing.inapp1').
token: The token provided to the user's device when the inapp product was purchased.
func (*PurchasesProductsService) Get ¶
func (r *PurchasesProductsService) Get(packageName string, productId string, token string) *PurchasesProductsGetCall

Get: Checks the purchase and consumption status of an inapp item.

packageName: The package name of the application the inapp product was sold in (for example, 'com.some.thing').
productId: The inapp product SKU (for example, 'com.some.thing.inapp1').
token: The token provided to the user's device when the inapp product was purchased.
type PurchasesProductsv2Getproductpurchasev2Call ¶
added in v0.240.0
type PurchasesProductsv2Getproductpurchasev2Call struct {
	// contains filtered or unexported fields
}
func (*PurchasesProductsv2Getproductpurchasev2Call) Context ¶
added in v0.240.0
func (c *PurchasesProductsv2Getproductpurchasev2Call) Context(ctx context.Context) *PurchasesProductsv2Getproductpurchasev2Call

Context sets the context to be used in this call's Do method.

func (*PurchasesProductsv2Getproductpurchasev2Call) Do ¶
added in v0.240.0
func (c *PurchasesProductsv2Getproductpurchasev2Call) Do(opts ...googleapi.CallOption) (*ProductPurchaseV2, error)

Do executes the "androidpublisher.purchases.productsv2.getproductpurchasev2" call. Any non-2xx status code is an error. Response headers are in either *ProductPurchaseV2.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesProductsv2Getproductpurchasev2Call) Fields ¶
added in v0.240.0
func (c *PurchasesProductsv2Getproductpurchasev2Call) Fields(s ...googleapi.Field) *PurchasesProductsv2Getproductpurchasev2Call

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesProductsv2Getproductpurchasev2Call) Header ¶
added in v0.240.0
func (c *PurchasesProductsv2Getproductpurchasev2Call) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PurchasesProductsv2Getproductpurchasev2Call) IfNoneMatch ¶
added in v0.240.0
func (c *PurchasesProductsv2Getproductpurchasev2Call) IfNoneMatch(entityTag string) *PurchasesProductsv2Getproductpurchasev2Call

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PurchasesProductsv2Service ¶
added in v0.240.0
type PurchasesProductsv2Service struct {
	// contains filtered or unexported fields
}
func NewPurchasesProductsv2Service ¶
added in v0.240.0
func NewPurchasesProductsv2Service(s *Service) *PurchasesProductsv2Service
func (*PurchasesProductsv2Service) Getproductpurchasev2 ¶
added in v0.240.0
func (r *PurchasesProductsv2Service) Getproductpurchasev2(packageName string, token string) *PurchasesProductsv2Getproductpurchasev2Call

Getproductpurchasev2: Checks the purchase and consumption status of an inapp item.

packageName: The package name of the application the inapp product was sold in (for example, 'com.some.thing').
token: The token provided to the user's device when the inapp product was purchased.
type PurchasesService ¶
type PurchasesService struct {
	Products *PurchasesProductsService

	Productsv2 *PurchasesProductsv2Service

	Subscriptions *PurchasesSubscriptionsService

	Subscriptionsv2 *PurchasesSubscriptionsv2Service

	Voidedpurchases *PurchasesVoidedpurchasesService
	// contains filtered or unexported fields
}
func NewPurchasesService ¶
func NewPurchasesService(s *Service) *PurchasesService
type PurchasesSubscriptionsAcknowledgeCall ¶
added in v0.6.0
type PurchasesSubscriptionsAcknowledgeCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsAcknowledgeCall) Context ¶
added in v0.6.0
func (c *PurchasesSubscriptionsAcknowledgeCall) Context(ctx context.Context) *PurchasesSubscriptionsAcknowledgeCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsAcknowledgeCall) Do ¶
added in v0.6.0
func (c *PurchasesSubscriptionsAcknowledgeCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.subscriptions.acknowledge" call.

func (*PurchasesSubscriptionsAcknowledgeCall) Fields ¶
added in v0.6.0
func (c *PurchasesSubscriptionsAcknowledgeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsAcknowledgeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsAcknowledgeCall) Header ¶
added in v0.6.0
func (c *PurchasesSubscriptionsAcknowledgeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsCancelCall ¶
type PurchasesSubscriptionsCancelCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsCancelCall) Context ¶
func (c *PurchasesSubscriptionsCancelCall) Context(ctx context.Context) *PurchasesSubscriptionsCancelCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsCancelCall) Do ¶
func (c *PurchasesSubscriptionsCancelCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.subscriptions.cancel" call.

func (*PurchasesSubscriptionsCancelCall) Fields ¶
func (c *PurchasesSubscriptionsCancelCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsCancelCall) Header ¶
func (c *PurchasesSubscriptionsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsDeferCall ¶
type PurchasesSubscriptionsDeferCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsDeferCall) Context ¶
func (c *PurchasesSubscriptionsDeferCall) Context(ctx context.Context) *PurchasesSubscriptionsDeferCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsDeferCall) Do ¶
func (c *PurchasesSubscriptionsDeferCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchasesDeferResponse, error)

Do executes the "androidpublisher.purchases.subscriptions.defer" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionPurchasesDeferResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsDeferCall) Fields ¶
func (c *PurchasesSubscriptionsDeferCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsDeferCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsDeferCall) Header ¶
func (c *PurchasesSubscriptionsDeferCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsGetCall ¶
type PurchasesSubscriptionsGetCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsGetCall) Context ¶
func (c *PurchasesSubscriptionsGetCall) Context(ctx context.Context) *PurchasesSubscriptionsGetCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsGetCall) Do ¶
func (c *PurchasesSubscriptionsGetCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchase, error)

Do executes the "androidpublisher.purchases.subscriptions.get" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionPurchase.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsGetCall) Fields ¶
func (c *PurchasesSubscriptionsGetCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsGetCall) Header ¶
func (c *PurchasesSubscriptionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PurchasesSubscriptionsGetCall) IfNoneMatch ¶
func (c *PurchasesSubscriptionsGetCall) IfNoneMatch(entityTag string) *PurchasesSubscriptionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PurchasesSubscriptionsRefundCall ¶
type PurchasesSubscriptionsRefundCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsRefundCall) Context ¶
func (c *PurchasesSubscriptionsRefundCall) Context(ctx context.Context) *PurchasesSubscriptionsRefundCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsRefundCall) Do ¶
func (c *PurchasesSubscriptionsRefundCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.subscriptions.refund" call.

func (*PurchasesSubscriptionsRefundCall) Fields ¶
func (c *PurchasesSubscriptionsRefundCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsRefundCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsRefundCall) Header ¶
func (c *PurchasesSubscriptionsRefundCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsRevokeCall ¶
type PurchasesSubscriptionsRevokeCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsRevokeCall) Context ¶
func (c *PurchasesSubscriptionsRevokeCall) Context(ctx context.Context) *PurchasesSubscriptionsRevokeCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsRevokeCall) Do ¶
func (c *PurchasesSubscriptionsRevokeCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.purchases.subscriptions.revoke" call.

func (*PurchasesSubscriptionsRevokeCall) Fields ¶
func (c *PurchasesSubscriptionsRevokeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsRevokeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsRevokeCall) Header ¶
func (c *PurchasesSubscriptionsRevokeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsService ¶
type PurchasesSubscriptionsService struct {
	// contains filtered or unexported fields
}
func NewPurchasesSubscriptionsService ¶
func NewPurchasesSubscriptionsService(s *Service) *PurchasesSubscriptionsService
func (*PurchasesSubscriptionsService) Acknowledge ¶
added in v0.6.0
func (r *PurchasesSubscriptionsService) Acknowledge(packageName string, subscriptionId string, token string, subscriptionpurchasesacknowledgerequest *SubscriptionPurchasesAcknowledgeRequest) *PurchasesSubscriptionsAcknowledgeCall

Acknowledge: Acknowledges a subscription purchase.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: Note: Since May 21, 2025, subscription_id is not required, and not recommended for subscription with add-ons. The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsService) Cancel ¶
func (r *PurchasesSubscriptionsService) Cancel(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsCancelCall

Cancel: Cancels a user's subscription purchase. The subscription remains valid until its expiration time. Newer version is available at purchases.subscriptionsv2.cancel for better client library support.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: Note: Since May 21, 2025, subscription_id is not required, and not recommended for subscription with add-ons. The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsService) Defer ¶
func (r *PurchasesSubscriptionsService) Defer(packageName string, subscriptionId string, token string, subscriptionpurchasesdeferrequest *SubscriptionPurchasesDeferRequest) *PurchasesSubscriptionsDeferCall

Defer: Defers a user's subscription purchase until a specified future expiration time.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsService) Get ¶
func (r *PurchasesSubscriptionsService) Get(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsGetCall

Get: Deprecated: Use purchases.subscriptionsv2.get instead. Checks whether a user's subscription purchase is valid and returns its expiry time.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsService) Refund ¶
func (r *PurchasesSubscriptionsService) Refund(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsRefundCall

Refund: Deprecated: Use orders.refund instead. Refunds a user's subscription purchase, but the subscription remains valid until its expiration time and it will continue to recur.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: "The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsService) Revoke ¶
func (r *PurchasesSubscriptionsService) Revoke(packageName string, subscriptionId string, token string) *PurchasesSubscriptionsRevokeCall

Revoke: Deprecated: Use purchases.subscriptionsv2.revoke instead. Refunds and immediately revokes a user's subscription purchase. Access to the subscription will be terminated immediately and it will stop recurring.

packageName: The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
subscriptionId: The purchased subscription ID (for example, 'monthly001').
token: The token provided to the user's device when the subscription was purchased.
type PurchasesSubscriptionsv2CancelCall ¶
added in v0.249.0
type PurchasesSubscriptionsv2CancelCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsv2CancelCall) Context ¶
added in v0.249.0
func (c *PurchasesSubscriptionsv2CancelCall) Context(ctx context.Context) *PurchasesSubscriptionsv2CancelCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsv2CancelCall) Do ¶
added in v0.249.0
func (c *PurchasesSubscriptionsv2CancelCall) Do(opts ...googleapi.CallOption) (*CancelSubscriptionPurchaseResponse, error)

Do executes the "androidpublisher.purchases.subscriptionsv2.cancel" call. Any non-2xx status code is an error. Response headers are in either *CancelSubscriptionPurchaseResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsv2CancelCall) Fields ¶
added in v0.249.0
func (c *PurchasesSubscriptionsv2CancelCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2CancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsv2CancelCall) Header ¶
added in v0.249.0
func (c *PurchasesSubscriptionsv2CancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsv2DeferCall ¶
added in v0.265.0
type PurchasesSubscriptionsv2DeferCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsv2DeferCall) Context ¶
added in v0.265.0
func (c *PurchasesSubscriptionsv2DeferCall) Context(ctx context.Context) *PurchasesSubscriptionsv2DeferCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsv2DeferCall) Do ¶
added in v0.265.0
func (c *PurchasesSubscriptionsv2DeferCall) Do(opts ...googleapi.CallOption) (*DeferSubscriptionPurchaseResponse, error)

Do executes the "androidpublisher.purchases.subscriptionsv2.defer" call. Any non-2xx status code is an error. Response headers are in either *DeferSubscriptionPurchaseResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsv2DeferCall) Fields ¶
added in v0.265.0
func (c *PurchasesSubscriptionsv2DeferCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2DeferCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsv2DeferCall) Header ¶
added in v0.265.0
func (c *PurchasesSubscriptionsv2DeferCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsv2GetCall ¶
added in v0.80.0
type PurchasesSubscriptionsv2GetCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsv2GetCall) Context ¶
added in v0.80.0
func (c *PurchasesSubscriptionsv2GetCall) Context(ctx context.Context) *PurchasesSubscriptionsv2GetCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsv2GetCall) Do ¶
added in v0.80.0
func (c *PurchasesSubscriptionsv2GetCall) Do(opts ...googleapi.CallOption) (*SubscriptionPurchaseV2, error)

Do executes the "androidpublisher.purchases.subscriptionsv2.get" call. Any non-2xx status code is an error. Response headers are in either *SubscriptionPurchaseV2.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsv2GetCall) Fields ¶
added in v0.80.0
func (c *PurchasesSubscriptionsv2GetCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2GetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsv2GetCall) Header ¶
added in v0.80.0
func (c *PurchasesSubscriptionsv2GetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PurchasesSubscriptionsv2GetCall) IfNoneMatch ¶
added in v0.80.0
func (c *PurchasesSubscriptionsv2GetCall) IfNoneMatch(entityTag string) *PurchasesSubscriptionsv2GetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PurchasesSubscriptionsv2RevokeCall ¶
added in v0.157.0
type PurchasesSubscriptionsv2RevokeCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesSubscriptionsv2RevokeCall) Context ¶
added in v0.157.0
func (c *PurchasesSubscriptionsv2RevokeCall) Context(ctx context.Context) *PurchasesSubscriptionsv2RevokeCall

Context sets the context to be used in this call's Do method.

func (*PurchasesSubscriptionsv2RevokeCall) Do ¶
added in v0.157.0
func (c *PurchasesSubscriptionsv2RevokeCall) Do(opts ...googleapi.CallOption) (*RevokeSubscriptionPurchaseResponse, error)

Do executes the "androidpublisher.purchases.subscriptionsv2.revoke" call. Any non-2xx status code is an error. Response headers are in either *RevokeSubscriptionPurchaseResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesSubscriptionsv2RevokeCall) Fields ¶
added in v0.157.0
func (c *PurchasesSubscriptionsv2RevokeCall) Fields(s ...googleapi.Field) *PurchasesSubscriptionsv2RevokeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesSubscriptionsv2RevokeCall) Header ¶
added in v0.157.0
func (c *PurchasesSubscriptionsv2RevokeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PurchasesSubscriptionsv2Service ¶
added in v0.80.0
type PurchasesSubscriptionsv2Service struct {
	// contains filtered or unexported fields
}
func NewPurchasesSubscriptionsv2Service ¶
added in v0.80.0
func NewPurchasesSubscriptionsv2Service(s *Service) *PurchasesSubscriptionsv2Service
func (*PurchasesSubscriptionsv2Service) Cancel ¶
added in v0.249.0
func (r *PurchasesSubscriptionsv2Service) Cancel(packageName string, token string, cancelsubscriptionpurchaserequest *CancelSubscriptionPurchaseRequest) *PurchasesSubscriptionsv2CancelCall

Cancel: Cancel a subscription purchase for the user.

packageName: The package of the application for which this subscription was purchased (for example, 'com.some.thing').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsv2Service) Defer ¶
added in v0.265.0
func (r *PurchasesSubscriptionsv2Service) Defer(packageName string, token string, defersubscriptionpurchaserequest *DeferSubscriptionPurchaseRequest) *PurchasesSubscriptionsv2DeferCall

Defer: Defers the renewal of a subscription.

packageName: The package of the application for which this subscription was purchased (for example, 'com.some.thing').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsv2Service) Get ¶
added in v0.80.0
func (r *PurchasesSubscriptionsv2Service) Get(packageName string, token string) *PurchasesSubscriptionsv2GetCall

Get: Get metadata about a subscription

packageName: The package of the application for which this subscription was purchased (for example, 'com.some.thing').
token: The token provided to the user's device when the subscription was purchased.
func (*PurchasesSubscriptionsv2Service) Revoke ¶
added in v0.157.0
func (r *PurchasesSubscriptionsv2Service) Revoke(packageName string, token string, revokesubscriptionpurchaserequest *RevokeSubscriptionPurchaseRequest) *PurchasesSubscriptionsv2RevokeCall

Revoke: Revoke a subscription purchase for the user.

packageName: The package of the application for which this subscription was purchased (for example, 'com.some.thing').
token: The token provided to the user's device when the subscription was purchased.
type PurchasesVoidedpurchasesListCall ¶
type PurchasesVoidedpurchasesListCall struct {
	// contains filtered or unexported fields
}
func (*PurchasesVoidedpurchasesListCall) Context ¶
func (c *PurchasesVoidedpurchasesListCall) Context(ctx context.Context) *PurchasesVoidedpurchasesListCall

Context sets the context to be used in this call's Do method.

func (*PurchasesVoidedpurchasesListCall) Do ¶
func (c *PurchasesVoidedpurchasesListCall) Do(opts ...googleapi.CallOption) (*VoidedPurchasesListResponse, error)

Do executes the "androidpublisher.purchases.voidedpurchases.list" call. Any non-2xx status code is an error. Response headers are in either *VoidedPurchasesListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PurchasesVoidedpurchasesListCall) EndTime ¶
func (c *PurchasesVoidedpurchasesListCall) EndTime(endTime int64) *PurchasesVoidedpurchasesListCall

EndTime sets the optional parameter "endTime": The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.

func (*PurchasesVoidedpurchasesListCall) Fields ¶
func (c *PurchasesVoidedpurchasesListCall) Fields(s ...googleapi.Field) *PurchasesVoidedpurchasesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PurchasesVoidedpurchasesListCall) Header ¶
func (c *PurchasesVoidedpurchasesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PurchasesVoidedpurchasesListCall) IfNoneMatch ¶
func (c *PurchasesVoidedpurchasesListCall) IfNoneMatch(entityTag string) *PurchasesVoidedpurchasesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PurchasesVoidedpurchasesListCall) IncludeQuantityBasedPartialRefund ¶
added in v0.171.0
func (c *PurchasesVoidedpurchasesListCall) IncludeQuantityBasedPartialRefund(includeQuantityBasedPartialRefund bool) *PurchasesVoidedpurchasesListCall

IncludeQuantityBasedPartialRefund sets the optional parameter "includeQuantityBasedPartialRefund": Whether to include voided purchases of quantity-based partial refunds, which are applicable only to multi-quantity purchases. If true, additional voided purchases may be returned with voidedQuantity that indicates the refund quantity of a quantity-based partial refund. The default value is false.

func (*PurchasesVoidedpurchasesListCall) MaxResults ¶
func (c *PurchasesVoidedpurchasesListCall) MaxResults(maxResults int64) *PurchasesVoidedpurchasesListCall

MaxResults sets the optional parameter "maxResults": Defines how many results the list operation should return. The default number depends on the resource collection.

func (*PurchasesVoidedpurchasesListCall) StartIndex ¶
func (c *PurchasesVoidedpurchasesListCall) StartIndex(startIndex int64) *PurchasesVoidedpurchasesListCall

StartIndex sets the optional parameter "startIndex": Defines the index of the first element to return. This can only be used if indexed paging is enabled.

func (*PurchasesVoidedpurchasesListCall) StartTime ¶
func (c *PurchasesVoidedpurchasesListCall) StartTime(startTime int64) *PurchasesVoidedpurchasesListCall

StartTime sets the optional parameter "startTime": The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.

func (*PurchasesVoidedpurchasesListCall) Token ¶
func (c *PurchasesVoidedpurchasesListCall) Token(token string) *PurchasesVoidedpurchasesListCall

Token sets the optional parameter "token": Defines the token of the page to return, usually taken from TokenPagination. This can only be used if token paging is enabled.

func (*PurchasesVoidedpurchasesListCall) Type ¶
added in v0.9.0
func (c *PurchasesVoidedpurchasesListCall) Type(type_ int64) *PurchasesVoidedpurchasesListCall

Type sets the optional parameter "type": The type of voided purchases that you want to see in the response. Possible values are: 0. Only voided in-app product purchases will be returned in the response. This is the default value. 1. Both voided in-app purchases and voided subscription purchases will be returned in the response. Note: Before requesting to receive voided subscription purchases, you must switch to use orderId in the response which uniquely identifies one-time purchases and subscriptions. Otherwise, you will receive multiple subscription orders with the same PurchaseToken, because subscription renewal orders share the same PurchaseToken.

type PurchasesVoidedpurchasesService ¶
type PurchasesVoidedpurchasesService struct {
	// contains filtered or unexported fields
}
func NewPurchasesVoidedpurchasesService ¶
func NewPurchasesVoidedpurchasesService(s *Service) *PurchasesVoidedpurchasesService
func (*PurchasesVoidedpurchasesService) List ¶
func (r *PurchasesVoidedpurchasesService) List(packageName string) *PurchasesVoidedpurchasesListCall

List: Lists the purchases that were canceled, refunded or charged-back.

packageName: The package name of the application for which voided purchases need to be returned (for example, 'com.some.thing').
type RecurringExternalTransaction ¶
added in v0.117.0
type RecurringExternalTransaction struct {
	// ExternalSubscription: Details of an external subscription.
	ExternalSubscription *ExternalSubscription `json:"externalSubscription,omitempty"`
	// ExternalTransactionToken: Input only. Provided during the call to Create.
	// Retrieved from the client when the alternative billing flow is launched.
	// Required only for the initial purchase.
	ExternalTransactionToken string `json:"externalTransactionToken,omitempty"`
	// InitialExternalTransactionId: The external transaction id of the first
	// transaction of this recurring series of transactions. For example, for a
	// subscription this would be the transaction id of the first payment. Required
	// when creating recurring external transactions.
	InitialExternalTransactionId string `json:"initialExternalTransactionId,omitempty"`
	// MigratedTransactionProgram: Input only. Provided during the call to Create.
	// Must only be used when migrating a subscription from manual monthly
	// reporting to automated reporting.
	//
	// Possible values:
	//   "EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED" - Unspecified transaction
	// program. Not used.
	//   "USER_CHOICE_BILLING" - User choice billing, where a user may choose
	// between Google Play Billing developer-managed billing.
	//   "ALTERNATIVE_BILLING_ONLY" - Alternative billing only, where users may
	// only use developer-manager billing.
	MigratedTransactionProgram string `json:"migratedTransactionProgram,omitempty"`
	// OtherRecurringProduct: Details of a recurring external transaction product
	// which doesn't belong to any other specific category.
	OtherRecurringProduct *OtherRecurringProduct `json:"otherRecurringProduct,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalSubscription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalSubscription") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RecurringExternalTransaction: Represents a transaction that is part of a recurring series of payments. This can be a subscription or a one-time product with multiple payments (such as preorder).

func (RecurringExternalTransaction) MarshalJSON ¶
added in v0.117.0
func (s RecurringExternalTransaction) MarshalJSON() ([]byte, error)
type RefundDetails ¶
added in v0.234.0
type RefundDetails struct {
	// Tax: The amount of tax refunded.
	Tax *Money `json:"tax,omitempty"`
	// Total: The total amount refunded, including tax.
	Total *Money `json:"total,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Tax") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Tax") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RefundDetails: Details for a partial or full refund.

func (RefundDetails) MarshalJSON ¶
added in v0.234.0
func (s RefundDetails) MarshalJSON() ([]byte, error)
type RefundEvent ¶
added in v0.234.0
type RefundEvent struct {
	// EventTime: The time when the order was fully refunded.
	EventTime string `json:"eventTime,omitempty"`
	// RefundDetails: Details for the full refund.
	RefundDetails *RefundDetails `json:"refundDetails,omitempty"`
	// RefundReason: The reason the order was refunded.
	//
	// Possible values:
	//   "REFUND_REASON_UNSPECIFIED" - Refund reason unspecified. This value is not
	// used.
	//   "OTHER" - The order was refunded for a reason other than the listed
	// reasons here.
	//   "CHARGEBACK" - The order was charged back.
	RefundReason string `json:"refundReason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RefundEvent: Details of when the order was fully refunded.

func (RefundEvent) MarshalJSON ¶
added in v0.234.0
func (s RefundEvent) MarshalJSON() ([]byte, error)
type RefundExternalTransactionRequest ¶
added in v0.117.0
type RefundExternalTransactionRequest struct {
	// FullRefund: A full-amount refund.
	FullRefund *FullRefund `json:"fullRefund,omitempty"`
	// PartialRefund: A partial refund.
	PartialRefund *PartialRefund `json:"partialRefund,omitempty"`
	// RefundTime: Required. The time that the transaction was refunded.
	RefundTime string `json:"refundTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FullRefund") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FullRefund") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RefundExternalTransactionRequest: A request to refund an existing external transaction.

func (RefundExternalTransactionRequest) MarshalJSON ¶
added in v0.117.0
func (s RefundExternalTransactionRequest) MarshalJSON() ([]byte, error)
type RegionalBasePlanConfig ¶
added in v0.80.0
type RegionalBasePlanConfig struct {
	// NewSubscriberAvailability: Whether the base plan in the specified region is
	// available for new subscribers. Existing subscribers will not have their
	// subscription canceled if this value is set to false. If not specified, this
	// will default to false.
	NewSubscriberAvailability bool `json:"newSubscriberAvailability,omitempty"`
	// Price: The price of the base plan in the specified region. Must be set if
	// the base plan is available to new subscribers. Must be set in the currency
	// that is linked to the specified region.
	Price *Money `json:"price,omitempty"`
	// RegionCode: Required. Region code this configuration applies to, as defined
	// by ISO 3166-2, e.g. "US".
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewSubscriberAvailability")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewSubscriberAvailability") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionalBasePlanConfig: Configuration for a base plan specific to a region.

func (RegionalBasePlanConfig) MarshalJSON ¶
added in v0.80.0
func (s RegionalBasePlanConfig) MarshalJSON() ([]byte, error)
type RegionalPriceMigrationConfig ¶
added in v0.80.0
type RegionalPriceMigrationConfig struct {
	// OldestAllowedPriceVersionTime: Required. Subscribers in all legacy price
	// cohorts before this time will be migrated to the current price. Subscribers
	// in any newer price cohorts are unaffected. Affected subscribers will receive
	// one or more notifications from Google Play about the price change. Price
	// decreases occur at the subscriber's next billing date. Price increases occur
	// at the subscriber's next billing date following a notification period that
	// varies by region and price increase type.
	OldestAllowedPriceVersionTime string `json:"oldestAllowedPriceVersionTime,omitempty"`
	// PriceIncreaseType: Optional. The requested type of price increase
	//
	// Possible values:
	//   "PRICE_INCREASE_TYPE_UNSPECIFIED" - Unspecified state.
	//   "PRICE_INCREASE_TYPE_OPT_IN" - Subscribers must accept the price increase
	// or their subscription is canceled.
	//   "PRICE_INCREASE_TYPE_OPT_OUT" - Subscribers are notified but do not have
	// to accept the price increase. Opt-out price increases not meeting regional,
	// frequency, and amount limits will proceed as opt-in price increase. The
	// first opt-out price increase for each app must be initiated in the Google
	// Play Console.
	PriceIncreaseType string `json:"priceIncreaseType,omitempty"`
	// RegionCode: Required. Region code this configuration applies to, as defined
	// by ISO 3166-2, e.g. "US".
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "OldestAllowedPriceVersionTime") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OldestAllowedPriceVersionTime")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionalPriceMigrationConfig: Configuration for migration of a legacy price cohort.

func (RegionalPriceMigrationConfig) MarshalJSON ¶
added in v0.80.0
func (s RegionalPriceMigrationConfig) MarshalJSON() ([]byte, error)
type RegionalProductAgeRatingInfo ¶
added in v0.260.0
type RegionalProductAgeRatingInfo struct {
	// ProductAgeRatingTier: The age rating tier of a product for the given region.
	//
	// Possible values:
	//   "PRODUCT_AGE_RATING_TIER_UNKNOWN" - Unknown age rating tier.
	//   "PRODUCT_AGE_RATING_TIER_EVERYONE" - Age rating tier for products that are
	// appropriate for all ages.
	//   "PRODUCT_AGE_RATING_TIER_THIRTEEN_AND_ABOVE" - Age rating tier for
	// products that are appropriate for 13 years and above.
	//   "PRODUCT_AGE_RATING_TIER_SIXTEEN_AND_ABOVE" - Age rating tier for products
	// that are appropriate for 16 years and above.
	//   "PRODUCT_AGE_RATING_TIER_EIGHTEEN_AND_ABOVE" - Age rating tier for
	// products that are appropriate for 18 years and above.
	ProductAgeRatingTier string `json:"productAgeRatingTier,omitempty"`
	// RegionCode: Region code this configuration applies to, as defined by ISO
	// 3166-2, e.g. "US".
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ProductAgeRatingTier") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProductAgeRatingTier") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionalProductAgeRatingInfo: Details about the age rating for a specific geographic region.

func (RegionalProductAgeRatingInfo) MarshalJSON ¶
added in v0.260.0
func (s RegionalProductAgeRatingInfo) MarshalJSON() ([]byte, error)
type RegionalSubscriptionOfferConfig ¶
added in v0.80.0
type RegionalSubscriptionOfferConfig struct {
	// NewSubscriberAvailability: Whether the subscription offer in the specified
	// region is available for new subscribers. Existing subscribers will not have
	// their subscription cancelled if this value is set to false. If not
	// specified, this will default to false.
	NewSubscriberAvailability bool `json:"newSubscriberAvailability,omitempty"`
	// RegionCode: Required. Immutable. Region code this configuration applies to,
	// as defined by ISO 3166-2, e.g. "US".
	RegionCode string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewSubscriberAvailability")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewSubscriberAvailability") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionalSubscriptionOfferConfig: Configuration for a subscription offer in a single region.

func (RegionalSubscriptionOfferConfig) MarshalJSON ¶
added in v0.80.0
func (s RegionalSubscriptionOfferConfig) MarshalJSON() ([]byte, error)
type RegionalSubscriptionOfferPhaseConfig ¶
added in v0.80.0
type RegionalSubscriptionOfferPhaseConfig struct {
	// AbsoluteDiscount: The absolute amount of money subtracted from the base plan
	// price prorated over the phase duration that the user pays for this offer
	// phase. For example, if the base plan price for this region is $12 for a
	// period of 1 year, then a $1 absolute discount for a phase of a duration of 3
	// months would correspond to a price of $2. The resulting price may not be
	// smaller than the minimum price allowed for this region.
	AbsoluteDiscount *Money `json:"absoluteDiscount,omitempty"`
	// Free: Set to specify this offer is free to obtain.
	Free *RegionalSubscriptionOfferPhaseFreePriceOverride `json:"free,omitempty"`
	// Price: The absolute price the user pays for this offer phase. The price must
	// not be smaller than the minimum price allowed for this region.
	Price *Money `json:"price,omitempty"`
	// RegionCode: Required. Immutable. The region to which this config applies.
	RegionCode string `json:"regionCode,omitempty"`
	// RelativeDiscount: The fraction of the base plan price prorated over the
	// phase duration that the user pays for this offer phase. For example, if the
	// base plan price for this region is $12 for a period of 1 year, then a 50%
	// discount for a phase of a duration of 3 months would correspond to a price
	// of $1.50. The discount must be specified as a fraction strictly larger than
	// 0 and strictly smaller than 1. The resulting price will be rounded to the
	// nearest billable unit (e.g. cents for USD). The relative discount is
	// considered invalid if the discounted price ends up being smaller than the
	// minimum price allowed in this region.
	RelativeDiscount float64 `json:"relativeDiscount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AbsoluteDiscount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbsoluteDiscount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionalSubscriptionOfferPhaseConfig: Configuration for a single phase of a subscription offer in a single region.

func (RegionalSubscriptionOfferPhaseConfig) MarshalJSON ¶
added in v0.80.0
func (s RegionalSubscriptionOfferPhaseConfig) MarshalJSON() ([]byte, error)
func (*RegionalSubscriptionOfferPhaseConfig) UnmarshalJSON ¶
added in v0.80.0
func (s *RegionalSubscriptionOfferPhaseConfig) UnmarshalJSON(data []byte) error
type RegionalSubscriptionOfferPhaseFreePriceOverride ¶
added in v0.175.0
type RegionalSubscriptionOfferPhaseFreePriceOverride struct {
}

RegionalSubscriptionOfferPhaseFreePriceOverride: Represents the free price override configuration for a single phase of a subscription offer

type RegionalTaxConfig ¶
added in v0.244.0
type RegionalTaxConfig struct {
	// EligibleForStreamingServiceTaxRate: You must tell us if your app contains
	// streaming products to correctly charge US state and local sales tax. Field
	// only supported in the United States.
	EligibleForStreamingServiceTaxRate bool `json:"eligibleForStreamingServiceTaxRate,omitempty"`
	// RegionCode: Required. Region code this configuration applies to, as defined
	// by ISO 3166-2, e.g. "US".
	RegionCode string `json:"regionCode,omitempty"`
	// StreamingTaxType: To collect communications or amusement taxes in the United
	// States, choose the appropriate tax category. Learn more
	// (https://support.google.com/googleplay/android-developer/answer/10463498#streaming_tax).
	//
	// Possible values:
	//   "STREAMING_TAX_TYPE_UNSPECIFIED" - No telecommunications tax collected.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL" - US-specific telecommunications
	// tax tier for video streaming, on demand, rentals / subscriptions /
	// pay-per-view.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_SALES" - US-specific telecommunications
	// tax tier for video streaming of pre-recorded content like movies, tv shows.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL" - US-specific
	// telecommunications tax tier for video streaming of multi-channel
	// programming.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL" - US-specific telecommunications
	// tax tier for audio streaming, rental / subscription.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_SALES" - US-specific telecommunications
	// tax tier for audio streaming, sale / permanent download.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL" - US-specific
	// telecommunications tax tier for multi channel audio streaming like radio.
	StreamingTaxType string `json:"streamingTaxType,omitempty"`
	// TaxTier: Tax tier to specify reduced tax rate. Developers who sell digital
	// news, magazines, newspapers, books, or audiobooks in various regions may be
	// eligible for reduced tax rates. Learn more
	// (https://support.google.com/googleplay/android-developer/answer/10463498).
	//
	// Possible values:
	//   "TAX_TIER_UNSPECIFIED"
	//   "TAX_TIER_BOOKS_1"
	//   "TAX_TIER_NEWS_1"
	//   "TAX_TIER_NEWS_2"
	//   "TAX_TIER_MUSIC_OR_AUDIO_1"
	//   "TAX_TIER_LIVE_OR_BROADCAST_1"
	TaxTier string `json:"taxTier,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "EligibleForStreamingServiceTaxRate") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "EligibleForStreamingServiceTaxRate") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

RegionalTaxConfig: Details about taxation in a given geographical region.

func (RegionalTaxConfig) MarshalJSON ¶
added in v0.244.0
func (s RegionalTaxConfig) MarshalJSON() ([]byte, error)
type RegionalTaxRateInfo ¶
added in v0.60.0
type RegionalTaxRateInfo struct {
	// EligibleForStreamingServiceTaxRate: You must tell us if your app contains
	// streaming products to correctly charge US state and local sales tax. Field
	// only supported in the United States.
	EligibleForStreamingServiceTaxRate bool `json:"eligibleForStreamingServiceTaxRate,omitempty"`
	// StreamingTaxType: To collect communications or amusement taxes in the United
	// States, choose the appropriate tax category. Learn more
	// (https://support.google.com/googleplay/android-developer/answer/10463498#streaming_tax).
	//
	// Possible values:
	//   "STREAMING_TAX_TYPE_UNSPECIFIED" - No telecommunications tax collected.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL" - US-specific telecommunications
	// tax tier for video streaming, on demand, rentals / subscriptions /
	// pay-per-view.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_SALES" - US-specific telecommunications
	// tax tier for video streaming of pre-recorded content like movies, tv shows.
	//   "STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL" - US-specific
	// telecommunications tax tier for video streaming of multi-channel
	// programming.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL" - US-specific telecommunications
	// tax tier for audio streaming, rental / subscription.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_SALES" - US-specific telecommunications
	// tax tier for audio streaming, sale / permanent download.
	//   "STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL" - US-specific
	// telecommunications tax tier for multi channel audio streaming like radio.
	StreamingTaxType string `json:"streamingTaxType,omitempty"`
	// TaxTier: Tax tier to specify reduced tax rate. Developers who sell digital
	// news, magazines, newspapers, books, or audiobooks in various regions may be
	// eligible for reduced tax rates. Learn more
	// (https://support.google.com/googleplay/android-developer/answer/10463498).
	//
	// Possible values:
	//   "TAX_TIER_UNSPECIFIED"
	//   "TAX_TIER_BOOKS_1"
	//   "TAX_TIER_NEWS_1"
	//   "TAX_TIER_NEWS_2"
	//   "TAX_TIER_MUSIC_OR_AUDIO_1"
	//   "TAX_TIER_LIVE_OR_BROADCAST_1"
	TaxTier string `json:"taxTier,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "EligibleForStreamingServiceTaxRate") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "EligibleForStreamingServiceTaxRate") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

RegionalTaxRateInfo: Specified details about taxation in a given geographical region.

func (RegionalTaxRateInfo) MarshalJSON ¶
added in v0.60.0
func (s RegionalTaxRateInfo) MarshalJSON() ([]byte, error)
type Regions ¶
added in v0.156.0
type Regions struct {
	// RegionCode: Regions targeted by the recovery action. Region codes are ISO
	// 3166 Alpha-2 country codes. For example, US stands for United States of
	// America. See https://www.iso.org/iso-3166-country-codes.html for the
	// complete list of country codes.
	RegionCode []string `json:"regionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RegionCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RegionCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Regions: Region targeting data for app recovery action targeting.

func (Regions) MarshalJSON ¶
added in v0.156.0
func (s Regions) MarshalJSON() ([]byte, error)
type RegionsVersion ¶
added in v0.80.0
type RegionsVersion struct {
	// Version: Required. A string representing the version of available regions
	// being used for the specified resource. Regional prices and latest supported
	// version for the resource have to be specified according to the information
	// published in this article
	// (https://support.google.com/googleplay/android-developer/answer/10532353).
	// Each time the supported locations substantially change, the version will be
	// incremented. Using this field will ensure that creating and updating the
	// resource with an older region's version and set of regional prices and
	// currencies will succeed even though a new version is available.
	Version string `json:"version,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Version") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Version") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RegionsVersion: The version of the available regions being used for the specified resource.

func (RegionsVersion) MarshalJSON ¶
added in v0.80.0
func (s RegionsVersion) MarshalJSON() ([]byte, error)
type RemoteInAppUpdate ¶
added in v0.156.0
type RemoteInAppUpdate struct {
	// IsRemoteInAppUpdateRequested: Required. Set to true if Remote In-App Update
	// action type is needed.
	IsRemoteInAppUpdateRequested bool `json:"isRemoteInAppUpdateRequested,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "IsRemoteInAppUpdateRequested") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsRemoteInAppUpdateRequested") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemoteInAppUpdate: Object representation for Remote in-app update action type.

func (RemoteInAppUpdate) MarshalJSON ¶
added in v0.156.0
func (s RemoteInAppUpdate) MarshalJSON() ([]byte, error)
type RemoteInAppUpdateData ¶
added in v0.156.0
type RemoteInAppUpdateData struct {
	// RemoteAppUpdateDataPerBundle: Data related to the recovery action at bundle
	// level.
	RemoteAppUpdateDataPerBundle []*RemoteInAppUpdateDataPerBundle `json:"remoteAppUpdateDataPerBundle,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "RemoteAppUpdateDataPerBundle") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RemoteAppUpdateDataPerBundle") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemoteInAppUpdateData: Data related to Remote In-App Update action such as recovered user count, affected user count etc.

func (RemoteInAppUpdateData) MarshalJSON ¶
added in v0.156.0
func (s RemoteInAppUpdateData) MarshalJSON() ([]byte, error)
type RemoteInAppUpdateDataPerBundle ¶
added in v0.156.0
type RemoteInAppUpdateDataPerBundle struct {
	// RecoveredDeviceCount: Total number of devices which have been rescued.
	RecoveredDeviceCount int64 `json:"recoveredDeviceCount,omitempty,string"`
	// TotalDeviceCount: Total number of devices affected by this recovery action
	// associated with bundle of the app.
	TotalDeviceCount int64 `json:"totalDeviceCount,omitempty,string"`
	// VersionCode: Version Code corresponding to the target bundle.
	VersionCode int64 `json:"versionCode,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "RecoveredDeviceCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RecoveredDeviceCount") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemoteInAppUpdateDataPerBundle: Data related to the recovery action at bundle level.

func (RemoteInAppUpdateDataPerBundle) MarshalJSON ¶
added in v0.156.0
func (s RemoteInAppUpdateDataPerBundle) MarshalJSON() ([]byte, error)
type RentOfferDetails ¶
added in v0.240.0
type RentOfferDetails struct {
}

RentOfferDetails: Offer details information related to a rental line item.

type RentalDetails ¶
added in v0.242.0
type RentalDetails struct {
}

RentalDetails: Details of a rental purchase.

type ReplacementCancellation ¶
added in v0.80.0
type ReplacementCancellation struct {
}

ReplacementCancellation: Information specific to cancellations caused by subscription replacement.

type RestrictedPaymentCountries ¶
added in v0.181.0
type RestrictedPaymentCountries struct {
	// RegionCodes: Required. Region codes to impose payment restrictions on, as
	// defined by ISO 3166-2, e.g. "US".
	RegionCodes []string `json:"regionCodes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RegionCodes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RegionCodes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RestrictedPaymentCountries: Countries where the purchase of this product is restricted to payment methods registered in the same country. If empty, no payment location restrictions are imposed.

func (RestrictedPaymentCountries) MarshalJSON ¶
added in v0.181.0
func (s RestrictedPaymentCountries) MarshalJSON() ([]byte, error)
type Review ¶
type Review struct {
	// AuthorName: The name of the user who wrote the review.
	AuthorName string `json:"authorName,omitempty"`
	// Comments: A repeated field containing comments for the review.
	Comments []*Comment `json:"comments,omitempty"`
	// ReviewId: Unique identifier for this review.
	ReviewId string `json:"reviewId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuthorName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthorName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Review: An Android app review.

func (Review) MarshalJSON ¶
func (s Review) MarshalJSON() ([]byte, error)
type ReviewReplyResult ¶
type ReviewReplyResult struct {
	// LastEdited: The time at which the reply took effect.
	LastEdited *Timestamp `json:"lastEdited,omitempty"`
	// ReplyText: The reply text that was applied.
	ReplyText string `json:"replyText,omitempty"`
	// ForceSendFields is a list of field names (e.g. "LastEdited") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LastEdited") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReviewReplyResult: The result of replying/updating a reply to review.

func (ReviewReplyResult) MarshalJSON ¶
func (s ReviewReplyResult) MarshalJSON() ([]byte, error)
type ReviewsGetCall ¶
type ReviewsGetCall struct {
	// contains filtered or unexported fields
}
func (*ReviewsGetCall) Context ¶
func (c *ReviewsGetCall) Context(ctx context.Context) *ReviewsGetCall

Context sets the context to be used in this call's Do method.

func (*ReviewsGetCall) Do ¶
func (c *ReviewsGetCall) Do(opts ...googleapi.CallOption) (*Review, error)

Do executes the "androidpublisher.reviews.get" call. Any non-2xx status code is an error. Response headers are in either *Review.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReviewsGetCall) Fields ¶
func (c *ReviewsGetCall) Fields(s ...googleapi.Field) *ReviewsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ReviewsGetCall) Header ¶
func (c *ReviewsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ReviewsGetCall) IfNoneMatch ¶
func (c *ReviewsGetCall) IfNoneMatch(entityTag string) *ReviewsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ReviewsGetCall) TranslationLanguage ¶
func (c *ReviewsGetCall) TranslationLanguage(translationLanguage string) *ReviewsGetCall

TranslationLanguage sets the optional parameter "translationLanguage": Language localization code.

type ReviewsListCall ¶
type ReviewsListCall struct {
	// contains filtered or unexported fields
}
func (*ReviewsListCall) Context ¶
func (c *ReviewsListCall) Context(ctx context.Context) *ReviewsListCall

Context sets the context to be used in this call's Do method.

func (*ReviewsListCall) Do ¶
func (c *ReviewsListCall) Do(opts ...googleapi.CallOption) (*ReviewsListResponse, error)

Do executes the "androidpublisher.reviews.list" call. Any non-2xx status code is an error. Response headers are in either *ReviewsListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReviewsListCall) Fields ¶
func (c *ReviewsListCall) Fields(s ...googleapi.Field) *ReviewsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ReviewsListCall) Header ¶
func (c *ReviewsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ReviewsListCall) IfNoneMatch ¶
func (c *ReviewsListCall) IfNoneMatch(entityTag string) *ReviewsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ReviewsListCall) MaxResults ¶
func (c *ReviewsListCall) MaxResults(maxResults int64) *ReviewsListCall

MaxResults sets the optional parameter "maxResults": How many results the list operation should return.

func (*ReviewsListCall) StartIndex ¶
func (c *ReviewsListCall) StartIndex(startIndex int64) *ReviewsListCall

StartIndex sets the optional parameter "startIndex": The index of the first element to return.

func (*ReviewsListCall) Token ¶
func (c *ReviewsListCall) Token(token string) *ReviewsListCall

Token sets the optional parameter "token": Pagination token. If empty, list starts at the first review.

func (*ReviewsListCall) TranslationLanguage ¶
func (c *ReviewsListCall) TranslationLanguage(translationLanguage string) *ReviewsListCall

TranslationLanguage sets the optional parameter "translationLanguage": Language localization code.

type ReviewsListResponse ¶
type ReviewsListResponse struct {
	// PageInfo: Information about the current page.
	PageInfo *PageInfo `json:"pageInfo,omitempty"`
	// Reviews: List of reviews.
	Reviews []*Review `json:"reviews,omitempty"`
	// TokenPagination: Pagination token, to handle a number of products that is
	// over one page.
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

ReviewsListResponse: Response listing reviews.

func (ReviewsListResponse) MarshalJSON ¶
func (s ReviewsListResponse) MarshalJSON() ([]byte, error)
type ReviewsReplyCall ¶
type ReviewsReplyCall struct {
	// contains filtered or unexported fields
}
func (*ReviewsReplyCall) Context ¶
func (c *ReviewsReplyCall) Context(ctx context.Context) *ReviewsReplyCall

Context sets the context to be used in this call's Do method.

func (*ReviewsReplyCall) Do ¶
func (c *ReviewsReplyCall) Do(opts ...googleapi.CallOption) (*ReviewsReplyResponse, error)

Do executes the "androidpublisher.reviews.reply" call. Any non-2xx status code is an error. Response headers are in either *ReviewsReplyResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReviewsReplyCall) Fields ¶
func (c *ReviewsReplyCall) Fields(s ...googleapi.Field) *ReviewsReplyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ReviewsReplyCall) Header ¶
func (c *ReviewsReplyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ReviewsReplyRequest ¶
type ReviewsReplyRequest struct {
	// ReplyText: The text to set as the reply. Replies of more than approximately
	// 350 characters will be rejected. HTML tags will be stripped.
	ReplyText string `json:"replyText,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReplyText") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReplyText") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReviewsReplyRequest: Request to reply to review or update existing reply.

func (ReviewsReplyRequest) MarshalJSON ¶
func (s ReviewsReplyRequest) MarshalJSON() ([]byte, error)
type ReviewsReplyResponse ¶
type ReviewsReplyResponse struct {
	// Result: The result of replying/updating a reply to review.
	Result *ReviewReplyResult `json:"result,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Result") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Result") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReviewsReplyResponse: Response on status of replying to a review.

func (ReviewsReplyResponse) MarshalJSON ¶
func (s ReviewsReplyResponse) MarshalJSON() ([]byte, error)
type ReviewsService ¶
type ReviewsService struct {
	// contains filtered or unexported fields
}
func NewReviewsService ¶
func NewReviewsService(s *Service) *ReviewsService
func (*ReviewsService) Get ¶
func (r *ReviewsService) Get(packageName string, reviewId string) *ReviewsGetCall

Get: Gets a single review.

- packageName: Package name of the app. - reviewId: Unique identifier for a review.

func (*ReviewsService) List ¶
func (r *ReviewsService) List(packageName string) *ReviewsListCall

List: Lists all reviews.

- packageName: Package name of the app.

func (*ReviewsService) Reply ¶
func (r *ReviewsService) Reply(packageName string, reviewId string, reviewsreplyrequest *ReviewsReplyRequest) *ReviewsReplyCall

Reply: Replies to a single review, or updates an existing reply.

- packageName: Package name of the app. - reviewId: Unique identifier for a review.

type RevocationContext ¶
added in v0.157.0
type RevocationContext struct {
	// FullRefund: Optional. Used when users should be refunded the full amount of
	// latest charge on each item in the subscription.
	FullRefund *RevocationContextFullRefund `json:"fullRefund,omitempty"`
	// ItemBasedRefund: Optional. Used when a specific item should be refunded in a
	// subscription with add-on items.
	ItemBasedRefund *RevocationContextItemBasedRefund `json:"itemBasedRefund,omitempty"`
	// ProratedRefund: Optional. Used when users should be refunded a prorated
	// amount they paid for their subscription based on the amount of time
	// remaining in a subscription.
	ProratedRefund *RevocationContextProratedRefund `json:"proratedRefund,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FullRefund") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FullRefund") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RevocationContext: Revocation context of the purchases.subscriptionsv2.revoke API.

func (RevocationContext) MarshalJSON ¶
added in v0.157.0
func (s RevocationContext) MarshalJSON() ([]byte, error)
type RevocationContextFullRefund ¶
added in v0.193.0
type RevocationContextFullRefund struct {
}

RevocationContextFullRefund: Used to determine if the refund type in the RevocationContext is a full refund.

type RevocationContextItemBasedRefund ¶
added in v0.234.0
type RevocationContextItemBasedRefund struct {
	// ProductId: Required. If the subscription is a subscription with add-ons, the
	// product id of the subscription item to revoke.
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

RevocationContextItemBasedRefund: Used to determine what specific item to revoke in a subscription with multiple items.

func (RevocationContextItemBasedRefund) MarshalJSON ¶
added in v0.234.0
func (s RevocationContextItemBasedRefund) MarshalJSON() ([]byte, error)
type RevocationContextProratedRefund ¶
added in v0.157.0
type RevocationContextProratedRefund struct {
}

RevocationContextProratedRefund: Used to determine if the refund type in the RevocationContext is a prorated refund.

type RevokeSubscriptionPurchaseRequest ¶
added in v0.157.0
type RevokeSubscriptionPurchaseRequest struct {
	// RevocationContext: Required. Additional details around the subscription
	// revocation.
	RevocationContext *RevocationContext `json:"revocationContext,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RevocationContext") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RevocationContext") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RevokeSubscriptionPurchaseRequest: Request for the purchases.subscriptionsv2.revoke API.

func (RevokeSubscriptionPurchaseRequest) MarshalJSON ¶
added in v0.157.0
func (s RevokeSubscriptionPurchaseRequest) MarshalJSON() ([]byte, error)
type RevokeSubscriptionPurchaseResponse ¶
added in v0.157.0
type RevokeSubscriptionPurchaseResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

RevokeSubscriptionPurchaseResponse: Response for the purchases.subscriptionsv2.revoke API.

type SafetyLabelsUpdateRequest ¶
added in v0.160.0
type SafetyLabelsUpdateRequest struct {
	// SafetyLabels: Required. Contents of the CSV file containing Data Safety
	// responses. For the format of this file, see the Help Center documentation at
	// https://support.google.com/googleplay/android-developer/answer/10787469?#zippy=%2Cunderstand-the-csv-format
	// To download an up to date template, follow the steps at
	// https://support.google.com/googleplay/android-developer/answer/10787469?#zippy=%2Cexport-to-a-csv-file
	SafetyLabels string `json:"safetyLabels,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SafetyLabels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SafetyLabels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SafetyLabelsUpdateRequest: Request to update Safety Labels of an app.

func (SafetyLabelsUpdateRequest) MarshalJSON ¶
added in v0.160.0
func (s SafetyLabelsUpdateRequest) MarshalJSON() ([]byte, error)
type SafetyLabelsUpdateResponse ¶
added in v0.160.0
type SafetyLabelsUpdateResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

SafetyLabelsUpdateResponse: Response for SafetyLabelsUpdate rpc.

type ScreenDensity ¶
added in v0.130.0
type ScreenDensity struct {
	// DensityAlias: Alias for a screen density.
	//
	// Possible values:
	//   "DENSITY_UNSPECIFIED" - Unspecified screen density.
	//   "NODPI" - NODPI screen density.
	//   "LDPI" - LDPI screen density.
	//   "MDPI" - MDPI screen density.
	//   "TVDPI" - TVDPI screen density.
	//   "HDPI" - HDPI screen density.
	//   "XHDPI" - XHDPI screen density.
	//   "XXHDPI" - XXHDPI screen density.
	//   "XXXHDPI" - XXXHDPI screen density.
	DensityAlias string `json:"densityAlias,omitempty"`
	// DensityDpi: Value for density dpi.
	DensityDpi int64 `json:"densityDpi,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DensityAlias") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DensityAlias") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ScreenDensity: Represents a screen density.

func (ScreenDensity) MarshalJSON ¶
added in v0.130.0
func (s ScreenDensity) MarshalJSON() ([]byte, error)
type ScreenDensityTargeting ¶
added in v0.130.0
type ScreenDensityTargeting struct {
	// Alternatives: Targeting of other sibling directories that were in the
	// Bundle. For main splits this is targeting of other main splits.
	Alternatives []*ScreenDensity `json:"alternatives,omitempty"`
	// Value: Value of a screen density.
	Value []*ScreenDensity `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ScreenDensityTargeting: Targeting based on screen density.

func (ScreenDensityTargeting) MarshalJSON ¶
added in v0.130.0
func (s ScreenDensityTargeting) MarshalJSON() ([]byte, error)
type SdkVersion ¶
added in v0.130.0
type SdkVersion struct {
	// Min: Inclusive minimum value of an sdk version.
	Min int64 `json:"min,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Min") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Min") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SdkVersion: Represents an sdk version.

func (SdkVersion) MarshalJSON ¶
added in v0.130.0
func (s SdkVersion) MarshalJSON() ([]byte, error)
type SdkVersionTargeting ¶
added in v0.130.0
type SdkVersionTargeting struct {
	// Alternatives: Targeting of other sibling directories that were in the
	// Bundle. For main splits this is targeting of other main splits.
	Alternatives []*SdkVersion `json:"alternatives,omitempty"`
	// Value: Value of an sdk version.
	Value []*SdkVersion `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SdkVersionTargeting: Targeting based on sdk version.

func (SdkVersionTargeting) MarshalJSON ¶
added in v0.130.0
func (s SdkVersionTargeting) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Applications *ApplicationsService

	Apprecovery *ApprecoveryService

	Edits *EditsService

	Externaltransactions *ExternaltransactionsService

	Generatedapks *GeneratedapksService

	Grants *GrantsService

	Inappproducts *InappproductsService

	Internalappsharingartifacts *InternalappsharingartifactsService

	Monetization *MonetizationService

	Orders *OrdersService

	Purchases *PurchasesService

	Reviews *ReviewsService

	Systemapks *SystemapksService

	Users *UsersService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type SignupPromotion ¶
added in v0.210.0
type SignupPromotion struct {
	// OneTimeCode: A one-time code was applied.
	OneTimeCode *OneTimeCode `json:"oneTimeCode,omitempty"`
	// VanityCode: A vanity code was applied.
	VanityCode *VanityCode `json:"vanityCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OneTimeCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OneTimeCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SignupPromotion: The promotion applied on this item when purchased.

func (SignupPromotion) MarshalJSON ¶
added in v0.210.0
func (s SignupPromotion) MarshalJSON() ([]byte, error)
type SplitApkMetadata ¶
added in v0.130.0
type SplitApkMetadata struct {
	// IsMasterSplit: Indicates whether this APK is the main split of the module.
	IsMasterSplit bool `json:"isMasterSplit,omitempty"`
	// SplitId: Id of the split.
	SplitId string `json:"splitId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IsMasterSplit") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IsMasterSplit") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SplitApkMetadata: Holds data specific to Split APKs.

func (SplitApkMetadata) MarshalJSON ¶
added in v0.130.0
func (s SplitApkMetadata) MarshalJSON() ([]byte, error)
type SplitApkVariant ¶
added in v0.130.0
type SplitApkVariant struct {
	// ApkSet: Set of APKs, one set per module.
	ApkSet []*ApkSet `json:"apkSet,omitempty"`
	// Targeting: Variant-level targeting.
	Targeting *VariantTargeting `json:"targeting,omitempty"`
	// VariantNumber: Number of the variant, starting at 0 (unless overridden). A
	// device will receive APKs from the first variant that matches the device
	// configuration, with higher variant numbers having priority over lower
	// variant numbers.
	VariantNumber int64 `json:"variantNumber,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApkSet") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApkSet") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SplitApkVariant: Variant is a group of APKs that covers a part of the device configuration space. APKs from multiple variants are never combined on one device.

func (SplitApkVariant) MarshalJSON ¶
added in v0.130.0
func (s SplitApkVariant) MarshalJSON() ([]byte, error)
type StandaloneApkMetadata ¶
added in v0.130.0
type StandaloneApkMetadata struct {
	// FusedModuleName: Names of the modules fused in this standalone APK.
	FusedModuleName []string `json:"fusedModuleName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FusedModuleName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FusedModuleName") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StandaloneApkMetadata: Holds data specific to Standalone APKs.

func (StandaloneApkMetadata) MarshalJSON ¶
added in v0.130.0
func (s StandaloneApkMetadata) MarshalJSON() ([]byte, error)
type SubscribeWithGoogleInfo ¶
added in v0.80.0
type SubscribeWithGoogleInfo struct {
	// EmailAddress: The email address of the user when the subscription was
	// purchased.
	EmailAddress string `json:"emailAddress,omitempty"`
	// FamilyName: The family name of the user when the subscription was purchased.
	FamilyName string `json:"familyName,omitempty"`
	// GivenName: The given name of the user when the subscription was purchased.
	GivenName string `json:"givenName,omitempty"`
	// ProfileId: The Google profile id of the user when the subscription was
	// purchased.
	ProfileId string `json:"profileId,omitempty"`
	// ProfileName: The profile name of the user when the subscription was
	// purchased.
	ProfileName string `json:"profileName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EmailAddress") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EmailAddress") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscribeWithGoogleInfo: Information associated with purchases made with 'Subscribe with Google'.

func (SubscribeWithGoogleInfo) MarshalJSON ¶
added in v0.80.0
func (s SubscribeWithGoogleInfo) MarshalJSON() ([]byte, error)
type Subscription ¶
added in v0.80.0
type Subscription struct {
	// Archived: Output only. Deprecated: subscription archiving is not supported.
	Archived bool `json:"archived,omitempty"`
	// BasePlans: The set of base plans for this subscription. Represents the
	// prices and duration of the subscription if no other offers apply.
	BasePlans []*BasePlan `json:"basePlans,omitempty"`
	// Listings: Required. List of localized listings for this subscription. Must
	// contain at least an entry for the default language of the parent app.
	Listings []*SubscriptionListing `json:"listings,omitempty"`
	// PackageName: Immutable. Package name of the parent app.
	PackageName string `json:"packageName,omitempty"`
	// ProductId: Immutable. Unique product ID of the product. Unique within the
	// parent app. Product IDs must be composed of lower-case letters (a-z),
	// numbers (0-9), underscores (_) and dots (.). It must start with a lower-case
	// letter or number, and be between 1 and 40 (inclusive) characters in length.
	ProductId string `json:"productId,omitempty"`
	// RestrictedPaymentCountries: Optional. Countries where the purchase of this
	// subscription is restricted to payment methods registered in the same
	// country. If empty, no payment location restrictions are imposed.
	RestrictedPaymentCountries *RestrictedPaymentCountries `json:"restrictedPaymentCountries,omitempty"`
	// TaxAndComplianceSettings: Details about taxes and legal compliance.
	TaxAndComplianceSettings *SubscriptionTaxAndComplianceSettings `json:"taxAndComplianceSettings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Archived") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Archived") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Subscription: A single subscription for an app.

func (Subscription) MarshalJSON ¶
added in v0.80.0
func (s Subscription) MarshalJSON() ([]byte, error)
type SubscriptionCancelSurveyResult ¶
type SubscriptionCancelSurveyResult struct {
	// CancelSurveyReason: The cancellation reason the user chose in the survey.
	// Possible values are: 0. Other 1. I don't use this service enough 2.
	// Technical issues 3. Cost-related reasons 4. I found a better app
	CancelSurveyReason int64 `json:"cancelSurveyReason,omitempty"`
	// UserInputCancelReason: The customized input cancel reason from the user.
	// Only present when cancelReason is 0.
	UserInputCancelReason string `json:"userInputCancelReason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CancelSurveyReason") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CancelSurveyReason") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionCancelSurveyResult: Information provided by the user when they complete the subscription cancellation flow (cancellation reason survey).

func (SubscriptionCancelSurveyResult) MarshalJSON ¶
func (s SubscriptionCancelSurveyResult) MarshalJSON() ([]byte, error)
type SubscriptionDeferralInfo ¶
type SubscriptionDeferralInfo struct {
	// DesiredExpiryTimeMillis: The desired next expiry time to assign to the
	// subscription, in milliseconds since the Epoch. The given time must be
	// later/greater than the current expiry time for the subscription.
	DesiredExpiryTimeMillis int64 `json:"desiredExpiryTimeMillis,omitempty,string"`
	// ExpectedExpiryTimeMillis: The expected expiry time for the subscription. If
	// the current expiry time for the subscription is not the value specified
	// here, the deferral will not occur.
	ExpectedExpiryTimeMillis int64 `json:"expectedExpiryTimeMillis,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "DesiredExpiryTimeMillis") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DesiredExpiryTimeMillis") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionDeferralInfo: A SubscriptionDeferralInfo contains the data needed to defer a subscription purchase to a future expiry time.

func (SubscriptionDeferralInfo) MarshalJSON ¶
func (s SubscriptionDeferralInfo) MarshalJSON() ([]byte, error)
type SubscriptionDetails ¶
added in v0.234.0
type SubscriptionDetails struct {
	// BasePlanId: The base plan ID of the subscription.
	BasePlanId string `json:"basePlanId,omitempty"`
	// OfferId: The offer ID for the current subscription offer.
	OfferId string `json:"offerId,omitempty"`
	// OfferPhase: The pricing phase for the billing period funded by this order.
	// Deprecated. Use offer_phase_details instead.
	//
	// Possible values:
	//   "OFFER_PHASE_UNSPECIFIED" - Offer phase unspecified. This value is not
	// used.
	//   "BASE" - The order funds a base price period.
	//   "INTRODUCTORY" - The order funds an introductory pricing period.
	//   "FREE_TRIAL" - The order funds a free trial period.
	OfferPhase string `json:"offerPhase,omitempty"`
	// OfferPhaseDetails: The pricing phase details for the entitlement period
	// funded by this order.
	OfferPhaseDetails *OfferPhaseDetails `json:"offerPhaseDetails,omitempty"`
	// ServicePeriodEndTime: The end of the billing period funded by this order.
	// This is a snapshot of the billing/service period end time at the moment the
	// order was processed, and should be used only for accounting. To get the
	// current end time of the subscription service period, use
	// purchases.subscriptionsv2.get.
	ServicePeriodEndTime string `json:"servicePeriodEndTime,omitempty"`
	// ServicePeriodStartTime: The start of the billing period funded by this
	// order. This is a snapshot of the billing/service period start time at the
	// moment the order was processed, and should be used only for accounting.
	ServicePeriodStartTime string `json:"servicePeriodStartTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionDetails: Details of a subscription purchase.

func (SubscriptionDetails) MarshalJSON ¶
added in v0.234.0
func (s SubscriptionDetails) MarshalJSON() ([]byte, error)
type SubscriptionItemPriceChangeDetails ¶
added in v0.104.0
type SubscriptionItemPriceChangeDetails struct {
	// ExpectedNewPriceChargeTime: The renewal time at which the price change will
	// become effective for the user. This is subject to change(to a future time)
	// due to cases where the renewal time shifts like pause. This field is only
	// populated if the price change has not taken effect.
	ExpectedNewPriceChargeTime string `json:"expectedNewPriceChargeTime,omitempty"`
	// NewPrice: New recurring price for the subscription item.
	NewPrice *Money `json:"newPrice,omitempty"`
	// PriceChangeMode: Price change mode specifies how the subscription item price
	// is changing.
	//
	// Possible values:
	//   "PRICE_CHANGE_MODE_UNSPECIFIED" - Price change mode unspecified. This
	// value should never be set.
	//   "PRICE_DECREASE" - If the subscription price is decreasing.
	//   "PRICE_INCREASE" - If the subscription price is increasing and the user
	// needs to accept it.
	//   "OPT_OUT_PRICE_INCREASE" - If the subscription price is increasing with
	// opt out mode.
	PriceChangeMode string `json:"priceChangeMode,omitempty"`
	// PriceChangeState: State the price change is currently in.
	//
	// Possible values:
	//   "PRICE_CHANGE_STATE_UNSPECIFIED" - Price change state unspecified. This
	// value should not be used.
	//   "OUTSTANDING" - Waiting for the user to agree for the price change.
	//   "CONFIRMED" - The price change is confirmed to happen for the user.
	//   "APPLIED" - The price change is applied, i.e. the user has started being
	// charged the new price.
	//   "CANCELED" - The price change was canceled.
	PriceChangeState string `json:"priceChangeState,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExpectedNewPriceChargeTime")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpectedNewPriceChargeTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionItemPriceChangeDetails: Price change related information of a subscription item.

func (SubscriptionItemPriceChangeDetails) MarshalJSON ¶
added in v0.104.0
func (s SubscriptionItemPriceChangeDetails) MarshalJSON() ([]byte, error)
type SubscriptionListing ¶
added in v0.80.0
type SubscriptionListing struct {
	// Benefits: A list of benefits shown to the user on platforms such as the Play
	// Store and in restoration flows in the language of this listing. Plain text.
	// Ordered list of at most four benefits.
	Benefits []string `json:"benefits,omitempty"`
	// Description: The description of this subscription in the language of this
	// listing. Maximum length - 80 characters. Plain text.
	Description string `json:"description,omitempty"`
	// LanguageCode: Required. The language of this listing, as defined by BCP-47,
	// e.g. "en-US".
	LanguageCode string `json:"languageCode,omitempty"`
	// Title: Required. The title of this subscription in the language of this
	// listing. Plain text.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Benefits") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Benefits") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionListing: The consumer-visible metadata of a subscription.

func (SubscriptionListing) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionListing) MarshalJSON() ([]byte, error)
type SubscriptionOffer ¶
added in v0.80.0
type SubscriptionOffer struct {
	// BasePlanId: Required. Immutable. The ID of the base plan to which this offer
	// is an extension.
	BasePlanId string `json:"basePlanId,omitempty"`
	// OfferId: Required. Immutable. Unique ID of this subscription offer. Must be
	// unique within the base plan.
	OfferId string `json:"offerId,omitempty"`
	// OfferTags: List of up to 20 custom tags specified for this offer, and
	// returned to the app through the billing library.
	OfferTags []*OfferTag `json:"offerTags,omitempty"`
	// OtherRegionsConfig: The configuration for any new locations Play may launch
	// in the future.
	OtherRegionsConfig *OtherRegionsSubscriptionOfferConfig `json:"otherRegionsConfig,omitempty"`
	// PackageName: Required. Immutable. The package name of the app the parent
	// subscription belongs to.
	PackageName string `json:"packageName,omitempty"`
	// Phases: Required. The phases of this subscription offer. Must contain at
	// least one and at most two entries. Users will always receive all these
	// phases in the specified order.
	Phases []*SubscriptionOfferPhase `json:"phases,omitempty"`
	// ProductId: Required. Immutable. The ID of the parent subscription this offer
	// belongs to.
	ProductId string `json:"productId,omitempty"`
	// RegionalConfigs: Required. The region-specific configuration of this offer.
	// Must contain at least one entry.
	RegionalConfigs []*RegionalSubscriptionOfferConfig `json:"regionalConfigs,omitempty"`
	// State: Output only. The current state of this offer. Can be changed using
	// Activate and Deactivate actions. NB: the base plan state supersedes this
	// state, so an active offer may not be available if the base plan is not
	// active.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value, should never be used.
	//   "DRAFT" - The subscription offer is not and has never been available to
	// users.
	//   "ACTIVE" - The subscription offer is available to new and existing users.
	//   "INACTIVE" - The subscription offer is not available to new users.
	// Existing users retain access.
	State string `json:"state,omitempty"`
	// Targeting: The requirements that users need to fulfil to be eligible for
	// this offer. Represents the requirements that Play will evaluate to decide
	// whether an offer should be returned. Developers may further filter these
	// offers themselves.
	Targeting *SubscriptionOfferTargeting `json:"targeting,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BasePlanId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BasePlanId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionOffer: A single, temporary offer

func (SubscriptionOffer) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionOffer) MarshalJSON() ([]byte, error)
type SubscriptionOfferPhase ¶
added in v0.80.0
type SubscriptionOfferPhase struct {
	// Duration: Required. The duration of a single recurrence of this phase.
	// Specified in ISO 8601 format.
	Duration string `json:"duration,omitempty"`
	// OtherRegionsConfig: Pricing information for any new locations Play may
	// launch in.
	OtherRegionsConfig *OtherRegionsSubscriptionOfferPhaseConfig `json:"otherRegionsConfig,omitempty"`
	// RecurrenceCount: Required. The number of times this phase repeats. If this
	// offer phase is not free, each recurrence charges the user the price of this
	// offer phase.
	RecurrenceCount int64 `json:"recurrenceCount,omitempty"`
	// RegionalConfigs: Required. The region-specific configuration of this offer
	// phase. This list must contain exactly one entry for each region for which
	// the subscription offer has a regional config.
	RegionalConfigs []*RegionalSubscriptionOfferPhaseConfig `json:"regionalConfigs,omitempty"`
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

SubscriptionOfferPhase: A single phase of a subscription offer.

func (SubscriptionOfferPhase) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionOfferPhase) MarshalJSON() ([]byte, error)
type SubscriptionOfferTargeting ¶
added in v0.80.0
type SubscriptionOfferTargeting struct {
	// AcquisitionRule: Offer targeting rule for new user acquisition.
	AcquisitionRule *AcquisitionTargetingRule `json:"acquisitionRule,omitempty"`
	// UpgradeRule: Offer targeting rule for upgrading users' existing plans.
	UpgradeRule *UpgradeTargetingRule `json:"upgradeRule,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AcquisitionRule") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcquisitionRule") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionOfferTargeting: Defines the rule a user needs to satisfy to receive this offer.

func (SubscriptionOfferTargeting) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionOfferTargeting) MarshalJSON() ([]byte, error)
type SubscriptionPriceChange ¶
type SubscriptionPriceChange struct {
	// NewPrice: The new price the subscription will renew with if the price change
	// is accepted by the user.
	NewPrice *Price `json:"newPrice,omitempty"`
	// State: The current state of the price change. Possible values are: 0.
	// Outstanding: State for a pending price change waiting for the user to agree.
	// In this state, you can optionally seek confirmation from the user using the
	// In-App API. 1. Accepted: State for an accepted price change that the
	// subscription will renew with unless it's canceled. The price change takes
	// effect on a future date when the subscription renews. Note that the change
	// might not occur when the subscription is renewed next.
	State int64 `json:"state,omitempty"`
	// ForceSendFields is a list of field names (e.g. "NewPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPriceChange: Contains the price change information for a subscription that can be used to control the user journey for the price change in the app. This can be in the form of seeking confirmation from the user or tailoring the experience for a successful conversion.

func (SubscriptionPriceChange) MarshalJSON ¶
func (s SubscriptionPriceChange) MarshalJSON() ([]byte, error)
type SubscriptionPurchase ¶
type SubscriptionPurchase struct {
	// AcknowledgementState: The acknowledgement state of the subscription product.
	// Possible values are: 0. Yet to be acknowledged 1. Acknowledged
	AcknowledgementState int64 `json:"acknowledgementState,omitempty"`
	// AutoRenewing: Whether the subscription will automatically be renewed when it
	// reaches its current expiry time.
	AutoRenewing bool `json:"autoRenewing,omitempty"`
	// AutoResumeTimeMillis: Time at which the subscription will be automatically
	// resumed, in milliseconds since the Epoch. Only present if the user has
	// requested to pause the subscription.
	AutoResumeTimeMillis int64 `json:"autoResumeTimeMillis,omitempty,string"`
	// CancelReason: The reason why a subscription was canceled or is not
	// auto-renewing. Possible values are: 0. User canceled the subscription 1.
	// Subscription was canceled by the system, for example because of a billing
	// problem 2. Subscription was replaced with a new subscription 3. Subscription
	// was canceled by the developer
	CancelReason int64 `json:"cancelReason,omitempty"`
	// CancelSurveyResult: Information provided by the user when they complete the
	// subscription cancellation flow (cancellation reason survey).
	CancelSurveyResult *SubscriptionCancelSurveyResult `json:"cancelSurveyResult,omitempty"`
	// CountryCode: ISO 3166-1 alpha-2 billing country/region code of the user at
	// the time the subscription was granted.
	CountryCode string `json:"countryCode,omitempty"`
	// DeveloperPayload: A developer-specified string that contains supplemental
	// information about an order.
	DeveloperPayload string `json:"developerPayload,omitempty"`
	// EmailAddress: The email address of the user when the subscription was
	// purchased. Only present for purchases made with 'Subscribe with Google'.
	EmailAddress string `json:"emailAddress,omitempty"`
	// ExpiryTimeMillis: Time at which the subscription will expire, in
	// milliseconds since the Epoch.
	ExpiryTimeMillis int64 `json:"expiryTimeMillis,omitempty,string"`
	// ExternalAccountId: User account identifier in the third-party service. Only
	// present if account linking happened as part of the subscription purchase
	// flow.
	ExternalAccountId string `json:"externalAccountId,omitempty"`
	// FamilyName: The family name of the user when the subscription was purchased.
	// Only present for purchases made with 'Subscribe with Google'.
	FamilyName string `json:"familyName,omitempty"`
	// GivenName: The given name of the user when the subscription was purchased.
	// Only present for purchases made with 'Subscribe with Google'.
	GivenName string `json:"givenName,omitempty"`
	// IntroductoryPriceInfo: Introductory price information of the subscription.
	// This is only present when the subscription was purchased with an
	// introductory price. This field does not indicate the subscription is
	// currently in introductory price period.
	IntroductoryPriceInfo *IntroductoryPriceInfo `json:"introductoryPriceInfo,omitempty"`
	// Kind: This kind represents a subscriptionPurchase object in the
	// androidpublisher service.
	Kind string `json:"kind,omitempty"`
	// LinkedPurchaseToken: The purchase token of the originating purchase if this
	// subscription is one of the following: 0. Re-signup of a canceled but
	// non-lapsed subscription 1. Upgrade/downgrade from a previous subscription
	// For example, suppose a user originally signs up and you receive purchase
	// token X, then the user cancels and goes through the resignup flow (before
	// their subscription lapses) and you receive purchase token Y, and finally the
	// user upgrades their subscription and you receive purchase token Z. If you
	// call this API with purchase token Z, this field will be set to Y. If you
	// call this API with purchase token Y, this field will be set to X. If you
	// call this API with purchase token X, this field will not be set.
	LinkedPurchaseToken string `json:"linkedPurchaseToken,omitempty"`
	// ObfuscatedExternalAccountId: An obfuscated version of the id that is
	// uniquely associated with the user's account in your app. Present for the
	// following purchases: * If account linking happened as part of the
	// subscription purchase flow. * It was specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid
	// when the purchase was made.
	ObfuscatedExternalAccountId string `json:"obfuscatedExternalAccountId,omitempty"`
	// ObfuscatedExternalProfileId: An obfuscated version of the id that is
	// uniquely associated with the user's profile in your app. Only present if
	// specified using
	// https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid
	// when the purchase was made.
	ObfuscatedExternalProfileId string `json:"obfuscatedExternalProfileId,omitempty"`
	// OrderId: The order id of the latest recurring order associated with the
	// purchase of the subscription. If the subscription was canceled because
	// payment was declined, this will be the order id from the payment declined
	// order.
	OrderId string `json:"orderId,omitempty"`
	// PaymentState: The payment state of the subscription. Possible values are: 0.
	// Payment pending 1. Payment received 2. Free trial 3. Pending deferred
	// upgrade/downgrade Not present for canceled, expired subscriptions.
	PaymentState *int64 `json:"paymentState,omitempty"`
	// PriceAmountMicros: Price of the subscription, For tax exclusive countries,
	// the price doesn't include tax. For tax inclusive countries, the price
	// includes tax. Price is expressed in micro-units, where 1,000,000 micro-units
	// represents one unit of the currency. For example, if the subscription price
	// is €1.99, price_amount_micros is 1990000.
	PriceAmountMicros int64 `json:"priceAmountMicros,omitempty,string"`
	// PriceChange: The latest price change information available. This is present
	// only when there is an upcoming price change for the subscription yet to be
	// applied. Once the subscription renews with the new price or the subscription
	// is canceled, no price change information will be returned.
	PriceChange *SubscriptionPriceChange `json:"priceChange,omitempty"`
	// PriceCurrencyCode: ISO 4217 currency code for the subscription price. For
	// example, if the price is specified in British pounds sterling,
	// price_currency_code is "GBP".
	PriceCurrencyCode string `json:"priceCurrencyCode,omitempty"`
	// ProfileId: The Google profile id of the user when the subscription was
	// purchased. Only present for purchases made with 'Subscribe with Google'.
	ProfileId string `json:"profileId,omitempty"`
	// ProfileName: The profile name of the user when the subscription was
	// purchased. Only present for purchases made with 'Subscribe with Google'.
	ProfileName string `json:"profileName,omitempty"`
	// PromotionCode: The promotion code applied on this purchase. This field is
	// only set if a vanity code promotion is applied when the subscription was
	// purchased.
	PromotionCode string `json:"promotionCode,omitempty"`
	// PromotionType: The type of promotion applied on this purchase. This field is
	// only set if a promotion is applied when the subscription was purchased.
	// Possible values are: 0. One time code 1. Vanity code
	PromotionType int64 `json:"promotionType,omitempty"`
	// PurchaseType: The type of purchase of the subscription. This field is only
	// set if this purchase was not made using the standard in-app billing flow.
	// Possible values are: 0. Test (i.e. purchased from a license testing account)
	// 1. Promo (i.e. purchased using a promo code)
	PurchaseType *int64 `json:"purchaseType,omitempty"`
	// StartTimeMillis: Time at which the subscription was granted, in milliseconds
	// since the Epoch.
	StartTimeMillis int64 `json:"startTimeMillis,omitempty,string"`
	// UserCancellationTimeMillis: The time at which the subscription was canceled
	// by the user, in milliseconds since the epoch. Only present if cancelReason
	// is 0.
	UserCancellationTimeMillis int64 `json:"userCancellationTimeMillis,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AcknowledgementState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcknowledgementState") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchase: A SubscriptionPurchase resource indicates the status of a user's subscription purchase.

func (SubscriptionPurchase) MarshalJSON ¶
func (s SubscriptionPurchase) MarshalJSON() ([]byte, error)
type SubscriptionPurchaseLineItem ¶
added in v0.80.0
type SubscriptionPurchaseLineItem struct {
	// AutoRenewingPlan: The item is auto renewing.
	AutoRenewingPlan *AutoRenewingPlan `json:"autoRenewingPlan,omitempty"`
	// DeferredItemRemoval: Information for deferred item removal.
	DeferredItemRemoval *DeferredItemRemoval `json:"deferredItemRemoval,omitempty"`
	// DeferredItemReplacement: Information for deferred item replacement.
	DeferredItemReplacement *DeferredItemReplacement `json:"deferredItemReplacement,omitempty"`
	// ExpiryTime: Time at which the subscription expired or will expire unless the
	// access is extended (ex. renews).
	ExpiryTime string `json:"expiryTime,omitempty"`
	// ItemReplacement: Details of the item being replaced. This field is only
	// populated if this item replaced another item in a previous subscription and
	// is only available for 60 days after the purchase time.
	ItemReplacement *ItemReplacement `json:"itemReplacement,omitempty"`
	// LatestSuccessfulOrderId: The order id of the latest successful order
	// associated with this item. Not present if the item is not owned by the user
	// yet (e.g. the item being deferred replaced to).
	LatestSuccessfulOrderId string `json:"latestSuccessfulOrderId,omitempty"`
	// OfferDetails: The offer details for this item.
	OfferDetails *OfferDetails `json:"offerDetails,omitempty"`
	// OfferPhase: Current offer phase details for this item.
	OfferPhase *OfferPhase `json:"offerPhase,omitempty"`
	// PrepaidPlan: The item is prepaid.
	PrepaidPlan *PrepaidPlan `json:"prepaidPlan,omitempty"`
	// ProductId: The purchased product ID (for example, 'monthly001').
	ProductId string `json:"productId,omitempty"`
	// SignupPromotion: Promotion details about this item. Only set if a promotion
	// was applied during signup.
	SignupPromotion *SignupPromotion `json:"signupPromotion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoRenewingPlan") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoRenewingPlan") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchaseLineItem: Item-level info for a subscription purchase.

func (SubscriptionPurchaseLineItem) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionPurchaseLineItem) MarshalJSON() ([]byte, error)
type SubscriptionPurchaseV2 ¶
added in v0.80.0
type SubscriptionPurchaseV2 struct {
	// AcknowledgementState: The acknowledgement state of the subscription.
	//
	// Possible values:
	//   "ACKNOWLEDGEMENT_STATE_UNSPECIFIED" - Unspecified acknowledgement state.
	//   "ACKNOWLEDGEMENT_STATE_PENDING" - The subscription is not acknowledged
	// yet.
	//   "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED" - The subscription is acknowledged.
	AcknowledgementState string `json:"acknowledgementState,omitempty"`
	// CanceledStateContext: Additional context around canceled subscriptions. Only
	// present if the subscription currently has subscription_state
	// SUBSCRIPTION_STATE_CANCELED or SUBSCRIPTION_STATE_EXPIRED.
	CanceledStateContext *CanceledStateContext `json:"canceledStateContext,omitempty"`
	// Etag: Entity tag representing the current state of the subscription. The
	// developer will provide this etag for subscription actions. This etag is
	// always present for auto-renewing and prepaid subscriptions.
	Etag string `json:"etag,omitempty"`
	// ExternalAccountIdentifiers: User account identifier in the third-party
	// service.
	ExternalAccountIdentifiers *ExternalAccountIdentifiers `json:"externalAccountIdentifiers,omitempty"`
	// Kind: This kind represents a SubscriptionPurchaseV2 object in the
	// androidpublisher service.
	Kind string `json:"kind,omitempty"`
	// LatestOrderId: Deprecated: Use line_items.latest_successful_order_id
	// instead. The order id of the latest order associated with the purchase of
	// the subscription. For autoRenewing subscription, this is the order id of
	// signup order if it is not renewed yet, or the last recurring order id
	// (success, pending, or declined order). For prepaid subscription, this is the
	// order id associated with the queried purchase token.
	LatestOrderId string `json:"latestOrderId,omitempty"`
	// LineItems: Item-level info for a subscription purchase. The items in the
	// same purchase should be either all with AutoRenewingPlan or all with
	// PrepaidPlan.
	LineItems []*SubscriptionPurchaseLineItem `json:"lineItems,omitempty"`
	// LinkedPurchaseToken: The purchase token of the old subscription if this
	// subscription is one of the following: * Re-signup of a canceled but
	// non-lapsed subscription * Upgrade/downgrade from a previous subscription. *
	// Convert from prepaid to auto renewing subscription. * Convert from an auto
	// renewing subscription to prepaid. * Topup a prepaid subscription.
	LinkedPurchaseToken string `json:"linkedPurchaseToken,omitempty"`
	// OutOfAppPurchaseContext: Additional context for out of app purchases. This
	// information is only present for re-subscription purchases (subscription
	// purchases made after the previous subscription of the same product has
	// expired) made through the Google Play subscriptions center. This field will
	// be removed after you acknowledge the subscription.
	OutOfAppPurchaseContext *OutOfAppPurchaseContext `json:"outOfAppPurchaseContext,omitempty"`
	// PausedStateContext: Additional context around paused subscriptions. Only
	// present if the subscription currently has subscription_state
	// SUBSCRIPTION_STATE_PAUSED.
	PausedStateContext *PausedStateContext `json:"pausedStateContext,omitempty"`
	// RegionCode: ISO 3166-1 alpha-2 billing country/region code of the user at
	// the time the subscription was granted.
	RegionCode string `json:"regionCode,omitempty"`
	// StartTime: Time at which the subscription was granted. Not set for pending
	// subscriptions (subscription was created but awaiting payment during signup).
	StartTime string `json:"startTime,omitempty"`
	// SubscribeWithGoogleInfo: User profile associated with purchases made with
	// 'Subscribe with Google'.
	SubscribeWithGoogleInfo *SubscribeWithGoogleInfo `json:"subscribeWithGoogleInfo,omitempty"`
	// SubscriptionState: The current state of the subscription.
	//
	// Possible values:
	//   "SUBSCRIPTION_STATE_UNSPECIFIED" - Unspecified subscription state.
	//   "SUBSCRIPTION_STATE_PENDING" - Subscription was created but awaiting
	// payment during signup. In this state, all items are awaiting payment.
	//   "SUBSCRIPTION_STATE_ACTIVE" - Subscription is active. - (1) If the
	// subscription is an auto renewing plan, at least one item is
	// auto_renew_enabled and not expired. - (2) If the subscription is a prepaid
	// plan, at least one item is not expired.
	//   "SUBSCRIPTION_STATE_PAUSED" - Subscription is paused. The state is only
	// available when the subscription is an auto renewing plan. In this state, all
	// items are in paused state.
	//   "SUBSCRIPTION_STATE_IN_GRACE_PERIOD" - Subscription is in grace period.
	// The state is only available when the subscription is an auto renewing plan.
	// In this state, all items are in grace period.
	//   "SUBSCRIPTION_STATE_ON_HOLD" - Subscription is on hold (suspended). The
	// state is only available when the subscription is an auto renewing plan. In
	// this state, all items are on hold.
	//   "SUBSCRIPTION_STATE_CANCELED" - Subscription is canceled but not expired
	// yet. The state is only available when the subscription is an auto renewing
	// plan. All items have auto_renew_enabled set to false.
	//   "SUBSCRIPTION_STATE_EXPIRED" - Subscription is expired. All items have
	// expiry_time in the past.
	//   "SUBSCRIPTION_STATE_PENDING_PURCHASE_CANCELED" - Pending transaction for
	// subscription is canceled. If this pending purchase was for an existing
	// subscription, use linked_purchase_token to get the current state of that
	// subscription.
	SubscriptionState string `json:"subscriptionState,omitempty"`
	// TestPurchase: Only present if this subscription purchase is a test purchase.
	TestPurchase *TestPurchase `json:"testPurchase,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AcknowledgementState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AcknowledgementState") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchaseV2: Indicates the status of a user's subscription purchase.

func (SubscriptionPurchaseV2) MarshalJSON ¶
added in v0.80.0
func (s SubscriptionPurchaseV2) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesAcknowledgeRequest ¶
added in v0.6.0
type SubscriptionPurchasesAcknowledgeRequest struct {
	// DeveloperPayload: Payload to attach to the purchase.
	DeveloperPayload string `json:"developerPayload,omitempty"`
	// ExternalAccountIds: Optional. User account identifier in your app.
	ExternalAccountIds *ExternalAccountIds `json:"externalAccountIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeveloperPayload") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeveloperPayload") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchasesAcknowledgeRequest: Request for the purchases.subscriptions.acknowledge API.

func (SubscriptionPurchasesAcknowledgeRequest) MarshalJSON ¶
added in v0.6.0
func (s SubscriptionPurchasesAcknowledgeRequest) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesDeferRequest ¶
type SubscriptionPurchasesDeferRequest struct {
	// DeferralInfo: The information about the new desired expiry time for the
	// subscription.
	DeferralInfo *SubscriptionDeferralInfo `json:"deferralInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeferralInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeferralInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchasesDeferRequest: Request for the purchases.subscriptions.defer API.

func (SubscriptionPurchasesDeferRequest) MarshalJSON ¶
func (s SubscriptionPurchasesDeferRequest) MarshalJSON() ([]byte, error)
type SubscriptionPurchasesDeferResponse ¶
type SubscriptionPurchasesDeferResponse struct {
	// NewExpiryTimeMillis: The new expiry time for the subscription in
	// milliseconds since the Epoch.
	NewExpiryTimeMillis int64 `json:"newExpiryTimeMillis,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NewExpiryTimeMillis") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NewExpiryTimeMillis") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionPurchasesDeferResponse: Response for the purchases.subscriptions.defer API.

func (SubscriptionPurchasesDeferResponse) MarshalJSON ¶
func (s SubscriptionPurchasesDeferResponse) MarshalJSON() ([]byte, error)
type SubscriptionTaxAndComplianceSettings ¶
added in v0.60.0
type SubscriptionTaxAndComplianceSettings struct {
	// EeaWithdrawalRightType: Digital content or service classification for
	// products distributed to users in the European Economic Area (EEA). The
	// withdrawal regime under EEA consumer laws depends on this classification.
	// Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/10463498)
	// for more information.
	//
	// Possible values:
	//   "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"
	//   "WITHDRAWAL_RIGHT_DIGITAL_CONTENT"
	//   "WITHDRAWAL_RIGHT_SERVICE"
	EeaWithdrawalRightType string `json:"eeaWithdrawalRightType,omitempty"`
	// IsTokenizedDigitalAsset: Whether this subscription is declared as a product
	// representing a tokenized digital asset.
	IsTokenizedDigitalAsset bool `json:"isTokenizedDigitalAsset,omitempty"`
	// ProductTaxCategoryCode: Product tax category code to assign to the
	// subscription. Product tax category determines the transaction tax rates
	// applied to the subscription. Refer to the Help Center article
	// (https://support.google.com/googleplay/android-developer/answer/16408159)
	// for more information.
	ProductTaxCategoryCode string `json:"productTaxCategoryCode,omitempty"`
	// RegionalProductAgeRatingInfos: Regional age rating information. Currently
	// this field is only supported for region code `US`.
	RegionalProductAgeRatingInfos []*RegionalProductAgeRatingInfo `json:"regionalProductAgeRatingInfos,omitempty"`
	// TaxRateInfoByRegionCode: A mapping from region code to tax rate details. The
	// keys are region codes as defined by Unicode's "CLDR".
	TaxRateInfoByRegionCode map[string]RegionalTaxRateInfo `json:"taxRateInfoByRegionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EeaWithdrawalRightType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EeaWithdrawalRightType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscriptionTaxAndComplianceSettings: Details about taxation, Google Play policy, and legal compliance for subscription products.

func (SubscriptionTaxAndComplianceSettings) MarshalJSON ¶
added in v0.60.0
func (s SubscriptionTaxAndComplianceSettings) MarshalJSON() ([]byte, error)
type SystemApkOptions ¶
added in v0.139.0
type SystemApkOptions struct {
	// Rotated: Whether to use the rotated key for signing the system APK.
	Rotated bool `json:"rotated,omitempty"`
	// UncompressedDexFiles: Whether system APK was generated with uncompressed dex
	// files.
	UncompressedDexFiles bool `json:"uncompressedDexFiles,omitempty"`
	// UncompressedNativeLibraries: Whether system APK was generated with
	// uncompressed native libraries.
	UncompressedNativeLibraries bool `json:"uncompressedNativeLibraries,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Rotated") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Rotated") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SystemApkOptions: Options for system APKs.

func (SystemApkOptions) MarshalJSON ¶
added in v0.139.0
func (s SystemApkOptions) MarshalJSON() ([]byte, error)
type SystemApksListResponse ¶
added in v0.29.0
type SystemApksListResponse struct {
	// Variants: All system APK variants created.
	Variants []*Variant `json:"variants,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Variants") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Variants") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SystemApksListResponse: Response to list previously created system APK variants.

func (SystemApksListResponse) MarshalJSON ¶
added in v0.29.0
func (s SystemApksListResponse) MarshalJSON() ([]byte, error)
type SystemFeature ¶
added in v0.74.0
type SystemFeature struct {
	// Name: The name of the feature.
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

SystemFeature: Representation of a system feature.

func (SystemFeature) MarshalJSON ¶
added in v0.74.0
func (s SystemFeature) MarshalJSON() ([]byte, error)
type SystemInitiatedCancellation ¶
added in v0.80.0
type SystemInitiatedCancellation struct {
}

SystemInitiatedCancellation: Information specific to cancellations initiated by Google system.

type SystemOnChip ¶
added in v0.202.0
type SystemOnChip struct {
	// Manufacturer: Required. The designer of the SoC, eg. "Google" Value of build
	// property "ro.soc.manufacturer"
	// https://developer.android.com/reference/android/os/Build#SOC_MANUFACTURER
	// Required.
	Manufacturer string `json:"manufacturer,omitempty"`
	// Model: Required. The model of the SoC, eg. "Tensor" Value of build property
	// "ro.soc.model"
	// https://developer.android.com/reference/android/os/Build#SOC_MODEL Required.
	Model string `json:"model,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Manufacturer") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Manufacturer") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SystemOnChip: Representation of a System-on-Chip (SoC) of an Android device. Can be used to target S+ devices.

func (SystemOnChip) MarshalJSON ¶
added in v0.202.0
func (s SystemOnChip) MarshalJSON() ([]byte, error)
type SystemapksService ¶
added in v0.16.0
type SystemapksService struct {
	Variants *SystemapksVariantsService
	// contains filtered or unexported fields
}
func NewSystemapksService ¶
added in v0.16.0
func NewSystemapksService(s *Service) *SystemapksService
type SystemapksVariantsCreateCall ¶
added in v0.16.0
type SystemapksVariantsCreateCall struct {
	// contains filtered or unexported fields
}
func (*SystemapksVariantsCreateCall) Context ¶
added in v0.16.0
func (c *SystemapksVariantsCreateCall) Context(ctx context.Context) *SystemapksVariantsCreateCall

Context sets the context to be used in this call's Do method.

func (*SystemapksVariantsCreateCall) Do ¶
added in v0.16.0
func (c *SystemapksVariantsCreateCall) Do(opts ...googleapi.CallOption) (*Variant, error)

Do executes the "androidpublisher.systemapks.variants.create" call. Any non-2xx status code is an error. Response headers are in either *Variant.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SystemapksVariantsCreateCall) Fields ¶
added in v0.16.0
func (c *SystemapksVariantsCreateCall) Fields(s ...googleapi.Field) *SystemapksVariantsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SystemapksVariantsCreateCall) Header ¶
added in v0.16.0
func (c *SystemapksVariantsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type SystemapksVariantsDownloadCall ¶
added in v0.16.0
type SystemapksVariantsDownloadCall struct {
	// contains filtered or unexported fields
}
func (*SystemapksVariantsDownloadCall) Context ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) Context(ctx context.Context) *SystemapksVariantsDownloadCall

Context sets the context to be used in this call's Do and Download methods.

func (*SystemapksVariantsDownloadCall) Do ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.systemapks.variants.download" call.

func (*SystemapksVariantsDownloadCall) Download ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) Download(opts ...googleapi.CallOption) (*http.Response, error)

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

func (*SystemapksVariantsDownloadCall) Fields ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) Fields(s ...googleapi.Field) *SystemapksVariantsDownloadCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SystemapksVariantsDownloadCall) Header ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*SystemapksVariantsDownloadCall) IfNoneMatch ¶
added in v0.16.0
func (c *SystemapksVariantsDownloadCall) IfNoneMatch(entityTag string) *SystemapksVariantsDownloadCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type SystemapksVariantsGetCall ¶
added in v0.16.0
type SystemapksVariantsGetCall struct {
	// contains filtered or unexported fields
}
func (*SystemapksVariantsGetCall) Context ¶
added in v0.16.0
func (c *SystemapksVariantsGetCall) Context(ctx context.Context) *SystemapksVariantsGetCall

Context sets the context to be used in this call's Do method.

func (*SystemapksVariantsGetCall) Do ¶
added in v0.16.0
func (c *SystemapksVariantsGetCall) Do(opts ...googleapi.CallOption) (*Variant, error)

Do executes the "androidpublisher.systemapks.variants.get" call. Any non-2xx status code is an error. Response headers are in either *Variant.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SystemapksVariantsGetCall) Fields ¶
added in v0.16.0
func (c *SystemapksVariantsGetCall) Fields(s ...googleapi.Field) *SystemapksVariantsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SystemapksVariantsGetCall) Header ¶
added in v0.16.0
func (c *SystemapksVariantsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*SystemapksVariantsGetCall) IfNoneMatch ¶
added in v0.16.0
func (c *SystemapksVariantsGetCall) IfNoneMatch(entityTag string) *SystemapksVariantsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type SystemapksVariantsListCall ¶
added in v0.16.0
type SystemapksVariantsListCall struct {
	// contains filtered or unexported fields
}
func (*SystemapksVariantsListCall) Context ¶
added in v0.16.0
func (c *SystemapksVariantsListCall) Context(ctx context.Context) *SystemapksVariantsListCall

Context sets the context to be used in this call's Do method.

func (*SystemapksVariantsListCall) Do ¶
added in v0.16.0
func (c *SystemapksVariantsListCall) Do(opts ...googleapi.CallOption) (*SystemApksListResponse, error)

Do executes the "androidpublisher.systemapks.variants.list" call. Any non-2xx status code is an error. Response headers are in either *SystemApksListResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SystemapksVariantsListCall) Fields ¶
added in v0.16.0
func (c *SystemapksVariantsListCall) Fields(s ...googleapi.Field) *SystemapksVariantsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*SystemapksVariantsListCall) Header ¶
added in v0.16.0
func (c *SystemapksVariantsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*SystemapksVariantsListCall) IfNoneMatch ¶
added in v0.16.0
func (c *SystemapksVariantsListCall) IfNoneMatch(entityTag string) *SystemapksVariantsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type SystemapksVariantsService ¶
added in v0.16.0
type SystemapksVariantsService struct {
	// contains filtered or unexported fields
}
func NewSystemapksVariantsService ¶
added in v0.16.0
func NewSystemapksVariantsService(s *Service) *SystemapksVariantsService
func (*SystemapksVariantsService) Create ¶
added in v0.16.0
func (r *SystemapksVariantsService) Create(packageName string, versionCode int64, variant *Variant) *SystemapksVariantsCreateCall

Create: Creates an APK which is suitable for inclusion in a system image from an already uploaded Android App Bundle.

- packageName: Package name of the app. - versionCode: The version code of the App Bundle.

func (*SystemapksVariantsService) Download ¶
added in v0.16.0
func (r *SystemapksVariantsService) Download(packageName string, versionCode int64, variantId int64) *SystemapksVariantsDownloadCall

Download: Downloads a previously created system APK which is suitable for inclusion in a system image.

- packageName: Package name of the app. - variantId: The ID of a previously created system APK variant. - versionCode: The version code of the App Bundle.

func (*SystemapksVariantsService) Get ¶
added in v0.16.0
func (r *SystemapksVariantsService) Get(packageName string, versionCode int64, variantId int64) *SystemapksVariantsGetCall

Get: Returns a previously created system APK variant.

- packageName: Package name of the app. - variantId: The ID of a previously created system APK variant. - versionCode: The version code of the App Bundle.

func (*SystemapksVariantsService) List ¶
added in v0.16.0
func (r *SystemapksVariantsService) List(packageName string, versionCode int64) *SystemapksVariantsListCall

List: Returns the list of previously created system APK variants.

- packageName: Package name of the app. - versionCode: The version code of the App Bundle.

type Targeting ¶
added in v0.156.0
type Targeting struct {
	// AllUsers: All users are targeted.
	AllUsers *AllUsers `json:"allUsers,omitempty"`
	// AndroidSdks: Targeting is based on android api levels of devices.
	AndroidSdks *AndroidSdks `json:"androidSdks,omitempty"`
	// Regions: Targeting is based on the user account region.
	Regions *Regions `json:"regions,omitempty"`
	// VersionList: Target version codes as a list.
	VersionList *AppVersionList `json:"versionList,omitempty"`
	// VersionRange: Target version codes as a range.
	VersionRange *AppVersionRange `json:"versionRange,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllUsers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllUsers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Targeting: Targeting details for a recovery action such as regions, android sdk levels, app versions etc.

func (Targeting) MarshalJSON ¶
added in v0.156.0
func (s Targeting) MarshalJSON() ([]byte, error)
type TargetingInfo ¶
added in v0.130.0
type TargetingInfo struct {
	// AssetSliceSet: List of created asset slices.
	AssetSliceSet []*AssetSliceSet `json:"assetSliceSet,omitempty"`
	// PackageName: The package name of this app.
	PackageName string `json:"packageName,omitempty"`
	// Variant: List of the created variants.
	Variant []*SplitApkVariant `json:"variant,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AssetSliceSet") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssetSliceSet") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetingInfo: Targeting information about the generated apks.

func (TargetingInfo) MarshalJSON ¶
added in v0.130.0
func (s TargetingInfo) MarshalJSON() ([]byte, error)
type TargetingRuleScope ¶
added in v0.80.0
type TargetingRuleScope struct {
	// AnySubscriptionInApp: The scope of the current targeting rule is any
	// subscription in the parent app.
	AnySubscriptionInApp *TargetingRuleScopeAnySubscriptionInApp `json:"anySubscriptionInApp,omitempty"`
	// SpecificSubscriptionInApp: The scope of the current targeting rule is the
	// subscription with the specified subscription ID. Must be a subscription
	// within the same parent app.
	SpecificSubscriptionInApp string `json:"specificSubscriptionInApp,omitempty"`
	// ThisSubscription: The scope of the current targeting rule is the
	// subscription in which this offer is defined.
	ThisSubscription *TargetingRuleScopeThisSubscription `json:"thisSubscription,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AnySubscriptionInApp") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AnySubscriptionInApp") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetingRuleScope: Defines the scope of subscriptions which a targeting rule can match to target offers to users based on past or current entitlement.

func (TargetingRuleScope) MarshalJSON ¶
added in v0.80.0
func (s TargetingRuleScope) MarshalJSON() ([]byte, error)
type TargetingRuleScopeAnySubscriptionInApp ¶
added in v0.173.0
type TargetingRuleScopeAnySubscriptionInApp struct {
}

TargetingRuleScopeAnySubscriptionInApp: Represents the targeting rule scope corresponding to any subscription in the parent app.

type TargetingRuleScopeThisSubscription ¶
added in v0.173.0
type TargetingRuleScopeThisSubscription struct {
}

TargetingRuleScopeThisSubscription: Represents the targeting rule scope corresponding to the subscriptions in which this offer is defined.

type TargetingUpdate ¶
added in v0.156.0
type TargetingUpdate struct {
	// AllUsers: All users are targeted.
	AllUsers *AllUsers `json:"allUsers,omitempty"`
	// AndroidSdks: Additional android sdk levels are targeted by the recovery
	// action.
	AndroidSdks *AndroidSdks `json:"androidSdks,omitempty"`
	// Regions: Additional regions are targeted by the recovery action.
	Regions *Regions `json:"regions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllUsers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllUsers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetingUpdate: Update type for targeting. Note it is always a subset Targeting.

func (TargetingUpdate) MarshalJSON ¶
added in v0.156.0
func (s TargetingUpdate) MarshalJSON() ([]byte, error)
type TestPurchase ¶
added in v0.80.0
type TestPurchase struct {
}

TestPurchase: Whether this subscription purchase is a test purchase.

type TestPurchaseContext ¶
added in v0.240.0
type TestPurchaseContext struct {
	// FopType: The fop type of the test purchase.
	//
	// Possible values:
	//   "FOP_TYPE_UNSPECIFIED" - Fop type unspecified. This value should never be
	// set.
	//   "TEST" - The purchase was made using a test card.
	FopType string `json:"fopType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FopType") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FopType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TestPurchaseContext: Context about a test purchase.

func (TestPurchaseContext) MarshalJSON ¶
added in v0.240.0
func (s TestPurchaseContext) MarshalJSON() ([]byte, error)
type Testers ¶
type Testers struct {
	// GoogleGroups: All testing Google Groups, as email addresses.
	GoogleGroups []string `json:"googleGroups,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GoogleGroups") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GoogleGroups") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Testers: The testers of an app. The resource for TestersService. Note: while it is possible in the Play Console UI to add testers via email lists, email lists are not supported by this resource.

func (Testers) MarshalJSON ¶
func (s Testers) MarshalJSON() ([]byte, error)
type TextureCompressionFormat ¶
added in v0.130.0
type TextureCompressionFormat struct {
	// Alias: Alias for texture compression format.
	//
	// Possible values:
	//   "UNSPECIFIED_TEXTURE_COMPRESSION_FORMAT" - Unspecified format.
	//   "ETC1_RGB8" - ETC1_RGB8 format.
	//   "PALETTED" - PALETTED format.
	//   "THREE_DC" - THREE_DC format.
	//   "ATC" - ATC format.
	//   "LATC" - LATC format.
	//   "DXT1" - DXT1 format.
	//   "S3TC" - S3TC format.
	//   "PVRTC" - PVRTC format.
	//   "ASTC" - ASTC format.
	//   "ETC2" - ETC2 format.
	Alias string `json:"alias,omitempty"`
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

TextureCompressionFormat: Represents texture compression format.

func (TextureCompressionFormat) MarshalJSON ¶
added in v0.130.0
func (s TextureCompressionFormat) MarshalJSON() ([]byte, error)
type TextureCompressionFormatTargeting ¶
added in v0.130.0
type TextureCompressionFormatTargeting struct {
	// Alternatives: List of alternative TCFs (TCFs targeted by the sibling
	// splits).
	Alternatives []*TextureCompressionFormat `json:"alternatives,omitempty"`
	// Value: The list of targeted TCFs. Should not be empty.
	Value []*TextureCompressionFormat `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Alternatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Alternatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TextureCompressionFormatTargeting: Targeting by a texture compression format.

func (TextureCompressionFormatTargeting) MarshalJSON ¶
added in v0.130.0
func (s TextureCompressionFormatTargeting) MarshalJSON() ([]byte, error)
type Timestamp ¶
type Timestamp struct {
	// Nanos: Non-negative fractions of a second at nanosecond resolution. Must be
	// from 0 to 999,999,999 inclusive.
	Nanos int64 `json:"nanos,omitempty"`
	// Seconds: Represents seconds of UTC time since Unix epoch.
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

Timestamp: A Timestamp represents a point in time independent of any time zone or local calendar, encoded as a count of seconds and fractions of seconds at nanosecond resolution. The count is relative to an epoch at UTC midnight on January 1, 1970.

func (Timestamp) MarshalJSON ¶
func (s Timestamp) MarshalJSON() ([]byte, error)
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
type Track ¶
type Track struct {
	// Releases: In a read request, represents all active releases in the track. In
	// an update request, represents desired changes.
	Releases []*TrackRelease `json:"releases,omitempty"`
	// Track: Identifier of the track. Form factor tracks have a special prefix as
	// an identifier, for example `wear:production`, `automotive:production`. More
	// on track name
	// (https://developers.google.com/android-publisher/tracks#ff-track-name)
	Track string `json:"track,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Releases") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Releases") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Track: A track configuration. The resource for TracksService.

func (Track) MarshalJSON ¶
func (s Track) MarshalJSON() ([]byte, error)
type TrackConfig ¶
added in v0.151.0
type TrackConfig struct {
	// FormFactor: Required. Form factor of the new track. Defaults to the default
	// track.
	//
	// Possible values:
	//   "FORM_FACTOR_UNSPECIFIED" - Fallback value, do not use.
	//   "DEFAULT" - Default track.
	//   "WEAR" - Wear form factor track.
	//   "AUTOMOTIVE" - Automotive form factor track.
	FormFactor string `json:"formFactor,omitempty"`
	// Track: Required. Identifier of the new track. For default tracks, this field
	// consists of the track alias only. Form factor tracks have a special prefix
	// as an identifier, for example `wear:production`, `automotive:production`.
	// This prefix must match the value of the `form_factor` field, if it is not a
	// default track. More on track name
	// (https://developers.google.com/android-publisher/tracks#ff-track-name)
	Track string `json:"track,omitempty"`
	// Type: Required. Type of the new track. Currently, the only supported value
	// is closedTesting.
	//
	// Possible values:
	//   "TRACK_TYPE_UNSPECIFIED" - Fallback value, do not use.
	//   "CLOSED_TESTING" - Closed testing track.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FormFactor") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FormFactor") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrackConfig: Configurations of the new track.

func (TrackConfig) MarshalJSON ¶
added in v0.151.0
func (s TrackConfig) MarshalJSON() ([]byte, error)
type TrackCountryAvailability ¶
added in v0.61.0
type TrackCountryAvailability struct {
	// Countries: A list of one or more countries where artifacts in this track are
	// available. This list includes all countries that are targeted by the track,
	// even if only specific carriers are targeted in that country.
	Countries []*TrackTargetedCountry `json:"countries,omitempty"`
	// RestOfWorld: Whether artifacts in this track are available to "rest of the
	// world" countries.
	RestOfWorld bool `json:"restOfWorld,omitempty"`
	// SyncWithProduction: Whether this track's availability is synced with the
	// default production track. See
	// https://support.google.com/googleplay/android-developer/answer/7550024 for
	// more information on syncing country availability with production. Note that
	// if this is true, the returned "countries" and "rest_of_world" fields will
	// reflect the values for the default production track.
	SyncWithProduction bool `json:"syncWithProduction,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Countries") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Countries") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrackCountryAvailability: Resource for per-track country availability information.

func (TrackCountryAvailability) MarshalJSON ¶
added in v0.61.0
func (s TrackCountryAvailability) MarshalJSON() ([]byte, error)
type TrackRelease ¶
type TrackRelease struct {
	// CountryTargeting: Restricts a release to a specific set of countries. Note
	// this is only allowed to be set for inProgress releases in the production
	// track.
	CountryTargeting *CountryTargeting `json:"countryTargeting,omitempty"`
	// InAppUpdatePriority: In-app update priority of the release. All newly added
	// APKs in the release will be considered at this priority. Can take values in
	// the range [0, 5], with 5 the highest priority. Defaults to 0.
	// in_app_update_priority can not be updated once the release is rolled out.
	// See https://developer.android.com/guide/playcore/in-app-updates.
	InAppUpdatePriority int64 `json:"inAppUpdatePriority,omitempty"`
	// Name: The release name. Not required to be unique. If not set, the name is
	// generated from the APK's version_name. If the release contains multiple
	// APKs, the name is generated from the date.
	Name string `json:"name,omitempty"`
	// ReleaseNotes: A description of what is new in this release.
	ReleaseNotes []*LocalizedText `json:"releaseNotes,omitempty"`
	// Status: The status of the release.
	//
	// Possible values:
	//   "statusUnspecified" - Unspecified status.
	//   "draft" - The release's APKs are not being served to users.
	//   "inProgress" - The release's APKs are being served to a fraction of users,
	// determined by 'user_fraction'.
	//   "halted" - The release's APKs will no longer be served to users. Users who
	// already have these APKs are unaffected.
	//   "completed" - The release will have no further changes. Its APKs are being
	// served to all users, unless they are eligible to APKs of a more recent
	// release.
	Status string `json:"status,omitempty"`
	// UserFraction: Fraction of users who are eligible for a staged release. 0 <
	// fraction < 1. Can only be set when status is "inProgress" or "halted".
	UserFraction float64 `json:"userFraction,omitempty"`
	// VersionCodes: Version codes of all APKs in the release. Must include version
	// codes to retain from previous releases.
	VersionCodes googleapi.Int64s `json:"versionCodes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CountryTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountryTargeting") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrackRelease: A release within a track.

func (TrackRelease) MarshalJSON ¶
func (s TrackRelease) MarshalJSON() ([]byte, error)
func (*TrackRelease) UnmarshalJSON ¶
func (s *TrackRelease) UnmarshalJSON(data []byte) error
type TrackTargetedCountry ¶
added in v0.61.0
type TrackTargetedCountry struct {
	// CountryCode: The country that can be targeted, as a two-letter CLDR code.
	CountryCode string `json:"countryCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CountryCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountryCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TrackTargetedCountry: Representation of a single country where the contents of a track can be made available.

func (TrackTargetedCountry) MarshalJSON ¶
added in v0.61.0
func (s TrackTargetedCountry) MarshalJSON() ([]byte, error)
type TracksListResponse ¶
type TracksListResponse struct {
	// Kind: The kind of this response ("androidpublisher#tracksListResponse").
	Kind string `json:"kind,omitempty"`
	// Tracks: All tracks (including tracks with no releases).
	Tracks []*Track `json:"tracks,omitempty"`

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

TracksListResponse: Response listing all tracks.

func (TracksListResponse) MarshalJSON ¶
func (s TracksListResponse) MarshalJSON() ([]byte, error)
type UpdateBasePlanStateRequest ¶
added in v0.154.0
type UpdateBasePlanStateRequest struct {
	// ActivateBasePlanRequest: Activates a base plan. Once activated, base plans
	// will be available to new subscribers.
	ActivateBasePlanRequest *ActivateBasePlanRequest `json:"activateBasePlanRequest,omitempty"`
	// DeactivateBasePlanRequest: Deactivates a base plan. Once deactivated, the
	// base plan will become unavailable to new subscribers, but existing
	// subscribers will maintain their subscription
	DeactivateBasePlanRequest *DeactivateBasePlanRequest `json:"deactivateBasePlanRequest,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActivateBasePlanRequest") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActivateBasePlanRequest") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateBasePlanStateRequest: Request message to update the state of a subscription base plan.

func (UpdateBasePlanStateRequest) MarshalJSON ¶
added in v0.154.0
func (s UpdateBasePlanStateRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductOfferRequest ¶
added in v0.244.0
type UpdateOneTimeProductOfferRequest struct {
	// AllowMissing: Optional. If set to true, and the offer with the given
	// package_name, product_id, purchase_option_id and offer_id doesn't exist, an
	// offer will be created. If a new offer is created, the update_mask is
	// ignored.
	AllowMissing bool `json:"allowMissing,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this offer update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OneTimeProductOffer: Required. The one-time product offer to update.
	OneTimeProductOffer *OneTimeProductOffer `json:"oneTimeProductOffer,omitempty"`
	// RegionsVersion: Required. The version of the available regions being used
	// for the offer.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// UpdateMask: Required. The list of fields to be updated.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowMissing") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowMissing") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateOneTimeProductOfferRequest: Request message for UpdateOneTimeProductOffer.

func (UpdateOneTimeProductOfferRequest) MarshalJSON ¶
added in v0.244.0
func (s UpdateOneTimeProductOfferRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductOfferStateRequest ¶
added in v0.244.0
type UpdateOneTimeProductOfferStateRequest struct {
	// ActivateOneTimeProductOfferRequest: Activates an offer. Once activated, the
	// offer is available to users, as long as its conditions are met.
	ActivateOneTimeProductOfferRequest *ActivateOneTimeProductOfferRequest `json:"activateOneTimeProductOfferRequest,omitempty"`
	// CancelOneTimeProductOfferRequest: Cancels an offer. Once cancelled, the
	// offer is not available to users. Any pending orders related to this offer
	// will be cancelled. This state transition is specific to pre-orders.
	CancelOneTimeProductOfferRequest *CancelOneTimeProductOfferRequest `json:"cancelOneTimeProductOfferRequest,omitempty"`
	// DeactivateOneTimeProductOfferRequest: Deactivates an offer. Once
	// deactivated, the offer is no longer available to users. This state
	// transition is specific to discounted offers.
	DeactivateOneTimeProductOfferRequest *DeactivateOneTimeProductOfferRequest `json:"deactivateOneTimeProductOfferRequest,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ActivateOneTimeProductOfferRequest") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ActivateOneTimeProductOfferRequest") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

UpdateOneTimeProductOfferStateRequest: Request message to update the state of a one-time product offer.

func (UpdateOneTimeProductOfferStateRequest) MarshalJSON ¶
added in v0.244.0
func (s UpdateOneTimeProductOfferStateRequest) MarshalJSON() ([]byte, error)
type UpdateOneTimeProductRequest ¶
added in v0.244.0
type UpdateOneTimeProductRequest struct {
	// AllowMissing: Optional. If set to true, and the one-time product with the
	// given package_name and product_id doesn't exist, the one-time product will
	// be created. If a new one-time product is created, update_mask is ignored.
	AllowMissing bool `json:"allowMissing,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product upsert. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// OneTimeProduct: Required. The one-time product to upsert.
	OneTimeProduct *OneTimeProduct `json:"oneTimeProduct,omitempty"`
	// RegionsVersion: Required. The version of the available regions being used
	// for the one-time product.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// UpdateMask: Required. The list of fields to be updated.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowMissing") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowMissing") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateOneTimeProductRequest: Request message for UpdateOneTimeProduct.

func (UpdateOneTimeProductRequest) MarshalJSON ¶
added in v0.244.0
func (s UpdateOneTimeProductRequest) MarshalJSON() ([]byte, error)
type UpdatePurchaseOptionStateRequest ¶
added in v0.244.0
type UpdatePurchaseOptionStateRequest struct {
	// ActivatePurchaseOptionRequest: Activates a purchase option. Once activated,
	// the purchase option will be available.
	ActivatePurchaseOptionRequest *ActivatePurchaseOptionRequest `json:"activatePurchaseOptionRequest,omitempty"`
	// DeactivatePurchaseOptionRequest: Deactivates a purchase option. Once
	// deactivated, the purchase option will become unavailable.
	DeactivatePurchaseOptionRequest *DeactivatePurchaseOptionRequest `json:"deactivatePurchaseOptionRequest,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ActivatePurchaseOptionRequest") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActivatePurchaseOptionRequest")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdatePurchaseOptionStateRequest: Request message to update the state of a one-time product purchase option.

func (UpdatePurchaseOptionStateRequest) MarshalJSON ¶
added in v0.244.0
func (s UpdatePurchaseOptionStateRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionOfferRequest ¶
added in v0.154.0
type UpdateSubscriptionOfferRequest struct {
	// AllowMissing: Optional. If set to true, and the subscription offer with the
	// given package_name, product_id, base_plan_id and offer_id doesn't exist, an
	// offer will be created. If a new offer is created, update_mask is ignored.
	AllowMissing bool `json:"allowMissing,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// RegionsVersion: Required. The version of the available regions being used
	// for the subscription_offer.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// SubscriptionOffer: Required. The subscription offer to update.
	SubscriptionOffer *SubscriptionOffer `json:"subscriptionOffer,omitempty"`
	// UpdateMask: Required. The list of fields to be updated.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowMissing") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowMissing") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateSubscriptionOfferRequest: Request message for UpdateSubscriptionOffer.

func (UpdateSubscriptionOfferRequest) MarshalJSON ¶
added in v0.154.0
func (s UpdateSubscriptionOfferRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionOfferStateRequest ¶
added in v0.154.0
type UpdateSubscriptionOfferStateRequest struct {
	// ActivateSubscriptionOfferRequest: Activates an offer. Once activated, the
	// offer will be available to new subscribers.
	ActivateSubscriptionOfferRequest *ActivateSubscriptionOfferRequest `json:"activateSubscriptionOfferRequest,omitempty"`
	// DeactivateSubscriptionOfferRequest: Deactivates an offer. Once deactivated,
	// the offer will become unavailable to new subscribers, but existing
	// subscribers will maintain their subscription
	DeactivateSubscriptionOfferRequest *DeactivateSubscriptionOfferRequest `json:"deactivateSubscriptionOfferRequest,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "ActivateSubscriptionOfferRequest") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "ActivateSubscriptionOfferRequest") to include in API requests with the JSON
	// null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

UpdateSubscriptionOfferStateRequest: Request message to update the state of a subscription offer.

func (UpdateSubscriptionOfferStateRequest) MarshalJSON ¶
added in v0.154.0
func (s UpdateSubscriptionOfferStateRequest) MarshalJSON() ([]byte, error)
type UpdateSubscriptionRequest ¶
added in v0.154.0
type UpdateSubscriptionRequest struct {
	// AllowMissing: Optional. If set to true, and the subscription with the given
	// package_name and product_id doesn't exist, the subscription will be created.
	// If a new subscription is created, update_mask is ignored.
	AllowMissing bool `json:"allowMissing,omitempty"`
	// LatencyTolerance: Optional. The latency tolerance for the propagation of
	// this product update. Defaults to latency-sensitive.
	//
	// Possible values:
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED" - Defaults to
	// PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE" - The update will
	// propagate to clients within several minutes on average and up to a few hours
	// in rare cases. Throughput is limited to 7,200 updates per app per hour.
	//   "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT" - The update will
	// propagate to clients within 24 hours. Supports high throughput of up to
	// 720,000 updates per app per hour using batch modification methods.
	LatencyTolerance string `json:"latencyTolerance,omitempty"`
	// RegionsVersion: Required. The version of the available regions being used
	// for the subscription.
	RegionsVersion *RegionsVersion `json:"regionsVersion,omitempty"`
	// Subscription: Required. The subscription to update.
	Subscription *Subscription `json:"subscription,omitempty"`
	// UpdateMask: Required. The list of fields to be updated.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowMissing") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowMissing") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateSubscriptionRequest: Request message for UpdateSubscription.

func (UpdateSubscriptionRequest) MarshalJSON ¶
added in v0.154.0
func (s UpdateSubscriptionRequest) MarshalJSON() ([]byte, error)
type UpgradeTargetingRule ¶
added in v0.80.0
type UpgradeTargetingRule struct {
	// BillingPeriodDuration: The specific billing period duration, specified in
	// ISO 8601 format, that a user must be currently subscribed to to be eligible
	// for this rule. If not specified, users subscribed to any billing period are
	// matched.
	BillingPeriodDuration string `json:"billingPeriodDuration,omitempty"`
	// OncePerUser: Limit this offer to only once per user. If set to true, a user
	// can never be eligible for this offer again if they ever subscribed to this
	// offer.
	OncePerUser bool `json:"oncePerUser,omitempty"`
	// Scope: Required. The scope of subscriptions this rule considers. Only allows
	// "this subscription" and "specific subscription in app".
	Scope *TargetingRuleScope `json:"scope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BillingPeriodDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BillingPeriodDuration") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpgradeTargetingRule: Represents a targeting rule of the form: User currently has {scope} [with billing period {billing_period}].

func (UpgradeTargetingRule) MarshalJSON ¶
added in v0.80.0
func (s UpgradeTargetingRule) MarshalJSON() ([]byte, error)
type User ¶
added in v0.59.0
type User struct {
	// AccessState: Output only. The state of the user's access to the Play
	// Console.
	//
	// Possible values:
	//   "ACCESS_STATE_UNSPECIFIED" - Unknown or unspecified access state.
	//   "INVITED" - User is invited but has not yet accepted the invitation.
	//   "INVITATION_EXPIRED" - Invitation has expired.
	//   "ACCESS_GRANTED" - User has accepted an invitation and has access to the
	// Play Console.
	//   "ACCESS_EXPIRED" - Account access has expired.
	AccessState string `json:"accessState,omitempty"`
	// DeveloperAccountPermissions: Permissions for the user which apply across the
	// developer account.
	//
	// Possible values:
	//   "DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED" - Unknown or unspecified
	// permission.
	//   "CAN_SEE_ALL_APPS" - View app information and download bulk reports
	// (read-only). Deprecated: Check CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL.
	//   "CAN_VIEW_FINANCIAL_DATA_GLOBAL" - View financial data, orders, and
	// cancellation survey responses.
	//   "CAN_MANAGE_PERMISSIONS_GLOBAL" - Admin (all permissions).
	//   "CAN_EDIT_GAMES_GLOBAL" - Edit Play Games Services projects.
	//   "CAN_PUBLISH_GAMES_GLOBAL" - Publish Play Games Services projects.
	//   "CAN_REPLY_TO_REVIEWS_GLOBAL" - Reply to reviews.
	//   "CAN_MANAGE_PUBLIC_APKS_GLOBAL" - Release to production, exclude devices,
	// and use app signing by Google Play.
	//   "CAN_MANAGE_TRACK_APKS_GLOBAL" - Release to testing tracks.
	//   "CAN_MANAGE_TRACK_USERS_GLOBAL" - Manage testing tracks and edit tester
	// lists.
	//   "CAN_MANAGE_PUBLIC_LISTING_GLOBAL" - Manage store presence.
	//   "CAN_MANAGE_DRAFT_APPS_GLOBAL" - Create, edit, and delete draft apps.
	//   "CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL" - Create and publish private apps to
	// your organization.
	//   "CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL" - Choose whether apps are public,
	// or only available to your organization.
	//   "CAN_MANAGE_ORDERS_GLOBAL" - Manage orders and subscriptions.
	//   "CAN_MANAGE_APP_CONTENT_GLOBAL" - Manage policy related pages on all apps
	// for the developer.
	//   "CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL" - View app information and download
	// bulk reports (read-only).
	//   "CAN_VIEW_APP_QUALITY_GLOBAL" - View app quality information for all apps
	// for the developer.
	//   "CAN_MANAGE_DEEPLINKS_GLOBAL" - Manage the deep links setup for all apps
	// for the developer.
	DeveloperAccountPermissions []string `json:"developerAccountPermissions,omitempty"`
	// Email: Immutable. The user's email address.
	Email string `json:"email,omitempty"`
	// ExpirationTime: The time at which the user's access expires, if set. When
	// setting this value, it must always be in the future.
	ExpirationTime string `json:"expirationTime,omitempty"`
	// Grants: Output only. Per-app permissions for the user.
	Grants []*Grant `json:"grants,omitempty"`
	// Name: Required. Resource name for this user, following the pattern
	// "developers/{developer}/users/{email}".
	Name string `json:"name,omitempty"`
	// Partial: Output only. Whether there are more permissions for the user that
	// are not represented here. This can happen if the caller does not have
	// permission to manage all apps in the account. This is also `true` if this
	// user is the account owner. If this field is `true`, it should be taken as a
	// signal that this user cannot be fully managed via the API. That is, the API
	// caller is not be able to manage all of the permissions this user holds,
	// either because it doesn't know about them or because the user is the account
	// owner.
	Partial bool `json:"partial,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessState") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessState") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

User: A user resource.

func (User) MarshalJSON ¶
added in v0.59.0
func (s User) MarshalJSON() ([]byte, error)
type UserComment ¶
type UserComment struct {
	// AndroidOsVersion: Integer Android SDK version of the user's device at the
	// time the review was written, e.g. 23 is Marshmallow. May be absent.
	AndroidOsVersion int64 `json:"androidOsVersion,omitempty"`
	// AppVersionCode: Integer version code of the app as installed at the time the
	// review was written. May be absent.
	AppVersionCode int64 `json:"appVersionCode,omitempty"`
	// AppVersionName: String version name of the app as installed at the time the
	// review was written. May be absent.
	AppVersionName string `json:"appVersionName,omitempty"`
	// Device: Codename for the reviewer's device, e.g. klte, flounder. May be
	// absent.
	Device string `json:"device,omitempty"`
	// DeviceMetadata: Information about the characteristics of the user's device.
	DeviceMetadata *DeviceMetadata `json:"deviceMetadata,omitempty"`
	// LastModified: The last time at which this comment was updated.
	LastModified *Timestamp `json:"lastModified,omitempty"`
	// OriginalText: Untranslated text of the review, where the review was
	// translated. If the review was not translated this is left blank.
	OriginalText string `json:"originalText,omitempty"`
	// ReviewerLanguage: Language code for the reviewer. This is taken from the
	// device settings so is not guaranteed to match the language the review is
	// written in. May be absent.
	ReviewerLanguage string `json:"reviewerLanguage,omitempty"`
	// StarRating: The star rating associated with the review, from 1 to 5.
	StarRating int64 `json:"starRating,omitempty"`
	// Text: The content of the comment, i.e. review body. In some cases users have
	// been able to write a review with separate title and body; in those cases the
	// title and body are concatenated and separated by a tab character.
	Text string `json:"text,omitempty"`
	// ThumbsDownCount: Number of users who have given this review a thumbs down.
	ThumbsDownCount int64 `json:"thumbsDownCount,omitempty"`
	// ThumbsUpCount: Number of users who have given this review a thumbs up.
	ThumbsUpCount int64 `json:"thumbsUpCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AndroidOsVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndroidOsVersion") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserComment: User entry from conversation between user and developer.

func (UserComment) MarshalJSON ¶
func (s UserComment) MarshalJSON() ([]byte, error)
type UserCountriesTargeting ¶
added in v0.130.0
type UserCountriesTargeting struct {
	// CountryCodes: List of country codes in the two-letter CLDR territory format.
	CountryCodes []string `json:"countryCodes,omitempty"`
	// Exclude: Indicates if the list above is exclusive.
	Exclude bool `json:"exclude,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CountryCodes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountryCodes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserCountriesTargeting: Describes an inclusive/exclusive list of country codes that module targets.

func (UserCountriesTargeting) MarshalJSON ¶
added in v0.130.0
func (s UserCountriesTargeting) MarshalJSON() ([]byte, error)
type UserCountrySet ¶
added in v0.110.0
type UserCountrySet struct {
	// CountryCodes: List of country codes representing countries. A Country code
	// is represented in ISO 3166 alpha-2 format. For Example:- "IT" for Italy,
	// "GE" for Georgia.
	CountryCodes []string `json:"countryCodes,omitempty"`
	// Name: Country set name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CountryCodes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountryCodes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserCountrySet: A set of user countries. A country set determines what variation of app content gets served to a specific location.

func (UserCountrySet) MarshalJSON ¶
added in v0.110.0
func (s UserCountrySet) MarshalJSON() ([]byte, error)
type UserInitiatedCancellation ¶
added in v0.80.0
type UserInitiatedCancellation struct {
	// CancelSurveyResult: Information provided by the user when they complete the
	// subscription cancellation flow (cancellation reason survey).
	CancelSurveyResult *CancelSurveyResult `json:"cancelSurveyResult,omitempty"`
	// CancelTime: The time at which the subscription was canceled by the user. The
	// user might still have access to the subscription after this time. Use
	// line_items.expiry_time to determine if a user still has access.
	CancelTime string `json:"cancelTime,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CancelSurveyResult") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CancelSurveyResult") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserInitiatedCancellation: Information specific to cancellations initiated by users.

func (UserInitiatedCancellation) MarshalJSON ¶
added in v0.80.0
func (s UserInitiatedCancellation) MarshalJSON() ([]byte, error)
type UsersCreateCall ¶
added in v0.59.0
type UsersCreateCall struct {
	// contains filtered or unexported fields
}
func (*UsersCreateCall) Context ¶
added in v0.59.0
func (c *UsersCreateCall) Context(ctx context.Context) *UsersCreateCall

Context sets the context to be used in this call's Do method.

func (*UsersCreateCall) Do ¶
added in v0.59.0
func (c *UsersCreateCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "androidpublisher.users.create" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersCreateCall) Fields ¶
added in v0.59.0
func (c *UsersCreateCall) Fields(s ...googleapi.Field) *UsersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersCreateCall) Header ¶
added in v0.59.0
func (c *UsersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersDeleteCall ¶
added in v0.59.0
type UsersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*UsersDeleteCall) Context ¶
added in v0.59.0
func (c *UsersDeleteCall) Context(ctx context.Context) *UsersDeleteCall

Context sets the context to be used in this call's Do method.

func (*UsersDeleteCall) Do ¶
added in v0.59.0
func (c *UsersDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "androidpublisher.users.delete" call.

func (*UsersDeleteCall) Fields ¶
added in v0.59.0
func (c *UsersDeleteCall) Fields(s ...googleapi.Field) *UsersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersDeleteCall) Header ¶
added in v0.59.0
func (c *UsersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UsersListCall ¶
added in v0.59.0
type UsersListCall struct {
	// contains filtered or unexported fields
}
func (*UsersListCall) Context ¶
added in v0.59.0
func (c *UsersListCall) Context(ctx context.Context) *UsersListCall

Context sets the context to be used in this call's Do method.

func (*UsersListCall) Do ¶
added in v0.59.0
func (c *UsersListCall) Do(opts ...googleapi.CallOption) (*ListUsersResponse, error)

Do executes the "androidpublisher.users.list" call. Any non-2xx status code is an error. Response headers are in either *ListUsersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersListCall) Fields ¶
added in v0.59.0
func (c *UsersListCall) Fields(s ...googleapi.Field) *UsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersListCall) Header ¶
added in v0.59.0
func (c *UsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersListCall) IfNoneMatch ¶
added in v0.59.0
func (c *UsersListCall) IfNoneMatch(entityTag string) *UsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*UsersListCall) PageSize ¶
added in v0.59.0
func (c *UsersListCall) PageSize(pageSize int64) *UsersListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. This must be set to -1 to disable pagination.

func (*UsersListCall) PageToken ¶
added in v0.59.0
func (c *UsersListCall) PageToken(pageToken string) *UsersListCall

PageToken sets the optional parameter "pageToken": A token received from a previous call to this method, in order to retrieve further results.

func (*UsersListCall) Pages ¶
added in v0.59.0
func (c *UsersListCall) Pages(ctx context.Context, f func(*ListUsersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type UsersPatchCall ¶
added in v0.59.0
type UsersPatchCall struct {
	// contains filtered or unexported fields
}
func (*UsersPatchCall) Context ¶
added in v0.59.0
func (c *UsersPatchCall) Context(ctx context.Context) *UsersPatchCall

Context sets the context to be used in this call's Do method.

func (*UsersPatchCall) Do ¶
added in v0.59.0
func (c *UsersPatchCall) Do(opts ...googleapi.CallOption) (*User, error)

Do executes the "androidpublisher.users.patch" call. Any non-2xx status code is an error. Response headers are in either *User.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UsersPatchCall) Fields ¶
added in v0.59.0
func (c *UsersPatchCall) Fields(s ...googleapi.Field) *UsersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UsersPatchCall) Header ¶
added in v0.59.0
func (c *UsersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*UsersPatchCall) UpdateMask ¶
added in v0.59.0
func (c *UsersPatchCall) UpdateMask(updateMask string) *UsersPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to be updated.

type UsersService ¶
added in v0.59.0
type UsersService struct {
	// contains filtered or unexported fields
}
func NewUsersService ¶
added in v0.59.0
func NewUsersService(s *Service) *UsersService
func (*UsersService) Create ¶
added in v0.59.0
func (r *UsersService) Create(parent string, user *User) *UsersCreateCall

Create: Grant access for a user to the given developer account.

parent: The developer account to add the user to. Format: developers/{developer}.
func (*UsersService) Delete ¶
added in v0.59.0
func (r *UsersService) Delete(name string) *UsersDeleteCall

Delete: Removes all access for the user to the given developer account.

name: The name of the user to delete. Format: developers/{developer}/users/{email}.
func (*UsersService) List ¶
added in v0.59.0
func (r *UsersService) List(parent string) *UsersListCall

List: Lists all users with access to a developer account.

parent: The developer account to fetch users from. Format: developers/{developer}.
func (*UsersService) Patch ¶
added in v0.59.0
func (r *UsersService) Patch(name string, user *User) *UsersPatchCall

Patch: Updates access for the user to the developer account.

name: Resource name for this user, following the pattern "developers/{developer}/users/{email}".
type UsesPermission ¶
added in v0.27.0
type UsesPermission struct {
	// MaxSdkVersion: Optionally, the maximum SDK version for which the permission
	// is required.
	MaxSdkVersion int64 `json:"maxSdkVersion,omitempty"`
	// Name: The name of the permission requested.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaxSdkVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxSdkVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UsesPermission: A permission used by this APK.

func (UsesPermission) MarshalJSON ¶
added in v0.27.0
func (s UsesPermission) MarshalJSON() ([]byte, error)
type VanityCode ¶
added in v0.210.0
type VanityCode struct {
	// PromotionCode: The promotion code.
	PromotionCode string `json:"promotionCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PromotionCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PromotionCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VanityCode: A multiple use, predefined promotion code.

func (VanityCode) MarshalJSON ¶
added in v0.210.0
func (s VanityCode) MarshalJSON() ([]byte, error)
type Variant ¶
added in v0.16.0
type Variant struct {
	// DeviceSpec: The device spec used to generate the APK.
	DeviceSpec *DeviceSpec `json:"deviceSpec,omitempty"`
	// Options: Optional. Options applied to the generated APK.
	Options *SystemApkOptions `json:"options,omitempty"`
	// VariantId: Output only. The ID of a previously created system APK variant.
	VariantId int64 `json:"variantId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeviceSpec") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceSpec") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Variant: APK that is suitable for inclusion in a system image. The resource of SystemApksService.

func (Variant) MarshalJSON ¶
added in v0.16.0
func (s Variant) MarshalJSON() ([]byte, error)
type VariantTargeting ¶
added in v0.130.0
type VariantTargeting struct {
	// AbiTargeting: The abi that the variant targets
	AbiTargeting *AbiTargeting `json:"abiTargeting,omitempty"`
	// MultiAbiTargeting: Multi-api-level targeting
	MultiAbiTargeting *MultiAbiTargeting `json:"multiAbiTargeting,omitempty"`
	// ScreenDensityTargeting: The screen densities that this variant supports
	ScreenDensityTargeting *ScreenDensityTargeting `json:"screenDensityTargeting,omitempty"`
	// SdkVersionTargeting: The sdk version that the variant targets
	SdkVersionTargeting *SdkVersionTargeting `json:"sdkVersionTargeting,omitempty"`
	// TextureCompressionFormatTargeting: Texture-compression-format-level
	// targeting
	TextureCompressionFormatTargeting *TextureCompressionFormatTargeting `json:"textureCompressionFormatTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AbiTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbiTargeting") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VariantTargeting: Targeting on the level of variants.

func (VariantTargeting) MarshalJSON ¶
added in v0.130.0
func (s VariantTargeting) MarshalJSON() ([]byte, error)
type VoidedPurchase ¶
type VoidedPurchase struct {
	// Kind: This kind represents a voided purchase object in the androidpublisher
	// service.
	Kind string `json:"kind,omitempty"`
	// OrderId: The order id which uniquely identifies a one-time purchase,
	// subscription purchase, or subscription renewal.
	OrderId string `json:"orderId,omitempty"`
	// PurchaseTimeMillis: The time at which the purchase was made, in milliseconds
	// since the epoch (Jan 1, 1970).
	PurchaseTimeMillis int64 `json:"purchaseTimeMillis,omitempty,string"`
	// PurchaseToken: The token which uniquely identifies a one-time purchase or
	// subscription. To uniquely identify subscription renewals use order_id
	// (available starting from version 3 of the API).
	PurchaseToken string `json:"purchaseToken,omitempty"`
	// VoidedQuantity: The voided quantity as the result of a quantity-based
	// partial refund. Voided purchases of quantity-based partial refunds may only
	// be returned when includeQuantityBasedPartialRefund is set to true.
	VoidedQuantity int64 `json:"voidedQuantity,omitempty"`
	// VoidedReason: The reason why the purchase was voided, possible values are:
	// 0. Other 1. Remorse 2. Not_received 3. Defective 4. Accidental_purchase 5.
	// Fraud 6. Friendly_fraud 7. Chargeback 8. Unacknowledged_purchase
	VoidedReason int64 `json:"voidedReason,omitempty"`
	// VoidedSource: The initiator of voided purchase, possible values are: 0. User
	// 1. Developer 2. Google
	VoidedSource int64 `json:"voidedSource,omitempty"`
	// VoidedTimeMillis: The time at which the purchase was
	// canceled/refunded/charged-back, in milliseconds since the epoch (Jan 1,
	// 1970).
	VoidedTimeMillis int64 `json:"voidedTimeMillis,omitempty,string"`
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

VoidedPurchase: A VoidedPurchase resource indicates a purchase that was either canceled/refunded/charged-back.

func (VoidedPurchase) MarshalJSON ¶
func (s VoidedPurchase) MarshalJSON() ([]byte, error)
type VoidedPurchasesListResponse ¶
type VoidedPurchasesListResponse struct {
	// PageInfo: General pagination information.
	PageInfo *PageInfo `json:"pageInfo,omitempty"`
	// TokenPagination: Pagination information for token pagination.
	TokenPagination *TokenPagination  `json:"tokenPagination,omitempty"`
	VoidedPurchases []*VoidedPurchase `json:"voidedPurchases,omitempty"`

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

VoidedPurchasesListResponse: Response for the voidedpurchases.list API.

func (VoidedPurchasesListResponse) MarshalJSON ¶
func (s VoidedPurchasesListResponse) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
androidpublisher-gen.go
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
