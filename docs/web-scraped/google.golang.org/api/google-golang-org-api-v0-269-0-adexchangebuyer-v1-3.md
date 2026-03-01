# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3

Title: adexchangebuyer package - google.golang.org/api/adexchangebuyer/v1.3 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3

Markdown Content:
Package adexchangebuyer provides access to the Ad Exchange Buyer API.

For product documentation, see: [https://developers.google.com/ad-exchange/buyer-rest](https://developers.google.com/ad-exchange/buyer-rest)

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/adexchangebuyer/v1.3"
...
ctx := context.Background()
adexchangebuyerService, err := adexchangebuyer.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication.

For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use option.WithAPIKey:

adexchangebuyerService, err := adexchangebuyer.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow), use option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adexchangebuyerService, err := adexchangebuyer.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [https://godoc.org/google.golang.org/api/option/](https://godoc.org/google.golang.org/api/option/) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#pkg-constants)
*   [type Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Account)
*       *   [func (s *Account) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Account.MarshalJSON)

*   [type AccountBidderLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountBidderLocation)
*       *   [func (s *AccountBidderLocation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountBidderLocation.MarshalJSON)

*   [type AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall)
*       *   [func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall.Context)
    *   [func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall.Do)
    *   [func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall.Fields)
    *   [func (c *AccountsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall.Header)
    *   [func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsGetCall.IfNoneMatch)

*   [type AccountsList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsList)
*       *   [func (s *AccountsList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsList.MarshalJSON)

*   [type AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall)
*       *   [func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall.Context)
    *   [func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*AccountsList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall.Do)
    *   [func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall.Fields)
    *   [func (c *AccountsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall.Header)
    *   [func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall.IfNoneMatch)

*   [type AccountsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsPatchCall)
*       *   [func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsPatchCall.Context)
    *   [func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*Account, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsPatchCall.Do)
    *   [func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsPatchCall.Fields)
    *   [func (c *AccountsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsPatchCall.Header)

*   [type AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService)
*       *   [func NewAccountsService(s *Service) *AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewAccountsService)

*       *   [func (r *AccountsService) Get(id int64) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService.Get)
    *   [func (r *AccountsService) List() *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService.List)
    *   [func (r *AccountsService) Patch(id int64, account *Account) *AccountsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService.Patch)
    *   [func (r *AccountsService) Update(id int64, account *Account) *AccountsUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService.Update)

*   [type AccountsUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsUpdateCall)
*       *   [func (c *AccountsUpdateCall) Context(ctx context.Context) *AccountsUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsUpdateCall.Context)
    *   [func (c *AccountsUpdateCall) Do(opts ...googleapi.CallOption) (*Account, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsUpdateCall.Do)
    *   [func (c *AccountsUpdateCall) Fields(s ...googleapi.Field) *AccountsUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsUpdateCall.Fields)
    *   [func (c *AccountsUpdateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsUpdateCall.Header)

*   [type BillingInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfo)
*       *   [func (s *BillingInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfo.MarshalJSON)

*   [type BillingInfoGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall)
*       *   [func (c *BillingInfoGetCall) Context(ctx context.Context) *BillingInfoGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall.Context)
    *   [func (c *BillingInfoGetCall) Do(opts ...googleapi.CallOption) (*BillingInfo, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall.Do)
    *   [func (c *BillingInfoGetCall) Fields(s ...googleapi.Field) *BillingInfoGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall.Fields)
    *   [func (c *BillingInfoGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall.Header)
    *   [func (c *BillingInfoGetCall) IfNoneMatch(entityTag string) *BillingInfoGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoGetCall.IfNoneMatch)

*   [type BillingInfoList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoList)
*       *   [func (s *BillingInfoList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoList.MarshalJSON)

*   [type BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall)
*       *   [func (c *BillingInfoListCall) Context(ctx context.Context) *BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall.Context)
    *   [func (c *BillingInfoListCall) Do(opts ...googleapi.CallOption) (*BillingInfoList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall.Do)
    *   [func (c *BillingInfoListCall) Fields(s ...googleapi.Field) *BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall.Fields)
    *   [func (c *BillingInfoListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall.Header)
    *   [func (c *BillingInfoListCall) IfNoneMatch(entityTag string) *BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall.IfNoneMatch)

*   [type BillingInfoService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService)
*       *   [func NewBillingInfoService(s *Service) *BillingInfoService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewBillingInfoService)

*       *   [func (r *BillingInfoService) Get(accountId int64) *BillingInfoGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService.Get)
    *   [func (r *BillingInfoService) List() *BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService.List)

*   [type Budget](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Budget)
*       *   [func (s *Budget) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Budget.MarshalJSON)

*   [type BudgetGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall)
*       *   [func (c *BudgetGetCall) Context(ctx context.Context) *BudgetGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall.Context)
    *   [func (c *BudgetGetCall) Do(opts ...googleapi.CallOption) (*Budget, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall.Do)
    *   [func (c *BudgetGetCall) Fields(s ...googleapi.Field) *BudgetGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall.Fields)
    *   [func (c *BudgetGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall.Header)
    *   [func (c *BudgetGetCall) IfNoneMatch(entityTag string) *BudgetGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetGetCall.IfNoneMatch)

*   [type BudgetPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetPatchCall)
*       *   [func (c *BudgetPatchCall) Context(ctx context.Context) *BudgetPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetPatchCall.Context)
    *   [func (c *BudgetPatchCall) Do(opts ...googleapi.CallOption) (*Budget, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetPatchCall.Do)
    *   [func (c *BudgetPatchCall) Fields(s ...googleapi.Field) *BudgetPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetPatchCall.Fields)
    *   [func (c *BudgetPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetPatchCall.Header)

*   [type BudgetService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService)
*       *   [func NewBudgetService(s *Service) *BudgetService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewBudgetService)

*       *   [func (r *BudgetService) Get(accountId int64, billingId int64) *BudgetGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService.Get)
    *   [func (r *BudgetService) Patch(accountId int64, billingId int64, budget *Budget) *BudgetPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService.Patch)
    *   [func (r *BudgetService) Update(accountId int64, billingId int64, budget *Budget) *BudgetUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService.Update)

*   [type BudgetUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetUpdateCall)
*       *   [func (c *BudgetUpdateCall) Context(ctx context.Context) *BudgetUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetUpdateCall.Context)
    *   [func (c *BudgetUpdateCall) Do(opts ...googleapi.CallOption) (*Budget, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetUpdateCall.Do)
    *   [func (c *BudgetUpdateCall) Fields(s ...googleapi.Field) *BudgetUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetUpdateCall.Fields)
    *   [func (c *BudgetUpdateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetUpdateCall.Header)

*   [type Creative](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Creative)
*       *   [func (s *Creative) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Creative.MarshalJSON)

*   [type CreativeAdTechnologyProviders](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeAdTechnologyProviders)
*       *   [func (s *CreativeAdTechnologyProviders) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeAdTechnologyProviders.MarshalJSON)

*   [type CreativeCorrections](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeCorrections)
*       *   [func (s *CreativeCorrections) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeCorrections.MarshalJSON)

*   [type CreativeDisapprovalReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeDisapprovalReasons)
*       *   [func (s *CreativeDisapprovalReasons) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeDisapprovalReasons.MarshalJSON)

*   [type CreativeFilteringReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasons)
*       *   [func (s *CreativeFilteringReasons) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasons.MarshalJSON)

*   [type CreativeFilteringReasonsReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasonsReasons)
*       *   [func (s *CreativeFilteringReasonsReasons) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasonsReasons.MarshalJSON)

*   [type CreativeNativeAd](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAd)
*       *   [func (s *CreativeNativeAd) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAd.MarshalJSON)
    *   [func (s *CreativeNativeAd) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAd.UnmarshalJSON)

*   [type CreativeNativeAdAppIcon](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdAppIcon)
*       *   [func (s *CreativeNativeAdAppIcon) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdAppIcon.MarshalJSON)

*   [type CreativeNativeAdImage](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdImage)
*       *   [func (s *CreativeNativeAdImage) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdImage.MarshalJSON)

*   [type CreativeNativeAdLogo](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdLogo)
*       *   [func (s *CreativeNativeAdLogo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdLogo.MarshalJSON)

*   [type CreativesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall)
*       *   [func (c *CreativesGetCall) Context(ctx context.Context) *CreativesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall.Context)
    *   [func (c *CreativesGetCall) Do(opts ...googleapi.CallOption) (*Creative, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall.Do)
    *   [func (c *CreativesGetCall) Fields(s ...googleapi.Field) *CreativesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall.Fields)
    *   [func (c *CreativesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall.Header)
    *   [func (c *CreativesGetCall) IfNoneMatch(entityTag string) *CreativesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesGetCall.IfNoneMatch)

*   [type CreativesInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall)
*       *   [func (c *CreativesInsertCall) Context(ctx context.Context) *CreativesInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall.Context)
    *   [func (c *CreativesInsertCall) Do(opts ...googleapi.CallOption) (*Creative, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall.Do)
    *   [func (c *CreativesInsertCall) Fields(s ...googleapi.Field) *CreativesInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall.Fields)
    *   [func (c *CreativesInsertCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall.Header)

*   [type CreativesList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesList)
*       *   [func (s *CreativesList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesList.MarshalJSON)

*   [type CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)
*       *   [func (c *CreativesListCall) AccountId(accountId ...int64) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.AccountId)
    *   [func (c *CreativesListCall) BuyerCreativeId(buyerCreativeId ...string) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.BuyerCreativeId)
    *   [func (c *CreativesListCall) Context(ctx context.Context) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.Context)
    *   [func (c *CreativesListCall) Do(opts ...googleapi.CallOption) (*CreativesList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.Do)
    *   [func (c *CreativesListCall) Fields(s ...googleapi.Field) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.Fields)
    *   [func (c *CreativesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.Header)
    *   [func (c *CreativesListCall) IfNoneMatch(entityTag string) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.IfNoneMatch)
    *   [func (c *CreativesListCall) MaxResults(maxResults int64) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.MaxResults)
    *   [func (c *CreativesListCall) PageToken(pageToken string) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.PageToken)
    *   [func (c *CreativesListCall) Pages(ctx context.Context, f func(*CreativesList) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.Pages)
    *   [func (c *CreativesListCall) StatusFilter(statusFilter string) *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall.StatusFilter)

*   [type CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService)
*       *   [func NewCreativesService(s *Service) *CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewCreativesService)

*       *   [func (r *CreativesService) Get(accountId int64, buyerCreativeId string) *CreativesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService.Get)
    *   [func (r *CreativesService) Insert(creative *Creative) *CreativesInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService.Insert)
    *   [func (r *CreativesService) List() *CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService.List)

*   [type DirectDeal](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDeal)
*       *   [func (s *DirectDeal) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDeal.MarshalJSON)

*   [type DirectDealsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall)
*       *   [func (c *DirectDealsGetCall) Context(ctx context.Context) *DirectDealsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall.Context)
    *   [func (c *DirectDealsGetCall) Do(opts ...googleapi.CallOption) (*DirectDeal, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall.Do)
    *   [func (c *DirectDealsGetCall) Fields(s ...googleapi.Field) *DirectDealsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall.Fields)
    *   [func (c *DirectDealsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall.Header)
    *   [func (c *DirectDealsGetCall) IfNoneMatch(entityTag string) *DirectDealsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsGetCall.IfNoneMatch)

*   [type DirectDealsList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsList)
*       *   [func (s *DirectDealsList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsList.MarshalJSON)

*   [type DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall)
*       *   [func (c *DirectDealsListCall) Context(ctx context.Context) *DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall.Context)
    *   [func (c *DirectDealsListCall) Do(opts ...googleapi.CallOption) (*DirectDealsList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall.Do)
    *   [func (c *DirectDealsListCall) Fields(s ...googleapi.Field) *DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall.Fields)
    *   [func (c *DirectDealsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall.Header)
    *   [func (c *DirectDealsListCall) IfNoneMatch(entityTag string) *DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall.IfNoneMatch)

*   [type DirectDealsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService)
*       *   [func NewDirectDealsService(s *Service) *DirectDealsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewDirectDealsService)

*       *   [func (r *DirectDealsService) Get(id int64) *DirectDealsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService.Get)
    *   [func (r *DirectDealsService) List() *DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService.List)

*   [type PerformanceReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReport)
*       *   [func (s *PerformanceReport) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReport.MarshalJSON)
    *   [func (s *PerformanceReport) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReport.UnmarshalJSON)

*   [type PerformanceReportList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportList)
*       *   [func (s *PerformanceReportList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportList.MarshalJSON)

*   [type PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall)
*       *   [func (c *PerformanceReportListCall) Context(ctx context.Context) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.Context)
    *   [func (c *PerformanceReportListCall) Do(opts ...googleapi.CallOption) (*PerformanceReportList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.Do)
    *   [func (c *PerformanceReportListCall) Fields(s ...googleapi.Field) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.Fields)
    *   [func (c *PerformanceReportListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.Header)
    *   [func (c *PerformanceReportListCall) IfNoneMatch(entityTag string) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.IfNoneMatch)
    *   [func (c *PerformanceReportListCall) MaxResults(maxResults int64) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.MaxResults)
    *   [func (c *PerformanceReportListCall) PageToken(pageToken string) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportListCall.PageToken)

*   [type PerformanceReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportService)
*       *   [func NewPerformanceReportService(s *Service) *PerformanceReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewPerformanceReportService)

*       *   [func (r *PerformanceReportService) List(accountId int64, endDateTime string, startDateTime string) *PerformanceReportListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportService.List)

*   [type PretargetingConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfig)
*       *   [func (s *PretargetingConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfig.MarshalJSON)

*   [type PretargetingConfigDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDeleteCall)
*       *   [func (c *PretargetingConfigDeleteCall) Context(ctx context.Context) *PretargetingConfigDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDeleteCall.Context)
    *   [func (c *PretargetingConfigDeleteCall) Do(opts ...googleapi.CallOption) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDeleteCall.Do)
    *   [func (c *PretargetingConfigDeleteCall) Fields(s ...googleapi.Field) *PretargetingConfigDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDeleteCall.Fields)
    *   [func (c *PretargetingConfigDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDeleteCall.Header)

*   [type PretargetingConfigDimensions](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDimensions)
*       *   [func (s *PretargetingConfigDimensions) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDimensions.MarshalJSON)

*   [type PretargetingConfigExcludedPlacements](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigExcludedPlacements)
*       *   [func (s *PretargetingConfigExcludedPlacements) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigExcludedPlacements.MarshalJSON)

*   [type PretargetingConfigGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall)
*       *   [func (c *PretargetingConfigGetCall) Context(ctx context.Context) *PretargetingConfigGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall.Context)
    *   [func (c *PretargetingConfigGetCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall.Do)
    *   [func (c *PretargetingConfigGetCall) Fields(s ...googleapi.Field) *PretargetingConfigGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall.Fields)
    *   [func (c *PretargetingConfigGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall.Header)
    *   [func (c *PretargetingConfigGetCall) IfNoneMatch(entityTag string) *PretargetingConfigGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigGetCall.IfNoneMatch)

*   [type PretargetingConfigInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigInsertCall)
*       *   [func (c *PretargetingConfigInsertCall) Context(ctx context.Context) *PretargetingConfigInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigInsertCall.Context)
    *   [func (c *PretargetingConfigInsertCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigInsertCall.Do)
    *   [func (c *PretargetingConfigInsertCall) Fields(s ...googleapi.Field) *PretargetingConfigInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigInsertCall.Fields)
    *   [func (c *PretargetingConfigInsertCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigInsertCall.Header)

*   [type PretargetingConfigList](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigList)
*       *   [func (s *PretargetingConfigList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigList.MarshalJSON)

*   [type PretargetingConfigListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall)
*       *   [func (c *PretargetingConfigListCall) Context(ctx context.Context) *PretargetingConfigListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall.Context)
    *   [func (c *PretargetingConfigListCall) Do(opts ...googleapi.CallOption) (*PretargetingConfigList, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall.Do)
    *   [func (c *PretargetingConfigListCall) Fields(s ...googleapi.Field) *PretargetingConfigListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall.Fields)
    *   [func (c *PretargetingConfigListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall.Header)
    *   [func (c *PretargetingConfigListCall) IfNoneMatch(entityTag string) *PretargetingConfigListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigListCall.IfNoneMatch)

*   [type PretargetingConfigPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPatchCall)
*       *   [func (c *PretargetingConfigPatchCall) Context(ctx context.Context) *PretargetingConfigPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPatchCall.Context)
    *   [func (c *PretargetingConfigPatchCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPatchCall.Do)
    *   [func (c *PretargetingConfigPatchCall) Fields(s ...googleapi.Field) *PretargetingConfigPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPatchCall.Fields)
    *   [func (c *PretargetingConfigPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPatchCall.Header)

*   [type PretargetingConfigPlacements](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPlacements)
*       *   [func (s *PretargetingConfigPlacements) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPlacements.MarshalJSON)

*   [type PretargetingConfigService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService)
*       *   [func NewPretargetingConfigService(s *Service) *PretargetingConfigService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewPretargetingConfigService)

*       *   [func (r *PretargetingConfigService) Delete(accountId int64, configId int64) *PretargetingConfigDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.Delete)
    *   [func (r *PretargetingConfigService) Get(accountId int64, configId int64) *PretargetingConfigGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.Get)
    *   [func (r *PretargetingConfigService) Insert(accountId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.Insert)
    *   [func (r *PretargetingConfigService) List(accountId int64) *PretargetingConfigListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.List)
    *   [func (r *PretargetingConfigService) Patch(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.Patch)
    *   [func (r *PretargetingConfigService) Update(accountId int64, configId int64, pretargetingconfig *PretargetingConfig) *PretargetingConfigUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService.Update)

*   [type PretargetingConfigUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigUpdateCall)
*       *   [func (c *PretargetingConfigUpdateCall) Context(ctx context.Context) *PretargetingConfigUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigUpdateCall.Context)
    *   [func (c *PretargetingConfigUpdateCall) Do(opts ...googleapi.CallOption) (*PretargetingConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigUpdateCall.Do)
    *   [func (c *PretargetingConfigUpdateCall) Fields(s ...googleapi.Field) *PretargetingConfigUpdateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigUpdateCall.Fields)
    *   [func (c *PretargetingConfigUpdateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigUpdateCall.Header)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#NewService)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adexchangebuyer/v1.3/adexchangebuyer-gen.go#L80)

const (
	AdexchangeBuyerScope = "https://www.googleapis.com/auth/adexchange.buyer"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type Account struct {
	BidderLocation []*[AccountBidderLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountBidderLocation) `json:"bidderLocation,omitempty"`

	
	
	CookieMatchingNid [string](https://pkg.go.dev/builtin#string) `json:"cookieMatchingNid,omitempty"`

	CookieMatchingUrl [string](https://pkg.go.dev/builtin#string) `json:"cookieMatchingUrl,omitempty"`

	Id [int64](https://pkg.go.dev/builtin#int64) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	
	MaximumActiveCreatives [int64](https://pkg.go.dev/builtin#int64) `json:"maximumActiveCreatives,omitempty"`

	
	
	MaximumTotalQps [int64](https://pkg.go.dev/builtin#int64) `json:"maximumTotalQps,omitempty"`

	
	NumberActiveCreatives [int64](https://pkg.go.dev/builtin#int64) `json:"numberActiveCreatives,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Account: Configuration data for an Ad Exchange buyer account.

type AccountBidderLocation struct {
	MaximumQps [int64](https://pkg.go.dev/builtin#int64) `json:"maximumQps,omitempty"`

	
	
	
	
	
	
	Region [string](https://pkg.go.dev/builtin#string) `json:"region,omitempty"`

	Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AccountsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.accounts.get" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

AccountsList: An account feed lists Ad Exchange buyer accounts that the user has access to. Each entry in the feed corresponds to a single buyer account.

type AccountsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.accounts.list" call. Exactly one of *AccountsList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AccountsList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsPatchCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.accounts.patch" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type AccountsService struct {
	
}

func NewAccountsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService)

Get: Gets one account by ID.

- id: The account id.

func (r *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService)) List() *[AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsListCall)

List: Retrieves the authenticated user's list of accounts.

Patch: Updates an existing account. This method supports patch semantics.

- id: The account id.

Update: Updates an existing account.

- id: The account id.

type AccountsUpdateCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.accounts.update" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type BillingInfo struct {
	AccountId [int64](https://pkg.go.dev/builtin#int64) `json:"accountId,omitempty"`

	AccountName [string](https://pkg.go.dev/builtin#string) `json:"accountName,omitempty"`

	
	
	BillingId [][string](https://pkg.go.dev/builtin#string) `json:"billingId,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BillingInfo: The configuration data for an Ad Exchange billing info.

type BillingInfoGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.billingInfo.get" call. Exactly one of *BillingInfo or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *BillingInfo.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

BillingInfoList: A billing info feed lists Billing Info the Ad Exchange buyer account has access to. Each entry in the feed corresponds to a single billing info.

type BillingInfoListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.billingInfo.list" call. Exactly one of *BillingInfoList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *BillingInfoList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type BillingInfoService struct {
	
}

func NewBillingInfoService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[BillingInfoService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService)

Get: Returns the billing information for one account specified by account ID.

- accountId: The account id.

func (r *[BillingInfoService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService)) List() *[BillingInfoListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoListCall)

List: Retrieves a list of billing information for all accounts of the authenticated user.

type Budget struct {
	
	AccountId [int64](https://pkg.go.dev/builtin#int64) `json:"accountId,omitempty,string"`

	
	BillingId [int64](https://pkg.go.dev/builtin#int64) `json:"billingId,omitempty,string"`

	
	
	BudgetAmount [int64](https://pkg.go.dev/builtin#int64) `json:"budgetAmount,omitempty,string"`

	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`

	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Budget: The configuration data for Ad Exchange RTB - Budget API.

type BudgetGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.budget.get" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type BudgetPatchCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.budget.patch" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type BudgetService struct {
	
}

func NewBudgetService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[BudgetService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService)

Get: Returns the budget information for the adgroup specified by the accountId and billingId.

- accountId: The account id to get the budget information for. - billingId: The billing id to get the budget information for.

Patch: Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request. This method supports patch semantics.

- accountId: The account id associated with the budget being updated. - billingId: The billing id associated with the budget being updated.

Update: Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request.

- accountId: The account id associated with the budget being updated. - billingId: The billing id associated with the budget being updated.

type BudgetUpdateCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.budget.update" call. Exactly one of *Budget or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Budget.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type Creative struct {
	
	HTMLSnippet [string](https://pkg.go.dev/builtin#string) `json:"HTMLSnippet,omitempty"`

	AccountId [int64](https://pkg.go.dev/builtin#int64) `json:"accountId,omitempty"`

 AdTechnologyProviders *[CreativeAdTechnologyProviders](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeAdTechnologyProviders) `json:"adTechnologyProviders,omitempty"` 
	
	AdvertiserId [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"advertiserId,omitempty"`

	
	AdvertiserName [string](https://pkg.go.dev/builtin#string) `json:"advertiserName,omitempty"`

	AgencyId [int64](https://pkg.go.dev/builtin#int64) `json:"agencyId,omitempty,string"`

	
	
	
	ApiUploadTimestamp [string](https://pkg.go.dev/builtin#string) `json:"apiUploadTimestamp,omitempty"`

	
	Attribute [][int64](https://pkg.go.dev/builtin#int64) `json:"attribute,omitempty"`

	
	BuyerCreativeId [string](https://pkg.go.dev/builtin#string) `json:"buyerCreativeId,omitempty"`

	ClickThroughUrl [][string](https://pkg.go.dev/builtin#string) `json:"clickThroughUrl,omitempty"`

	
	Corrections []*[CreativeCorrections](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeCorrections) `json:"corrections,omitempty"`

	
	
	
	
	
	DisapprovalReasons []*[CreativeDisapprovalReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeDisapprovalReasons) `json:"disapprovalReasons,omitempty"`

	
	FilteringReasons *[CreativeFilteringReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasons) `json:"filteringReasons,omitempty"`

	Height [int64](https://pkg.go.dev/builtin#int64) `json:"height,omitempty"`

	
	ImpressionTrackingUrl [][string](https://pkg.go.dev/builtin#string) `json:"impressionTrackingUrl,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	NativeAd *[CreativeNativeAd](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAd) `json:"nativeAd,omitempty"`

	
	ProductCategories [][int64](https://pkg.go.dev/builtin#int64) `json:"productCategories,omitempty"`

	
	RestrictedCategories [][int64](https://pkg.go.dev/builtin#int64) `json:"restrictedCategories,omitempty"`

	
	SensitiveCategories [][int64](https://pkg.go.dev/builtin#int64) `json:"sensitiveCategories,omitempty"`

	
	Status [string](https://pkg.go.dev/builtin#string) `json:"status,omitempty"`

	
	VendorType [][int64](https://pkg.go.dev/builtin#int64) `json:"vendorType,omitempty"`

	
	Version [int64](https://pkg.go.dev/builtin#int64) `json:"version,omitempty"`

	
	VideoURL [string](https://pkg.go.dev/builtin#string) `json:"videoURL,omitempty"`

	Width [int64](https://pkg.go.dev/builtin#int64) `json:"width,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Creative: A creative and its classification data.

type CreativeAdTechnologyProviders struct {
	
	
	
	
	
	
	
	
	
	
	
	
	
	DetectedProviderIds [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"detectedProviderIds,omitempty"`

	
	
	
	
	HasUnidentifiedProvider [bool](https://pkg.go.dev/builtin#bool) `json:"hasUnidentifiedProvider,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CreativeCorrections struct {
	Details [][string](https://pkg.go.dev/builtin#string) `json:"details,omitempty"`

	Reason [string](https://pkg.go.dev/builtin#string) `json:"reason,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CreativeDisapprovalReasons struct {
	Details [][string](https://pkg.go.dev/builtin#string) `json:"details,omitempty"`

	Reason [string](https://pkg.go.dev/builtin#string) `json:"reason,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CreativeFilteringReasons struct {
	
	Date [string](https://pkg.go.dev/builtin#string) `json:"date,omitempty"`

	Reasons []*[CreativeFilteringReasonsReasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeFilteringReasonsReasons) `json:"reasons,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativeFilteringReasons: The filtering reasons for the creative. Read-only. This field should not be set in requests.

type CreativeFilteringReasonsReasons struct {
	
	
	FilteringCount [int64](https://pkg.go.dev/builtin#int64) `json:"filteringCount,omitempty,string"`

	
	FilteringStatus [int64](https://pkg.go.dev/builtin#int64) `json:"filteringStatus,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CreativeNativeAd struct {
 Advertiser [string](https://pkg.go.dev/builtin#string) `json:"advertiser,omitempty"` 
	AppIcon *[CreativeNativeAdAppIcon](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdAppIcon) `json:"appIcon,omitempty"`

	Body [string](https://pkg.go.dev/builtin#string) `json:"body,omitempty"`

	
	CallToAction [string](https://pkg.go.dev/builtin#string) `json:"callToAction,omitempty"`

	ClickTrackingUrl [string](https://pkg.go.dev/builtin#string) `json:"clickTrackingUrl,omitempty"`

	Headline [string](https://pkg.go.dev/builtin#string) `json:"headline,omitempty"`

	Image *[CreativeNativeAdImage](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdImage) `json:"image,omitempty"`

	
	ImpressionTrackingUrl [][string](https://pkg.go.dev/builtin#string) `json:"impressionTrackingUrl,omitempty"`

	Logo *[CreativeNativeAdLogo](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativeNativeAdLogo) `json:"logo,omitempty"`

	Price [string](https://pkg.go.dev/builtin#string) `json:"price,omitempty"`

	
	StarRating [float64](https://pkg.go.dev/builtin#float64) `json:"starRating,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativeNativeAd: If nativeAd is set, HTMLSnippet and videoURL should not be set.

type CreativeNativeAdAppIcon struct {
 Height [int64](https://pkg.go.dev/builtin#int64) `json:"height,omitempty"` 
 Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"` 
 Width [int64](https://pkg.go.dev/builtin#int64) `json:"width,omitempty"` 
	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativeNativeAdAppIcon: The app icon, for app download ads.

type CreativeNativeAdImage struct {
 Height [int64](https://pkg.go.dev/builtin#int64) `json:"height,omitempty"` 
 Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"` 
 Width [int64](https://pkg.go.dev/builtin#int64) `json:"width,omitempty"` 
	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativeNativeAdImage: A large image.

type CreativeNativeAdLogo struct {
 Height [int64](https://pkg.go.dev/builtin#int64) `json:"height,omitempty"` 
 Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"` 
 Width [int64](https://pkg.go.dev/builtin#int64) `json:"width,omitempty"` 
	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativeNativeAdLogo: A smaller image, for the advertiser logo.

type CreativesGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.creatives.get" call. Exactly one of *Creative or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type CreativesInsertCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.creatives.insert" call. Exactly one of *Creative or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type CreativesList struct {
	Items []*[Creative](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Creative) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreativesList: The creatives feed lists the active creatives for the Ad Exchange buyer accounts that the user has access to. Each entry in the feed corresponds to a single creative.

type CreativesListCall struct {
	
}

func (c *[CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)) AccountId(accountId ...[int64](https://pkg.go.dev/builtin#int64)) *[CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)

AccountId sets the optional parameter "accountId": When specified, only creatives for the given account ids are returned.

func (c *[CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)) BuyerCreativeId(buyerCreativeId ...[string](https://pkg.go.dev/builtin#string)) *[CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)

BuyerCreativeId sets the optional parameter "buyerCreativeId": When specified, only creatives for the given buyer creative ids are returned.

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.creatives.list" call. Exactly one of *CreativesList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CreativesList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": Maximum number of entries returned on one result page. If not set, the default is 100.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

StatusFilter sets the optional parameter "statusFilter": When specified, only creatives having the given status are returned.

Possible values:

"approved" - Creatives which have been approved.
"disapproved" - Creatives which have been disapproved.
"not_checked" - Creatives whose status is not yet checked.

type CreativesService struct {
	
}

func NewCreativesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService)

Get: Gets the status for a single creative. A creative will be available 30-40 minutes after submission.

- accountId: The id for the account that will serve this creative. - buyerCreativeId: The buyer-specific id for this creative.

func (r *[CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService)) Insert(creative *[Creative](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Creative)) *[CreativesInsertCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesInsertCall)

Insert: Submit a new creative.

func (r *[CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService)) List() *[CreativesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesListCall)

List: Retrieves a list of the authenticated user's active creatives. A creative will be available 30-40 minutes after submission.

type DirectDeal struct {
	AccountId [int64](https://pkg.go.dev/builtin#int64) `json:"accountId,omitempty"`

	Advertiser [string](https://pkg.go.dev/builtin#string) `json:"advertiser,omitempty"`

	
	AllowsAlcohol [bool](https://pkg.go.dev/builtin#bool) `json:"allowsAlcohol,omitempty"`

	
	
	BuyerAccountId [int64](https://pkg.go.dev/builtin#int64) `json:"buyerAccountId,omitempty,string"`

	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`

	
	DealTier [string](https://pkg.go.dev/builtin#string) `json:"dealTier,omitempty"`

	
	
	EndTime [int64](https://pkg.go.dev/builtin#int64) `json:"endTime,omitempty,string"`

	
	
	
	FixedCpm [int64](https://pkg.go.dev/builtin#int64) `json:"fixedCpm,omitempty,string"`

	Id [int64](https://pkg.go.dev/builtin#int64) `json:"id,omitempty,string"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	
	
	PrivateExchangeMinCpm [int64](https://pkg.go.dev/builtin#int64) `json:"privateExchangeMinCpm,omitempty,string"`

	
	PublisherBlocksOverriden [bool](https://pkg.go.dev/builtin#bool) `json:"publisherBlocksOverriden,omitempty"`

	SellerNetwork [string](https://pkg.go.dev/builtin#string) `json:"sellerNetwork,omitempty"`

	
	
	StartTime [int64](https://pkg.go.dev/builtin#int64) `json:"startTime,omitempty,string"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DirectDeal: The configuration data for an Ad Exchange direct deal.

type DirectDealsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.directDeals.get" call. Exactly one of *DirectDeal or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *DirectDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type DirectDealsList struct {
	DirectDeals []*[DirectDeal](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDeal) `json:"directDeals,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DirectDealsList: A direct deals feed lists Direct Deals the Ad Exchange buyer account has access to. This includes direct deals set up for the buyer account as well as its merged stream seats.

type DirectDealsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.directDeals.list" call. Exactly one of *DirectDealsList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *DirectDealsList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type DirectDealsService struct {
	
}

func NewDirectDealsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[DirectDealsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService)

Get: Gets one direct deal by ID.

- id: The direct deal id.

func (r *[DirectDealsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService)) List() *[DirectDealsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsListCall)

List: Retrieves the authenticated user's list of direct deals.

type PerformanceReport struct {
	BidRate [float64](https://pkg.go.dev/builtin#float64) `json:"bidRate,omitempty"`

	BidRequestRate [float64](https://pkg.go.dev/builtin#float64) `json:"bidRequestRate,omitempty"`

	
	
	CalloutStatusRate []interface{} `json:"calloutStatusRate,omitempty"`

	CookieMatcherStatusRate []interface{} `json:"cookieMatcherStatusRate,omitempty"`

	
	CreativeStatusRate []interface{} `json:"creativeStatusRate,omitempty"`

	
	FilteredBidRate [float64](https://pkg.go.dev/builtin#float64) `json:"filteredBidRate,omitempty"`

	HostedMatchStatusRate []interface{} `json:"hostedMatchStatusRate,omitempty"`

	
	InventoryMatchRate [float64](https://pkg.go.dev/builtin#float64) `json:"inventoryMatchRate,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	Latency50thPercentile [float64](https://pkg.go.dev/builtin#float64) `json:"latency50thPercentile,omitempty"`

	
	
	Latency85thPercentile [float64](https://pkg.go.dev/builtin#float64) `json:"latency85thPercentile,omitempty"`

	
	
	Latency95thPercentile [float64](https://pkg.go.dev/builtin#float64) `json:"latency95thPercentile,omitempty"`

	
	NoQuotaInRegion [float64](https://pkg.go.dev/builtin#float64) `json:"noQuotaInRegion,omitempty"`

	OutOfQuota [float64](https://pkg.go.dev/builtin#float64) `json:"outOfQuota,omitempty"`

	
	PixelMatchRequests [float64](https://pkg.go.dev/builtin#float64) `json:"pixelMatchRequests,omitempty"`

	
	PixelMatchResponses [float64](https://pkg.go.dev/builtin#float64) `json:"pixelMatchResponses,omitempty"`

	QuotaConfiguredLimit [float64](https://pkg.go.dev/builtin#float64) `json:"quotaConfiguredLimit,omitempty"`

	QuotaThrottledLimit [float64](https://pkg.go.dev/builtin#float64) `json:"quotaThrottledLimit,omitempty"`

	Region [string](https://pkg.go.dev/builtin#string) `json:"region,omitempty"`

	
	SuccessfulRequestRate [float64](https://pkg.go.dev/builtin#float64) `json:"successfulRequestRate,omitempty"`

	
	Timestamp [int64](https://pkg.go.dev/builtin#int64) `json:"timestamp,omitempty,string"`

	
	UnsuccessfulRequestRate [float64](https://pkg.go.dev/builtin#float64) `json:"unsuccessfulRequestRate,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PerformanceReport: The configuration data for an Ad Exchange performance report list.

type PerformanceReportList struct {
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	PerformanceReport []*[PerformanceReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReport) `json:"performanceReport,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PerformanceReportList: The configuration data for an Ad Exchange performance report list.

type PerformanceReportListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.performanceReport.list" call. Exactly one of *PerformanceReportList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PerformanceReportList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": Maximum number of entries returned on one result page. If not set, the default is 100.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

type PerformanceReportService struct {
	
}

func NewPerformanceReportService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[PerformanceReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportService)

List: Retrieves the authenticated user's list of performance metrics.

*   accountId: The account id to get the reports.
*   endDateTime: The end time of the report in ISO 8601 timestamp format using UTC.
*   startDateTime: The start time of the report in ISO 8601 timestamp format using UTC.

type PretargetingConfig struct {
	
	
	BillingId [int64](https://pkg.go.dev/builtin#int64) `json:"billingId,omitempty,string"`

	
	ConfigId [int64](https://pkg.go.dev/builtin#int64) `json:"configId,omitempty,string"`

	
	ConfigName [string](https://pkg.go.dev/builtin#string) `json:"configName,omitempty"`

	
	CreativeType [][string](https://pkg.go.dev/builtin#string) `json:"creativeType,omitempty"`

	
	Dimensions []*[PretargetingConfigDimensions](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigDimensions) `json:"dimensions,omitempty"`

	
	
	ExcludedContentLabels [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"excludedContentLabels,omitempty"`

	
	ExcludedGeoCriteriaIds [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"excludedGeoCriteriaIds,omitempty"`

	
	ExcludedPlacements []*[PretargetingConfigExcludedPlacements](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigExcludedPlacements) `json:"excludedPlacements,omitempty"`

	
	ExcludedUserLists [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"excludedUserLists,omitempty"`

	
	
	ExcludedVerticals [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"excludedVerticals,omitempty"`

	
	GeoCriteriaIds [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"geoCriteriaIds,omitempty"`

	IsActive [bool](https://pkg.go.dev/builtin#bool) `json:"isActive,omitempty"`

	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Languages [][string](https://pkg.go.dev/builtin#string) `json:"languages,omitempty"`

	
	
	
	
	MaximumQps [int64](https://pkg.go.dev/builtin#int64) `json:"maximumQps,omitempty,string"`

	
	
	MobileCarriers [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"mobileCarriers,omitempty"`

	
	
	MobileDevices [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"mobileDevices,omitempty"`

	
	
	MobileOperatingSystemVersions [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"mobileOperatingSystemVersions,omitempty"`

	Placements []*[PretargetingConfigPlacements](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigPlacements) `json:"placements,omitempty"`

	
	
	Platforms [][string](https://pkg.go.dev/builtin#string) `json:"platforms,omitempty"`

	
	
	
	
	SupportedCreativeAttributes [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"supportedCreativeAttributes,omitempty"`

	UserLists [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"userLists,omitempty"`

	
	VendorTypes [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"vendorTypes,omitempty"`

	Verticals [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[Int64s](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#Int64s) `json:"verticals,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type PretargetingConfigDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.delete" call.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigDimensions struct {
	Height [int64](https://pkg.go.dev/builtin#int64) `json:"height,omitempty,string"`

	Width [int64](https://pkg.go.dev/builtin#int64) `json:"width,omitempty,string"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type PretargetingConfigExcludedPlacements struct {
	
	
	Token [string](https://pkg.go.dev/builtin#string) `json:"token,omitempty"`

	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type PretargetingConfigGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.get" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PretargetingConfigInsertCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.insert" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.list" call. Exactly one of *PretargetingConfigList or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfigList.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PretargetingConfigPatchCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.patch" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type PretargetingConfigPlacements struct {
	
	
	Token [string](https://pkg.go.dev/builtin#string) `json:"token,omitempty"`

	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type PretargetingConfigService struct {
	
}

func NewPretargetingConfigService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#Service)) *[PretargetingConfigService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService)

Delete: Deletes an existing pretargeting config.

- accountId: The account id to delete the pretargeting config for. - configId: The specific id of the configuration to delete.

Get: Gets a specific pretargeting configuration

- accountId: The account id to get the pretargeting config for. - configId: The specific id of the configuration to retrieve.

Insert: Inserts a new pretargeting configuration.

- accountId: The account id to insert the pretargeting config for.

List: Retrieves a list of the authenticated user's pretargeting configurations.

- accountId: The account id to get the pretargeting configs for.

Patch: Updates an existing pretargeting config. This method supports patch semantics.

- accountId: The account id to update the pretargeting config for. - configId: The specific id of the configuration to update.

Update: Updates an existing pretargeting config.

- accountId: The account id to update the pretargeting config for. - configId: The specific id of the configuration to update.

type PretargetingConfigUpdateCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adexchangebuyer.pretargetingConfig.update" call. Exactly one of *PretargetingConfig or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *PretargetingConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Accounts *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#AccountsService)
 BillingInfo *[BillingInfoService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BillingInfoService)
 Budget *[BudgetService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#BudgetService)
 Creatives *[CreativesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#CreativesService)
 DirectDeals *[DirectDealsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#DirectDealsService)
 PerformanceReport *[PerformanceReportService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PerformanceReportService)
 PretargetingConfig *[PretargetingConfigService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer/v1.3#PretargetingConfigService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.
