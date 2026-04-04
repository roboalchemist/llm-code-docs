# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.4

Title: adexchangebuyer package - google.golang.org/api/adexchangebuyer/v1.4 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.4

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
adexchangebuyer
 
v1.4
adexchangebuyer
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 15 
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
Creating a client
Other authentication options

Package adexchangebuyer provides access to the Ad Exchange Buyer API.

For product documentation, see: https://developers.google.com/ad-exchange/buyer-rest

Creating a client ¶

Usage example:

import "google.golang.org/api/adexchangebuyer/v1.4"
...
ctx := context.Background()
adexchangebuyerService, err := adexchangebuyer.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication.

For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use option.WithAPIKey:

adexchangebuyerService, err := adexchangebuyer.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow), use option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adexchangebuyerService, err := adexchangebuyer.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See https://godoc.org/google.golang.org/api/option/ for details on options.

Index ¶
Constants
type Account
func (s *Account) MarshalJSON() ([]byte, error)
type AccountBidderLocation
func (s *AccountBidderLocation) MarshalJSON() ([]byte, error)
type AccountsGetCall
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall
func (c *AccountsGetCall) Header() http.Header
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall
type AccountsList
func (s *AccountsList) MarshalJSON() ([]byte, error)
type AccountsListCall
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*AccountsList, error)
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall
func (c *AccountsListCall) Header() http.Header
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall
type AccountsPatchCall
func (c *AccountsPatchCall) ConfirmUnsafeAccountChange(confirmUnsafeAccountChange bool) *AccountsPatchCall
func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*Account, error)
func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall
func (c *AccountsPatchCall) Header() http.Header
type AccountsService
func NewAccountsService(s *Service) *AccountsService
func (r *AccountsService) Get(id int64) *AccountsGetCall
func (r *AccountsService) List() *AccountsListCall
func (r *AccountsService) Patch(id int64, account *Account) *AccountsPatchCall
func (r *AccountsService) Update(id int64, account *Account) *AccountsUpdateCall
type AccountsUpdateCall
func (c *AccountsUpdateCall) ConfirmUnsafeAccountChange(confirmUnsafeAccountChange bool) *AccountsUpdateCall
func (c *AccountsUpdateCall) Context(ctx context.Context) *AccountsUpdateCall
func (c *AccountsUpdateCall) Do(opts ...googleapi.CallOption) (*Account, error)
func (c *AccountsUpdateCall) Fields(s ...googleapi.Field) *AccountsUpdateCall
func (c *AccountsUpdateCall) Header() http.Header
type AddOrderDealsRequest
func (s *AddOrderDealsRequest) MarshalJSON() ([]byte, error)
type AddOrderDealsResponse
func (s *AddOrderDealsResponse) MarshalJSON() ([]byte, error)
type AddOrderNotesRequest
func (s *AddOrderNotesRequest) MarshalJSON() ([]byte, error)
type AddOrderNotesResponse
func (s *AddOrderNotesResponse) MarshalJSON() ([]byte, error)
type BillingInfo
func (s *BillingInfo) MarshalJSON() ([]byte, error)
type BillingInfoGetCall
func (c *BillingInfoGetCall) Context(ctx context.Context) *BillingInfoGetCall
func (c *BillingInfoGetCall) Do(opts ...googleapi.CallOption) (*BillingInfo, error)
func (c *BillingInfoGetCall) Fields(s ...googleapi.Field) *BillingInfoGetCall
func (c *BillingInfoGetCall) Header() http.Header
func (c *BillingInfoGetCall) IfNoneMatch(entityTag string) *BillingInfoGetCall
type BillingInfoList
func (s *BillingInfoList) MarshalJSON() ([]byte, error)
type BillingInfoListCall
func (c *BillingInfoListCall) Context(ctx context.Context) *BillingInfoListCall
func (c *BillingInfoListCall) Do(opts ...googleapi.CallOption) (*BillingInfoList, error)
func (c *BillingInfoListCall) Fields(s ...googleapi.Field) *BillingInfoListCall
func (c *BillingInfoListCall) Header() http.Header
func (c *BillingInfoListCall) IfNoneMatch(entityTag string) *BillingInfoListCall
type BillingInfoService
func NewBillingInfoService(s *Service) *BillingInfoService
func (r *BillingInfoService) Get(accountId int64) *BillingInfoGetCall
func (r *BillingInfoService) List() *BillingInfoListCall
type Budget
func (s *Budget) MarshalJSON() ([]byte, error)
type BudgetGetCall
func (c *BudgetGetCall) Context(ctx context.Context) *BudgetGetCall
func (c *BudgetGetCall) Do(opts ...googleapi.CallOption) (*Budget, error)
func (c *BudgetGetCall) Fields(s ...googleapi.Field) *BudgetGetCall
func (c *BudgetGetCall) Header() http.Header
func (c *BudgetGetCall) IfNoneMatch(entityTag string) *BudgetGetCall
type BudgetPatchCall
func (c *BudgetPatchCall) Context(ctx context.Context) *BudgetPatchCall
func (c *BudgetPatchCall) Do(opts ...googleapi.CallOption) (*Budget, error)
func (c *BudgetPatchCall) Fields(s ...googleapi.Field) *BudgetPatchCall
func (c *BudgetPatchCall) Header() http.Header
type BudgetService
func NewBudgetService(s *Service) *BudgetService
func (r *BudgetService) Get(accountId int64, billingId int64) *BudgetGetCall
func (r *BudgetService) Patch(accountId int64, billingId int64, budget *Budget) *BudgetPatchCall
func (r *BudgetService) Update(accountId int64, billingId int64, budget *Budget) *BudgetUpdateCall
type BudgetUpdateCall
func (c *BudgetUpdateCall) Context(ctx context.Context) *BudgetUpdateCall
func (c *BudgetUpdateCall) Do(opts ...googleapi.CallOption) (*Budget, error)
func (c *BudgetUpdateCall) Fields(s ...googleapi.Field) *BudgetUpdateCall
func (c *BudgetUpdateCall) Header() http.Header
type Buyer
func (s *Buyer) MarshalJSON() ([]byte, error)
type ContactInformation
func (s *ContactInformation) MarshalJSON() ([]byte, error)
type CreateOrdersRequest
func (s *CreateOrdersRequest) MarshalJSON() ([]byte, error)
type CreateOrdersResponse
func (s *CreateOrdersResponse) MarshalJSON() ([]byte, error)
type Creative
func (s *Creative) MarshalJSON() ([]byte, error)
type CreativeAdTechnologyProviders
func (s *CreativeAdTechnologyProviders) MarshalJSON() ([]byte, error)
type CreativeCorrections
func (s *CreativeCorrections) MarshalJSON() ([]byte, error)
type CreativeCorrectionsContexts
func (s *CreativeCorrectionsContexts) MarshalJSON() ([]byte, error)
type CreativeDealIds
func (s *CreativeDealIds) MarshalJSON() ([]byte, error)
type CreativeDealIdsDealStatuses
func (s *CreativeDealIdsDealStatuses) MarshalJSON() ([]byte, error)
type CreativeFilteringReasons
func (s *CreativeFilteringReasons) MarshalJSON() ([]byte, error)
type CreativeFilteringReasonsReasons
func (s *CreativeFilteringReasonsReasons) MarshalJSON() ([]byte, error)
type CreativeNativeAd
func (s *CreativeNativeAd) MarshalJSON() ([]byte, error)
func (s *CreativeNativeAd) UnmarshalJSON(data []byte) error
type CreativeNativeAdAppIcon
func (s *CreativeNativeAdAppIcon) MarshalJSON() ([]byte, error)
type CreativeNativeAdImage
func (s *CreativeNativeAdImage) MarshalJSON() ([]byte, error)
type CreativeNativeAdLogo
func (s *CreativeNativeAdLogo) MarshalJSON() ([]byte, error)
type CreativeServingRestrictions
func (s *CreativeServingRestrictions) MarshalJSON() ([]byte, error)
type CreativeServingRestrictionsContexts
func (s *CreativeServingRestrictionsContexts) MarshalJSON() ([]byte, error)
type CreativeServingRestrictionsDisapprovalReasons
func (s *CreativeServingRestrictionsDisapprovalReasons) MarshalJSON() ([]byte, error)
type CreativesAddDealCall
func (c *CreativesAddDealCall) Context(ctx context.Context) *CreativesAddDealCall
func (c *CreativesAddDealCall) Do(opts ...googleapi.CallOption) error
func (c *CreativesAddDealCall) Fields(s ...googleapi.Field) *CreativesAddDealCall
func (c *CreativesAddDealCall) Header() http.Header
type CreativesGetCall
func (c *CreativesGetCall) Context(ctx context.Context) *CreativesGetCall
func (c *CreativesGetCall) Do(opts ...googleapi.CallOption) (*Creative, error)
func (c *CreativesGetCall) Fields(s ...googleapi.Field) *CreativesGetCall
func (c *CreativesGetCall) Header() http.Header
func (c *CreativesGetCall) IfNoneMatch(entityTag string) *CreativesGetCall
type CreativesInsertCall
func (c *CreativesInsertCall) Context(ctx context.Context) *CreativesInsertCall
func (c *CreativesInsertCall) Do(opts ...googleapi.CallOption) (*Creative, error)
func (c *CreativesInsertCall) Fields(s ...googleapi.Field) *CreativesInsertCall
func (c *CreativesInsertCall) Header() http.Header
type CreativesList
func (s *CreativesList) MarshalJSON() ([]byte, error)
type CreativesListCall
func (c *CreativesListCall) AccountId(accountId ...int64) *CreativesListCall
func (c *CreativesListCall) BuyerCreativeId(buyerCreativeId ...string) *CreativesListCall
func (c *CreativesListCall) Context(ctx context.Context) *CreativesListCall
func (c *CreativesListCall) DealsStatusFilter(dealsStatusFilter string) *CreativesListCall
func (c *CreativesListCall) Do(opts ...googleapi.CallOption) (*CreativesList, error)
func (c *CreativesListCall) Fields(s ...googleapi.Field) *CreativesListCall
func (c *CreativesListCall) Header() http.Header
func (c *CreativesListCall) IfNoneMatch(entityTag string) *CreativesListCall
func (c *CreativesListCall) MaxResults(maxResults int64) *CreativesListCall
func (c *CreativesListCall) OpenAuctionStatusFilter(openAuctionStatusFilter string) *CreativesListCall
func (c *CreativesListCall) PageToken(pageToken string) *CreativesListCall
func (c *CreativesListCall) Pages(ctx context.Context, f func(*CreativesList) error) error
type CreativesListDealsCall
func (c *CreativesListDealsCall) Context(ctx context.Context) *CreativesListDealsCall
func (c *CreativesListDealsCall) Do(opts ...googleapi.CallOption) (*CreativeDealIds, error)
func (c *CreativesListDealsCall) Fields(s ...googleapi.Field) *CreativesListDealsCall
func (c *CreativesListDealsCall) Header() http.Header
func (c *CreativesListDealsCall) IfNoneMatch(entityTag string) *CreativesListDealsCall
type CreativesRemoveDealCall
func (c *CreativesRemoveDealCall) Context(ctx context.Context) *CreativesRemoveDealCall
func (c *CreativesRemoveDealCall) Do(opts ...googleapi.CallOption) error
func (c *CreativesRemoveDealCall) Fields(s ...googleapi.Field) *CreativesRemoveDealCall
func (c *CreativesRemoveDealCall) Header() http.Header
type CreativesService
func NewCreativesService(s *Service) *CreativesService
func (r *CreativesService) AddDeal(accountId int64, buyerCreativeId string, dealId int64) *CreativesAddDealCall
func (r *CreativesService) Get(accountId int64, buyerCreativeId string) *CreativesGetCall
func (r *CreativesService) Insert(creative *Creative) *CreativesInsertCall
func (r *CreativesService) List() *CreativesListCall
func (r *CreativesService) ListDeals(accountId int64, buyerCreativeId string) *CreativesListDealsCall
func (r *CreativesService) RemoveDeal(accountId int64, buyerCreativeId string, dealId int64) *CreativesRemoveDealCall
type DealServingMetadata
func (s *DealServingMetadata) MarshalJSON() ([]byte, error)
type DealServingMetadataDealPauseStatus
func (s *DealServingMetadataDealPauseStatus) MarshalJSON() ([]byte, error)
type DealTerms
func (s *DealTerms) MarshalJSON() ([]byte, error)
type DealTermsGuaranteedFixedPriceTerms
func (s *DealTermsGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type DealTermsGuaranteedFixedPriceTermsBillingInfo
func (s *DealTermsGuaranteedFixedPriceTermsBillingInfo) MarshalJSON() ([]byte, error)
type DealTermsNonGuaranteedAuctionTerms
func (s *DealTermsNonGuaranteedAuctionTerms) MarshalJSON() ([]byte, error)
type DealTermsNonGuaranteedFixedPriceTerms
func (s *DealTermsNonGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type DealTermsRubiconNonGuaranteedTerms
func (s *DealTermsRubiconNonGuaranteedTerms) MarshalJSON() ([]byte, error)
type DeleteOrderDealsRequest
func (s *DeleteOrderDealsRequest) MarshalJSON() ([]byte, error)
type DeleteOrderDealsResponse
func (s *DeleteOrderDealsResponse) MarshalJSON() ([]byte, error)
type DeliveryControl
func (s *DeliveryControl) MarshalJSON() ([]byte, error)
type DeliveryControlFrequencyCap
func (s *DeliveryControlFrequencyCap) MarshalJSON() ([]byte, error)
type Dimension
func (s *Dimension) MarshalJSON() ([]byte, error)
type DimensionDimensionValue
func (s *DimensionDimensionValue) MarshalJSON() ([]byte, error)
type EditAllOrderDealsRequest
func (s *EditAllOrderDealsRequest) MarshalJSON() ([]byte, error)
type EditAllOrderDealsResponse
func (s *EditAllOrderDealsResponse) MarshalJSON() ([]byte, error)
type GetOffersResponse
func (s *GetOffersResponse) MarshalJSON() ([]byte, error)
type GetOrderDealsResponse
func (s *GetOrderDealsResponse) MarshalJSON() ([]byte, error)
type GetOrderNotesResponse
func (s *GetOrderNotesResponse) MarshalJSON() ([]byte, error)
type GetOrdersResponse
func (s *GetOrdersResponse) MarshalJSON() ([]byte, error)
type GetPublisherProfilesByAccountIdResponse
func (s *GetPublisherProfilesByAccountIdResponse) MarshalJSON() ([]byte, error)
type MarketplaceDeal
func (s *MarketplaceDeal) MarshalJSON() ([]byte, error)
type MarketplaceDealParty
func (s *MarketplaceDealParty) MarshalJSON() ([]byte, error)
type MarketplaceLabel
func (s *MarketplaceLabel) MarshalJSON() ([]byte, error)
type MarketplaceNote
func (s *MarketplaceNote) MarshalJSON() ([]byte, error)
type MarketplacedealsDeleteCall
func (c *MarketplacedealsDeleteCall) Context(ctx context.Context) *MarketplacedealsDeleteCall
func (c *MarketplacedealsDeleteCall) Do(opts ...googleapi.CallOption) (*DeleteOrderDealsResponse, error)
func (c *MarketplacedealsDeleteCall) Fields(s ...googleapi.Field) *MarketplacedealsDeleteCall
func (c *MarketplacedealsDeleteCall) Header() http.Header
type MarketplacedealsInsertCall
func (c *MarketplacedealsInsertCall) Context(ctx context.Context) *MarketplacedealsInsertCall
func (c *MarketplacedealsInsertCall) Do(opts ...googleapi.CallOption) (*AddOrderDealsResponse, error)
func (c *MarketplacedealsInsertCall) Fields(s ...googleapi.Field) *MarketplacedealsInsertCall
func (c *MarketplacedealsInsertCall) Header() http.Header
type MarketplacedealsListCall
func (c *MarketplacedealsListCall) Context(ctx context.Context) *MarketplacedealsListCall
func (c *MarketplacedealsListCall) Do(opts ...googleapi.CallOption) (*GetOrderDealsResponse, error)
func (c *MarketplacedealsListCall) Fields(s ...googleapi.Field) *MarketplacedealsListCall
func (c *MarketplacedealsListCall) Header() http.Header
func (c *MarketplacedealsListCall) IfNoneMatch(entityTag string) *MarketplacedealsListCall
func (c *MarketplacedealsListCall) PqlQuery(pqlQuery string) *MarketplacedealsListCall
type MarketplacedealsService
func NewMarketplacedealsService(s *Service) *MarketplacedealsService
func (r *MarketplacedealsService) Delete(proposalId string, deleteorderdealsrequest *DeleteOrderDealsRequest) *MarketplacedealsDeleteCall
func (r *MarketplacedealsService) Insert(proposalId string, addorderdealsrequest *AddOrderDealsRequest) *MarketplacedealsInsertCall
func (r *MarketplacedealsService) List(proposalId string) *MarketplacedealsListCall
func (r *MarketplacedealsService) Update(proposalId string, editallorderdealsrequest *EditAllOrderDealsRequest) *MarketplacedealsUpdateCall
type MarketplacedealsUpdateCall
func (c *MarketplacedealsUpdateCall) Context(ctx context.Context) *MarketplacedealsUpdateCall
func (c *MarketplacedealsUpdateCall) Do(opts ...googleapi.CallOption) (*EditAllOrderDealsResponse, error)
func (c *MarketplacedealsUpdateCall) Fields(s ...googleapi.Field) *MarketplacedealsUpdateCall
func (c *MarketplacedealsUpdateCall) Header() http.Header
type MarketplacenotesInsertCall
func (c *MarketplacenotesInsertCall) Context(ctx context.Context) *MarketplacenotesInsertCall
func (c *MarketplacenotesInsertCall) Do(opts ...googleapi.CallOption) (*AddOrderNotesResponse, error)
func (c *MarketplacenotesInsertCall) Fields(s ...googleapi.Field) *MarketplacenotesInsertCall
func (c *MarketplacenotesInsertCall) Header() http.Header
type MarketplacenotesListCall
func (c *MarketplacenotesListCall) Context(ctx context.Context) *MarketplacenotesListCall
func (c *MarketplacenotesListCall) Do(opts ...googleapi.CallOption) (*GetOrderNotesResponse, error)
func (c *MarketplacenotesListCall) Fields(s ...googleapi.Field) *MarketplacenotesListCall
func (c *MarketplacenotesListCall) Header() http.Header
func (c *MarketplacenotesListCall) IfNoneMatch(entityTag string) *MarketplacenotesListCall
func (c *MarketplacenotesListCall) PqlQuery(pqlQuery string) *MarketplacenotesListCall
type MarketplacenotesService
func NewMarketplacenotesService(s *Service) *MarketplacenotesService
func (r *MarketplacenotesService) Insert(proposalId string, addordernotesrequest *AddOrderNotesRequest) *MarketplacenotesInsertCall
func (r *MarketplacenotesService) List(proposalId string) *MarketplacenotesListCall
type MarketplaceprivateauctionService
func NewMarketplaceprivateauctionService(s *Service) *MarketplaceprivateauctionService
func (r *MarketplaceprivateauctionService) Updateproposal(privateAuctionId string, ...) *MarketplaceprivateauctionUpdateproposalCall
type MarketplaceprivateauctionUpdateproposalCall
func (c *MarketplaceprivateauctionUpdateproposalCall) Context(ctx context.Context) *MarketplaceprivateauctionUpdateproposalCall
func (c *MarketplaceprivateauctionUpdateproposalCall) Do(opts ...googleapi.CallOption) error
func (c *MarketplaceprivateauctionUpdateproposalCall) Fields(s ...googleapi.Field) *MarketplaceprivateauctionUpdateproposalCall
func (c *MarketplaceprivateauctionUpdateproposalCall) Header() http.Header
type MobileApplication
func (s *MobileApplication) MarshalJSON() ([]byte, error)
type PerformanceReport
func (s *PerformanceReport) MarshalJSON() ([]byte, error)
func (s *PerformanceReport) UnmarshalJSON(data []byte) error
type PerformanceReportList
func (s *PerformanceReportList) MarshalJSON() ([]byte, error)
type PerformanceReportListCall
func (c *PerformanceReportListCall) Context(ctx context.Context) *PerformanceReportListCall
func (c *PerformanceReportListCall) Do(opts ...googleapi.CallOption) (*PerformanceReportList, error)
func (c *PerformanceReportListCall) Fields(s ...googleapi.Field) *PerformanceReportListCall
func (c *PerformanceReportListCall) Header() http.Header
func (c *PerformanceReportListCall) IfNoneMatch(entityTag string) *PerformanceReportListCall
func (c *PerformanceReportListCall) MaxResults(maxResults int64) *PerformanceReportListCall
func (c *PerformanceReportListCall) PageToken(pageToken string) *PerformanceReportListCall
type PerformanceReportService
func NewPerformanceReportService(s *Service) *PerformanceReportService
func (r *PerformanceReportService) List(accountId int64, endDateTime string, startDateTime string) *PerformanceReportListCall
type PretargetingConfig
func (s *PretargetingConfig) MarshalJSON() ([]byte, error)
type PretargetingConfigDeleteCall
func (c *PretargetingConfigDeleteCall) Context(ctx context.Context) *PretargetingConfigDeleteCall
func (c *PretargetingConfigDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *PretargetingConfigDeleteCall) Fields(s ...googleapi.Field) *PretargetingConfigDeleteCall
func (c *PretargetingConfigDeleteCall) Header() http.Header
type PretargetingConfigDimensions
func (s *PretargetingConfigDimensions) MarshalJSON() ([]byte, error)
type PretargetingConfigExcludedPlacements
func (s *PretargetingConfigExcludedPlacements) MarshalJSON() ([]byte, error)
type PretargetingConfigGetCall
func (c *PretargetingConfigGetCall) Context(ctx context.Context) *PretargetingConfigGetCall
func (c *PretargetingConfigGetCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)
func (c *PretargetingConfigGetCall) Fields(s ...googleapi.Field) *PretargetingConfigGetCall
func (c *PretargetingConfigGetCall) Header() http.Header
func (c *PretargetingConfigGetCall) IfNoneMatch(entityTag string) *PretargetingConfigGetCall
type PretargetingConfigInsertCall
func (c *PretargetingConfigInsertCall) Context(ctx context.Context) *PretargetingConfigInsertCall
func (c *PretargetingConfigInsertCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)
func (c *PretargetingConfigInsertCall) Fields(s ...googleapi.Field) *PretargetingConfigInsertCall
func (c *PretargetingConfigInsertCall) Header() http.Header
type PretargetingConfigList
func (s *PretargetingConfigList) MarshalJSON() ([]byte, error)
type PretargetingConfigListCall
func (c *PretargetingConfigListCall) Context(ctx context.Context) *PretargetingConfigListCall
func (c *PretargetingConfigListCall) Do(opts ...googleapi.CallOption) (*PretargetingConfigList, error)
func (c *PretargetingConfigListCall) Fields(s ...googleapi.Field) *PretargetingConfigListCall
func (c *PretargetingConfigListCall) Header() http.Header
func (c *PretargetingConfigListCall) IfNoneMatch(entityTag string) *PretargetingConfigListCall
type PretargetingConfigPatchCall
func (c *PretargetingConfigPatchCall) Context(ctx context.Context) *PretargetingConfigPatchCall
func (c *PretargetingConfigPatchCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)
func (c *PretargetingConfigPatchCall) Fields(s ...googleapi.Field) *PretargetingConfigPatchCall
func (c *PretargetingConfigPatchCall) Header() http.Header
type PretargetingConfigPlacements
func (s *PretargetingConfigPlacements) MarshalJSON() ([]byte, error)
type PretargetingConfigService
func NewPretargetingConfigService(s *Service) *PretargetingConfigService
func (r *PretargetingConfigService) Delete(accountId int64, configId int64) *PretargetingConfigDeleteCall
func (r *PretargetingConfigService) Get(accountId int64, configId int64) *PretargetingConfigGetCall
func (r *PretargetingConfigService) Insert(accountId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigInsertCall
func (r *PretargetingConfigService) List(accountId int64) *PretargetingConfigListCall
func (r *PretargetingConfigService) Patch(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigPatchCall
func (r *PretargetingConfigService) Update(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigUpdateCall
type PretargetingConfigUpdateCall
func (c *PretargetingConfigUpdateCall) Context(ctx context.Context) *PretargetingConfigUpdateCall
func (c *PretargetingConfigUpdateCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)
func (c *PretargetingConfigUpdateCall) Fields(s ...googleapi.Field) *PretargetingConfigUpdateCall
func (c *PretargetingConfigUpdateCall) Header() http.Header
type PretargetingConfigVideoPlayerSizes
func (s *PretargetingConfigVideoPlayerSizes) MarshalJSON() ([]byte, error)
type Price
func (s *Price) MarshalJSON() ([]byte, error)
func (s *Price) UnmarshalJSON(data []byte) error
type PricePerBuyer
func (s *PricePerBuyer) MarshalJSON() ([]byte, error)
type PrivateData
func (s *PrivateData) MarshalJSON() ([]byte, error)
type Product
func (s *Product) MarshalJSON() ([]byte, error)
type ProductsGetCall
func (c *ProductsGetCall) Context(ctx context.Context) *ProductsGetCall
func (c *ProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)
func (c *ProductsGetCall) Fields(s ...googleapi.Field) *ProductsGetCall
func (c *ProductsGetCall) Header() http.Header
func (c *ProductsGetCall) IfNoneMatch(entityTag string) *ProductsGetCall
type ProductsSearchCall
func (c *ProductsSearchCall) Context(ctx context.Context) *ProductsSearchCall
func (c *ProductsSearchCall) Do(opts ...googleapi.CallOption) (*GetOffersResponse, error)
func (c *ProductsSearchCall) Fields(s ...googleapi.Field) *ProductsSearchCall
func (c *ProductsSearchCall) Header() http.Header
func (c *ProductsSearchCall) IfNoneMatch(entityTag string) *ProductsSearchCall
func (c *ProductsSearchCall) PqlQuery(pqlQuery string) *ProductsSearchCall
type ProductsService
func NewProductsService(s *Service) *ProductsService
func (r *ProductsService) Get(productId string) *ProductsGetCall
func (r *ProductsService) Search() *ProductsSearchCall
type Proposal
func (s *Proposal) MarshalJSON() ([]byte, error)
type ProposalsGetCall
func (c *ProposalsGetCall) Context(ctx context.Context) *ProposalsGetCall
func (c *ProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *ProposalsGetCall) Fields(s ...googleapi.Field) *ProposalsGetCall
func (c *ProposalsGetCall) Header() http.Header
func (c *ProposalsGetCall) IfNoneMatch(entityTag string) *ProposalsGetCall
type ProposalsInsertCall
func (c *ProposalsInsertCall) Context(ctx context.Context) *ProposalsInsertCall
func (c *ProposalsInsertCall) Do(opts ...googleapi.CallOption) (*CreateOrdersResponse, error)
func (c *ProposalsInsertCall) Fields(s ...googleapi.Field) *ProposalsInsertCall
func (c *ProposalsInsertCall) Header() http.Header
type ProposalsPatchCall
func (c *ProposalsPatchCall) Context(ctx context.Context) *ProposalsPatchCall
func (c *ProposalsPatchCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *ProposalsPatchCall) Fields(s ...googleapi.Field) *ProposalsPatchCall
func (c *ProposalsPatchCall) Header() http.Header
type ProposalsSearchCall
func (c *ProposalsSearchCall) Context(ctx context.Context) *ProposalsSearchCall
func (c *ProposalsSearchCall) Do(opts ...googleapi.CallOption) (*GetOrdersResponse, error)
func (c *ProposalsSearchCall) Fields(s ...googleapi.Field) *ProposalsSearchCall
func (c *ProposalsSearchCall) Header() http.Header
func (c *ProposalsSearchCall) IfNoneMatch(entityTag string) *ProposalsSearchCall
func (c *ProposalsSearchCall) PqlQuery(pqlQuery string) *ProposalsSearchCall
type ProposalsService
func NewProposalsService(s *Service) *ProposalsService
func (r *ProposalsService) Get(proposalId string) *ProposalsGetCall
func (r *ProposalsService) Insert(createordersrequest *CreateOrdersRequest) *ProposalsInsertCall
func (r *ProposalsService) Patch(proposalId string, revisionNumber int64, updateAction string, ...) *ProposalsPatchCall
func (r *ProposalsService) Search() *ProposalsSearchCall
func (r *ProposalsService) Setupcomplete(proposalId string) *ProposalsSetupcompleteCall
func (r *ProposalsService) Update(proposalId string, revisionNumber int64, updateAction string, ...) *ProposalsUpdateCall
type ProposalsSetupcompleteCall
func (c *ProposalsSetupcompleteCall) Context(ctx context.Context) *ProposalsSetupcompleteCall
func (c *ProposalsSetupcompleteCall) Do(opts ...googleapi.CallOption) error
func (c *ProposalsSetupcompleteCall) Fields(s ...googleapi.Field) *ProposalsSetupcompleteCall
func (c *ProposalsSetupcompleteCall) Header() http.Header
type ProposalsUpdateCall
func (c *ProposalsUpdateCall) Context(ctx context.Context) *ProposalsUpdateCall
func (c *ProposalsUpdateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *ProposalsUpdateCall) Fields(s ...googleapi.Field) *ProposalsUpdateCall
func (c *ProposalsUpdateCall) Header() http.Header
type PublisherProfileApiProto
func (s *PublisherProfileApiProto) MarshalJSON() ([]byte, error)
type PublisherProvidedForecast
func (s *PublisherProvidedForecast) MarshalJSON() ([]byte, error)
type PubprofilesListCall
func (c *PubprofilesListCall) Context(ctx context.Context) *PubprofilesListCall
func (c *PubprofilesListCall) Do(opts ...googleapi.CallOption) (*GetPublisherProfilesByAccountIdResponse, error)
func (c *PubprofilesListCall) Fields(s ...googleapi.Field) *PubprofilesListCall
func (c *PubprofilesListCall) Header() http.Header
func (c *PubprofilesListCall) IfNoneMatch(entityTag string) *PubprofilesListCall
type PubprofilesService
func NewPubprofilesService(s *Service) *PubprofilesService
func (r *PubprofilesService) List(accountId int64) *PubprofilesListCall
type Seller
func (s *Seller) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SharedTargeting
func (s *SharedTargeting) MarshalJSON() ([]byte, error)
type TargetingValue
func (s *TargetingValue) MarshalJSON() ([]byte, error)
type TargetingValueCreativeSize
func (s *TargetingValueCreativeSize) MarshalJSON() ([]byte, error)
type TargetingValueDayPartTargeting
func (s *TargetingValueDayPartTargeting) MarshalJSON() ([]byte, error)
type TargetingValueDayPartTargetingDayPart
func (s *TargetingValueDayPartTargetingDayPart) MarshalJSON() ([]byte, error)
type TargetingValueDemogAgeCriteria
func (s *TargetingValueDemogAgeCriteria) MarshalJSON() ([]byte, error)
type TargetingValueDemogGenderCriteria
func (s *TargetingValueDemogGenderCriteria) MarshalJSON() ([]byte, error)
type TargetingValueRequestPlatformTargeting
func (s *TargetingValueRequestPlatformTargeting) MarshalJSON() ([]byte, error)
type TargetingValueSize
func (s *TargetingValueSize) MarshalJSON() ([]byte, error)
type UpdatePrivateAuctionProposalRequest
func (s *UpdatePrivateAuctionProposalRequest) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// Manage your Ad Exchange buyer account configuration
	AdexchangeBuyerScope = "https://www.googleapis.com/auth/adexchange.buyer"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Account ¶
type Account struct {
	// ApplyPretargetingToNonGuaranteedDeals: When this is false, bid
	// requests that include a deal ID for a private auction or preferred
	// deal are always sent to your bidder. When true, all active
	// pretargeting configs will be applied to private auctions and
	// preferred deals. Programmatic Guaranteed deals (when enabled) are
	// always sent to your bidder.
	ApplyPretargetingToNonGuaranteedDeals bool `json:"applyPretargetingToNonGuaranteedDeals,omitempty"`

	// BidderLocation: Your bidder locations that have distinct URLs.
	BidderLocation []*AccountBidderLocation `json:"bidderLocation,omitempty"`

	// CookieMatchingNid: The nid parameter value used in cookie match
	// requests. Please contact your technical account manager if you need
	// to change this.
	CookieMatchingNid string `json:"cookieMatchingNid,omitempty"`

	// CookieMatchingUrl: The base URL used in cookie match requests.
	CookieMatchingUrl string `json:"cookieMatchingUrl,omitempty"`

	// Id: Account id.
	Id int64 `json:"id,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// MaximumActiveCreatives: The maximum number of active creatives that
	// an account can have, where a creative is active if it was inserted or
	// bid with in the last 30 days. Please contact your technical account
	// manager if you need to change this.
	MaximumActiveCreatives int64 `json:"maximumActiveCreatives,omitempty"`

	// MaximumTotalQps: The sum of all bidderLocation.maximumQps values
	// cannot exceed this. Please contact your technical account manager if
	// you need to change this.
	MaximumTotalQps int64 `json:"maximumTotalQps,omitempty"`

	// NumberActiveCreatives: The number of creatives that this account
	// inserted or bid with in the last 30 days.
	NumberActiveCreatives int64 `json:"numberActiveCreatives,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g.
	// "ApplyPretargetingToNonGuaranteedDeals") to unconditionally include
	// in API requests. By default, fields with empty or default values are
	// omitted from API requests. However, any non-pointer, non-interface
	// field appearing in ForceSendFields will be sent to the server
	// regardless of whether the field is empty or not. This may be used to
	// include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g.
	// "ApplyPretargetingToNonGuaranteedDeals") to include in API requests
	// with the JSON null value. By default, fields with empty values are
	// omitted from API requests. However, any field with an empty value
	// appearing in NullFields will be sent to the server as null. It is an
	// error if a field in this list has a non-empty value. This may be used
	// to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Account: Configuration data for an Ad Exchange buyer account.

func (*Account) MarshalJSON ¶
func (s *Account) MarshalJSON() ([]byte, error)
type AccountBidderLocation ¶
type AccountBidderLocation struct {
	// BidProtocol: The protocol that the bidder endpoint is using. OpenRTB
	// protocols with prefix PROTOCOL_OPENRTB_PROTOBUF use proto buffer,
	// otherwise use JSON.  Allowed values:
	// - PROTOCOL_ADX
	// - PROTOCOL_OPENRTB_2_2
	// - PROTOCOL_OPENRTB_2_3
	// - PROTOCOL_OPENRTB_2_4
	// - PROTOCOL_OPENRTB_2_5
	// - PROTOCOL_OPENRTB_PROTOBUF_2_3
	// - PROTOCOL_OPENRTB_PROTOBUF_2_4
	// - PROTOCOL_OPENRTB_PROTOBUF_2_5
	BidProtocol string `json:"bidProtocol,omitempty"`

	// MaximumQps: The maximum queries per second the Ad Exchange will send.
	MaximumQps int64 `json:"maximumQps,omitempty"`

	// Region: The geographical region the Ad Exchange should send requests
	// from. Only used by some quota systems, but always setting the value
	// is recommended. Allowed values:
	// - ASIA
	// - EUROPE
	// - US_EAST
	// - US_WEST
	Region string `json:"region,omitempty"`

	// Url: The URL to which the Ad Exchange will send bid requests.
	Url string `json:"url,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BidProtocol") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BidProtocol") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AccountBidderLocation) MarshalJSON ¶
func (s *AccountBidderLocation) MarshalJSON() ([]byte, error)
type AccountsGetCall ¶
type AccountsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsGetCall) Context ¶
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsGetCall) Do ¶
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)

Do executes the "adexchangebuyer.accounts.get" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsGetCall) Fields ¶
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsGetCall) Header ¶
func (c *AccountsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsGetCall) IfNoneMatch ¶
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsList ¶
type AccountsList struct {
	// Items: A list of accounts.
	Items []*Account `json:"items,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AccountsList: An account feed lists Ad Exchange buyer accounts that the user has access to. Each entry in the feed corresponds to a single buyer account.

func (*AccountsList) MarshalJSON ¶
func (s *AccountsList) MarshalJSON() ([]byte, error)
type AccountsListCall ¶
type AccountsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsListCall) Context ¶
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsListCall) Do ¶
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*AccountsList, error)

Do executes the "adexchangebuyer.accounts.list" call. Exactly one of *AccountsList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AccountsList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsListCall) Fields ¶
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsListCall) Header ¶
func (c *AccountsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsListCall) IfNoneMatch ¶
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsPatchCall ¶
type AccountsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccountsPatchCall) ConfirmUnsafeAccountChange ¶
func (c *AccountsPatchCall) ConfirmUnsafeAccountChange(confirmUnsafeAccountChange bool) *AccountsPatchCall

ConfirmUnsafeAccountChange sets the optional parameter "confirmUnsafeAccountChange": Confirmation for erasing bidder and cookie matching urls.

func (*AccountsPatchCall) Context ¶
func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsPatchCall) Do ¶
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*Account, error)

Do executes the "adexchangebuyer.accounts.patch" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsPatchCall) Fields ¶
func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsPatchCall) Header ¶
func (c *AccountsPatchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type AccountsService ¶
type AccountsService struct {
	// contains filtered or unexported fields
}
func NewAccountsService ¶
func NewAccountsService(s *Service) *AccountsService
func (*AccountsService) Get ¶
func (r *AccountsService) Get(id int64) *AccountsGetCall

Get: Gets one account by ID.

- id: The account id.

func (*AccountsService) List ¶
func (r *AccountsService) List() *AccountsListCall

List: Retrieves the authenticated user's list of accounts.

func (*AccountsService) Patch ¶
func (r *AccountsService) Patch(id int64, account *Account) *AccountsPatchCall

Patch: Updates an existing account. This method supports patch semantics.

- id: The account id.

func (*AccountsService) Update ¶
func (r *AccountsService) Update(id int64, account *Account) *AccountsUpdateCall

Update: Updates an existing account.

- id: The account id.

type AccountsUpdateCall ¶
type AccountsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsUpdateCall) ConfirmUnsafeAccountChange ¶
func (c *AccountsUpdateCall) ConfirmUnsafeAccountChange(confirmUnsafeAccountChange bool) *AccountsUpdateCall

ConfirmUnsafeAccountChange sets the optional parameter "confirmUnsafeAccountChange": Confirmation for erasing bidder and cookie matching urls.

func (*AccountsUpdateCall) Context ¶
func (c *AccountsUpdateCall) Context(ctx context.Context) *AccountsUpdateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsUpdateCall) Do ¶
func (c *AccountsUpdateCall) Do(opts ...googleapi.CallOption) (*Account, error)

Do executes the "adexchangebuyer.accounts.update" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsUpdateCall) Fields ¶
func (c *AccountsUpdateCall) Fields(s ...googleapi.Field) *AccountsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsUpdateCall) Header ¶
func (c *AccountsUpdateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type AddOrderDealsRequest ¶
type AddOrderDealsRequest struct {
	// Deals: The list of deals to add
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// ProposalRevisionNumber: The last known proposal revision number.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// UpdateAction: Indicates an optional action to take on the proposal
	UpdateAction string `json:"updateAction,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AddOrderDealsRequest) MarshalJSON ¶
func (s *AddOrderDealsRequest) MarshalJSON() ([]byte, error)
type AddOrderDealsResponse ¶
type AddOrderDealsResponse struct {
	// Deals: List of deals added (in the same proposal as passed in the
	// request)
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// ProposalRevisionNumber: The updated revision number for the proposal.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AddOrderDealsResponse) MarshalJSON ¶
func (s *AddOrderDealsResponse) MarshalJSON() ([]byte, error)
type AddOrderNotesRequest ¶
type AddOrderNotesRequest struct {
	// Notes: The list of notes to add.
	Notes []*MarketplaceNote `json:"notes,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Notes") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Notes") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AddOrderNotesRequest) MarshalJSON ¶
func (s *AddOrderNotesRequest) MarshalJSON() ([]byte, error)
type AddOrderNotesResponse ¶
type AddOrderNotesResponse struct {
	Notes []*MarketplaceNote `json:"notes,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Notes") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Notes") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AddOrderNotesResponse) MarshalJSON ¶
func (s *AddOrderNotesResponse) MarshalJSON() ([]byte, error)
type BillingInfo ¶
type BillingInfo struct {
	// AccountId: Account id.
	AccountId int64 `json:"accountId,omitempty"`

	// AccountName: Account name.
	AccountName string `json:"accountName,omitempty"`

	// BillingId: A list of adgroup IDs associated with this particular
	// account. These IDs may show up as part of a realtime bidding
	// BidRequest, which indicates a bid request for this account.
	BillingId []string `json:"billingId,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AccountId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

BillingInfo: The configuration data for an Ad Exchange billing info.

func (*BillingInfo) MarshalJSON ¶
func (s *BillingInfo) MarshalJSON() ([]byte, error)
type BillingInfoGetCall ¶
type BillingInfoGetCall struct {
	// contains filtered or unexported fields
}
func (*BillingInfoGetCall) Context ¶
func (c *BillingInfoGetCall) Context(ctx context.Context) *BillingInfoGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*BillingInfoGetCall) Do ¶
func (c *BillingInfoGetCall) Do(opts ...googleapi.CallOption) (*BillingInfo, error)

Do executes the "adexchangebuyer.billingInfo.get" call. Exactly one of *BillingInfo or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *BillingInfo.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BillingInfoGetCall) Fields ¶
func (c *BillingInfoGetCall) Fields(s ...googleapi.Field) *BillingInfoGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*BillingInfoGetCall) Header ¶
func (c *BillingInfoGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*BillingInfoGetCall) IfNoneMatch ¶
func (c *BillingInfoGetCall) IfNoneMatch(entityTag string) *BillingInfoGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type BillingInfoList ¶
type BillingInfoList struct {
	// Items: A list of billing info relevant for your account.
	Items []*BillingInfo `json:"items,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

BillingInfoList: A billing info feed lists Billing Info the Ad Exchange buyer account has access to. Each entry in the feed corresponds to a single billing info.

func (*BillingInfoList) MarshalJSON ¶
func (s *BillingInfoList) MarshalJSON() ([]byte, error)
type BillingInfoListCall ¶
type BillingInfoListCall struct {
	// contains filtered or unexported fields
}
func (*BillingInfoListCall) Context ¶
func (c *BillingInfoListCall) Context(ctx context.Context) *BillingInfoListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*BillingInfoListCall) Do ¶
func (c *BillingInfoListCall) Do(opts ...googleapi.CallOption) (*BillingInfoList, error)

Do executes the "adexchangebuyer.billingInfo.list" call. Exactly one of *BillingInfoList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *BillingInfoList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BillingInfoListCall) Fields ¶
func (c *BillingInfoListCall) Fields(s ...googleapi.Field) *BillingInfoListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*BillingInfoListCall) Header ¶
func (c *BillingInfoListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*BillingInfoListCall) IfNoneMatch ¶
func (c *BillingInfoListCall) IfNoneMatch(entityTag string) *BillingInfoListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type BillingInfoService ¶
type BillingInfoService struct {
	// contains filtered or unexported fields
}
func NewBillingInfoService ¶
func NewBillingInfoService(s *Service) *BillingInfoService
func (*BillingInfoService) Get ¶
func (r *BillingInfoService) Get(accountId int64) *BillingInfoGetCall

Get: Returns the billing information for one account specified by account ID.

- accountId: The account id.

func (*BillingInfoService) List ¶
func (r *BillingInfoService) List() *BillingInfoListCall

List: Retrieves a list of billing information for all accounts of the authenticated user.

type Budget ¶
type Budget struct {
	// AccountId: The id of the account. This is required for get and update
	// requests.
	AccountId int64 `json:"accountId,omitempty,string"`

	// BillingId: The billing id to determine which adgroup to provide
	// budget information for. This is required for get and update requests.
	BillingId int64 `json:"billingId,omitempty,string"`

	// BudgetAmount: The daily budget amount in unit amount of the account
	// currency to apply for the billingId provided. This is required for
	// update requests.
	BudgetAmount int64 `json:"budgetAmount,omitempty,string"`

	// CurrencyCode: The currency code for the buyer. This cannot be altered
	// here.
	CurrencyCode string `json:"currencyCode,omitempty"`

	// Id: The unique id that describes this item.
	Id string `json:"id,omitempty"`

	// Kind: The kind of the resource, i.e. "adexchangebuyer#budget".
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AccountId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Budget: The configuration data for Ad Exchange RTB - Budget API.

func (*Budget) MarshalJSON ¶
func (s *Budget) MarshalJSON() ([]byte, error)
type BudgetGetCall ¶
type BudgetGetCall struct {
	// contains filtered or unexported fields
}
func (*BudgetGetCall) Context ¶
func (c *BudgetGetCall) Context(ctx context.Context) *BudgetGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*BudgetGetCall) Do ¶
func (c *BudgetGetCall) Do(opts ...googleapi.CallOption) (*Budget, error)

Do executes the "adexchangebuyer.budget.get" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BudgetGetCall) Fields ¶
func (c *BudgetGetCall) Fields(s ...googleapi.Field) *BudgetGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*BudgetGetCall) Header ¶
func (c *BudgetGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*BudgetGetCall) IfNoneMatch ¶
func (c *BudgetGetCall) IfNoneMatch(entityTag string) *BudgetGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type BudgetPatchCall ¶
type BudgetPatchCall struct {
	// contains filtered or unexported fields
}
func (*BudgetPatchCall) Context ¶
func (c *BudgetPatchCall) Context(ctx context.Context) *BudgetPatchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*BudgetPatchCall) Do ¶
func (c *BudgetPatchCall) Do(opts ...googleapi.CallOption) (*Budget, error)

Do executes the "adexchangebuyer.budget.patch" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BudgetPatchCall) Fields ¶
func (c *BudgetPatchCall) Fields(s ...googleapi.Field) *BudgetPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*BudgetPatchCall) Header ¶
func (c *BudgetPatchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type BudgetService ¶
type BudgetService struct {
	// contains filtered or unexported fields
}
func NewBudgetService ¶
func NewBudgetService(s *Service) *BudgetService
func (*BudgetService) Get ¶
func (r *BudgetService) Get(accountId int64, billingId int64) *BudgetGetCall

Get: Returns the budget information for the adgroup specified by the accountId and billingId.

- accountId: The account id to get the budget information for. - billingId: The billing id to get the budget information for.

func (*BudgetService) Patch ¶
func (r *BudgetService) Patch(accountId int64, billingId int64, budget *Budget) *BudgetPatchCall

Patch: Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request. This method supports patch semantics.

- accountId: The account id associated with the budget being updated. - billingId: The billing id associated with the budget being updated.

func (*BudgetService) Update ¶
func (r *BudgetService) Update(accountId int64, billingId int64, budget *Budget) *BudgetUpdateCall

Update: Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request.

- accountId: The account id associated with the budget being updated. - billingId: The billing id associated with the budget being updated.

type BudgetUpdateCall ¶
type BudgetUpdateCall struct {
	// contains filtered or unexported fields
}
func (*BudgetUpdateCall) Context ¶
func (c *BudgetUpdateCall) Context(ctx context.Context) *BudgetUpdateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*BudgetUpdateCall) Do ¶
func (c *BudgetUpdateCall) Do(opts ...googleapi.CallOption) (*Budget, error)

Do executes the "adexchangebuyer.budget.update" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BudgetUpdateCall) Fields ¶
func (c *BudgetUpdateCall) Fields(s ...googleapi.Field) *BudgetUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*BudgetUpdateCall) Header ¶
func (c *BudgetUpdateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type Buyer ¶
type Buyer struct {
	// AccountId: Adx account id of the buyer.
	AccountId string `json:"accountId,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AccountId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Buyer) MarshalJSON ¶
func (s *Buyer) MarshalJSON() ([]byte, error)
type ContactInformation ¶
type ContactInformation struct {
	// Email: Email address of the contact.
	Email string `json:"email,omitempty"`

	// Name: The name of the contact.
	Name string `json:"name,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Email") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Email") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*ContactInformation) MarshalJSON ¶
func (s *ContactInformation) MarshalJSON() ([]byte, error)
type CreateOrdersRequest ¶
type CreateOrdersRequest struct {
	// Proposals: The list of proposals to create.
	Proposals []*Proposal `json:"proposals,omitempty"`

	// WebPropertyCode: Web property id of the seller creating these orders
	WebPropertyCode string `json:"webPropertyCode,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Proposals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Proposals") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreateOrdersRequest) MarshalJSON ¶
func (s *CreateOrdersRequest) MarshalJSON() ([]byte, error)
type CreateOrdersResponse ¶
type CreateOrdersResponse struct {
	// Proposals: The list of proposals successfully created.
	Proposals []*Proposal `json:"proposals,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Proposals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Proposals") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreateOrdersResponse) MarshalJSON ¶
func (s *CreateOrdersResponse) MarshalJSON() ([]byte, error)
type Creative ¶
type Creative struct {
	// HTMLSnippet: The HTML snippet that displays the ad when inserted in
	// the web page. If set, videoURL, videoVastXML, and nativeAd should not
	// be set.
	HTMLSnippet string `json:"HTMLSnippet,omitempty"`

	// AccountId: Account id.
	AccountId int64 `json:"accountId,omitempty"`

	// AdChoicesDestinationUrl: The link to the Ad Preferences page. This is
	// only supported for native ads.
	AdChoicesDestinationUrl string `json:"adChoicesDestinationUrl,omitempty"`

	AdTechnologyProviders *CreativeAdTechnologyProviders `json:"adTechnologyProviders,omitempty"`

	// AdvertiserId: Detected advertiser id, if any. Read-only. This field
	// should not be set in requests.
	AdvertiserId googleapi.Int64s `json:"advertiserId,omitempty"`

	// AdvertiserName: The name of the company being advertised in the
	// creative. A list of advertisers is provided in the advertisers.txt
	// file.
	AdvertiserName string `json:"advertiserName,omitempty"`

	// AgencyId: The agency id for this creative.
	AgencyId int64 `json:"agencyId,omitempty,string"`

	// ApiUploadTimestamp: The last upload timestamp of this creative if it
	// was uploaded via API. Read-only. The value of this field is
	// generated, and will be ignored for uploads. (formatted RFC 3339
	// timestamp).
	ApiUploadTimestamp string `json:"apiUploadTimestamp,omitempty"`

	// Attribute: List of buyer selectable attributes for the ads that may
	// be shown from this snippet. Each attribute is represented by an
	// integer as defined in  buyer-declarable-creative-attributes.txt.
	Attribute []int64 `json:"attribute,omitempty"`

	// BuyerCreativeId: A buyer-specific id identifying the creative in this
	// ad.
	BuyerCreativeId string `json:"buyerCreativeId,omitempty"`

	// ClickThroughUrl: The set of destination urls for the snippet.
	ClickThroughUrl []string `json:"clickThroughUrl,omitempty"`

	// Corrections: Shows any corrections that were applied to this
	// creative. Read-only. This field should not be set in requests.
	Corrections []*CreativeCorrections `json:"corrections,omitempty"`

	// CreativeStatusIdentityType: Creative status identity type that the
	// creative item applies to. Ad Exchange real-time bidding is migrating
	// to the sizeless creative verification. Originally, Ad Exchange
	// assigned creative verification status to a unique combination of a
	// buyer creative ID and creative dimensions. Post-migration, a single
	// verification status will be assigned at the buyer creative ID level.
	// This field allows to distinguish whether a given creative status
	// applies to a unique combination of a buyer creative ID and creative
	// dimensions, or to a buyer creative ID as a whole.
	CreativeStatusIdentityType string `json:"creativeStatusIdentityType,omitempty"`

	// DealsStatus: Top-level deals status. Read-only. This field should not
	// be set in requests. If disapproved, an entry for
	// auctionType=DIRECT_DEALS (or ALL) in servingRestrictions will also
	// exist. Note that this may be nuanced with other contextual
	// restrictions, in which case it may be preferable to read from
	// servingRestrictions directly.
	DealsStatus string `json:"dealsStatus,omitempty"`

	// DetectedDomains: Detected domains for this creative. Read-only. This
	// field should not be set in requests.
	DetectedDomains []string `json:"detectedDomains,omitempty"`

	// FilteringReasons: The filtering reasons for the creative. Read-only.
	// This field should not be set in requests.
	FilteringReasons *CreativeFilteringReasons `json:"filteringReasons,omitempty"`

	// Height: Ad height.
	Height int64 `json:"height,omitempty"`

	// ImpressionTrackingUrl: The set of urls to be called to record an
	// impression.
	ImpressionTrackingUrl []string `json:"impressionTrackingUrl,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// Languages: Detected languages for this creative. Read-only. This
	// field should not be set in requests.
	Languages []string `json:"languages,omitempty"`

	// NativeAd: If nativeAd is set, HTMLSnippet, videoVastXML, and the
	// videoURL outside of nativeAd should not be set. (The videoURL inside
	// nativeAd can be set.)
	NativeAd *CreativeNativeAd `json:"nativeAd,omitempty"`

	// OpenAuctionStatus: Top-level open auction status. Read-only. This
	// field should not be set in requests. If disapproved, an entry for
	// auctionType=OPEN_AUCTION (or ALL) in servingRestrictions will also
	// exist. Note that this may be nuanced with other contextual
	// restrictions, in which case it may be preferable to read from
	// ServingRestrictions directly.
	OpenAuctionStatus string `json:"openAuctionStatus,omitempty"`

	// ProductCategories: Detected product categories, if any. Each category
	// is represented by an integer as defined in
	// ad-product-categories.txt. Read-only. This field should not be set in
	// requests.
	ProductCategories []int64 `json:"productCategories,omitempty"`

	// RestrictedCategories: All restricted categories for the ads that may
	// be shown from this snippet. Each category is represented by an
	// integer as defined in the  ad-restricted-categories.txt.
	RestrictedCategories []int64 `json:"restrictedCategories,omitempty"`

	// SensitiveCategories: Detected sensitive categories, if any. Each
	// category is represented by an integer as defined in
	// ad-sensitive-categories.txt. Read-only. This field should not be set
	// in requests.
	SensitiveCategories []int64 `json:"sensitiveCategories,omitempty"`

	// ServingRestrictions: The granular status of this ad in specific
	// contexts. A context here relates to where something ultimately serves
	// (for example, a physical location, a platform, an HTTPS vs HTTP
	// request, or the type of auction). Read-only. This field should not be
	// set in requests. See the examples in the Creatives guide for more
	// details.
	ServingRestrictions []*CreativeServingRestrictions `json:"servingRestrictions,omitempty"`

	// VendorType: List of vendor types for the ads that may be shown from
	// this snippet. Each vendor type is represented by an integer as
	// defined in vendors.txt.
	VendorType []int64 `json:"vendorType,omitempty"`

	// Version: The version for this creative. Read-only. This field should
	// not be set in requests.
	Version int64 `json:"version,omitempty"`

	// VideoURL: The URL to fetch a video ad. If set, HTMLSnippet,
	// videoVastXML, and nativeAd should not be set. Note, this is different
	// from resource.native_ad.video_url above.
	VideoURL string `json:"videoURL,omitempty"`

	// VideoVastXML: The contents of a VAST document for a video ad. This
	// document should conform to the VAST 2.0 or 3.0 standard. If set,
	// HTMLSnippet, videoURL, and nativeAd and should not be set.
	VideoVastXML string `json:"videoVastXML,omitempty"`

	// Width: Ad width.
	Width int64 `json:"width,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "HTMLSnippet") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "HTMLSnippet") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Creative: A creative and its classification data.

func (*Creative) MarshalJSON ¶
func (s *Creative) MarshalJSON() ([]byte, error)
type CreativeAdTechnologyProviders ¶
added in v0.7.0
type CreativeAdTechnologyProviders struct {
	// DetectedProviderIds: The detected ad technology provider IDs for this
	// creative. See
	// https://storage.googleapis.com/adx-rtb-dictionaries/providers.csv for
	// mapping of provider ID to provided name, a privacy policy URL, and a
	// list of domains which can be attributed to the provider. If this
	// creative contains provider IDs that are outside of those listed in
	// the
	// `BidRequest.adslot.consented_providers_settings.consented_providers`
	// field on the  Authorized Buyers Real-Time Bidding protocol or the
	// `BidRequest.user.ext.consented_providers_settings.consented_providers`
	//  field on the OpenRTB protocol, a bid submitted for a European
	// Economic Area (EEA) user with this creative is not compliant with the
	// GDPR policies as mentioned in the "Third-party Ad Technology Vendors"
	// section of Authorized Buyers Program Guidelines.
	DetectedProviderIds googleapi.Int64s `json:"detectedProviderIds,omitempty"`

	// HasUnidentifiedProvider: Whether the creative contains an
	// unidentified ad technology provider. If true, a bid submitted for a
	// European Economic Area (EEA) user with this creative is not compliant
	// with the GDPR policies as mentioned in the "Third-party Ad Technology
	// Vendors" section of Authorized Buyers Program Guidelines.
	HasUnidentifiedProvider bool `json:"hasUnidentifiedProvider,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DetectedProviderIds")
	// to unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DetectedProviderIds") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*CreativeAdTechnologyProviders) MarshalJSON ¶
added in v0.7.0
func (s *CreativeAdTechnologyProviders) MarshalJSON() ([]byte, error)
type CreativeCorrections ¶
type CreativeCorrections struct {
	// Contexts: All known serving contexts containing serving status
	// information.
	Contexts []*CreativeCorrectionsContexts `json:"contexts,omitempty"`

	// Details: Additional details about the correction.
	Details []string `json:"details,omitempty"`

	// Reason: The type of correction that was applied to the creative.
	Reason string `json:"reason,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Contexts") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Contexts") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeCorrections) MarshalJSON ¶
func (s *CreativeCorrections) MarshalJSON() ([]byte, error)
type CreativeCorrectionsContexts ¶
type CreativeCorrectionsContexts struct {
	// AuctionType: Only set when contextType=AUCTION_TYPE. Represents the
	// auction types this correction applies to.
	AuctionType []string `json:"auctionType,omitempty"`

	// ContextType: The type of context (e.g., location, platform, auction
	// type, SSL-ness).
	ContextType string `json:"contextType,omitempty"`

	// GeoCriteriaId: Only set when contextType=LOCATION. Represents the geo
	// criterias this correction applies to.
	GeoCriteriaId []int64 `json:"geoCriteriaId,omitempty"`

	// Platform: Only set when contextType=PLATFORM. Represents the
	// platforms this correction applies to.
	Platform []string `json:"platform,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AuctionType") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AuctionType") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeCorrectionsContexts) MarshalJSON ¶
func (s *CreativeCorrectionsContexts) MarshalJSON() ([]byte, error)
type CreativeDealIds ¶
type CreativeDealIds struct {
	// DealStatuses: A list of external deal ids and ARC approval status.
	DealStatuses []*CreativeDealIdsDealStatuses `json:"dealStatuses,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "DealStatuses") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DealStatuses") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeDealIds: The external deal ids associated with a creative.

func (*CreativeDealIds) MarshalJSON ¶
func (s *CreativeDealIds) MarshalJSON() ([]byte, error)
type CreativeDealIdsDealStatuses ¶
type CreativeDealIdsDealStatuses struct {
	// ArcStatus: ARC approval status.
	ArcStatus string `json:"arcStatus,omitempty"`

	// DealId: External deal ID.
	DealId int64 `json:"dealId,omitempty,string"`

	// WebPropertyId: Publisher ID.
	WebPropertyId int64 `json:"webPropertyId,omitempty"`

	// ForceSendFields is a list of field names (e.g. "ArcStatus") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "ArcStatus") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeDealIdsDealStatuses) MarshalJSON ¶
func (s *CreativeDealIdsDealStatuses) MarshalJSON() ([]byte, error)
type CreativeFilteringReasons ¶
type CreativeFilteringReasons struct {
	// Date: The date in ISO 8601 format for the data. The data is collected
	// from 00:00:00 to 23:59:59 in PST.
	Date string `json:"date,omitempty"`

	// Reasons: The filtering reasons.
	Reasons []*CreativeFilteringReasonsReasons `json:"reasons,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Date") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Date") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeFilteringReasons: The filtering reasons for the creative. Read-only. This field should not be set in requests.

func (*CreativeFilteringReasons) MarshalJSON ¶
func (s *CreativeFilteringReasons) MarshalJSON() ([]byte, error)
type CreativeFilteringReasonsReasons ¶
type CreativeFilteringReasonsReasons struct {
	// FilteringCount: The number of times the creative was filtered for the
	// status. The count is aggregated across all publishers on the
	// exchange.
	FilteringCount int64 `json:"filteringCount,omitempty,string"`

	// FilteringStatus: The filtering status code as defined in
	// creative-status-codes.txt.
	FilteringStatus int64 `json:"filteringStatus,omitempty"`

	// ForceSendFields is a list of field names (e.g. "FilteringCount") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "FilteringCount") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*CreativeFilteringReasonsReasons) MarshalJSON ¶
func (s *CreativeFilteringReasonsReasons) MarshalJSON() ([]byte, error)
type CreativeNativeAd ¶
type CreativeNativeAd struct {
	Advertiser string `json:"advertiser,omitempty"`

	// AppIcon: The app icon, for app download ads.
	AppIcon *CreativeNativeAdAppIcon `json:"appIcon,omitempty"`

	// Body: A long description of the ad.
	Body string `json:"body,omitempty"`

	// CallToAction: A label for the button that the user is supposed to
	// click.
	CallToAction string `json:"callToAction,omitempty"`

	// ClickLinkUrl: The URL that the browser/SDK will load when the user
	// clicks the ad.
	ClickLinkUrl string `json:"clickLinkUrl,omitempty"`

	// ClickTrackingUrl: The URL to use for click tracking.
	ClickTrackingUrl string `json:"clickTrackingUrl,omitempty"`

	// Headline: A short title for the ad.
	Headline string `json:"headline,omitempty"`

	// Image: A large image.
	Image *CreativeNativeAdImage `json:"image,omitempty"`

	// ImpressionTrackingUrl: The URLs are called when the impression is
	// rendered.
	ImpressionTrackingUrl []string `json:"impressionTrackingUrl,omitempty"`

	// Logo: A smaller image, for the advertiser logo.
	Logo *CreativeNativeAdLogo `json:"logo,omitempty"`

	// Price: The price of the promoted app including the currency info.
	Price string `json:"price,omitempty"`

	// StarRating: The app rating in the app store. Must be in the range
	// [0-5].
	StarRating float64 `json:"starRating,omitempty"`

	// VideoURL: The URL of the XML VAST for a native ad. Note this is a
	// separate field from resource.video_url.
	VideoURL string `json:"videoURL,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Advertiser") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Advertiser") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeNativeAd: If nativeAd is set, HTMLSnippet, videoVastXML, and the videoURL outside of nativeAd should not be set. (The videoURL inside nativeAd can be set.)

func (*CreativeNativeAd) MarshalJSON ¶
func (s *CreativeNativeAd) MarshalJSON() ([]byte, error)
func (*CreativeNativeAd) UnmarshalJSON ¶
func (s *CreativeNativeAd) UnmarshalJSON(data []byte) error
type CreativeNativeAdAppIcon ¶
type CreativeNativeAdAppIcon struct {
	Height int64 `json:"height,omitempty"`

	Url string `json:"url,omitempty"`

	Width int64 `json:"width,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Height") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeNativeAdAppIcon: The app icon, for app download ads.

func (*CreativeNativeAdAppIcon) MarshalJSON ¶
func (s *CreativeNativeAdAppIcon) MarshalJSON() ([]byte, error)
type CreativeNativeAdImage ¶
type CreativeNativeAdImage struct {
	Height int64 `json:"height,omitempty"`

	Url string `json:"url,omitempty"`

	Width int64 `json:"width,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Height") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeNativeAdImage: A large image.

func (*CreativeNativeAdImage) MarshalJSON ¶
func (s *CreativeNativeAdImage) MarshalJSON() ([]byte, error)
type CreativeNativeAdLogo ¶
type CreativeNativeAdLogo struct {
	Height int64 `json:"height,omitempty"`

	Url string `json:"url,omitempty"`

	Width int64 `json:"width,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Height") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativeNativeAdLogo: A smaller image, for the advertiser logo.

func (*CreativeNativeAdLogo) MarshalJSON ¶
func (s *CreativeNativeAdLogo) MarshalJSON() ([]byte, error)
type CreativeServingRestrictions ¶
type CreativeServingRestrictions struct {
	// Contexts: All known contexts/restrictions.
	Contexts []*CreativeServingRestrictionsContexts `json:"contexts,omitempty"`

	// DisapprovalReasons: The reasons for disapproval within this
	// restriction, if any. Note that not all disapproval reasons may be
	// categorized, so it is possible for the creative to have a status of
	// DISAPPROVED or CONDITIONALLY_APPROVED with an empty list for
	// disapproval_reasons. In this case, please reach out to your TAM to
	// help debug the issue.
	DisapprovalReasons []*CreativeServingRestrictionsDisapprovalReasons `json:"disapprovalReasons,omitempty"`

	// Reason: Why the creative is ineligible to serve in this context
	// (e.g., it has been explicitly disapproved or is pending review).
	Reason string `json:"reason,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Contexts") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Contexts") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeServingRestrictions) MarshalJSON ¶
func (s *CreativeServingRestrictions) MarshalJSON() ([]byte, error)
type CreativeServingRestrictionsContexts ¶
type CreativeServingRestrictionsContexts struct {
	// AuctionType: Only set when contextType=AUCTION_TYPE. Represents the
	// auction types this restriction applies to.
	AuctionType []string `json:"auctionType,omitempty"`

	// ContextType: The type of context (e.g., location, platform, auction
	// type, SSL-ness).
	ContextType string `json:"contextType,omitempty"`

	// GeoCriteriaId: Only set when contextType=LOCATION. Represents the geo
	// criterias this restriction applies to. Impressions are considered to
	// match a context if either the user location or publisher location
	// matches a given geoCriteriaId.
	GeoCriteriaId []int64 `json:"geoCriteriaId,omitempty"`

	// Platform: Only set when contextType=PLATFORM. Represents the
	// platforms this restriction applies to.
	Platform []string `json:"platform,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AuctionType") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AuctionType") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeServingRestrictionsContexts) MarshalJSON ¶
func (s *CreativeServingRestrictionsContexts) MarshalJSON() ([]byte, error)
type CreativeServingRestrictionsDisapprovalReasons ¶
type CreativeServingRestrictionsDisapprovalReasons struct {
	// Details: Additional details about the reason for disapproval.
	Details []string `json:"details,omitempty"`

	// Reason: The categorized reason for disapproval.
	Reason string `json:"reason,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Details") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Details") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CreativeServingRestrictionsDisapprovalReasons) MarshalJSON ¶
func (s *CreativeServingRestrictionsDisapprovalReasons) MarshalJSON() ([]byte, error)
type CreativesAddDealCall ¶
type CreativesAddDealCall struct {
	// contains filtered or unexported fields
}
func (*CreativesAddDealCall) Context ¶
func (c *CreativesAddDealCall) Context(ctx context.Context) *CreativesAddDealCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesAddDealCall) Do ¶
func (c *CreativesAddDealCall) Do(opts ...googleapi.CallOption) error

Do executes the "adexchangebuyer.creatives.addDeal" call.

func (*CreativesAddDealCall) Fields ¶
func (c *CreativesAddDealCall) Fields(s ...googleapi.Field) *CreativesAddDealCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesAddDealCall) Header ¶
func (c *CreativesAddDealCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type CreativesGetCall ¶
type CreativesGetCall struct {
	// contains filtered or unexported fields
}
func (*CreativesGetCall) Context ¶
func (c *CreativesGetCall) Context(ctx context.Context) *CreativesGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesGetCall) Do ¶
func (c *CreativesGetCall) Do(opts ...googleapi.CallOption) (*Creative, error)

Do executes the "adexchangebuyer.creatives.get" call. Exactly one of *Creative or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CreativesGetCall) Fields ¶
func (c *CreativesGetCall) Fields(s ...googleapi.Field) *CreativesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesGetCall) Header ¶
func (c *CreativesGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CreativesGetCall) IfNoneMatch ¶
func (c *CreativesGetCall) IfNoneMatch(entityTag string) *CreativesGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type CreativesInsertCall ¶
type CreativesInsertCall struct {
	// contains filtered or unexported fields
}
func (*CreativesInsertCall) Context ¶
func (c *CreativesInsertCall) Context(ctx context.Context) *CreativesInsertCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesInsertCall) Do ¶
func (c *CreativesInsertCall) Do(opts ...googleapi.CallOption) (*Creative, error)

Do executes the "adexchangebuyer.creatives.insert" call. Exactly one of *Creative or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CreativesInsertCall) Fields ¶
func (c *CreativesInsertCall) Fields(s ...googleapi.Field) *CreativesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesInsertCall) Header ¶
func (c *CreativesInsertCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type CreativesList ¶
type CreativesList struct {
	// Items: A list of creatives.
	Items []*Creative `json:"items,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through creatives. To
	// retrieve the next page of results, set the next request's "pageToken"
	// value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CreativesList: The creatives feed lists the active creatives for the Ad Exchange buyer accounts that the user has access to. Each entry in the feed corresponds to a single creative.

func (*CreativesList) MarshalJSON ¶
func (s *CreativesList) MarshalJSON() ([]byte, error)
type CreativesListCall ¶
type CreativesListCall struct {
	// contains filtered or unexported fields
}
func (*CreativesListCall) AccountId ¶
func (c *CreativesListCall) AccountId(accountId ...int64) *CreativesListCall

AccountId sets the optional parameter "accountId": When specified, only creatives for the given account ids are returned.

func (*CreativesListCall) BuyerCreativeId ¶
func (c *CreativesListCall) BuyerCreativeId(buyerCreativeId ...string) *CreativesListCall

BuyerCreativeId sets the optional parameter "buyerCreativeId": When specified, only creatives for the given buyer creative ids are returned.

func (*CreativesListCall) Context ¶
func (c *CreativesListCall) Context(ctx context.Context) *CreativesListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesListCall) DealsStatusFilter ¶
func (c *CreativesListCall) DealsStatusFilter(dealsStatusFilter string) *CreativesListCall

DealsStatusFilter sets the optional parameter "dealsStatusFilter": When specified, only creatives having the given deals status are returned.

Possible values:

"approved" - Creatives which have been approved for serving on


deals.

"conditionally_approved" - Creatives which have been conditionally


approved for serving on deals.

"disapproved" - Creatives which have been disapproved for serving


on deals.

"not_checked" - Creatives whose deals status is not yet checked.

func (*CreativesListCall) Do ¶
func (c *CreativesListCall) Do(opts ...googleapi.CallOption) (*CreativesList, error)

Do executes the "adexchangebuyer.creatives.list" call. Exactly one of *CreativesList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CreativesList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CreativesListCall) Fields ¶
func (c *CreativesListCall) Fields(s ...googleapi.Field) *CreativesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesListCall) Header ¶
func (c *CreativesListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CreativesListCall) IfNoneMatch ¶
func (c *CreativesListCall) IfNoneMatch(entityTag string) *CreativesListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*CreativesListCall) MaxResults ¶
func (c *CreativesListCall) MaxResults(maxResults int64) *CreativesListCall

MaxResults sets the optional parameter "maxResults": Maximum number of entries returned on one result page. If not set, the default is 100.

func (*CreativesListCall) OpenAuctionStatusFilter ¶
func (c *CreativesListCall) OpenAuctionStatusFilter(openAuctionStatusFilter string) *CreativesListCall

OpenAuctionStatusFilter sets the optional parameter "openAuctionStatusFilter": When specified, only creatives having the given open auction status are returned.

Possible values:

"approved" - Creatives which have been approved for serving on the


open auction.

"conditionally_approved" - Creatives which have been conditionally


approved for serving on the open auction.

"disapproved" - Creatives which have been disapproved for serving


on the open auction.

"not_checked" - Creatives whose open auction status is not yet


checked.

func (*CreativesListCall) PageToken ¶
func (c *CreativesListCall) PageToken(pageToken string) *CreativesListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*CreativesListCall) Pages ¶
func (c *CreativesListCall) Pages(ctx context.Context, f func(*CreativesList) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CreativesListDealsCall ¶
type CreativesListDealsCall struct {
	// contains filtered or unexported fields
}
func (*CreativesListDealsCall) Context ¶
func (c *CreativesListDealsCall) Context(ctx context.Context) *CreativesListDealsCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesListDealsCall) Do ¶
func (c *CreativesListDealsCall) Do(opts ...googleapi.CallOption) (*CreativeDealIds, error)

Do executes the "adexchangebuyer.creatives.listDeals" call. Exactly one of *CreativeDealIds or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CreativeDealIds.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CreativesListDealsCall) Fields ¶
func (c *CreativesListDealsCall) Fields(s ...googleapi.Field) *CreativesListDealsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesListDealsCall) Header ¶
func (c *CreativesListDealsCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CreativesListDealsCall) IfNoneMatch ¶
func (c *CreativesListDealsCall) IfNoneMatch(entityTag string) *CreativesListDealsCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type CreativesRemoveDealCall ¶
type CreativesRemoveDealCall struct {
	// contains filtered or unexported fields
}
func (*CreativesRemoveDealCall) Context ¶
func (c *CreativesRemoveDealCall) Context(ctx context.Context) *CreativesRemoveDealCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CreativesRemoveDealCall) Do ¶
func (c *CreativesRemoveDealCall) Do(opts ...googleapi.CallOption) error

Do executes the "adexchangebuyer.creatives.removeDeal" call.

func (*CreativesRemoveDealCall) Fields ¶
func (c *CreativesRemoveDealCall) Fields(s ...googleapi.Field) *CreativesRemoveDealCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CreativesRemoveDealCall) Header ¶
func (c *CreativesRemoveDealCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type CreativesService ¶
type CreativesService struct {
	// contains filtered or unexported fields
}
func NewCreativesService ¶
func NewCreativesService(s *Service) *CreativesService
func (*CreativesService) AddDeal ¶
func (r *CreativesService) AddDeal(accountId int64, buyerCreativeId string, dealId int64) *CreativesAddDealCall

AddDeal: Add a deal id association for the creative.

- accountId: The id for the account that will serve this creative. - buyerCreativeId: The buyer-specific id for this creative. - dealId: The id of the deal id to associate with this creative.

func (*CreativesService) Get ¶
func (r *CreativesService) Get(accountId int64, buyerCreativeId string) *CreativesGetCall

Get: Gets the status for a single creative. A creative will be available 30-40 minutes after submission.

- accountId: The id for the account that will serve this creative. - buyerCreativeId: The buyer-specific id for this creative.

func (*CreativesService) Insert ¶
func (r *CreativesService) Insert(creative *Creative) *CreativesInsertCall

Insert: Submit a new creative.

func (*CreativesService) List ¶
func (r *CreativesService) List() *CreativesListCall

List: Retrieves a list of the authenticated user's active creatives. A creative will be available 30-40 minutes after submission.

func (*CreativesService) ListDeals ¶
func (r *CreativesService) ListDeals(accountId int64, buyerCreativeId string) *CreativesListDealsCall

ListDeals: Lists the external deal ids associated with the creative.

- accountId: The id for the account that will serve this creative. - buyerCreativeId: The buyer-specific id for this creative.

func (*CreativesService) RemoveDeal ¶
func (r *CreativesService) RemoveDeal(accountId int64, buyerCreativeId string, dealId int64) *CreativesRemoveDealCall

RemoveDeal: Remove a deal id associated with the creative.

- accountId: The id for the account that will serve this creative. - buyerCreativeId: The buyer-specific id for this creative. - dealId: The id of the deal id to disassociate with this creative.

type DealServingMetadata ¶
type DealServingMetadata struct {
	// AlcoholAdsAllowed: True if alcohol ads are allowed for this deal
	// (read-only). This field is only populated when querying for finalized
	// orders using the method GetFinalizedOrderDeals
	AlcoholAdsAllowed bool `json:"alcoholAdsAllowed,omitempty"`

	// DealPauseStatus: Tracks which parties (if any) have paused a deal.
	// (readonly, except via PauseResumeOrderDeals action)
	DealPauseStatus *DealServingMetadataDealPauseStatus `json:"dealPauseStatus,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AlcoholAdsAllowed")
	// to unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AlcoholAdsAllowed") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*DealServingMetadata) MarshalJSON ¶
func (s *DealServingMetadata) MarshalJSON() ([]byte, error)
type DealServingMetadataDealPauseStatus ¶
type DealServingMetadataDealPauseStatus struct {
	BuyerPauseReason string `json:"buyerPauseReason,omitempty"`

	// FirstPausedBy: If the deal is paused, records which party paused the
	// deal first.
	FirstPausedBy string `json:"firstPausedBy,omitempty"`

	HasBuyerPaused bool `json:"hasBuyerPaused,omitempty"`

	HasSellerPaused bool `json:"hasSellerPaused,omitempty"`

	SellerPauseReason string `json:"sellerPauseReason,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BuyerPauseReason") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BuyerPauseReason") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}

DealServingMetadataDealPauseStatus: Tracks which parties (if any) have paused a deal. The deal is considered paused if has_buyer_paused || has_seller_paused. Each of the has_buyer_paused or the has_seller_paused bits can be set independently.

func (*DealServingMetadataDealPauseStatus) MarshalJSON ¶
func (s *DealServingMetadataDealPauseStatus) MarshalJSON() ([]byte, error)
type DealTerms ¶
type DealTerms struct {
	// BrandingType: Visibility of the URL in bid requests.
	BrandingType string `json:"brandingType,omitempty"`

	// CrossListedExternalDealIdType: Indicates that this ExternalDealId
	// exists under at least two different AdxInventoryDeals. Currently, the
	// only case that the same ExternalDealId will exist is programmatic
	// cross sell case.
	CrossListedExternalDealIdType string `json:"crossListedExternalDealIdType,omitempty"`

	// Description: Description for the proposed terms of the deal.
	Description string `json:"description,omitempty"`

	// EstimatedGrossSpend: Non-binding estimate of the estimated gross
	// spend for this deal Can be set by buyer or seller.
	EstimatedGrossSpend *Price `json:"estimatedGrossSpend,omitempty"`

	// EstimatedImpressionsPerDay: Non-binding estimate of the impressions
	// served per day Can be set by buyer or seller.
	EstimatedImpressionsPerDay int64 `json:"estimatedImpressionsPerDay,omitempty,string"`

	// GuaranteedFixedPriceTerms: The terms for guaranteed fixed price
	// deals.
	GuaranteedFixedPriceTerms *DealTermsGuaranteedFixedPriceTerms `json:"guaranteedFixedPriceTerms,omitempty"`

	// NonGuaranteedAuctionTerms: The terms for non-guaranteed auction
	// deals.
	NonGuaranteedAuctionTerms *DealTermsNonGuaranteedAuctionTerms `json:"nonGuaranteedAuctionTerms,omitempty"`

	// NonGuaranteedFixedPriceTerms: The terms for non-guaranteed fixed
	// price deals.
	NonGuaranteedFixedPriceTerms *DealTermsNonGuaranteedFixedPriceTerms `json:"nonGuaranteedFixedPriceTerms,omitempty"`

	// RubiconNonGuaranteedTerms: The terms for rubicon non-guaranteed
	// deals.
	RubiconNonGuaranteedTerms *DealTermsRubiconNonGuaranteedTerms `json:"rubiconNonGuaranteedTerms,omitempty"`

	// SellerTimeZone: For deals with Cost Per Day billing, defines the
	// timezone used to mark the boundaries of a day (buyer-readonly)
	SellerTimeZone string `json:"sellerTimeZone,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BrandingType") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BrandingType") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DealTerms) MarshalJSON ¶
func (s *DealTerms) MarshalJSON() ([]byte, error)
type DealTermsGuaranteedFixedPriceTerms ¶
type DealTermsGuaranteedFixedPriceTerms struct {
	// BillingInfo: External billing info for this Deal. This field is
	// relevant when external billing info such as price has a different
	// currency code than DFP/AdX.
	BillingInfo *DealTermsGuaranteedFixedPriceTermsBillingInfo `json:"billingInfo,omitempty"`

	// FixedPrices: Fixed price for the specified buyer.
	FixedPrices []*PricePerBuyer `json:"fixedPrices,omitempty"`

	// GuaranteedImpressions: Guaranteed impressions as a percentage. This
	// is the percentage of guaranteed looks that the buyer is guaranteeing
	// to buy.
	GuaranteedImpressions int64 `json:"guaranteedImpressions,omitempty,string"`

	// GuaranteedLooks: Count of guaranteed looks. Required for deal,
	// optional for product. For CPD deals, buyer changes to
	// guaranteed_looks will be ignored.
	GuaranteedLooks int64 `json:"guaranteedLooks,omitempty,string"`

	// MinimumDailyLooks: Count of minimum daily looks for a CPD deal. For
	// CPD deals, buyer should negotiate on this field instead of
	// guaranteed_looks.
	MinimumDailyLooks int64 `json:"minimumDailyLooks,omitempty,string"`

	// ForceSendFields is a list of field names (e.g. "BillingInfo") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BillingInfo") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DealTermsGuaranteedFixedPriceTerms) MarshalJSON ¶
func (s *DealTermsGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type DealTermsGuaranteedFixedPriceTermsBillingInfo ¶
type DealTermsGuaranteedFixedPriceTermsBillingInfo struct {
	// CurrencyConversionTimeMs: The timestamp (in ms since epoch) when the
	// original reservation price for the deal was first converted to DFP
	// currency. This is used to convert the contracted price into buyer's
	// currency without discrepancy.
	CurrencyConversionTimeMs int64 `json:"currencyConversionTimeMs,omitempty,string"`

	// DfpLineItemId: The DFP line item id associated with this deal. For
	// features like CPD, buyers can retrieve the DFP line item for billing
	// reconciliation.
	DfpLineItemId int64 `json:"dfpLineItemId,omitempty,string"`

	// OriginalContractedQuantity: The original contracted quantity (#
	// impressions) for this deal. To ensure delivery, sometimes the
	// publisher will book the deal with a impression buffer, such that
	// guaranteed_looks is greater than the contracted quantity. However
	// clients are billed using the original contracted quantity.
	OriginalContractedQuantity int64 `json:"originalContractedQuantity,omitempty,string"`

	// Price: The original reservation price for the deal, if the currency
	// code is different from the one used in negotiation.
	Price *Price `json:"price,omitempty"`

	// ForceSendFields is a list of field names (e.g.
	// "CurrencyConversionTimeMs") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted
	// from API requests. However, any non-pointer, non-interface field
	// appearing in ForceSendFields will be sent to the server regardless of
	// whether the field is empty or not. This may be used to include empty
	// fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CurrencyConversionTimeMs")
	// to include in API requests with the JSON null value. By default,
	// fields with empty values are omitted from API requests. However, any
	// field with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*DealTermsGuaranteedFixedPriceTermsBillingInfo) MarshalJSON ¶
func (s *DealTermsGuaranteedFixedPriceTermsBillingInfo) MarshalJSON() ([]byte, error)
type DealTermsNonGuaranteedAuctionTerms ¶
type DealTermsNonGuaranteedAuctionTerms struct {
	// AutoOptimizePrivateAuction: True if open auction buyers are allowed
	// to compete with invited buyers in this private auction
	// (buyer-readonly).
	AutoOptimizePrivateAuction bool `json:"autoOptimizePrivateAuction,omitempty"`

	// ReservePricePerBuyers: Reserve price for the specified buyer.
	ReservePricePerBuyers []*PricePerBuyer `json:"reservePricePerBuyers,omitempty"`

	// ForceSendFields is a list of field names (e.g.
	// "AutoOptimizePrivateAuction") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted
	// from API requests. However, any non-pointer, non-interface field
	// appearing in ForceSendFields will be sent to the server regardless of
	// whether the field is empty or not. This may be used to include empty
	// fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g.
	// "AutoOptimizePrivateAuction") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted
	// from API requests. However, any field with an empty value appearing
	// in NullFields will be sent to the server as null. It is an error if a
	// field in this list has a non-empty value. This may be used to include
	// null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DealTermsNonGuaranteedAuctionTerms) MarshalJSON ¶
func (s *DealTermsNonGuaranteedAuctionTerms) MarshalJSON() ([]byte, error)
type DealTermsNonGuaranteedFixedPriceTerms ¶
type DealTermsNonGuaranteedFixedPriceTerms struct {
	// FixedPrices: Fixed price for the specified buyer.
	FixedPrices []*PricePerBuyer `json:"fixedPrices,omitempty"`

	// ForceSendFields is a list of field names (e.g. "FixedPrices") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "FixedPrices") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DealTermsNonGuaranteedFixedPriceTerms) MarshalJSON ¶
func (s *DealTermsNonGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type DealTermsRubiconNonGuaranteedTerms ¶
type DealTermsRubiconNonGuaranteedTerms struct {
	// PriorityPrice: Optional price for Rubicon priority access in the
	// auction.
	PriorityPrice *Price `json:"priorityPrice,omitempty"`

	// StandardPrice: Optional price for Rubicon standard access in the
	// auction.
	StandardPrice *Price `json:"standardPrice,omitempty"`

	// ForceSendFields is a list of field names (e.g. "PriorityPrice") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "PriorityPrice") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DealTermsRubiconNonGuaranteedTerms) MarshalJSON ¶
func (s *DealTermsRubiconNonGuaranteedTerms) MarshalJSON() ([]byte, error)
type DeleteOrderDealsRequest ¶
type DeleteOrderDealsRequest struct {
	// DealIds: List of deals to delete for a given proposal
	DealIds []string `json:"dealIds,omitempty"`

	// ProposalRevisionNumber: The last known proposal revision number.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// UpdateAction: Indicates an optional action to take on the proposal
	UpdateAction string `json:"updateAction,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DealIds") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DealIds") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DeleteOrderDealsRequest) MarshalJSON ¶
func (s *DeleteOrderDealsRequest) MarshalJSON() ([]byte, error)
type DeleteOrderDealsResponse ¶
type DeleteOrderDealsResponse struct {
	// Deals: List of deals deleted (in the same proposal as passed in the
	// request)
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// ProposalRevisionNumber: The updated revision number for the proposal.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*DeleteOrderDealsResponse) MarshalJSON ¶
func (s *DeleteOrderDealsResponse) MarshalJSON() ([]byte, error)
type DeliveryControl ¶
type DeliveryControl struct {
	CreativeBlockingLevel string `json:"creativeBlockingLevel,omitempty"`

	DeliveryRateType string `json:"deliveryRateType,omitempty"`

	FrequencyCaps []*DeliveryControlFrequencyCap `json:"frequencyCaps,omitempty"`

	// ForceSendFields is a list of field names (e.g.
	// "CreativeBlockingLevel") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. However, any non-pointer, non-interface field appearing in
	// ForceSendFields will be sent to the server regardless of whether the
	// field is empty or not. This may be used to include empty fields in
	// Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CreativeBlockingLevel") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*DeliveryControl) MarshalJSON ¶
func (s *DeliveryControl) MarshalJSON() ([]byte, error)
type DeliveryControlFrequencyCap ¶
type DeliveryControlFrequencyCap struct {
	MaxImpressions int64 `json:"maxImpressions,omitempty"`

	NumTimeUnits int64 `json:"numTimeUnits,omitempty"`

	TimeUnitType string `json:"timeUnitType,omitempty"`

	// ForceSendFields is a list of field names (e.g. "MaxImpressions") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "MaxImpressions") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*DeliveryControlFrequencyCap) MarshalJSON ¶
func (s *DeliveryControlFrequencyCap) MarshalJSON() ([]byte, error)
type Dimension ¶
type Dimension struct {
	DimensionType string `json:"dimensionType,omitempty"`

	DimensionValues []*DimensionDimensionValue `json:"dimensionValues,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DimensionType") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DimensionType") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Dimension: This message carries publisher provided breakdown. E.g. {dimension_type: 'COUNTRY', [{dimension_value: {id: 1, name: 'US'}}, {dimension_value: {id: 2, name: 'UK'}}]}

func (*Dimension) MarshalJSON ¶
func (s *Dimension) MarshalJSON() ([]byte, error)
type DimensionDimensionValue ¶
type DimensionDimensionValue struct {
	// Id: Id of the dimension.
	Id int64 `json:"id,omitempty"`

	// Name: Name of the dimension mainly for debugging purposes, except for
	// the case of CREATIVE_SIZE. For CREATIVE_SIZE, strings are used
	// instead of ids.
	Name string `json:"name,omitempty"`

	// Percentage: Percent of total impressions for a dimension type. e.g.
	// {dimension_type: 'GENDER', [{dimension_value: {id: 1, name: 'MALE',
	// percentage: 60}}]} Gender MALE is 60% of all impressions which have
	// gender.
	Percentage int64 `json:"percentage,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Id") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Id") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

DimensionDimensionValue: Value of the dimension.

func (*DimensionDimensionValue) MarshalJSON ¶
func (s *DimensionDimensionValue) MarshalJSON() ([]byte, error)
type EditAllOrderDealsRequest ¶
type EditAllOrderDealsRequest struct {
	// Deals: List of deals to edit. Service may perform 3 different
	// operations based on comparison of deals in this list vs deals already
	// persisted in database: 1. Add new deal to proposal If a deal in this
	// list does not exist in the proposal, the service will create a new
	// deal and add it to the proposal. Validation will follow
	// AddOrderDealsRequest. 2. Update existing deal in the proposal If a
	// deal in this list already exist in the proposal, the service will
	// update that existing deal to this new deal in the request. Validation
	// will follow UpdateOrderDealsRequest. 3. Delete deals from the
	// proposal (just need the id) If a existing deal in the proposal is not
	// present in this list, the service will delete that deal from the
	// proposal. Validation will follow DeleteOrderDealsRequest.
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// Proposal: If specified, also updates the proposal in the batch
	// transaction. This is useful when the proposal and the deals need to
	// be updated in one transaction.
	Proposal *Proposal `json:"proposal,omitempty"`

	// ProposalRevisionNumber: The last known revision number for the
	// proposal.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// UpdateAction: Indicates an optional action to take on the proposal
	UpdateAction string `json:"updateAction,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*EditAllOrderDealsRequest) MarshalJSON ¶
func (s *EditAllOrderDealsRequest) MarshalJSON() ([]byte, error)
type EditAllOrderDealsResponse ¶
type EditAllOrderDealsResponse struct {
	// Deals: List of all deals in the proposal after edit.
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// OrderRevisionNumber: The latest revision number after the update has
	// been applied.
	OrderRevisionNumber int64 `json:"orderRevisionNumber,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*EditAllOrderDealsResponse) MarshalJSON ¶
func (s *EditAllOrderDealsResponse) MarshalJSON() ([]byte, error)
type GetOffersResponse ¶
type GetOffersResponse struct {
	// Products: The returned list of products.
	Products []*Product `json:"products,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Products") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Products") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*GetOffersResponse) MarshalJSON ¶
func (s *GetOffersResponse) MarshalJSON() ([]byte, error)
type GetOrderDealsResponse ¶
type GetOrderDealsResponse struct {
	// Deals: List of deals for the proposal
	Deals []*MarketplaceDeal `json:"deals,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Deals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*GetOrderDealsResponse) MarshalJSON ¶
func (s *GetOrderDealsResponse) MarshalJSON() ([]byte, error)
type GetOrderNotesResponse ¶
type GetOrderNotesResponse struct {
	// Notes: The list of matching notes. The notes for a proposal are
	// ordered from oldest to newest. If the notes span multiple proposals,
	// they will be grouped by proposal, with the notes for the most
	// recently modified proposal appearing first.
	Notes []*MarketplaceNote `json:"notes,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Notes") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Notes") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*GetOrderNotesResponse) MarshalJSON ¶
func (s *GetOrderNotesResponse) MarshalJSON() ([]byte, error)
type GetOrdersResponse ¶
type GetOrdersResponse struct {
	// Proposals: The list of matching proposals.
	Proposals []*Proposal `json:"proposals,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Proposals") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Proposals") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*GetOrdersResponse) MarshalJSON ¶
func (s *GetOrdersResponse) MarshalJSON() ([]byte, error)
type GetPublisherProfilesByAccountIdResponse ¶
type GetPublisherProfilesByAccountIdResponse struct {
	// Profiles: Profiles for the requested publisher
	Profiles []*PublisherProfileApiProto `json:"profiles,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Profiles") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Profiles") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*GetPublisherProfilesByAccountIdResponse) MarshalJSON ¶
func (s *GetPublisherProfilesByAccountIdResponse) MarshalJSON() ([]byte, error)
type MarketplaceDeal ¶
type MarketplaceDeal struct {
	// BuyerPrivateData: Buyer private data (hidden from seller).
	BuyerPrivateData *PrivateData `json:"buyerPrivateData,omitempty"`

	// CreationTimeMs: The time (ms since epoch) of the deal creation.
	// (readonly)
	CreationTimeMs int64 `json:"creationTimeMs,omitempty,string"`

	// CreativePreApprovalPolicy: Specifies the creative pre-approval policy
	// (buyer-readonly)
	CreativePreApprovalPolicy string `json:"creativePreApprovalPolicy,omitempty"`

	// CreativeSafeFrameCompatibility: Specifies whether the creative is
	// safeFrame compatible (buyer-readonly)
	CreativeSafeFrameCompatibility string `json:"creativeSafeFrameCompatibility,omitempty"`

	// DealId: A unique deal-id for the deal (readonly).
	DealId string `json:"dealId,omitempty"`

	// DealServingMetadata: Metadata about the serving status of this deal
	// (readonly, writes via custom actions)
	DealServingMetadata *DealServingMetadata `json:"dealServingMetadata,omitempty"`

	// DeliveryControl: The set of fields around delivery control that are
	// interesting for a buyer to see but are non-negotiable. These are set
	// by the publisher. This message is assigned an id of 100 since some
	// day we would want to model this as a protobuf extension.
	DeliveryControl *DeliveryControl `json:"deliveryControl,omitempty"`

	// ExternalDealId: The external deal id assigned to this deal once the
	// deal is finalized. This is the deal-id that shows up in
	// serving/reporting etc. (readonly)
	ExternalDealId string `json:"externalDealId,omitempty"`

	// FlightEndTimeMs: Proposed flight end time of the deal (ms since
	// epoch) This will generally be stored in a granularity of a second.
	// (updatable)
	FlightEndTimeMs int64 `json:"flightEndTimeMs,omitempty,string"`

	// FlightStartTimeMs: Proposed flight start time of the deal (ms since
	// epoch) This will generally be stored in a granularity of a second.
	// (updatable)
	FlightStartTimeMs int64 `json:"flightStartTimeMs,omitempty,string"`

	// InventoryDescription: Description for the deal terms.
	// (buyer-readonly)
	InventoryDescription string `json:"inventoryDescription,omitempty"`

	// IsRfpTemplate: Indicates whether the current deal is a RFP template.
	// RFP template is created by buyer and not based on seller created
	// products.
	IsRfpTemplate bool `json:"isRfpTemplate,omitempty"`

	// IsSetupComplete: True, if the buyside inventory setup is complete for
	// this deal. (readonly, except via OrderSetupCompleted action)
	IsSetupComplete bool `json:"isSetupComplete,omitempty"`

	// Kind: Identifies what kind of resource this is. Value: the fixed
	// string "adexchangebuyer#marketplaceDeal".
	Kind string `json:"kind,omitempty"`

	// LastUpdateTimeMs: The time (ms since epoch) when the deal was last
	// updated. (readonly)
	LastUpdateTimeMs int64 `json:"lastUpdateTimeMs,omitempty,string"`

	MakegoodRequestedReason string `json:"makegoodRequestedReason,omitempty"`

	// Name: The name of the deal. (updatable)
	Name string `json:"name,omitempty"`

	// ProductId: The product-id from which this deal was created.
	// (readonly, except on create)
	ProductId string `json:"productId,omitempty"`

	// ProductRevisionNumber: The revision number of the product that the
	// deal was created from (readonly, except on create)
	ProductRevisionNumber int64 `json:"productRevisionNumber,omitempty,string"`

	// ProgrammaticCreativeSource: Specifies the creative source for
	// programmatic deals, PUBLISHER means creative is provided by seller
	// and ADVERTISR means creative is provided by buyer. (buyer-readonly)
	ProgrammaticCreativeSource string `json:"programmaticCreativeSource,omitempty"`

	ProposalId string `json:"proposalId,omitempty"`

	// SellerContacts: Optional Seller contact information for the deal
	// (buyer-readonly)
	SellerContacts []*ContactInformation `json:"sellerContacts,omitempty"`

	// SharedTargetings: The shared targeting visible to buyers and sellers.
	// Each shared targeting entity is AND'd together. (updatable)
	SharedTargetings []*SharedTargeting `json:"sharedTargetings,omitempty"`

	// SyndicationProduct: The syndication product associated with the deal.
	// (readonly, except on create)
	SyndicationProduct string `json:"syndicationProduct,omitempty"`

	// Terms: The negotiable terms of the deal. (updatable)
	Terms *DealTerms `json:"terms,omitempty"`

	WebPropertyCode string `json:"webPropertyCode,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BuyerPrivateData") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BuyerPrivateData") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}

MarketplaceDeal: A proposal can contain multiple deals. A deal contains the terms and targeting information that is used for serving.

func (*MarketplaceDeal) MarshalJSON ¶
func (s *MarketplaceDeal) MarshalJSON() ([]byte, error)
type MarketplaceDealParty ¶
type MarketplaceDealParty struct {
	// Buyer: The buyer/seller associated with the deal. One of buyer/seller
	// is specified for a deal-party.
	Buyer *Buyer `json:"buyer,omitempty"`

	// Seller: The buyer/seller associated with the deal. One of
	// buyer/seller is specified for a deal party.
	Seller *Seller `json:"seller,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Buyer") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Buyer") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*MarketplaceDealParty) MarshalJSON ¶
func (s *MarketplaceDealParty) MarshalJSON() ([]byte, error)
type MarketplaceLabel ¶
type MarketplaceLabel struct {
	// AccountId: The accountId of the party that created the label.
	AccountId string `json:"accountId,omitempty"`

	// CreateTimeMs: The creation time (in ms since epoch) for the label.
	CreateTimeMs int64 `json:"createTimeMs,omitempty,string"`

	// DeprecatedMarketplaceDealParty: Information about the party that
	// created the label.
	DeprecatedMarketplaceDealParty *MarketplaceDealParty `json:"deprecatedMarketplaceDealParty,omitempty"`

	// Label: The label to use.
	Label string `json:"label,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AccountId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*MarketplaceLabel) MarshalJSON ¶
func (s *MarketplaceLabel) MarshalJSON() ([]byte, error)
type MarketplaceNote ¶
type MarketplaceNote struct {
	// CreatorRole: The role of the person (buyer/seller) creating the note.
	// (readonly)
	CreatorRole string `json:"creatorRole,omitempty"`

	// DealId: Notes can optionally be associated with a deal. (readonly,
	// except on create)
	DealId string `json:"dealId,omitempty"`

	// Kind: Identifies what kind of resource this is. Value: the fixed
	// string "adexchangebuyer#marketplaceNote".
	Kind string `json:"kind,omitempty"`

	// Note: The actual note to attach. (readonly, except on create)
	Note string `json:"note,omitempty"`

	// NoteId: The unique id for the note. (readonly)
	NoteId string `json:"noteId,omitempty"`

	// ProposalId: The proposalId that a note is attached to. (readonly)
	ProposalId string `json:"proposalId,omitempty"`

	// ProposalRevisionNumber: If the note is associated with a proposal
	// revision number, then store that here. (readonly, except on create)
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// TimestampMs: The timestamp (ms since epoch) that this note was
	// created. (readonly)
	TimestampMs int64 `json:"timestampMs,omitempty,string"`

	// ForceSendFields is a list of field names (e.g. "CreatorRole") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CreatorRole") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

MarketplaceNote: A proposal is associated with a bunch of notes which may optionally be associated with a deal and/or revision number.

func (*MarketplaceNote) MarshalJSON ¶
func (s *MarketplaceNote) MarshalJSON() ([]byte, error)
type MarketplacedealsDeleteCall ¶
type MarketplacedealsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacedealsDeleteCall) Context ¶
func (c *MarketplacedealsDeleteCall) Context(ctx context.Context) *MarketplacedealsDeleteCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacedealsDeleteCall) Do ¶
func (c *MarketplacedealsDeleteCall) Do(opts ...googleapi.CallOption) (*DeleteOrderDealsResponse, error)

Do executes the "adexchangebuyer.marketplacedeals.delete" call. Exactly one of *DeleteOrderDealsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *DeleteOrderDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacedealsDeleteCall) Fields ¶
func (c *MarketplacedealsDeleteCall) Fields(s ...googleapi.Field) *MarketplacedealsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacedealsDeleteCall) Header ¶
func (c *MarketplacedealsDeleteCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type MarketplacedealsInsertCall ¶
type MarketplacedealsInsertCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacedealsInsertCall) Context ¶
func (c *MarketplacedealsInsertCall) Context(ctx context.Context) *MarketplacedealsInsertCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacedealsInsertCall) Do ¶
func (c *MarketplacedealsInsertCall) Do(opts ...googleapi.CallOption) (*AddOrderDealsResponse, error)

Do executes the "adexchangebuyer.marketplacedeals.insert" call. Exactly one of *AddOrderDealsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AddOrderDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacedealsInsertCall) Fields ¶
func (c *MarketplacedealsInsertCall) Fields(s ...googleapi.Field) *MarketplacedealsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacedealsInsertCall) Header ¶
func (c *MarketplacedealsInsertCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type MarketplacedealsListCall ¶
type MarketplacedealsListCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacedealsListCall) Context ¶
func (c *MarketplacedealsListCall) Context(ctx context.Context) *MarketplacedealsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacedealsListCall) Do ¶
func (c *MarketplacedealsListCall) Do(opts ...googleapi.CallOption) (*GetOrderDealsResponse, error)

Do executes the "adexchangebuyer.marketplacedeals.list" call. Exactly one of *GetOrderDealsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *GetOrderDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacedealsListCall) Fields ¶
func (c *MarketplacedealsListCall) Fields(s ...googleapi.Field) *MarketplacedealsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacedealsListCall) Header ¶
func (c *MarketplacedealsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*MarketplacedealsListCall) IfNoneMatch ¶
func (c *MarketplacedealsListCall) IfNoneMatch(entityTag string) *MarketplacedealsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*MarketplacedealsListCall) PqlQuery ¶
func (c *MarketplacedealsListCall) PqlQuery(pqlQuery string) *MarketplacedealsListCall

PqlQuery sets the optional parameter "pqlQuery": Query string to retrieve specific deals.

type MarketplacedealsService ¶
type MarketplacedealsService struct {
	// contains filtered or unexported fields
}
func NewMarketplacedealsService ¶
func NewMarketplacedealsService(s *Service) *MarketplacedealsService
func (*MarketplacedealsService) Delete ¶
func (r *MarketplacedealsService) Delete(proposalId string, deleteorderdealsrequest *DeleteOrderDealsRequest) *MarketplacedealsDeleteCall

Delete: Delete the specified deals from the proposal

- proposalId: The proposalId to delete deals from.

func (*MarketplacedealsService) Insert ¶
func (r *MarketplacedealsService) Insert(proposalId string, addorderdealsrequest *AddOrderDealsRequest) *MarketplacedealsInsertCall

Insert: Add new deals for the specified proposal

- proposalId: proposalId for which deals need to be added.

func (*MarketplacedealsService) List ¶
func (r *MarketplacedealsService) List(proposalId string) *MarketplacedealsListCall

List: List all the deals for a given proposal

proposalId: The proposalId to get deals for. To search across all proposals specify order_id = '-' as part of the URL.
func (*MarketplacedealsService) Update ¶
func (r *MarketplacedealsService) Update(proposalId string, editallorderdealsrequest *EditAllOrderDealsRequest) *MarketplacedealsUpdateCall

Update: Replaces all the deals in the proposal with the passed in deals

- proposalId: The proposalId to edit deals on.

type MarketplacedealsUpdateCall ¶
type MarketplacedealsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacedealsUpdateCall) Context ¶
func (c *MarketplacedealsUpdateCall) Context(ctx context.Context) *MarketplacedealsUpdateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacedealsUpdateCall) Do ¶
func (c *MarketplacedealsUpdateCall) Do(opts ...googleapi.CallOption) (*EditAllOrderDealsResponse, error)

Do executes the "adexchangebuyer.marketplacedeals.update" call. Exactly one of *EditAllOrderDealsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *EditAllOrderDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacedealsUpdateCall) Fields ¶
func (c *MarketplacedealsUpdateCall) Fields(s ...googleapi.Field) *MarketplacedealsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacedealsUpdateCall) Header ¶
func (c *MarketplacedealsUpdateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type MarketplacenotesInsertCall ¶
type MarketplacenotesInsertCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacenotesInsertCall) Context ¶
func (c *MarketplacenotesInsertCall) Context(ctx context.Context) *MarketplacenotesInsertCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacenotesInsertCall) Do ¶
func (c *MarketplacenotesInsertCall) Do(opts ...googleapi.CallOption) (*AddOrderNotesResponse, error)

Do executes the "adexchangebuyer.marketplacenotes.insert" call. Exactly one of *AddOrderNotesResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AddOrderNotesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacenotesInsertCall) Fields ¶
func (c *MarketplacenotesInsertCall) Fields(s ...googleapi.Field) *MarketplacenotesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacenotesInsertCall) Header ¶
func (c *MarketplacenotesInsertCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type MarketplacenotesListCall ¶
type MarketplacenotesListCall struct {
	// contains filtered or unexported fields
}
func (*MarketplacenotesListCall) Context ¶
func (c *MarketplacenotesListCall) Context(ctx context.Context) *MarketplacenotesListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplacenotesListCall) Do ¶
func (c *MarketplacenotesListCall) Do(opts ...googleapi.CallOption) (*GetOrderNotesResponse, error)

Do executes the "adexchangebuyer.marketplacenotes.list" call. Exactly one of *GetOrderNotesResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *GetOrderNotesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MarketplacenotesListCall) Fields ¶
func (c *MarketplacenotesListCall) Fields(s ...googleapi.Field) *MarketplacenotesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplacenotesListCall) Header ¶
func (c *MarketplacenotesListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*MarketplacenotesListCall) IfNoneMatch ¶
func (c *MarketplacenotesListCall) IfNoneMatch(entityTag string) *MarketplacenotesListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*MarketplacenotesListCall) PqlQuery ¶
func (c *MarketplacenotesListCall) PqlQuery(pqlQuery string) *MarketplacenotesListCall

PqlQuery sets the optional parameter "pqlQuery": Query string to retrieve specific notes. To search the text contents of notes, please use syntax like "WHERE note.note = "foo" or "WHERE note.note LIKE "%bar%"

type MarketplacenotesService ¶
type MarketplacenotesService struct {
	// contains filtered or unexported fields
}
func NewMarketplacenotesService ¶
func NewMarketplacenotesService(s *Service) *MarketplacenotesService
func (*MarketplacenotesService) Insert ¶
func (r *MarketplacenotesService) Insert(proposalId string, addordernotesrequest *AddOrderNotesRequest) *MarketplacenotesInsertCall

Insert: Add notes to the proposal

- proposalId: The proposalId to add notes for.

func (*MarketplacenotesService) List ¶
func (r *MarketplacenotesService) List(proposalId string) *MarketplacenotesListCall

List: Get all the notes associated with a proposal

proposalId: The proposalId to get notes for. To search across all proposals specify order_id = '-' as part of the URL.
type MarketplaceprivateauctionService ¶
type MarketplaceprivateauctionService struct {
	// contains filtered or unexported fields
}
func NewMarketplaceprivateauctionService ¶
func NewMarketplaceprivateauctionService(s *Service) *MarketplaceprivateauctionService
func (*MarketplaceprivateauctionService) Updateproposal ¶
func (r *MarketplaceprivateauctionService) Updateproposal(privateAuctionId string, updateprivateauctionproposalrequest *UpdatePrivateAuctionProposalRequest) *MarketplaceprivateauctionUpdateproposalCall

Updateproposal: Update a given private auction proposal

- privateAuctionId: The private auction id to be updated.

type MarketplaceprivateauctionUpdateproposalCall ¶
type MarketplaceprivateauctionUpdateproposalCall struct {
	// contains filtered or unexported fields
}
func (*MarketplaceprivateauctionUpdateproposalCall) Context ¶
func (c *MarketplaceprivateauctionUpdateproposalCall) Context(ctx context.Context) *MarketplaceprivateauctionUpdateproposalCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MarketplaceprivateauctionUpdateproposalCall) Do ¶
func (c *MarketplaceprivateauctionUpdateproposalCall) Do(opts ...googleapi.CallOption) error

Do executes the "adexchangebuyer.marketplaceprivateauction.updateproposal" call.

func (*MarketplaceprivateauctionUpdateproposalCall) Fields ¶
func (c *MarketplaceprivateauctionUpdateproposalCall) Fields(s ...googleapi.Field) *MarketplaceprivateauctionUpdateproposalCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MarketplaceprivateauctionUpdateproposalCall) Header ¶
func (c *MarketplaceprivateauctionUpdateproposalCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type MobileApplication ¶
added in v0.32.0
type MobileApplication struct {
	AppStore string `json:"appStore,omitempty"`

	ExternalAppId string `json:"externalAppId,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AppStore") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AppStore") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*MobileApplication) MarshalJSON ¶
added in v0.32.0
func (s *MobileApplication) MarshalJSON() ([]byte, error)
type PerformanceReport ¶
type PerformanceReport struct {
	// BidRate: The number of bid responses with an ad.
	BidRate float64 `json:"bidRate,omitempty"`

	// BidRequestRate: The number of bid requests sent to your bidder.
	BidRequestRate float64 `json:"bidRequestRate,omitempty"`

	// CalloutStatusRate: Rate of various prefiltering statuses per match.
	// Please refer to the callout-status-codes.txt file for different
	// statuses.
	CalloutStatusRate []interface{} `json:"calloutStatusRate,omitempty"`

	// CookieMatcherStatusRate: Average QPS for cookie matcher operations.
	CookieMatcherStatusRate []interface{} `json:"cookieMatcherStatusRate,omitempty"`

	// CreativeStatusRate: Rate of ads with a given status. Please refer to
	// the creative-status-codes.txt file for different statuses.
	CreativeStatusRate []interface{} `json:"creativeStatusRate,omitempty"`

	// FilteredBidRate: The number of bid responses that were filtered due
	// to a policy violation or other errors.
	FilteredBidRate float64 `json:"filteredBidRate,omitempty"`

	// HostedMatchStatusRate: Average QPS for hosted match operations.
	HostedMatchStatusRate []interface{} `json:"hostedMatchStatusRate,omitempty"`

	// InventoryMatchRate: The number of potential queries based on your
	// pretargeting settings.
	InventoryMatchRate float64 `json:"inventoryMatchRate,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// Latency50thPercentile: The 50th percentile round trip latency(ms) as
	// perceived from Google servers for the duration period covered by the
	// report.
	Latency50thPercentile float64 `json:"latency50thPercentile,omitempty"`

	// Latency85thPercentile: The 85th percentile round trip latency(ms) as
	// perceived from Google servers for the duration period covered by the
	// report.
	Latency85thPercentile float64 `json:"latency85thPercentile,omitempty"`

	// Latency95thPercentile: The 95th percentile round trip latency(ms) as
	// perceived from Google servers for the duration period covered by the
	// report.
	Latency95thPercentile float64 `json:"latency95thPercentile,omitempty"`

	// NoQuotaInRegion: Rate of various quota account statuses per quota
	// check.
	NoQuotaInRegion float64 `json:"noQuotaInRegion,omitempty"`

	// OutOfQuota: Rate of various quota account statuses per quota check.
	OutOfQuota float64 `json:"outOfQuota,omitempty"`

	// PixelMatchRequests: Average QPS for pixel match requests from
	// clients.
	PixelMatchRequests float64 `json:"pixelMatchRequests,omitempty"`

	// PixelMatchResponses: Average QPS for pixel match responses from
	// clients.
	PixelMatchResponses float64 `json:"pixelMatchResponses,omitempty"`

	// QuotaConfiguredLimit: The configured quota limits for this account.
	QuotaConfiguredLimit float64 `json:"quotaConfiguredLimit,omitempty"`

	// QuotaThrottledLimit: The throttled quota limits for this account.
	QuotaThrottledLimit float64 `json:"quotaThrottledLimit,omitempty"`

	// Region: The trading location of this data.
	Region string `json:"region,omitempty"`

	// SuccessfulRequestRate: The number of properly formed bid responses
	// received by our servers within the deadline.
	SuccessfulRequestRate float64 `json:"successfulRequestRate,omitempty"`

	// Timestamp: The unix timestamp of the starting time of this
	// performance data.
	Timestamp int64 `json:"timestamp,omitempty,string"`

	// UnsuccessfulRequestRate: The number of bid responses that were
	// unsuccessful due to timeouts, incorrect formatting, etc.
	UnsuccessfulRequestRate float64 `json:"unsuccessfulRequestRate,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BidRate") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BidRate") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

PerformanceReport: The configuration data for an Ad Exchange performance report list.

func (*PerformanceReport) MarshalJSON ¶
func (s *PerformanceReport) MarshalJSON() ([]byte, error)
func (*PerformanceReport) UnmarshalJSON ¶
func (s *PerformanceReport) UnmarshalJSON(data []byte) error
type PerformanceReportList ¶
type PerformanceReportList struct {
	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// PerformanceReport: A list of performance reports relevant for the
	// account.
	PerformanceReport []*PerformanceReport `json:"performanceReport,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Kind") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Kind") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

PerformanceReportList: The configuration data for an Ad Exchange performance report list.

func (*PerformanceReportList) MarshalJSON ¶
func (s *PerformanceReportList) MarshalJSON() ([]byte, error)
type PerformanceReportListCall ¶
type PerformanceReportListCall struct {
	// contains filtered or unexported fields
}
func (*PerformanceReportListCall) Context ¶
func (c *PerformanceReportListCall) Context(ctx context.Context) *PerformanceReportListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PerformanceReportListCall) Do ¶
func (c *PerformanceReportListCall) Do(opts ...googleapi.CallOption) (*PerformanceReportList, error)

Do executes the "adexchangebuyer.performanceReport.list" call. Exactly one of *PerformanceReportList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PerformanceReportList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PerformanceReportListCall) Fields ¶
func (c *PerformanceReportListCall) Fields(s ...googleapi.Field) *PerformanceReportListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PerformanceReportListCall) Header ¶
func (c *PerformanceReportListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*PerformanceReportListCall) IfNoneMatch ¶
func (c *PerformanceReportListCall) IfNoneMatch(entityTag string) *PerformanceReportListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*PerformanceReportListCall) MaxResults ¶
func (c *PerformanceReportListCall) MaxResults(maxResults int64) *PerformanceReportListCall

MaxResults sets the optional parameter "maxResults": Maximum number of entries returned on one result page. If not set, the default is 100.

func (*PerformanceReportListCall) PageToken ¶
func (c *PerformanceReportListCall) PageToken(pageToken string) *PerformanceReportListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

type PerformanceReportService ¶
type PerformanceReportService struct {
	// contains filtered or unexported fields
}
func NewPerformanceReportService ¶
func NewPerformanceReportService(s *Service) *PerformanceReportService
func (*PerformanceReportService) List ¶
func (r *PerformanceReportService) List(accountId int64, endDateTime string, startDateTime string) *PerformanceReportListCall

List: Retrieves the authenticated user's list of performance metrics.

accountId: The account id to get the reports.
endDateTime: The end time of the report in ISO 8601 timestamp format using UTC.
startDateTime: The start time of the report in ISO 8601 timestamp format using UTC.
type PretargetingConfig ¶
type PretargetingConfig struct {
	// BillingId: The id for billing purposes, provided for reference. Leave
	// this field blank for insert requests; the id will be generated
	// automatically.
	BillingId int64 `json:"billingId,omitempty,string"`

	// ConfigId: The config id; generated automatically. Leave this field
	// blank for insert requests.
	ConfigId int64 `json:"configId,omitempty,string"`

	// ConfigName: The name of the config. Must be unique. Required for all
	// requests.
	ConfigName string `json:"configName,omitempty"`

	// CreativeType: List must contain exactly one of
	// PRETARGETING_CREATIVE_TYPE_HTML or PRETARGETING_CREATIVE_TYPE_VIDEO.
	CreativeType []string `json:"creativeType,omitempty"`

	// Dimensions: Requests which allow one of these (width, height) pairs
	// will match. All pairs must be supported ad dimensions.
	Dimensions []*PretargetingConfigDimensions `json:"dimensions,omitempty"`

	// ExcludedContentLabels: Requests with any of these content labels will
	// not match. Values are from content-labels.txt in the downloadable
	// files section.
	ExcludedContentLabels googleapi.Int64s `json:"excludedContentLabels,omitempty"`

	// ExcludedGeoCriteriaIds: Requests containing any of these geo criteria
	// ids will not match.
	ExcludedGeoCriteriaIds googleapi.Int64s `json:"excludedGeoCriteriaIds,omitempty"`

	// ExcludedPlacements: Requests containing any of these placements will
	// not match.
	ExcludedPlacements []*PretargetingConfigExcludedPlacements `json:"excludedPlacements,omitempty"`

	// ExcludedUserLists: Requests containing any of these users list ids
	// will not match.
	ExcludedUserLists googleapi.Int64s `json:"excludedUserLists,omitempty"`

	// ExcludedVerticals: Requests containing any of these vertical ids will
	// not match. Values are from the publisher-verticals.txt file in the
	// downloadable files section.
	ExcludedVerticals googleapi.Int64s `json:"excludedVerticals,omitempty"`

	// GeoCriteriaIds: Requests containing any of these geo criteria ids
	// will match.
	GeoCriteriaIds googleapi.Int64s `json:"geoCriteriaIds,omitempty"`

	// IsActive: Whether this config is active. Required for all requests.
	IsActive bool `json:"isActive,omitempty"`

	// Kind: The kind of the resource, i.e.
	// "adexchangebuyer#pretargetingConfig".
	Kind string `json:"kind,omitempty"`

	// Languages: Request containing any of these language codes will match.
	Languages []string `json:"languages,omitempty"`

	// MaximumQps: The maximum QPS allocated to this pretargeting
	// configuration, used for pretargeting-level QPS limits. By default,
	// this is not set, which indicates that there is no QPS limit at the
	// configuration level (a global or account-level limit may still be
	// imposed).
	MaximumQps int64 `json:"maximumQps,omitempty,string"`

	// MinimumViewabilityDecile: Requests where the predicted viewability is
	// below the specified decile will not match. E.g. if the buyer sets
	// this value to 5, requests from slots where the predicted viewability
	// is below 50% will not match. If the predicted viewability is unknown
	// this field will be ignored.
	MinimumViewabilityDecile int64 `json:"minimumViewabilityDecile,omitempty"`

	// MobileCarriers: Requests containing any of these mobile carrier ids
	// will match. Values are from mobile-carriers.csv in the downloadable
	// files section.
	MobileCarriers googleapi.Int64s `json:"mobileCarriers,omitempty"`

	// MobileDevices: Requests containing any of these mobile device ids
	// will match. Values are from mobile-devices.csv in the downloadable
	// files section.
	MobileDevices googleapi.Int64s `json:"mobileDevices,omitempty"`

	// MobileOperatingSystemVersions: Requests containing any of these
	// mobile operating system version ids will match. Values are from
	// mobile-os.csv in the downloadable files section.
	MobileOperatingSystemVersions googleapi.Int64s `json:"mobileOperatingSystemVersions,omitempty"`

	// Placements: Requests containing any of these placements will match.
	Placements []*PretargetingConfigPlacements `json:"placements,omitempty"`

	// Platforms: Requests matching any of these platforms will match.
	// Possible values are PRETARGETING_PLATFORM_MOBILE,
	// PRETARGETING_PLATFORM_DESKTOP, and PRETARGETING_PLATFORM_TABLET.
	Platforms []string `json:"platforms,omitempty"`

	// SupportedCreativeAttributes: Creative attributes should be declared
	// here if all creatives corresponding to this pretargeting
	// configuration have that creative attribute. Values are from
	// pretargetable-creative-attributes.txt in the downloadable files
	// section.
	SupportedCreativeAttributes googleapi.Int64s `json:"supportedCreativeAttributes,omitempty"`

	// UserIdentifierDataRequired: Requests containing the specified type of
	// user data will match. Possible values are HOSTED_MATCH_DATA, which
	// means the request is cookie-targetable and has a match in the buyer's
	// hosted match table, and COOKIE_OR_IDFA, which means the request has
	// either a targetable cookie or an iOS IDFA.
	UserIdentifierDataRequired []string `json:"userIdentifierDataRequired,omitempty"`

	// UserLists: Requests containing any of these user list ids will match.
	UserLists googleapi.Int64s `json:"userLists,omitempty"`

	// VendorTypes: Requests that allow any of these vendor ids will match.
	// Values are from vendors.txt in the downloadable files section.
	VendorTypes googleapi.Int64s `json:"vendorTypes,omitempty"`

	// Verticals: Requests containing any of these vertical ids will match.
	Verticals googleapi.Int64s `json:"verticals,omitempty"`

	// VideoPlayerSizes: Video requests satisfying any of these player size
	// constraints will match.
	VideoPlayerSizes []*PretargetingConfigVideoPlayerSizes `json:"videoPlayerSizes,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "BillingId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BillingId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfig) MarshalJSON ¶
func (s *PretargetingConfig) MarshalJSON() ([]byte, error)
type PretargetingConfigDeleteCall ¶
type PretargetingConfigDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigDeleteCall) Context ¶
func (c *PretargetingConfigDeleteCall) Context(ctx context.Context) *PretargetingConfigDeleteCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigDeleteCall) Do ¶
func (c *PretargetingConfigDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "adexchangebuyer.pretargetingConfig.delete" call.

func (*PretargetingConfigDeleteCall) Fields ¶
func (c *PretargetingConfigDeleteCall) Fields(s ...googleapi.Field) *PretargetingConfigDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigDeleteCall) Header ¶
func (c *PretargetingConfigDeleteCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigDimensions ¶
type PretargetingConfigDimensions struct {
	// Height: Height in pixels.
	Height int64 `json:"height,omitempty,string"`

	// Width: Width in pixels.
	Width int64 `json:"width,omitempty,string"`

	// ForceSendFields is a list of field names (e.g. "Height") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfigDimensions) MarshalJSON ¶
func (s *PretargetingConfigDimensions) MarshalJSON() ([]byte, error)
type PretargetingConfigExcludedPlacements ¶
type PretargetingConfigExcludedPlacements struct {
	// Token: The value of the placement. Interpretation depends on the
	// placement type, e.g. URL for a site placement, channel name for a
	// channel placement, app id for a mobile app placement.
	Token string `json:"token,omitempty"`

	// Type: The type of the placement.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Token") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Token") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfigExcludedPlacements) MarshalJSON ¶
func (s *PretargetingConfigExcludedPlacements) MarshalJSON() ([]byte, error)
type PretargetingConfigGetCall ¶
type PretargetingConfigGetCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigGetCall) Context ¶
func (c *PretargetingConfigGetCall) Context(ctx context.Context) *PretargetingConfigGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigGetCall) Do ¶
func (c *PretargetingConfigGetCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)

Do executes the "adexchangebuyer.pretargetingConfig.get" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PretargetingConfigGetCall) Fields ¶
func (c *PretargetingConfigGetCall) Fields(s ...googleapi.Field) *PretargetingConfigGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigGetCall) Header ¶
func (c *PretargetingConfigGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*PretargetingConfigGetCall) IfNoneMatch ¶
func (c *PretargetingConfigGetCall) IfNoneMatch(entityTag string) *PretargetingConfigGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PretargetingConfigInsertCall ¶
type PretargetingConfigInsertCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigInsertCall) Context ¶
func (c *PretargetingConfigInsertCall) Context(ctx context.Context) *PretargetingConfigInsertCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigInsertCall) Do ¶
func (c *PretargetingConfigInsertCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)

Do executes the "adexchangebuyer.pretargetingConfig.insert" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PretargetingConfigInsertCall) Fields ¶
func (c *PretargetingConfigInsertCall) Fields(s ...googleapi.Field) *PretargetingConfigInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigInsertCall) Header ¶
func (c *PretargetingConfigInsertCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigList ¶
type PretargetingConfigList struct {
	// Items: A list of pretargeting configs
	Items []*PretargetingConfig `json:"items,omitempty"`

	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfigList) MarshalJSON ¶
func (s *PretargetingConfigList) MarshalJSON() ([]byte, error)
type PretargetingConfigListCall ¶
type PretargetingConfigListCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigListCall) Context ¶
func (c *PretargetingConfigListCall) Context(ctx context.Context) *PretargetingConfigListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigListCall) Do ¶
func (c *PretargetingConfigListCall) Do(opts ...googleapi.CallOption) (*PretargetingConfigList, error)

Do executes the "adexchangebuyer.pretargetingConfig.list" call. Exactly one of *PretargetingConfigList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfigList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PretargetingConfigListCall) Fields ¶
func (c *PretargetingConfigListCall) Fields(s ...googleapi.Field) *PretargetingConfigListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigListCall) Header ¶
func (c *PretargetingConfigListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*PretargetingConfigListCall) IfNoneMatch ¶
func (c *PretargetingConfigListCall) IfNoneMatch(entityTag string) *PretargetingConfigListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PretargetingConfigPatchCall ¶
type PretargetingConfigPatchCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigPatchCall) Context ¶
func (c *PretargetingConfigPatchCall) Context(ctx context.Context) *PretargetingConfigPatchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigPatchCall) Do ¶
func (c *PretargetingConfigPatchCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)

Do executes the "adexchangebuyer.pretargetingConfig.patch" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PretargetingConfigPatchCall) Fields ¶
func (c *PretargetingConfigPatchCall) Fields(s ...googleapi.Field) *PretargetingConfigPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigPatchCall) Header ¶
func (c *PretargetingConfigPatchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigPlacements ¶
type PretargetingConfigPlacements struct {
	// Token: The value of the placement. Interpretation depends on the
	// placement type, e.g. URL for a site placement, channel name for a
	// channel placement, app id for a mobile app placement.
	Token string `json:"token,omitempty"`

	// Type: The type of the placement.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Token") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Token") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfigPlacements) MarshalJSON ¶
func (s *PretargetingConfigPlacements) MarshalJSON() ([]byte, error)
type PretargetingConfigService ¶
type PretargetingConfigService struct {
	// contains filtered or unexported fields
}
func NewPretargetingConfigService ¶
func NewPretargetingConfigService(s *Service) *PretargetingConfigService
func (*PretargetingConfigService) Delete ¶
func (r *PretargetingConfigService) Delete(accountId int64, configId int64) *PretargetingConfigDeleteCall

Delete: Deletes an existing pretargeting config.

- accountId: The account id to delete the pretargeting config for. - configId: The specific id of the configuration to delete.

func (*PretargetingConfigService) Get ¶
func (r *PretargetingConfigService) Get(accountId int64, configId int64) *PretargetingConfigGetCall

Get: Gets a specific pretargeting configuration

- accountId: The account id to get the pretargeting config for. - configId: The specific id of the configuration to retrieve.

func (*PretargetingConfigService) Insert ¶
func (r *PretargetingConfigService) Insert(accountId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigInsertCall

Insert: Inserts a new pretargeting configuration.

- accountId: The account id to insert the pretargeting config for.

func (*PretargetingConfigService) List ¶
func (r *PretargetingConfigService) List(accountId int64) *PretargetingConfigListCall

List: Retrieves a list of the authenticated user's pretargeting configurations.

- accountId: The account id to get the pretargeting configs for.

func (*PretargetingConfigService) Patch ¶
func (r *PretargetingConfigService) Patch(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigPatchCall

Patch: Updates an existing pretargeting config. This method supports patch semantics.

- accountId: The account id to update the pretargeting config for. - configId: The specific id of the configuration to update.

func (*PretargetingConfigService) Update ¶
func (r *PretargetingConfigService) Update(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigUpdateCall

Update: Updates an existing pretargeting config.

- accountId: The account id to update the pretargeting config for. - configId: The specific id of the configuration to update.

type PretargetingConfigUpdateCall ¶
type PretargetingConfigUpdateCall struct {
	// contains filtered or unexported fields
}
func (*PretargetingConfigUpdateCall) Context ¶
func (c *PretargetingConfigUpdateCall) Context(ctx context.Context) *PretargetingConfigUpdateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PretargetingConfigUpdateCall) Do ¶
func (c *PretargetingConfigUpdateCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)

Do executes the "adexchangebuyer.pretargetingConfig.update" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PretargetingConfigUpdateCall) Fields ¶
func (c *PretargetingConfigUpdateCall) Fields(s ...googleapi.Field) *PretargetingConfigUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PretargetingConfigUpdateCall) Header ¶
func (c *PretargetingConfigUpdateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigVideoPlayerSizes ¶
type PretargetingConfigVideoPlayerSizes struct {
	// AspectRatio: The type of aspect ratio. Leave this field blank to
	// match all aspect ratios.
	AspectRatio string `json:"aspectRatio,omitempty"`

	// MinHeight: The minimum player height in pixels. Leave this field
	// blank to match any player height.
	MinHeight int64 `json:"minHeight,omitempty,string"`

	// MinWidth: The minimum player width in pixels. Leave this field blank
	// to match any player width.
	MinWidth int64 `json:"minWidth,omitempty,string"`

	// ForceSendFields is a list of field names (e.g. "AspectRatio") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AspectRatio") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PretargetingConfigVideoPlayerSizes) MarshalJSON ¶
func (s *PretargetingConfigVideoPlayerSizes) MarshalJSON() ([]byte, error)
type Price ¶
type Price struct {
	// AmountMicros: The price value in micros.
	AmountMicros float64 `json:"amountMicros,omitempty"`

	// CurrencyCode: The currency code for the price.
	CurrencyCode string `json:"currencyCode,omitempty"`

	// ExpectedCpmMicros: In case of CPD deals, the expected CPM in micros.
	ExpectedCpmMicros float64 `json:"expectedCpmMicros,omitempty"`

	// PricingType: The pricing type for the deal/product.
	PricingType string `json:"pricingType,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AmountMicros") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AmountMicros") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Price) MarshalJSON ¶
func (s *Price) MarshalJSON() ([]byte, error)
func (*Price) UnmarshalJSON ¶
func (s *Price) UnmarshalJSON(data []byte) error
type PricePerBuyer ¶
type PricePerBuyer struct {
	// AuctionTier: Optional access type for this buyer.
	AuctionTier string `json:"auctionTier,omitempty"`

	// BilledBuyer: Reference to the buyer that will get billed.
	BilledBuyer *Buyer `json:"billedBuyer,omitempty"`

	// Buyer: The buyer who will pay this price. If unset, all buyers can
	// pay this price (if the advertisers match, and there's no more
	// specific rule matching the buyer).
	Buyer *Buyer `json:"buyer,omitempty"`

	// Price: The specified price
	Price *Price `json:"price,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AuctionTier") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AuctionTier") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

PricePerBuyer: Used to specify pricing rules for buyers. Each PricePerBuyer in a product can become [0,1] deals. To check if there is a PricePerBuyer for a particular buyer we look for the most specific matching rule - we first look for a rule matching the buyer and otherwise look for a matching rule where no buyer is set.

func (*PricePerBuyer) MarshalJSON ¶
func (s *PricePerBuyer) MarshalJSON() ([]byte, error)
type PrivateData ¶
type PrivateData struct {
	ReferenceId string `json:"referenceId,omitempty"`

	ReferencePayload string `json:"referencePayload,omitempty"`

	// ForceSendFields is a list of field names (e.g. "ReferenceId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "ReferenceId") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PrivateData) MarshalJSON ¶
func (s *PrivateData) MarshalJSON() ([]byte, error)
type Product ¶
type Product struct {
	// BilledBuyer: The billed buyer corresponding to the buyer that created
	// the offer. (readonly, except on create)
	BilledBuyer *Buyer `json:"billedBuyer,omitempty"`

	// Buyer: The buyer that created the offer if this is a buyer initiated
	// offer (readonly, except on create)
	Buyer *Buyer `json:"buyer,omitempty"`

	// CreationTimeMs: Creation time in ms. since epoch (readonly)
	CreationTimeMs int64 `json:"creationTimeMs,omitempty,string"`

	// CreatorContacts: Optional contact information for the creator of this
	// product. (buyer-readonly)
	CreatorContacts []*ContactInformation `json:"creatorContacts,omitempty"`

	// CreatorRole: The role that created the offer. Set to BUYER for buyer
	// initiated offers.
	CreatorRole string `json:"creatorRole,omitempty"`

	// DeliveryControl: The set of fields around delivery control that are
	// interesting for a buyer to see but are non-negotiable. These are set
	// by the publisher. This message is assigned an id of 100 since some
	// day we would want to model this as a protobuf extension.
	DeliveryControl *DeliveryControl `json:"deliveryControl,omitempty"`

	// FlightEndTimeMs: The proposed end time for the deal (ms since epoch)
	// (buyer-readonly)
	FlightEndTimeMs int64 `json:"flightEndTimeMs,omitempty,string"`

	// FlightStartTimeMs: Inventory availability dates. (times are in ms
	// since epoch) The granularity is generally in the order of seconds.
	// (buyer-readonly)
	FlightStartTimeMs int64 `json:"flightStartTimeMs,omitempty,string"`

	// HasCreatorSignedOff: If the creator has already signed off on the
	// product, then the buyer can finalize the deal by accepting the
	// product as is. When copying to a proposal, if any of the terms are
	// changed, then auto_finalize is automatically set to false.
	HasCreatorSignedOff bool `json:"hasCreatorSignedOff,omitempty"`

	// InventorySource: What exchange will provide this inventory (readonly,
	// except on create).
	InventorySource string `json:"inventorySource,omitempty"`

	// Kind: Identifies what kind of resource this is. Value: the fixed
	// string "adexchangebuyer#product".
	Kind string `json:"kind,omitempty"`

	// Labels: Optional List of labels for the product (optional,
	// buyer-readonly).
	Labels []*MarketplaceLabel `json:"labels,omitempty"`

	// LastUpdateTimeMs: Time of last update in ms. since epoch (readonly)
	LastUpdateTimeMs int64 `json:"lastUpdateTimeMs,omitempty,string"`

	// LegacyOfferId: Optional legacy offer id if this offer is a preferred
	// deal offer.
	LegacyOfferId string `json:"legacyOfferId,omitempty"`

	// MarketplacePublisherProfileId: Marketplace publisher profile Id. This
	// Id differs from the regular publisher_profile_id in that 1. This is a
	// new id, the old Id will be deprecated in 2017. 2. This id uniquely
	// identifies a publisher profile by itself.
	MarketplacePublisherProfileId string `json:"marketplacePublisherProfileId,omitempty"`

	// Name: The name for this product as set by the seller.
	// (buyer-readonly)
	Name string `json:"name,omitempty"`

	// PrivateAuctionId: Optional private auction id if this offer is a
	// private auction offer.
	PrivateAuctionId string `json:"privateAuctionId,omitempty"`

	// ProductId: The unique id for the product (readonly)
	ProductId string `json:"productId,omitempty"`

	// PublisherProfileId: Id of the publisher profile for a given seller. A
	// (seller.account_id, publisher_profile_id) pair uniquely identifies a
	// publisher profile. Buyers can call the PublisherProfiles::List
	// endpoint to get a list of publisher profiles for a given seller.
	PublisherProfileId string `json:"publisherProfileId,omitempty"`

	// PublisherProvidedForecast: Publisher self-provided forecast
	// information.
	PublisherProvidedForecast *PublisherProvidedForecast `json:"publisherProvidedForecast,omitempty"`

	// RevisionNumber: The revision number of the product. (readonly)
	RevisionNumber int64 `json:"revisionNumber,omitempty,string"`

	// Seller: Information about the seller that created this product
	// (readonly, except on create)
	Seller *Seller `json:"seller,omitempty"`

	// SharedTargetings: Targeting that is shared between the buyer and the
	// seller. Each targeting criteria has a specified key and for each key
	// there is a list of inclusion value or exclusion values.
	// (buyer-readonly)
	SharedTargetings []*SharedTargeting `json:"sharedTargetings,omitempty"`

	// State: The state of the product. (buyer-readonly)
	State string `json:"state,omitempty"`

	// SyndicationProduct: The syndication product associated with the deal.
	// (readonly, except on create)
	SyndicationProduct string `json:"syndicationProduct,omitempty"`

	// Terms: The negotiable terms of the deal (buyer-readonly)
	Terms *DealTerms `json:"terms,omitempty"`

	// WebPropertyCode: The web property code for the seller. This field is
	// meant to be copied over as is when creating deals.
	WebPropertyCode string `json:"webPropertyCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "BilledBuyer") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BilledBuyer") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Product: A product is segment of inventory that a seller wishes to sell. It is associated with certain terms and targeting information which helps buyer know more about the inventory. Each field in a product can have one of the following setting:

(readonly) - It is an error to try and set this field. (buyer-readonly) - Only the seller can set this field. (seller-readonly) - Only the buyer can set this field. (updatable) - The field is updatable at all times by either buyer or the seller.

func (*Product) MarshalJSON ¶
func (s *Product) MarshalJSON() ([]byte, error)
type ProductsGetCall ¶
type ProductsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProductsGetCall) Context ¶
func (c *ProductsGetCall) Context(ctx context.Context) *ProductsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProductsGetCall) Do ¶
func (c *ProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)

Do executes the "adexchangebuyer.products.get" call. Exactly one of *Product or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Product.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsGetCall) Fields ¶
func (c *ProductsGetCall) Fields(s ...googleapi.Field) *ProductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProductsGetCall) Header ¶
func (c *ProductsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ProductsGetCall) IfNoneMatch ¶
func (c *ProductsGetCall) IfNoneMatch(entityTag string) *ProductsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type ProductsSearchCall ¶
type ProductsSearchCall struct {
	// contains filtered or unexported fields
}
func (*ProductsSearchCall) Context ¶
func (c *ProductsSearchCall) Context(ctx context.Context) *ProductsSearchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProductsSearchCall) Do ¶
func (c *ProductsSearchCall) Do(opts ...googleapi.CallOption) (*GetOffersResponse, error)

Do executes the "adexchangebuyer.products.search" call. Exactly one of *GetOffersResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *GetOffersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProductsSearchCall) Fields ¶
func (c *ProductsSearchCall) Fields(s ...googleapi.Field) *ProductsSearchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProductsSearchCall) Header ¶
func (c *ProductsSearchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ProductsSearchCall) IfNoneMatch ¶
func (c *ProductsSearchCall) IfNoneMatch(entityTag string) *ProductsSearchCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*ProductsSearchCall) PqlQuery ¶
func (c *ProductsSearchCall) PqlQuery(pqlQuery string) *ProductsSearchCall

PqlQuery sets the optional parameter "pqlQuery": The pql query used to query for products.

type ProductsService ¶
type ProductsService struct {
	// contains filtered or unexported fields
}
func NewProductsService ¶
func NewProductsService(s *Service) *ProductsService
func (*ProductsService) Get ¶
func (r *ProductsService) Get(productId string) *ProductsGetCall

Get: Gets the requested product by id.

- productId: The id for the product to get the head revision for.

func (*ProductsService) Search ¶
func (r *ProductsService) Search() *ProductsSearchCall

Search: Gets the requested product.

type Proposal ¶
type Proposal struct {
	// BilledBuyer: Reference to the buyer that will get billed for this
	// proposal. (readonly)
	BilledBuyer *Buyer `json:"billedBuyer,omitempty"`

	// Buyer: Reference to the buyer on the proposal. (readonly, except on
	// create)
	Buyer *Buyer `json:"buyer,omitempty"`

	// BuyerContacts: Optional contact information of the buyer.
	// (seller-readonly)
	BuyerContacts []*ContactInformation `json:"buyerContacts,omitempty"`

	// BuyerPrivateData: Private data for buyer. (hidden from seller).
	BuyerPrivateData *PrivateData `json:"buyerPrivateData,omitempty"`

	// DbmAdvertiserIds: IDs of DBM advertisers permission to this proposal.
	DbmAdvertiserIds []string `json:"dbmAdvertiserIds,omitempty"`

	// HasBuyerSignedOff: When an proposal is in an accepted state,
	// indicates whether the buyer has signed off. Once both sides have
	// signed off on a deal, the proposal can be finalized by the seller.
	// (seller-readonly)
	HasBuyerSignedOff bool `json:"hasBuyerSignedOff,omitempty"`

	// HasSellerSignedOff: When an proposal is in an accepted state,
	// indicates whether the buyer has signed off Once both sides have
	// signed off on a deal, the proposal can be finalized by the seller.
	// (buyer-readonly)
	HasSellerSignedOff bool `json:"hasSellerSignedOff,omitempty"`

	// InventorySource: What exchange will provide this inventory (readonly,
	// except on create).
	InventorySource string `json:"inventorySource,omitempty"`

	// IsRenegotiating: True if the proposal is being renegotiated
	// (readonly).
	IsRenegotiating bool `json:"isRenegotiating,omitempty"`

	// IsSetupComplete: True, if the buyside inventory setup is complete for
	// this proposal. (readonly, except via OrderSetupCompleted action)
	// Deprecated in favor of deal level setup complete flag.
	IsSetupComplete bool `json:"isSetupComplete,omitempty"`

	// Kind: Identifies what kind of resource this is. Value: the fixed
	// string "adexchangebuyer#proposal".
	Kind string `json:"kind,omitempty"`

	// Labels: List of labels associated with the proposal. (readonly)
	Labels []*MarketplaceLabel `json:"labels,omitempty"`

	// LastUpdaterOrCommentorRole: The role of the last user that either
	// updated the proposal or left a comment. (readonly)
	LastUpdaterOrCommentorRole string `json:"lastUpdaterOrCommentorRole,omitempty"`

	// Name: The name for the proposal (updatable)
	Name string `json:"name,omitempty"`

	// NegotiationId: Optional negotiation id if this proposal is a
	// preferred deal proposal.
	NegotiationId string `json:"negotiationId,omitempty"`

	// OriginatorRole: Indicates whether the buyer/seller created the
	// proposal.(readonly)
	OriginatorRole string `json:"originatorRole,omitempty"`

	// PrivateAuctionId: Optional private auction id if this proposal is a
	// private auction proposal.
	PrivateAuctionId string `json:"privateAuctionId,omitempty"`

	// ProposalId: The unique id of the proposal. (readonly).
	ProposalId string `json:"proposalId,omitempty"`

	// ProposalState: The current state of the proposal. (readonly)
	ProposalState string `json:"proposalState,omitempty"`

	// RevisionNumber: The revision number for the proposal (readonly).
	RevisionNumber int64 `json:"revisionNumber,omitempty,string"`

	// RevisionTimeMs: The time (ms since epoch) when the proposal was last
	// revised (readonly).
	RevisionTimeMs int64 `json:"revisionTimeMs,omitempty,string"`

	// Seller: Reference to the seller on the proposal. (readonly, except on
	// create)
	Seller *Seller `json:"seller,omitempty"`

	// SellerContacts: Optional contact information of the seller
	// (buyer-readonly).
	SellerContacts []*ContactInformation `json:"sellerContacts,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "BilledBuyer") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BilledBuyer") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

Proposal: Represents a proposal in the marketplace. A proposal is the unit of negotiation between a seller and a buyer and contains deals which are served. Each field in a proposal can have one of the following setting:

(readonly) - It is an error to try and set this field. (buyer-readonly) - Only the seller can set this field. (seller-readonly) - Only the buyer can set this field. (updatable) - The field is updatable at all times by either buyer or the seller.

func (*Proposal) MarshalJSON ¶
func (s *Proposal) MarshalJSON() ([]byte, error)
type ProposalsGetCall ¶
type ProposalsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsGetCall) Context ¶
func (c *ProposalsGetCall) Context(ctx context.Context) *ProposalsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsGetCall) Do ¶
func (c *ProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer.proposals.get" call. Exactly one of *Proposal or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProposalsGetCall) Fields ¶
func (c *ProposalsGetCall) Fields(s ...googleapi.Field) *ProposalsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsGetCall) Header ¶
func (c *ProposalsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ProposalsGetCall) IfNoneMatch ¶
func (c *ProposalsGetCall) IfNoneMatch(entityTag string) *ProposalsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type ProposalsInsertCall ¶
type ProposalsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsInsertCall) Context ¶
func (c *ProposalsInsertCall) Context(ctx context.Context) *ProposalsInsertCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsInsertCall) Do ¶
func (c *ProposalsInsertCall) Do(opts ...googleapi.CallOption) (*CreateOrdersResponse, error)

Do executes the "adexchangebuyer.proposals.insert" call. Exactly one of *CreateOrdersResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CreateOrdersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProposalsInsertCall) Fields ¶
func (c *ProposalsInsertCall) Fields(s ...googleapi.Field) *ProposalsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsInsertCall) Header ¶
func (c *ProposalsInsertCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProposalsPatchCall ¶
type ProposalsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsPatchCall) Context ¶
func (c *ProposalsPatchCall) Context(ctx context.Context) *ProposalsPatchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsPatchCall) Do ¶
func (c *ProposalsPatchCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer.proposals.patch" call. Exactly one of *Proposal or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProposalsPatchCall) Fields ¶
func (c *ProposalsPatchCall) Fields(s ...googleapi.Field) *ProposalsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsPatchCall) Header ¶
func (c *ProposalsPatchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProposalsSearchCall ¶
type ProposalsSearchCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsSearchCall) Context ¶
func (c *ProposalsSearchCall) Context(ctx context.Context) *ProposalsSearchCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsSearchCall) Do ¶
func (c *ProposalsSearchCall) Do(opts ...googleapi.CallOption) (*GetOrdersResponse, error)

Do executes the "adexchangebuyer.proposals.search" call. Exactly one of *GetOrdersResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *GetOrdersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProposalsSearchCall) Fields ¶
func (c *ProposalsSearchCall) Fields(s ...googleapi.Field) *ProposalsSearchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsSearchCall) Header ¶
func (c *ProposalsSearchCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ProposalsSearchCall) IfNoneMatch ¶
func (c *ProposalsSearchCall) IfNoneMatch(entityTag string) *ProposalsSearchCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*ProposalsSearchCall) PqlQuery ¶
func (c *ProposalsSearchCall) PqlQuery(pqlQuery string) *ProposalsSearchCall

PqlQuery sets the optional parameter "pqlQuery": Query string to retrieve specific proposals.

type ProposalsService ¶
type ProposalsService struct {
	// contains filtered or unexported fields
}
func NewProposalsService ¶
func NewProposalsService(s *Service) *ProposalsService
func (*ProposalsService) Get ¶
func (r *ProposalsService) Get(proposalId string) *ProposalsGetCall

Get: Get a proposal given its id

- proposalId: Id of the proposal to retrieve.

func (*ProposalsService) Insert ¶
func (r *ProposalsService) Insert(createordersrequest *CreateOrdersRequest) *ProposalsInsertCall

Insert: Create the given list of proposals

func (*ProposalsService) Patch ¶
func (r *ProposalsService) Patch(proposalId string, revisionNumber int64, updateAction string, proposal *Proposal) *ProposalsPatchCall

Patch: Update the given proposal. This method supports patch semantics.

proposalId: The proposal id to update.
revisionNumber: The last known revision number to update. If the head revision in the marketplace database has since changed, an error will be thrown. The caller should then fetch the latest proposal at head revision and retry the update at that revision.
updateAction: The proposed action to take on the proposal. This field is required and it must be set when updating a proposal.
func (*ProposalsService) Search ¶
func (r *ProposalsService) Search() *ProposalsSearchCall

Search: Search for proposals using pql query

func (*ProposalsService) Setupcomplete ¶
func (r *ProposalsService) Setupcomplete(proposalId string) *ProposalsSetupcompleteCall

Setupcomplete: Update the given proposal to indicate that setup has been completed.

- proposalId: The proposal id for which the setup is complete.

func (*ProposalsService) Update ¶
func (r *ProposalsService) Update(proposalId string, revisionNumber int64, updateAction string, proposal *Proposal) *ProposalsUpdateCall

Update: Update the given proposal

proposalId: The proposal id to update.
revisionNumber: The last known revision number to update. If the head revision in the marketplace database has since changed, an error will be thrown. The caller should then fetch the latest proposal at head revision and retry the update at that revision.
updateAction: The proposed action to take on the proposal. This field is required and it must be set when updating a proposal.
type ProposalsSetupcompleteCall ¶
type ProposalsSetupcompleteCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsSetupcompleteCall) Context ¶
func (c *ProposalsSetupcompleteCall) Context(ctx context.Context) *ProposalsSetupcompleteCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsSetupcompleteCall) Do ¶
func (c *ProposalsSetupcompleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "adexchangebuyer.proposals.setupcomplete" call.

func (*ProposalsSetupcompleteCall) Fields ¶
func (c *ProposalsSetupcompleteCall) Fields(s ...googleapi.Field) *ProposalsSetupcompleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsSetupcompleteCall) Header ¶
func (c *ProposalsSetupcompleteCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProposalsUpdateCall ¶
type ProposalsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ProposalsUpdateCall) Context ¶
func (c *ProposalsUpdateCall) Context(ctx context.Context) *ProposalsUpdateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ProposalsUpdateCall) Do ¶
func (c *ProposalsUpdateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer.proposals.update" call. Exactly one of *Proposal or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProposalsUpdateCall) Fields ¶
func (c *ProposalsUpdateCall) Fields(s ...googleapi.Field) *ProposalsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ProposalsUpdateCall) Header ¶
func (c *ProposalsUpdateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PublisherProfileApiProto ¶
type PublisherProfileApiProto struct {
	// Audience: Publisher provided info on its audience.
	Audience string `json:"audience,omitempty"`

	// BuyerPitchStatement: A pitch statement for the buyer
	BuyerPitchStatement string `json:"buyerPitchStatement,omitempty"`

	// DirectContact: Direct contact for the publisher profile.
	DirectContact string `json:"directContact,omitempty"`

	// Exchange: Exchange where this publisher profile is from. E.g. AdX,
	// Rubicon etc...
	Exchange string `json:"exchange,omitempty"`

	ForecastInventory string `json:"forecastInventory,omitempty"`

	// GooglePlusLink: Link to publisher's Google+ page.
	GooglePlusLink string `json:"googlePlusLink,omitempty"`

	// IsParent: True, if this is the parent profile, which represents all
	// domains owned by the publisher.
	IsParent bool `json:"isParent,omitempty"`

	// IsPublished: True, if this profile is published. Deprecated for
	// state.
	IsPublished bool `json:"isPublished,omitempty"`

	// Kind: Identifies what kind of resource this is. Value: the fixed
	// string "adexchangebuyer#publisherProfileApiProto".
	Kind string `json:"kind,omitempty"`

	// LogoUrl: The url to the logo for the publisher.
	LogoUrl string `json:"logoUrl,omitempty"`

	// MediaKitLink: The url for additional marketing and sales materials.
	MediaKitLink string `json:"mediaKitLink,omitempty"`

	Name string `json:"name,omitempty"`

	// Overview: Publisher provided overview.
	Overview string `json:"overview,omitempty"`

	// ProfileId: The pair of (seller.account_id, profile_id) uniquely
	// identifies a publisher profile for a given publisher.
	ProfileId int64 `json:"profileId,omitempty"`

	// ProgrammaticContact: Programmatic contact for the publisher profile.
	ProgrammaticContact string `json:"programmaticContact,omitempty"`

	// PublisherAppIds: The list of app IDs represented in this publisher
	// profile. Empty if this is a parent profile. Deprecated in favor of
	// publisher_app.
	PublisherAppIds googleapi.Int64s `json:"publisherAppIds,omitempty"`

	// PublisherApps: The list of apps represented in this publisher
	// profile. Empty if this is a parent profile.
	PublisherApps []*MobileApplication `json:"publisherApps,omitempty"`

	// PublisherDomains: The list of domains represented in this publisher
	// profile. Empty if this is a parent profile.
	PublisherDomains []string `json:"publisherDomains,omitempty"`

	// PublisherProfileId: Unique Id for publisher profile.
	PublisherProfileId string `json:"publisherProfileId,omitempty"`

	// PublisherProvidedForecast: Publisher provided forecasting
	// information.
	PublisherProvidedForecast *PublisherProvidedForecast `json:"publisherProvidedForecast,omitempty"`

	// RateCardInfoLink: Link to publisher rate card
	RateCardInfoLink string `json:"rateCardInfoLink,omitempty"`

	// SamplePageLink: Link for a sample content page.
	SamplePageLink string `json:"samplePageLink,omitempty"`

	// Seller: Seller of the publisher profile.
	Seller *Seller `json:"seller,omitempty"`

	// State: State of the publisher profile.
	State string `json:"state,omitempty"`

	// TopHeadlines: Publisher provided key metrics and rankings.
	TopHeadlines []string `json:"topHeadlines,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Audience") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Audience") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*PublisherProfileApiProto) MarshalJSON ¶
func (s *PublisherProfileApiProto) MarshalJSON() ([]byte, error)
type PublisherProvidedForecast ¶
type PublisherProvidedForecast struct {
	// Dimensions: Publisher provided dimensions. E.g. geo, sizes etc...
	Dimensions []*Dimension `json:"dimensions,omitempty"`

	// WeeklyImpressions: Publisher provided weekly impressions.
	WeeklyImpressions int64 `json:"weeklyImpressions,omitempty,string"`

	// WeeklyUniques: Publisher provided weekly uniques.
	WeeklyUniques int64 `json:"weeklyUniques,omitempty,string"`

	// ForceSendFields is a list of field names (e.g. "Dimensions") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Dimensions") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

PublisherProvidedForecast: This message carries publisher provided forecasting information.

func (*PublisherProvidedForecast) MarshalJSON ¶
func (s *PublisherProvidedForecast) MarshalJSON() ([]byte, error)
type PubprofilesListCall ¶
type PubprofilesListCall struct {
	// contains filtered or unexported fields
}
func (*PubprofilesListCall) Context ¶
func (c *PubprofilesListCall) Context(ctx context.Context) *PubprofilesListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PubprofilesListCall) Do ¶
func (c *PubprofilesListCall) Do(opts ...googleapi.CallOption) (*GetPublisherProfilesByAccountIdResponse, error)

Do executes the "adexchangebuyer.pubprofiles.list" call. Exactly one of *GetPublisherProfilesByAccountIdResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *GetPublisherProfilesByAccountIdResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PubprofilesListCall) Fields ¶
func (c *PubprofilesListCall) Fields(s ...googleapi.Field) *PubprofilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PubprofilesListCall) Header ¶
func (c *PubprofilesListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*PubprofilesListCall) IfNoneMatch ¶
func (c *PubprofilesListCall) IfNoneMatch(entityTag string) *PubprofilesListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PubprofilesService ¶
type PubprofilesService struct {
	// contains filtered or unexported fields
}
func NewPubprofilesService ¶
func NewPubprofilesService(s *Service) *PubprofilesService
func (*PubprofilesService) List ¶
func (r *PubprofilesService) List(accountId int64) *PubprofilesListCall

List: Gets the requested publisher profile(s) by publisher accountId.

- accountId: The accountId of the publisher to get profiles for.

type Seller ¶
type Seller struct {
	// AccountId: The unique id for the seller. The seller fills in this
	// field. The seller account id is then available to buyer in the
	// product.
	AccountId string `json:"accountId,omitempty"`

	// SubAccountId: Optional sub-account id for the seller.
	SubAccountId string `json:"subAccountId,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AccountId") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Seller) MarshalJSON ¶
func (s *Seller) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Accounts *AccountsService

	BillingInfo *BillingInfoService

	Budget *BudgetService

	Creatives *CreativesService

	Marketplacedeals *MarketplacedealsService

	Marketplacenotes *MarketplacenotesService

	Marketplaceprivateauction *MarketplaceprivateauctionService

	PerformanceReport *PerformanceReportService

	PretargetingConfig *PretargetingConfigService

	Products *ProductsService

	Proposals *ProposalsService

	Pubprofiles *PubprofilesService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type SharedTargeting ¶
type SharedTargeting struct {
	// Exclusions: The list of values to exclude from targeting. Each value
	// is AND'd together.
	Exclusions []*TargetingValue `json:"exclusions,omitempty"`

	// Inclusions: The list of value to include as part of the targeting.
	// Each value is OR'd together.
	Inclusions []*TargetingValue `json:"inclusions,omitempty"`

	// Key: The key representing the shared targeting criterion.
	Key string `json:"key,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Exclusions") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Exclusions") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*SharedTargeting) MarshalJSON ¶
func (s *SharedTargeting) MarshalJSON() ([]byte, error)
type TargetingValue ¶
type TargetingValue struct {
	// CreativeSizeValue: The creative size value to exclude/include.
	CreativeSizeValue *TargetingValueCreativeSize `json:"creativeSizeValue,omitempty"`

	// DayPartTargetingValue: The daypart targeting to include / exclude.
	// Filled in when the key is GOOG_DAYPART_TARGETING.
	DayPartTargetingValue *TargetingValueDayPartTargeting `json:"dayPartTargetingValue,omitempty"`

	DemogAgeCriteriaValue *TargetingValueDemogAgeCriteria `json:"demogAgeCriteriaValue,omitempty"`

	DemogGenderCriteriaValue *TargetingValueDemogGenderCriteria `json:"demogGenderCriteriaValue,omitempty"`

	// LongValue: The long value to exclude/include.
	LongValue int64 `json:"longValue,omitempty,string"`

	RequestPlatformTargetingValue *TargetingValueRequestPlatformTargeting `json:"requestPlatformTargetingValue,omitempty"`

	// StringValue: The string value to exclude/include.
	StringValue string `json:"stringValue,omitempty"`

	// ForceSendFields is a list of field names (e.g. "CreativeSizeValue")
	// to unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CreativeSizeValue") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*TargetingValue) MarshalJSON ¶
func (s *TargetingValue) MarshalJSON() ([]byte, error)
type TargetingValueCreativeSize ¶
type TargetingValueCreativeSize struct {
	// AllowedFormats: The formats allowed by the publisher.
	AllowedFormats []string `json:"allowedFormats,omitempty"`

	// CompanionSizes: For video size type, the list of companion sizes.
	CompanionSizes []*TargetingValueSize `json:"companionSizes,omitempty"`

	// CreativeSizeType: The Creative size type.
	CreativeSizeType string `json:"creativeSizeType,omitempty"`

	// NativeTemplate: The native template for native ad.
	NativeTemplate string `json:"nativeTemplate,omitempty"`

	// Size: For regular or video creative size type, specifies the size of
	// the creative.
	Size *TargetingValueSize `json:"size,omitempty"`

	// SkippableAdType: The skippable ad type for video size.
	SkippableAdType string `json:"skippableAdType,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AllowedFormats") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AllowedFormats") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}

TargetingValueCreativeSize: Next Id: 7

func (*TargetingValueCreativeSize) MarshalJSON ¶
func (s *TargetingValueCreativeSize) MarshalJSON() ([]byte, error)
type TargetingValueDayPartTargeting ¶
type TargetingValueDayPartTargeting struct {
	DayParts []*TargetingValueDayPartTargetingDayPart `json:"dayParts,omitempty"`

	TimeZoneType string `json:"timeZoneType,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DayParts") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DayParts") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueDayPartTargeting) MarshalJSON ¶
func (s *TargetingValueDayPartTargeting) MarshalJSON() ([]byte, error)
type TargetingValueDayPartTargetingDayPart ¶
type TargetingValueDayPartTargetingDayPart struct {
	DayOfWeek string `json:"dayOfWeek,omitempty"`

	EndHour int64 `json:"endHour,omitempty"`

	EndMinute int64 `json:"endMinute,omitempty"`

	StartHour int64 `json:"startHour,omitempty"`

	StartMinute int64 `json:"startMinute,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DayOfWeek") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DayOfWeek") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueDayPartTargetingDayPart) MarshalJSON ¶
func (s *TargetingValueDayPartTargetingDayPart) MarshalJSON() ([]byte, error)
type TargetingValueDemogAgeCriteria ¶
type TargetingValueDemogAgeCriteria struct {
	DemogAgeCriteriaIds []string `json:"demogAgeCriteriaIds,omitempty"`

	// ForceSendFields is a list of field names (e.g. "DemogAgeCriteriaIds")
	// to unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DemogAgeCriteriaIds") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueDemogAgeCriteria) MarshalJSON ¶
func (s *TargetingValueDemogAgeCriteria) MarshalJSON() ([]byte, error)
type TargetingValueDemogGenderCriteria ¶
type TargetingValueDemogGenderCriteria struct {
	DemogGenderCriteriaIds []string `json:"demogGenderCriteriaIds,omitempty"`

	// ForceSendFields is a list of field names (e.g.
	// "DemogGenderCriteriaIds") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. However, any non-pointer, non-interface field appearing in
	// ForceSendFields will be sent to the server regardless of whether the
	// field is empty or not. This may be used to include empty fields in
	// Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "DemogGenderCriteriaIds")
	// to include in API requests with the JSON null value. By default,
	// fields with empty values are omitted from API requests. However, any
	// field with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueDemogGenderCriteria) MarshalJSON ¶
func (s *TargetingValueDemogGenderCriteria) MarshalJSON() ([]byte, error)
type TargetingValueRequestPlatformTargeting ¶
added in v0.33.0
type TargetingValueRequestPlatformTargeting struct {
	RequestPlatforms []string `json:"requestPlatforms,omitempty"`

	// ForceSendFields is a list of field names (e.g. "RequestPlatforms") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "RequestPlatforms") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueRequestPlatformTargeting) MarshalJSON ¶
added in v0.33.0
func (s *TargetingValueRequestPlatformTargeting) MarshalJSON() ([]byte, error)
type TargetingValueSize ¶
type TargetingValueSize struct {
	// Height: The height of the creative.
	Height int64 `json:"height,omitempty"`

	// Width: The width of the creative.
	Width int64 `json:"width,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Height") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*TargetingValueSize) MarshalJSON ¶
func (s *TargetingValueSize) MarshalJSON() ([]byte, error)
type UpdatePrivateAuctionProposalRequest ¶
type UpdatePrivateAuctionProposalRequest struct {
	// ExternalDealId: The externalDealId of the deal to be updated.
	ExternalDealId string `json:"externalDealId,omitempty"`

	// Note: Optional note to be added.
	Note *MarketplaceNote `json:"note,omitempty"`

	// ProposalRevisionNumber: The current revision number of the proposal
	// to be updated.
	ProposalRevisionNumber int64 `json:"proposalRevisionNumber,omitempty,string"`

	// UpdateAction: The proposed action on the private auction proposal.
	UpdateAction string `json:"updateAction,omitempty"`

	// ForceSendFields is a list of field names (e.g. "ExternalDealId") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "ExternalDealId") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*UpdatePrivateAuctionProposalRequest) MarshalJSON ¶
func (s *UpdatePrivateAuctionProposalRequest) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
adexchangebuyer-gen.go
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
