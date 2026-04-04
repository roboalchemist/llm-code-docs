# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/authorizedbuyersmarketplace/v1alpha

Title: authorizedbuyersmarketplace package - google.golang.org/api/authorizedbuyersmarketplace/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/authorizedbuyersmarketplace/v1alpha

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
authorizedbuyersmarketplace
 
v1alpha
authorizedbuyersmarketplace
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

Package authorizedbuyersmarketplace provides access to the Authorized Buyers Marketplace API.

For product documentation, see: https://developers.google.com/authorized-buyers/apis/marketplace/reference/rest/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/authorizedbuyersmarketplace/v1alpha"
...
ctx := context.Background()
authorizedbuyersmarketplaceService, err := authorizedbuyersmarketplace.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

authorizedbuyersmarketplaceService, err := authorizedbuyersmarketplace.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
authorizedbuyersmarketplaceService, err := authorizedbuyersmarketplace.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AcceptProposalRequest
func (s AcceptProposalRequest) MarshalJSON() ([]byte, error)
type AccessControlSettings
func (s AccessControlSettings) MarshalJSON() ([]byte, error)
type ActivateClientRequest
type ActivateClientUserRequest
type ActivateCuratedPackageRequest
type ActivateDataSegmentRequest
type AdSize
func (s AdSize) MarshalJSON() ([]byte, error)
type AddCreativeRequest
func (s AddCreativeRequest) MarshalJSON() ([]byte, error)
type AddNoteRequest
func (s AddNoteRequest) MarshalJSON() ([]byte, error)
type AuctionPackage
func (s AuctionPackage) MarshalJSON() ([]byte, error)
type BatchUpdateDealsRequest
func (s BatchUpdateDealsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateDealsResponse
func (s BatchUpdateDealsResponse) MarshalJSON() ([]byte, error)
type BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) Context(ctx context.Context) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) Do(opts ...googleapi.CallOption) (*ListAuctionPackagesResponse, error)
func (c *BiddersAuctionPackagesListCall) Fields(s ...googleapi.Field) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) Filter(filter string) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) Header() http.Header
func (c *BiddersAuctionPackagesListCall) IfNoneMatch(entityTag string) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) OrderBy(orderBy string) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) PageSize(pageSize int64) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) PageToken(pageToken string) *BiddersAuctionPackagesListCall
func (c *BiddersAuctionPackagesListCall) Pages(ctx context.Context, f func(*ListAuctionPackagesResponse) error) error
type BiddersAuctionPackagesService
func NewBiddersAuctionPackagesService(s *Service) *BiddersAuctionPackagesService
func (r *BiddersAuctionPackagesService) List(parent string) *BiddersAuctionPackagesListCall
type BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) Context(ctx context.Context) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) Do(opts ...googleapi.CallOption) (*ListFinalizedDealsResponse, error)
func (c *BiddersFinalizedDealsListCall) Fields(s ...googleapi.Field) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) Filter(filter string) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) Header() http.Header
func (c *BiddersFinalizedDealsListCall) IfNoneMatch(entityTag string) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) OrderBy(orderBy string) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) PageSize(pageSize int64) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) PageToken(pageToken string) *BiddersFinalizedDealsListCall
func (c *BiddersFinalizedDealsListCall) Pages(ctx context.Context, f func(*ListFinalizedDealsResponse) error) error
type BiddersFinalizedDealsService
func NewBiddersFinalizedDealsService(s *Service) *BiddersFinalizedDealsService
func (r *BiddersFinalizedDealsService) List(parent string) *BiddersFinalizedDealsListCall
func (r *BiddersFinalizedDealsService) SetReadyToServe(deal string, setreadytoserverequest *SetReadyToServeRequest) *BiddersFinalizedDealsSetReadyToServeCall
type BiddersFinalizedDealsSetReadyToServeCall
func (c *BiddersFinalizedDealsSetReadyToServeCall) Context(ctx context.Context) *BiddersFinalizedDealsSetReadyToServeCall
func (c *BiddersFinalizedDealsSetReadyToServeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BiddersFinalizedDealsSetReadyToServeCall) Fields(s ...googleapi.Field) *BiddersFinalizedDealsSetReadyToServeCall
func (c *BiddersFinalizedDealsSetReadyToServeCall) Header() http.Header
type BiddersService
func NewBiddersService(s *Service) *BiddersService
type BuyersAuctionPackagesGetCall
func (c *BuyersAuctionPackagesGetCall) Context(ctx context.Context) *BuyersAuctionPackagesGetCall
func (c *BuyersAuctionPackagesGetCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)
func (c *BuyersAuctionPackagesGetCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesGetCall
func (c *BuyersAuctionPackagesGetCall) Header() http.Header
func (c *BuyersAuctionPackagesGetCall) IfNoneMatch(entityTag string) *BuyersAuctionPackagesGetCall
type BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) Context(ctx context.Context) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) Do(opts ...googleapi.CallOption) (*ListAuctionPackagesResponse, error)
func (c *BuyersAuctionPackagesListCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) Filter(filter string) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) Header() http.Header
func (c *BuyersAuctionPackagesListCall) IfNoneMatch(entityTag string) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) OrderBy(orderBy string) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) PageSize(pageSize int64) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) PageToken(pageToken string) *BuyersAuctionPackagesListCall
func (c *BuyersAuctionPackagesListCall) Pages(ctx context.Context, f func(*ListAuctionPackagesResponse) error) error
type BuyersAuctionPackagesService
func NewBuyersAuctionPackagesService(s *Service) *BuyersAuctionPackagesService
func (r *BuyersAuctionPackagesService) Get(name string) *BuyersAuctionPackagesGetCall
func (r *BuyersAuctionPackagesService) List(parent string) *BuyersAuctionPackagesListCall
func (r *BuyersAuctionPackagesService) Subscribe(name string, subscribeauctionpackagerequest *SubscribeAuctionPackageRequest) *BuyersAuctionPackagesSubscribeCall
func (r *BuyersAuctionPackagesService) SubscribeClients(auctionPackage string, subscribeclientsrequest *SubscribeClientsRequest) *BuyersAuctionPackagesSubscribeClientsCall
func (r *BuyersAuctionPackagesService) Unsubscribe(name string, ...) *BuyersAuctionPackagesUnsubscribeCall
func (r *BuyersAuctionPackagesService) UnsubscribeClients(auctionPackage string, unsubscribeclientsrequest *UnsubscribeClientsRequest) *BuyersAuctionPackagesUnsubscribeClientsCall
type BuyersAuctionPackagesSubscribeCall
func (c *BuyersAuctionPackagesSubscribeCall) Context(ctx context.Context) *BuyersAuctionPackagesSubscribeCall
func (c *BuyersAuctionPackagesSubscribeCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)
func (c *BuyersAuctionPackagesSubscribeCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesSubscribeCall
func (c *BuyersAuctionPackagesSubscribeCall) Header() http.Header
type BuyersAuctionPackagesSubscribeClientsCall
func (c *BuyersAuctionPackagesSubscribeClientsCall) Context(ctx context.Context) *BuyersAuctionPackagesSubscribeClientsCall
func (c *BuyersAuctionPackagesSubscribeClientsCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)
func (c *BuyersAuctionPackagesSubscribeClientsCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesSubscribeClientsCall
func (c *BuyersAuctionPackagesSubscribeClientsCall) Header() http.Header
type BuyersAuctionPackagesUnsubscribeCall
func (c *BuyersAuctionPackagesUnsubscribeCall) Context(ctx context.Context) *BuyersAuctionPackagesUnsubscribeCall
func (c *BuyersAuctionPackagesUnsubscribeCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)
func (c *BuyersAuctionPackagesUnsubscribeCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesUnsubscribeCall
func (c *BuyersAuctionPackagesUnsubscribeCall) Header() http.Header
type BuyersAuctionPackagesUnsubscribeClientsCall
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Context(ctx context.Context) *BuyersAuctionPackagesUnsubscribeClientsCall
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesUnsubscribeClientsCall
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Header() http.Header
type BuyersClientsActivateCall
func (c *BuyersClientsActivateCall) Context(ctx context.Context) *BuyersClientsActivateCall
func (c *BuyersClientsActivateCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *BuyersClientsActivateCall) Fields(s ...googleapi.Field) *BuyersClientsActivateCall
func (c *BuyersClientsActivateCall) Header() http.Header
type BuyersClientsCreateCall
func (c *BuyersClientsCreateCall) Context(ctx context.Context) *BuyersClientsCreateCall
func (c *BuyersClientsCreateCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *BuyersClientsCreateCall) Fields(s ...googleapi.Field) *BuyersClientsCreateCall
func (c *BuyersClientsCreateCall) Header() http.Header
type BuyersClientsDeactivateCall
func (c *BuyersClientsDeactivateCall) Context(ctx context.Context) *BuyersClientsDeactivateCall
func (c *BuyersClientsDeactivateCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *BuyersClientsDeactivateCall) Fields(s ...googleapi.Field) *BuyersClientsDeactivateCall
func (c *BuyersClientsDeactivateCall) Header() http.Header
type BuyersClientsGetCall
func (c *BuyersClientsGetCall) Context(ctx context.Context) *BuyersClientsGetCall
func (c *BuyersClientsGetCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *BuyersClientsGetCall) Fields(s ...googleapi.Field) *BuyersClientsGetCall
func (c *BuyersClientsGetCall) Header() http.Header
func (c *BuyersClientsGetCall) IfNoneMatch(entityTag string) *BuyersClientsGetCall
type BuyersClientsListCall
func (c *BuyersClientsListCall) Context(ctx context.Context) *BuyersClientsListCall
func (c *BuyersClientsListCall) Do(opts ...googleapi.CallOption) (*ListClientsResponse, error)
func (c *BuyersClientsListCall) Fields(s ...googleapi.Field) *BuyersClientsListCall
func (c *BuyersClientsListCall) Filter(filter string) *BuyersClientsListCall
func (c *BuyersClientsListCall) Header() http.Header
func (c *BuyersClientsListCall) IfNoneMatch(entityTag string) *BuyersClientsListCall
func (c *BuyersClientsListCall) PageSize(pageSize int64) *BuyersClientsListCall
func (c *BuyersClientsListCall) PageToken(pageToken string) *BuyersClientsListCall
func (c *BuyersClientsListCall) Pages(ctx context.Context, f func(*ListClientsResponse) error) error
type BuyersClientsPatchCall
func (c *BuyersClientsPatchCall) Context(ctx context.Context) *BuyersClientsPatchCall
func (c *BuyersClientsPatchCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *BuyersClientsPatchCall) Fields(s ...googleapi.Field) *BuyersClientsPatchCall
func (c *BuyersClientsPatchCall) Header() http.Header
func (c *BuyersClientsPatchCall) UpdateMask(updateMask string) *BuyersClientsPatchCall
type BuyersClientsService
func NewBuyersClientsService(s *Service) *BuyersClientsService
func (r *BuyersClientsService) Activate(name string, activateclientrequest *ActivateClientRequest) *BuyersClientsActivateCall
func (r *BuyersClientsService) Create(parent string, client *Client) *BuyersClientsCreateCall
func (r *BuyersClientsService) Deactivate(name string, deactivateclientrequest *DeactivateClientRequest) *BuyersClientsDeactivateCall
func (r *BuyersClientsService) Get(name string) *BuyersClientsGetCall
func (r *BuyersClientsService) List(parent string) *BuyersClientsListCall
func (r *BuyersClientsService) Patch(name string, client *Client) *BuyersClientsPatchCall
type BuyersClientsUsersActivateCall
func (c *BuyersClientsUsersActivateCall) Context(ctx context.Context) *BuyersClientsUsersActivateCall
func (c *BuyersClientsUsersActivateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *BuyersClientsUsersActivateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersActivateCall
func (c *BuyersClientsUsersActivateCall) Header() http.Header
type BuyersClientsUsersCreateCall
func (c *BuyersClientsUsersCreateCall) Context(ctx context.Context) *BuyersClientsUsersCreateCall
func (c *BuyersClientsUsersCreateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *BuyersClientsUsersCreateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersCreateCall
func (c *BuyersClientsUsersCreateCall) Header() http.Header
type BuyersClientsUsersDeactivateCall
func (c *BuyersClientsUsersDeactivateCall) Context(ctx context.Context) *BuyersClientsUsersDeactivateCall
func (c *BuyersClientsUsersDeactivateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *BuyersClientsUsersDeactivateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersDeactivateCall
func (c *BuyersClientsUsersDeactivateCall) Header() http.Header
type BuyersClientsUsersDeleteCall
func (c *BuyersClientsUsersDeleteCall) Context(ctx context.Context) *BuyersClientsUsersDeleteCall
func (c *BuyersClientsUsersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *BuyersClientsUsersDeleteCall) Fields(s ...googleapi.Field) *BuyersClientsUsersDeleteCall
func (c *BuyersClientsUsersDeleteCall) Header() http.Header
type BuyersClientsUsersGetCall
func (c *BuyersClientsUsersGetCall) Context(ctx context.Context) *BuyersClientsUsersGetCall
func (c *BuyersClientsUsersGetCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *BuyersClientsUsersGetCall) Fields(s ...googleapi.Field) *BuyersClientsUsersGetCall
func (c *BuyersClientsUsersGetCall) Header() http.Header
func (c *BuyersClientsUsersGetCall) IfNoneMatch(entityTag string) *BuyersClientsUsersGetCall
type BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) Context(ctx context.Context) *BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) Do(opts ...googleapi.CallOption) (*ListClientUsersResponse, error)
func (c *BuyersClientsUsersListCall) Fields(s ...googleapi.Field) *BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) Header() http.Header
func (c *BuyersClientsUsersListCall) IfNoneMatch(entityTag string) *BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) PageSize(pageSize int64) *BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) PageToken(pageToken string) *BuyersClientsUsersListCall
func (c *BuyersClientsUsersListCall) Pages(ctx context.Context, f func(*ListClientUsersResponse) error) error
type BuyersClientsUsersService
func NewBuyersClientsUsersService(s *Service) *BuyersClientsUsersService
func (r *BuyersClientsUsersService) Activate(name string, activateclientuserrequest *ActivateClientUserRequest) *BuyersClientsUsersActivateCall
func (r *BuyersClientsUsersService) Create(parent string, clientuser *ClientUser) *BuyersClientsUsersCreateCall
func (r *BuyersClientsUsersService) Deactivate(name string, deactivateclientuserrequest *DeactivateClientUserRequest) *BuyersClientsUsersDeactivateCall
func (r *BuyersClientsUsersService) Delete(name string) *BuyersClientsUsersDeleteCall
func (r *BuyersClientsUsersService) Get(name string) *BuyersClientsUsersGetCall
func (r *BuyersClientsUsersService) List(parent string) *BuyersClientsUsersListCall
type BuyersDataSegmentsActivateCall
func (c *BuyersDataSegmentsActivateCall) Context(ctx context.Context) *BuyersDataSegmentsActivateCall
func (c *BuyersDataSegmentsActivateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)
func (c *BuyersDataSegmentsActivateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsActivateCall
func (c *BuyersDataSegmentsActivateCall) Header() http.Header
type BuyersDataSegmentsCreateCall
func (c *BuyersDataSegmentsCreateCall) Context(ctx context.Context) *BuyersDataSegmentsCreateCall
func (c *BuyersDataSegmentsCreateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)
func (c *BuyersDataSegmentsCreateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsCreateCall
func (c *BuyersDataSegmentsCreateCall) Header() http.Header
type BuyersDataSegmentsDeactivateCall
func (c *BuyersDataSegmentsDeactivateCall) Context(ctx context.Context) *BuyersDataSegmentsDeactivateCall
func (c *BuyersDataSegmentsDeactivateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)
func (c *BuyersDataSegmentsDeactivateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsDeactivateCall
func (c *BuyersDataSegmentsDeactivateCall) Header() http.Header
type BuyersDataSegmentsGetCall
func (c *BuyersDataSegmentsGetCall) Context(ctx context.Context) *BuyersDataSegmentsGetCall
func (c *BuyersDataSegmentsGetCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)
func (c *BuyersDataSegmentsGetCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsGetCall
func (c *BuyersDataSegmentsGetCall) Header() http.Header
func (c *BuyersDataSegmentsGetCall) IfNoneMatch(entityTag string) *BuyersDataSegmentsGetCall
type BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) Context(ctx context.Context) *BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) Do(opts ...googleapi.CallOption) (*ListDataSegmentsResponse, error)
func (c *BuyersDataSegmentsListCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) Header() http.Header
func (c *BuyersDataSegmentsListCall) IfNoneMatch(entityTag string) *BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) PageSize(pageSize int64) *BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) PageToken(pageToken string) *BuyersDataSegmentsListCall
func (c *BuyersDataSegmentsListCall) Pages(ctx context.Context, f func(*ListDataSegmentsResponse) error) error
type BuyersDataSegmentsPatchCall
func (c *BuyersDataSegmentsPatchCall) Context(ctx context.Context) *BuyersDataSegmentsPatchCall
func (c *BuyersDataSegmentsPatchCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)
func (c *BuyersDataSegmentsPatchCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsPatchCall
func (c *BuyersDataSegmentsPatchCall) Header() http.Header
func (c *BuyersDataSegmentsPatchCall) UpdateMask(updateMask string) *BuyersDataSegmentsPatchCall
type BuyersDataSegmentsService
func NewBuyersDataSegmentsService(s *Service) *BuyersDataSegmentsService
func (r *BuyersDataSegmentsService) Activate(name string, activatedatasegmentrequest *ActivateDataSegmentRequest) *BuyersDataSegmentsActivateCall
func (r *BuyersDataSegmentsService) Create(parent string, datasegment *DataSegment) *BuyersDataSegmentsCreateCall
func (r *BuyersDataSegmentsService) Deactivate(name string, deactivatedatasegmentrequest *DeactivateDataSegmentRequest) *BuyersDataSegmentsDeactivateCall
func (r *BuyersDataSegmentsService) Get(name string) *BuyersDataSegmentsGetCall
func (r *BuyersDataSegmentsService) List(parent string) *BuyersDataSegmentsListCall
func (r *BuyersDataSegmentsService) Patch(nameid string, datasegment *DataSegment) *BuyersDataSegmentsPatchCall
type BuyersFinalizedDealsAddCreativeCall
func (c *BuyersFinalizedDealsAddCreativeCall) Context(ctx context.Context) *BuyersFinalizedDealsAddCreativeCall
func (c *BuyersFinalizedDealsAddCreativeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BuyersFinalizedDealsAddCreativeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsAddCreativeCall
func (c *BuyersFinalizedDealsAddCreativeCall) Header() http.Header
type BuyersFinalizedDealsGetCall
func (c *BuyersFinalizedDealsGetCall) Context(ctx context.Context) *BuyersFinalizedDealsGetCall
func (c *BuyersFinalizedDealsGetCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BuyersFinalizedDealsGetCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsGetCall
func (c *BuyersFinalizedDealsGetCall) Header() http.Header
func (c *BuyersFinalizedDealsGetCall) IfNoneMatch(entityTag string) *BuyersFinalizedDealsGetCall
type BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) Context(ctx context.Context) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) Do(opts ...googleapi.CallOption) (*ListFinalizedDealsResponse, error)
func (c *BuyersFinalizedDealsListCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) Filter(filter string) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) Header() http.Header
func (c *BuyersFinalizedDealsListCall) IfNoneMatch(entityTag string) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) OrderBy(orderBy string) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) PageSize(pageSize int64) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) PageToken(pageToken string) *BuyersFinalizedDealsListCall
func (c *BuyersFinalizedDealsListCall) Pages(ctx context.Context, f func(*ListFinalizedDealsResponse) error) error
type BuyersFinalizedDealsPauseCall
func (c *BuyersFinalizedDealsPauseCall) Context(ctx context.Context) *BuyersFinalizedDealsPauseCall
func (c *BuyersFinalizedDealsPauseCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BuyersFinalizedDealsPauseCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsPauseCall
func (c *BuyersFinalizedDealsPauseCall) Header() http.Header
type BuyersFinalizedDealsResumeCall
func (c *BuyersFinalizedDealsResumeCall) Context(ctx context.Context) *BuyersFinalizedDealsResumeCall
func (c *BuyersFinalizedDealsResumeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BuyersFinalizedDealsResumeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsResumeCall
func (c *BuyersFinalizedDealsResumeCall) Header() http.Header
type BuyersFinalizedDealsService
func NewBuyersFinalizedDealsService(s *Service) *BuyersFinalizedDealsService
func (r *BuyersFinalizedDealsService) AddCreative(deal string, addcreativerequest *AddCreativeRequest) *BuyersFinalizedDealsAddCreativeCall
func (r *BuyersFinalizedDealsService) Get(name string) *BuyersFinalizedDealsGetCall
func (r *BuyersFinalizedDealsService) List(parent string) *BuyersFinalizedDealsListCall
func (r *BuyersFinalizedDealsService) Pause(name string, pausefinalizeddealrequest *PauseFinalizedDealRequest) *BuyersFinalizedDealsPauseCall
func (r *BuyersFinalizedDealsService) Resume(name string, resumefinalizeddealrequest *ResumeFinalizedDealRequest) *BuyersFinalizedDealsResumeCall
func (r *BuyersFinalizedDealsService) SetReadyToServe(deal string, setreadytoserverequest *SetReadyToServeRequest) *BuyersFinalizedDealsSetReadyToServeCall
type BuyersFinalizedDealsSetReadyToServeCall
func (c *BuyersFinalizedDealsSetReadyToServeCall) Context(ctx context.Context) *BuyersFinalizedDealsSetReadyToServeCall
func (c *BuyersFinalizedDealsSetReadyToServeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)
func (c *BuyersFinalizedDealsSetReadyToServeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsSetReadyToServeCall
func (c *BuyersFinalizedDealsSetReadyToServeCall) Header() http.Header
type BuyersProposalsAcceptCall
func (c *BuyersProposalsAcceptCall) Context(ctx context.Context) *BuyersProposalsAcceptCall
func (c *BuyersProposalsAcceptCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsAcceptCall) Fields(s ...googleapi.Field) *BuyersProposalsAcceptCall
func (c *BuyersProposalsAcceptCall) Header() http.Header
type BuyersProposalsAddNoteCall
func (c *BuyersProposalsAddNoteCall) Context(ctx context.Context) *BuyersProposalsAddNoteCall
func (c *BuyersProposalsAddNoteCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsAddNoteCall) Fields(s ...googleapi.Field) *BuyersProposalsAddNoteCall
func (c *BuyersProposalsAddNoteCall) Header() http.Header
type BuyersProposalsCancelNegotiationCall
func (c *BuyersProposalsCancelNegotiationCall) Context(ctx context.Context) *BuyersProposalsCancelNegotiationCall
func (c *BuyersProposalsCancelNegotiationCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsCancelNegotiationCall) Fields(s ...googleapi.Field) *BuyersProposalsCancelNegotiationCall
func (c *BuyersProposalsCancelNegotiationCall) Header() http.Header
type BuyersProposalsDealsBatchUpdateCall
func (c *BuyersProposalsDealsBatchUpdateCall) Context(ctx context.Context) *BuyersProposalsDealsBatchUpdateCall
func (c *BuyersProposalsDealsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateDealsResponse, error)
func (c *BuyersProposalsDealsBatchUpdateCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsBatchUpdateCall
func (c *BuyersProposalsDealsBatchUpdateCall) Header() http.Header
type BuyersProposalsDealsGetCall
func (c *BuyersProposalsDealsGetCall) Context(ctx context.Context) *BuyersProposalsDealsGetCall
func (c *BuyersProposalsDealsGetCall) Do(opts ...googleapi.CallOption) (*Deal, error)
func (c *BuyersProposalsDealsGetCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsGetCall
func (c *BuyersProposalsDealsGetCall) Header() http.Header
func (c *BuyersProposalsDealsGetCall) IfNoneMatch(entityTag string) *BuyersProposalsDealsGetCall
type BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) Context(ctx context.Context) *BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) Do(opts ...googleapi.CallOption) (*ListDealsResponse, error)
func (c *BuyersProposalsDealsListCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) Header() http.Header
func (c *BuyersProposalsDealsListCall) IfNoneMatch(entityTag string) *BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) PageSize(pageSize int64) *BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) PageToken(pageToken string) *BuyersProposalsDealsListCall
func (c *BuyersProposalsDealsListCall) Pages(ctx context.Context, f func(*ListDealsResponse) error) error
type BuyersProposalsDealsPatchCall
func (c *BuyersProposalsDealsPatchCall) Context(ctx context.Context) *BuyersProposalsDealsPatchCall
func (c *BuyersProposalsDealsPatchCall) Do(opts ...googleapi.CallOption) (*Deal, error)
func (c *BuyersProposalsDealsPatchCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsPatchCall
func (c *BuyersProposalsDealsPatchCall) Header() http.Header
func (c *BuyersProposalsDealsPatchCall) UpdateMask(updateMask string) *BuyersProposalsDealsPatchCall
type BuyersProposalsDealsService
func NewBuyersProposalsDealsService(s *Service) *BuyersProposalsDealsService
func (r *BuyersProposalsDealsService) BatchUpdate(parent string, batchupdatedealsrequest *BatchUpdateDealsRequest) *BuyersProposalsDealsBatchUpdateCall
func (r *BuyersProposalsDealsService) Get(name string) *BuyersProposalsDealsGetCall
func (r *BuyersProposalsDealsService) List(parent string) *BuyersProposalsDealsListCall
func (r *BuyersProposalsDealsService) Patch(nameid string, deal *Deal) *BuyersProposalsDealsPatchCall
type BuyersProposalsGetCall
func (c *BuyersProposalsGetCall) Context(ctx context.Context) *BuyersProposalsGetCall
func (c *BuyersProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsGetCall) Fields(s ...googleapi.Field) *BuyersProposalsGetCall
func (c *BuyersProposalsGetCall) Header() http.Header
func (c *BuyersProposalsGetCall) IfNoneMatch(entityTag string) *BuyersProposalsGetCall
type BuyersProposalsListCall
func (c *BuyersProposalsListCall) Context(ctx context.Context) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)
func (c *BuyersProposalsListCall) Fields(s ...googleapi.Field) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) Filter(filter string) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) Header() http.Header
func (c *BuyersProposalsListCall) IfNoneMatch(entityTag string) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) PageSize(pageSize int64) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) PageToken(pageToken string) *BuyersProposalsListCall
func (c *BuyersProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error
type BuyersProposalsPatchCall
func (c *BuyersProposalsPatchCall) Context(ctx context.Context) *BuyersProposalsPatchCall
func (c *BuyersProposalsPatchCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsPatchCall) Fields(s ...googleapi.Field) *BuyersProposalsPatchCall
func (c *BuyersProposalsPatchCall) Header() http.Header
func (c *BuyersProposalsPatchCall) UpdateMask(updateMask string) *BuyersProposalsPatchCall
type BuyersProposalsSendRfpCall
func (c *BuyersProposalsSendRfpCall) Context(ctx context.Context) *BuyersProposalsSendRfpCall
func (c *BuyersProposalsSendRfpCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *BuyersProposalsSendRfpCall) Fields(s ...googleapi.Field) *BuyersProposalsSendRfpCall
func (c *BuyersProposalsSendRfpCall) Header() http.Header
type BuyersProposalsService
func NewBuyersProposalsService(s *Service) *BuyersProposalsService
func (r *BuyersProposalsService) Accept(name string, acceptproposalrequest *AcceptProposalRequest) *BuyersProposalsAcceptCall
func (r *BuyersProposalsService) AddNote(proposal string, addnoterequest *AddNoteRequest) *BuyersProposalsAddNoteCall
func (r *BuyersProposalsService) CancelNegotiation(proposal string, cancelnegotiationrequest *CancelNegotiationRequest) *BuyersProposalsCancelNegotiationCall
func (r *BuyersProposalsService) Get(name string) *BuyersProposalsGetCall
func (r *BuyersProposalsService) List(parent string) *BuyersProposalsListCall
func (r *BuyersProposalsService) Patch(nameid string, proposal *Proposal) *BuyersProposalsPatchCall
func (r *BuyersProposalsService) SendRfp(buyer string, sendrfprequest *SendRfpRequest) *BuyersProposalsSendRfpCall
type BuyersPublisherProfilesGetCall
func (c *BuyersPublisherProfilesGetCall) Context(ctx context.Context) *BuyersPublisherProfilesGetCall
func (c *BuyersPublisherProfilesGetCall) Do(opts ...googleapi.CallOption) (*PublisherProfile, error)
func (c *BuyersPublisherProfilesGetCall) Fields(s ...googleapi.Field) *BuyersPublisherProfilesGetCall
func (c *BuyersPublisherProfilesGetCall) Header() http.Header
func (c *BuyersPublisherProfilesGetCall) IfNoneMatch(entityTag string) *BuyersPublisherProfilesGetCall
type BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) Context(ctx context.Context) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) Do(opts ...googleapi.CallOption) (*ListPublisherProfilesResponse, error)
func (c *BuyersPublisherProfilesListCall) Fields(s ...googleapi.Field) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) Filter(filter string) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) Header() http.Header
func (c *BuyersPublisherProfilesListCall) IfNoneMatch(entityTag string) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) PageSize(pageSize int64) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) PageToken(pageToken string) *BuyersPublisherProfilesListCall
func (c *BuyersPublisherProfilesListCall) Pages(ctx context.Context, f func(*ListPublisherProfilesResponse) error) error
type BuyersPublisherProfilesService
func NewBuyersPublisherProfilesService(s *Service) *BuyersPublisherProfilesService
func (r *BuyersPublisherProfilesService) Get(name string) *BuyersPublisherProfilesGetCall
func (r *BuyersPublisherProfilesService) List(parent string) *BuyersPublisherProfilesListCall
type BuyersService
func NewBuyersService(s *Service) *BuyersService
type CancelNegotiationRequest
type Client
func (s Client) MarshalJSON() ([]byte, error)
type ClientUser
func (s ClientUser) MarshalJSON() ([]byte, error)
type Contact
func (s Contact) MarshalJSON() ([]byte, error)
type CreativeRequirements
func (s CreativeRequirements) MarshalJSON() ([]byte, error)
type CriteriaTargeting
func (s CriteriaTargeting) MarshalJSON() ([]byte, error)
type CuratedPackage
func (s CuratedPackage) MarshalJSON() ([]byte, error)
type CuratorsCuratedPackagesActivateCall
func (c *CuratorsCuratedPackagesActivateCall) Context(ctx context.Context) *CuratorsCuratedPackagesActivateCall
func (c *CuratorsCuratedPackagesActivateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)
func (c *CuratorsCuratedPackagesActivateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesActivateCall
func (c *CuratorsCuratedPackagesActivateCall) Header() http.Header
type CuratorsCuratedPackagesCreateCall
func (c *CuratorsCuratedPackagesCreateCall) Context(ctx context.Context) *CuratorsCuratedPackagesCreateCall
func (c *CuratorsCuratedPackagesCreateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)
func (c *CuratorsCuratedPackagesCreateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesCreateCall
func (c *CuratorsCuratedPackagesCreateCall) Header() http.Header
type CuratorsCuratedPackagesDeactivateCall
func (c *CuratorsCuratedPackagesDeactivateCall) Context(ctx context.Context) *CuratorsCuratedPackagesDeactivateCall
func (c *CuratorsCuratedPackagesDeactivateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)
func (c *CuratorsCuratedPackagesDeactivateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesDeactivateCall
func (c *CuratorsCuratedPackagesDeactivateCall) Header() http.Header
type CuratorsCuratedPackagesGetCall
func (c *CuratorsCuratedPackagesGetCall) Context(ctx context.Context) *CuratorsCuratedPackagesGetCall
func (c *CuratorsCuratedPackagesGetCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)
func (c *CuratorsCuratedPackagesGetCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesGetCall
func (c *CuratorsCuratedPackagesGetCall) Header() http.Header
func (c *CuratorsCuratedPackagesGetCall) IfNoneMatch(entityTag string) *CuratorsCuratedPackagesGetCall
type CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) Context(ctx context.Context) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) Do(opts ...googleapi.CallOption) (*ListCuratedPackagesResponse, error)
func (c *CuratorsCuratedPackagesListCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) Filter(filter string) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) Header() http.Header
func (c *CuratorsCuratedPackagesListCall) IfNoneMatch(entityTag string) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) PageSize(pageSize int64) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) PageToken(pageToken string) *CuratorsCuratedPackagesListCall
func (c *CuratorsCuratedPackagesListCall) Pages(ctx context.Context, f func(*ListCuratedPackagesResponse) error) error
type CuratorsCuratedPackagesPatchCall
func (c *CuratorsCuratedPackagesPatchCall) Context(ctx context.Context) *CuratorsCuratedPackagesPatchCall
func (c *CuratorsCuratedPackagesPatchCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)
func (c *CuratorsCuratedPackagesPatchCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesPatchCall
func (c *CuratorsCuratedPackagesPatchCall) Header() http.Header
func (c *CuratorsCuratedPackagesPatchCall) UpdateMask(updateMask string) *CuratorsCuratedPackagesPatchCall
type CuratorsCuratedPackagesService
func NewCuratorsCuratedPackagesService(s *Service) *CuratorsCuratedPackagesService
func (r *CuratorsCuratedPackagesService) Activate(name string, activatecuratedpackagerequest *ActivateCuratedPackageRequest) *CuratorsCuratedPackagesActivateCall
func (r *CuratorsCuratedPackagesService) Create(parent string, curatedpackage *CuratedPackage) *CuratorsCuratedPackagesCreateCall
func (r *CuratorsCuratedPackagesService) Deactivate(name string, deactivatecuratedpackagerequest *DeactivateCuratedPackageRequest) *CuratorsCuratedPackagesDeactivateCall
func (r *CuratorsCuratedPackagesService) Get(name string) *CuratorsCuratedPackagesGetCall
func (r *CuratorsCuratedPackagesService) List(parent string) *CuratorsCuratedPackagesListCall
func (r *CuratorsCuratedPackagesService) Patch(name string, curatedpackage *CuratedPackage) *CuratorsCuratedPackagesPatchCall
type CuratorsService
func NewCuratorsService(s *Service) *CuratorsService
type DataSegment
func (s DataSegment) MarshalJSON() ([]byte, error)
type DayPart
func (s DayPart) MarshalJSON() ([]byte, error)
type DayPartTargeting
func (s DayPartTargeting) MarshalJSON() ([]byte, error)
type DeactivateClientRequest
type DeactivateClientUserRequest
type DeactivateCuratedPackageRequest
type DeactivateDataSegmentRequest
type Deal
func (s Deal) MarshalJSON() ([]byte, error)
type DealPausingInfo
func (s DealPausingInfo) MarshalJSON() ([]byte, error)
type DeliveryControl
func (s DeliveryControl) MarshalJSON() ([]byte, error)
type Empty
type FinalizedDeal
func (s FinalizedDeal) MarshalJSON() ([]byte, error)
type FirstPartyMobileApplicationTargeting
func (s FirstPartyMobileApplicationTargeting) MarshalJSON() ([]byte, error)
type FrequencyCap
func (s FrequencyCap) MarshalJSON() ([]byte, error)
type InventorySizeTargeting
func (s InventorySizeTargeting) MarshalJSON() ([]byte, error)
type InventoryTypeTargeting
func (s InventoryTypeTargeting) MarshalJSON() ([]byte, error)
type ListAuctionPackagesResponse
func (s ListAuctionPackagesResponse) MarshalJSON() ([]byte, error)
type ListClientUsersResponse
func (s ListClientUsersResponse) MarshalJSON() ([]byte, error)
type ListClientsResponse
func (s ListClientsResponse) MarshalJSON() ([]byte, error)
type ListCuratedPackagesResponse
func (s ListCuratedPackagesResponse) MarshalJSON() ([]byte, error)
type ListDataSegmentsResponse
func (s ListDataSegmentsResponse) MarshalJSON() ([]byte, error)
type ListDealsResponse
func (s ListDealsResponse) MarshalJSON() ([]byte, error)
type ListFinalizedDealsResponse
func (s ListFinalizedDealsResponse) MarshalJSON() ([]byte, error)
type ListMediaPlannersResponse
func (s ListMediaPlannersResponse) MarshalJSON() ([]byte, error)
type ListProposalsResponse
func (s ListProposalsResponse) MarshalJSON() ([]byte, error)
type ListPublisherProfilesResponse
func (s ListPublisherProfilesResponse) MarshalJSON() ([]byte, error)
type MarketplaceTargeting
func (s MarketplaceTargeting) MarshalJSON() ([]byte, error)
type MediaPlanner
func (s MediaPlanner) MarshalJSON() ([]byte, error)
type MediaPlannersListCall
func (c *MediaPlannersListCall) Context(ctx context.Context) *MediaPlannersListCall
func (c *MediaPlannersListCall) Do(opts ...googleapi.CallOption) (*ListMediaPlannersResponse, error)
func (c *MediaPlannersListCall) Fields(s ...googleapi.Field) *MediaPlannersListCall
func (c *MediaPlannersListCall) Filter(filter string) *MediaPlannersListCall
func (c *MediaPlannersListCall) Header() http.Header
func (c *MediaPlannersListCall) IfNoneMatch(entityTag string) *MediaPlannersListCall
func (c *MediaPlannersListCall) PageSize(pageSize int64) *MediaPlannersListCall
func (c *MediaPlannersListCall) PageToken(pageToken string) *MediaPlannersListCall
func (c *MediaPlannersListCall) Pages(ctx context.Context, f func(*ListMediaPlannersResponse) error) error
type MediaPlannersService
func NewMediaPlannersService(s *Service) *MediaPlannersService
func (r *MediaPlannersService) List() *MediaPlannersListCall
type MobileApplicationTargeting
func (s MobileApplicationTargeting) MarshalJSON() ([]byte, error)
type Money
func (s Money) MarshalJSON() ([]byte, error)
type Note
func (s Note) MarshalJSON() ([]byte, error)
type OperatingSystemTargeting
func (s OperatingSystemTargeting) MarshalJSON() ([]byte, error)
type PackagePlacementTargeting
func (s PackagePlacementTargeting) MarshalJSON() ([]byte, error)
type PackagePublisherProvidedSignalsTargeting
func (s PackagePublisherProvidedSignalsTargeting) MarshalJSON() ([]byte, error)
type PackageTargeting
func (s PackageTargeting) MarshalJSON() ([]byte, error)
type PackageVideoTargeting
func (s PackageVideoTargeting) MarshalJSON() ([]byte, error)
type PauseFinalizedDealRequest
func (s PauseFinalizedDealRequest) MarshalJSON() ([]byte, error)
type PlacementTargeting
func (s PlacementTargeting) MarshalJSON() ([]byte, error)
type PreferredDealTerms
func (s PreferredDealTerms) MarshalJSON() ([]byte, error)
type Price
func (s Price) MarshalJSON() ([]byte, error)
type PrivateAuctionTerms
func (s PrivateAuctionTerms) MarshalJSON() ([]byte, error)
type PrivateData
func (s PrivateData) MarshalJSON() ([]byte, error)
type ProgrammaticGuaranteedTerms
func (s ProgrammaticGuaranteedTerms) MarshalJSON() ([]byte, error)
type Proposal
func (s Proposal) MarshalJSON() ([]byte, error)
type PublisherProfile
func (s PublisherProfile) MarshalJSON() ([]byte, error)
type PublisherProfileMobileApplication
func (s PublisherProfileMobileApplication) MarshalJSON() ([]byte, error)
type ResumeFinalizedDealRequest
type RtbMetrics
func (s RtbMetrics) MarshalJSON() ([]byte, error)
func (s *RtbMetrics) UnmarshalJSON(data []byte) error
type SendRfpRequest
func (s SendRfpRequest) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type SetReadyToServeRequest
type StringTargetingDimension
func (s StringTargetingDimension) MarshalJSON() ([]byte, error)
type SubscribeAuctionPackageRequest
type SubscribeClientsRequest
func (s SubscribeClientsRequest) MarshalJSON() ([]byte, error)
type TaxonomyTargeting
func (s TaxonomyTargeting) MarshalJSON() ([]byte, error)
type TechnologyTargeting
func (s TechnologyTargeting) MarshalJSON() ([]byte, error)
type TimeOfDay
func (s TimeOfDay) MarshalJSON() ([]byte, error)
type TimeZone
func (s TimeZone) MarshalJSON() ([]byte, error)
type UnsubscribeAuctionPackageRequest
type UnsubscribeClientsRequest
func (s UnsubscribeClientsRequest) MarshalJSON() ([]byte, error)
type UpdateDealRequest
func (s UpdateDealRequest) MarshalJSON() ([]byte, error)
type UriTargeting
func (s UriTargeting) MarshalJSON() ([]byte, error)
type VideoPlayerSizeTargeting
func (s VideoPlayerSizeTargeting) MarshalJSON() ([]byte, error)
type VideoPlcmtTargeting
func (s VideoPlcmtTargeting) MarshalJSON() ([]byte, error)
type VideoTargeting
func (s VideoTargeting) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// See, create, edit, and delete your Authorized Buyers Marketplace entities.
	AuthorizedBuyersMarketplaceScope = "https://www.googleapis.com/auth/authorized-buyers-marketplace"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type AcceptProposalRequest ¶
type AcceptProposalRequest struct {
	// ProposalRevision: The last known client revision number of the proposal.
	ProposalRevision int64 `json:"proposalRevision,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "ProposalRevision") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ProposalRevision") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AcceptProposalRequest: Request to accept a proposal. Accepting a proposal implies acceptance of the publisher terms_and_conditions, if any.

func (AcceptProposalRequest) MarshalJSON ¶
func (s AcceptProposalRequest) MarshalJSON() ([]byte, error)
type AccessControlSettings ¶
added in v0.259.0
type AccessControlSettings struct {
	// AllowlistedMediaPlanners: Required. Immutable. The list of media planners
	// that are explicitly granted access to the curated package. Eligible media
	// planners can be found in the mediaPlanners.list method. Only a single media
	// planner may be allowlisted at this time. Format:
	// `mediaPlanners/{mediaPlannerAccountId}`
	AllowlistedMediaPlanners []string `json:"allowlistedMediaPlanners,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowlistedMediaPlanners")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowlistedMediaPlanners") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessControlSettings: Settings for controlling access to a curated package.

func (AccessControlSettings) MarshalJSON ¶
added in v0.259.0
func (s AccessControlSettings) MarshalJSON() ([]byte, error)
type ActivateClientRequest ¶
type ActivateClientRequest struct {
}

ActivateClientRequest: Request message for activating a client.

type ActivateClientUserRequest ¶
type ActivateClientUserRequest struct {
}

ActivateClientUserRequest: Request message for activating a client user.

type ActivateCuratedPackageRequest ¶
added in v0.259.0
type ActivateCuratedPackageRequest struct {
}

ActivateCuratedPackageRequest: Request message for ActivateCuratedPackage.

type ActivateDataSegmentRequest ¶
type ActivateDataSegmentRequest struct {
}

ActivateDataSegmentRequest: Request message for activating a data segment

type AdSize ¶
type AdSize struct {
	// Height: The height of the ad slot in pixels. This field will be present only
	// when size type is `PIXEL`.
	Height int64 `json:"height,omitempty,string"`
	// Type: The type of the ad slot size.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - A placeholder for an undefined size type.
	//   "PIXEL" - Ad slot with size specified by height and width in pixels.
	//   "INTERSTITIAL" - Special size to describe an interstitial ad slot.
	//   "NATIVE" - Native (mobile) ads rendered by the publisher.
	//   "FLUID" - Fluid size (responsive size) can be resized automatically with
	// the change of outside environment.
	Type string `json:"type,omitempty"`
	// Width: The width of the ad slot in pixels. This field will be present only
	// when size type is `PIXEL`.
	Width int64 `json:"width,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "Height") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Height") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdSize: Represents size of a single ad slot, or a creative.

func (AdSize) MarshalJSON ¶
func (s AdSize) MarshalJSON() ([]byte, error)
type AddCreativeRequest ¶
type AddCreativeRequest struct {
	// Creative: Name of the creative to add to the finalized deal, in the format
	// `buyers/{buyerAccountId}/creatives/{creativeId}`. See creative.name.
	Creative string `json:"creative,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Creative") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Creative") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AddCreativeRequest: Request message for adding creative to be used in the bidding process for the finalized deal.

func (AddCreativeRequest) MarshalJSON ¶
func (s AddCreativeRequest) MarshalJSON() ([]byte, error)
type AddNoteRequest ¶
type AddNoteRequest struct {
	// Note: The note to add.
	Note *Note `json:"note,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Note") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Note") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AddNoteRequest: Request to add a note.

func (AddNoteRequest) MarshalJSON ¶
func (s AddNoteRequest) MarshalJSON() ([]byte, error)
type AuctionPackage ¶
type AuctionPackage struct {
	// CreateTime: Output only. Time the auction package was created.
	CreateTime string `json:"createTime,omitempty"`
	// Creator: Output only. The buyer that created this auction package. Format:
	// `buyers/{buyerAccountId}`
	Creator string `json:"creator,omitempty"`
	// DealOwnerSeatId: Output only. If set, this field contains the DSP specific
	// seat id set by the media planner account that is considered the owner of
	// this deal. The seat ID is in the calling DSP's namespace.
	DealOwnerSeatId string `json:"dealOwnerSeatId,omitempty"`
	// Description: Output only. A description of the auction package.
	Description string `json:"description,omitempty"`
	// DisplayName: The display_name assigned to the auction package.
	DisplayName string `json:"displayName,omitempty"`
	// EligibleSeatIds: Output only. If set, this field identifies a seat that the
	// media planner selected as the owner of this auction package. This is a seat
	// ID in the DSP's namespace that was provided to the media planner.
	EligibleSeatIds []string `json:"eligibleSeatIds,omitempty"`
	// FloorPriceCpm: Output only. The minimum price a buyer has to bid to compete
	// in this auction package. If this is field is not populated, there is no
	// floor price.
	FloorPriceCpm *Money `json:"floorPriceCpm,omitempty"`
	// Name: Immutable. The unique identifier for the auction package. Format:
	// `buyers/{accountId}/auctionPackages/{auctionPackageId}` The
	// auction_package_id part of name is sent in the BidRequest to all RTB bidders
	// and is returned as deal_id by the bidder in the BidResponse.
	Name string `json:"name,omitempty"`
	// SubscribedBuyers: Output only. The list of buyers that are subscribed to the
	// AuctionPackage. This field is only populated when calling as a bidder.
	// Format: `buyers/{buyerAccountId}`
	SubscribedBuyers []string `json:"subscribedBuyers,omitempty"`
	// SubscribedClients: Output only. When calling as a buyer, the list of clients
	// of the current buyer that are subscribed to the AuctionPackage. When calling
	// as a bidder, the list of clients that are subscribed to the AuctionPackage
	// owned by the bidder or its buyers. Format:
	// `buyers/{buyerAccountId}/clients/{clientAccountId}`
	SubscribedClients []string `json:"subscribedClients,omitempty"`
	// SubscribedMediaPlanners: Output only. The list of media planners that are
	// subscribed to the AuctionPackage. This field is only populated when calling
	// as a bidder.
	SubscribedMediaPlanners []*MediaPlanner `json:"subscribedMediaPlanners,omitempty"`
	// UpdateTime: Output only. Time the auction package was last updated. This
	// value is only increased when this auction package is updated but never when
	// a buyer subscribed.
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

AuctionPackage: Defines a segment of inventory that buyer wants to buy. It's created by buyer and could be shared with multiple buyers.

func (AuctionPackage) MarshalJSON ¶
func (s AuctionPackage) MarshalJSON() ([]byte, error)
type BatchUpdateDealsRequest ¶
type BatchUpdateDealsRequest struct {
	// Requests: Required. List of request messages to update deals.
	Requests []*UpdateDealRequest `json:"requests,omitempty"`
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

BatchUpdateDealsRequest: Request message for batch updating deals.

func (BatchUpdateDealsRequest) MarshalJSON ¶
func (s BatchUpdateDealsRequest) MarshalJSON() ([]byte, error)
type BatchUpdateDealsResponse ¶
type BatchUpdateDealsResponse struct {
	// Deals: Deals updated.
	Deals []*Deal `json:"deals,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Deals") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BatchUpdateDealsResponse: Response message for batch updating deals.

func (BatchUpdateDealsResponse) MarshalJSON ¶
func (s BatchUpdateDealsResponse) MarshalJSON() ([]byte, error)
type BiddersAuctionPackagesListCall ¶
type BiddersAuctionPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAuctionPackagesListCall) Context ¶
func (c *BiddersAuctionPackagesListCall) Context(ctx context.Context) *BiddersAuctionPackagesListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAuctionPackagesListCall) Do ¶
func (c *BiddersAuctionPackagesListCall) Do(opts ...googleapi.CallOption) (*ListAuctionPackagesResponse, error)

Do executes the "authorizedbuyersmarketplace.bidders.auctionPackages.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuctionPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAuctionPackagesListCall) Fields ¶
func (c *BiddersAuctionPackagesListCall) Fields(s ...googleapi.Field) *BiddersAuctionPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAuctionPackagesListCall) Filter ¶
func (c *BiddersAuctionPackagesListCall) Filter(filter string) *BiddersAuctionPackagesListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (/authorized-buyers/apis/guides/list-filters). Only supported when parent is bidder. Supported columns for filtering are: * displayName * createTime * updateTime * eligibleSeatIds

func (*BiddersAuctionPackagesListCall) Header ¶
func (c *BiddersAuctionPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAuctionPackagesListCall) IfNoneMatch ¶
func (c *BiddersAuctionPackagesListCall) IfNoneMatch(entityTag string) *BiddersAuctionPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAuctionPackagesListCall) OrderBy ¶
func (c *BiddersAuctionPackagesListCall) OrderBy(orderBy string) *BiddersAuctionPackagesListCall

OrderBy sets the optional parameter "orderBy": An optional query string to sort auction packages using the Cloud API sorting syntax (https://cloud.google.com/apis/design/design_patterns#sorting_order). If no sort order is specified, results will be returned in an arbitrary order. Only supported when parent is bidder. Supported columns for sorting are: * displayName * createTime * updateTime

func (*BiddersAuctionPackagesListCall) PageSize ¶
func (c *BiddersAuctionPackagesListCall) PageSize(pageSize int64) *BiddersAuctionPackagesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. Max allowed page size is 500.

func (*BiddersAuctionPackagesListCall) PageToken ¶
func (c *BiddersAuctionPackagesListCall) PageToken(pageToken string) *BiddersAuctionPackagesListCall

PageToken sets the optional parameter "pageToken": The page token as returned. ListAuctionPackagesResponse.nextPageToken

func (*BiddersAuctionPackagesListCall) Pages ¶
func (c *BiddersAuctionPackagesListCall) Pages(ctx context.Context, f func(*ListAuctionPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAuctionPackagesService ¶
type BiddersAuctionPackagesService struct {
	// contains filtered or unexported fields
}
func NewBiddersAuctionPackagesService ¶
func NewBiddersAuctionPackagesService(s *Service) *BiddersAuctionPackagesService
func (*BiddersAuctionPackagesService) List ¶
func (r *BiddersAuctionPackagesService) List(parent string) *BiddersAuctionPackagesListCall

List: List the auction packages. Buyers can use the URL path "/v1alpha/buyers/{accountId}/auctionPackages" to list auction packages for the current buyer and its clients. Bidders can use the URL path "/v1alpha/bidders/{accountId}/auctionPackages" to list auction packages for the bidder, its media planners, its buyers, and all their clients.

parent: Name of the parent buyer that can access the auction package. Format: `buyers/{accountId}`. When used with a bidder account, the auction packages that the bidder, its media planners, its buyers and clients are subscribed to will be listed, in the format `bidders/{accountId}`.
type BiddersFinalizedDealsListCall ¶
type BiddersFinalizedDealsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFinalizedDealsListCall) Context ¶
func (c *BiddersFinalizedDealsListCall) Context(ctx context.Context) *BiddersFinalizedDealsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFinalizedDealsListCall) Do ¶
func (c *BiddersFinalizedDealsListCall) Do(opts ...googleapi.CallOption) (*ListFinalizedDealsResponse, error)

Do executes the "authorizedbuyersmarketplace.bidders.finalizedDeals.list" call. Any non-2xx status code is an error. Response headers are in either *ListFinalizedDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFinalizedDealsListCall) Fields ¶
func (c *BiddersFinalizedDealsListCall) Fields(s ...googleapi.Field) *BiddersFinalizedDealsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFinalizedDealsListCall) Filter ¶
func (c *BiddersFinalizedDealsListCall) Filter(filter string) *BiddersFinalizedDealsListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (https://developers.google.com/authorized-buyers/apis/guides/list-filters) Supported columns for filtering are: * deal.displayName * deal.dealType * deal.createTime * deal.updateTime * deal.flightStartTime * deal.flightEndTime * deal.eligibleSeatIds * dealServingStatus

func (*BiddersFinalizedDealsListCall) Header ¶
func (c *BiddersFinalizedDealsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFinalizedDealsListCall) IfNoneMatch ¶
func (c *BiddersFinalizedDealsListCall) IfNoneMatch(entityTag string) *BiddersFinalizedDealsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFinalizedDealsListCall) OrderBy ¶
func (c *BiddersFinalizedDealsListCall) OrderBy(orderBy string) *BiddersFinalizedDealsListCall

OrderBy sets the optional parameter "orderBy": An optional query string to sort finalized deals using the Cloud API sorting syntax (https://cloud.google.com/apis/design/design_patterns#sorting_order). If no sort order is specified, results will be returned in an arbitrary order. Supported columns for sorting are: * deal.displayName * deal.createTime * deal.updateTime * deal.flightStartTime * deal.flightEndTime * rtbMetrics.bidRequests7Days * rtbMetrics.bids7Days * rtbMetrics.adImpressions7Days * rtbMetrics.bidRate7Days * rtbMetrics.filteredBidRate7Days * rtbMetrics.mustBidRateCurrentMonth

func (*BiddersFinalizedDealsListCall) PageSize ¶
func (c *BiddersFinalizedDealsListCall) PageSize(pageSize int64) *BiddersFinalizedDealsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If requested more than 500, the server will return 500 results per page. If unspecified, the server will pick a default page size of 100.

func (*BiddersFinalizedDealsListCall) PageToken ¶
func (c *BiddersFinalizedDealsListCall) PageToken(pageToken string) *BiddersFinalizedDealsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListFinalizedDealsResponse.

func (*BiddersFinalizedDealsListCall) Pages ¶
func (c *BiddersFinalizedDealsListCall) Pages(ctx context.Context, f func(*ListFinalizedDealsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFinalizedDealsService ¶
type BiddersFinalizedDealsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFinalizedDealsService ¶
func NewBiddersFinalizedDealsService(s *Service) *BiddersFinalizedDealsService
func (*BiddersFinalizedDealsService) List ¶
func (r *BiddersFinalizedDealsService) List(parent string) *BiddersFinalizedDealsListCall

List: Lists finalized deals. Use the URL path "/v1alpha/buyers/{accountId}/finalizedDeals" to list finalized deals for the current buyer and its clients. Bidders can use the URL path "/v1alpha/bidders/{accountId}/finalizedDeals" to list finalized deals for the bidder, its buyers and all their clients.

parent: The buyer to list the finalized deals for, in the format: `buyers/{accountId}`. When used to list finalized deals for a bidder, its buyers and clients, in the format `bidders/{accountId}`.
func (*BiddersFinalizedDealsService) SetReadyToServe ¶
added in v0.255.0
func (r *BiddersFinalizedDealsService) SetReadyToServe(deal string, setreadytoserverequest *SetReadyToServeRequest) *BiddersFinalizedDealsSetReadyToServeCall

SetReadyToServe: Sets the given finalized deal as ready to serve. By default, deals are set as ready to serve as soon as they're finalized. If you want to opt out of the default behavior, and manually indicate that deals are ready to serve, ask your Technical Account Manager to add you to the allowlist. If you choose to use this method, finalized deals belonging to the bidder and its child seats don't start serving until after you call `setReadyToServe`, and after the deals become active. For example, you can use this method to delay receiving bid requests until your creative is ready. In addition, bidders can use the URL path "/v1alpha/bidders/{accountId}/finalizedDeals/{dealId}" to set ready to serve for the finalized deals belong to itself, its child seats and all their clients. This method only applies to programmatic guaranteed deals.

deal: Format: `buyers/{accountId}/finalizedDeals/{dealId}` or `bidders/{accountId}/finalizedDeals/{dealId}`.
type BiddersFinalizedDealsSetReadyToServeCall ¶
added in v0.255.0
type BiddersFinalizedDealsSetReadyToServeCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFinalizedDealsSetReadyToServeCall) Context ¶
added in v0.255.0
func (c *BiddersFinalizedDealsSetReadyToServeCall) Context(ctx context.Context) *BiddersFinalizedDealsSetReadyToServeCall

Context sets the context to be used in this call's Do method.

func (*BiddersFinalizedDealsSetReadyToServeCall) Do ¶
added in v0.255.0
func (c *BiddersFinalizedDealsSetReadyToServeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.bidders.finalizedDeals.setReadyToServe" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFinalizedDealsSetReadyToServeCall) Fields ¶
added in v0.255.0
func (c *BiddersFinalizedDealsSetReadyToServeCall) Fields(s ...googleapi.Field) *BiddersFinalizedDealsSetReadyToServeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFinalizedDealsSetReadyToServeCall) Header ¶
added in v0.255.0
func (c *BiddersFinalizedDealsSetReadyToServeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BiddersService ¶
type BiddersService struct {
	AuctionPackages *BiddersAuctionPackagesService

	FinalizedDeals *BiddersFinalizedDealsService
	// contains filtered or unexported fields
}
func NewBiddersService ¶
func NewBiddersService(s *Service) *BiddersService
type BuyersAuctionPackagesGetCall ¶
type BuyersAuctionPackagesGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesGetCall) Context ¶
func (c *BuyersAuctionPackagesGetCall) Context(ctx context.Context) *BuyersAuctionPackagesGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesGetCall) Do ¶
func (c *BuyersAuctionPackagesGetCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.get" call. Any non-2xx status code is an error. Response headers are in either *AuctionPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesGetCall) Fields ¶
func (c *BuyersAuctionPackagesGetCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesGetCall) Header ¶
func (c *BuyersAuctionPackagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersAuctionPackagesGetCall) IfNoneMatch ¶
func (c *BuyersAuctionPackagesGetCall) IfNoneMatch(entityTag string) *BuyersAuctionPackagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersAuctionPackagesListCall ¶
type BuyersAuctionPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesListCall) Context ¶
func (c *BuyersAuctionPackagesListCall) Context(ctx context.Context) *BuyersAuctionPackagesListCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesListCall) Do ¶
func (c *BuyersAuctionPackagesListCall) Do(opts ...googleapi.CallOption) (*ListAuctionPackagesResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuctionPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesListCall) Fields ¶
func (c *BuyersAuctionPackagesListCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesListCall) Filter ¶
func (c *BuyersAuctionPackagesListCall) Filter(filter string) *BuyersAuctionPackagesListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (/authorized-buyers/apis/guides/list-filters). Only supported when parent is bidder. Supported columns for filtering are: * displayName * createTime * updateTime * eligibleSeatIds

func (*BuyersAuctionPackagesListCall) Header ¶
func (c *BuyersAuctionPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersAuctionPackagesListCall) IfNoneMatch ¶
func (c *BuyersAuctionPackagesListCall) IfNoneMatch(entityTag string) *BuyersAuctionPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersAuctionPackagesListCall) OrderBy ¶
func (c *BuyersAuctionPackagesListCall) OrderBy(orderBy string) *BuyersAuctionPackagesListCall

OrderBy sets the optional parameter "orderBy": An optional query string to sort auction packages using the Cloud API sorting syntax (https://cloud.google.com/apis/design/design_patterns#sorting_order). If no sort order is specified, results will be returned in an arbitrary order. Only supported when parent is bidder. Supported columns for sorting are: * displayName * createTime * updateTime

func (*BuyersAuctionPackagesListCall) PageSize ¶
func (c *BuyersAuctionPackagesListCall) PageSize(pageSize int64) *BuyersAuctionPackagesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. Max allowed page size is 500.

func (*BuyersAuctionPackagesListCall) PageToken ¶
func (c *BuyersAuctionPackagesListCall) PageToken(pageToken string) *BuyersAuctionPackagesListCall

PageToken sets the optional parameter "pageToken": The page token as returned. ListAuctionPackagesResponse.nextPageToken

func (*BuyersAuctionPackagesListCall) Pages ¶
func (c *BuyersAuctionPackagesListCall) Pages(ctx context.Context, f func(*ListAuctionPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersAuctionPackagesService ¶
type BuyersAuctionPackagesService struct {
	// contains filtered or unexported fields
}
func NewBuyersAuctionPackagesService ¶
func NewBuyersAuctionPackagesService(s *Service) *BuyersAuctionPackagesService
func (*BuyersAuctionPackagesService) Get ¶
func (r *BuyersAuctionPackagesService) Get(name string) *BuyersAuctionPackagesGetCall

Get: Gets an auction package given its name.

name: Name of auction package to get. Format: `buyers/{accountId}/auctionPackages/{auctionPackageId}`.
func (*BuyersAuctionPackagesService) List ¶
func (r *BuyersAuctionPackagesService) List(parent string) *BuyersAuctionPackagesListCall

List: List the auction packages. Buyers can use the URL path "/v1alpha/buyers/{accountId}/auctionPackages" to list auction packages for the current buyer and its clients. Bidders can use the URL path "/v1alpha/bidders/{accountId}/auctionPackages" to list auction packages for the bidder, its media planners, its buyers, and all their clients.

parent: Name of the parent buyer that can access the auction package. Format: `buyers/{accountId}`. When used with a bidder account, the auction packages that the bidder, its media planners, its buyers and clients are subscribed to will be listed, in the format `bidders/{accountId}`.
func (*BuyersAuctionPackagesService) Subscribe ¶
func (r *BuyersAuctionPackagesService) Subscribe(name string, subscribeauctionpackagerequest *SubscribeAuctionPackageRequest) *BuyersAuctionPackagesSubscribeCall

Subscribe: Subscribe to the auction package for the specified buyer. Once subscribed, the bidder will receive a call out for inventory matching the auction package targeting criteria with the auction package deal ID and the specified buyer.

name: Name of the auction package. Format: `buyers/{accountId}/auctionPackages/{auctionPackageId}`.
func (*BuyersAuctionPackagesService) SubscribeClients ¶
func (r *BuyersAuctionPackagesService) SubscribeClients(auctionPackage string, subscribeclientsrequest *SubscribeClientsRequest) *BuyersAuctionPackagesSubscribeClientsCall

SubscribeClients: Subscribe the specified clients of the buyer to the auction package. If a client in the list does not belong to the buyer, an error response will be returned, and all of the following clients in the list will not be subscribed. Subscribing an already subscribed client will have no effect.

auctionPackage: Name of the auction package. Format: `buyers/{accountId}/auctionPackages/{auctionPackageId}`.
func (*BuyersAuctionPackagesService) Unsubscribe ¶
func (r *BuyersAuctionPackagesService) Unsubscribe(name string, unsubscribeauctionpackagerequest *UnsubscribeAuctionPackageRequest) *BuyersAuctionPackagesUnsubscribeCall

Unsubscribe: Unsubscribe from the auction package for the specified buyer. Once unsubscribed, the bidder will no longer receive a call out for the auction package deal ID and the specified buyer.

name: Name of the auction package. Format: `buyers/{accountId}/auctionPackages/{auctionPackageId}`.
func (*BuyersAuctionPackagesService) UnsubscribeClients ¶
func (r *BuyersAuctionPackagesService) UnsubscribeClients(auctionPackage string, unsubscribeclientsrequest *UnsubscribeClientsRequest) *BuyersAuctionPackagesUnsubscribeClientsCall

UnsubscribeClients: Unsubscribe from the auction package for the specified clients of the buyer. Unsubscribing a client that is not subscribed will have no effect.

auctionPackage: Name of the auction package. Format: `buyers/{accountId}/auctionPackages/{auctionPackageId}`.
type BuyersAuctionPackagesSubscribeCall ¶
type BuyersAuctionPackagesSubscribeCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesSubscribeCall) Context ¶
func (c *BuyersAuctionPackagesSubscribeCall) Context(ctx context.Context) *BuyersAuctionPackagesSubscribeCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesSubscribeCall) Do ¶
func (c *BuyersAuctionPackagesSubscribeCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.subscribe" call. Any non-2xx status code is an error. Response headers are in either *AuctionPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesSubscribeCall) Fields ¶
func (c *BuyersAuctionPackagesSubscribeCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesSubscribeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesSubscribeCall) Header ¶
func (c *BuyersAuctionPackagesSubscribeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersAuctionPackagesSubscribeClientsCall ¶
type BuyersAuctionPackagesSubscribeClientsCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesSubscribeClientsCall) Context ¶
func (c *BuyersAuctionPackagesSubscribeClientsCall) Context(ctx context.Context) *BuyersAuctionPackagesSubscribeClientsCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesSubscribeClientsCall) Do ¶
func (c *BuyersAuctionPackagesSubscribeClientsCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.subscribeClients" call. Any non-2xx status code is an error. Response headers are in either *AuctionPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesSubscribeClientsCall) Fields ¶
func (c *BuyersAuctionPackagesSubscribeClientsCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesSubscribeClientsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesSubscribeClientsCall) Header ¶
func (c *BuyersAuctionPackagesSubscribeClientsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersAuctionPackagesUnsubscribeCall ¶
type BuyersAuctionPackagesUnsubscribeCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesUnsubscribeCall) Context ¶
func (c *BuyersAuctionPackagesUnsubscribeCall) Context(ctx context.Context) *BuyersAuctionPackagesUnsubscribeCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesUnsubscribeCall) Do ¶
func (c *BuyersAuctionPackagesUnsubscribeCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.unsubscribe" call. Any non-2xx status code is an error. Response headers are in either *AuctionPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesUnsubscribeCall) Fields ¶
func (c *BuyersAuctionPackagesUnsubscribeCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesUnsubscribeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesUnsubscribeCall) Header ¶
func (c *BuyersAuctionPackagesUnsubscribeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersAuctionPackagesUnsubscribeClientsCall ¶
type BuyersAuctionPackagesUnsubscribeClientsCall struct {
	// contains filtered or unexported fields
}
func (*BuyersAuctionPackagesUnsubscribeClientsCall) Context ¶
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Context(ctx context.Context) *BuyersAuctionPackagesUnsubscribeClientsCall

Context sets the context to be used in this call's Do method.

func (*BuyersAuctionPackagesUnsubscribeClientsCall) Do ¶
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Do(opts ...googleapi.CallOption) (*AuctionPackage, error)

Do executes the "authorizedbuyersmarketplace.buyers.auctionPackages.unsubscribeClients" call. Any non-2xx status code is an error. Response headers are in either *AuctionPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersAuctionPackagesUnsubscribeClientsCall) Fields ¶
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Fields(s ...googleapi.Field) *BuyersAuctionPackagesUnsubscribeClientsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersAuctionPackagesUnsubscribeClientsCall) Header ¶
func (c *BuyersAuctionPackagesUnsubscribeClientsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsActivateCall ¶
type BuyersClientsActivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsActivateCall) Context ¶
func (c *BuyersClientsActivateCall) Context(ctx context.Context) *BuyersClientsActivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsActivateCall) Do ¶
func (c *BuyersClientsActivateCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.activate" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsActivateCall) Fields ¶
func (c *BuyersClientsActivateCall) Fields(s ...googleapi.Field) *BuyersClientsActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsActivateCall) Header ¶
func (c *BuyersClientsActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsCreateCall ¶
type BuyersClientsCreateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsCreateCall) Context ¶
func (c *BuyersClientsCreateCall) Context(ctx context.Context) *BuyersClientsCreateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsCreateCall) Do ¶
func (c *BuyersClientsCreateCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.create" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsCreateCall) Fields ¶
func (c *BuyersClientsCreateCall) Fields(s ...googleapi.Field) *BuyersClientsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsCreateCall) Header ¶
func (c *BuyersClientsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsDeactivateCall ¶
type BuyersClientsDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsDeactivateCall) Context ¶
func (c *BuyersClientsDeactivateCall) Context(ctx context.Context) *BuyersClientsDeactivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsDeactivateCall) Do ¶
func (c *BuyersClientsDeactivateCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.deactivate" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsDeactivateCall) Fields ¶
func (c *BuyersClientsDeactivateCall) Fields(s ...googleapi.Field) *BuyersClientsDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsDeactivateCall) Header ¶
func (c *BuyersClientsDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsGetCall ¶
type BuyersClientsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsGetCall) Context ¶
func (c *BuyersClientsGetCall) Context(ctx context.Context) *BuyersClientsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsGetCall) Do ¶
func (c *BuyersClientsGetCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.get" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsGetCall) Fields ¶
func (c *BuyersClientsGetCall) Fields(s ...googleapi.Field) *BuyersClientsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsGetCall) Header ¶
func (c *BuyersClientsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersClientsGetCall) IfNoneMatch ¶
func (c *BuyersClientsGetCall) IfNoneMatch(entityTag string) *BuyersClientsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersClientsListCall ¶
type BuyersClientsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsListCall) Context ¶
func (c *BuyersClientsListCall) Context(ctx context.Context) *BuyersClientsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsListCall) Do ¶
func (c *BuyersClientsListCall) Do(opts ...googleapi.CallOption) (*ListClientsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.list" call. Any non-2xx status code is an error. Response headers are in either *ListClientsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsListCall) Fields ¶
func (c *BuyersClientsListCall) Fields(s ...googleapi.Field) *BuyersClientsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsListCall) Filter ¶
func (c *BuyersClientsListCall) Filter(filter string) *BuyersClientsListCall

Filter sets the optional parameter "filter": Query string using the Filtering Syntax (https://developers.google.com/authorized-buyers/apis/guides/list-filters) Supported fields for filtering are: * partnerClientId Use this field to filter the clients by the partnerClientId. For example, if the partnerClientId of the client is "1234", the value of this field should be `partnerClientId = "1234", in order to get only the client whose partnerClientId is "1234" in the response.

func (*BuyersClientsListCall) Header ¶
func (c *BuyersClientsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersClientsListCall) IfNoneMatch ¶
func (c *BuyersClientsListCall) IfNoneMatch(entityTag string) *BuyersClientsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersClientsListCall) PageSize ¶
func (c *BuyersClientsListCall) PageSize(pageSize int64) *BuyersClientsListCall

PageSize sets the optional parameter "pageSize": Requested page size. If left blank, a default page size of 500 will be applied.

func (*BuyersClientsListCall) PageToken ¶
func (c *BuyersClientsListCall) PageToken(pageToken string) *BuyersClientsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListClientsResponse.nextPageToken returned from the previous call to the list method.

func (*BuyersClientsListCall) Pages ¶
func (c *BuyersClientsListCall) Pages(ctx context.Context, f func(*ListClientsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersClientsPatchCall ¶
type BuyersClientsPatchCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsPatchCall) Context ¶
func (c *BuyersClientsPatchCall) Context(ctx context.Context) *BuyersClientsPatchCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsPatchCall) Do ¶
func (c *BuyersClientsPatchCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.patch" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsPatchCall) Fields ¶
func (c *BuyersClientsPatchCall) Fields(s ...googleapi.Field) *BuyersClientsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsPatchCall) Header ¶
func (c *BuyersClientsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersClientsPatchCall) UpdateMask ¶
func (c *BuyersClientsPatchCall) UpdateMask(updateMask string) *BuyersClientsPatchCall

UpdateMask sets the optional parameter "updateMask": List of fields to be updated. If empty or unspecified, the service will update all fields populated in the update request excluding the output only fields and primitive fields with default value. Note that explicit field mask is required in order to reset a primitive field back to its default value, for example, false for boolean fields, 0 for integer fields. A special field mask consisting of a single path "*" can be used to indicate full replacement(the equivalent of PUT method), updatable fields unset or unspecified in the input will be cleared or set to default value. Output only fields will be ignored regardless of the value of updateMask.

type BuyersClientsService ¶
type BuyersClientsService struct {
	Users *BuyersClientsUsersService
	// contains filtered or unexported fields
}
func NewBuyersClientsService ¶
func NewBuyersClientsService(s *Service) *BuyersClientsService
func (*BuyersClientsService) Activate ¶
func (r *BuyersClientsService) Activate(name string, activateclientrequest *ActivateClientRequest) *BuyersClientsActivateCall

Activate: Activates an existing client. The state of the client will be updated to "ACTIVE". This method has no effect if the client is already in "ACTIVE" state.

- name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}`.

func (*BuyersClientsService) Create ¶
func (r *BuyersClientsService) Create(parent string, client *Client) *BuyersClientsCreateCall

Create: Creates a new client.

- parent: The name of the buyer. Format: `buyers/{accountId}`.

func (*BuyersClientsService) Deactivate ¶
func (r *BuyersClientsService) Deactivate(name string, deactivateclientrequest *DeactivateClientRequest) *BuyersClientsDeactivateCall

Deactivate: Deactivates an existing client. The state of the client will be updated to "INACTIVE". This method has no effect if the client is already in "INACTIVE" state.

- name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}`.

func (*BuyersClientsService) Get ¶
func (r *BuyersClientsService) Get(name string) *BuyersClientsGetCall

Get: Gets a client with a given resource name.

- name: Format: `buyers/{accountId}/clients/{clientAccountId}`.

func (*BuyersClientsService) List ¶
func (r *BuyersClientsService) List(parent string) *BuyersClientsListCall

List: Lists all the clients for the current buyer.

- parent: The name of the buyer. Format: `buyers/{accountId}`.

func (*BuyersClientsService) Patch ¶
func (r *BuyersClientsService) Patch(name string, client *Client) *BuyersClientsPatchCall

Patch: Updates an existing client.

name: Output only. The resource name of the client. Format: `buyers/{accountId}/clients/{clientAccountId}`.
type BuyersClientsUsersActivateCall ¶
type BuyersClientsUsersActivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersActivateCall) Context ¶
func (c *BuyersClientsUsersActivateCall) Context(ctx context.Context) *BuyersClientsUsersActivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersActivateCall) Do ¶
func (c *BuyersClientsUsersActivateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.activate" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersActivateCall) Fields ¶
func (c *BuyersClientsUsersActivateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersActivateCall) Header ¶
func (c *BuyersClientsUsersActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsUsersCreateCall ¶
type BuyersClientsUsersCreateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersCreateCall) Context ¶
func (c *BuyersClientsUsersCreateCall) Context(ctx context.Context) *BuyersClientsUsersCreateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersCreateCall) Do ¶
func (c *BuyersClientsUsersCreateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.create" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersCreateCall) Fields ¶
func (c *BuyersClientsUsersCreateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersCreateCall) Header ¶
func (c *BuyersClientsUsersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsUsersDeactivateCall ¶
type BuyersClientsUsersDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersDeactivateCall) Context ¶
func (c *BuyersClientsUsersDeactivateCall) Context(ctx context.Context) *BuyersClientsUsersDeactivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersDeactivateCall) Do ¶
func (c *BuyersClientsUsersDeactivateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.deactivate" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersDeactivateCall) Fields ¶
func (c *BuyersClientsUsersDeactivateCall) Fields(s ...googleapi.Field) *BuyersClientsUsersDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersDeactivateCall) Header ¶
func (c *BuyersClientsUsersDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsUsersDeleteCall ¶
type BuyersClientsUsersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersDeleteCall) Context ¶
func (c *BuyersClientsUsersDeleteCall) Context(ctx context.Context) *BuyersClientsUsersDeleteCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersDeleteCall) Do ¶
func (c *BuyersClientsUsersDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersDeleteCall) Fields ¶
func (c *BuyersClientsUsersDeleteCall) Fields(s ...googleapi.Field) *BuyersClientsUsersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersDeleteCall) Header ¶
func (c *BuyersClientsUsersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersClientsUsersGetCall ¶
type BuyersClientsUsersGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersGetCall) Context ¶
func (c *BuyersClientsUsersGetCall) Context(ctx context.Context) *BuyersClientsUsersGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersGetCall) Do ¶
func (c *BuyersClientsUsersGetCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.get" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersGetCall) Fields ¶
func (c *BuyersClientsUsersGetCall) Fields(s ...googleapi.Field) *BuyersClientsUsersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersGetCall) Header ¶
func (c *BuyersClientsUsersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersClientsUsersGetCall) IfNoneMatch ¶
func (c *BuyersClientsUsersGetCall) IfNoneMatch(entityTag string) *BuyersClientsUsersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersClientsUsersListCall ¶
type BuyersClientsUsersListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersClientsUsersListCall) Context ¶
func (c *BuyersClientsUsersListCall) Context(ctx context.Context) *BuyersClientsUsersListCall

Context sets the context to be used in this call's Do method.

func (*BuyersClientsUsersListCall) Do ¶
func (c *BuyersClientsUsersListCall) Do(opts ...googleapi.CallOption) (*ListClientUsersResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.clients.users.list" call. Any non-2xx status code is an error. Response headers are in either *ListClientUsersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersClientsUsersListCall) Fields ¶
func (c *BuyersClientsUsersListCall) Fields(s ...googleapi.Field) *BuyersClientsUsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersClientsUsersListCall) Header ¶
func (c *BuyersClientsUsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersClientsUsersListCall) IfNoneMatch ¶
func (c *BuyersClientsUsersListCall) IfNoneMatch(entityTag string) *BuyersClientsUsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersClientsUsersListCall) PageSize ¶
func (c *BuyersClientsUsersListCall) PageSize(pageSize int64) *BuyersClientsUsersListCall

PageSize sets the optional parameter "pageSize": Requested page size. If left blank, a default page size of 500 will be applied.

func (*BuyersClientsUsersListCall) PageToken ¶
func (c *BuyersClientsUsersListCall) PageToken(pageToken string) *BuyersClientsUsersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListClientUsersResponse.nextPageToken returned from the previous call to the list method.

func (*BuyersClientsUsersListCall) Pages ¶
func (c *BuyersClientsUsersListCall) Pages(ctx context.Context, f func(*ListClientUsersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersClientsUsersService ¶
type BuyersClientsUsersService struct {
	// contains filtered or unexported fields
}
func NewBuyersClientsUsersService ¶
func NewBuyersClientsUsersService(s *Service) *BuyersClientsUsersService
func (*BuyersClientsUsersService) Activate ¶
func (r *BuyersClientsUsersService) Activate(name string, activateclientuserrequest *ActivateClientUserRequest) *BuyersClientsUsersActivateCall

Activate: Activates an existing client user. The state of the client user will be updated from "INACTIVE" to "ACTIVE". This method has no effect if the client user is already in "ACTIVE" state. An error will be returned if the client user to activate is still in "INVITED" state.

name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}/clientUsers/{userId}`.
func (*BuyersClientsUsersService) Create ¶
func (r *BuyersClientsUsersService) Create(parent string, clientuser *ClientUser) *BuyersClientsUsersCreateCall

Create: Creates a new client user in "INVITED" state. An email invitation will be sent to the new user, once accepted the user will become active.

parent: The name of the client. Format: `buyers/{accountId}/clients/{clientAccountId}`.
func (*BuyersClientsUsersService) Deactivate ¶
func (r *BuyersClientsUsersService) Deactivate(name string, deactivateclientuserrequest *DeactivateClientUserRequest) *BuyersClientsUsersDeactivateCall

Deactivate: Deactivates an existing client user. The state of the client user will be updated from "ACTIVE" to "INACTIVE". This method has no effect if the client user is already in "INACTIVE" state. An error will be returned if the client user to deactivate is still in "INVITED" state.

name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}/clientUsers/{userId}`.
func (*BuyersClientsUsersService) Delete ¶
func (r *BuyersClientsUsersService) Delete(name string) *BuyersClientsUsersDeleteCall

Delete: Deletes an existing client user. The client user will lose access to the Authorized Buyers UI. Note that if a client user is deleted, the user's access to the UI can't be restored unless a new client user is created and activated.

name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}/clientUsers/{userId}`.
func (*BuyersClientsUsersService) Get ¶
func (r *BuyersClientsUsersService) Get(name string) *BuyersClientsUsersGetCall

Get: Retrieves an existing client user.

name: Format: `buyers/{buyerAccountId}/clients/{clientAccountId}/clientUsers/{userId}`.
func (*BuyersClientsUsersService) List ¶
func (r *BuyersClientsUsersService) List(parent string) *BuyersClientsUsersListCall

List: Lists all client users for a specified client.

parent: The name of the client. Format: `buyers/{buyerAccountId}/clients/{clientAccountId}`.
type BuyersDataSegmentsActivateCall ¶
type BuyersDataSegmentsActivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsActivateCall) Context ¶
func (c *BuyersDataSegmentsActivateCall) Context(ctx context.Context) *BuyersDataSegmentsActivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsActivateCall) Do ¶
func (c *BuyersDataSegmentsActivateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.activate" call. Any non-2xx status code is an error. Response headers are in either *DataSegment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsActivateCall) Fields ¶
func (c *BuyersDataSegmentsActivateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsActivateCall) Header ¶
func (c *BuyersDataSegmentsActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersDataSegmentsCreateCall ¶
type BuyersDataSegmentsCreateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsCreateCall) Context ¶
func (c *BuyersDataSegmentsCreateCall) Context(ctx context.Context) *BuyersDataSegmentsCreateCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsCreateCall) Do ¶
func (c *BuyersDataSegmentsCreateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.create" call. Any non-2xx status code is an error. Response headers are in either *DataSegment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsCreateCall) Fields ¶
func (c *BuyersDataSegmentsCreateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsCreateCall) Header ¶
func (c *BuyersDataSegmentsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersDataSegmentsDeactivateCall ¶
type BuyersDataSegmentsDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsDeactivateCall) Context ¶
func (c *BuyersDataSegmentsDeactivateCall) Context(ctx context.Context) *BuyersDataSegmentsDeactivateCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsDeactivateCall) Do ¶
func (c *BuyersDataSegmentsDeactivateCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.deactivate" call. Any non-2xx status code is an error. Response headers are in either *DataSegment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsDeactivateCall) Fields ¶
func (c *BuyersDataSegmentsDeactivateCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsDeactivateCall) Header ¶
func (c *BuyersDataSegmentsDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersDataSegmentsGetCall ¶
type BuyersDataSegmentsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsGetCall) Context ¶
func (c *BuyersDataSegmentsGetCall) Context(ctx context.Context) *BuyersDataSegmentsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsGetCall) Do ¶
func (c *BuyersDataSegmentsGetCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.get" call. Any non-2xx status code is an error. Response headers are in either *DataSegment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsGetCall) Fields ¶
func (c *BuyersDataSegmentsGetCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsGetCall) Header ¶
func (c *BuyersDataSegmentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersDataSegmentsGetCall) IfNoneMatch ¶
func (c *BuyersDataSegmentsGetCall) IfNoneMatch(entityTag string) *BuyersDataSegmentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersDataSegmentsListCall ¶
type BuyersDataSegmentsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsListCall) Context ¶
func (c *BuyersDataSegmentsListCall) Context(ctx context.Context) *BuyersDataSegmentsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsListCall) Do ¶
func (c *BuyersDataSegmentsListCall) Do(opts ...googleapi.CallOption) (*ListDataSegmentsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.list" call. Any non-2xx status code is an error. Response headers are in either *ListDataSegmentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsListCall) Fields ¶
func (c *BuyersDataSegmentsListCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsListCall) Header ¶
func (c *BuyersDataSegmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersDataSegmentsListCall) IfNoneMatch ¶
func (c *BuyersDataSegmentsListCall) IfNoneMatch(entityTag string) *BuyersDataSegmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersDataSegmentsListCall) PageSize ¶
func (c *BuyersDataSegmentsListCall) PageSize(pageSize int64) *BuyersDataSegmentsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. Max allowed page size is 500. If unspecified, the server will default to 500.

func (*BuyersDataSegmentsListCall) PageToken ¶
func (c *BuyersDataSegmentsListCall) PageToken(pageToken string) *BuyersDataSegmentsListCall

PageToken sets the optional parameter "pageToken": The page token as returned. ListDataSegmentsResponse.nextPageToken

func (*BuyersDataSegmentsListCall) Pages ¶
func (c *BuyersDataSegmentsListCall) Pages(ctx context.Context, f func(*ListDataSegmentsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersDataSegmentsPatchCall ¶
type BuyersDataSegmentsPatchCall struct {
	// contains filtered or unexported fields
}
func (*BuyersDataSegmentsPatchCall) Context ¶
func (c *BuyersDataSegmentsPatchCall) Context(ctx context.Context) *BuyersDataSegmentsPatchCall

Context sets the context to be used in this call's Do method.

func (*BuyersDataSegmentsPatchCall) Do ¶
func (c *BuyersDataSegmentsPatchCall) Do(opts ...googleapi.CallOption) (*DataSegment, error)

Do executes the "authorizedbuyersmarketplace.buyers.dataSegments.patch" call. Any non-2xx status code is an error. Response headers are in either *DataSegment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersDataSegmentsPatchCall) Fields ¶
func (c *BuyersDataSegmentsPatchCall) Fields(s ...googleapi.Field) *BuyersDataSegmentsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersDataSegmentsPatchCall) Header ¶
func (c *BuyersDataSegmentsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersDataSegmentsPatchCall) UpdateMask ¶
func (c *BuyersDataSegmentsPatchCall) UpdateMask(updateMask string) *BuyersDataSegmentsPatchCall

UpdateMask sets the optional parameter "updateMask": List of fields to be updated. If empty or unspecified, the service will update all fields populated in the update request excluding the output only fields and primitive fields with default value. Note that explicit field mask is required in order to reset a primitive field back to its default value, for example, false for boolean fields, 0 for integer fields. A special field mask consisting of a single path "*" can be used to indicate full replacement(the equivalent of PUT method), updatable fields unset or unspecified in the input will be cleared or set to default value. Output only fields will be ignored regardless of the value of updateMask.

type BuyersDataSegmentsService ¶
type BuyersDataSegmentsService struct {
	// contains filtered or unexported fields
}
func NewBuyersDataSegmentsService ¶
func NewBuyersDataSegmentsService(s *Service) *BuyersDataSegmentsService
func (*BuyersDataSegmentsService) Activate ¶
func (r *BuyersDataSegmentsService) Activate(name string, activatedatasegmentrequest *ActivateDataSegmentRequest) *BuyersDataSegmentsActivateCall

Activate: Activates a data segment.

name: Name of data segment to activate. v1alpha format: `buyers/{accountId}/dataSegments/{curatorDataSegmentId}` v1beta format: `curators/{accountId}/dataSegments/{curatorDataSegmentId}`.
func (*BuyersDataSegmentsService) Create ¶
func (r *BuyersDataSegmentsService) Create(parent string, datasegment *DataSegment) *BuyersDataSegmentsCreateCall

Create: Creates a data segment owned by the listed curator. The data segment will be created in the `ACTIVE` state, meaning it will be immediately available for buyers to use in preferred deals, private auction deals, and auction packages.

parent: The parent resource where this data segment will be created. v1alpha format: `buyers/{accountId}` v1beta format: `curators/{accountId}`.
func (*BuyersDataSegmentsService) Deactivate ¶
func (r *BuyersDataSegmentsService) Deactivate(name string, deactivatedatasegmentrequest *DeactivateDataSegmentRequest) *BuyersDataSegmentsDeactivateCall

Deactivate: Deactivates a data segment.

name: Name of data segment to deactivate. v1alpha format: `buyers/{accountId}/dataSegments/{curatorDataSegmentId}` v1beta format: `curators/{accountId}/dataSegments/{curatorDataSegmentId}`.
func (*BuyersDataSegmentsService) Get ¶
func (r *BuyersDataSegmentsService) Get(name string) *BuyersDataSegmentsGetCall

Get: Gets a data segment given its name.

name: Name of data segment to get. v1alpha format: `buyers/{accountId}/dataSegments/{curatorDataSegmentId}` v1beta format: `curators/{accountId}/dataSegments/{curatorDataSegmentId}`.
func (*BuyersDataSegmentsService) List ¶
func (r *BuyersDataSegmentsService) List(parent string) *BuyersDataSegmentsListCall

List: List the data segments owned by a curator.

parent: Name of the parent curator that can access the data segment. v1alpha format: `buyers/{accountId}` v1beta format: `curators/{accountId}`.
func (*BuyersDataSegmentsService) Patch ¶
func (r *BuyersDataSegmentsService) Patch(nameid string, datasegment *DataSegment) *BuyersDataSegmentsPatchCall

Patch: Updates a data segment.

name: Immutable. Identifier. The unique identifier for the data segment. Account ID corresponds to the account ID that created the segment. v1alpha format: `buyers/{accountId}/dataSegments/{curatorDataSegmentId}` v1beta format: `curators/{curatorAccountId}/dataSegments/{curatorDataSegmentId}`.
type BuyersFinalizedDealsAddCreativeCall ¶
type BuyersFinalizedDealsAddCreativeCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsAddCreativeCall) Context ¶
func (c *BuyersFinalizedDealsAddCreativeCall) Context(ctx context.Context) *BuyersFinalizedDealsAddCreativeCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsAddCreativeCall) Do ¶
func (c *BuyersFinalizedDealsAddCreativeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.addCreative" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsAddCreativeCall) Fields ¶
func (c *BuyersFinalizedDealsAddCreativeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsAddCreativeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsAddCreativeCall) Header ¶
func (c *BuyersFinalizedDealsAddCreativeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersFinalizedDealsGetCall ¶
type BuyersFinalizedDealsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsGetCall) Context ¶
func (c *BuyersFinalizedDealsGetCall) Context(ctx context.Context) *BuyersFinalizedDealsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsGetCall) Do ¶
func (c *BuyersFinalizedDealsGetCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.get" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsGetCall) Fields ¶
func (c *BuyersFinalizedDealsGetCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsGetCall) Header ¶
func (c *BuyersFinalizedDealsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFinalizedDealsGetCall) IfNoneMatch ¶
func (c *BuyersFinalizedDealsGetCall) IfNoneMatch(entityTag string) *BuyersFinalizedDealsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersFinalizedDealsListCall ¶
type BuyersFinalizedDealsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsListCall) Context ¶
func (c *BuyersFinalizedDealsListCall) Context(ctx context.Context) *BuyersFinalizedDealsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsListCall) Do ¶
func (c *BuyersFinalizedDealsListCall) Do(opts ...googleapi.CallOption) (*ListFinalizedDealsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.list" call. Any non-2xx status code is an error. Response headers are in either *ListFinalizedDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsListCall) Fields ¶
func (c *BuyersFinalizedDealsListCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsListCall) Filter ¶
func (c *BuyersFinalizedDealsListCall) Filter(filter string) *BuyersFinalizedDealsListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (https://developers.google.com/authorized-buyers/apis/guides/list-filters) Supported columns for filtering are: * deal.displayName * deal.dealType * deal.createTime * deal.updateTime * deal.flightStartTime * deal.flightEndTime * deal.eligibleSeatIds * dealServingStatus

func (*BuyersFinalizedDealsListCall) Header ¶
func (c *BuyersFinalizedDealsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFinalizedDealsListCall) IfNoneMatch ¶
func (c *BuyersFinalizedDealsListCall) IfNoneMatch(entityTag string) *BuyersFinalizedDealsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFinalizedDealsListCall) OrderBy ¶
func (c *BuyersFinalizedDealsListCall) OrderBy(orderBy string) *BuyersFinalizedDealsListCall

OrderBy sets the optional parameter "orderBy": An optional query string to sort finalized deals using the Cloud API sorting syntax (https://cloud.google.com/apis/design/design_patterns#sorting_order). If no sort order is specified, results will be returned in an arbitrary order. Supported columns for sorting are: * deal.displayName * deal.createTime * deal.updateTime * deal.flightStartTime * deal.flightEndTime * rtbMetrics.bidRequests7Days * rtbMetrics.bids7Days * rtbMetrics.adImpressions7Days * rtbMetrics.bidRate7Days * rtbMetrics.filteredBidRate7Days * rtbMetrics.mustBidRateCurrentMonth

func (*BuyersFinalizedDealsListCall) PageSize ¶
func (c *BuyersFinalizedDealsListCall) PageSize(pageSize int64) *BuyersFinalizedDealsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If requested more than 500, the server will return 500 results per page. If unspecified, the server will pick a default page size of 100.

func (*BuyersFinalizedDealsListCall) PageToken ¶
func (c *BuyersFinalizedDealsListCall) PageToken(pageToken string) *BuyersFinalizedDealsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListFinalizedDealsResponse.

func (*BuyersFinalizedDealsListCall) Pages ¶
func (c *BuyersFinalizedDealsListCall) Pages(ctx context.Context, f func(*ListFinalizedDealsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFinalizedDealsPauseCall ¶
type BuyersFinalizedDealsPauseCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsPauseCall) Context ¶
func (c *BuyersFinalizedDealsPauseCall) Context(ctx context.Context) *BuyersFinalizedDealsPauseCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsPauseCall) Do ¶
func (c *BuyersFinalizedDealsPauseCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.pause" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsPauseCall) Fields ¶
func (c *BuyersFinalizedDealsPauseCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsPauseCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsPauseCall) Header ¶
func (c *BuyersFinalizedDealsPauseCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersFinalizedDealsResumeCall ¶
type BuyersFinalizedDealsResumeCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsResumeCall) Context ¶
func (c *BuyersFinalizedDealsResumeCall) Context(ctx context.Context) *BuyersFinalizedDealsResumeCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsResumeCall) Do ¶
func (c *BuyersFinalizedDealsResumeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.resume" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsResumeCall) Fields ¶
func (c *BuyersFinalizedDealsResumeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsResumeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsResumeCall) Header ¶
func (c *BuyersFinalizedDealsResumeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersFinalizedDealsService ¶
type BuyersFinalizedDealsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFinalizedDealsService ¶
func NewBuyersFinalizedDealsService(s *Service) *BuyersFinalizedDealsService
func (*BuyersFinalizedDealsService) AddCreative ¶
func (r *BuyersFinalizedDealsService) AddCreative(deal string, addcreativerequest *AddCreativeRequest) *BuyersFinalizedDealsAddCreativeCall

AddCreative: Add creative to be used in the bidding process for a finalized deal. For programmatic guaranteed deals, it's recommended that you associate at least one approved creative with the deal before calling SetReadyToServe, to help reduce the number of bid responses filtered because they don't contain approved creatives. Creatives successfully added to a deal can be found in the Realtime-bidding Creatives API creative.deal_ids. This method only applies to programmatic guaranteed deals. Maximum number of 1000 creatives can be added to a finalized deal.

deal: Name of the finalized deal in the format of: `buyers/{accountId}/finalizedDeals/{dealId}`.
func (*BuyersFinalizedDealsService) Get ¶
func (r *BuyersFinalizedDealsService) Get(name string) *BuyersFinalizedDealsGetCall

Get: Gets a finalized deal given its name.

- name: Format: `buyers/{accountId}/finalizedDeals/{dealId}`.

func (*BuyersFinalizedDealsService) List ¶
func (r *BuyersFinalizedDealsService) List(parent string) *BuyersFinalizedDealsListCall

List: Lists finalized deals. Use the URL path "/v1alpha/buyers/{accountId}/finalizedDeals" to list finalized deals for the current buyer and its clients. Bidders can use the URL path "/v1alpha/bidders/{accountId}/finalizedDeals" to list finalized deals for the bidder, its buyers and all their clients.

parent: The buyer to list the finalized deals for, in the format: `buyers/{accountId}`. When used to list finalized deals for a bidder, its buyers and clients, in the format `bidders/{accountId}`.
func (*BuyersFinalizedDealsService) Pause ¶
func (r *BuyersFinalizedDealsService) Pause(name string, pausefinalizeddealrequest *PauseFinalizedDealRequest) *BuyersFinalizedDealsPauseCall

Pause: Pauses serving of the given finalized deal. This call only pauses the serving status, and does not affect other fields of the finalized deal. Calling this method for an already paused deal has no effect. This method only applies to programmatic guaranteed deals and preferred deals.

- name: Format: `buyers/{accountId}/finalizedDeals/{dealId}`.

func (*BuyersFinalizedDealsService) Resume ¶
func (r *BuyersFinalizedDealsService) Resume(name string, resumefinalizeddealrequest *ResumeFinalizedDealRequest) *BuyersFinalizedDealsResumeCall

Resume: Resumes serving of the given finalized deal. Calling this method for an running deal has no effect. If a deal is initially paused by the seller, calling this method will not resume serving of the deal until the seller also resumes the deal. This method only applies to programmatic guaranteed deals and preferred deals.

- name: Format: `buyers/{accountId}/finalizedDeals/{dealId}`.

func (*BuyersFinalizedDealsService) SetReadyToServe ¶
func (r *BuyersFinalizedDealsService) SetReadyToServe(deal string, setreadytoserverequest *SetReadyToServeRequest) *BuyersFinalizedDealsSetReadyToServeCall

SetReadyToServe: Sets the given finalized deal as ready to serve. By default, deals are set as ready to serve as soon as they're finalized. If you want to opt out of the default behavior, and manually indicate that deals are ready to serve, ask your Technical Account Manager to add you to the allowlist. If you choose to use this method, finalized deals belonging to the bidder and its child seats don't start serving until after you call `setReadyToServe`, and after the deals become active. For example, you can use this method to delay receiving bid requests until your creative is ready. In addition, bidders can use the URL path "/v1alpha/bidders/{accountId}/finalizedDeals/{dealId}" to set ready to serve for the finalized deals belong to itself, its child seats and all their clients. This method only applies to programmatic guaranteed deals.

deal: Format: `buyers/{accountId}/finalizedDeals/{dealId}` or `bidders/{accountId}/finalizedDeals/{dealId}`.
type BuyersFinalizedDealsSetReadyToServeCall ¶
type BuyersFinalizedDealsSetReadyToServeCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFinalizedDealsSetReadyToServeCall) Context ¶
func (c *BuyersFinalizedDealsSetReadyToServeCall) Context(ctx context.Context) *BuyersFinalizedDealsSetReadyToServeCall

Context sets the context to be used in this call's Do method.

func (*BuyersFinalizedDealsSetReadyToServeCall) Do ¶
func (c *BuyersFinalizedDealsSetReadyToServeCall) Do(opts ...googleapi.CallOption) (*FinalizedDeal, error)

Do executes the "authorizedbuyersmarketplace.buyers.finalizedDeals.setReadyToServe" call. Any non-2xx status code is an error. Response headers are in either *FinalizedDeal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFinalizedDealsSetReadyToServeCall) Fields ¶
func (c *BuyersFinalizedDealsSetReadyToServeCall) Fields(s ...googleapi.Field) *BuyersFinalizedDealsSetReadyToServeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFinalizedDealsSetReadyToServeCall) Header ¶
func (c *BuyersFinalizedDealsSetReadyToServeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsAcceptCall ¶
type BuyersProposalsAcceptCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsAcceptCall) Context ¶
func (c *BuyersProposalsAcceptCall) Context(ctx context.Context) *BuyersProposalsAcceptCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsAcceptCall) Do ¶
func (c *BuyersProposalsAcceptCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.accept" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsAcceptCall) Fields ¶
func (c *BuyersProposalsAcceptCall) Fields(s ...googleapi.Field) *BuyersProposalsAcceptCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsAcceptCall) Header ¶
func (c *BuyersProposalsAcceptCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsAddNoteCall ¶
type BuyersProposalsAddNoteCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsAddNoteCall) Context ¶
func (c *BuyersProposalsAddNoteCall) Context(ctx context.Context) *BuyersProposalsAddNoteCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsAddNoteCall) Do ¶
func (c *BuyersProposalsAddNoteCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.addNote" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsAddNoteCall) Fields ¶
func (c *BuyersProposalsAddNoteCall) Fields(s ...googleapi.Field) *BuyersProposalsAddNoteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsAddNoteCall) Header ¶
func (c *BuyersProposalsAddNoteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsCancelNegotiationCall ¶
type BuyersProposalsCancelNegotiationCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsCancelNegotiationCall) Context ¶
func (c *BuyersProposalsCancelNegotiationCall) Context(ctx context.Context) *BuyersProposalsCancelNegotiationCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsCancelNegotiationCall) Do ¶
func (c *BuyersProposalsCancelNegotiationCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.cancelNegotiation" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsCancelNegotiationCall) Fields ¶
func (c *BuyersProposalsCancelNegotiationCall) Fields(s ...googleapi.Field) *BuyersProposalsCancelNegotiationCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsCancelNegotiationCall) Header ¶
func (c *BuyersProposalsCancelNegotiationCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsDealsBatchUpdateCall ¶
type BuyersProposalsDealsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsDealsBatchUpdateCall) Context ¶
func (c *BuyersProposalsDealsBatchUpdateCall) Context(ctx context.Context) *BuyersProposalsDealsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsDealsBatchUpdateCall) Do ¶
func (c *BuyersProposalsDealsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*BatchUpdateDealsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.deals.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *BatchUpdateDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsDealsBatchUpdateCall) Fields ¶
func (c *BuyersProposalsDealsBatchUpdateCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsDealsBatchUpdateCall) Header ¶
func (c *BuyersProposalsDealsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsDealsGetCall ¶
type BuyersProposalsDealsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsDealsGetCall) Context ¶
func (c *BuyersProposalsDealsGetCall) Context(ctx context.Context) *BuyersProposalsDealsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsDealsGetCall) Do ¶
func (c *BuyersProposalsDealsGetCall) Do(opts ...googleapi.CallOption) (*Deal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.deals.get" call. Any non-2xx status code is an error. Response headers are in either *Deal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsDealsGetCall) Fields ¶
func (c *BuyersProposalsDealsGetCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsDealsGetCall) Header ¶
func (c *BuyersProposalsDealsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsDealsGetCall) IfNoneMatch ¶
func (c *BuyersProposalsDealsGetCall) IfNoneMatch(entityTag string) *BuyersProposalsDealsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersProposalsDealsListCall ¶
type BuyersProposalsDealsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsDealsListCall) Context ¶
func (c *BuyersProposalsDealsListCall) Context(ctx context.Context) *BuyersProposalsDealsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsDealsListCall) Do ¶
func (c *BuyersProposalsDealsListCall) Do(opts ...googleapi.CallOption) (*ListDealsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.deals.list" call. Any non-2xx status code is an error. Response headers are in either *ListDealsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsDealsListCall) Fields ¶
func (c *BuyersProposalsDealsListCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsDealsListCall) Header ¶
func (c *BuyersProposalsDealsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsDealsListCall) IfNoneMatch ¶
func (c *BuyersProposalsDealsListCall) IfNoneMatch(entityTag string) *BuyersProposalsDealsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersProposalsDealsListCall) PageSize ¶
func (c *BuyersProposalsDealsListCall) PageSize(pageSize int64) *BuyersProposalsDealsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If requested more than 500, the server will return 500 results per page. If unspecified, the server will pick a default page size of 100.

func (*BuyersProposalsDealsListCall) PageToken ¶
func (c *BuyersProposalsDealsListCall) PageToken(pageToken string) *BuyersProposalsDealsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListDealsResponse.

func (*BuyersProposalsDealsListCall) Pages ¶
func (c *BuyersProposalsDealsListCall) Pages(ctx context.Context, f func(*ListDealsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersProposalsDealsPatchCall ¶
type BuyersProposalsDealsPatchCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsDealsPatchCall) Context ¶
func (c *BuyersProposalsDealsPatchCall) Context(ctx context.Context) *BuyersProposalsDealsPatchCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsDealsPatchCall) Do ¶
func (c *BuyersProposalsDealsPatchCall) Do(opts ...googleapi.CallOption) (*Deal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.deals.patch" call. Any non-2xx status code is an error. Response headers are in either *Deal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsDealsPatchCall) Fields ¶
func (c *BuyersProposalsDealsPatchCall) Fields(s ...googleapi.Field) *BuyersProposalsDealsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsDealsPatchCall) Header ¶
func (c *BuyersProposalsDealsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsDealsPatchCall) UpdateMask ¶
func (c *BuyersProposalsDealsPatchCall) UpdateMask(updateMask string) *BuyersProposalsDealsPatchCall

UpdateMask sets the optional parameter "updateMask": List of fields to be updated. If empty or unspecified, the service will update all fields populated in the update request excluding the output only fields and primitive fields with default value. Note that explicit field mask is required in order to reset a primitive field back to its default value, for example, false for boolean fields, 0 for integer fields. A special field mask consisting of a single path "*" can be used to indicate full replacement(the equivalent of PUT method), updatable fields unset or unspecified in the input will be cleared or set to default value. Output only fields will be ignored regardless of the value of updateMask.

type BuyersProposalsDealsService ¶
type BuyersProposalsDealsService struct {
	// contains filtered or unexported fields
}
func NewBuyersProposalsDealsService ¶
func NewBuyersProposalsDealsService(s *Service) *BuyersProposalsDealsService
func (*BuyersProposalsDealsService) BatchUpdate ¶
func (r *BuyersProposalsDealsService) BatchUpdate(parent string, batchupdatedealsrequest *BatchUpdateDealsRequest) *BuyersProposalsDealsBatchUpdateCall

BatchUpdate: Batch updates multiple deals in the same proposal.

parent: The name of the proposal containing the deals to batch update. Format: buyers/{accountId}/proposals/{proposalId}.
func (*BuyersProposalsDealsService) Get ¶
func (r *BuyersProposalsDealsService) Get(name string) *BuyersProposalsDealsGetCall

Get: Gets a deal given its name. The deal is returned at its head revision.

- name: Format: buyers/{accountId}/proposals/{proposalId}/deals/{dealId}.

func (*BuyersProposalsDealsService) List ¶
func (r *BuyersProposalsDealsService) List(parent string) *BuyersProposalsDealsListCall

List: Lists all deals in a proposal. To retrieve only the finalized revision deals regardless if a deal is being renegotiated, see the FinalizedDeals resource.

parent: The name of the proposal containing the deals to retrieve. Format: buyers/{accountId}/proposals/{proposalId}.
func (*BuyersProposalsDealsService) Patch ¶
func (r *BuyersProposalsDealsService) Patch(nameid string, deal *Deal) *BuyersProposalsDealsPatchCall

Patch: Updates the given deal at the buyer known revision number. If the server revision has advanced since the passed-in proposal.proposal_revision an ABORTED error message will be returned. The revision number is incremented by the server whenever the proposal or its constituent deals are updated. Note: The revision number is kept at a proposal level. The buyer of the API is expected to keep track of the revision number after the last update operation and send it in as part of the next update request. This way, if there are further changes on the server (for example, seller making new updates), then the server can detect conflicts and reject the proposed changes.

name: Immutable. The unique identifier of the deal. Auto-generated by the server when a deal is created. Format: buyers/{accountId}/proposals/{proposalId}/deals/{dealId}.
type BuyersProposalsGetCall ¶
type BuyersProposalsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsGetCall) Context ¶
func (c *BuyersProposalsGetCall) Context(ctx context.Context) *BuyersProposalsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsGetCall) Do ¶
func (c *BuyersProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.get" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsGetCall) Fields ¶
func (c *BuyersProposalsGetCall) Fields(s ...googleapi.Field) *BuyersProposalsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsGetCall) Header ¶
func (c *BuyersProposalsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsGetCall) IfNoneMatch ¶
func (c *BuyersProposalsGetCall) IfNoneMatch(entityTag string) *BuyersProposalsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersProposalsListCall ¶
type BuyersProposalsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsListCall) Context ¶
func (c *BuyersProposalsListCall) Context(ctx context.Context) *BuyersProposalsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsListCall) Do ¶
func (c *BuyersProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.list" call. Any non-2xx status code is an error. Response headers are in either *ListProposalsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsListCall) Fields ¶
func (c *BuyersProposalsListCall) Fields(s ...googleapi.Field) *BuyersProposalsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsListCall) Filter ¶
func (c *BuyersProposalsListCall) Filter(filter string) *BuyersProposalsListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (https://developers.google.com/authorized-buyers/apis/guides/list-filters) Supported columns for filtering are: * displayName * dealType * updateTime * state

func (*BuyersProposalsListCall) Header ¶
func (c *BuyersProposalsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsListCall) IfNoneMatch ¶
func (c *BuyersProposalsListCall) IfNoneMatch(entityTag string) *BuyersProposalsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersProposalsListCall) PageSize ¶
func (c *BuyersProposalsListCall) PageSize(pageSize int64) *BuyersProposalsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will put a size of 500.

func (*BuyersProposalsListCall) PageToken ¶
func (c *BuyersProposalsListCall) PageToken(pageToken string) *BuyersProposalsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListProposalsResponse.

func (*BuyersProposalsListCall) Pages ¶
func (c *BuyersProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersProposalsPatchCall ¶
type BuyersProposalsPatchCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsPatchCall) Context ¶
func (c *BuyersProposalsPatchCall) Context(ctx context.Context) *BuyersProposalsPatchCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsPatchCall) Do ¶
func (c *BuyersProposalsPatchCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.patch" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsPatchCall) Fields ¶
func (c *BuyersProposalsPatchCall) Fields(s ...googleapi.Field) *BuyersProposalsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsPatchCall) Header ¶
func (c *BuyersProposalsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersProposalsPatchCall) UpdateMask ¶
func (c *BuyersProposalsPatchCall) UpdateMask(updateMask string) *BuyersProposalsPatchCall

UpdateMask sets the optional parameter "updateMask": List of fields to be updated. If empty or unspecified, the service will update all fields populated in the update request excluding the output only fields and primitive fields with default value. Note that explicit field mask is required in order to reset a primitive field back to its default value, for example, false for boolean fields, 0 for integer fields. A special field mask consisting of a single path "*" can be used to indicate full replacement(the equivalent of PUT method), updatable fields unset or unspecified in the input will be cleared or set to default value. Output only fields will be ignored regardless of the value of updateMask.

type BuyersProposalsSendRfpCall ¶
type BuyersProposalsSendRfpCall struct {
	// contains filtered or unexported fields
}
func (*BuyersProposalsSendRfpCall) Context ¶
func (c *BuyersProposalsSendRfpCall) Context(ctx context.Context) *BuyersProposalsSendRfpCall

Context sets the context to be used in this call's Do method.

func (*BuyersProposalsSendRfpCall) Do ¶
func (c *BuyersProposalsSendRfpCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "authorizedbuyersmarketplace.buyers.proposals.sendRfp" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersProposalsSendRfpCall) Fields ¶
func (c *BuyersProposalsSendRfpCall) Fields(s ...googleapi.Field) *BuyersProposalsSendRfpCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersProposalsSendRfpCall) Header ¶
func (c *BuyersProposalsSendRfpCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersProposalsService ¶
type BuyersProposalsService struct {
	Deals *BuyersProposalsDealsService
	// contains filtered or unexported fields
}
func NewBuyersProposalsService ¶
func NewBuyersProposalsService(s *Service) *BuyersProposalsService
func (*BuyersProposalsService) Accept ¶
func (r *BuyersProposalsService) Accept(name string, acceptproposalrequest *AcceptProposalRequest) *BuyersProposalsAcceptCall

Accept: Accepts the proposal at the given revision number. If the revision number in the request is behind the latest from the server, an error message will be returned. This call updates the Proposal.state from `BUYER_ACCEPTANCE_REQUESTED` to `FINALIZED`; it has no side effect if the Proposal.state is already `FINALIZED` and throws exception if the Proposal.state is not either `BUYER_ACCEPTANCE_REQUESTED` or `FINALIZED`. Accepting a proposal means the buyer understands and accepts the Proposal.terms_and_conditions proposed by the seller.

name: Name of the proposal. Format: `buyers/{accountId}/proposals/{proposalId}`.
func (*BuyersProposalsService) AddNote ¶
func (r *BuyersProposalsService) AddNote(proposal string, addnoterequest *AddNoteRequest) *BuyersProposalsAddNoteCall

AddNote: Creates a note for this proposal and sends to the seller. This method is not supported for proposals with DealType set to 'PRIVATE_AUCTION'.

proposal: Name of the proposal. Format: `buyers/{accountId}/proposals/{proposalId}`.
func (*BuyersProposalsService) CancelNegotiation ¶
func (r *BuyersProposalsService) CancelNegotiation(proposal string, cancelnegotiationrequest *CancelNegotiationRequest) *BuyersProposalsCancelNegotiationCall

CancelNegotiation: Cancels an ongoing negotiation on a proposal. This does not cancel or end serving for the deals if the proposal has been finalized. If the proposal has not been finalized before, calling this method will set the Proposal.state to `TERMINATED` and increment the Proposal.proposal_revision. If the proposal has been finalized before and is under renegotiation now, calling this method will reset the Proposal.state to `FINALIZED` and increment the Proposal.proposal_revision. This method does not support private auction proposals whose Proposal.deal_type is 'PRIVATE_AUCTION'.

proposal: Name of the proposal. Format: `buyers/{accountId}/proposals/{proposalId}`.
func (*BuyersProposalsService) Get ¶
func (r *BuyersProposalsService) Get(name string) *BuyersProposalsGetCall

Get: Gets a proposal using its resource name. The proposal is returned at the latest revision.

name: Name of the proposal. Format: `buyers/{accountId}/proposals/{proposalId}`.
func (*BuyersProposalsService) List ¶
func (r *BuyersProposalsService) List(parent string) *BuyersProposalsListCall

List: Lists proposals. A filter expression using Cloud API list filtering syntax (https://developers.google.com/authorized-buyers/apis/guides/list-filters) may be specified to filter the results.

parent: Parent that owns the collection of proposals Format: `buyers/{accountId}`.
func (*BuyersProposalsService) Patch ¶
func (r *BuyersProposalsService) Patch(nameid string, proposal *Proposal) *BuyersProposalsPatchCall

Patch: Updates the proposal at the given revision number. If the revision number in the request is behind the latest one kept in the server, an error message will be returned. See FieldMask for how to use FieldMask. Only fields specified in the UpdateProposalRequest.update_mask will be updated; Fields noted as 'Immutable' or 'Output only' yet specified in the UpdateProposalRequest.update_mask will be ignored and left unchanged. Updating a private auction proposal is only allowed for buyer private data, all other fields are immutable.

name: Immutable. The name of the proposal serving as a unique identifier. Format: buyers/{accountId}/proposals/{proposalId}.
func (*BuyersProposalsService) SendRfp ¶
func (r *BuyersProposalsService) SendRfp(buyer string, sendrfprequest *SendRfpRequest) *BuyersProposalsSendRfpCall

SendRfp: Sends a request for proposal (RFP) to a publisher to initiate the negotiation regarding certain inventory. In the RFP, buyers can specify the deal type, deal terms, start and end dates, targeting, and a message to the publisher. Once the RFP is sent, a proposal in `SELLER_REVIEW_REQUESTED` state will be created and returned in the response. The publisher may review your request and respond with detailed deals in the proposal.

buyer: The current buyer who is sending the RFP in the format: `buyers/{accountId}`.
type BuyersPublisherProfilesGetCall ¶
type BuyersPublisherProfilesGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersPublisherProfilesGetCall) Context ¶
func (c *BuyersPublisherProfilesGetCall) Context(ctx context.Context) *BuyersPublisherProfilesGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersPublisherProfilesGetCall) Do ¶
func (c *BuyersPublisherProfilesGetCall) Do(opts ...googleapi.CallOption) (*PublisherProfile, error)

Do executes the "authorizedbuyersmarketplace.buyers.publisherProfiles.get" call. Any non-2xx status code is an error. Response headers are in either *PublisherProfile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersPublisherProfilesGetCall) Fields ¶
func (c *BuyersPublisherProfilesGetCall) Fields(s ...googleapi.Field) *BuyersPublisherProfilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersPublisherProfilesGetCall) Header ¶
func (c *BuyersPublisherProfilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersPublisherProfilesGetCall) IfNoneMatch ¶
func (c *BuyersPublisherProfilesGetCall) IfNoneMatch(entityTag string) *BuyersPublisherProfilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersPublisherProfilesListCall ¶
type BuyersPublisherProfilesListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersPublisherProfilesListCall) Context ¶
func (c *BuyersPublisherProfilesListCall) Context(ctx context.Context) *BuyersPublisherProfilesListCall

Context sets the context to be used in this call's Do method.

func (*BuyersPublisherProfilesListCall) Do ¶
func (c *BuyersPublisherProfilesListCall) Do(opts ...googleapi.CallOption) (*ListPublisherProfilesResponse, error)

Do executes the "authorizedbuyersmarketplace.buyers.publisherProfiles.list" call. Any non-2xx status code is an error. Response headers are in either *ListPublisherProfilesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersPublisherProfilesListCall) Fields ¶
func (c *BuyersPublisherProfilesListCall) Fields(s ...googleapi.Field) *BuyersPublisherProfilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersPublisherProfilesListCall) Filter ¶
func (c *BuyersPublisherProfilesListCall) Filter(filter string) *BuyersPublisherProfilesListCall

Filter sets the optional parameter "filter": Optional query string using the [Cloud API list filtering] (https://developers.google.com/authorized-buyers/apis/guides/list-filters) syntax.

func (*BuyersPublisherProfilesListCall) Header ¶
func (c *BuyersPublisherProfilesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersPublisherProfilesListCall) IfNoneMatch ¶
func (c *BuyersPublisherProfilesListCall) IfNoneMatch(entityTag string) *BuyersPublisherProfilesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersPublisherProfilesListCall) PageSize ¶
func (c *BuyersPublisherProfilesListCall) PageSize(pageSize int64) *BuyersPublisherProfilesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If requested more than 500, the server will return 500 results per page. If unspecified, the server will pick a default page size of 100.

func (*BuyersPublisherProfilesListCall) PageToken ¶
func (c *BuyersPublisherProfilesListCall) PageToken(pageToken string) *BuyersPublisherProfilesListCall

PageToken sets the optional parameter "pageToken": The page token as returned from a previous ListPublisherProfilesResponse.

func (*BuyersPublisherProfilesListCall) Pages ¶
func (c *BuyersPublisherProfilesListCall) Pages(ctx context.Context, f func(*ListPublisherProfilesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersPublisherProfilesService ¶
type BuyersPublisherProfilesService struct {
	// contains filtered or unexported fields
}
func NewBuyersPublisherProfilesService ¶
func NewBuyersPublisherProfilesService(s *Service) *BuyersPublisherProfilesService
func (*BuyersPublisherProfilesService) Get ¶
func (r *BuyersPublisherProfilesService) Get(name string) *BuyersPublisherProfilesGetCall

Get: Gets the requested publisher profile by name.

name: Name of the publisher profile. Format: `buyers/{buyerId}/publisherProfiles/{publisherProfileId}`.
func (*BuyersPublisherProfilesService) List ¶
func (r *BuyersPublisherProfilesService) List(parent string) *BuyersPublisherProfilesListCall

List: Lists publisher profiles. The returned publisher profiles aren't in any defined order. The order of the results might change. A new publisher profile can appear in any place in the list of returned results.

parent: Parent that owns the collection of publisher profiles Format: `buyers/{buyerId}`.
type BuyersService ¶
type BuyersService struct {
	AuctionPackages *BuyersAuctionPackagesService

	Clients *BuyersClientsService

	DataSegments *BuyersDataSegmentsService

	FinalizedDeals *BuyersFinalizedDealsService

	Proposals *BuyersProposalsService

	PublisherProfiles *BuyersPublisherProfilesService
	// contains filtered or unexported fields
}
func NewBuyersService ¶
func NewBuyersService(s *Service) *BuyersService
type CancelNegotiationRequest ¶
type CancelNegotiationRequest struct {
}

CancelNegotiationRequest: Request to cancel an ongoing negotiation.

type Client ¶
type Client struct {
	// DisplayName: Required. Display name shown to publishers. Must be unique for
	// clients without partnerClientId specified. Maximum length of 255 characters
	// is allowed.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Output only. The resource name of the client. Format:
	// `buyers/{accountId}/clients/{clientAccountId}`
	Name string `json:"name,omitempty"`
	// PartnerClientId: Arbitrary unique identifier provided by the buyer. This
	// field can be used to associate a client with an identifier in the namespace
	// of the buyer, lookup clients by that identifier and verify whether an
	// Authorized Buyers account of the client already exists. If present, must be
	// unique across all the clients.
	PartnerClientId string `json:"partnerClientId,omitempty"`
	// Role: Required. The role assigned to the client. Each role implies a set of
	// permissions granted to the client.
	//
	// Possible values:
	//   "CLIENT_ROLE_UNSPECIFIED" - A placeholder for an undefined client role.
	// This value should never be specified in user input for create or update
	// method, otherwise an error will be returned.
	//   "CLIENT_DEAL_VIEWER" - Users associated with this client role can only
	// view proposals and deals in the Marketplace UI. They cannot negotiate or
	// approve proposals and deals sent from publishers or send RFP to publishers.
	//   "CLIENT_DEAL_NEGOTIATOR" - Users associated with this client role can view
	// and negotiate on the proposals and deals in the Marketplace UI sent from
	// publishers and send RFP to publishers, but cannot approve the proposals and
	// deals by themselves. The buyer can approve the proposals and deals on behalf
	// of the client.
	//   "CLIENT_DEAL_APPROVER" - Users associated with this client role can view,
	// negotiate and approve proposals and deals in the Marketplace UI and send RFP
	// to publishers.
	Role string `json:"role,omitempty"`
	// SellerVisible: Whether the client will be visible to sellers.
	SellerVisible bool `json:"sellerVisible,omitempty"`
	// State: Output only. The state of the client.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - A placeholder for an undefined client state. Should
	// not be used.
	//   "ACTIVE" - A client that is currently active and allowed to access the
	// Authorized Buyers UI.
	//   "INACTIVE" - A client that is currently inactive and not allowed to access
	// the Authorized Buyers UI.
	State string `json:"state,omitempty"`

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

Client: A client represents an agency, a brand, or an advertiser customer of the buyer. Based on the client's role, its client users will have varying levels of restricted access to the Marketplace and certain other sections of the Authorized Buyers UI.

func (Client) MarshalJSON ¶
func (s Client) MarshalJSON() ([]byte, error)
type ClientUser ¶
type ClientUser struct {
	// Email: Required. The client user's email address that has to be unique
	// across all users for the same client.
	Email string `json:"email,omitempty"`
	// Name: Output only. The resource name of the client user. Format:
	// `buyers/{accountId}/clients/{clientAccountId}/users/{userId}`
	Name string `json:"name,omitempty"`
	// State: Output only. The state of the client user.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - A placeholder for an undefined user state.
	//   "INVITED" - A user who was created but hasn't accepted the invitation yet,
	// not allowed to access the Authorized Buyers UI.
	//   "ACTIVE" - A user that is currently active and allowed to access the
	// Authorized Buyers UI.
	//   "INACTIVE" - A user that is currently inactive and not allowed to access
	// the Authorized Buyers UI.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

ClientUser: A user of a client who has restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the associated client.

func (ClientUser) MarshalJSON ¶
func (s ClientUser) MarshalJSON() ([]byte, error)
type Contact ¶
type Contact struct {
	// DisplayName: The display_name of the contact.
	DisplayName string `json:"displayName,omitempty"`
	// Email: Email address for the contact.
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

Contact: Contains information on how a buyer or seller can be reached.

func (Contact) MarshalJSON ¶
func (s Contact) MarshalJSON() ([]byte, error)
type CreativeRequirements ¶
type CreativeRequirements struct {
	// CreativeFormat: Output only. The format of the creative, only applicable for
	// programmatic guaranteed and preferred deals.
	//
	// Possible values:
	//   "CREATIVE_FORMAT_UNSPECIFIED" - A placeholder for an unspecified creative
	// format.
	//   "DISPLAY" - Banner creatives such as image or HTML5 assets.
	//   "VIDEO" - Video creatives that can be played in a video player.
	//   "AUDIO" - Audio creatives that can play during audio content or point to a
	// third party ad server.
	CreativeFormat string `json:"creativeFormat,omitempty"`
	// CreativePreApprovalPolicy: Output only. Specifies the creative pre-approval
	// policy.
	//
	// Possible values:
	//   "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED" - A placeholder for an
	// undefined creative pre-approval policy.
	//   "SELLER_PRE_APPROVAL_REQUIRED" - The seller needs to approve each creative
	// before it can serve.
	//   "SELLER_PRE_APPROVAL_NOT_REQUIRED" - The seller does not need to approve
	// each creative before it can serve.
	CreativePreApprovalPolicy string `json:"creativePreApprovalPolicy,omitempty"`
	// CreativeSafeFrameCompatibility: Output only. Specifies whether the creative
	// is safeFrame compatible.
	//
	// Possible values:
	//   "CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED" - A placeholder for an
	// undefined creative safe-frame compatibility.
	//   "COMPATIBLE" - The creatives need to be compatible with the safe frame
	// option.
	//   "INCOMPATIBLE" - The creatives can be incompatible with the safe frame
	// option.
	CreativeSafeFrameCompatibility string `json:"creativeSafeFrameCompatibility,omitempty"`
	// MaxAdDurationMs: Output only. The max duration of the video creative in
	// milliseconds. only applicable for deals with video creatives.
	MaxAdDurationMs int64 `json:"maxAdDurationMs,omitempty,string"`
	// ProgrammaticCreativeSource: Output only. Specifies the creative source for
	// programmatic deals. PUBLISHER means creative is provided by seller and
	// ADVERTISER means creative is provided by the buyer.
	//
	// Possible values:
	//   "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED" - A placeholder for an
	// undefined programmatic creative source.
	//   "ADVERTISER" - The advertiser provides the creatives.
	//   "PUBLISHER" - The publisher provides the creatives to be served.
	ProgrammaticCreativeSource string `json:"programmaticCreativeSource,omitempty"`
	// SkippableAdType: Output only. Skippable video ads allow viewers to skip ads
	// after 5 seconds. Only applicable for deals with video creatives.
	//
	// Possible values:
	//   "SKIPPABLE_AD_TYPE_UNSPECIFIED" - A placeholder for an unspecified
	// skippable ad type.
	//   "SKIPPABLE" - Video ad that can be skipped after 5 seconds. This value
	// will appear in RTB bid requests as
	// SkippableBidRequestType::REQUIRE_SKIPPABLE.
	//   "INSTREAM_SELECT" - Video ad that can be skipped after 5 seconds, and is
	// counted as engaged view after 30 seconds. The creative is hosted on YouTube
	// only, and viewcount of the YouTube video increments after the engaged view.
	// This value will appear in RTB bid requests as
	// SkippableBidRequestType::REQUIRE_SKIPPABLE.
	//   "NOT_SKIPPABLE" - This video ad is not skippable. This value will appear
	// in RTB bid requests as SkippableBidRequestType::BLOCK_SKIPPABLE.
	//   "ANY" - This video ad can be skipped after 5 seconds or not-skippable.
	// This value will appear in RTB bid requests as
	// SkippableBidRequestType::ALLOW_SKIPPABLE.
	SkippableAdType string `json:"skippableAdType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreativeFormat") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeFormat") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreativeRequirements: Message captures data about the creatives in the deal.

func (CreativeRequirements) MarshalJSON ¶
func (s CreativeRequirements) MarshalJSON() ([]byte, error)
type CriteriaTargeting ¶
type CriteriaTargeting struct {
	// ExcludedCriteriaIds: A list of numeric IDs to be excluded.
	ExcludedCriteriaIds googleapi.Int64s `json:"excludedCriteriaIds,omitempty"`
	// TargetedCriteriaIds: A list of numeric IDs to be included.
	TargetedCriteriaIds googleapi.Int64s `json:"targetedCriteriaIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedCriteriaIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedCriteriaIds") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CriteriaTargeting: Generic targeting used for targeting dimensions that contains a list of included and excluded numeric IDs. This cannot be filtered using list filter syntax.

func (CriteriaTargeting) MarshalJSON ¶
func (s CriteriaTargeting) MarshalJSON() ([]byte, error)
type CuratedPackage ¶
added in v0.259.0
type CuratedPackage struct {
	// AccessSettings: Required. Settings for controlling access to the curated
	// package. Access to this curated package is limited to the allowlisted media
	// planners and the creator. Buyers and bidders can not be allowlisted for or
	// have direct access to this resource.
	AccessSettings *AccessControlSettings `json:"accessSettings,omitempty"`
	// CreateTime: Output only. The timestamp when the curated package was created.
	// Can be used to filter the response of the curatedPackages.list method.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Optional. A description of the curated package, provided by the
	// curator.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name assigned to the curated package by
	// the curator. Can be used to filter the response of the curatedPackages.list
	// method.
	DisplayName string `json:"displayName,omitempty"`
	// FeeCpm: Optional. The CPM fee charged by the curator to buyers using this
	// curated package. Can be used to filter the response of the
	// curatedPackages.list method.
	FeeCpm *Money `json:"feeCpm,omitempty"`
	// FloorPriceCpm: Optional. The minimum CPM a buyer has to bid to participate
	// in auctions for inventory in this curated package. Can be used to filter the
	// response of the curatedPackages.list method.
	FloorPriceCpm *Money `json:"floorPriceCpm,omitempty"`
	// Name: Identifier. The unique resource name for the curated package. Format:
	// `curators/{accountId}/curatedPackages/{curatedPackageId}`
	Name string `json:"name,omitempty"`
	// State: Output only. The state of the curated package. Can be used to filter
	// the response of the curatedPackages.list method.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value.
	//   "ACTIVE" - The curated package is active.
	//   "INACTIVE" - The curated package is inactive.
	State string `json:"state,omitempty"`
	// Targeting: Optional. Targeting criteria for the curated package.
	Targeting *PackageTargeting `json:"targeting,omitempty"`
	// UpdateTime: Output only. The timestamp when the curated package was last
	// updated. Can be used to filter the response of the curatedPackages.list
	// method.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessSettings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessSettings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CuratedPackage: Represents a curated package of inventory created and managed by a Curator.

func (CuratedPackage) MarshalJSON ¶
added in v0.259.0
func (s CuratedPackage) MarshalJSON() ([]byte, error)
type CuratorsCuratedPackagesActivateCall ¶
added in v0.259.0
type CuratorsCuratedPackagesActivateCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesActivateCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesActivateCall) Context(ctx context.Context) *CuratorsCuratedPackagesActivateCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesActivateCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesActivateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.activate" call. Any non-2xx status code is an error. Response headers are in either *CuratedPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesActivateCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesActivateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesActivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesActivateCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesActivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CuratorsCuratedPackagesCreateCall ¶
added in v0.259.0
type CuratorsCuratedPackagesCreateCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesCreateCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesCreateCall) Context(ctx context.Context) *CuratorsCuratedPackagesCreateCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesCreateCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesCreateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.create" call. Any non-2xx status code is an error. Response headers are in either *CuratedPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesCreateCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesCreateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesCreateCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CuratorsCuratedPackagesDeactivateCall ¶
added in v0.259.0
type CuratorsCuratedPackagesDeactivateCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesDeactivateCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesDeactivateCall) Context(ctx context.Context) *CuratorsCuratedPackagesDeactivateCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesDeactivateCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesDeactivateCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.deactivate" call. Any non-2xx status code is an error. Response headers are in either *CuratedPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesDeactivateCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesDeactivateCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesDeactivateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesDeactivateCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesDeactivateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CuratorsCuratedPackagesGetCall ¶
added in v0.259.0
type CuratorsCuratedPackagesGetCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesGetCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesGetCall) Context(ctx context.Context) *CuratorsCuratedPackagesGetCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesGetCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesGetCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.get" call. Any non-2xx status code is an error. Response headers are in either *CuratedPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesGetCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesGetCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesGetCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CuratorsCuratedPackagesGetCall) IfNoneMatch ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesGetCall) IfNoneMatch(entityTag string) *CuratorsCuratedPackagesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type CuratorsCuratedPackagesListCall ¶
added in v0.259.0
type CuratorsCuratedPackagesListCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesListCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Context(ctx context.Context) *CuratorsCuratedPackagesListCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesListCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Do(opts ...googleapi.CallOption) (*ListCuratedPackagesResponse, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.list" call. Any non-2xx status code is an error. Response headers are in either *ListCuratedPackagesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesListCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesListCall) Filter ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Filter(filter string) *CuratorsCuratedPackagesListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (/authorized-buyers/apis/guides/list-filters). Supported columns for filtering are: * displayName * createTime * updateTime * state * feeCpm.currencyCode * feeCpm.units * feeCpm.nanos * floorPriceCpm.currencyCode * floorPriceCpm.units * floorPriceCpm.nanos

func (*CuratorsCuratedPackagesListCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CuratorsCuratedPackagesListCall) IfNoneMatch ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) IfNoneMatch(entityTag string) *CuratorsCuratedPackagesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*CuratorsCuratedPackagesListCall) PageSize ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) PageSize(pageSize int64) *CuratorsCuratedPackagesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. Max allowed page size is 500. If unspecified, the server will default to 500.

func (*CuratorsCuratedPackagesListCall) PageToken ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) PageToken(pageToken string) *CuratorsCuratedPackagesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCuratedPackages` call. Provide this to retrieve the subsequent page.

func (*CuratorsCuratedPackagesListCall) Pages ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesListCall) Pages(ctx context.Context, f func(*ListCuratedPackagesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CuratorsCuratedPackagesPatchCall ¶
added in v0.259.0
type CuratorsCuratedPackagesPatchCall struct {
	// contains filtered or unexported fields
}
func (*CuratorsCuratedPackagesPatchCall) Context ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesPatchCall) Context(ctx context.Context) *CuratorsCuratedPackagesPatchCall

Context sets the context to be used in this call's Do method.

func (*CuratorsCuratedPackagesPatchCall) Do ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesPatchCall) Do(opts ...googleapi.CallOption) (*CuratedPackage, error)

Do executes the "authorizedbuyersmarketplace.curators.curatedPackages.patch" call. Any non-2xx status code is an error. Response headers are in either *CuratedPackage.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CuratorsCuratedPackagesPatchCall) Fields ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesPatchCall) Fields(s ...googleapi.Field) *CuratorsCuratedPackagesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*CuratorsCuratedPackagesPatchCall) Header ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*CuratorsCuratedPackagesPatchCall) UpdateMask ¶
added in v0.259.0
func (c *CuratorsCuratedPackagesPatchCall) UpdateMask(updateMask string) *CuratorsCuratedPackagesPatchCall

UpdateMask sets the optional parameter "updateMask": List of fields to be updated. If empty or unspecified, the service will update all fields populated in the update request excluding the output only fields and primitive fields with default value. Note that explicit field mask is required in order to reset a primitive field back to its default value, for example, false for boolean fields, 0 for integer fields. A special field mask consisting of a single path "*" can be used to indicate full replacement (the equivalent of PUT method), updatable fields unset or unspecified in the input will be cleared or set to default value. Output only fields will be ignored regardless of the value of updateMask.

type CuratorsCuratedPackagesService ¶
added in v0.259.0
type CuratorsCuratedPackagesService struct {
	// contains filtered or unexported fields
}
func NewCuratorsCuratedPackagesService ¶
added in v0.259.0
func NewCuratorsCuratedPackagesService(s *Service) *CuratorsCuratedPackagesService
func (*CuratorsCuratedPackagesService) Activate ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) Activate(name string, activatecuratedpackagerequest *ActivateCuratedPackageRequest) *CuratorsCuratedPackagesActivateCall

Activate: Activates an existing curated package.

name: The name of the curated package to activate. Format: `curators/{accountId}/curatedPackages/{curatedPackageId}`.
func (*CuratorsCuratedPackagesService) Create ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) Create(parent string, curatedpackage *CuratedPackage) *CuratorsCuratedPackagesCreateCall

Create: Creates a new curated package.

parent: The parent curator account where this curated package will be created. Format: `curators/{accountId}`.
func (*CuratorsCuratedPackagesService) Deactivate ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) Deactivate(name string, deactivatecuratedpackagerequest *DeactivateCuratedPackageRequest) *CuratorsCuratedPackagesDeactivateCall

Deactivate: Deactivates an existing curated package.

name: The name of the curated package to deactivate. Format: `curators/{accountId}/curatedPackages/{curatedPackageId}`.
func (*CuratorsCuratedPackagesService) Get ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) Get(name string) *CuratorsCuratedPackagesGetCall

Get: Gets a curated package given its resource name.

name: The name of the curated package to retrieve. Format: `curators/{accountId}/curatedPackages/{curatedPackageId}`.
func (*CuratorsCuratedPackagesService) List ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) List(parent string) *CuratorsCuratedPackagesListCall

List: Lists curated packages owned by the specified curator.

parent: The parent curator account which owns this collection of curated packages. Format: `curators/{accountId}`.
func (*CuratorsCuratedPackagesService) Patch ¶
added in v0.259.0
func (r *CuratorsCuratedPackagesService) Patch(name string, curatedpackage *CuratedPackage) *CuratorsCuratedPackagesPatchCall

Patch: Updates an existing curated package.

name: Identifier. The unique resource name for the curated package. Format: `curators/{accountId}/curatedPackages/{curatedPackageId}`.
type CuratorsService ¶
added in v0.259.0
type CuratorsService struct {
	CuratedPackages *CuratorsCuratedPackagesService
	// contains filtered or unexported fields
}
func NewCuratorsService ¶
added in v0.259.0
func NewCuratorsService(s *Service) *CuratorsService
type DataSegment ¶
type DataSegment struct {
	// CpmFee: Optional. A fixed fee charged per thousand impressions. Once set,
	// the currency code cannot be changed.
	CpmFee *Money `json:"cpmFee,omitempty"`
	// CreateTime: Output only. Time the data segment was created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Immutable. Identifier. The unique identifier for the data segment.
	// Account ID corresponds to the account ID that created the segment. v1alpha
	// format: `buyers/{accountId}/dataSegments/{curatorDataSegmentId}` v1beta
	// format: `curators/{curatorAccountId}/dataSegments/{curatorDataSegmentId}`
	Name string `json:"name,omitempty"`
	// State: Output only. The state of the data segment.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value.
	//   "ACTIVE" - The data segment is active.
	//   "INACTIVE" - The data segment is inactive.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. Time the data segment was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CpmFee") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CpmFee") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DataSegment: Defines an identifier for a segment of inventory that can be targeted by curators or media planners in the deals or auction packages UI. Curation of inventory is done by curators on external platforms.

func (DataSegment) MarshalJSON ¶
func (s DataSegment) MarshalJSON() ([]byte, error)
type DayPart ¶
type DayPart struct {
	// DayOfWeek: Day of week for the period.
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
	// EndTime: Hours in 24 hour time between 0 and 24, inclusive. Note: 24 is
	// logically equivalent to 0, but is supported since in some cases there may
	// need to be differentiation made between midnight on one day and midnight on
	// the next day. Accepted values for minutes are [0, 15, 30, 45]. 0 is the only
	// acceptable minute value for hour 24. Seconds and nanos are ignored.
	EndTime *TimeOfDay `json:"endTime,omitempty"`
	// StartTime: Hours in 24 hour time between 0 and 24, inclusive. Note: 24 is
	// logically equivalent to 0, but is supported since in some cases there may
	// need to be differentiation made between midnight on one day and midnight on
	// the next day. Accepted values for minutes are [0, 15, 30, 45]. 0 is the only
	// acceptable minute value for hour 24. Seconds and nanos are ignored.
	StartTime *TimeOfDay `json:"startTime,omitempty"`
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

DayPart: Defines targeting for a period of time on a specific week day.

func (DayPart) MarshalJSON ¶
func (s DayPart) MarshalJSON() ([]byte, error)
type DayPartTargeting ¶
type DayPartTargeting struct {
	// DayParts: The targeted weekdays and times
	DayParts []*DayPart `json:"dayParts,omitempty"`
	// TimeZoneType: The time zone type of the day parts
	//
	// Possible values:
	//   "TIME_ZONE_TYPE_UNSPECIFIED" - Default value. This field is unused.
	//   "SELLER" - The publisher's time zone
	//   "USER" - The user's time zone
	TimeZoneType string `json:"timeZoneType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DayParts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DayParts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DayPartTargeting: Represents Daypart targeting.

func (DayPartTargeting) MarshalJSON ¶
func (s DayPartTargeting) MarshalJSON() ([]byte, error)
type DeactivateClientRequest ¶
type DeactivateClientRequest struct {
}

DeactivateClientRequest: Request message for disabling a client.

type DeactivateClientUserRequest ¶
type DeactivateClientUserRequest struct {
}

DeactivateClientUserRequest: Request message for deactivating a client user.

type DeactivateCuratedPackageRequest ¶
added in v0.259.0
type DeactivateCuratedPackageRequest struct {
}

DeactivateCuratedPackageRequest: Request message for DeactivateCuratedPackage.

type DeactivateDataSegmentRequest ¶
type DeactivateDataSegmentRequest struct {
}

DeactivateDataSegmentRequest: Request message for deactivating a data segment

type Deal ¶
type Deal struct {
	// BilledBuyer: Output only. When the client field is populated, this field
	// refers to the buyer who creates and manages the client buyer and gets billed
	// on behalf of the client buyer; when the buyer field is populated, this field
	// is the same value as buyer; when the deal belongs to a media planner
	// account, this field will be empty. Format : `buyers/{buyerAccountId}`
	BilledBuyer string `json:"billedBuyer,omitempty"`
	// Buyer: Output only. Refers to a buyer in Real-time Bidding API's Buyer
	// resource. Format: `buyers/{buyerAccountId}`
	Buyer string `json:"buyer,omitempty"`
	// BuyerPermissionType: Output only. The buyer permission type of the deal.
	//
	// Possible values:
	//   "BUYER_PERMISSION_TYPE_UNSPECIFIED" - A placeholder for an undefined buyer
	// permission type.
	//   "NEGOTIATOR_ONLY" - Only the [Deal.negotiating_buyer] can transact on the
	// deal.
	//   "BIDDER" - All buyers under the [Deal.negotiating_buyer]'s bidder can
	// transact on the deal.
	BuyerPermissionType string `json:"buyerPermissionType,omitempty"`
	// Client: Output only. Refers to a Client. Format:
	// `buyers/{buyerAccountId}/clients/{clientAccountid}`
	Client string `json:"client,omitempty"`
	// CreateTime: Output only. The time of the deal creation.
	CreateTime string `json:"createTime,omitempty"`
	// CreativeRequirements: Output only. Metadata about the creatives of this
	// deal.
	CreativeRequirements *CreativeRequirements `json:"creativeRequirements,omitempty"`
	// DealType: Output only. Type of deal.
	//
	// Possible values:
	//   "DEAL_TYPE_UNSPECIFIED" - Default, unspecified deal type.
	//   "PREFERRED_DEAL" - Preferred deals.
	//   "PRIVATE_AUCTION" - Private auction deals.
	//   "PROGRAMMATIC_GUARANTEED" - Programmatic guaranteed deals.
	DealType string `json:"dealType,omitempty"`
	// DeliveryControl: Output only. Specifies the pacing set by the publisher.
	DeliveryControl *DeliveryControl `json:"deliveryControl,omitempty"`
	// Description: Output only. Free text description for the deal terms.
	Description string `json:"description,omitempty"`
	// DisplayName: Output only. The name of the deal. Maximum length of 255
	// unicode characters is allowed. Control characters are not allowed. Buyers
	// cannot update this field. Note: Not to be confused with name, which is a
	// unique identifier of the deal.
	DisplayName string `json:"displayName,omitempty"`
	// EligibleSeatIds: Output only. If set, this field contains the list of DSP
	// specific seat ids set by media planners that are eligible to transact on
	// this deal. The seat ID is in the calling DSP's namespace.
	EligibleSeatIds []string `json:"eligibleSeatIds,omitempty"`
	// EstimatedGrossSpend: Specified by buyers in request for proposal (RFP) to
	// notify publisher the total estimated spend for the proposal. Publishers will
	// receive this information and send back proposed deals accordingly.
	EstimatedGrossSpend *Money `json:"estimatedGrossSpend,omitempty"`
	// FlightEndTime: Proposed flight end time of the deal. This will generally be
	// stored in a granularity of a second. A value is not necessary for Private
	// Auction deals.
	FlightEndTime string `json:"flightEndTime,omitempty"`
	// FlightStartTime: Proposed flight start time of the deal. This will generally
	// be stored in the granularity of one second since deal serving starts at
	// seconds boundary. Any time specified with more granularity (for example, in
	// milliseconds) will be truncated towards the start of time in seconds.
	FlightStartTime string `json:"flightStartTime,omitempty"`
	// MediaPlanner: Output only. Refers to a buyer in Real-time Bidding API's
	// Buyer resource. This field represents a media planner (For example, agency
	// or big advertiser).
	MediaPlanner *MediaPlanner `json:"mediaPlanner,omitempty"`
	// Name: Immutable. The unique identifier of the deal. Auto-generated by the
	// server when a deal is created. Format:
	// buyers/{accountId}/proposals/{proposalId}/deals/{dealId}
	Name string `json:"name,omitempty"`
	// PreferredDealTerms: The terms for preferred deals.
	PreferredDealTerms *PreferredDealTerms `json:"preferredDealTerms,omitempty"`
	// PrivateAuctionTerms: The terms for private auction deals.
	PrivateAuctionTerms *PrivateAuctionTerms `json:"privateAuctionTerms,omitempty"`
	// ProgrammaticGuaranteedTerms: The terms for programmatic guaranteed deals.
	ProgrammaticGuaranteedTerms *ProgrammaticGuaranteedTerms `json:"programmaticGuaranteedTerms,omitempty"`
	// ProposalRevision: Output only. The revision number for the proposal and is
	// the same value as proposal.proposal_revision. Each update to deal causes the
	// proposal revision number to auto-increment. The buyer keeps track of the
	// last revision number they know of and pass it in when making an update. If
	// the head revision number on the server has since incremented, then an
	// ABORTED error is returned during the update operation to let the buyer know
	// that a subsequent update was made.
	ProposalRevision int64 `json:"proposalRevision,omitempty,string"`
	// PublisherProfile: Immutable. Reference to the seller on the deal. Format:
	// `buyers/{buyerAccountId}/publisherProfiles/{publisherProfileId}`
	PublisherProfile string `json:"publisherProfile,omitempty"`
	// SellerTimeZone: Output only. Time zone of the seller used to mark the
	// boundaries of a day for daypart targeting and CPD billing.
	SellerTimeZone *TimeZone `json:"sellerTimeZone,omitempty"`
	// Targeting: Specifies the subset of inventory targeted by the deal. Can be
	// updated by the buyer before the deal is finalized.
	Targeting *MarketplaceTargeting `json:"targeting,omitempty"`
	// UpdateTime: Output only. The time when the deal was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BilledBuyer") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BilledBuyer") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Deal: A deal represents a segment of inventory for displaying ads that contains the terms and targeting information that is used for serving as well as the deal stats and status. Note: A proposal may contain multiple deals.

func (Deal) MarshalJSON ¶
func (s Deal) MarshalJSON() ([]byte, error)
type DealPausingInfo ¶
type DealPausingInfo struct {
	// PauseReason: The reason for the pausing of the deal; empty for active deals.
	PauseReason string `json:"pauseReason,omitempty"`
	// PauseRole: The party that first paused the deal; unspecified for active
	// deals.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	PauseRole string `json:"pauseRole,omitempty"`
	// PausingConsented: Whether pausing is consented between buyer and seller for
	// the deal.
	PausingConsented bool `json:"pausingConsented,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PauseReason") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PauseReason") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DealPausingInfo: Information related to deal pausing.

func (DealPausingInfo) MarshalJSON ¶
func (s DealPausingInfo) MarshalJSON() ([]byte, error)
type DeliveryControl ¶
type DeliveryControl struct {
	// CompanionDeliveryType: Output only. Specifies roadblocking in a main
	// companion lineitem.
	//
	// Possible values:
	//   "COMPANION_DELIVERY_TYPE_UNSPECIFIED" - A placeholder for an unspecified
	// companion delivery type.
	//   "DELIVERY_OPTIONAL" - Companions are not required to serve a creative set.
	// The creative set can serve an inventory that has zero or more matching
	// companions.
	//   "DELIVERY_AT_LEAST_ONE" - At least one companion must be served in order
	// for the creative set to be used.
	//   "DELIVERY_ALL" - All companions in the set must be served in order for the
	// creative set to be used. This can still serve to inventory that has more
	// companions than can be filled.
	CompanionDeliveryType string `json:"companionDeliveryType,omitempty"`
	// CreativeRotationType: Output only. Specifies strategy to use for selecting a
	// creative when multiple creatives of the same size are available.
	//
	// Possible values:
	//   "CREATIVE_ROTATION_TYPE_UNSPECIFIED" - Creatives are displayed roughly the
	// same number of times over the duration of the deal.
	//   "ROTATION_EVEN" - Creatives are displayed roughly the same number of times
	// over the duration of the deal.
	//   "ROTATION_OPTIMIZED" - Creatives are served roughly proportionally to
	// their performance.
	//   "ROTATION_MANUAL" - Creatives are served roughly proportionally to their
	// weights.
	//   "ROTATION_SEQUENTIAL" - Creatives are served exactly in sequential order,
	// also known as Storyboarding.
	CreativeRotationType string `json:"creativeRotationType,omitempty"`
	// DeliveryRateType: Output only. Specifies how the impression delivery will be
	// paced.
	//
	// Possible values:
	//   "DELIVERY_RATE_TYPE_UNSPECIFIED" - A placeholder for an undefined delivery
	// rate type.
	//   "EVENLY" - Impressions are served uniformly over the life of the deal.
	//   "FRONT_LOADED" - Impressions are served front-loaded.
	//   "AS_FAST_AS_POSSIBLE" - Impressions are served as fast as possible.
	DeliveryRateType string `json:"deliveryRateType,omitempty"`
	// FrequencyCap: Output only. Specifies any frequency caps. Cannot be filtered
	// within ListDealsRequest.
	FrequencyCap []*FrequencyCap `json:"frequencyCap,omitempty"`
	// RoadblockingType: Output only. Specifies the roadblocking type in display
	// creatives.
	//
	// Possible values:
	//   "ROADBLOCKING_TYPE_UNSPECIFIED" - A placeholder for an unspecified
	// roadblocking type.
	//   "ONLY_ONE" - Only one creative from a deal can serve per ad request.
	// https://support.google.com/admanager/answer/177277.
	//   "ONE_OR_MORE" - Any number of creatives from a deal can serve together per
	// ad request.
	//   "AS_MANY_AS_POSSIBLE" - As many creatives from a deal as can fit on a page
	// will serve. This could mean anywhere from one to all of a deal's creatives
	// given the size constraints of ad slots on a page.
	//   "ALL_ROADBLOCK" - All or none of the creatives from a deal will serve.
	//   "CREATIVE_SET" - A main/companion creative set roadblocking type.
	RoadblockingType string `json:"roadblockingType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CompanionDeliveryType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CompanionDeliveryType") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeliveryControl: Message contains details about how the deal will be paced.

func (DeliveryControl) MarshalJSON ¶
func (s DeliveryControl) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type FinalizedDeal ¶
type FinalizedDeal struct {
	// Deal: A copy of the Deal made upon finalization. During renegotiation, this
	// will reflect the last finalized deal before renegotiation was initiated.
	Deal *Deal `json:"deal,omitempty"`
	// DealPausingInfo: Information related to deal pausing for the deal.
	DealPausingInfo *DealPausingInfo `json:"dealPausingInfo,omitempty"`
	// DealServingStatus: Serving status of the deal.
	//
	// Possible values:
	//   "DEAL_SERVING_STATUS_UNSPECIFIED" - Unspecified.
	//   "ACTIVE" - The deal is actively serving or ready to serve when the start
	// date is reached.
	//   "ENDED" - The deal serving has ended.
	//   "PAUSED_BY_BUYER" - The deal serving is paused by buyer.
	//   "PAUSED_BY_SELLER" - The deal serving is paused by seller.
	DealServingStatus string `json:"dealServingStatus,omitempty"`
	// Name: The resource name of the finalized deal. Format:
	// `buyers/{accountId}/finalizedDeals/{finalizedDealId}`
	Name string `json:"name,omitempty"`
	// ReadyToServe: Whether the Programmatic Guaranteed deal is ready for serving.
	ReadyToServe bool `json:"readyToServe,omitempty"`
	// RtbMetrics: Real-time bidding metrics for this deal.
	RtbMetrics *RtbMetrics `json:"rtbMetrics,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Deal") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deal") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FinalizedDeal: A finalized deal is a snapshot of the deal when both buyer and seller accept the deal. The buyer or seller can update the deal after it's been finalized and renegotiate on the deal targeting, terms and other fields, while at the same time the finalized snapshot of the deal can still be retrieved using this API. The finalized deal contains a copy of the deal as it existed when most recently finalized, as well as fields related to deal serving such as pause/resume status, RTB metrics, and more.

func (FinalizedDeal) MarshalJSON ¶
func (s FinalizedDeal) MarshalJSON() ([]byte, error)
type FirstPartyMobileApplicationTargeting ¶
type FirstPartyMobileApplicationTargeting struct {
	// ExcludedAppIds: A list of application IDs to be excluded.
	ExcludedAppIds []string `json:"excludedAppIds,omitempty"`
	// TargetedAppIds: A list of application IDs to be included.
	TargetedAppIds []string `json:"targetedAppIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedAppIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedAppIds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FirstPartyMobileApplicationTargeting: Represents a list of targeted and excluded mobile application IDs that publishers own. Android App ID, for example, com.google.android.apps.maps, can be found in Google Play Store URL. iOS App ID (which is a number) can be found at the end of iTunes store URL. First party mobile applications is either included or excluded.

func (FirstPartyMobileApplicationTargeting) MarshalJSON ¶
func (s FirstPartyMobileApplicationTargeting) MarshalJSON() ([]byte, error)
type FrequencyCap ¶
type FrequencyCap struct {
	// MaxImpressions: The maximum number of impressions that can be served to a
	// user within the specified time period.
	MaxImpressions int64 `json:"maxImpressions,omitempty"`
	// TimeUnitType: The time unit. Along with num_time_units defines the amount of
	// time over which impressions per user are counted and capped.
	//
	// Possible values:
	//   "TIME_UNIT_TYPE_UNSPECIFIED" - A placeholder for an undefined time unit
	// type. This just indicates the variable with this value hasn't been
	// initialized.
	//   "MINUTE" - Minute unit.
	//   "HOUR" - Hour unit.
	//   "DAY" - Day unit.
	//   "WEEK" - Week unit.
	//   "MONTH" - Month unit.
	//   "LIFETIME" - Lifecycle/Lifetime unit.
	//   "POD" - Pod unit.
	//   "STREAM" - Stream unit.
	TimeUnitType string `json:"timeUnitType,omitempty"`
	// TimeUnitsCount: The amount of time, in the units specified by
	// time_unit_type. Defines the amount of time over which impressions per user
	// are counted and capped.
	TimeUnitsCount int64 `json:"timeUnitsCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaxImpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxImpressions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FrequencyCap: Message contains details about publisher-set frequency caps of the delivery.

func (FrequencyCap) MarshalJSON ¶
func (s FrequencyCap) MarshalJSON() ([]byte, error)
type InventorySizeTargeting ¶
type InventorySizeTargeting struct {
	// ExcludedInventorySizes: A list of inventory sizes to be excluded.
	ExcludedInventorySizes []*AdSize `json:"excludedInventorySizes,omitempty"`
	// TargetedInventorySizes: A list of inventory sizes to be included.
	TargetedInventorySizes []*AdSize `json:"targetedInventorySizes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedInventorySizes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedInventorySizes") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InventorySizeTargeting: Represents the size of an ad unit that can be targeted on a bid request.

func (InventorySizeTargeting) MarshalJSON ¶
func (s InventorySizeTargeting) MarshalJSON() ([]byte, error)
type InventoryTypeTargeting ¶
type InventoryTypeTargeting struct {
	// InventoryTypes: The list of targeted inventory types for the bid request.
	//
	// Possible values:
	//   "INVENTORY_TYPE_UNSPECIFIED" - Unspecified inventory type
	//   "BROWSER" - Desktop or mobile web browser excluding ads inside a video
	// player
	//   "MOBILE_APP" - Mobile apps other than video players and web browsers
	//   "VIDEO_PLAYER" - Instream video and audio
	InventoryTypes []string `json:"inventoryTypes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InventoryTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InventoryTypes") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

InventoryTypeTargeting: Targeting of the inventory types a bid request can originate from.

func (InventoryTypeTargeting) MarshalJSON ¶
func (s InventoryTypeTargeting) MarshalJSON() ([]byte, error)
type ListAuctionPackagesResponse ¶
type ListAuctionPackagesResponse struct {
	// AuctionPackages: The list of auction packages.
	AuctionPackages []*AuctionPackage `json:"auctionPackages,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	// Pass this value in the ListAuctionPackagesRequest.pageToken field in the
	// subsequent call to the `ListAuctionPackages` method to retrieve the next
	// page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuctionPackages") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuctionPackages") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAuctionPackagesResponse: Response message for listing auction packages.

func (ListAuctionPackagesResponse) MarshalJSON ¶
func (s ListAuctionPackagesResponse) MarshalJSON() ([]byte, error)
type ListClientUsersResponse ¶
type ListClientUsersResponse struct {
	// ClientUsers: The returned list of client users.
	ClientUsers []*ClientUser `json:"clientUsers,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListClientUsersRequest.pageToken field in the subsequent call to the
	// list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClientUsers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientUsers") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListClientUsersResponse: Response message for the list method.

func (ListClientUsersResponse) MarshalJSON ¶
func (s ListClientUsersResponse) MarshalJSON() ([]byte, error)
type ListClientsResponse ¶
type ListClientsResponse struct {
	// Clients: The returned list of clients.
	Clients []*Client `json:"clients,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListClientsRequest.pageToken field in the subsequent call to the list
	// method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Clients") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Clients") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListClientsResponse: Response message for the list method.

func (ListClientsResponse) MarshalJSON ¶
func (s ListClientsResponse) MarshalJSON() ([]byte, error)
type ListCuratedPackagesResponse ¶
added in v0.259.0
type ListCuratedPackagesResponse struct {
	// CuratedPackages: The list of curated packages.
	CuratedPackages []*CuratedPackage `json:"curatedPackages,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListCuratedPackagesRequest.pageToken field in the subsequent call to
	// `ListCuratedPackages` method to retrieve the next page of results. If empty,
	// then there are no more results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CuratedPackages") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CuratedPackages") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListCuratedPackagesResponse: Response message for ListCuratedPackages.

func (ListCuratedPackagesResponse) MarshalJSON ¶
added in v0.259.0
func (s ListCuratedPackagesResponse) MarshalJSON() ([]byte, error)
type ListDataSegmentsResponse ¶
type ListDataSegmentsResponse struct {
	// DataSegments: The list of data segments.
	DataSegments []*DataSegment `json:"dataSegments,omitempty"`
	// NextPageToken: Continuation token for fetching the next page of results.
	// Pass this value in the ListDataSegmentsRequest.pageToken field in the
	// subsequent call to the `ListDataSegments` method to retrieve the next page
	// of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataSegments") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataSegments") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDataSegmentsResponse: Response message for listing data segments.

func (ListDataSegmentsResponse) MarshalJSON ¶
func (s ListDataSegmentsResponse) MarshalJSON() ([]byte, error)
type ListDealsResponse ¶
type ListDealsResponse struct {
	// Deals: The list of deals.
	Deals []*Deal `json:"deals,omitempty"`
	// NextPageToken: Token to fetch the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Deals") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deals") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDealsResponse: Response message for listing deals in a proposal.

func (ListDealsResponse) MarshalJSON ¶
func (s ListDealsResponse) MarshalJSON() ([]byte, error)
type ListFinalizedDealsResponse ¶
type ListFinalizedDealsResponse struct {
	// FinalizedDeals: The list of finalized deals.
	FinalizedDeals []*FinalizedDeal `json:"finalizedDeals,omitempty"`
	// NextPageToken: Token to fetch the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FinalizedDeals") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FinalizedDeals") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListFinalizedDealsResponse: Response message for listing finalized deals.

func (ListFinalizedDealsResponse) MarshalJSON ¶
func (s ListFinalizedDealsResponse) MarshalJSON() ([]byte, error)
type ListMediaPlannersResponse ¶
added in v0.259.0
type ListMediaPlannersResponse struct {
	// MediaPlanners: List of media planners.
	MediaPlanners []*MediaPlanner `json:"mediaPlanners,omitempty"`
	// NextPageToken: A token which can be passed to a subsequent call to the
	// `ListMediaPlanners` method to retrieve the next page of results in
	// ListMediaPlannersRequest.pageToken.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "MediaPlanners") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MediaPlanners") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListMediaPlannersResponse: A response containing media planner account information.

func (ListMediaPlannersResponse) MarshalJSON ¶
added in v0.259.0
func (s ListMediaPlannersResponse) MarshalJSON() ([]byte, error)
type ListProposalsResponse ¶
type ListProposalsResponse struct {
	// NextPageToken: Continuation token for fetching the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Proposals: The list of proposals.
	Proposals []*Proposal `json:"proposals,omitempty"`

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

ListProposalsResponse: Response message for listing proposals.

func (ListProposalsResponse) MarshalJSON ¶
func (s ListProposalsResponse) MarshalJSON() ([]byte, error)
type ListPublisherProfilesResponse ¶
type ListPublisherProfilesResponse struct {
	// NextPageToken: Token to fetch the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// PublisherProfiles: The list of matching publisher profiles.
	PublisherProfiles []*PublisherProfile `json:"publisherProfiles,omitempty"`

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

ListPublisherProfilesResponse: Response message for profiles visible to the buyer.

func (ListPublisherProfilesResponse) MarshalJSON ¶
func (s ListPublisherProfilesResponse) MarshalJSON() ([]byte, error)
type MarketplaceTargeting ¶
type MarketplaceTargeting struct {
	// DaypartTargeting: Daypart targeting information.
	DaypartTargeting *DayPartTargeting `json:"daypartTargeting,omitempty"`
	// ExcludedSensitiveCategoryIds: Output only. The sensitive content category
	// label IDs excluded. Refer to this file
	// https://storage.googleapis.com/adx-rtb-dictionaries/content-labels.txt for
	// category IDs.
	ExcludedSensitiveCategoryIds googleapi.Int64s `json:"excludedSensitiveCategoryIds,omitempty"`
	// GeoTargeting: Output only. Geo criteria IDs to be included/excluded.
	GeoTargeting *CriteriaTargeting `json:"geoTargeting,omitempty"`
	// InventorySizeTargeting: Output only. Inventory sizes to be
	// included/excluded.
	InventorySizeTargeting *InventorySizeTargeting `json:"inventorySizeTargeting,omitempty"`
	// InventoryTypeTargeting: Output only. Inventory type targeting information.
	InventoryTypeTargeting *InventoryTypeTargeting `json:"inventoryTypeTargeting,omitempty"`
	// PlacementTargeting: Output only. Placement targeting information, for
	// example, URL, mobile applications.
	PlacementTargeting *PlacementTargeting `json:"placementTargeting,omitempty"`
	// TechnologyTargeting: Output only. Technology targeting information, for
	// example, operating system, device category.
	TechnologyTargeting *TechnologyTargeting `json:"technologyTargeting,omitempty"`
	// UserListTargeting: Buyer user list targeting information. User lists can be
	// uploaded using
	// https://developers.google.com/authorized-buyers/rtb/bulk-uploader.
	UserListTargeting *CriteriaTargeting `json:"userListTargeting,omitempty"`
	// VerticalTargeting: Output only. The verticals included or excluded as
	// defined in
	// https://developers.google.com/authorized-buyers/rtb/downloads/publisher-verticals
	VerticalTargeting *CriteriaTargeting `json:"verticalTargeting,omitempty"`
	// VideoTargeting: Output only. Video targeting information.
	VideoTargeting *VideoTargeting `json:"videoTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DaypartTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DaypartTargeting") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MarketplaceTargeting: Targeting represents different criteria that can be used to target deals or auction packages. For example, they can choose to target inventory only if the user is in the US. Multiple types of targeting are always applied as a logical AND, unless noted otherwise.

func (MarketplaceTargeting) MarshalJSON ¶
func (s MarketplaceTargeting) MarshalJSON() ([]byte, error)
type MediaPlanner ¶
type MediaPlanner struct {
	// AccountId: Output only. Account ID of the media planner.
	AccountId string `json:"accountId,omitempty"`
	// AncestorNames: Output only. The ancestor names of the media planner. Format:
	// `mediaPlanners/{mediaPlannerAccountId}` Can be used to filter the response
	// of the mediaPlanners.list method.
	AncestorNames []string `json:"ancestorNames,omitempty"`
	// DisplayName: Output only. The display name of the media planner. Can be used
	// to filter the response of the mediaPlanners.list method.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Identifier. The unique resource name of the media planner. Format:
	// `mediaPlanners/{mediaPlannerAccountId}` Can be used to filter the response
	// of the mediaPlanners.list method.
	Name string `json:"name,omitempty"`
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

MediaPlanner: Represents a media planner account.

func (MediaPlanner) MarshalJSON ¶
func (s MediaPlanner) MarshalJSON() ([]byte, error)
type MediaPlannersListCall ¶
added in v0.259.0
type MediaPlannersListCall struct {
	// contains filtered or unexported fields
}
func (*MediaPlannersListCall) Context ¶
added in v0.259.0
func (c *MediaPlannersListCall) Context(ctx context.Context) *MediaPlannersListCall

Context sets the context to be used in this call's Do method.

func (*MediaPlannersListCall) Do ¶
added in v0.259.0
func (c *MediaPlannersListCall) Do(opts ...googleapi.CallOption) (*ListMediaPlannersResponse, error)

Do executes the "authorizedbuyersmarketplace.mediaPlanners.list" call. Any non-2xx status code is an error. Response headers are in either *ListMediaPlannersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MediaPlannersListCall) Fields ¶
added in v0.259.0
func (c *MediaPlannersListCall) Fields(s ...googleapi.Field) *MediaPlannersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MediaPlannersListCall) Filter ¶
added in v0.259.0
func (c *MediaPlannersListCall) Filter(filter string) *MediaPlannersListCall

Filter sets the optional parameter "filter": Optional query string using the Cloud API list filtering syntax (/authorized-buyers/apis/guides/list-filters). Supported columns for filtering are: * `name` * `displayName` * `ancestorNames`

func (*MediaPlannersListCall) Header ¶
added in v0.259.0
func (c *MediaPlannersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MediaPlannersListCall) IfNoneMatch ¶
added in v0.259.0
func (c *MediaPlannersListCall) IfNoneMatch(entityTag string) *MediaPlannersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*MediaPlannersListCall) PageSize ¶
added in v0.259.0
func (c *MediaPlannersListCall) PageSize(pageSize int64) *MediaPlannersListCall

PageSize sets the optional parameter "pageSize": The maximum number of media planners to return. If unspecified, at most 100 media planners will be returned. The maximum value is 500; values above 500 will be coerced to 500.

func (*MediaPlannersListCall) PageToken ¶
added in v0.259.0
func (c *MediaPlannersListCall) PageToken(pageToken string) *MediaPlannersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. This value is received from a previous `ListMediaPlanners` call in ListMediaPlannersResponse.nextPageToken.

func (*MediaPlannersListCall) Pages ¶
added in v0.259.0
func (c *MediaPlannersListCall) Pages(ctx context.Context, f func(*ListMediaPlannersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type MediaPlannersService ¶
added in v0.259.0
type MediaPlannersService struct {
	// contains filtered or unexported fields
}
func NewMediaPlannersService ¶
added in v0.259.0
func NewMediaPlannersService(s *Service) *MediaPlannersService
func (*MediaPlannersService) List ¶
added in v0.259.0
func (r *MediaPlannersService) List() *MediaPlannersListCall

List: Lists all media planner accounts that the caller has access to. For curators, this will return all media planners that have accepted curator terms. For other accounts, attempting to list media planners will return an error.

type MobileApplicationTargeting ¶
type MobileApplicationTargeting struct {
	// FirstPartyTargeting: Publisher owned apps to be targeted or excluded by the
	// publisher to display the ads in.
	FirstPartyTargeting *FirstPartyMobileApplicationTargeting `json:"firstPartyTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FirstPartyTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirstPartyTargeting") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MobileApplicationTargeting: Mobile application targeting settings.

func (MobileApplicationTargeting) MarshalJSON ¶
func (s MobileApplicationTargeting) MarshalJSON() ([]byte, error)
type Money ¶
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
func (s Money) MarshalJSON() ([]byte, error)
type Note ¶
type Note struct {
	// CreateTime: Output only. When this note was created.
	CreateTime string `json:"createTime,omitempty"`
	// CreatorRole: Output only. The role who created the note.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	CreatorRole string `json:"creatorRole,omitempty"`
	// Note: The text of the note. Maximum length is 1024 characters.
	Note string `json:"note,omitempty"`
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

Note: A text note attached to the proposal to facilitate the communication between buyers and sellers.

func (Note) MarshalJSON ¶
func (s Note) MarshalJSON() ([]byte, error)
type OperatingSystemTargeting ¶
type OperatingSystemTargeting struct {
	// OperatingSystemCriteria: IDs of operating systems to be included/excluded.
	OperatingSystemCriteria *CriteriaTargeting `json:"operatingSystemCriteria,omitempty"`
	// OperatingSystemVersionCriteria: IDs of operating system versions to be
	// included/excluded.
	OperatingSystemVersionCriteria *CriteriaTargeting `json:"operatingSystemVersionCriteria,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OperatingSystemCriteria") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OperatingSystemCriteria") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OperatingSystemTargeting: Represents targeting information for operating systems.

func (OperatingSystemTargeting) MarshalJSON ¶
func (s OperatingSystemTargeting) MarshalJSON() ([]byte, error)
type PackagePlacementTargeting ¶
added in v0.259.0
type PackagePlacementTargeting struct {
	// IncludedMobileAppCategoryTargeting: Optional. The list of targeted mobile
	// app categories.
	IncludedMobileAppCategoryTargeting googleapi.Int64s `json:"includedMobileAppCategoryTargeting,omitempty"`
	// MobileAppTargeting: Optional. The list of targeted or excluded mobile
	// application IDs that publishers own. Currently, only Android and Apple apps
	// are supported. Android App ID, for example, com.google.android.apps.maps,
	// can be found in Google Play Store URL. iOS App ID (which is a number) can be
	// found at the end of iTunes store URL. First party mobile applications is
	// either included or excluded.
	MobileAppTargeting *StringTargetingDimension `json:"mobileAppTargeting,omitempty"`
	// UriTargeting: Optional. The list of targeted or excluded URLs. The domains
	// should have the http/https stripped (for example, google.com), and can
	// contain a max of 5 paths per url.
	UriTargeting *StringTargetingDimension `json:"uriTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "IncludedMobileAppCategoryTargeting") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "IncludedMobileAppCategoryTargeting") to include in API requests with the
	// JSON null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

PackagePlacementTargeting: Represents targeting about where the ads can appear, for example, certain sites or mobile applications. Different placement targeting types will be logically OR'ed.

func (PackagePlacementTargeting) MarshalJSON ¶
added in v0.259.0
func (s PackagePlacementTargeting) MarshalJSON() ([]byte, error)
type PackagePublisherProvidedSignalsTargeting ¶
added in v0.259.0
type PackagePublisherProvidedSignalsTargeting struct {
	// AudienceTargeting: Optional. The list of targeted or excluded audience IDs.
	// Based off of IAB Audience Taxonomy version 1.1
	// (https://github.com/InteractiveAdvertisingBureau/Taxonomies/blob/main/Audience%20Taxonomies/Audience%20Taxonomy%201.1.tsv)
	AudienceTargeting *TaxonomyTargeting `json:"audienceTargeting,omitempty"`
	// ContentTargeting: Optional. The list of targeted or excluded content IDs.
	// Based off of IAB Content Taxonomy version 2.2
	// (https://github.com/InteractiveAdvertisingBureau/Taxonomies/blob/main/Content%20Taxonomies/Content%20Taxonomy%202.2.tsv)
	ContentTargeting *TaxonomyTargeting `json:"contentTargeting,omitempty"`
	// VideoAndAudioSignalsTargeting: Optional. The list of targeted and excluded
	// video and audio signals IDs. These are additional signals supported by
	// publisher provided signals.
	VideoAndAudioSignalsTargeting *StringTargetingDimension `json:"videoAndAudioSignalsTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AudienceTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AudienceTargeting") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PackagePublisherProvidedSignalsTargeting: Represents targeting about publisher provided signals. Different publisher provided signals types will be logically OR'ed.

func (PackagePublisherProvidedSignalsTargeting) MarshalJSON ¶
added in v0.259.0
func (s PackagePublisherProvidedSignalsTargeting) MarshalJSON() ([]byte, error)
type PackageTargeting ¶
added in v0.259.0
type PackageTargeting struct {
	// GeoTargeting: Optional. The geo criteria IDs to be included or excluded as
	// defined in
	// https://storage.googleapis.com/adx-rtb-dictionaries/geo-table.csv. If unset,
	// inventory will be targeted regardless of geo.
	GeoTargeting *CriteriaTargeting `json:"geoTargeting,omitempty"`
	// IncludedAcceleratedMobilePageType: Optional. The targeted accelerated mobile
	// page type. If unset, inventory will be targeted regardless of AMP status.
	//
	// Possible values:
	//   "ACCELERATED_MOBILE_PAGE_TYPE_UNSPECIFIED" - Default value. Should not be
	// used in targeting specifications.
	//   "ACCELERATED_MOBILE_PAGE_TYPE_NON_AMP" - Targets inventory on standard web
	// pages not using any AMP framework.
	//   "ACCELERATED_MOBILE_PAGE_TYPE_AMP" - Targets inventory on pages built
	// using the core AMP HTML framework.
	//   "ACCELERATED_MOBILE_PAGE_TYPE_AMP_STORY" - Targets inventory on pages
	// using the AMP Story (STAMP) format, which is optimized for visual
	// storytelling (e.g., tappable full-screen experiences).
	IncludedAcceleratedMobilePageType string `json:"includedAcceleratedMobilePageType,omitempty"`
	// IncludedAdSizes: Optional. The list of ad sizes to target. If unset,
	// inventory will be targeted regardless of ad size. Curated packages supports
	// `PIXEL` and `INTERSTITIAL` ad sizes.
	IncludedAdSizes []*AdSize `json:"includedAdSizes,omitempty"`
	// IncludedAuthorizedSellerStatuses: Optional. The included list of targeted
	// authorized seller statuses. If empty, inventory will be targeted regardless
	// of seller status.
	//
	// Possible values:
	//   "AUTHORIZED_SELLER_STATUS_UNSPECIFIED" - Default value. Should not be used
	// in targeting specifications.
	//   "AUTHORIZED_SELLER_STATUS_DIRECT" - Targets inventory where the seller is
	// declared as 'DIRECT'. This indicates the publisher (content owner) directly
	// controls the seller account and has a direct business contract with the
	// advertising system for this account.
	//   "AUTHORIZED_SELLER_STATUS_RESELLER" - Targets inventory where the seller
	// is declared as 'RESELLER'. This indicates the publisher has authorized
	// another entity to operate the listed seller account and resell their ad
	// space.
	IncludedAuthorizedSellerStatuses []string `json:"includedAuthorizedSellerStatuses,omitempty"`
	// IncludedCreativeFormat: Optional. The creative format to target. If unset,
	// all creative markup types are targeted.
	//
	// Possible values:
	//   "CREATIVE_FORMAT_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "CREATIVE_FORMAT_DISPLAY" - Targets ad slots intended for HTML display
	// creatives.
	//   "CREATIVE_FORMAT_VIDEO" - Targets ad slots intended for video creatives.
	//   "CREATIVE_FORMAT_AUDIO" - Targets ad slots intended for audio creatives.
	IncludedCreativeFormat string `json:"includedCreativeFormat,omitempty"`
	// IncludedDataSegments: Optional. The active data segments to be targeted. If
	// unset, inventory will be targeted regardless of data segments. Format:
	// `curators/{account_id}/dataSegments/{data_segment_id}`
	IncludedDataSegments []string `json:"includedDataSegments,omitempty"`
	// IncludedDeviceTypes: Optional. The list of included device types to target.
	// If empty, all device types are targeted.
	//
	// Possible values:
	//   "DEVICE_TYPE_UNSPECIFIED" - Default value. Should not be used in targeting
	// specifications.
	//   "DEVICE_TYPE_PERSONAL_COMPUTER" - Targets desktop or laptop computers.
	//   "DEVICE_TYPE_CONNECTED_TV" - Targets connected TVs: devices that stream TV
	// content, including smart TVs, gaming consoles, and streaming boxes/sticks.
	//   "DEVICE_TYPE_PHONE" - Targets high-end mobile devices.
	//   "DEVICE_TYPE_TABLET" - Targets tablet devices.
	IncludedDeviceTypes []string `json:"includedDeviceTypes,omitempty"`
	// IncludedEnvironment: Optional. The environment to target. If unspecified,
	// all environments are targeted.
	//
	// Possible values:
	//   "ENVIRONMENT_UNSPECIFIED" - Default value. Should not be used in targeting
	// specifications.
	//   "ENVIRONMENT_SITE" - Targets inventory rendered within an ad-supported
	// website.
	//   "ENVIRONMENT_APP" - Targets inventory within a mobile application.
	IncludedEnvironment string `json:"includedEnvironment,omitempty"`
	// IncludedNativeInventoryTypes: Optional. The targeted native inventory types.
	// If empty, inventory will be targeted regardless of native inventory type.
	//
	// Possible values:
	//   "NATIVE_INVENTORY_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "NATIVE_INVENTORY_TYPE_NATIVE_ONLY" - Targets ad slots that *only* accept
	// and render native ads.
	//   "NATIVE_INVENTORY_TYPE_NATIVE_OR_BANNER" - Targets ad slots that accept
	// and render either native or banner ads.
	IncludedNativeInventoryTypes []string `json:"includedNativeInventoryTypes,omitempty"`
	// IncludedOpenMeasurementTypes: Optional. The list of targeted open
	// measurement types. If empty, inventory will be targeted regardless of Open
	// Measurement support.
	//
	// Possible values:
	//   "OPEN_MEASUREMENT_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "OPEN_MEASUREMENT_TYPE_OMID_V1" - Targets inventory that supports the v1
	// Open Measurement Interface Definition (OMID).
	IncludedOpenMeasurementTypes []string `json:"includedOpenMeasurementTypes,omitempty"`
	// IncludedRestrictedCategories: Optional. The list of targeted restricted
	// categories. If empty, inventory will be targeted regardless of restricted
	// categories.
	//
	// Possible values:
	//   "RESTRICTED_CATEGORY_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "RESTRICTED_CATEGORY_ALCOHOL" - Targets inventory where alcohol ads are
	// allowed by the publisher.
	//   "RESTRICTED_CATEGORY_GAMBLING" - Targets inventory where gambling ads are
	// allowed by the publisher.
	IncludedRestrictedCategories []string `json:"includedRestrictedCategories,omitempty"`
	// IncludedRewardedType: Optional. The targeted rewarded type. If unset,
	// inventory will be targeted regardless of rewarded type.
	//
	// Possible values:
	//   "REWARDED_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "REWARDED_TYPE_NON_REWARDED" - Targets inventory that does NOT offer an
	// explicit reward to the user for watching or interacting with the ad.
	//   "REWARDED_TYPE_REWARDED" - Targets inventory that offers a reward to the
	// user in exchange for watching or engaging with the ad.
	IncludedRewardedType string `json:"includedRewardedType,omitempty"`
	// LanguageTargeting: Optional. The languages to target. If unset, inventory
	// will be targeted regardless of language. See
	// https://developers.google.com/google-ads/api/data/codes-formats#languages
	// for the list of supported language codes.
	LanguageTargeting *StringTargetingDimension `json:"languageTargeting,omitempty"`
	// MinimumPredictedClickThroughRatePercentageMillis: Optional. The targeted
	// minimum predicted click through rate, ranging in values [10, 10000] (0.01% -
	// 10%). A value of 50 means that the configuration will only match adslots for
	// which we predict at least 0.05% click through rate. An unset value indicates
	// inventory will be targeted regardless of predicted click through rate.
	MinimumPredictedClickThroughRatePercentageMillis int64 `json:"minimumPredictedClickThroughRatePercentageMillis,omitempty,string"`
	// MinimumPredictedViewabilityPercentage: Optional. The targeted minimum
	// predicted viewability percentage. This value must be a multiple of 10
	// between 10 and 90 (inclusive). For example, 10 is valid, but 0, 15, and 100
	// are not. A value of 10 means that the configuration will only match adslots
	// for which we predict at least 10% viewability. An unset value indicates
	// inventory will be targeted regardless of predicted viewability.
	MinimumPredictedViewabilityPercentage int64 `json:"minimumPredictedViewabilityPercentage,omitempty,string"`
	// PlacementTargeting: Optional. Placement targeting information, for example,
	// URL, mobile applications.
	PlacementTargeting *PackagePlacementTargeting `json:"placementTargeting,omitempty"`
	// PublisherProvidedSignalsTargeting: Optional. The publisher provided signals
	// to target. If unset, inventory will be targeted regardless of publisher
	// provided signals.
	PublisherProvidedSignalsTargeting *PackagePublisherProvidedSignalsTargeting `json:"publisherProvidedSignalsTargeting,omitempty"`
	// PublisherTargeting: Optional. The targeted publishers. If unset, inventory
	// will be targeted regardless of publisher. Publishers are identified by their
	// publisher ID from ads.txt / app-ads.txt. See https://iabtechlab.com/ads-txt/
	// and https://iabtechlab.com/app-ads-txt/ for more details.
	PublisherTargeting *StringTargetingDimension `json:"publisherTargeting,omitempty"`
	// VerticalTargeting: Optional. The verticals included or excluded as defined
	// in
	// https://developers.google.com/authorized-buyers/rtb/downloads/publisher-verticals.
	// If unset, inventory will be targeted regardless of vertical.
	VerticalTargeting *CriteriaTargeting `json:"verticalTargeting,omitempty"`
	// VideoTargeting: Optional. Video specific targeting criteria.
	VideoTargeting *PackageVideoTargeting `json:"videoTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GeoTargeting") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GeoTargeting") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PackageTargeting: Targeting criteria for curated and auction packages.

func (PackageTargeting) MarshalJSON ¶
added in v0.259.0
func (s PackageTargeting) MarshalJSON() ([]byte, error)
type PackageVideoTargeting ¶
added in v0.259.0
type PackageVideoTargeting struct {
	// IncludedContentDeliveryMethod: Optional. The targeted video delivery method.
	// If unset, inventory will be targeted regardless of video delivery method.
	//
	// Possible values:
	//   "CONTENT_DELIVERY_METHOD_UNSPECIFIED" - Default value. Should not be used
	// in targeting specifications.
	//   "CONTENT_DELIVERY_METHOD_STREAMING" - Targets video content that is being
	// broadcast live.
	//   "CONTENT_DELIVERY_METHOD_PROGRESSIVE" - Targets video content that is
	// transferred incrementally as client's playback requires.
	IncludedContentDeliveryMethod string `json:"includedContentDeliveryMethod,omitempty"`
	// IncludedMaximumAdDurationTargeting: Optional. The targeted maximum video ad
	// duration. If unset, inventory will be targeted regardless of maximum video
	// ad duration.
	//
	// Possible values:
	//   "MAXIMUM_VIDEO_AD_DURATION_UNSPECIFIED" - Default value. Should not be
	// used in targeting specifications.
	//   "MAXIMUM_VIDEO_AD_DURATION_FIFTEEN_SECONDS" - Applies to video ads with a
	// duration up to 15 seconds (0 < duration <= 15s).
	//   "MAXIMUM_VIDEO_AD_DURATION_TWENTY_SECONDS" - Applies to video ads with a
	// duration up to 20 seconds (0 < duration <= 20s).
	//   "MAXIMUM_VIDEO_AD_DURATION_THIRTY_SECONDS" - Applies to video ads with a
	// duration up to 30 seconds (0 < duration <= 30s).
	//   "MAXIMUM_VIDEO_AD_DURATION_SIXTY_SECONDS" - Applies to video ads with a
	// duration up to 60 seconds (0 < duration <= 60s).
	//   "MAXIMUM_VIDEO_AD_DURATION_NINETY_SECONDS" - Applies to video ads with a
	// duration up to 90 seconds (0 < duration <= 90s).
	//   "MAXIMUM_VIDEO_AD_DURATION_ONE_HUNDRED_TWENTY_SECONDS" - Applies to video
	// ads with a duration up to 120 seconds (0 < duration <= 120s).
	IncludedMaximumAdDurationTargeting string `json:"includedMaximumAdDurationTargeting,omitempty"`
	// IncludedMimeTypes: Optional. The list of targeted video mime types using the
	// IANA published MIME type strings
	// (https://www.iana.org/assignments/media-types/media-types.xhtml). If empty,
	// inventory will be targeted regardless of video mime type.
	//
	// Possible values:
	//   "VIDEO_MIME_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "VIDEO_MIME_TYPE_THREEGPP" - 3GPP container format used on 3G phones.
	//   "VIDEO_MIME_TYPE_APPLICATION_MPEGURL" - HLS/M3U8
	//   "VIDEO_MIME_TYPE_MP4" - MPEG-4 container typically with H.264 codec.
	//   "VIDEO_MIME_TYPE_APPLICATION_MPEGDASH" - DASH.
	//   "VIDEO_MIME_TYPE_APPLICATION_JAVASCRIPT" - JavaScript (used for VPAID
	// ads).
	//   "VIDEO_MIME_TYPE_WEBM" - WebM container assuming VP9 codec.
	IncludedMimeTypes []string `json:"includedMimeTypes,omitempty"`
	// IncludedPlaybackMethods: Optional. The list of targeted video playback
	// methods. If empty, inventory will be targeted regardless of video playback
	// method.
	//
	// Possible values:
	//   "PLAYBACK_METHOD_UNSPECIFIED" - Unspecified video playback method. Should
	// not be used.
	//   "PLAYBACK_METHOD_AUTO_PLAY_SOUND_ON" - Playback starts automatically when
	// the page/content loads.
	//   "PLAYBACK_METHOD_AUTO_PLAY_SOUND_OFF" - Playback starts automatically when
	// the page/content loads, but with sound off.
	//   "PLAYBACK_METHOD_CLICK_TO_PLAY" - Playback is initiated by a user action
	// (e.g., clicking a play button).
	IncludedPlaybackMethods []string `json:"includedPlaybackMethods,omitempty"`
	// IncludedPlayerSizeTargeting: Optional. The targeted video player size. If
	// unset, inventory will be targeted regardless of video player size.
	IncludedPlayerSizeTargeting *VideoPlayerSizeTargeting `json:"includedPlayerSizeTargeting,omitempty"`
	// IncludedPositionTypes: Optional. The targeted video ad position types. If
	// empty, inventory will be targeted regardless of video ad position type.
	//
	// Possible values:
	//   "POSITION_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "POSITION_TYPE_MIDROLL" - The ad is played in the middle of the video
	// content.
	//   "POSITION_TYPE_POSTROLL" - The ad is played after the video content.
	//   "POSITION_TYPE_PREROLL" - The ad is played before the video content.
	IncludedPositionTypes []string `json:"includedPositionTypes,omitempty"`
	// MinimumPredictedCompletionRatePercentage: Optional. The targeted minimum
	// predicted completion rate percentage. This value must be a multiple of 10
	// between 10 and 90 (inclusive). For example, 10 is valid, but 0, 15, and 100
	// are not. A value of 10 means that the configuration will only match adslots
	// for which we predict at least 10% completion rate. An unset value indicates
	// inventory will be targeted regardless of predicted completion rate.
	MinimumPredictedCompletionRatePercentage int64 `json:"minimumPredictedCompletionRatePercentage,omitempty,string"`
	// PlcmtTargeting: Optional. The targeted video plcmt types. If unset,
	// inventory will be targeted regardless of video plcmt type.
	PlcmtTargeting *VideoPlcmtTargeting `json:"plcmtTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "IncludedContentDeliveryMethod") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IncludedContentDeliveryMethod")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PackageVideoTargeting: Video specific targeting criteria.

func (PackageVideoTargeting) MarshalJSON ¶
added in v0.259.0
func (s PackageVideoTargeting) MarshalJSON() ([]byte, error)
type PauseFinalizedDealRequest ¶
type PauseFinalizedDealRequest struct {
	// Reason: The reason to pause the finalized deal, will be displayed to the
	// seller. Maximum length is 1000 characters.
	Reason string `json:"reason,omitempty"`
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

PauseFinalizedDealRequest: Request message for pausing a finalized deal.

func (PauseFinalizedDealRequest) MarshalJSON ¶
func (s PauseFinalizedDealRequest) MarshalJSON() ([]byte, error)
type PlacementTargeting ¶
type PlacementTargeting struct {
	// MobileApplicationTargeting: Mobile application targeting information in a
	// deal. This doesn't apply to Auction Packages.
	MobileApplicationTargeting *MobileApplicationTargeting `json:"mobileApplicationTargeting,omitempty"`
	// UriTargeting: URLs to be included/excluded.
	UriTargeting *UriTargeting `json:"uriTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MobileApplicationTargeting")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MobileApplicationTargeting") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PlacementTargeting: Represents targeting about where the ads can appear, for example, certain sites or mobile applications. Different placement targeting types will be logically OR'ed.

func (PlacementTargeting) MarshalJSON ¶
func (s PlacementTargeting) MarshalJSON() ([]byte, error)
type PreferredDealTerms ¶
type PreferredDealTerms struct {
	// FixedPrice: Fixed price for the deal.
	FixedPrice *Price `json:"fixedPrice,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FixedPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FixedPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PreferredDealTerms: Pricing terms for Preferred Deals.

func (PreferredDealTerms) MarshalJSON ¶
func (s PreferredDealTerms) MarshalJSON() ([]byte, error)
type Price ¶
type Price struct {
	// Amount: The actual price with currency specified.
	Amount *Money `json:"amount,omitempty"`
	// Type: The pricing type for the deal.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - A placeholder for an undefined pricing type. If the
	// pricing type is unspecified, CPM will be used instead.
	//   "CPM" - Cost per thousand impressions.
	//   "CPD" - Cost per day.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Amount") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Amount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Price: Represents a price and a pricing type for a deal.

func (Price) MarshalJSON ¶
func (s Price) MarshalJSON() ([]byte, error)
type PrivateAuctionTerms ¶
type PrivateAuctionTerms struct {
	// FloorPrice: The minimum price buyer has to bid to compete in the private
	// auction.
	FloorPrice *Price `json:"floorPrice,omitempty"`
	// OpenAuctionAllowed: Output only. True if open auction buyers are allowed to
	// compete with invited buyers in this private auction.
	OpenAuctionAllowed bool `json:"openAuctionAllowed,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FloorPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FloorPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrivateAuctionTerms: Pricing terms for Private Auctions.

func (PrivateAuctionTerms) MarshalJSON ¶
func (s PrivateAuctionTerms) MarshalJSON() ([]byte, error)
type PrivateData ¶
type PrivateData struct {
	// ReferenceId: A buyer specified reference ID. This can be queried in the list
	// operations (max-length: 1024 unicode code units).
	ReferenceId string `json:"referenceId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ReferenceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ReferenceId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PrivateData: Buyers are allowed to store certain types of private data in a proposal.

func (PrivateData) MarshalJSON ¶
func (s PrivateData) MarshalJSON() ([]byte, error)
type ProgrammaticGuaranteedTerms ¶
type ProgrammaticGuaranteedTerms struct {
	// FixedPrice: Fixed price for the deal.
	FixedPrice *Price `json:"fixedPrice,omitempty"`
	// GuaranteedLooks: Count of guaranteed looks. For CPD deals, buyer changes to
	// guaranteed_looks will be ignored.
	GuaranteedLooks int64 `json:"guaranteedLooks,omitempty,string"`
	// ImpressionCap: The lifetime impression cap for CPM Sponsorship deals. Deal
	// will stop serving when cap is reached.
	ImpressionCap int64 `json:"impressionCap,omitempty,string"`
	// MinimumDailyLooks: Daily minimum looks for CPD deal types. For CPD deals,
	// buyer should negotiate on this field instead of guaranteed_looks.
	MinimumDailyLooks int64 `json:"minimumDailyLooks,omitempty,string"`
	// PercentShareOfVoice: For sponsorship deals, this is the percentage of the
	// seller's eligible impressions that the deal will serve until the cap is
	// reached. Valid value is within range 0~100.
	PercentShareOfVoice int64 `json:"percentShareOfVoice,omitempty,string"`
	// ReservationType: The reservation type for a Programmatic Guaranteed deal.
	// This indicates whether the number of impressions is fixed, or a percent of
	// available impressions. If not specified, the default reservation type is
	// STANDARD.
	//
	// Possible values:
	//   "RESERVATION_TYPE_UNSPECIFIED" - An unspecified reservation type.
	//   "STANDARD" - Non-sponsorship deal.
	//   "SPONSORSHIP" - Sponsorship deals don't have impression goal
	// (guaranteed_looks) and they are served based on the flight dates. For CPM
	// Sponsorship deals, impression_cap is the lifetime impression limit.
	ReservationType string `json:"reservationType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FixedPrice") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FixedPrice") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProgrammaticGuaranteedTerms: Pricing terms for Programmatic Guaranteed Deals.

func (ProgrammaticGuaranteedTerms) MarshalJSON ¶
func (s ProgrammaticGuaranteedTerms) MarshalJSON() ([]byte, error)
type Proposal ¶
type Proposal struct {
	// BilledBuyer: Output only. When the client field is populated, this field
	// refers to the buyer who creates and manages the client buyer and gets billed
	// on behalf of the client buyer; when the buyer field is populated, this field
	// is the same value as buyer. Format : `buyers/{buyerAccountId}`
	BilledBuyer string `json:"billedBuyer,omitempty"`
	// Buyer: Output only. Refers to a buyer in The Realtime-bidding API. Format:
	// `buyers/{buyerAccountId}`
	Buyer string `json:"buyer,omitempty"`
	// BuyerContacts: Contact information for the buyer.
	BuyerContacts []*Contact `json:"buyerContacts,omitempty"`
	// BuyerPrivateData: Buyer private data (hidden from seller).
	BuyerPrivateData *PrivateData `json:"buyerPrivateData,omitempty"`
	// Client: Output only. Refers to a Client. Format:
	// `buyers/{buyerAccountId}/clients/{clientAccountid}`
	Client string `json:"client,omitempty"`
	// DealType: Output only. Type of deal the proposal contains.
	//
	// Possible values:
	//   "DEAL_TYPE_UNSPECIFIED" - Default, unspecified deal type.
	//   "PREFERRED_DEAL" - Preferred deals.
	//   "PRIVATE_AUCTION" - Private auction deals.
	//   "PROGRAMMATIC_GUARANTEED" - Programmatic guaranteed deals.
	DealType string `json:"dealType,omitempty"`
	// DisplayName: Output only. The descriptive name for the proposal. Maximum
	// length of 255 unicode characters is allowed. Control characters are not
	// allowed. Buyers cannot update this field. Note: Not to be confused with
	// name, which is a unique identifier of the proposal.
	DisplayName string `json:"displayName,omitempty"`
	// IsRenegotiating: Output only. True if the proposal was previously finalized
	// and is now being renegotiated.
	IsRenegotiating bool `json:"isRenegotiating,omitempty"`
	// LastUpdaterOrCommentorRole: Output only. The role of the last user that
	// either updated the proposal or left a comment.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	LastUpdaterOrCommentorRole string `json:"lastUpdaterOrCommentorRole,omitempty"`
	// Name: Immutable. The name of the proposal serving as a unique identifier.
	// Format: buyers/{accountId}/proposals/{proposalId}
	Name string `json:"name,omitempty"`
	// Notes: A list of notes from the buyer and the seller attached to this
	// proposal.
	Notes []*Note `json:"notes,omitempty"`
	// OriginatorRole: Output only. Indicates whether the buyer/seller created the
	// proposal.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	OriginatorRole string `json:"originatorRole,omitempty"`
	// PausingConsented: Whether pausing is allowed for the proposal. This is a
	// negotiable term between buyers and publishers.
	PausingConsented bool `json:"pausingConsented,omitempty"`
	// ProposalRevision: Output only. The revision number for the proposal. Each
	// update to the proposal or deal causes the proposal revision number to
	// auto-increment. The buyer keeps track of the last revision number they know
	// of and pass it in when making an update. If the head revision number on the
	// server has since incremented, then an ABORTED error is returned during the
	// update operation to let the buyer know that a subsequent update was made.
	ProposalRevision int64 `json:"proposalRevision,omitempty,string"`
	// PublisherProfile: Immutable. Reference to the seller on the proposal.
	// Format: `buyers/{buyerAccountId}/publisherProfiles/{publisherProfileId}`
	// Note: This field may be set only when creating the resource. Modifying this
	// field while updating the resource will result in an error.
	PublisherProfile string `json:"publisherProfile,omitempty"`
	// SellerContacts: Output only. Contact information for the seller.
	SellerContacts []*Contact `json:"sellerContacts,omitempty"`
	// State: Output only. Indicates the state of the proposal.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Unspecified proposal state
	//   "BUYER_REVIEW_REQUESTED" - When a proposal is waiting for buyer to review.
	//   "SELLER_REVIEW_REQUESTED" - When the proposal is waiting for the seller to
	// review.
	//   "BUYER_ACCEPTANCE_REQUESTED" - When the seller accepted the proposal and
	// sent it to the buyer for review.
	//   "FINALIZED" - When both buyer and seller has accepted the proposal
	//   "TERMINATED" - When either buyer or seller has cancelled the proposal
	State string `json:"state,omitempty"`
	// TermsAndConditions: Output only. The terms and conditions associated with
	// this proposal. Accepting a proposal implies acceptance of this field. This
	// is created by the seller, the buyer can only view it.
	TermsAndConditions string `json:"termsAndConditions,omitempty"`
	// UpdateTime: Output only. The time when the proposal was last revised.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BilledBuyer") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BilledBuyer") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Proposal: Represents a proposal in the Marketplace. A proposal is the unit of negotiation between a seller and a buyer.

func (Proposal) MarshalJSON ¶
func (s Proposal) MarshalJSON() ([]byte, error)
type PublisherProfile ¶
type PublisherProfile struct {
	// AudienceDescription: Description on the publisher's audience.
	AudienceDescription string `json:"audienceDescription,omitempty"`
	// DirectDealsContact: Contact information for direct reservation deals. This
	// is free text entered by the publisher and may include information like
	// names, phone numbers and email addresses.
	DirectDealsContact string `json:"directDealsContact,omitempty"`
	// DisplayName: Display name of the publisher profile. Can be used to filter
	// the response of the publisherProfiles.list method.
	DisplayName string `json:"displayName,omitempty"`
	// Domains: The list of domains represented in this publisher profile. Empty if
	// this is a parent profile. These are top private domains, meaning that these
	// will not contain a string like "photos.google.co.uk/123", but will instead
	// contain "google.co.uk". Can be used to filter the response of the
	// publisherProfiles.list method.
	Domains []string `json:"domains,omitempty"`
	// IsParent: Indicates if this profile is the parent profile of the seller. A
	// parent profile represents all the inventory from the seller, as opposed to
	// child profile that is created to brand a portion of inventory. One seller
	// has only one parent publisher profile, and can have multiple child profiles.
	// See https://support.google.com/admanager/answer/6035806 for details. Can be
	// used to filter the response of the publisherProfiles.list method by setting
	// the filter to "is_parent: true".
	IsParent bool `json:"isParent,omitempty"`
	// LogoUrl: A Google public URL to the logo for this publisher profile. The
	// logo is stored as a PNG, JPG, or GIF image.
	LogoUrl string `json:"logoUrl,omitempty"`
	// MediaKitUrl: URL to additional marketing and sales materials.
	MediaKitUrl string `json:"mediaKitUrl,omitempty"`
	// MobileApps: The list of apps represented in this publisher profile. Empty if
	// this is a parent profile.
	MobileApps []*PublisherProfileMobileApplication `json:"mobileApps,omitempty"`
	// Name: Name of the publisher profile. Format:
	// `buyers/{buyer}/publisherProfiles/{publisher_profile}`
	Name string `json:"name,omitempty"`
	// Overview: Overview of the publisher.
	Overview string `json:"overview,omitempty"`
	// PitchStatement: Statement explaining what's unique about publisher's
	// business, and why buyers should partner with the publisher.
	PitchStatement string `json:"pitchStatement,omitempty"`
	// ProgrammaticDealsContact: Contact information for programmatic deals. This
	// is free text entered by the publisher and may include information like
	// names, phone numbers and email addresses.
	ProgrammaticDealsContact string `json:"programmaticDealsContact,omitempty"`
	// PublisherCode: A unique identifying code for the seller. This value is the
	// same for all of the seller's parent and child publisher profiles. Can be
	// used to filter the response of the publisherProfiles.list method.
	PublisherCode string `json:"publisherCode,omitempty"`
	// SamplePageUrl: URL to a sample content page.
	SamplePageUrl string `json:"samplePageUrl,omitempty"`
	// TopHeadlines: Up to three key metrics and rankings. For example, "#1 Mobile
	// News Site for 20 Straight Months".
	TopHeadlines []string `json:"topHeadlines,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AudienceDescription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AudienceDescription") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PublisherProfile: The values in the publisher profile are supplied by the publisher. All fields are not filterable unless stated otherwise.

func (PublisherProfile) MarshalJSON ¶
func (s PublisherProfile) MarshalJSON() ([]byte, error)
type PublisherProfileMobileApplication ¶
type PublisherProfileMobileApplication struct {
	// AppStore: The app store the app belongs to. Can be used to filter the
	// response of the publisherProfiles.list method.
	//
	// Possible values:
	//   "APP_STORE_TYPE_UNSPECIFIED" - A placeholder for an unknown app store.
	//   "APPLE_ITUNES" - Apple iTunes
	//   "GOOGLE_PLAY" - Google Play
	//   "ROKU" - Roku
	//   "AMAZON_FIRE_TV" - Amazon Fire TV
	//   "PLAYSTATION" - PlayStation
	//   "XBOX" - Xbox
	//   "SAMSUNG_TV" - Samsung TV
	//   "AMAZON" - Amazon Appstore
	//   "OPPO" - OPPO App Market
	//   "SAMSUNG" - Samsung Galaxy Store
	//   "VIVO" - VIVO App Store
	//   "XIAOMI" - Xiaomi GetApps
	//   "LG_TV" - LG TV
	AppStore string `json:"appStore,omitempty"`
	// ExternalAppId: The external ID for the app from its app store. Can be used
	// to filter the response of the publisherProfiles.list method.
	ExternalAppId string `json:"externalAppId,omitempty"`
	// Name: The name of the app.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppStore") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppStore") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PublisherProfileMobileApplication: A mobile application that contains a external app ID, name, and app store.

func (PublisherProfileMobileApplication) MarshalJSON ¶
func (s PublisherProfileMobileApplication) MarshalJSON() ([]byte, error)
type ResumeFinalizedDealRequest ¶
type ResumeFinalizedDealRequest struct {
}

ResumeFinalizedDealRequest: Request message for resuming a finalized deal.

type RtbMetrics ¶
type RtbMetrics struct {
	// AdImpressions7Days: Ad impressions in last 7 days.
	AdImpressions7Days int64 `json:"adImpressions7Days,omitempty,string"`
	// BidRate7Days: Bid rate in last 7 days, calculated by (bids / bid requests).
	BidRate7Days float64 `json:"bidRate7Days,omitempty"`
	// BidRequests7Days: Bid requests in last 7 days.
	BidRequests7Days int64 `json:"bidRequests7Days,omitempty,string"`
	// Bids7Days: Bids in last 7 days.
	Bids7Days int64 `json:"bids7Days,omitempty,string"`
	// FilteredBidRate7Days: Filtered bid rate in last 7 days, calculated by
	// (filtered bids / bids).
	FilteredBidRate7Days float64 `json:"filteredBidRate7Days,omitempty"`
	// MustBidRateCurrentMonth: Must bid rate for current month.
	MustBidRateCurrentMonth float64 `json:"mustBidRateCurrentMonth,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdImpressions7Days") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdImpressions7Days") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RtbMetrics: Real-time bidding metrics. For what each metric means refer to Report metrics (https://support.google.com/adxbuyer/answer/6115195#report-metrics)

func (RtbMetrics) MarshalJSON ¶
func (s RtbMetrics) MarshalJSON() ([]byte, error)
func (*RtbMetrics) UnmarshalJSON ¶
func (s *RtbMetrics) UnmarshalJSON(data []byte) error
type SendRfpRequest ¶
type SendRfpRequest struct {
	// BuyerContacts: Contact information for the buyer.
	BuyerContacts []*Contact `json:"buyerContacts,omitempty"`
	// Client: If the current buyer is sending the RFP on behalf of its client, use
	// this field to specify the name of the client in the format:
	// `buyers/{accountId}/clients/{clientAccountid}`.
	Client string `json:"client,omitempty"`
	// DisplayName: Required. The display name of the proposal being created by
	// this RFP.
	DisplayName string `json:"displayName,omitempty"`
	// EstimatedGrossSpend: Specified by buyers in request for proposal (RFP) to
	// notify publisher the total estimated spend for the proposal. Publishers will
	// receive this information and send back proposed deals accordingly.
	EstimatedGrossSpend *Money `json:"estimatedGrossSpend,omitempty"`
	// FlightEndTime: Required. Proposed flight end time of the RFP. A timestamp in
	// RFC3339 UTC "Zulu" format. Note that the specified value will be truncated
	// to a granularity of one second.
	FlightEndTime string `json:"flightEndTime,omitempty"`
	// FlightStartTime: Required. Proposed flight start time of the RFP. A
	// timestamp in RFC3339 UTC "Zulu" format. Note that the specified value will
	// be truncated to a granularity of one second.
	FlightStartTime string `json:"flightStartTime,omitempty"`
	// GeoTargeting: Geo criteria IDs to be targeted. Refer to Geo tables.
	GeoTargeting *CriteriaTargeting `json:"geoTargeting,omitempty"`
	// InventorySizeTargeting: Inventory sizes to be targeted. Only PIXEL inventory
	// size type is supported.
	InventorySizeTargeting *InventorySizeTargeting `json:"inventorySizeTargeting,omitempty"`
	// Note: A message that is sent to the publisher. Maximum length is 1024
	// characters.
	Note string `json:"note,omitempty"`
	// PreferredDealTerms: The terms for preferred deals.
	PreferredDealTerms *PreferredDealTerms `json:"preferredDealTerms,omitempty"`
	// ProgrammaticGuaranteedTerms: The terms for programmatic guaranteed deals.
	ProgrammaticGuaranteedTerms *ProgrammaticGuaranteedTerms `json:"programmaticGuaranteedTerms,omitempty"`
	// PublisherProfile: Required. The profile of the publisher who will receive
	// this RFP in the format:
	// `buyers/{accountId}/publisherProfiles/{publisherProfileId}`.
	PublisherProfile string `json:"publisherProfile,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BuyerContacts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuyerContacts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SendRfpRequest: Request to send an RFP. All fields in this request are proposed to publisher and subject to changes by publisher during later negotiation.

func (SendRfpRequest) MarshalJSON ¶
func (s SendRfpRequest) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Bidders *BiddersService

	Buyers *BuyersService

	Curators *CuratorsService

	MediaPlanners *MediaPlannersService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type SetReadyToServeRequest ¶
type SetReadyToServeRequest struct {
}

SetReadyToServeRequest: Request message for setting ready to serve for a finalized deal.

type StringTargetingDimension ¶
added in v0.259.0
type StringTargetingDimension struct {
	// SelectionType: Required. How the items in this list should be targeted.
	//
	// Possible values:
	//   "SELECTION_TYPE_UNSPECIFIED" - Unspecified selection type. Should not be
	// used.
	//   "SELECTION_TYPE_INCLUDE" - The values in the targeting dimension are
	// included.
	//   "SELECTION_TYPE_EXCLUDE" - The values in the targeting dimension are
	// excluded.
	SelectionType string `json:"selectionType,omitempty"`
	// Values: Required. The values specified.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SelectionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SelectionType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

StringTargetingDimension: Generic targeting with string values.

func (StringTargetingDimension) MarshalJSON ¶
added in v0.259.0
func (s StringTargetingDimension) MarshalJSON() ([]byte, error)
type SubscribeAuctionPackageRequest ¶
type SubscribeAuctionPackageRequest struct {
}

SubscribeAuctionPackageRequest: Request message for SubscribeAuctionPackage.

type SubscribeClientsRequest ¶
type SubscribeClientsRequest struct {
	// Clients: Optional. A list of client buyers to subscribe to the auction
	// package, with client buyer in the format
	// `buyers/{accountId}/clients/{clientAccountId}`. The current buyer will be
	// subscribed to the auction package regardless of the list contents if not
	// already.
	Clients []string `json:"clients,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Clients") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Clients") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SubscribeClientsRequest: Request message for SubscribeAuctionPackageClients.

func (SubscribeClientsRequest) MarshalJSON ¶
func (s SubscribeClientsRequest) MarshalJSON() ([]byte, error)
type TaxonomyTargeting ¶
added in v0.259.0
type TaxonomyTargeting struct {
	// ExcludedTaxonomyIds: Optional. The list of excluded content taxonomy IDs.
	ExcludedTaxonomyIds []string `json:"excludedTaxonomyIds,omitempty"`
	// TargetedTaxonomyIds: Optional. The list of targeted content taxonomy IDs.
	TargetedTaxonomyIds []string `json:"targetedTaxonomyIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedTaxonomyIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedTaxonomyIds") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TaxonomyTargeting: Defines targeting criteria for handling the IAB audience and content Taxonomy ID space.

func (TaxonomyTargeting) MarshalJSON ¶
added in v0.259.0
func (s TaxonomyTargeting) MarshalJSON() ([]byte, error)
type TechnologyTargeting ¶
type TechnologyTargeting struct {
	// DeviceCapabilityTargeting: IDs of device capabilities to be
	// included/excluded.
	DeviceCapabilityTargeting *CriteriaTargeting `json:"deviceCapabilityTargeting,omitempty"`
	// DeviceCategoryTargeting: IDs of device categories to be included/excluded.
	DeviceCategoryTargeting *CriteriaTargeting `json:"deviceCategoryTargeting,omitempty"`
	// OperatingSystemTargeting: Operating system related targeting information.
	OperatingSystemTargeting *OperatingSystemTargeting `json:"operatingSystemTargeting,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceCapabilityTargeting")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceCapabilityTargeting") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TechnologyTargeting: Represents targeting about various types of technology.

func (TechnologyTargeting) MarshalJSON ¶
func (s TechnologyTargeting) MarshalJSON() ([]byte, error)
type TimeOfDay ¶
type TimeOfDay struct {
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

TimeOfDay: Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`.

func (TimeOfDay) MarshalJSON ¶
func (s TimeOfDay) MarshalJSON() ([]byte, error)
type TimeZone ¶
type TimeZone struct {
	// Id: IANA Time Zone Database time zone. For example "America/New_York".
	Id string `json:"id,omitempty"`
	// Version: Optional. IANA Time Zone Database version number. For example
	// "2019a".
	Version string `json:"version,omitempty"`
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

TimeZone: Represents a time zone from the IANA Time Zone Database (https://www.iana.org/time-zones).

func (TimeZone) MarshalJSON ¶
func (s TimeZone) MarshalJSON() ([]byte, error)
type UnsubscribeAuctionPackageRequest ¶
type UnsubscribeAuctionPackageRequest struct {
}

UnsubscribeAuctionPackageRequest: Request message for UnsubscribeAuctionPackage.

type UnsubscribeClientsRequest ¶
type UnsubscribeClientsRequest struct {
	// Clients: Optional. A list of client buyers to unsubscribe from the auction
	// package, with client buyer in the format
	// `buyers/{accountId}/clients/{clientAccountId}`.
	Clients []string `json:"clients,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Clients") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Clients") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UnsubscribeClientsRequest: Request message for UnsubscribeAuctionPackage.

func (UnsubscribeClientsRequest) MarshalJSON ¶
func (s UnsubscribeClientsRequest) MarshalJSON() ([]byte, error)
type UpdateDealRequest ¶
type UpdateDealRequest struct {
	// Deal: Required. The deal to update. The deal's `name` field is used to
	// identify the deal to be updated. Note: proposal_revision will have to be
	// provided within the resource or else an error will be thrown. Format:
	// buyers/{accountId}/proposals/{proposalId}/deals/{dealId}
	Deal *Deal `json:"deal,omitempty"`
	// UpdateMask: List of fields to be updated. If empty or unspecified, the
	// service will update all fields populated in the update request excluding the
	// output only fields and primitive fields with default value. Note that
	// explicit field mask is required in order to reset a primitive field back to
	// its default value, for example, false for boolean fields, 0 for integer
	// fields. A special field mask consisting of a single path "*" can be used to
	// indicate full replacement(the equivalent of PUT method), updatable fields
	// unset or unspecified in the input will be cleared or set to default value.
	// Output only fields will be ignored regardless of the value of updateMask.
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Deal") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Deal") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UpdateDealRequest: Request message for updating the deal at the given revision number.

func (UpdateDealRequest) MarshalJSON ¶
func (s UpdateDealRequest) MarshalJSON() ([]byte, error)
type UriTargeting ¶
type UriTargeting struct {
	// ExcludedUris: A list of URLs to be excluded.
	ExcludedUris []string `json:"excludedUris,omitempty"`
	// TargetedUris: A list of URLs to be included.
	TargetedUris []string `json:"targetedUris,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedUris") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedUris") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UriTargeting: Represents a list of targeted and excluded URLs (for example, google.com). For Private Auction Deals, URLs are either included or excluded. For Programmatic Guaranteed and Preferred Deals, this doesn't apply.

func (UriTargeting) MarshalJSON ¶
func (s UriTargeting) MarshalJSON() ([]byte, error)
type VideoPlayerSizeTargeting ¶
added in v0.259.0
type VideoPlayerSizeTargeting struct {
	// MinimumHeight: Required. The minimum height of the video player in pixels.
	MinimumHeight int64 `json:"minimumHeight,omitempty,string"`
	// MinimumWidth: Required. The minimum width of the video player in pixels.
	MinimumWidth int64 `json:"minimumWidth,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "MinimumHeight") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MinimumHeight") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VideoPlayerSizeTargeting: Represents the size of the video player that can be targeted. Both width and height are required to be set to non-zero values.

func (VideoPlayerSizeTargeting) MarshalJSON ¶
added in v0.259.0
func (s VideoPlayerSizeTargeting) MarshalJSON() ([]byte, error)
type VideoPlcmtTargeting ¶
added in v0.259.0
type VideoPlcmtTargeting struct {
	// SelectionType: Required. The selection type for the list of video plcmts.
	//
	// Possible values:
	//   "SELECTION_TYPE_UNSPECIFIED" - Unspecified selection type. Should not be
	// used.
	//   "SELECTION_TYPE_INCLUDE" - The values in the targeting dimension are
	// included.
	//   "SELECTION_TYPE_EXCLUDE" - The values in the targeting dimension are
	// excluded.
	SelectionType string `json:"selectionType,omitempty"`
	// VideoPlcmtTypes: Required. The list of targeted video plcmts types. If
	// empty, inventory will be targeted regardless of video plcmt type.
	//
	// Possible values:
	//   "VIDEO_PLCMT_TYPE_UNSPECIFIED" - Default value. Should not be used in
	// targeting specifications.
	//   "INSTREAM" - Pre-roll, mid-roll, and post-roll ads that are played before,
	// during or after the streaming video content that the consumer has requested.
	// Instream video must be set to “sound on” by default at player start, or
	// have explicitly clear user intent to watch the video content. While there
	// may be other content surrounding the player, the video content must be the
	// focus of the user’s visit. It should remain the primary content on the
	// page and the only video player in-view capable of audio when playing. If the
	// player converts to floating/sticky, subsequent ad calls should accurately
	// convey the updated player size.
	//   "ACCOMPANYING_CONTENT" - Pre-roll, mid-roll, and post-roll ads that are
	// played before, during, or after streaming video content. The video player
	// loads and plays before, between, or after paragraphs of text or graphical
	// content, and starts playing only when it enters the viewport. Accompanying
	// content should only start playback upon entering the viewport. It may
	// convert to a floating/sticky player as it scrolls off the page.
	//   "INTERSTITIAL" - Video ads that are played without video content. During
	// playback, it must be the primary focus of the page and take up the majority
	// of the viewport and cannot be scrolled out of view. This can be in
	// placements like in-app video or slideshows.
	//   "NO_CONTENT" - Video ads that are played without streaming video content.
	// This can be in placements like slideshows, native feeds, in-content or
	// sticky/floating.
	VideoPlcmtTypes []string `json:"videoPlcmtTypes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "SelectionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "SelectionType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VideoPlcmtTargeting: Defines targeting criteria based on the video placement type, often corresponding to the IAB OpenRTB 'plcmt' field.

func (VideoPlcmtTargeting) MarshalJSON ¶
added in v0.259.0
func (s VideoPlcmtTargeting) MarshalJSON() ([]byte, error)
type VideoTargeting ¶
type VideoTargeting struct {
	// ExcludedPositionTypes: A list of video positions to be excluded. When this
	// field is populated, the targeted_position_types field must be empty.
	//
	// Possible values:
	//   "POSITION_TYPE_UNSPECIFIED" - A placeholder for an undefined video
	// position.
	//   "PREROLL" - Ad is played before the video.
	//   "MIDROLL" - Ad is played during the video.
	//   "POSTROLL" - Ad is played after the video.
	ExcludedPositionTypes []string `json:"excludedPositionTypes,omitempty"`
	// TargetedPositionTypes: A list of video positions to be included. When this
	// field is populated, the excluded_position_types field must be empty.
	//
	// Possible values:
	//   "POSITION_TYPE_UNSPECIFIED" - A placeholder for an undefined video
	// position.
	//   "PREROLL" - Ad is played before the video.
	//   "MIDROLL" - Ad is played during the video.
	//   "POSTROLL" - Ad is played after the video.
	TargetedPositionTypes []string `json:"targetedPositionTypes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedPositionTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedPositionTypes") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VideoTargeting: Represents targeting information about video.

func (VideoTargeting) MarshalJSON ¶
func (s VideoTargeting) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
authorizedbuyersmarketplace-gen.go
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
