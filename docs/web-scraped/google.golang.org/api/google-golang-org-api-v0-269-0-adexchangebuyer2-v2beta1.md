# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer2/v2beta1

Title: adexchangebuyer2 package - google.golang.org/api/adexchangebuyer2/v2beta1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adexchangebuyer2/v2beta1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
adexchangebuyer2
 
v2beta1
adexchangebuyer2
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

Package adexchangebuyer2 provides access to the Ad Exchange Buyer API II.

For product documentation, see: https://developers.google.com/authorized-buyers/apis/reference/rest/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/adexchangebuyer2/v2beta1"
...
ctx := context.Background()
adexchangebuyer2Service, err := adexchangebuyer2.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

adexchangebuyer2Service, err := adexchangebuyer2.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adexchangebuyer2Service, err := adexchangebuyer2.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AbsoluteDateRange
func (s AbsoluteDateRange) MarshalJSON() ([]byte, error)
type AcceptProposalRequest
func (s AcceptProposalRequest) MarshalJSON() ([]byte, error)
type AccountsClientsCreateCall
func (c *AccountsClientsCreateCall) Context(ctx context.Context) *AccountsClientsCreateCall
func (c *AccountsClientsCreateCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *AccountsClientsCreateCall) Fields(s ...googleapi.Field) *AccountsClientsCreateCall
func (c *AccountsClientsCreateCall) Header() http.Header
type AccountsClientsGetCall
func (c *AccountsClientsGetCall) Context(ctx context.Context) *AccountsClientsGetCall
func (c *AccountsClientsGetCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *AccountsClientsGetCall) Fields(s ...googleapi.Field) *AccountsClientsGetCall
func (c *AccountsClientsGetCall) Header() http.Header
func (c *AccountsClientsGetCall) IfNoneMatch(entityTag string) *AccountsClientsGetCall
type AccountsClientsInvitationsCreateCall
func (c *AccountsClientsInvitationsCreateCall) Context(ctx context.Context) *AccountsClientsInvitationsCreateCall
func (c *AccountsClientsInvitationsCreateCall) Do(opts ...googleapi.CallOption) (*ClientUserInvitation, error)
func (c *AccountsClientsInvitationsCreateCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsCreateCall
func (c *AccountsClientsInvitationsCreateCall) Header() http.Header
type AccountsClientsInvitationsGetCall
func (c *AccountsClientsInvitationsGetCall) Context(ctx context.Context) *AccountsClientsInvitationsGetCall
func (c *AccountsClientsInvitationsGetCall) Do(opts ...googleapi.CallOption) (*ClientUserInvitation, error)
func (c *AccountsClientsInvitationsGetCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsGetCall
func (c *AccountsClientsInvitationsGetCall) Header() http.Header
func (c *AccountsClientsInvitationsGetCall) IfNoneMatch(entityTag string) *AccountsClientsInvitationsGetCall
type AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) Context(ctx context.Context) *AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) Do(opts ...googleapi.CallOption) (*ListClientUserInvitationsResponse, error)
func (c *AccountsClientsInvitationsListCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) Header() http.Header
func (c *AccountsClientsInvitationsListCall) IfNoneMatch(entityTag string) *AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) PageSize(pageSize int64) *AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) PageToken(pageToken string) *AccountsClientsInvitationsListCall
func (c *AccountsClientsInvitationsListCall) Pages(ctx context.Context, f func(*ListClientUserInvitationsResponse) error) error
type AccountsClientsInvitationsService
func NewAccountsClientsInvitationsService(s *Service) *AccountsClientsInvitationsService
func (r *AccountsClientsInvitationsService) Create(accountId int64, clientAccountId int64, ...) *AccountsClientsInvitationsCreateCall
func (r *AccountsClientsInvitationsService) Get(accountId int64, clientAccountId int64, invitationId int64) *AccountsClientsInvitationsGetCall
func (r *AccountsClientsInvitationsService) List(accountId int64, clientAccountId string) *AccountsClientsInvitationsListCall
type AccountsClientsListCall
func (c *AccountsClientsListCall) Context(ctx context.Context) *AccountsClientsListCall
func (c *AccountsClientsListCall) Do(opts ...googleapi.CallOption) (*ListClientsResponse, error)
func (c *AccountsClientsListCall) Fields(s ...googleapi.Field) *AccountsClientsListCall
func (c *AccountsClientsListCall) Header() http.Header
func (c *AccountsClientsListCall) IfNoneMatch(entityTag string) *AccountsClientsListCall
func (c *AccountsClientsListCall) PageSize(pageSize int64) *AccountsClientsListCall
func (c *AccountsClientsListCall) PageToken(pageToken string) *AccountsClientsListCall
func (c *AccountsClientsListCall) Pages(ctx context.Context, f func(*ListClientsResponse) error) error
func (c *AccountsClientsListCall) PartnerClientId(partnerClientId string) *AccountsClientsListCall
type AccountsClientsService
func NewAccountsClientsService(s *Service) *AccountsClientsService
func (r *AccountsClientsService) Create(accountId int64, client *Client) *AccountsClientsCreateCall
func (r *AccountsClientsService) Get(accountId int64, clientAccountId int64) *AccountsClientsGetCall
func (r *AccountsClientsService) List(accountId int64) *AccountsClientsListCall
func (r *AccountsClientsService) Update(accountId int64, clientAccountId int64, client *Client) *AccountsClientsUpdateCall
type AccountsClientsUpdateCall
func (c *AccountsClientsUpdateCall) Context(ctx context.Context) *AccountsClientsUpdateCall
func (c *AccountsClientsUpdateCall) Do(opts ...googleapi.CallOption) (*Client, error)
func (c *AccountsClientsUpdateCall) Fields(s ...googleapi.Field) *AccountsClientsUpdateCall
func (c *AccountsClientsUpdateCall) Header() http.Header
type AccountsClientsUsersGetCall
func (c *AccountsClientsUsersGetCall) Context(ctx context.Context) *AccountsClientsUsersGetCall
func (c *AccountsClientsUsersGetCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *AccountsClientsUsersGetCall) Fields(s ...googleapi.Field) *AccountsClientsUsersGetCall
func (c *AccountsClientsUsersGetCall) Header() http.Header
func (c *AccountsClientsUsersGetCall) IfNoneMatch(entityTag string) *AccountsClientsUsersGetCall
type AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) Context(ctx context.Context) *AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) Do(opts ...googleapi.CallOption) (*ListClientUsersResponse, error)
func (c *AccountsClientsUsersListCall) Fields(s ...googleapi.Field) *AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) Header() http.Header
func (c *AccountsClientsUsersListCall) IfNoneMatch(entityTag string) *AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) PageSize(pageSize int64) *AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) PageToken(pageToken string) *AccountsClientsUsersListCall
func (c *AccountsClientsUsersListCall) Pages(ctx context.Context, f func(*ListClientUsersResponse) error) error
type AccountsClientsUsersService
func NewAccountsClientsUsersService(s *Service) *AccountsClientsUsersService
func (r *AccountsClientsUsersService) Get(accountId int64, clientAccountId int64, userId int64) *AccountsClientsUsersGetCall
func (r *AccountsClientsUsersService) List(accountId int64, clientAccountId string) *AccountsClientsUsersListCall
func (r *AccountsClientsUsersService) Update(accountId int64, clientAccountId int64, userId int64, clientuser *ClientUser) *AccountsClientsUsersUpdateCall
type AccountsClientsUsersUpdateCall
func (c *AccountsClientsUsersUpdateCall) Context(ctx context.Context) *AccountsClientsUsersUpdateCall
func (c *AccountsClientsUsersUpdateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)
func (c *AccountsClientsUsersUpdateCall) Fields(s ...googleapi.Field) *AccountsClientsUsersUpdateCall
func (c *AccountsClientsUsersUpdateCall) Header() http.Header
type AccountsCreativesCreateCall
func (c *AccountsCreativesCreateCall) Context(ctx context.Context) *AccountsCreativesCreateCall
func (c *AccountsCreativesCreateCall) Do(opts ...googleapi.CallOption) (*Creative, error)
func (c *AccountsCreativesCreateCall) DuplicateIdMode(duplicateIdMode string) *AccountsCreativesCreateCall
func (c *AccountsCreativesCreateCall) Fields(s ...googleapi.Field) *AccountsCreativesCreateCall
func (c *AccountsCreativesCreateCall) Header() http.Header
type AccountsCreativesDealAssociationsAddCall
func (c *AccountsCreativesDealAssociationsAddCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsAddCall
func (c *AccountsCreativesDealAssociationsAddCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AccountsCreativesDealAssociationsAddCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsAddCall
func (c *AccountsCreativesDealAssociationsAddCall) Header() http.Header
type AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) Do(opts ...googleapi.CallOption) (*ListDealAssociationsResponse, error)
func (c *AccountsCreativesDealAssociationsListCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) Header() http.Header
func (c *AccountsCreativesDealAssociationsListCall) IfNoneMatch(entityTag string) *AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) PageSize(pageSize int64) *AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) PageToken(pageToken string) *AccountsCreativesDealAssociationsListCall
func (c *AccountsCreativesDealAssociationsListCall) Pages(ctx context.Context, f func(*ListDealAssociationsResponse) error) error
func (c *AccountsCreativesDealAssociationsListCall) Query(query string) *AccountsCreativesDealAssociationsListCall
type AccountsCreativesDealAssociationsRemoveCall
func (c *AccountsCreativesDealAssociationsRemoveCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsRemoveCall
func (c *AccountsCreativesDealAssociationsRemoveCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AccountsCreativesDealAssociationsRemoveCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsRemoveCall
func (c *AccountsCreativesDealAssociationsRemoveCall) Header() http.Header
type AccountsCreativesDealAssociationsService
func NewAccountsCreativesDealAssociationsService(s *Service) *AccountsCreativesDealAssociationsService
func (r *AccountsCreativesDealAssociationsService) Add(accountId string, creativeId string, ...) *AccountsCreativesDealAssociationsAddCall
func (r *AccountsCreativesDealAssociationsService) List(accountId string, creativeId string) *AccountsCreativesDealAssociationsListCall
func (r *AccountsCreativesDealAssociationsService) Remove(accountId string, creativeId string, ...) *AccountsCreativesDealAssociationsRemoveCall
type AccountsCreativesGetCall
func (c *AccountsCreativesGetCall) Context(ctx context.Context) *AccountsCreativesGetCall
func (c *AccountsCreativesGetCall) Do(opts ...googleapi.CallOption) (*Creative, error)
func (c *AccountsCreativesGetCall) Fields(s ...googleapi.Field) *AccountsCreativesGetCall
func (c *AccountsCreativesGetCall) Header() http.Header
func (c *AccountsCreativesGetCall) IfNoneMatch(entityTag string) *AccountsCreativesGetCall
type AccountsCreativesListCall
func (c *AccountsCreativesListCall) Context(ctx context.Context) *AccountsCreativesListCall
func (c *AccountsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativesResponse, error)
func (c *AccountsCreativesListCall) Fields(s ...googleapi.Field) *AccountsCreativesListCall
func (c *AccountsCreativesListCall) Header() http.Header
func (c *AccountsCreativesListCall) IfNoneMatch(entityTag string) *AccountsCreativesListCall
func (c *AccountsCreativesListCall) PageSize(pageSize int64) *AccountsCreativesListCall
func (c *AccountsCreativesListCall) PageToken(pageToken string) *AccountsCreativesListCall
func (c *AccountsCreativesListCall) Pages(ctx context.Context, f func(*ListCreativesResponse) error) error
func (c *AccountsCreativesListCall) Query(query string) *AccountsCreativesListCall
type AccountsCreativesService
func NewAccountsCreativesService(s *Service) *AccountsCreativesService
func (r *AccountsCreativesService) Create(accountId string, creative *Creative) *AccountsCreativesCreateCall
func (r *AccountsCreativesService) Get(accountId string, creativeId string) *AccountsCreativesGetCall
func (r *AccountsCreativesService) List(accountId string) *AccountsCreativesListCall
func (r *AccountsCreativesService) StopWatching(accountId string, creativeId string, ...) *AccountsCreativesStopWatchingCall
func (r *AccountsCreativesService) Update(accountId string, creativeId string, creative *Creative) *AccountsCreativesUpdateCall
func (r *AccountsCreativesService) Watch(accountId string, creativeId string, ...) *AccountsCreativesWatchCall
type AccountsCreativesStopWatchingCall
func (c *AccountsCreativesStopWatchingCall) Context(ctx context.Context) *AccountsCreativesStopWatchingCall
func (c *AccountsCreativesStopWatchingCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AccountsCreativesStopWatchingCall) Fields(s ...googleapi.Field) *AccountsCreativesStopWatchingCall
func (c *AccountsCreativesStopWatchingCall) Header() http.Header
type AccountsCreativesUpdateCall
func (c *AccountsCreativesUpdateCall) Context(ctx context.Context) *AccountsCreativesUpdateCall
func (c *AccountsCreativesUpdateCall) Do(opts ...googleapi.CallOption) (*Creative, error)
func (c *AccountsCreativesUpdateCall) Fields(s ...googleapi.Field) *AccountsCreativesUpdateCall
func (c *AccountsCreativesUpdateCall) Header() http.Header
type AccountsCreativesWatchCall
func (c *AccountsCreativesWatchCall) Context(ctx context.Context) *AccountsCreativesWatchCall
func (c *AccountsCreativesWatchCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *AccountsCreativesWatchCall) Fields(s ...googleapi.Field) *AccountsCreativesWatchCall
func (c *AccountsCreativesWatchCall) Header() http.Header
type AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) Context(ctx context.Context) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)
func (c *AccountsFinalizedProposalsListCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) Filter(filter string) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) FilterSyntax(filterSyntax string) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) Header() http.Header
func (c *AccountsFinalizedProposalsListCall) IfNoneMatch(entityTag string) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) PageSize(pageSize int64) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) PageToken(pageToken string) *AccountsFinalizedProposalsListCall
func (c *AccountsFinalizedProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error
type AccountsFinalizedProposalsPauseCall
func (c *AccountsFinalizedProposalsPauseCall) Context(ctx context.Context) *AccountsFinalizedProposalsPauseCall
func (c *AccountsFinalizedProposalsPauseCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsFinalizedProposalsPauseCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsPauseCall
func (c *AccountsFinalizedProposalsPauseCall) Header() http.Header
type AccountsFinalizedProposalsResumeCall
func (c *AccountsFinalizedProposalsResumeCall) Context(ctx context.Context) *AccountsFinalizedProposalsResumeCall
func (c *AccountsFinalizedProposalsResumeCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsFinalizedProposalsResumeCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsResumeCall
func (c *AccountsFinalizedProposalsResumeCall) Header() http.Header
type AccountsFinalizedProposalsService
func NewAccountsFinalizedProposalsService(s *Service) *AccountsFinalizedProposalsService
func (r *AccountsFinalizedProposalsService) List(accountId string) *AccountsFinalizedProposalsListCall
func (r *AccountsFinalizedProposalsService) Pause(accountId string, proposalId string, ...) *AccountsFinalizedProposalsPauseCall
func (r *AccountsFinalizedProposalsService) Resume(accountId string, proposalId string, ...) *AccountsFinalizedProposalsResumeCall
type AccountsProductsGetCall
func (c *AccountsProductsGetCall) Context(ctx context.Context) *AccountsProductsGetCall
func (c *AccountsProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)
func (c *AccountsProductsGetCall) Fields(s ...googleapi.Field) *AccountsProductsGetCall
func (c *AccountsProductsGetCall) Header() http.Header
func (c *AccountsProductsGetCall) IfNoneMatch(entityTag string) *AccountsProductsGetCall
type AccountsProductsListCall
func (c *AccountsProductsListCall) Context(ctx context.Context) *AccountsProductsListCall
func (c *AccountsProductsListCall) Do(opts ...googleapi.CallOption) (*ListProductsResponse, error)
func (c *AccountsProductsListCall) Fields(s ...googleapi.Field) *AccountsProductsListCall
func (c *AccountsProductsListCall) Filter(filter string) *AccountsProductsListCall
func (c *AccountsProductsListCall) Header() http.Header
func (c *AccountsProductsListCall) IfNoneMatch(entityTag string) *AccountsProductsListCall
func (c *AccountsProductsListCall) PageSize(pageSize int64) *AccountsProductsListCall
func (c *AccountsProductsListCall) PageToken(pageToken string) *AccountsProductsListCall
func (c *AccountsProductsListCall) Pages(ctx context.Context, f func(*ListProductsResponse) error) error
type AccountsProductsService
func NewAccountsProductsService(s *Service) *AccountsProductsService
func (r *AccountsProductsService) Get(accountId string, productId string) *AccountsProductsGetCall
func (r *AccountsProductsService) List(accountId string) *AccountsProductsListCall
type AccountsProposalsAcceptCall
func (c *AccountsProposalsAcceptCall) Context(ctx context.Context) *AccountsProposalsAcceptCall
func (c *AccountsProposalsAcceptCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsAcceptCall) Fields(s ...googleapi.Field) *AccountsProposalsAcceptCall
func (c *AccountsProposalsAcceptCall) Header() http.Header
type AccountsProposalsAddNoteCall
func (c *AccountsProposalsAddNoteCall) Context(ctx context.Context) *AccountsProposalsAddNoteCall
func (c *AccountsProposalsAddNoteCall) Do(opts ...googleapi.CallOption) (*Note, error)
func (c *AccountsProposalsAddNoteCall) Fields(s ...googleapi.Field) *AccountsProposalsAddNoteCall
func (c *AccountsProposalsAddNoteCall) Header() http.Header
type AccountsProposalsCancelNegotiationCall
func (c *AccountsProposalsCancelNegotiationCall) Context(ctx context.Context) *AccountsProposalsCancelNegotiationCall
func (c *AccountsProposalsCancelNegotiationCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsCancelNegotiationCall) Fields(s ...googleapi.Field) *AccountsProposalsCancelNegotiationCall
func (c *AccountsProposalsCancelNegotiationCall) Header() http.Header
type AccountsProposalsCompleteSetupCall
func (c *AccountsProposalsCompleteSetupCall) Context(ctx context.Context) *AccountsProposalsCompleteSetupCall
func (c *AccountsProposalsCompleteSetupCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsCompleteSetupCall) Fields(s ...googleapi.Field) *AccountsProposalsCompleteSetupCall
func (c *AccountsProposalsCompleteSetupCall) Header() http.Header
type AccountsProposalsCreateCall
func (c *AccountsProposalsCreateCall) Context(ctx context.Context) *AccountsProposalsCreateCall
func (c *AccountsProposalsCreateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsCreateCall) Fields(s ...googleapi.Field) *AccountsProposalsCreateCall
func (c *AccountsProposalsCreateCall) Header() http.Header
type AccountsProposalsGetCall
func (c *AccountsProposalsGetCall) Context(ctx context.Context) *AccountsProposalsGetCall
func (c *AccountsProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsGetCall) Fields(s ...googleapi.Field) *AccountsProposalsGetCall
func (c *AccountsProposalsGetCall) Header() http.Header
func (c *AccountsProposalsGetCall) IfNoneMatch(entityTag string) *AccountsProposalsGetCall
type AccountsProposalsListCall
func (c *AccountsProposalsListCall) Context(ctx context.Context) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)
func (c *AccountsProposalsListCall) Fields(s ...googleapi.Field) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) Filter(filter string) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) FilterSyntax(filterSyntax string) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) Header() http.Header
func (c *AccountsProposalsListCall) IfNoneMatch(entityTag string) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) PageSize(pageSize int64) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) PageToken(pageToken string) *AccountsProposalsListCall
func (c *AccountsProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error
type AccountsProposalsPauseCall
func (c *AccountsProposalsPauseCall) Context(ctx context.Context) *AccountsProposalsPauseCall
func (c *AccountsProposalsPauseCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsPauseCall) Fields(s ...googleapi.Field) *AccountsProposalsPauseCall
func (c *AccountsProposalsPauseCall) Header() http.Header
type AccountsProposalsResumeCall
func (c *AccountsProposalsResumeCall) Context(ctx context.Context) *AccountsProposalsResumeCall
func (c *AccountsProposalsResumeCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsResumeCall) Fields(s ...googleapi.Field) *AccountsProposalsResumeCall
func (c *AccountsProposalsResumeCall) Header() http.Header
type AccountsProposalsService
func NewAccountsProposalsService(s *Service) *AccountsProposalsService
func (r *AccountsProposalsService) Accept(accountId string, proposalId string, ...) *AccountsProposalsAcceptCall
func (r *AccountsProposalsService) AddNote(accountId string, proposalId string, addnoterequest *AddNoteRequest) *AccountsProposalsAddNoteCall
func (r *AccountsProposalsService) CancelNegotiation(accountId string, proposalId string, ...) *AccountsProposalsCancelNegotiationCall
func (r *AccountsProposalsService) CompleteSetup(accountId string, proposalId string, ...) *AccountsProposalsCompleteSetupCall
func (r *AccountsProposalsService) Create(accountId string, proposal *Proposal) *AccountsProposalsCreateCall
func (r *AccountsProposalsService) Get(accountId string, proposalId string) *AccountsProposalsGetCall
func (r *AccountsProposalsService) List(accountId string) *AccountsProposalsListCall
func (r *AccountsProposalsService) Pause(accountId string, proposalId string, ...) *AccountsProposalsPauseCall
func (r *AccountsProposalsService) Resume(accountId string, proposalId string, ...) *AccountsProposalsResumeCall
func (r *AccountsProposalsService) Update(accountId string, proposalId string, proposal *Proposal) *AccountsProposalsUpdateCall
type AccountsProposalsUpdateCall
func (c *AccountsProposalsUpdateCall) Context(ctx context.Context) *AccountsProposalsUpdateCall
func (c *AccountsProposalsUpdateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)
func (c *AccountsProposalsUpdateCall) Fields(s ...googleapi.Field) *AccountsProposalsUpdateCall
func (c *AccountsProposalsUpdateCall) Header() http.Header
type AccountsPublisherProfilesGetCall
func (c *AccountsPublisherProfilesGetCall) Context(ctx context.Context) *AccountsPublisherProfilesGetCall
func (c *AccountsPublisherProfilesGetCall) Do(opts ...googleapi.CallOption) (*PublisherProfile, error)
func (c *AccountsPublisherProfilesGetCall) Fields(s ...googleapi.Field) *AccountsPublisherProfilesGetCall
func (c *AccountsPublisherProfilesGetCall) Header() http.Header
func (c *AccountsPublisherProfilesGetCall) IfNoneMatch(entityTag string) *AccountsPublisherProfilesGetCall
type AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) Context(ctx context.Context) *AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) Do(opts ...googleapi.CallOption) (*ListPublisherProfilesResponse, error)
func (c *AccountsPublisherProfilesListCall) Fields(s ...googleapi.Field) *AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) Header() http.Header
func (c *AccountsPublisherProfilesListCall) IfNoneMatch(entityTag string) *AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) PageSize(pageSize int64) *AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) PageToken(pageToken string) *AccountsPublisherProfilesListCall
func (c *AccountsPublisherProfilesListCall) Pages(ctx context.Context, f func(*ListPublisherProfilesResponse) error) error
type AccountsPublisherProfilesService
func NewAccountsPublisherProfilesService(s *Service) *AccountsPublisherProfilesService
func (r *AccountsPublisherProfilesService) Get(accountId string, publisherProfileId string) *AccountsPublisherProfilesGetCall
func (r *AccountsPublisherProfilesService) List(accountId string) *AccountsPublisherProfilesListCall
type AccountsService
func NewAccountsService(s *Service) *AccountsService
type AdSize
func (s AdSize) MarshalJSON() ([]byte, error)
type AdTechnologyProviders
func (s AdTechnologyProviders) MarshalJSON() ([]byte, error)
type AddDealAssociationRequest
func (s AddDealAssociationRequest) MarshalJSON() ([]byte, error)
type AddNoteRequest
func (s AddNoteRequest) MarshalJSON() ([]byte, error)
type AppContext
func (s AppContext) MarshalJSON() ([]byte, error)
type AuctionContext
func (s AuctionContext) MarshalJSON() ([]byte, error)
type BidMetricsRow
func (s BidMetricsRow) MarshalJSON() ([]byte, error)
type BidResponseWithoutBidsStatusRow
func (s BidResponseWithoutBidsStatusRow) MarshalJSON() ([]byte, error)
type BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidMetricsListCall
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error
type BiddersAccountsFilterSetsBidMetricsService
func NewBiddersAccountsFilterSetsBidMetricsService(s *Service) *BiddersAccountsFilterSetsBidMetricsService
func (r *BiddersAccountsFilterSetsBidMetricsService) List(filterSetName string) *BiddersAccountsFilterSetsBidMetricsListCall
type BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidResponseErrorsListCall
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error
type BiddersAccountsFilterSetsBidResponseErrorsService
func NewBiddersAccountsFilterSetsBidResponseErrorsService(s *Service) *BiddersAccountsFilterSetsBidResponseErrorsService
func (r *BiddersAccountsFilterSetsBidResponseErrorsService) List(filterSetName string) *BiddersAccountsFilterSetsBidResponseErrorsListCall
type BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error
type BiddersAccountsFilterSetsBidResponsesWithoutBidsService
func NewBiddersAccountsFilterSetsBidResponsesWithoutBidsService(s *Service) *BiddersAccountsFilterSetsBidResponsesWithoutBidsService
func (r *BiddersAccountsFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall
type BiddersAccountsFilterSetsCreateCall
func (c *BiddersAccountsFilterSetsCreateCall) Context(ctx context.Context) *BiddersAccountsFilterSetsCreateCall
func (c *BiddersAccountsFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BiddersAccountsFilterSetsCreateCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsCreateCall
func (c *BiddersAccountsFilterSetsCreateCall) Header() http.Header
func (c *BiddersAccountsFilterSetsCreateCall) IsTransient(isTransient bool) *BiddersAccountsFilterSetsCreateCall
type BiddersAccountsFilterSetsDeleteCall
func (c *BiddersAccountsFilterSetsDeleteCall) Context(ctx context.Context) *BiddersAccountsFilterSetsDeleteCall
func (c *BiddersAccountsFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *BiddersAccountsFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsDeleteCall
func (c *BiddersAccountsFilterSetsDeleteCall) Header() http.Header
type BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error
type BiddersAccountsFilterSetsFilteredBidRequestsService
func NewBiddersAccountsFilterSetsFilteredBidRequestsService(s *Service) *BiddersAccountsFilterSetsFilteredBidRequestsService
func (r *BiddersAccountsFilterSetsFilteredBidRequestsService) List(filterSetName string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall
type BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, ...) error
type BiddersAccountsFilterSetsFilteredBidsCreativesService
func NewBiddersAccountsFilterSetsFilteredBidsCreativesService(s *Service) *BiddersAccountsFilterSetsFilteredBidsCreativesService
func (r *BiddersAccountsFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall
type BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, ...) error
type BiddersAccountsFilterSetsFilteredBidsDetailsService
func NewBiddersAccountsFilterSetsFilteredBidsDetailsService(s *Service) *BiddersAccountsFilterSetsFilteredBidsDetailsService
func (r *BiddersAccountsFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall
type BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsListCall
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error
type BiddersAccountsFilterSetsFilteredBidsService
func NewBiddersAccountsFilterSetsFilteredBidsService(s *Service) *BiddersAccountsFilterSetsFilteredBidsService
func (r *BiddersAccountsFilterSetsFilteredBidsService) List(filterSetName string) *BiddersAccountsFilterSetsFilteredBidsListCall
type BiddersAccountsFilterSetsGetCall
func (c *BiddersAccountsFilterSetsGetCall) Context(ctx context.Context) *BiddersAccountsFilterSetsGetCall
func (c *BiddersAccountsFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BiddersAccountsFilterSetsGetCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsGetCall
func (c *BiddersAccountsFilterSetsGetCall) Header() http.Header
func (c *BiddersAccountsFilterSetsGetCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsGetCall
type BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsImpressionMetricsListCall
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error
type BiddersAccountsFilterSetsImpressionMetricsService
func NewBiddersAccountsFilterSetsImpressionMetricsService(s *Service) *BiddersAccountsFilterSetsImpressionMetricsService
func (r *BiddersAccountsFilterSetsImpressionMetricsService) List(filterSetName string) *BiddersAccountsFilterSetsImpressionMetricsListCall
type BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)
func (c *BiddersAccountsFilterSetsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsListCall
func (c *BiddersAccountsFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error
type BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsLosingBidsListCall
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error
type BiddersAccountsFilterSetsLosingBidsService
func NewBiddersAccountsFilterSetsLosingBidsService(s *Service) *BiddersAccountsFilterSetsLosingBidsService
func (r *BiddersAccountsFilterSetsLosingBidsService) List(filterSetName string) *BiddersAccountsFilterSetsLosingBidsListCall
type BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Header() http.Header
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error
type BiddersAccountsFilterSetsNonBillableWinningBidsService
func NewBiddersAccountsFilterSetsNonBillableWinningBidsService(s *Service) *BiddersAccountsFilterSetsNonBillableWinningBidsService
func (r *BiddersAccountsFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall
type BiddersAccountsFilterSetsService
func NewBiddersAccountsFilterSetsService(s *Service) *BiddersAccountsFilterSetsService
func (r *BiddersAccountsFilterSetsService) Create(ownerName string, filterset *FilterSet) *BiddersAccountsFilterSetsCreateCall
func (r *BiddersAccountsFilterSetsService) Delete(name string) *BiddersAccountsFilterSetsDeleteCall
func (r *BiddersAccountsFilterSetsService) Get(name string) *BiddersAccountsFilterSetsGetCall
func (r *BiddersAccountsFilterSetsService) List(ownerName string) *BiddersAccountsFilterSetsListCall
type BiddersAccountsService
func NewBiddersAccountsService(s *Service) *BiddersAccountsService
type BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) Context(ctx context.Context) *BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)
func (c *BiddersFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) Header() http.Header
func (c *BiddersFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) PageToken(pageToken string) *BiddersFilterSetsBidMetricsListCall
func (c *BiddersFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error
type BiddersFilterSetsBidMetricsService
func NewBiddersFilterSetsBidMetricsService(s *Service) *BiddersFilterSetsBidMetricsService
func (r *BiddersFilterSetsBidMetricsService) List(filterSetName string) *BiddersFilterSetsBidMetricsListCall
type BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)
func (c *BiddersFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) Header() http.Header
func (c *BiddersFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BiddersFilterSetsBidResponseErrorsListCall
func (c *BiddersFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error
type BiddersFilterSetsBidResponseErrorsService
func NewBiddersFilterSetsBidResponseErrorsService(s *Service) *BiddersFilterSetsBidResponseErrorsService
func (r *BiddersFilterSetsBidResponseErrorsService) List(filterSetName string) *BiddersFilterSetsBidResponseErrorsListCall
type BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BiddersFilterSetsBidResponsesWithoutBidsListCall
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error
type BiddersFilterSetsBidResponsesWithoutBidsService
func NewBiddersFilterSetsBidResponsesWithoutBidsService(s *Service) *BiddersFilterSetsBidResponsesWithoutBidsService
func (r *BiddersFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BiddersFilterSetsBidResponsesWithoutBidsListCall
type BiddersFilterSetsCreateCall
func (c *BiddersFilterSetsCreateCall) Context(ctx context.Context) *BiddersFilterSetsCreateCall
func (c *BiddersFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BiddersFilterSetsCreateCall) Fields(s ...googleapi.Field) *BiddersFilterSetsCreateCall
func (c *BiddersFilterSetsCreateCall) Header() http.Header
func (c *BiddersFilterSetsCreateCall) IsTransient(isTransient bool) *BiddersFilterSetsCreateCall
type BiddersFilterSetsDeleteCall
func (c *BiddersFilterSetsDeleteCall) Context(ctx context.Context) *BiddersFilterSetsDeleteCall
func (c *BiddersFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *BiddersFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BiddersFilterSetsDeleteCall
func (c *BiddersFilterSetsDeleteCall) Header() http.Header
type BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Header() http.Header
func (c *BiddersFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidRequestsListCall
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error
type BiddersFilterSetsFilteredBidRequestsService
func NewBiddersFilterSetsFilteredBidRequestsService(s *Service) *BiddersFilterSetsFilteredBidRequestsService
func (r *BiddersFilterSetsFilteredBidRequestsService) List(filterSetName string) *BiddersFilterSetsFilteredBidRequestsListCall
type BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Header() http.Header
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsCreativesListCall
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, ...) error
type BiddersFilterSetsFilteredBidsCreativesService
func NewBiddersFilterSetsFilteredBidsCreativesService(s *Service) *BiddersFilterSetsFilteredBidsCreativesService
func (r *BiddersFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BiddersFilterSetsFilteredBidsCreativesListCall
type BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Header() http.Header
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsDetailsListCall
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, ...) error
type BiddersFilterSetsFilteredBidsDetailsService
func NewBiddersFilterSetsFilteredBidsDetailsService(s *Service) *BiddersFilterSetsFilteredBidsDetailsService
func (r *BiddersFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BiddersFilterSetsFilteredBidsDetailsListCall
type BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)
func (c *BiddersFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) Header() http.Header
func (c *BiddersFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsListCall
func (c *BiddersFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error
type BiddersFilterSetsFilteredBidsService
func NewBiddersFilterSetsFilteredBidsService(s *Service) *BiddersFilterSetsFilteredBidsService
func (r *BiddersFilterSetsFilteredBidsService) List(filterSetName string) *BiddersFilterSetsFilteredBidsListCall
type BiddersFilterSetsGetCall
func (c *BiddersFilterSetsGetCall) Context(ctx context.Context) *BiddersFilterSetsGetCall
func (c *BiddersFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BiddersFilterSetsGetCall) Fields(s ...googleapi.Field) *BiddersFilterSetsGetCall
func (c *BiddersFilterSetsGetCall) Header() http.Header
func (c *BiddersFilterSetsGetCall) IfNoneMatch(entityTag string) *BiddersFilterSetsGetCall
type BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)
func (c *BiddersFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) Header() http.Header
func (c *BiddersFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BiddersFilterSetsImpressionMetricsListCall
func (c *BiddersFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error
type BiddersFilterSetsImpressionMetricsService
func NewBiddersFilterSetsImpressionMetricsService(s *Service) *BiddersFilterSetsImpressionMetricsService
func (r *BiddersFilterSetsImpressionMetricsService) List(filterSetName string) *BiddersFilterSetsImpressionMetricsListCall
type BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) Context(ctx context.Context) *BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)
func (c *BiddersFilterSetsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) Header() http.Header
func (c *BiddersFilterSetsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) PageSize(pageSize int64) *BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) PageToken(pageToken string) *BiddersFilterSetsListCall
func (c *BiddersFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error
type BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) Context(ctx context.Context) *BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)
func (c *BiddersFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) Header() http.Header
func (c *BiddersFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) PageToken(pageToken string) *BiddersFilterSetsLosingBidsListCall
func (c *BiddersFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error
type BiddersFilterSetsLosingBidsService
func NewBiddersFilterSetsLosingBidsService(s *Service) *BiddersFilterSetsLosingBidsService
func (r *BiddersFilterSetsLosingBidsService) List(filterSetName string) *BiddersFilterSetsLosingBidsListCall
type BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Header() http.Header
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BiddersFilterSetsNonBillableWinningBidsListCall
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error
type BiddersFilterSetsNonBillableWinningBidsService
func NewBiddersFilterSetsNonBillableWinningBidsService(s *Service) *BiddersFilterSetsNonBillableWinningBidsService
func (r *BiddersFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BiddersFilterSetsNonBillableWinningBidsListCall
type BiddersFilterSetsService
func NewBiddersFilterSetsService(s *Service) *BiddersFilterSetsService
func (r *BiddersFilterSetsService) Create(ownerName string, filterset *FilterSet) *BiddersFilterSetsCreateCall
func (r *BiddersFilterSetsService) Delete(name string) *BiddersFilterSetsDeleteCall
func (r *BiddersFilterSetsService) Get(name string) *BiddersFilterSetsGetCall
func (r *BiddersFilterSetsService) List(ownerName string) *BiddersFilterSetsListCall
type BiddersService
func NewBiddersService(s *Service) *BiddersService
type Buyer
func (s Buyer) MarshalJSON() ([]byte, error)
type BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) Context(ctx context.Context) *BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)
func (c *BuyersFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) Header() http.Header
func (c *BuyersFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) PageToken(pageToken string) *BuyersFilterSetsBidMetricsListCall
func (c *BuyersFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error
type BuyersFilterSetsBidMetricsService
func NewBuyersFilterSetsBidMetricsService(s *Service) *BuyersFilterSetsBidMetricsService
func (r *BuyersFilterSetsBidMetricsService) List(filterSetName string) *BuyersFilterSetsBidMetricsListCall
type BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)
func (c *BuyersFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) Header() http.Header
func (c *BuyersFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BuyersFilterSetsBidResponseErrorsListCall
func (c *BuyersFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error
type BuyersFilterSetsBidResponseErrorsService
func NewBuyersFilterSetsBidResponseErrorsService(s *Service) *BuyersFilterSetsBidResponseErrorsService
func (r *BuyersFilterSetsBidResponseErrorsService) List(filterSetName string) *BuyersFilterSetsBidResponseErrorsListCall
type BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BuyersFilterSetsBidResponsesWithoutBidsListCall
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error
type BuyersFilterSetsBidResponsesWithoutBidsService
func NewBuyersFilterSetsBidResponsesWithoutBidsService(s *Service) *BuyersFilterSetsBidResponsesWithoutBidsService
func (r *BuyersFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BuyersFilterSetsBidResponsesWithoutBidsListCall
type BuyersFilterSetsCreateCall
func (c *BuyersFilterSetsCreateCall) Context(ctx context.Context) *BuyersFilterSetsCreateCall
func (c *BuyersFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BuyersFilterSetsCreateCall) Fields(s ...googleapi.Field) *BuyersFilterSetsCreateCall
func (c *BuyersFilterSetsCreateCall) Header() http.Header
func (c *BuyersFilterSetsCreateCall) IsTransient(isTransient bool) *BuyersFilterSetsCreateCall
type BuyersFilterSetsDeleteCall
func (c *BuyersFilterSetsDeleteCall) Context(ctx context.Context) *BuyersFilterSetsDeleteCall
func (c *BuyersFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *BuyersFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BuyersFilterSetsDeleteCall
func (c *BuyersFilterSetsDeleteCall) Header() http.Header
type BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Header() http.Header
func (c *BuyersFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidRequestsListCall
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error
type BuyersFilterSetsFilteredBidRequestsService
func NewBuyersFilterSetsFilteredBidRequestsService(s *Service) *BuyersFilterSetsFilteredBidRequestsService
func (r *BuyersFilterSetsFilteredBidRequestsService) List(filterSetName string) *BuyersFilterSetsFilteredBidRequestsListCall
type BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Header() http.Header
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsCreativesListCall
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, ...) error
type BuyersFilterSetsFilteredBidsCreativesService
func NewBuyersFilterSetsFilteredBidsCreativesService(s *Service) *BuyersFilterSetsFilteredBidsCreativesService
func (r *BuyersFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BuyersFilterSetsFilteredBidsCreativesListCall
type BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Header() http.Header
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsDetailsListCall
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, ...) error
type BuyersFilterSetsFilteredBidsDetailsService
func NewBuyersFilterSetsFilteredBidsDetailsService(s *Service) *BuyersFilterSetsFilteredBidsDetailsService
func (r *BuyersFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BuyersFilterSetsFilteredBidsDetailsListCall
type BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)
func (c *BuyersFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) Header() http.Header
func (c *BuyersFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsListCall
func (c *BuyersFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error
type BuyersFilterSetsFilteredBidsService
func NewBuyersFilterSetsFilteredBidsService(s *Service) *BuyersFilterSetsFilteredBidsService
func (r *BuyersFilterSetsFilteredBidsService) List(filterSetName string) *BuyersFilterSetsFilteredBidsListCall
type BuyersFilterSetsGetCall
func (c *BuyersFilterSetsGetCall) Context(ctx context.Context) *BuyersFilterSetsGetCall
func (c *BuyersFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)
func (c *BuyersFilterSetsGetCall) Fields(s ...googleapi.Field) *BuyersFilterSetsGetCall
func (c *BuyersFilterSetsGetCall) Header() http.Header
func (c *BuyersFilterSetsGetCall) IfNoneMatch(entityTag string) *BuyersFilterSetsGetCall
type BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)
func (c *BuyersFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) Header() http.Header
func (c *BuyersFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BuyersFilterSetsImpressionMetricsListCall
func (c *BuyersFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error
type BuyersFilterSetsImpressionMetricsService
func NewBuyersFilterSetsImpressionMetricsService(s *Service) *BuyersFilterSetsImpressionMetricsService
func (r *BuyersFilterSetsImpressionMetricsService) List(filterSetName string) *BuyersFilterSetsImpressionMetricsListCall
type BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) Context(ctx context.Context) *BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)
func (c *BuyersFilterSetsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) Header() http.Header
func (c *BuyersFilterSetsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) PageSize(pageSize int64) *BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) PageToken(pageToken string) *BuyersFilterSetsListCall
func (c *BuyersFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error
type BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) Context(ctx context.Context) *BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)
func (c *BuyersFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) Header() http.Header
func (c *BuyersFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) PageToken(pageToken string) *BuyersFilterSetsLosingBidsListCall
func (c *BuyersFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error
type BuyersFilterSetsLosingBidsService
func NewBuyersFilterSetsLosingBidsService(s *Service) *BuyersFilterSetsLosingBidsService
func (r *BuyersFilterSetsLosingBidsService) List(filterSetName string) *BuyersFilterSetsLosingBidsListCall
type BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Header() http.Header
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BuyersFilterSetsNonBillableWinningBidsListCall
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error
type BuyersFilterSetsNonBillableWinningBidsService
func NewBuyersFilterSetsNonBillableWinningBidsService(s *Service) *BuyersFilterSetsNonBillableWinningBidsService
func (r *BuyersFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BuyersFilterSetsNonBillableWinningBidsListCall
type BuyersFilterSetsService
func NewBuyersFilterSetsService(s *Service) *BuyersFilterSetsService
func (r *BuyersFilterSetsService) Create(ownerName string, filterset *FilterSet) *BuyersFilterSetsCreateCall
func (r *BuyersFilterSetsService) Delete(name string) *BuyersFilterSetsDeleteCall
func (r *BuyersFilterSetsService) Get(name string) *BuyersFilterSetsGetCall
func (r *BuyersFilterSetsService) List(ownerName string) *BuyersFilterSetsListCall
type BuyersService
func NewBuyersService(s *Service) *BuyersService
type CalloutStatusRow
func (s CalloutStatusRow) MarshalJSON() ([]byte, error)
type CancelNegotiationRequest
type Client
func (s Client) MarshalJSON() ([]byte, error)
type ClientUser
func (s ClientUser) MarshalJSON() ([]byte, error)
type ClientUserInvitation
func (s ClientUserInvitation) MarshalJSON() ([]byte, error)
type CompleteSetupRequest
type ContactInformation
func (s ContactInformation) MarshalJSON() ([]byte, error)
type Correction
func (s Correction) MarshalJSON() ([]byte, error)
type Creative
func (s Creative) MarshalJSON() ([]byte, error)
type CreativeDealAssociation
func (s CreativeDealAssociation) MarshalJSON() ([]byte, error)
type CreativeRestrictions
func (s CreativeRestrictions) MarshalJSON() ([]byte, error)
type CreativeSize
func (s CreativeSize) MarshalJSON() ([]byte, error)
type CreativeSpecification
func (s CreativeSpecification) MarshalJSON() ([]byte, error)
type CreativeStatusRow
func (s CreativeStatusRow) MarshalJSON() ([]byte, error)
type CriteriaTargeting
func (s CriteriaTargeting) MarshalJSON() ([]byte, error)
type Date
func (s Date) MarshalJSON() ([]byte, error)
type DayPart
func (s DayPart) MarshalJSON() ([]byte, error)
type DayPartTargeting
func (s DayPartTargeting) MarshalJSON() ([]byte, error)
type Deal
func (s Deal) MarshalJSON() ([]byte, error)
type DealPauseStatus
func (s DealPauseStatus) MarshalJSON() ([]byte, error)
type DealServingMetadata
func (s DealServingMetadata) MarshalJSON() ([]byte, error)
type DealTerms
func (s DealTerms) MarshalJSON() ([]byte, error)
type DeliveryControl
func (s DeliveryControl) MarshalJSON() ([]byte, error)
type Disapproval
func (s Disapproval) MarshalJSON() ([]byte, error)
type Empty
type FilterSet
func (s FilterSet) MarshalJSON() ([]byte, error)
type FilteredBidCreativeRow
func (s FilteredBidCreativeRow) MarshalJSON() ([]byte, error)
type FilteredBidDetailRow
func (s FilteredBidDetailRow) MarshalJSON() ([]byte, error)
type FirstPartyMobileApplicationTargeting
func (s FirstPartyMobileApplicationTargeting) MarshalJSON() ([]byte, error)
type FrequencyCap
func (s FrequencyCap) MarshalJSON() ([]byte, error)
type GuaranteedFixedPriceTerms
func (s GuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type HtmlContent
func (s HtmlContent) MarshalJSON() ([]byte, error)
type Image
func (s Image) MarshalJSON() ([]byte, error)
type ImpressionMetricsRow
func (s ImpressionMetricsRow) MarshalJSON() ([]byte, error)
type InventorySizeTargeting
func (s InventorySizeTargeting) MarshalJSON() ([]byte, error)
type ListBidMetricsResponse
func (s ListBidMetricsResponse) MarshalJSON() ([]byte, error)
type ListBidResponseErrorsResponse
func (s ListBidResponseErrorsResponse) MarshalJSON() ([]byte, error)
type ListBidResponsesWithoutBidsResponse
func (s ListBidResponsesWithoutBidsResponse) MarshalJSON() ([]byte, error)
type ListClientUserInvitationsResponse
func (s ListClientUserInvitationsResponse) MarshalJSON() ([]byte, error)
type ListClientUsersResponse
func (s ListClientUsersResponse) MarshalJSON() ([]byte, error)
type ListClientsResponse
func (s ListClientsResponse) MarshalJSON() ([]byte, error)
type ListCreativeStatusBreakdownByCreativeResponse
func (s ListCreativeStatusBreakdownByCreativeResponse) MarshalJSON() ([]byte, error)
type ListCreativeStatusBreakdownByDetailResponse
func (s ListCreativeStatusBreakdownByDetailResponse) MarshalJSON() ([]byte, error)
type ListCreativesResponse
func (s ListCreativesResponse) MarshalJSON() ([]byte, error)
type ListDealAssociationsResponse
func (s ListDealAssociationsResponse) MarshalJSON() ([]byte, error)
type ListFilterSetsResponse
func (s ListFilterSetsResponse) MarshalJSON() ([]byte, error)
type ListFilteredBidRequestsResponse
func (s ListFilteredBidRequestsResponse) MarshalJSON() ([]byte, error)
type ListFilteredBidsResponse
func (s ListFilteredBidsResponse) MarshalJSON() ([]byte, error)
type ListImpressionMetricsResponse
func (s ListImpressionMetricsResponse) MarshalJSON() ([]byte, error)
type ListLosingBidsResponse
func (s ListLosingBidsResponse) MarshalJSON() ([]byte, error)
type ListNonBillableWinningBidsResponse
func (s ListNonBillableWinningBidsResponse) MarshalJSON() ([]byte, error)
type ListProductsResponse
func (s ListProductsResponse) MarshalJSON() ([]byte, error)
type ListProposalsResponse
func (s ListProposalsResponse) MarshalJSON() ([]byte, error)
type ListPublisherProfilesResponse
func (s ListPublisherProfilesResponse) MarshalJSON() ([]byte, error)
type LocationContext
func (s LocationContext) MarshalJSON() ([]byte, error)
type MarketplaceTargeting
func (s MarketplaceTargeting) MarshalJSON() ([]byte, error)
type MetricValue
func (s MetricValue) MarshalJSON() ([]byte, error)
type MobileApplicationTargeting
func (s MobileApplicationTargeting) MarshalJSON() ([]byte, error)
type Money
func (s Money) MarshalJSON() ([]byte, error)
type NativeContent
func (s NativeContent) MarshalJSON() ([]byte, error)
func (s *NativeContent) UnmarshalJSON(data []byte) error
type NonBillableWinningBidStatusRow
func (s NonBillableWinningBidStatusRow) MarshalJSON() ([]byte, error)
type NonGuaranteedAuctionTerms
func (s NonGuaranteedAuctionTerms) MarshalJSON() ([]byte, error)
type NonGuaranteedFixedPriceTerms
func (s NonGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type Note
func (s Note) MarshalJSON() ([]byte, error)
type OperatingSystemTargeting
func (s OperatingSystemTargeting) MarshalJSON() ([]byte, error)
type PauseProposalDealsRequest
func (s PauseProposalDealsRequest) MarshalJSON() ([]byte, error)
type PauseProposalRequest
func (s PauseProposalRequest) MarshalJSON() ([]byte, error)
type PlacementTargeting
func (s PlacementTargeting) MarshalJSON() ([]byte, error)
type PlatformContext
func (s PlatformContext) MarshalJSON() ([]byte, error)
type Price
func (s Price) MarshalJSON() ([]byte, error)
type PricePerBuyer
func (s PricePerBuyer) MarshalJSON() ([]byte, error)
type PrivateData
func (s PrivateData) MarshalJSON() ([]byte, error)
type Product
func (s Product) MarshalJSON() ([]byte, error)
type Proposal
func (s Proposal) MarshalJSON() ([]byte, error)
type PublisherProfile
func (s PublisherProfile) MarshalJSON() ([]byte, error)
type PublisherProfileMobileApplication
func (s PublisherProfileMobileApplication) MarshalJSON() ([]byte, error)
type RealtimeTimeRange
func (s RealtimeTimeRange) MarshalJSON() ([]byte, error)
type RelativeDateRange
func (s RelativeDateRange) MarshalJSON() ([]byte, error)
type RemoveDealAssociationRequest
func (s RemoveDealAssociationRequest) MarshalJSON() ([]byte, error)
type ResumeProposalDealsRequest
func (s ResumeProposalDealsRequest) MarshalJSON() ([]byte, error)
type ResumeProposalRequest
type RowDimensions
func (s RowDimensions) MarshalJSON() ([]byte, error)
type SecurityContext
func (s SecurityContext) MarshalJSON() ([]byte, error)
type Seller
func (s Seller) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type ServingContext
func (s ServingContext) MarshalJSON() ([]byte, error)
type ServingRestriction
func (s ServingRestriction) MarshalJSON() ([]byte, error)
type Size
func (s Size) MarshalJSON() ([]byte, error)
type StopWatchingCreativeRequest
type TargetingCriteria
func (s TargetingCriteria) MarshalJSON() ([]byte, error)
type TargetingValue
func (s TargetingValue) MarshalJSON() ([]byte, error)
type TechnologyTargeting
func (s TechnologyTargeting) MarshalJSON() ([]byte, error)
type TimeInterval
func (s TimeInterval) MarshalJSON() ([]byte, error)
type TimeOfDay
func (s TimeOfDay) MarshalJSON() ([]byte, error)
type UrlTargeting
func (s UrlTargeting) MarshalJSON() ([]byte, error)
type VideoContent
func (s VideoContent) MarshalJSON() ([]byte, error)
type VideoTargeting
func (s VideoTargeting) MarshalJSON() ([]byte, error)
type WatchCreativeRequest
func (s WatchCreativeRequest) MarshalJSON() ([]byte, error)
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
type AbsoluteDateRange ¶
type AbsoluteDateRange struct {
	// EndDate: The end date of the range (inclusive). Must be within the 30 days
	// leading up to current date, and must be equal to or after start_date.
	EndDate *Date `json:"endDate,omitempty"`
	// StartDate: The start date of the range (inclusive). Must be within the 30
	// days leading up to current date, and must be equal to or before end_date.
	StartDate *Date `json:"startDate,omitempty"`
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

AbsoluteDateRange: An absolute date range, specified by its start date and end date. The supported range of dates begins 30 days before today and ends today. Validity checked upon filter set creation. If a filter set with an absolute date range is run at a later date more than 30 days after start_date, it will fail.

func (AbsoluteDateRange) MarshalJSON ¶
func (s AbsoluteDateRange) MarshalJSON() ([]byte, error)
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

AcceptProposalRequest: Request to accept a proposal.

func (AcceptProposalRequest) MarshalJSON ¶
func (s AcceptProposalRequest) MarshalJSON() ([]byte, error)
type AccountsClientsCreateCall ¶
type AccountsClientsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsCreateCall) Context ¶
func (c *AccountsClientsCreateCall) Context(ctx context.Context) *AccountsClientsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsCreateCall) Do ¶
func (c *AccountsClientsCreateCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "adexchangebuyer2.accounts.clients.create" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsCreateCall) Fields ¶
func (c *AccountsClientsCreateCall) Fields(s ...googleapi.Field) *AccountsClientsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsCreateCall) Header ¶
func (c *AccountsClientsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsClientsGetCall ¶
type AccountsClientsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsGetCall) Context ¶
func (c *AccountsClientsGetCall) Context(ctx context.Context) *AccountsClientsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsGetCall) Do ¶
func (c *AccountsClientsGetCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "adexchangebuyer2.accounts.clients.get" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsGetCall) Fields ¶
func (c *AccountsClientsGetCall) Fields(s ...googleapi.Field) *AccountsClientsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsGetCall) Header ¶
func (c *AccountsClientsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsGetCall) IfNoneMatch ¶
func (c *AccountsClientsGetCall) IfNoneMatch(entityTag string) *AccountsClientsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsClientsInvitationsCreateCall ¶
type AccountsClientsInvitationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsInvitationsCreateCall) Context ¶
func (c *AccountsClientsInvitationsCreateCall) Context(ctx context.Context) *AccountsClientsInvitationsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsInvitationsCreateCall) Do ¶
func (c *AccountsClientsInvitationsCreateCall) Do(opts ...googleapi.CallOption) (*ClientUserInvitation, error)

Do executes the "adexchangebuyer2.accounts.clients.invitations.create" call. Any non-2xx status code is an error. Response headers are in either *ClientUserInvitation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsInvitationsCreateCall) Fields ¶
func (c *AccountsClientsInvitationsCreateCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsInvitationsCreateCall) Header ¶
func (c *AccountsClientsInvitationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsClientsInvitationsGetCall ¶
type AccountsClientsInvitationsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsInvitationsGetCall) Context ¶
func (c *AccountsClientsInvitationsGetCall) Context(ctx context.Context) *AccountsClientsInvitationsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsInvitationsGetCall) Do ¶
func (c *AccountsClientsInvitationsGetCall) Do(opts ...googleapi.CallOption) (*ClientUserInvitation, error)

Do executes the "adexchangebuyer2.accounts.clients.invitations.get" call. Any non-2xx status code is an error. Response headers are in either *ClientUserInvitation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsInvitationsGetCall) Fields ¶
func (c *AccountsClientsInvitationsGetCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsInvitationsGetCall) Header ¶
func (c *AccountsClientsInvitationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsInvitationsGetCall) IfNoneMatch ¶
func (c *AccountsClientsInvitationsGetCall) IfNoneMatch(entityTag string) *AccountsClientsInvitationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsClientsInvitationsListCall ¶
type AccountsClientsInvitationsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsInvitationsListCall) Context ¶
func (c *AccountsClientsInvitationsListCall) Context(ctx context.Context) *AccountsClientsInvitationsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsInvitationsListCall) Do ¶
func (c *AccountsClientsInvitationsListCall) Do(opts ...googleapi.CallOption) (*ListClientUserInvitationsResponse, error)

Do executes the "adexchangebuyer2.accounts.clients.invitations.list" call. Any non-2xx status code is an error. Response headers are in either *ListClientUserInvitationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsInvitationsListCall) Fields ¶
func (c *AccountsClientsInvitationsListCall) Fields(s ...googleapi.Field) *AccountsClientsInvitationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsInvitationsListCall) Header ¶
func (c *AccountsClientsInvitationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsInvitationsListCall) IfNoneMatch ¶
func (c *AccountsClientsInvitationsListCall) IfNoneMatch(entityTag string) *AccountsClientsInvitationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsClientsInvitationsListCall) PageSize ¶
func (c *AccountsClientsInvitationsListCall) PageSize(pageSize int64) *AccountsClientsInvitationsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer clients than requested. If unspecified, server will pick an appropriate default.

func (*AccountsClientsInvitationsListCall) PageToken ¶
func (c *AccountsClientsInvitationsListCall) PageToken(pageToken string) *AccountsClientsInvitationsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListClientUserInvitationsResponse.nextPageToken returned from the previous call to the clients.invitations.list method.

func (*AccountsClientsInvitationsListCall) Pages ¶
func (c *AccountsClientsInvitationsListCall) Pages(ctx context.Context, f func(*ListClientUserInvitationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsClientsInvitationsService ¶
type AccountsClientsInvitationsService struct {
	// contains filtered or unexported fields
}
func NewAccountsClientsInvitationsService ¶
func NewAccountsClientsInvitationsService(s *Service) *AccountsClientsInvitationsService
func (*AccountsClientsInvitationsService) Create ¶
func (r *AccountsClientsInvitationsService) Create(accountId int64, clientAccountId int64, clientuserinvitation *ClientUserInvitation) *AccountsClientsInvitationsCreateCall

Create: Creates and sends out an email invitation to access an Ad Exchange client buyer account.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer that the user should be associated with. (required).
func (*AccountsClientsInvitationsService) Get ¶
func (r *AccountsClientsInvitationsService) Get(accountId int64, clientAccountId int64, invitationId int64) *AccountsClientsInvitationsGetCall

Get: Retrieves an existing client user invitation.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer that the user invitation to be retrieved is associated with. (required).
invitationId: Numerical identifier of the user invitation to retrieve. (required).
func (*AccountsClientsInvitationsService) List ¶
func (r *AccountsClientsInvitationsService) List(accountId int64, clientAccountId string) *AccountsClientsInvitationsListCall

List: Lists all the client users invitations for a client with a given account ID.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer to list invitations for. (required) You must either specify a string representation of a numerical account identifier or the `-` character to list all the invitations for all the clients of a given sponsor buyer.
type AccountsClientsListCall ¶
type AccountsClientsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsListCall) Context ¶
func (c *AccountsClientsListCall) Context(ctx context.Context) *AccountsClientsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsListCall) Do ¶
func (c *AccountsClientsListCall) Do(opts ...googleapi.CallOption) (*ListClientsResponse, error)

Do executes the "adexchangebuyer2.accounts.clients.list" call. Any non-2xx status code is an error. Response headers are in either *ListClientsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsListCall) Fields ¶
func (c *AccountsClientsListCall) Fields(s ...googleapi.Field) *AccountsClientsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsListCall) Header ¶
func (c *AccountsClientsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsListCall) IfNoneMatch ¶
func (c *AccountsClientsListCall) IfNoneMatch(entityTag string) *AccountsClientsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsClientsListCall) PageSize ¶
func (c *AccountsClientsListCall) PageSize(pageSize int64) *AccountsClientsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer clients than requested. If unspecified, the server will pick an appropriate default.

func (*AccountsClientsListCall) PageToken ¶
func (c *AccountsClientsListCall) PageToken(pageToken string) *AccountsClientsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListClientsResponse.nextPageToken returned from the previous call to the accounts.clients.list method.

func (*AccountsClientsListCall) Pages ¶
func (c *AccountsClientsListCall) Pages(ctx context.Context, f func(*ListClientsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AccountsClientsListCall) PartnerClientId ¶
func (c *AccountsClientsListCall) PartnerClientId(partnerClientId string) *AccountsClientsListCall

PartnerClientId sets the optional parameter "partnerClientId": Optional unique identifier (from the standpoint of an Ad Exchange sponsor buyer partner) of the client to return. If specified, at most one client will be returned in the response.

type AccountsClientsService ¶
type AccountsClientsService struct {
	Invitations *AccountsClientsInvitationsService

	Users *AccountsClientsUsersService
	// contains filtered or unexported fields
}
func NewAccountsClientsService ¶
func NewAccountsClientsService(s *Service) *AccountsClientsService
func (*AccountsClientsService) Create ¶
func (r *AccountsClientsService) Create(accountId int64, client *Client) *AccountsClientsCreateCall

Create: Creates a new client buyer.

accountId: Unique numerical account ID for the buyer of which the client buyer is a customer; the sponsor buyer to create a client for. (required).
func (*AccountsClientsService) Get ¶
func (r *AccountsClientsService) Get(accountId int64, clientAccountId int64) *AccountsClientsGetCall

Get: Gets a client buyer with a given client account ID.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer to retrieve. (required).
func (*AccountsClientsService) List ¶
func (r *AccountsClientsService) List(accountId int64) *AccountsClientsListCall

List: Lists all the clients for the current sponsor buyer.

accountId: Unique numerical account ID of the sponsor buyer to list the clients for.
func (*AccountsClientsService) Update ¶
func (r *AccountsClientsService) Update(accountId int64, clientAccountId int64, client *Client) *AccountsClientsUpdateCall

Update: Updates an existing client buyer.

accountId: Unique numerical account ID for the buyer of which the client buyer is a customer; the sponsor buyer to update a client for. (required).
clientAccountId: Unique numerical account ID of the client to update. (required).
type AccountsClientsUpdateCall ¶
type AccountsClientsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsUpdateCall) Context ¶
func (c *AccountsClientsUpdateCall) Context(ctx context.Context) *AccountsClientsUpdateCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsUpdateCall) Do ¶
func (c *AccountsClientsUpdateCall) Do(opts ...googleapi.CallOption) (*Client, error)

Do executes the "adexchangebuyer2.accounts.clients.update" call. Any non-2xx status code is an error. Response headers are in either *Client.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsUpdateCall) Fields ¶
func (c *AccountsClientsUpdateCall) Fields(s ...googleapi.Field) *AccountsClientsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsUpdateCall) Header ¶
func (c *AccountsClientsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsClientsUsersGetCall ¶
type AccountsClientsUsersGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsUsersGetCall) Context ¶
func (c *AccountsClientsUsersGetCall) Context(ctx context.Context) *AccountsClientsUsersGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsUsersGetCall) Do ¶
func (c *AccountsClientsUsersGetCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "adexchangebuyer2.accounts.clients.users.get" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsUsersGetCall) Fields ¶
func (c *AccountsClientsUsersGetCall) Fields(s ...googleapi.Field) *AccountsClientsUsersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsUsersGetCall) Header ¶
func (c *AccountsClientsUsersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsUsersGetCall) IfNoneMatch ¶
func (c *AccountsClientsUsersGetCall) IfNoneMatch(entityTag string) *AccountsClientsUsersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsClientsUsersListCall ¶
type AccountsClientsUsersListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsUsersListCall) Context ¶
func (c *AccountsClientsUsersListCall) Context(ctx context.Context) *AccountsClientsUsersListCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsUsersListCall) Do ¶
func (c *AccountsClientsUsersListCall) Do(opts ...googleapi.CallOption) (*ListClientUsersResponse, error)

Do executes the "adexchangebuyer2.accounts.clients.users.list" call. Any non-2xx status code is an error. Response headers are in either *ListClientUsersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsUsersListCall) Fields ¶
func (c *AccountsClientsUsersListCall) Fields(s ...googleapi.Field) *AccountsClientsUsersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsUsersListCall) Header ¶
func (c *AccountsClientsUsersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsClientsUsersListCall) IfNoneMatch ¶
func (c *AccountsClientsUsersListCall) IfNoneMatch(entityTag string) *AccountsClientsUsersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsClientsUsersListCall) PageSize ¶
func (c *AccountsClientsUsersListCall) PageSize(pageSize int64) *AccountsClientsUsersListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer clients than requested. If unspecified, the server will pick an appropriate default.

func (*AccountsClientsUsersListCall) PageToken ¶
func (c *AccountsClientsUsersListCall) PageToken(pageToken string) *AccountsClientsUsersListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListClientUsersResponse.nextPageToken returned from the previous call to the accounts.clients.users.list method.

func (*AccountsClientsUsersListCall) Pages ¶
func (c *AccountsClientsUsersListCall) Pages(ctx context.Context, f func(*ListClientUsersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsClientsUsersService ¶
type AccountsClientsUsersService struct {
	// contains filtered or unexported fields
}
func NewAccountsClientsUsersService ¶
func NewAccountsClientsUsersService(s *Service) *AccountsClientsUsersService
func (*AccountsClientsUsersService) Get ¶
func (r *AccountsClientsUsersService) Get(accountId int64, clientAccountId int64, userId int64) *AccountsClientsUsersGetCall

Get: Retrieves an existing client user.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer that the user to be retrieved is associated with. (required).
userId: Numerical identifier of the user to retrieve. (required).
func (*AccountsClientsUsersService) List ¶
func (r *AccountsClientsUsersService) List(accountId int64, clientAccountId string) *AccountsClientsUsersListCall

List: Lists all the known client users for a specified sponsor buyer account ID.

accountId: Numerical account ID of the sponsor buyer of the client to list users for. (required).
clientAccountId: The account ID of the client buyer to list users for. (required) You must specify either a string representation of a numerical account identifier or the `-` character to list all the client users for all the clients of a given sponsor buyer.
func (*AccountsClientsUsersService) Update ¶
func (r *AccountsClientsUsersService) Update(accountId int64, clientAccountId int64, userId int64, clientuser *ClientUser) *AccountsClientsUsersUpdateCall

Update: Updates an existing client user. Only the user status can be changed on update.

accountId: Numerical account ID of the client's sponsor buyer. (required).
clientAccountId: Numerical account ID of the client buyer that the user to be retrieved is associated with. (required).
userId: Numerical identifier of the user to retrieve. (required).
type AccountsClientsUsersUpdateCall ¶
type AccountsClientsUsersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsClientsUsersUpdateCall) Context ¶
func (c *AccountsClientsUsersUpdateCall) Context(ctx context.Context) *AccountsClientsUsersUpdateCall

Context sets the context to be used in this call's Do method.

func (*AccountsClientsUsersUpdateCall) Do ¶
func (c *AccountsClientsUsersUpdateCall) Do(opts ...googleapi.CallOption) (*ClientUser, error)

Do executes the "adexchangebuyer2.accounts.clients.users.update" call. Any non-2xx status code is an error. Response headers are in either *ClientUser.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsClientsUsersUpdateCall) Fields ¶
func (c *AccountsClientsUsersUpdateCall) Fields(s ...googleapi.Field) *AccountsClientsUsersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsClientsUsersUpdateCall) Header ¶
func (c *AccountsClientsUsersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesCreateCall ¶
type AccountsCreativesCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesCreateCall) Context ¶
func (c *AccountsCreativesCreateCall) Context(ctx context.Context) *AccountsCreativesCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesCreateCall) Do ¶
func (c *AccountsCreativesCreateCall) Do(opts ...googleapi.CallOption) (*Creative, error)

Do executes the "adexchangebuyer2.accounts.creatives.create" call. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesCreateCall) DuplicateIdMode ¶
func (c *AccountsCreativesCreateCall) DuplicateIdMode(duplicateIdMode string) *AccountsCreativesCreateCall

DuplicateIdMode sets the optional parameter "duplicateIdMode": Indicates if multiple creatives can share an ID or not. Default is NO_DUPLICATES (one ID per creative).

Possible values:

"NO_DUPLICATES" - Recommended. This means that an ID will be unique to a


single creative. Multiple creatives will not share an ID.

"FORCE_ENABLE_DUPLICATE_IDS" - Not recommended. Using this option will


allow multiple creatives to share the same ID. Get and Update requests will not be possible for any ID that has more than one creative associated. (List will still function.) This is only intended for backwards compatibility in cases where a single ID is already shared by multiple creatives from previous APIs.

func (*AccountsCreativesCreateCall) Fields ¶
func (c *AccountsCreativesCreateCall) Fields(s ...googleapi.Field) *AccountsCreativesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesCreateCall) Header ¶
func (c *AccountsCreativesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesDealAssociationsAddCall ¶
type AccountsCreativesDealAssociationsAddCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesDealAssociationsAddCall) Context ¶
func (c *AccountsCreativesDealAssociationsAddCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsAddCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesDealAssociationsAddCall) Do ¶
func (c *AccountsCreativesDealAssociationsAddCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.accounts.creatives.dealAssociations.add" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesDealAssociationsAddCall) Fields ¶
func (c *AccountsCreativesDealAssociationsAddCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsAddCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesDealAssociationsAddCall) Header ¶
func (c *AccountsCreativesDealAssociationsAddCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesDealAssociationsListCall ¶
type AccountsCreativesDealAssociationsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesDealAssociationsListCall) Context ¶
func (c *AccountsCreativesDealAssociationsListCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesDealAssociationsListCall) Do ¶
func (c *AccountsCreativesDealAssociationsListCall) Do(opts ...googleapi.CallOption) (*ListDealAssociationsResponse, error)

Do executes the "adexchangebuyer2.accounts.creatives.dealAssociations.list" call. Any non-2xx status code is an error. Response headers are in either *ListDealAssociationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesDealAssociationsListCall) Fields ¶
func (c *AccountsCreativesDealAssociationsListCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesDealAssociationsListCall) Header ¶
func (c *AccountsCreativesDealAssociationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsCreativesDealAssociationsListCall) IfNoneMatch ¶
func (c *AccountsCreativesDealAssociationsListCall) IfNoneMatch(entityTag string) *AccountsCreativesDealAssociationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsCreativesDealAssociationsListCall) PageSize ¶
func (c *AccountsCreativesDealAssociationsListCall) PageSize(pageSize int64) *AccountsCreativesDealAssociationsListCall

PageSize sets the optional parameter "pageSize": Requested page size. Server may return fewer associations than requested. If unspecified, server will pick an appropriate default.

func (*AccountsCreativesDealAssociationsListCall) PageToken ¶
func (c *AccountsCreativesDealAssociationsListCall) PageToken(pageToken string) *AccountsCreativesDealAssociationsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListDealAssociationsResponse.next_page_token returned from the previous call to 'ListDealAssociations' method.

func (*AccountsCreativesDealAssociationsListCall) Pages ¶
func (c *AccountsCreativesDealAssociationsListCall) Pages(ctx context.Context, f func(*ListDealAssociationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AccountsCreativesDealAssociationsListCall) Query ¶
func (c *AccountsCreativesDealAssociationsListCall) Query(query string) *AccountsCreativesDealAssociationsListCall

Query sets the optional parameter "query": An optional query string to filter deal associations. If no filter is specified, all associations will be returned. Supported queries are: - accountId=*account_id_string* - creativeId=*creative_id_string* - dealsId=*deals_id_string* - dealsStatus:{approved, conditionally_approved, disapproved, not_checked} - openAuctionStatus:{approved, conditionally_approved, disapproved, not_checked} Example: 'dealsId=12345 AND dealsStatus:disapproved'

type AccountsCreativesDealAssociationsRemoveCall ¶
type AccountsCreativesDealAssociationsRemoveCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesDealAssociationsRemoveCall) Context ¶
func (c *AccountsCreativesDealAssociationsRemoveCall) Context(ctx context.Context) *AccountsCreativesDealAssociationsRemoveCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesDealAssociationsRemoveCall) Do ¶
func (c *AccountsCreativesDealAssociationsRemoveCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.accounts.creatives.dealAssociations.remove" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesDealAssociationsRemoveCall) Fields ¶
func (c *AccountsCreativesDealAssociationsRemoveCall) Fields(s ...googleapi.Field) *AccountsCreativesDealAssociationsRemoveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesDealAssociationsRemoveCall) Header ¶
func (c *AccountsCreativesDealAssociationsRemoveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesDealAssociationsService ¶
type AccountsCreativesDealAssociationsService struct {
	// contains filtered or unexported fields
}
func NewAccountsCreativesDealAssociationsService ¶
func NewAccountsCreativesDealAssociationsService(s *Service) *AccountsCreativesDealAssociationsService
func (*AccountsCreativesDealAssociationsService) Add ¶
func (r *AccountsCreativesDealAssociationsService) Add(accountId string, creativeId string, adddealassociationrequest *AddDealAssociationRequest) *AccountsCreativesDealAssociationsAddCall

Add: Associate an existing deal with a creative.

- accountId: The account the creative belongs to. - creativeId: The ID of the creative associated with the deal.

func (*AccountsCreativesDealAssociationsService) List ¶
func (r *AccountsCreativesDealAssociationsService) List(accountId string, creativeId string) *AccountsCreativesDealAssociationsListCall

List: List all creative-deal associations.

accountId: The account to list the associations from. Specify "-" to list all creatives the current user has access to.
creativeId: The creative ID to list the associations from. Specify "-" to list all creatives under the above account.
func (*AccountsCreativesDealAssociationsService) Remove ¶
func (r *AccountsCreativesDealAssociationsService) Remove(accountId string, creativeId string, removedealassociationrequest *RemoveDealAssociationRequest) *AccountsCreativesDealAssociationsRemoveCall

Remove: Remove the association between a deal and a creative.

- accountId: The account the creative belongs to. - creativeId: The ID of the creative associated with the deal.

type AccountsCreativesGetCall ¶
type AccountsCreativesGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesGetCall) Context ¶
func (c *AccountsCreativesGetCall) Context(ctx context.Context) *AccountsCreativesGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesGetCall) Do ¶
func (c *AccountsCreativesGetCall) Do(opts ...googleapi.CallOption) (*Creative, error)

Do executes the "adexchangebuyer2.accounts.creatives.get" call. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesGetCall) Fields ¶
func (c *AccountsCreativesGetCall) Fields(s ...googleapi.Field) *AccountsCreativesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesGetCall) Header ¶
func (c *AccountsCreativesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsCreativesGetCall) IfNoneMatch ¶
func (c *AccountsCreativesGetCall) IfNoneMatch(entityTag string) *AccountsCreativesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsCreativesListCall ¶
type AccountsCreativesListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesListCall) Context ¶
func (c *AccountsCreativesListCall) Context(ctx context.Context) *AccountsCreativesListCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesListCall) Do ¶
func (c *AccountsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativesResponse, error)

Do executes the "adexchangebuyer2.accounts.creatives.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesListCall) Fields ¶
func (c *AccountsCreativesListCall) Fields(s ...googleapi.Field) *AccountsCreativesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesListCall) Header ¶
func (c *AccountsCreativesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsCreativesListCall) IfNoneMatch ¶
func (c *AccountsCreativesListCall) IfNoneMatch(entityTag string) *AccountsCreativesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsCreativesListCall) PageSize ¶
func (c *AccountsCreativesListCall) PageSize(pageSize int64) *AccountsCreativesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer creatives than requested (due to timeout constraint) even if more are available through another call. If unspecified, server will pick an appropriate default. Acceptable values are 1 to 1000, inclusive.

func (*AccountsCreativesListCall) PageToken ¶
func (c *AccountsCreativesListCall) PageToken(pageToken string) *AccountsCreativesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativesResponse.next_page_token returned from the previous call to 'ListCreatives' method.

func (*AccountsCreativesListCall) Pages ¶
func (c *AccountsCreativesListCall) Pages(ctx context.Context, f func(*ListCreativesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AccountsCreativesListCall) Query ¶
func (c *AccountsCreativesListCall) Query(query string) *AccountsCreativesListCall

Query sets the optional parameter "query": An optional query string to filter creatives. If no filter is specified, all active creatives will be returned. Supported queries are: - accountId=*account_id_string* - creativeId=*creative_id_string* - dealsStatus: {approved, conditionally_approved, disapproved, not_checked} - openAuctionStatus: {approved, conditionally_approved, disapproved, not_checked} - attribute: {a numeric attribute from the list of attributes} - disapprovalReason: {a reason from DisapprovalReason} Example: 'accountId=12345 AND (dealsStatus:disapproved AND disapprovalReason:unacceptable_content) OR attribute:47'

type AccountsCreativesService ¶
type AccountsCreativesService struct {
	DealAssociations *AccountsCreativesDealAssociationsService
	// contains filtered or unexported fields
}
func NewAccountsCreativesService ¶
func NewAccountsCreativesService(s *Service) *AccountsCreativesService
func (*AccountsCreativesService) Create ¶
func (r *AccountsCreativesService) Create(accountId string, creative *Creative) *AccountsCreativesCreateCall

Create: Creates a creative.

accountId: The account that this creative belongs to. Can be used to filter the response of the creatives.list method.
func (*AccountsCreativesService) Get ¶
func (r *AccountsCreativesService) Get(accountId string, creativeId string) *AccountsCreativesGetCall

Get: Gets a creative.

- accountId: The account the creative belongs to. - creativeId: The ID of the creative to retrieve.

func (*AccountsCreativesService) List ¶
func (r *AccountsCreativesService) List(accountId string) *AccountsCreativesListCall

List: Lists creatives.

accountId: The account to list the creatives from. Specify "-" to list all creatives the current user has access to.
func (*AccountsCreativesService) StopWatching ¶
func (r *AccountsCreativesService) StopWatching(accountId string, creativeId string, stopwatchingcreativerequest *StopWatchingCreativeRequest) *AccountsCreativesStopWatchingCall

StopWatching: Stops watching a creative. Will stop push notifications being sent to the topics when the creative changes status.

accountId: The account of the creative to stop notifications for.
creativeId: The creative ID of the creative to stop notifications for. Specify "-" to specify stopping account level notifications.
func (*AccountsCreativesService) Update ¶
func (r *AccountsCreativesService) Update(accountId string, creativeId string, creative *Creative) *AccountsCreativesUpdateCall

Update: Updates a creative.

accountId: The account that this creative belongs to. Can be used to filter the response of the creatives.list method.
creativeId: The buyer-defined creative ID of this creative. Can be used to filter the response of the creatives.list method.
func (*AccountsCreativesService) Watch ¶
func (r *AccountsCreativesService) Watch(accountId string, creativeId string, watchcreativerequest *WatchCreativeRequest) *AccountsCreativesWatchCall

Watch: Watches a creative. Will result in push notifications being sent to the topic when the creative changes status.

accountId: The account of the creative to watch.
creativeId: The creative ID to watch for status changes. Specify "-" to watch all creatives under the above account. If both creative-level and account-level notifications are sent, only a single notification will be sent to the creative-level notification topic.
type AccountsCreativesStopWatchingCall ¶
type AccountsCreativesStopWatchingCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesStopWatchingCall) Context ¶
func (c *AccountsCreativesStopWatchingCall) Context(ctx context.Context) *AccountsCreativesStopWatchingCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesStopWatchingCall) Do ¶
func (c *AccountsCreativesStopWatchingCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.accounts.creatives.stopWatching" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesStopWatchingCall) Fields ¶
func (c *AccountsCreativesStopWatchingCall) Fields(s ...googleapi.Field) *AccountsCreativesStopWatchingCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesStopWatchingCall) Header ¶
func (c *AccountsCreativesStopWatchingCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesUpdateCall ¶
type AccountsCreativesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesUpdateCall) Context ¶
func (c *AccountsCreativesUpdateCall) Context(ctx context.Context) *AccountsCreativesUpdateCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesUpdateCall) Do ¶
func (c *AccountsCreativesUpdateCall) Do(opts ...googleapi.CallOption) (*Creative, error)

Do executes the "adexchangebuyer2.accounts.creatives.update" call. Any non-2xx status code is an error. Response headers are in either *Creative.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesUpdateCall) Fields ¶
func (c *AccountsCreativesUpdateCall) Fields(s ...googleapi.Field) *AccountsCreativesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesUpdateCall) Header ¶
func (c *AccountsCreativesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsCreativesWatchCall ¶
type AccountsCreativesWatchCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCreativesWatchCall) Context ¶
func (c *AccountsCreativesWatchCall) Context(ctx context.Context) *AccountsCreativesWatchCall

Context sets the context to be used in this call's Do method.

func (*AccountsCreativesWatchCall) Do ¶
func (c *AccountsCreativesWatchCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.accounts.creatives.watch" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCreativesWatchCall) Fields ¶
func (c *AccountsCreativesWatchCall) Fields(s ...googleapi.Field) *AccountsCreativesWatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsCreativesWatchCall) Header ¶
func (c *AccountsCreativesWatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsFinalizedProposalsListCall ¶
type AccountsFinalizedProposalsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsFinalizedProposalsListCall) Context ¶
func (c *AccountsFinalizedProposalsListCall) Context(ctx context.Context) *AccountsFinalizedProposalsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsFinalizedProposalsListCall) Do ¶
func (c *AccountsFinalizedProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)

Do executes the "adexchangebuyer2.accounts.finalizedProposals.list" call. Any non-2xx status code is an error. Response headers are in either *ListProposalsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsFinalizedProposalsListCall) Fields ¶
func (c *AccountsFinalizedProposalsListCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsFinalizedProposalsListCall) Filter ¶
func (c *AccountsFinalizedProposalsListCall) Filter(filter string) *AccountsFinalizedProposalsListCall

Filter sets the optional parameter "filter": An optional PQL filter query used to query for proposals. Nested repeated fields, such as proposal.deals.targetingCriterion, cannot be filtered.

func (*AccountsFinalizedProposalsListCall) FilterSyntax ¶
func (c *AccountsFinalizedProposalsListCall) FilterSyntax(filterSyntax string) *AccountsFinalizedProposalsListCall

FilterSyntax sets the optional parameter "filterSyntax": Syntax the filter is written in. Current implementation defaults to PQL but in the future it will be LIST_FILTER.

Possible values:

"FILTER_SYNTAX_UNSPECIFIED" - A placeholder for an undefined filter


syntax.

"PQL" - PQL query syntax. Visit


https://developers.google.com/ad-manager/api/pqlreference for PQL documentation and examples.

"LIST_FILTER" - API list filtering syntax. Read about syntax and usage at


https://developers.google.com/authorized-buyers/apis/guides/v2/list-filters.

func (*AccountsFinalizedProposalsListCall) Header ¶
func (c *AccountsFinalizedProposalsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsFinalizedProposalsListCall) IfNoneMatch ¶
func (c *AccountsFinalizedProposalsListCall) IfNoneMatch(entityTag string) *AccountsFinalizedProposalsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsFinalizedProposalsListCall) PageSize ¶
func (c *AccountsFinalizedProposalsListCall) PageSize(pageSize int64) *AccountsFinalizedProposalsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*AccountsFinalizedProposalsListCall) PageToken ¶
func (c *AccountsFinalizedProposalsListCall) PageToken(pageToken string) *AccountsFinalizedProposalsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListProposalsResponse.

func (*AccountsFinalizedProposalsListCall) Pages ¶
func (c *AccountsFinalizedProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsFinalizedProposalsPauseCall ¶
added in v0.48.0
type AccountsFinalizedProposalsPauseCall struct {
	// contains filtered or unexported fields
}
func (*AccountsFinalizedProposalsPauseCall) Context ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsPauseCall) Context(ctx context.Context) *AccountsFinalizedProposalsPauseCall

Context sets the context to be used in this call's Do method.

func (*AccountsFinalizedProposalsPauseCall) Do ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsPauseCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.finalizedProposals.pause" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsFinalizedProposalsPauseCall) Fields ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsPauseCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsPauseCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsFinalizedProposalsPauseCall) Header ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsPauseCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsFinalizedProposalsResumeCall ¶
added in v0.48.0
type AccountsFinalizedProposalsResumeCall struct {
	// contains filtered or unexported fields
}
func (*AccountsFinalizedProposalsResumeCall) Context ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsResumeCall) Context(ctx context.Context) *AccountsFinalizedProposalsResumeCall

Context sets the context to be used in this call's Do method.

func (*AccountsFinalizedProposalsResumeCall) Do ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsResumeCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.finalizedProposals.resume" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsFinalizedProposalsResumeCall) Fields ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsResumeCall) Fields(s ...googleapi.Field) *AccountsFinalizedProposalsResumeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsFinalizedProposalsResumeCall) Header ¶
added in v0.48.0
func (c *AccountsFinalizedProposalsResumeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsFinalizedProposalsService ¶
type AccountsFinalizedProposalsService struct {
	// contains filtered or unexported fields
}
func NewAccountsFinalizedProposalsService ¶
func NewAccountsFinalizedProposalsService(s *Service) *AccountsFinalizedProposalsService
func (*AccountsFinalizedProposalsService) List ¶
func (r *AccountsFinalizedProposalsService) List(accountId string) *AccountsFinalizedProposalsListCall

List: List finalized proposals, regardless if a proposal is being renegotiated. A filter expression (PQL query) may be specified to filter the results. The notes will not be returned.

- accountId: Account ID of the buyer.

func (*AccountsFinalizedProposalsService) Pause ¶
added in v0.48.0
func (r *AccountsFinalizedProposalsService) Pause(accountId string, proposalId string, pauseproposaldealsrequest *PauseProposalDealsRequest) *AccountsFinalizedProposalsPauseCall

Pause: Update given deals to pause serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to true for all listed deals in the request. Currently, this method only applies to PG and PD deals. For PA deals, call accounts.proposals.pause endpoint. It is a no-op to pause already-paused deals. It is an error to call PauseProposalDeals for deals which are not part of the proposal of proposal_id or which are not finalized or renegotiating.

- accountId: Account ID of the buyer. - proposalId: The proposal_id of the proposal containing the deals.

func (*AccountsFinalizedProposalsService) Resume ¶
added in v0.48.0
func (r *AccountsFinalizedProposalsService) Resume(accountId string, proposalId string, resumeproposaldealsrequest *ResumeProposalDealsRequest) *AccountsFinalizedProposalsResumeCall

Resume: Update given deals to resume serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to false for all listed deals in the request. Currently, this method only applies to PG and PD deals. For PA deals, call accounts.proposals.resume endpoint. It is a no-op to resume running deals or deals paused by the other party. It is an error to call ResumeProposalDeals for deals which are not part of the proposal of proposal_id or which are not finalized or renegotiating.

- accountId: Account ID of the buyer. - proposalId: The proposal_id of the proposal containing the deals.

type AccountsProductsGetCall ¶
type AccountsProductsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProductsGetCall) Context ¶
func (c *AccountsProductsGetCall) Context(ctx context.Context) *AccountsProductsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsProductsGetCall) Do ¶
func (c *AccountsProductsGetCall) Do(opts ...googleapi.CallOption) (*Product, error)

Do executes the "adexchangebuyer2.accounts.products.get" call. Any non-2xx status code is an error. Response headers are in either *Product.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProductsGetCall) Fields ¶
func (c *AccountsProductsGetCall) Fields(s ...googleapi.Field) *AccountsProductsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProductsGetCall) Header ¶
func (c *AccountsProductsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsProductsGetCall) IfNoneMatch ¶
func (c *AccountsProductsGetCall) IfNoneMatch(entityTag string) *AccountsProductsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsProductsListCall ¶
type AccountsProductsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProductsListCall) Context ¶
func (c *AccountsProductsListCall) Context(ctx context.Context) *AccountsProductsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsProductsListCall) Do ¶
func (c *AccountsProductsListCall) Do(opts ...googleapi.CallOption) (*ListProductsResponse, error)

Do executes the "adexchangebuyer2.accounts.products.list" call. Any non-2xx status code is an error. Response headers are in either *ListProductsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProductsListCall) Fields ¶
func (c *AccountsProductsListCall) Fields(s ...googleapi.Field) *AccountsProductsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProductsListCall) Filter ¶
func (c *AccountsProductsListCall) Filter(filter string) *AccountsProductsListCall

Filter sets the optional parameter "filter": An optional PQL query used to query for products. See https://developers.google.com/ad-manager/docs/pqlreference for documentation about PQL and examples. Nested repeated fields, such as product.targetingCriterion.inclusions, cannot be filtered.

func (*AccountsProductsListCall) Header ¶
func (c *AccountsProductsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsProductsListCall) IfNoneMatch ¶
func (c *AccountsProductsListCall) IfNoneMatch(entityTag string) *AccountsProductsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsProductsListCall) PageSize ¶
func (c *AccountsProductsListCall) PageSize(pageSize int64) *AccountsProductsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*AccountsProductsListCall) PageToken ¶
func (c *AccountsProductsListCall) PageToken(pageToken string) *AccountsProductsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListProductsResponse.

func (*AccountsProductsListCall) Pages ¶
func (c *AccountsProductsListCall) Pages(ctx context.Context, f func(*ListProductsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsProductsService ¶
type AccountsProductsService struct {
	// contains filtered or unexported fields
}
func NewAccountsProductsService ¶
func NewAccountsProductsService(s *Service) *AccountsProductsService
func (*AccountsProductsService) Get ¶
func (r *AccountsProductsService) Get(accountId string, productId string) *AccountsProductsGetCall

Get: Gets the requested product by ID.

- accountId: Account ID of the buyer. - productId: The ID for the product to get the head revision for.

func (*AccountsProductsService) List ¶
func (r *AccountsProductsService) List(accountId string) *AccountsProductsListCall

List: List all products visible to the buyer (optionally filtered by the specified PQL query).

- accountId: Account ID of the buyer.

type AccountsProposalsAcceptCall ¶
type AccountsProposalsAcceptCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsAcceptCall) Context ¶
func (c *AccountsProposalsAcceptCall) Context(ctx context.Context) *AccountsProposalsAcceptCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsAcceptCall) Do ¶
func (c *AccountsProposalsAcceptCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.accept" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsAcceptCall) Fields ¶
func (c *AccountsProposalsAcceptCall) Fields(s ...googleapi.Field) *AccountsProposalsAcceptCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsAcceptCall) Header ¶
func (c *AccountsProposalsAcceptCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsAddNoteCall ¶
type AccountsProposalsAddNoteCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsAddNoteCall) Context ¶
func (c *AccountsProposalsAddNoteCall) Context(ctx context.Context) *AccountsProposalsAddNoteCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsAddNoteCall) Do ¶
func (c *AccountsProposalsAddNoteCall) Do(opts ...googleapi.CallOption) (*Note, error)

Do executes the "adexchangebuyer2.accounts.proposals.addNote" call. Any non-2xx status code is an error. Response headers are in either *Note.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsAddNoteCall) Fields ¶
func (c *AccountsProposalsAddNoteCall) Fields(s ...googleapi.Field) *AccountsProposalsAddNoteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsAddNoteCall) Header ¶
func (c *AccountsProposalsAddNoteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsCancelNegotiationCall ¶
type AccountsProposalsCancelNegotiationCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsCancelNegotiationCall) Context ¶
func (c *AccountsProposalsCancelNegotiationCall) Context(ctx context.Context) *AccountsProposalsCancelNegotiationCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsCancelNegotiationCall) Do ¶
func (c *AccountsProposalsCancelNegotiationCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.cancelNegotiation" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsCancelNegotiationCall) Fields ¶
func (c *AccountsProposalsCancelNegotiationCall) Fields(s ...googleapi.Field) *AccountsProposalsCancelNegotiationCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsCancelNegotiationCall) Header ¶
func (c *AccountsProposalsCancelNegotiationCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsCompleteSetupCall ¶
type AccountsProposalsCompleteSetupCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsCompleteSetupCall) Context ¶
func (c *AccountsProposalsCompleteSetupCall) Context(ctx context.Context) *AccountsProposalsCompleteSetupCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsCompleteSetupCall) Do ¶
func (c *AccountsProposalsCompleteSetupCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.completeSetup" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsCompleteSetupCall) Fields ¶
func (c *AccountsProposalsCompleteSetupCall) Fields(s ...googleapi.Field) *AccountsProposalsCompleteSetupCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsCompleteSetupCall) Header ¶
func (c *AccountsProposalsCompleteSetupCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsCreateCall ¶
type AccountsProposalsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsCreateCall) Context ¶
func (c *AccountsProposalsCreateCall) Context(ctx context.Context) *AccountsProposalsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsCreateCall) Do ¶
func (c *AccountsProposalsCreateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.create" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsCreateCall) Fields ¶
func (c *AccountsProposalsCreateCall) Fields(s ...googleapi.Field) *AccountsProposalsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsCreateCall) Header ¶
func (c *AccountsProposalsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsGetCall ¶
type AccountsProposalsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsGetCall) Context ¶
func (c *AccountsProposalsGetCall) Context(ctx context.Context) *AccountsProposalsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsGetCall) Do ¶
func (c *AccountsProposalsGetCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.get" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsGetCall) Fields ¶
func (c *AccountsProposalsGetCall) Fields(s ...googleapi.Field) *AccountsProposalsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsGetCall) Header ¶
func (c *AccountsProposalsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsProposalsGetCall) IfNoneMatch ¶
func (c *AccountsProposalsGetCall) IfNoneMatch(entityTag string) *AccountsProposalsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsProposalsListCall ¶
type AccountsProposalsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsListCall) Context ¶
func (c *AccountsProposalsListCall) Context(ctx context.Context) *AccountsProposalsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsListCall) Do ¶
func (c *AccountsProposalsListCall) Do(opts ...googleapi.CallOption) (*ListProposalsResponse, error)

Do executes the "adexchangebuyer2.accounts.proposals.list" call. Any non-2xx status code is an error. Response headers are in either *ListProposalsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsListCall) Fields ¶
func (c *AccountsProposalsListCall) Fields(s ...googleapi.Field) *AccountsProposalsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsListCall) Filter ¶
func (c *AccountsProposalsListCall) Filter(filter string) *AccountsProposalsListCall

Filter sets the optional parameter "filter": An optional PQL filter query used to query for proposals. Nested repeated fields, such as proposal.deals.targetingCriterion, cannot be filtered.

func (*AccountsProposalsListCall) FilterSyntax ¶
func (c *AccountsProposalsListCall) FilterSyntax(filterSyntax string) *AccountsProposalsListCall

FilterSyntax sets the optional parameter "filterSyntax": Syntax the filter is written in. Current implementation defaults to PQL but in the future it will be LIST_FILTER.

Possible values:

"FILTER_SYNTAX_UNSPECIFIED" - A placeholder for an undefined filter


syntax.

"PQL" - PQL query syntax. Visit


https://developers.google.com/ad-manager/api/pqlreference for PQL documentation and examples.

"LIST_FILTER" - API list filtering syntax. Read about syntax and usage at


https://developers.google.com/authorized-buyers/apis/guides/v2/list-filters.

func (*AccountsProposalsListCall) Header ¶
func (c *AccountsProposalsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsProposalsListCall) IfNoneMatch ¶
func (c *AccountsProposalsListCall) IfNoneMatch(entityTag string) *AccountsProposalsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsProposalsListCall) PageSize ¶
func (c *AccountsProposalsListCall) PageSize(pageSize int64) *AccountsProposalsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*AccountsProposalsListCall) PageToken ¶
func (c *AccountsProposalsListCall) PageToken(pageToken string) *AccountsProposalsListCall

PageToken sets the optional parameter "pageToken": The page token as returned from ListProposalsResponse.

func (*AccountsProposalsListCall) Pages ¶
func (c *AccountsProposalsListCall) Pages(ctx context.Context, f func(*ListProposalsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsProposalsPauseCall ¶
type AccountsProposalsPauseCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsPauseCall) Context ¶
func (c *AccountsProposalsPauseCall) Context(ctx context.Context) *AccountsProposalsPauseCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsPauseCall) Do ¶
func (c *AccountsProposalsPauseCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.pause" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsPauseCall) Fields ¶
func (c *AccountsProposalsPauseCall) Fields(s ...googleapi.Field) *AccountsProposalsPauseCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsPauseCall) Header ¶
func (c *AccountsProposalsPauseCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsResumeCall ¶
type AccountsProposalsResumeCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsResumeCall) Context ¶
func (c *AccountsProposalsResumeCall) Context(ctx context.Context) *AccountsProposalsResumeCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsResumeCall) Do ¶
func (c *AccountsProposalsResumeCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.resume" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsResumeCall) Fields ¶
func (c *AccountsProposalsResumeCall) Fields(s ...googleapi.Field) *AccountsProposalsResumeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsResumeCall) Header ¶
func (c *AccountsProposalsResumeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsProposalsService ¶
type AccountsProposalsService struct {
	// contains filtered or unexported fields
}
func NewAccountsProposalsService ¶
func NewAccountsProposalsService(s *Service) *AccountsProposalsService
func (*AccountsProposalsService) Accept ¶
func (r *AccountsProposalsService) Accept(accountId string, proposalId string, acceptproposalrequest *AcceptProposalRequest) *AccountsProposalsAcceptCall

Accept: Mark the proposal as accepted at the given revision number. If the number does not match the server's revision number an `ABORTED` error message will be returned. This call updates the proposal_state from `PROPOSED` to `BUYER_ACCEPTED`, or from `SELLER_ACCEPTED` to `FINALIZED`. Upon calling this endpoint, the buyer implicitly agrees to the terms and conditions optionally set within the proposal by the publisher.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to accept.

func (*AccountsProposalsService) AddNote ¶
func (r *AccountsProposalsService) AddNote(accountId string, proposalId string, addnoterequest *AddNoteRequest) *AccountsProposalsAddNoteCall

AddNote: Create a new note and attach it to the proposal. The note is assigned a unique ID by the server. The proposal revision number will not increase when associated with a new note.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to attach the note to.

func (*AccountsProposalsService) CancelNegotiation ¶
func (r *AccountsProposalsService) CancelNegotiation(accountId string, proposalId string, cancelnegotiationrequest *CancelNegotiationRequest) *AccountsProposalsCancelNegotiationCall

CancelNegotiation: Cancel an ongoing negotiation on a proposal. This does not cancel or end serving for the deals if the proposal has been finalized, but only cancels a negotiation unilaterally.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to cancel negotiation for.

func (*AccountsProposalsService) CompleteSetup ¶
func (r *AccountsProposalsService) CompleteSetup(accountId string, proposalId string, completesetuprequest *CompleteSetupRequest) *AccountsProposalsCompleteSetupCall

CompleteSetup: You can opt-in to manually update proposals to indicate that setup is complete. By default, proposal setup is automatically completed after their deals are finalized. Contact your Technical Account Manager to opt in. Buyers can call this method when the proposal has been finalized, and all the required creatives have been uploaded using the Creatives API. This call updates the `is_setup_completed` field on the deals in the proposal, and notifies the seller. The server then advances the revision number of the most recent proposal. To mark an individual deal as ready to serve, call `buyers.finalizedDeals.setReadyToServe` in the Marketplace API.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to mark as setup completed.

func (*AccountsProposalsService) Create ¶
func (r *AccountsProposalsService) Create(accountId string, proposal *Proposal) *AccountsProposalsCreateCall

Create: Create the given proposal. Each created proposal and any deals it contains are assigned a unique ID by the server.

- accountId: Account ID of the buyer.

func (*AccountsProposalsService) Get ¶
func (r *AccountsProposalsService) Get(accountId string, proposalId string) *AccountsProposalsGetCall

Get: Gets a proposal given its ID. The proposal is returned at its head revision.

- accountId: Account ID of the buyer. - proposalId: The unique ID of the proposal.

func (*AccountsProposalsService) List ¶
func (r *AccountsProposalsService) List(accountId string) *AccountsProposalsListCall

List: List proposals. A filter expression (PQL query) may be specified to filter the results. To retrieve all finalized proposals, regardless if a proposal is being renegotiated, see the FinalizedProposals resource. Note that Bidder/ChildSeat relationships differ from the usual behavior. A Bidder account can only see its child seats' proposals by specifying the ChildSeat's accountId in the request path.

- accountId: Account ID of the buyer.

func (*AccountsProposalsService) Pause ¶
func (r *AccountsProposalsService) Pause(accountId string, proposalId string, pauseproposalrequest *PauseProposalRequest) *AccountsProposalsPauseCall

Pause: Update the given proposal to pause serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to true for all deals in the proposal. It is a no-op to pause an already-paused proposal. It is an error to call PauseProposal for a proposal that is not finalized or renegotiating.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to pause.

func (*AccountsProposalsService) Resume ¶
func (r *AccountsProposalsService) Resume(accountId string, proposalId string, resumeproposalrequest *ResumeProposalRequest) *AccountsProposalsResumeCall

Resume: Update the given proposal to resume serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to false for all deals in the proposal. Note that if the `has_seller_paused` bit is also set, serving will not resume until the seller also resumes. It is a no-op to resume an already-running proposal. It is an error to call ResumeProposal for a proposal that is not finalized or renegotiating.

- accountId: Account ID of the buyer. - proposalId: The ID of the proposal to resume.

func (*AccountsProposalsService) Update ¶
func (r *AccountsProposalsService) Update(accountId string, proposalId string, proposal *Proposal) *AccountsProposalsUpdateCall

Update: Update the given proposal at the client known revision number. If the server revision has advanced since the passed-in `proposal.proposal_revision`, an `ABORTED` error message will be returned. Only the buyer-modifiable fields of the proposal will be updated. Note that the deals in the proposal will be updated to match the passed-in copy. If a passed-in deal does not have a `deal_id`, the server will assign a new unique ID and create the deal. If passed-in deal has a `deal_id`, it will be updated to match the passed-in copy. Any existing deals not present in the passed-in proposal will be deleted. It is an error to pass in a deal with a `deal_id` not present at head.

- accountId: Account ID of the buyer. - proposalId: The unique ID of the proposal.

type AccountsProposalsUpdateCall ¶
type AccountsProposalsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProposalsUpdateCall) Context ¶
func (c *AccountsProposalsUpdateCall) Context(ctx context.Context) *AccountsProposalsUpdateCall

Context sets the context to be used in this call's Do method.

func (*AccountsProposalsUpdateCall) Do ¶
func (c *AccountsProposalsUpdateCall) Do(opts ...googleapi.CallOption) (*Proposal, error)

Do executes the "adexchangebuyer2.accounts.proposals.update" call. Any non-2xx status code is an error. Response headers are in either *Proposal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProposalsUpdateCall) Fields ¶
func (c *AccountsProposalsUpdateCall) Fields(s ...googleapi.Field) *AccountsProposalsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProposalsUpdateCall) Header ¶
func (c *AccountsProposalsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsPublisherProfilesGetCall ¶
type AccountsPublisherProfilesGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsPublisherProfilesGetCall) Context ¶
func (c *AccountsPublisherProfilesGetCall) Context(ctx context.Context) *AccountsPublisherProfilesGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsPublisherProfilesGetCall) Do ¶
func (c *AccountsPublisherProfilesGetCall) Do(opts ...googleapi.CallOption) (*PublisherProfile, error)

Do executes the "adexchangebuyer2.accounts.publisherProfiles.get" call. Any non-2xx status code is an error. Response headers are in either *PublisherProfile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsPublisherProfilesGetCall) Fields ¶
func (c *AccountsPublisherProfilesGetCall) Fields(s ...googleapi.Field) *AccountsPublisherProfilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsPublisherProfilesGetCall) Header ¶
func (c *AccountsPublisherProfilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsPublisherProfilesGetCall) IfNoneMatch ¶
func (c *AccountsPublisherProfilesGetCall) IfNoneMatch(entityTag string) *AccountsPublisherProfilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsPublisherProfilesListCall ¶
type AccountsPublisherProfilesListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsPublisherProfilesListCall) Context ¶
func (c *AccountsPublisherProfilesListCall) Context(ctx context.Context) *AccountsPublisherProfilesListCall

Context sets the context to be used in this call's Do method.

func (*AccountsPublisherProfilesListCall) Do ¶
func (c *AccountsPublisherProfilesListCall) Do(opts ...googleapi.CallOption) (*ListPublisherProfilesResponse, error)

Do executes the "adexchangebuyer2.accounts.publisherProfiles.list" call. Any non-2xx status code is an error. Response headers are in either *ListPublisherProfilesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsPublisherProfilesListCall) Fields ¶
func (c *AccountsPublisherProfilesListCall) Fields(s ...googleapi.Field) *AccountsPublisherProfilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsPublisherProfilesListCall) Header ¶
func (c *AccountsPublisherProfilesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsPublisherProfilesListCall) IfNoneMatch ¶
func (c *AccountsPublisherProfilesListCall) IfNoneMatch(entityTag string) *AccountsPublisherProfilesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsPublisherProfilesListCall) PageSize ¶
func (c *AccountsPublisherProfilesListCall) PageSize(pageSize int64) *AccountsPublisherProfilesListCall

PageSize sets the optional parameter "pageSize": Specify the number of results to include per page.

func (*AccountsPublisherProfilesListCall) PageToken ¶
func (c *AccountsPublisherProfilesListCall) PageToken(pageToken string) *AccountsPublisherProfilesListCall

PageToken sets the optional parameter "pageToken": The page token as return from ListPublisherProfilesResponse.

func (*AccountsPublisherProfilesListCall) Pages ¶
func (c *AccountsPublisherProfilesListCall) Pages(ctx context.Context, f func(*ListPublisherProfilesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsPublisherProfilesService ¶
type AccountsPublisherProfilesService struct {
	// contains filtered or unexported fields
}
func NewAccountsPublisherProfilesService ¶
func NewAccountsPublisherProfilesService(s *Service) *AccountsPublisherProfilesService
func (*AccountsPublisherProfilesService) Get ¶
func (r *AccountsPublisherProfilesService) Get(accountId string, publisherProfileId string) *AccountsPublisherProfilesGetCall

Get: Gets the requested publisher profile by id.

- accountId: Account ID of the buyer. - publisherProfileId: The id for the publisher profile to get.

func (*AccountsPublisherProfilesService) List ¶
func (r *AccountsPublisherProfilesService) List(accountId string) *AccountsPublisherProfilesListCall

List: List all publisher profiles visible to the buyer

- accountId: Account ID of the buyer.

type AccountsService ¶
type AccountsService struct {
	Clients *AccountsClientsService

	Creatives *AccountsCreativesService

	FinalizedProposals *AccountsFinalizedProposalsService

	Products *AccountsProductsService

	Proposals *AccountsProposalsService

	PublisherProfiles *AccountsPublisherProfilesService
	// contains filtered or unexported fields
}
func NewAccountsService ¶
func NewAccountsService(s *Service) *AccountsService
type AdSize ¶
type AdSize struct {
	// Height: The height of the ad slot in pixels. This field will be present only
	// when size type is `PIXEL`.
	Height int64 `json:"height,omitempty,string"`
	// SizeType: The size type of the ad slot.
	//
	// Possible values:
	//   "SIZE_TYPE_UNSPECIFIED" - A placeholder for an undefined size type.
	//   "PIXEL" - Ad slot with size specified by height and width in pixels.
	//   "INTERSTITIAL" - Special size to describe an interstitial ad slot.
	//   "NATIVE" - Native (mobile) ads rendered by the publisher.
	//   "FLUID" - Fluid size (for example, responsive size) can be resized
	// automatically with the change of outside environment.
	SizeType string `json:"sizeType,omitempty"`
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
type AdTechnologyProviders ¶
added in v0.6.0
type AdTechnologyProviders struct {
	// DetectedProviderIds: The detected ad technology provider IDs for this
	// creative. See
	// https://storage.googleapis.com/adx-rtb-dictionaries/providers.csv for
	// mapping of provider ID to provided name, a privacy policy URL, and a list of
	// domains which can be attributed to the provider. If the creative contains
	// provider IDs that are outside of those listed in the
	// `BidRequest.adslot.consented_providers_settings.consented_providers` field
	// on the (Google bid
	// protocol)[https://developers.google.com/authorized-buyers/rtb/downloads/realt
	// ime-bidding-proto] and the
	// `BidRequest.user.ext.consented_providers_settings.consented_providers` field
	// on the (OpenRTB
	// protocol)[https://developers.google.com/authorized-buyers/rtb/downloads/openr
	// tb-adx-proto], and a bid is submitted with that creative for an impression
	// that will serve to an EEA user, the bid will be filtered before the auction.
	DetectedProviderIds googleapi.Int64s `json:"detectedProviderIds,omitempty"`
	// HasUnidentifiedProvider: Whether the creative contains an unidentified ad
	// technology provider. If true for a given creative, any bid submitted with
	// that creative for an impression that will serve to an EEA user will be
	// filtered before the auction.
	HasUnidentifiedProvider bool `json:"hasUnidentifiedProvider,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DetectedProviderIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DetectedProviderIds") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdTechnologyProviders: Detected ad technology provider information.

func (AdTechnologyProviders) MarshalJSON ¶
added in v0.6.0
func (s AdTechnologyProviders) MarshalJSON() ([]byte, error)
type AddDealAssociationRequest ¶
type AddDealAssociationRequest struct {
	// Association: The association between a creative and a deal that should be
	// added.
	Association *CreativeDealAssociation `json:"association,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Association") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Association") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AddDealAssociationRequest: A request for associating a deal and a creative.

func (AddDealAssociationRequest) MarshalJSON ¶
func (s AddDealAssociationRequest) MarshalJSON() ([]byte, error)
type AddNoteRequest ¶
type AddNoteRequest struct {
	// Note: Details of the note to add.
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

AddNoteRequest: Request message for adding a note to a given proposal.

func (AddNoteRequest) MarshalJSON ¶
func (s AddNoteRequest) MarshalJSON() ([]byte, error)
type AppContext ¶
type AppContext struct {
	// AppTypes: The app types this restriction applies to.
	//
	// Possible values:
	//   "NATIVE" - Native app context.
	//   "WEB" - Mobile web app context.
	AppTypes []string `json:"appTypes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppTypes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppContext: Output only. The app type the restriction applies to for mobile device.

func (AppContext) MarshalJSON ¶
func (s AppContext) MarshalJSON() ([]byte, error)
type AuctionContext ¶
type AuctionContext struct {
	// AuctionTypes: The auction types this restriction applies to.
	//
	// Possible values:
	//   "OPEN_AUCTION" - The restriction applies to open auction.
	//   "DIRECT_DEALS" - The restriction applies to direct deals.
	AuctionTypes []string `json:"auctionTypes,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuctionTypes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuctionTypes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuctionContext: Output only. The auction type the restriction applies to.

func (AuctionContext) MarshalJSON ¶
func (s AuctionContext) MarshalJSON() ([]byte, error)
type BidMetricsRow ¶
type BidMetricsRow struct {
	// Bids: The number of bids that Ad Exchange received from the buyer.
	Bids *MetricValue `json:"bids,omitempty"`
	// BidsInAuction: The number of bids that were permitted to compete in the
	// auction.
	BidsInAuction *MetricValue `json:"bidsInAuction,omitempty"`
	// BilledImpressions: The number of bids for which the buyer was billed. Also
	// called valid impressions as invalid impressions are not billed.
	BilledImpressions *MetricValue `json:"billedImpressions,omitempty"`
	// ImpressionsWon: The number of bids that won the auction.
	ImpressionsWon *MetricValue `json:"impressionsWon,omitempty"`
	// MeasurableImpressions: The number of bids for which the corresponding
	// impression was measurable for viewability (as defined by Active View).
	MeasurableImpressions *MetricValue `json:"measurableImpressions,omitempty"`
	// ReachedQueries: The number of bids that won the auction and also won the
	// mediation waterfall (if any).
	ReachedQueries *MetricValue `json:"reachedQueries,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// ViewableImpressions: The number of bids for which the corresponding
	// impression was viewable (as defined by Active View).
	ViewableImpressions *MetricValue `json:"viewableImpressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Bids") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Bids") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BidMetricsRow: The set of metrics that are measured in numbers of bids, representing how many bids with the specified dimension values were considered eligible at each stage of the bidding funnel;

func (BidMetricsRow) MarshalJSON ¶
func (s BidMetricsRow) MarshalJSON() ([]byte, error)
type BidResponseWithoutBidsStatusRow ¶
type BidResponseWithoutBidsStatusRow struct {
	// ImpressionCount: The number of impressions for which there was a bid
	// response with the specified status.
	ImpressionCount *MetricValue `json:"impressionCount,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// Status: The status specifying why the bid responses were considered to have
	// no applicable bids.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - A placeholder for an undefined status. This value
	// will never be returned in responses.
	//   "RESPONSES_WITHOUT_BIDS" - The response had no bids.
	//   "RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT" - The response had no bids for the
	// specified account, though it may have included bids on behalf of other
	// accounts. Applies if: 1. Request is on behalf of a bidder and an account
	// filter is present. 2. Request is on behalf of a child seat.
	//   "RESPONSES_WITHOUT_BIDS_FOR_DEAL" - The response had no bids for the
	// specified deal, though it may have included bids on other deals on behalf of
	// the account to which the deal belongs. If request is on behalf of a bidder
	// and an account filter is not present, this also includes responses that have
	// bids on behalf of accounts other than the account to which the deal belongs.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ImpressionCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ImpressionCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BidResponseWithoutBidsStatusRow: The number of impressions with the specified dimension values that were considered to have no applicable bids, as described by the specified status.

func (BidResponseWithoutBidsStatusRow) MarshalJSON ¶
func (s BidResponseWithoutBidsStatusRow) MarshalJSON() ([]byte, error)
type BiddersAccountsFilterSetsBidMetricsListCall ¶
type BiddersAccountsFilterSetsBidMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsBidMetricsListCall) Context ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsBidMetricsListCall) Do ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.bidMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsBidMetricsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsBidMetricsListCall) Header ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsBidMetricsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsBidMetricsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsBidMetricsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidMetricsResponse.nextPageToken returned from the previous call to the bidMetrics.list method.

func (*BiddersAccountsFilterSetsBidMetricsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsBidMetricsService ¶
type BiddersAccountsFilterSetsBidMetricsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsBidMetricsService ¶
func NewBiddersAccountsFilterSetsBidMetricsService(s *Service) *BiddersAccountsFilterSetsBidMetricsService
func (*BiddersAccountsFilterSetsBidMetricsService) List ¶
func (r *BiddersAccountsFilterSetsBidMetricsService) List(filterSetName string) *BiddersAccountsFilterSetsBidMetricsListCall

List: Lists all metrics that are measured in terms of number of bids.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsBidResponseErrorsListCall ¶
type BiddersAccountsFilterSetsBidResponseErrorsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) Context ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidResponseErrorsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) Do ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.bidResponseErrors.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponseErrorsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidResponseErrorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) Header ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidResponseErrorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidResponseErrorsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidResponseErrorsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponseErrorsResponse.nextPageToken returned from the previous call to the bidResponseErrors.list method.

func (*BiddersAccountsFilterSetsBidResponseErrorsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsBidResponseErrorsService ¶
type BiddersAccountsFilterSetsBidResponseErrorsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsBidResponseErrorsService ¶
func NewBiddersAccountsFilterSetsBidResponseErrorsService(s *Service) *BiddersAccountsFilterSetsBidResponseErrorsService
func (*BiddersAccountsFilterSetsBidResponseErrorsService) List ¶
func (r *BiddersAccountsFilterSetsBidResponseErrorsService) List(filterSetName string) *BiddersAccountsFilterSetsBidResponseErrorsListCall

List: List all errors that occurred in bid responses, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall ¶
type BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Context ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Do ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.bidResponsesWithoutBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponsesWithoutBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Header ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponsesWithoutBidsResponse.nextPageToken returned from the previous call to the bidResponsesWithoutBids.list method.

func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsBidResponsesWithoutBidsService ¶
type BiddersAccountsFilterSetsBidResponsesWithoutBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsBidResponsesWithoutBidsService ¶
func NewBiddersAccountsFilterSetsBidResponsesWithoutBidsService(s *Service) *BiddersAccountsFilterSetsBidResponsesWithoutBidsService
func (*BiddersAccountsFilterSetsBidResponsesWithoutBidsService) List ¶
func (r *BiddersAccountsFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BiddersAccountsFilterSetsBidResponsesWithoutBidsListCall

List: List all reasons for which bid responses were considered to have no applicable bids, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsCreateCall ¶
type BiddersAccountsFilterSetsCreateCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsCreateCall) Context ¶
func (c *BiddersAccountsFilterSetsCreateCall) Context(ctx context.Context) *BiddersAccountsFilterSetsCreateCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsCreateCall) Do ¶
func (c *BiddersAccountsFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.create" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsCreateCall) Fields ¶
func (c *BiddersAccountsFilterSetsCreateCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsCreateCall) Header ¶
func (c *BiddersAccountsFilterSetsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsCreateCall) IsTransient ¶
func (c *BiddersAccountsFilterSetsCreateCall) IsTransient(isTransient bool) *BiddersAccountsFilterSetsCreateCall

IsTransient sets the optional parameter "isTransient": Whether the filter set is transient, or should be persisted indefinitely. By default, filter sets are not transient. If transient, it will be available for at least 1 hour after creation.

type BiddersAccountsFilterSetsDeleteCall ¶
type BiddersAccountsFilterSetsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsDeleteCall) Context ¶
func (c *BiddersAccountsFilterSetsDeleteCall) Context(ctx context.Context) *BiddersAccountsFilterSetsDeleteCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsDeleteCall) Do ¶
func (c *BiddersAccountsFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsDeleteCall) Fields ¶
func (c *BiddersAccountsFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsDeleteCall) Header ¶
func (c *BiddersAccountsFilterSetsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BiddersAccountsFilterSetsFilteredBidRequestsListCall ¶
type BiddersAccountsFilterSetsFilteredBidRequestsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) Context ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) Do ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.filteredBidRequests.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidRequestsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) Header ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidRequestsResponse.nextPageToken returned from the previous call to the filteredBidRequests.list method.

func (*BiddersAccountsFilterSetsFilteredBidRequestsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsFilteredBidRequestsService ¶
type BiddersAccountsFilterSetsFilteredBidRequestsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsFilteredBidRequestsService ¶
func NewBiddersAccountsFilterSetsFilteredBidRequestsService(s *Service) *BiddersAccountsFilterSetsFilteredBidRequestsService
func (*BiddersAccountsFilterSetsFilteredBidRequestsService) List ¶
func (r *BiddersAccountsFilterSetsFilteredBidRequestsService) List(filterSetName string) *BiddersAccountsFilterSetsFilteredBidRequestsListCall

List: List all reasons that caused a bid request not to be sent for an impression, with the number of bid requests not sent for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsFilteredBidsCreativesListCall ¶
type BiddersAccountsFilterSetsFilteredBidsCreativesListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Context ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Do ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.filteredBids.creatives.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByCreativeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Fields ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Header ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByCreativeResponse.nextPageToken returned from the previous call to the filteredBids.creatives.list method.

func (*BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Pages ¶
func (c *BiddersAccountsFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByCreativeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsFilteredBidsCreativesService ¶
type BiddersAccountsFilterSetsFilteredBidsCreativesService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsFilteredBidsCreativesService ¶
func NewBiddersAccountsFilterSetsFilteredBidsCreativesService(s *Service) *BiddersAccountsFilterSetsFilteredBidsCreativesService
func (*BiddersAccountsFilterSetsFilteredBidsCreativesService) List ¶
func (r *BiddersAccountsFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BiddersAccountsFilterSetsFilteredBidsCreativesListCall

List: List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by creative. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes).
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsFilteredBidsDetailsListCall ¶
type BiddersAccountsFilterSetsFilteredBidsDetailsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Context ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Do ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.filteredBids.details.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByDetailResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Header ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByDetailResponse.nextPageToken returned from the previous call to the filteredBids.details.list method.

func (*BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByDetailResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsFilteredBidsDetailsService ¶
type BiddersAccountsFilterSetsFilteredBidsDetailsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsFilteredBidsDetailsService ¶
func NewBiddersAccountsFilterSetsFilteredBidsDetailsService(s *Service) *BiddersAccountsFilterSetsFilteredBidsDetailsService
func (*BiddersAccountsFilterSetsFilteredBidsDetailsService) List ¶
func (r *BiddersAccountsFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BiddersAccountsFilterSetsFilteredBidsDetailsListCall

List: List all details associated with a specific reason for which bids were filtered, with the number of bids filtered for each detail.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by detail. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes). Details are only available for statuses 10, 14, 15, 17, 18, 19, 86, and 87.
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsFilteredBidsListCall ¶
type BiddersAccountsFilterSetsFilteredBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsFilteredBidsListCall) Context ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsFilteredBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) Do ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.filteredBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsFilteredBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) Header ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsFilteredBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsFilteredBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsFilteredBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidsResponse.nextPageToken returned from the previous call to the filteredBids.list method.

func (*BiddersAccountsFilterSetsFilteredBidsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsFilteredBidsService ¶
type BiddersAccountsFilterSetsFilteredBidsService struct {
	Creatives *BiddersAccountsFilterSetsFilteredBidsCreativesService

	Details *BiddersAccountsFilterSetsFilteredBidsDetailsService
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsFilteredBidsService ¶
func NewBiddersAccountsFilterSetsFilteredBidsService(s *Service) *BiddersAccountsFilterSetsFilteredBidsService
func (*BiddersAccountsFilterSetsFilteredBidsService) List ¶
func (r *BiddersAccountsFilterSetsFilteredBidsService) List(filterSetName string) *BiddersAccountsFilterSetsFilteredBidsListCall

List: List all reasons for which bids were filtered, with the number of bids filtered for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsGetCall ¶
type BiddersAccountsFilterSetsGetCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsGetCall) Context ¶
func (c *BiddersAccountsFilterSetsGetCall) Context(ctx context.Context) *BiddersAccountsFilterSetsGetCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsGetCall) Do ¶
func (c *BiddersAccountsFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.get" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsGetCall) Fields ¶
func (c *BiddersAccountsFilterSetsGetCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsGetCall) Header ¶
func (c *BiddersAccountsFilterSetsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsGetCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsGetCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BiddersAccountsFilterSetsImpressionMetricsListCall ¶
type BiddersAccountsFilterSetsImpressionMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsImpressionMetricsListCall) Context ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsImpressionMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) Do ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.impressionMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListImpressionMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsImpressionMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) Header ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsImpressionMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsImpressionMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsImpressionMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListImpressionMetricsResponse.nextPageToken returned from the previous call to the impressionMetrics.list method.

func (*BiddersAccountsFilterSetsImpressionMetricsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsImpressionMetricsService ¶
type BiddersAccountsFilterSetsImpressionMetricsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsImpressionMetricsService ¶
func NewBiddersAccountsFilterSetsImpressionMetricsService(s *Service) *BiddersAccountsFilterSetsImpressionMetricsService
func (*BiddersAccountsFilterSetsImpressionMetricsService) List ¶
func (r *BiddersAccountsFilterSetsImpressionMetricsService) List(filterSetName string) *BiddersAccountsFilterSetsImpressionMetricsListCall

List: Lists all metrics that are measured in terms of number of impressions.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsListCall ¶
type BiddersAccountsFilterSetsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsListCall) Context ¶
func (c *BiddersAccountsFilterSetsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsListCall) Do ¶
func (c *BiddersAccountsFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilterSetsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsListCall) Header ¶
func (c *BiddersAccountsFilterSetsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilterSetsResponse.nextPageToken returned from the previous call to the accounts.filterSets.list method.

func (*BiddersAccountsFilterSetsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsLosingBidsListCall ¶
type BiddersAccountsFilterSetsLosingBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsLosingBidsListCall) Context ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsLosingBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsLosingBidsListCall) Do ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.losingBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListLosingBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsLosingBidsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsLosingBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsLosingBidsListCall) Header ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsLosingBidsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsLosingBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsLosingBidsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsLosingBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsLosingBidsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsLosingBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListLosingBidsResponse.nextPageToken returned from the previous call to the losingBids.list method.

func (*BiddersAccountsFilterSetsLosingBidsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsLosingBidsService ¶
type BiddersAccountsFilterSetsLosingBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsLosingBidsService ¶
func NewBiddersAccountsFilterSetsLosingBidsService(s *Service) *BiddersAccountsFilterSetsLosingBidsService
func (*BiddersAccountsFilterSetsLosingBidsService) List ¶
func (r *BiddersAccountsFilterSetsLosingBidsService) List(filterSetName string) *BiddersAccountsFilterSetsLosingBidsListCall

List: List all reasons for which bids lost in the auction, with the number of bids that lost for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsNonBillableWinningBidsListCall ¶
type BiddersAccountsFilterSetsNonBillableWinningBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Context ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Do ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.accounts.filterSets.nonBillableWinningBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListNonBillableWinningBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Fields ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Header ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) IfNoneMatch ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageSize ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageToken ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListNonBillableWinningBidsResponse.nextPageToken returned from the previous call to the nonBillableWinningBids.list method.

func (*BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Pages ¶
func (c *BiddersAccountsFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersAccountsFilterSetsNonBillableWinningBidsService ¶
type BiddersAccountsFilterSetsNonBillableWinningBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsNonBillableWinningBidsService ¶
func NewBiddersAccountsFilterSetsNonBillableWinningBidsService(s *Service) *BiddersAccountsFilterSetsNonBillableWinningBidsService
func (*BiddersAccountsFilterSetsNonBillableWinningBidsService) List ¶
func (r *BiddersAccountsFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BiddersAccountsFilterSetsNonBillableWinningBidsListCall

List: List all reasons for which winning bids were not billable, with the number of bids not billed for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersAccountsFilterSetsService ¶
type BiddersAccountsFilterSetsService struct {
	BidMetrics *BiddersAccountsFilterSetsBidMetricsService

	BidResponseErrors *BiddersAccountsFilterSetsBidResponseErrorsService

	BidResponsesWithoutBids *BiddersAccountsFilterSetsBidResponsesWithoutBidsService

	FilteredBidRequests *BiddersAccountsFilterSetsFilteredBidRequestsService

	FilteredBids *BiddersAccountsFilterSetsFilteredBidsService

	ImpressionMetrics *BiddersAccountsFilterSetsImpressionMetricsService

	LosingBids *BiddersAccountsFilterSetsLosingBidsService

	NonBillableWinningBids *BiddersAccountsFilterSetsNonBillableWinningBidsService
	// contains filtered or unexported fields
}
func NewBiddersAccountsFilterSetsService ¶
func NewBiddersAccountsFilterSetsService(s *Service) *BiddersAccountsFilterSetsService
func (*BiddersAccountsFilterSetsService) Create ¶
func (r *BiddersAccountsFilterSetsService) Create(ownerName string, filterset *FilterSet) *BiddersAccountsFilterSetsCreateCall

Create: Creates the specified filter set for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter set to be created. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
func (*BiddersAccountsFilterSetsService) Delete ¶
func (r *BiddersAccountsFilterSetsService) Delete(name string) *BiddersAccountsFilterSetsDeleteCall

Delete: Deletes the requested filter set from the account with the given account ID.

name: Full name of the resource to delete. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BiddersAccountsFilterSetsService) Get ¶
func (r *BiddersAccountsFilterSetsService) Get(name string) *BiddersAccountsFilterSetsGetCall

Get: Retrieves the requested filter set for the account with the given account ID.

name: Full name of the resource being requested. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BiddersAccountsFilterSetsService) List ¶
func (r *BiddersAccountsFilterSetsService) List(ownerName string) *BiddersAccountsFilterSetsListCall

List: Lists all filter sets for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter sets to be listed. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
type BiddersAccountsService ¶
type BiddersAccountsService struct {
	FilterSets *BiddersAccountsFilterSetsService
	// contains filtered or unexported fields
}
func NewBiddersAccountsService ¶
func NewBiddersAccountsService(s *Service) *BiddersAccountsService
type BiddersFilterSetsBidMetricsListCall ¶
type BiddersFilterSetsBidMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsBidMetricsListCall) Context ¶
func (c *BiddersFilterSetsBidMetricsListCall) Context(ctx context.Context) *BiddersFilterSetsBidMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsBidMetricsListCall) Do ¶
func (c *BiddersFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.bidMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsBidMetricsListCall) Fields ¶
func (c *BiddersFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsBidMetricsListCall) Header ¶
func (c *BiddersFilterSetsBidMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsBidMetricsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsBidMetricsListCall) PageSize ¶
func (c *BiddersFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsBidMetricsListCall) PageToken ¶
func (c *BiddersFilterSetsBidMetricsListCall) PageToken(pageToken string) *BiddersFilterSetsBidMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidMetricsResponse.nextPageToken returned from the previous call to the bidMetrics.list method.

func (*BiddersFilterSetsBidMetricsListCall) Pages ¶
func (c *BiddersFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsBidMetricsService ¶
type BiddersFilterSetsBidMetricsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsBidMetricsService ¶
func NewBiddersFilterSetsBidMetricsService(s *Service) *BiddersFilterSetsBidMetricsService
func (*BiddersFilterSetsBidMetricsService) List ¶
func (r *BiddersFilterSetsBidMetricsService) List(filterSetName string) *BiddersFilterSetsBidMetricsListCall

List: Lists all metrics that are measured in terms of number of bids.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsBidResponseErrorsListCall ¶
type BiddersFilterSetsBidResponseErrorsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsBidResponseErrorsListCall) Context ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BiddersFilterSetsBidResponseErrorsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsBidResponseErrorsListCall) Do ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.bidResponseErrors.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponseErrorsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsBidResponseErrorsListCall) Fields ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidResponseErrorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsBidResponseErrorsListCall) Header ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsBidResponseErrorsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidResponseErrorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsBidResponseErrorsListCall) PageSize ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidResponseErrorsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsBidResponseErrorsListCall) PageToken ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BiddersFilterSetsBidResponseErrorsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponseErrorsResponse.nextPageToken returned from the previous call to the bidResponseErrors.list method.

func (*BiddersFilterSetsBidResponseErrorsListCall) Pages ¶
func (c *BiddersFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsBidResponseErrorsService ¶
type BiddersFilterSetsBidResponseErrorsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsBidResponseErrorsService ¶
func NewBiddersFilterSetsBidResponseErrorsService(s *Service) *BiddersFilterSetsBidResponseErrorsService
func (*BiddersFilterSetsBidResponseErrorsService) List ¶
func (r *BiddersFilterSetsBidResponseErrorsService) List(filterSetName string) *BiddersFilterSetsBidResponseErrorsListCall

List: List all errors that occurred in bid responses, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsBidResponsesWithoutBidsListCall ¶
type BiddersFilterSetsBidResponsesWithoutBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) Context ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BiddersFilterSetsBidResponsesWithoutBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) Do ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.bidResponsesWithoutBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponsesWithoutBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) Fields ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsBidResponsesWithoutBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) Header ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsBidResponsesWithoutBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) PageSize ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsBidResponsesWithoutBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) PageToken ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BiddersFilterSetsBidResponsesWithoutBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponsesWithoutBidsResponse.nextPageToken returned from the previous call to the bidResponsesWithoutBids.list method.

func (*BiddersFilterSetsBidResponsesWithoutBidsListCall) Pages ¶
func (c *BiddersFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsBidResponsesWithoutBidsService ¶
type BiddersFilterSetsBidResponsesWithoutBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsBidResponsesWithoutBidsService ¶
func NewBiddersFilterSetsBidResponsesWithoutBidsService(s *Service) *BiddersFilterSetsBidResponsesWithoutBidsService
func (*BiddersFilterSetsBidResponsesWithoutBidsService) List ¶
func (r *BiddersFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BiddersFilterSetsBidResponsesWithoutBidsListCall

List: List all reasons for which bid responses were considered to have no applicable bids, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsCreateCall ¶
type BiddersFilterSetsCreateCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsCreateCall) Context ¶
func (c *BiddersFilterSetsCreateCall) Context(ctx context.Context) *BiddersFilterSetsCreateCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsCreateCall) Do ¶
func (c *BiddersFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.bidders.filterSets.create" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsCreateCall) Fields ¶
func (c *BiddersFilterSetsCreateCall) Fields(s ...googleapi.Field) *BiddersFilterSetsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsCreateCall) Header ¶
func (c *BiddersFilterSetsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsCreateCall) IsTransient ¶
func (c *BiddersFilterSetsCreateCall) IsTransient(isTransient bool) *BiddersFilterSetsCreateCall

IsTransient sets the optional parameter "isTransient": Whether the filter set is transient, or should be persisted indefinitely. By default, filter sets are not transient. If transient, it will be available for at least 1 hour after creation.

type BiddersFilterSetsDeleteCall ¶
type BiddersFilterSetsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsDeleteCall) Context ¶
func (c *BiddersFilterSetsDeleteCall) Context(ctx context.Context) *BiddersFilterSetsDeleteCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsDeleteCall) Do ¶
func (c *BiddersFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.bidders.filterSets.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsDeleteCall) Fields ¶
func (c *BiddersFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BiddersFilterSetsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsDeleteCall) Header ¶
func (c *BiddersFilterSetsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BiddersFilterSetsFilteredBidRequestsListCall ¶
type BiddersFilterSetsFilteredBidRequestsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsFilteredBidRequestsListCall) Context ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidRequestsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsFilteredBidRequestsListCall) Do ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.filteredBidRequests.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidRequestsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsFilteredBidRequestsListCall) Fields ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidRequestsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsFilteredBidRequestsListCall) Header ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsFilteredBidRequestsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidRequestsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsFilteredBidRequestsListCall) PageSize ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidRequestsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsFilteredBidRequestsListCall) PageToken ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidRequestsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidRequestsResponse.nextPageToken returned from the previous call to the filteredBidRequests.list method.

func (*BiddersFilterSetsFilteredBidRequestsListCall) Pages ¶
func (c *BiddersFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsFilteredBidRequestsService ¶
type BiddersFilterSetsFilteredBidRequestsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsFilteredBidRequestsService ¶
func NewBiddersFilterSetsFilteredBidRequestsService(s *Service) *BiddersFilterSetsFilteredBidRequestsService
func (*BiddersFilterSetsFilteredBidRequestsService) List ¶
func (r *BiddersFilterSetsFilteredBidRequestsService) List(filterSetName string) *BiddersFilterSetsFilteredBidRequestsListCall

List: List all reasons that caused a bid request not to be sent for an impression, with the number of bid requests not sent for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsFilteredBidsCreativesListCall ¶
type BiddersFilterSetsFilteredBidsCreativesListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsFilteredBidsCreativesListCall) Context ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsCreativesListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) Do ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.filteredBids.creatives.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByCreativeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) Fields ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsCreativesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) Header ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsCreativesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) PageSize ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsCreativesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) PageToken ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsCreativesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByCreativeResponse.nextPageToken returned from the previous call to the filteredBids.creatives.list method.

func (*BiddersFilterSetsFilteredBidsCreativesListCall) Pages ¶
func (c *BiddersFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByCreativeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsFilteredBidsCreativesService ¶
type BiddersFilterSetsFilteredBidsCreativesService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsFilteredBidsCreativesService ¶
func NewBiddersFilterSetsFilteredBidsCreativesService(s *Service) *BiddersFilterSetsFilteredBidsCreativesService
func (*BiddersFilterSetsFilteredBidsCreativesService) List ¶
func (r *BiddersFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BiddersFilterSetsFilteredBidsCreativesListCall

List: List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by creative. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes).
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsFilteredBidsDetailsListCall ¶
type BiddersFilterSetsFilteredBidsDetailsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsFilteredBidsDetailsListCall) Context ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsDetailsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) Do ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.filteredBids.details.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByDetailResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) Fields ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsDetailsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) Header ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsDetailsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) PageSize ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsDetailsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) PageToken ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsDetailsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByDetailResponse.nextPageToken returned from the previous call to the filteredBids.details.list method.

func (*BiddersFilterSetsFilteredBidsDetailsListCall) Pages ¶
func (c *BiddersFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByDetailResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsFilteredBidsDetailsService ¶
type BiddersFilterSetsFilteredBidsDetailsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsFilteredBidsDetailsService ¶
func NewBiddersFilterSetsFilteredBidsDetailsService(s *Service) *BiddersFilterSetsFilteredBidsDetailsService
func (*BiddersFilterSetsFilteredBidsDetailsService) List ¶
func (r *BiddersFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BiddersFilterSetsFilteredBidsDetailsListCall

List: List all details associated with a specific reason for which bids were filtered, with the number of bids filtered for each detail.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by detail. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes). Details are only available for statuses 10, 14, 15, 17, 18, 19, 86, and 87.
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsFilteredBidsListCall ¶
type BiddersFilterSetsFilteredBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsFilteredBidsListCall) Context ¶
func (c *BiddersFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BiddersFilterSetsFilteredBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsFilteredBidsListCall) Do ¶
func (c *BiddersFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.filteredBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsFilteredBidsListCall) Fields ¶
func (c *BiddersFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsFilteredBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsFilteredBidsListCall) Header ¶
func (c *BiddersFilterSetsFilteredBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsFilteredBidsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsFilteredBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsFilteredBidsListCall) PageSize ¶
func (c *BiddersFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsFilteredBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsFilteredBidsListCall) PageToken ¶
func (c *BiddersFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BiddersFilterSetsFilteredBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidsResponse.nextPageToken returned from the previous call to the filteredBids.list method.

func (*BiddersFilterSetsFilteredBidsListCall) Pages ¶
func (c *BiddersFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsFilteredBidsService ¶
type BiddersFilterSetsFilteredBidsService struct {
	Creatives *BiddersFilterSetsFilteredBidsCreativesService

	Details *BiddersFilterSetsFilteredBidsDetailsService
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsFilteredBidsService ¶
func NewBiddersFilterSetsFilteredBidsService(s *Service) *BiddersFilterSetsFilteredBidsService
func (*BiddersFilterSetsFilteredBidsService) List ¶
func (r *BiddersFilterSetsFilteredBidsService) List(filterSetName string) *BiddersFilterSetsFilteredBidsListCall

List: List all reasons for which bids were filtered, with the number of bids filtered for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsGetCall ¶
type BiddersFilterSetsGetCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsGetCall) Context ¶
func (c *BiddersFilterSetsGetCall) Context(ctx context.Context) *BiddersFilterSetsGetCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsGetCall) Do ¶
func (c *BiddersFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.bidders.filterSets.get" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsGetCall) Fields ¶
func (c *BiddersFilterSetsGetCall) Fields(s ...googleapi.Field) *BiddersFilterSetsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsGetCall) Header ¶
func (c *BiddersFilterSetsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsGetCall) IfNoneMatch ¶
func (c *BiddersFilterSetsGetCall) IfNoneMatch(entityTag string) *BiddersFilterSetsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BiddersFilterSetsImpressionMetricsListCall ¶
type BiddersFilterSetsImpressionMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsImpressionMetricsListCall) Context ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BiddersFilterSetsImpressionMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsImpressionMetricsListCall) Do ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.impressionMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListImpressionMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsImpressionMetricsListCall) Fields ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsImpressionMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsImpressionMetricsListCall) Header ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsImpressionMetricsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsImpressionMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsImpressionMetricsListCall) PageSize ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BiddersFilterSetsImpressionMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsImpressionMetricsListCall) PageToken ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BiddersFilterSetsImpressionMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListImpressionMetricsResponse.nextPageToken returned from the previous call to the impressionMetrics.list method.

func (*BiddersFilterSetsImpressionMetricsListCall) Pages ¶
func (c *BiddersFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsImpressionMetricsService ¶
type BiddersFilterSetsImpressionMetricsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsImpressionMetricsService ¶
func NewBiddersFilterSetsImpressionMetricsService(s *Service) *BiddersFilterSetsImpressionMetricsService
func (*BiddersFilterSetsImpressionMetricsService) List ¶
func (r *BiddersFilterSetsImpressionMetricsService) List(filterSetName string) *BiddersFilterSetsImpressionMetricsListCall

List: Lists all metrics that are measured in terms of number of impressions.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsListCall ¶
type BiddersFilterSetsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsListCall) Context ¶
func (c *BiddersFilterSetsListCall) Context(ctx context.Context) *BiddersFilterSetsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsListCall) Do ¶
func (c *BiddersFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilterSetsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsListCall) Fields ¶
func (c *BiddersFilterSetsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsListCall) Header ¶
func (c *BiddersFilterSetsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsListCall) PageSize ¶
func (c *BiddersFilterSetsListCall) PageSize(pageSize int64) *BiddersFilterSetsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsListCall) PageToken ¶
func (c *BiddersFilterSetsListCall) PageToken(pageToken string) *BiddersFilterSetsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilterSetsResponse.nextPageToken returned from the previous call to the accounts.filterSets.list method.

func (*BiddersFilterSetsListCall) Pages ¶
func (c *BiddersFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsLosingBidsListCall ¶
type BiddersFilterSetsLosingBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsLosingBidsListCall) Context ¶
func (c *BiddersFilterSetsLosingBidsListCall) Context(ctx context.Context) *BiddersFilterSetsLosingBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsLosingBidsListCall) Do ¶
func (c *BiddersFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.losingBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListLosingBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsLosingBidsListCall) Fields ¶
func (c *BiddersFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsLosingBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsLosingBidsListCall) Header ¶
func (c *BiddersFilterSetsLosingBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsLosingBidsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsLosingBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsLosingBidsListCall) PageSize ¶
func (c *BiddersFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsLosingBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsLosingBidsListCall) PageToken ¶
func (c *BiddersFilterSetsLosingBidsListCall) PageToken(pageToken string) *BiddersFilterSetsLosingBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListLosingBidsResponse.nextPageToken returned from the previous call to the losingBids.list method.

func (*BiddersFilterSetsLosingBidsListCall) Pages ¶
func (c *BiddersFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsLosingBidsService ¶
type BiddersFilterSetsLosingBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsLosingBidsService ¶
func NewBiddersFilterSetsLosingBidsService(s *Service) *BiddersFilterSetsLosingBidsService
func (*BiddersFilterSetsLosingBidsService) List ¶
func (r *BiddersFilterSetsLosingBidsService) List(filterSetName string) *BiddersFilterSetsLosingBidsListCall

List: List all reasons for which bids lost in the auction, with the number of bids that lost for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsNonBillableWinningBidsListCall ¶
type BiddersFilterSetsNonBillableWinningBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BiddersFilterSetsNonBillableWinningBidsListCall) Context ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BiddersFilterSetsNonBillableWinningBidsListCall

Context sets the context to be used in this call's Do method.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) Do ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)

Do executes the "adexchangebuyer2.bidders.filterSets.nonBillableWinningBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListNonBillableWinningBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) Fields ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BiddersFilterSetsNonBillableWinningBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) Header ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BiddersFilterSetsNonBillableWinningBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) PageSize ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BiddersFilterSetsNonBillableWinningBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) PageToken ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BiddersFilterSetsNonBillableWinningBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListNonBillableWinningBidsResponse.nextPageToken returned from the previous call to the nonBillableWinningBids.list method.

func (*BiddersFilterSetsNonBillableWinningBidsListCall) Pages ¶
func (c *BiddersFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BiddersFilterSetsNonBillableWinningBidsService ¶
type BiddersFilterSetsNonBillableWinningBidsService struct {
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsNonBillableWinningBidsService ¶
func NewBiddersFilterSetsNonBillableWinningBidsService(s *Service) *BiddersFilterSetsNonBillableWinningBidsService
func (*BiddersFilterSetsNonBillableWinningBidsService) List ¶
func (r *BiddersFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BiddersFilterSetsNonBillableWinningBidsListCall

List: List all reasons for which winning bids were not billable, with the number of bids not billed for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BiddersFilterSetsService ¶
type BiddersFilterSetsService struct {
	BidMetrics *BiddersFilterSetsBidMetricsService

	BidResponseErrors *BiddersFilterSetsBidResponseErrorsService

	BidResponsesWithoutBids *BiddersFilterSetsBidResponsesWithoutBidsService

	FilteredBidRequests *BiddersFilterSetsFilteredBidRequestsService

	FilteredBids *BiddersFilterSetsFilteredBidsService

	ImpressionMetrics *BiddersFilterSetsImpressionMetricsService

	LosingBids *BiddersFilterSetsLosingBidsService

	NonBillableWinningBids *BiddersFilterSetsNonBillableWinningBidsService
	// contains filtered or unexported fields
}
func NewBiddersFilterSetsService ¶
func NewBiddersFilterSetsService(s *Service) *BiddersFilterSetsService
func (*BiddersFilterSetsService) Create ¶
func (r *BiddersFilterSetsService) Create(ownerName string, filterset *FilterSet) *BiddersFilterSetsCreateCall

Create: Creates the specified filter set for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter set to be created. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
func (*BiddersFilterSetsService) Delete ¶
func (r *BiddersFilterSetsService) Delete(name string) *BiddersFilterSetsDeleteCall

Delete: Deletes the requested filter set from the account with the given account ID.

name: Full name of the resource to delete. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BiddersFilterSetsService) Get ¶
func (r *BiddersFilterSetsService) Get(name string) *BiddersFilterSetsGetCall

Get: Retrieves the requested filter set for the account with the given account ID.

name: Full name of the resource being requested. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BiddersFilterSetsService) List ¶
func (r *BiddersFilterSetsService) List(ownerName string) *BiddersFilterSetsListCall

List: Lists all filter sets for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter sets to be listed. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
type BiddersService ¶
type BiddersService struct {
	Accounts *BiddersAccountsService

	FilterSets *BiddersFilterSetsService
	// contains filtered or unexported fields
}
func NewBiddersService ¶
func NewBiddersService(s *Service) *BiddersService
type Buyer ¶
type Buyer struct {
	// AccountId: Authorized Buyers account ID of the buyer.
	AccountId string `json:"accountId,omitempty"`
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

Buyer: Represents a buyer of inventory. Each buyer is identified by a unique Authorized Buyers account ID.

func (Buyer) MarshalJSON ¶
func (s Buyer) MarshalJSON() ([]byte, error)
type BuyersFilterSetsBidMetricsListCall ¶
added in v0.154.0
type BuyersFilterSetsBidMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsBidMetricsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) Context(ctx context.Context) *BuyersFilterSetsBidMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsBidMetricsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) Do(opts ...googleapi.CallOption) (*ListBidMetricsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.bidMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsBidMetricsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsBidMetricsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsBidMetricsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsBidMetricsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsBidMetricsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) PageToken(pageToken string) *BuyersFilterSetsBidMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidMetricsResponse.nextPageToken returned from the previous call to the bidMetrics.list method.

func (*BuyersFilterSetsBidMetricsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsBidMetricsListCall) Pages(ctx context.Context, f func(*ListBidMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsBidMetricsService ¶
added in v0.154.0
type BuyersFilterSetsBidMetricsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsBidMetricsService ¶
added in v0.154.0
func NewBuyersFilterSetsBidMetricsService(s *Service) *BuyersFilterSetsBidMetricsService
func (*BuyersFilterSetsBidMetricsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsBidMetricsService) List(filterSetName string) *BuyersFilterSetsBidMetricsListCall

List: Lists all metrics that are measured in terms of number of bids.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsBidResponseErrorsListCall ¶
added in v0.154.0
type BuyersFilterSetsBidResponseErrorsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsBidResponseErrorsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) Context(ctx context.Context) *BuyersFilterSetsBidResponseErrorsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsBidResponseErrorsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponseErrorsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.bidResponseErrors.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponseErrorsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsBidResponseErrorsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidResponseErrorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsBidResponseErrorsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsBidResponseErrorsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidResponseErrorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsBidResponseErrorsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidResponseErrorsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsBidResponseErrorsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) PageToken(pageToken string) *BuyersFilterSetsBidResponseErrorsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponseErrorsResponse.nextPageToken returned from the previous call to the bidResponseErrors.list method.

func (*BuyersFilterSetsBidResponseErrorsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponseErrorsListCall) Pages(ctx context.Context, f func(*ListBidResponseErrorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsBidResponseErrorsService ¶
added in v0.154.0
type BuyersFilterSetsBidResponseErrorsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsBidResponseErrorsService ¶
added in v0.154.0
func NewBuyersFilterSetsBidResponseErrorsService(s *Service) *BuyersFilterSetsBidResponseErrorsService
func (*BuyersFilterSetsBidResponseErrorsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsBidResponseErrorsService) List(filterSetName string) *BuyersFilterSetsBidResponseErrorsListCall

List: List all errors that occurred in bid responses, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsBidResponsesWithoutBidsListCall ¶
added in v0.154.0
type BuyersFilterSetsBidResponsesWithoutBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Context(ctx context.Context) *BuyersFilterSetsBidResponsesWithoutBidsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Do(opts ...googleapi.CallOption) (*ListBidResponsesWithoutBidsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.bidResponsesWithoutBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListBidResponsesWithoutBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsBidResponsesWithoutBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsBidResponsesWithoutBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsBidResponsesWithoutBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) PageToken(pageToken string) *BuyersFilterSetsBidResponsesWithoutBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListBidResponsesWithoutBidsResponse.nextPageToken returned from the previous call to the bidResponsesWithoutBids.list method.

func (*BuyersFilterSetsBidResponsesWithoutBidsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsBidResponsesWithoutBidsListCall) Pages(ctx context.Context, f func(*ListBidResponsesWithoutBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsBidResponsesWithoutBidsService ¶
added in v0.154.0
type BuyersFilterSetsBidResponsesWithoutBidsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsBidResponsesWithoutBidsService ¶
added in v0.154.0
func NewBuyersFilterSetsBidResponsesWithoutBidsService(s *Service) *BuyersFilterSetsBidResponsesWithoutBidsService
func (*BuyersFilterSetsBidResponsesWithoutBidsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsBidResponsesWithoutBidsService) List(filterSetName string) *BuyersFilterSetsBidResponsesWithoutBidsListCall

List: List all reasons for which bid responses were considered to have no applicable bids, with the number of bid responses affected for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsCreateCall ¶
added in v0.154.0
type BuyersFilterSetsCreateCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsCreateCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsCreateCall) Context(ctx context.Context) *BuyersFilterSetsCreateCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsCreateCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsCreateCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.buyers.filterSets.create" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsCreateCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsCreateCall) Fields(s ...googleapi.Field) *BuyersFilterSetsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsCreateCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsCreateCall) IsTransient ¶
added in v0.154.0
func (c *BuyersFilterSetsCreateCall) IsTransient(isTransient bool) *BuyersFilterSetsCreateCall

IsTransient sets the optional parameter "isTransient": Whether the filter set is transient, or should be persisted indefinitely. By default, filter sets are not transient. If transient, it will be available for at least 1 hour after creation.

type BuyersFilterSetsDeleteCall ¶
added in v0.154.0
type BuyersFilterSetsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsDeleteCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsDeleteCall) Context(ctx context.Context) *BuyersFilterSetsDeleteCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsDeleteCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "adexchangebuyer2.buyers.filterSets.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsDeleteCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsDeleteCall) Fields(s ...googleapi.Field) *BuyersFilterSetsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsDeleteCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type BuyersFilterSetsFilteredBidRequestsListCall ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidRequestsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsFilteredBidRequestsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidRequestsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsFilteredBidRequestsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidRequestsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.filteredBidRequests.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidRequestsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsFilteredBidRequestsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidRequestsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsFilteredBidRequestsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsFilteredBidRequestsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidRequestsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsFilteredBidRequestsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidRequestsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsFilteredBidRequestsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidRequestsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidRequestsResponse.nextPageToken returned from the previous call to the filteredBidRequests.list method.

func (*BuyersFilterSetsFilteredBidRequestsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidRequestsListCall) Pages(ctx context.Context, f func(*ListFilteredBidRequestsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsFilteredBidRequestsService ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidRequestsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsFilteredBidRequestsService ¶
added in v0.154.0
func NewBuyersFilterSetsFilteredBidRequestsService(s *Service) *BuyersFilterSetsFilteredBidRequestsService
func (*BuyersFilterSetsFilteredBidRequestsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsFilteredBidRequestsService) List(filterSetName string) *BuyersFilterSetsFilteredBidRequestsListCall

List: List all reasons that caused a bid request not to be sent for an impression, with the number of bid requests not sent for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsFilteredBidsCreativesListCall ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsCreativesListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsFilteredBidsCreativesListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsCreativesListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByCreativeResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.filteredBids.creatives.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByCreativeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsCreativesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsCreativesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsCreativesListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsCreativesListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByCreativeResponse.nextPageToken returned from the previous call to the filteredBids.creatives.list method.

func (*BuyersFilterSetsFilteredBidsCreativesListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsCreativesListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByCreativeResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsFilteredBidsCreativesService ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsCreativesService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsFilteredBidsCreativesService ¶
added in v0.154.0
func NewBuyersFilterSetsFilteredBidsCreativesService(s *Service) *BuyersFilterSetsFilteredBidsCreativesService
func (*BuyersFilterSetsFilteredBidsCreativesService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsFilteredBidsCreativesService) List(filterSetName string, creativeStatusId int64) *BuyersFilterSetsFilteredBidsCreativesListCall

List: List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by creative. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes).
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsFilteredBidsDetailsListCall ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsDetailsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsFilteredBidsDetailsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsDetailsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Do(opts ...googleapi.CallOption) (*ListCreativeStatusBreakdownByDetailResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.filteredBids.details.list" call. Any non-2xx status code is an error. Response headers are in either *ListCreativeStatusBreakdownByDetailResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsDetailsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsDetailsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsDetailsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsDetailsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByDetailResponse.nextPageToken returned from the previous call to the filteredBids.details.list method.

func (*BuyersFilterSetsFilteredBidsDetailsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsDetailsListCall) Pages(ctx context.Context, f func(*ListCreativeStatusBreakdownByDetailResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsFilteredBidsDetailsService ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsDetailsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsFilteredBidsDetailsService ¶
added in v0.154.0
func NewBuyersFilterSetsFilteredBidsDetailsService(s *Service) *BuyersFilterSetsFilteredBidsDetailsService
func (*BuyersFilterSetsFilteredBidsDetailsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsFilteredBidsDetailsService) List(filterSetName string, creativeStatusId int64) *BuyersFilterSetsFilteredBidsDetailsListCall

List: List all details associated with a specific reason for which bids were filtered, with the number of bids filtered for each detail.

creativeStatusId: The ID of the creative status for which to retrieve a breakdown by detail. See creative-status-codes (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes). Details are only available for statuses 10, 14, 15, 17, 18, 19, 86, and 87.
filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsFilteredBidsListCall ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsFilteredBidsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) Context(ctx context.Context) *BuyersFilterSetsFilteredBidsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsFilteredBidsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) Do(opts ...googleapi.CallOption) (*ListFilteredBidsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.filteredBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilteredBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsFilteredBidsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsFilteredBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsFilteredBidsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsFilteredBidsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsFilteredBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsFilteredBidsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsFilteredBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsFilteredBidsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) PageToken(pageToken string) *BuyersFilterSetsFilteredBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidsResponse.nextPageToken returned from the previous call to the filteredBids.list method.

func (*BuyersFilterSetsFilteredBidsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsFilteredBidsListCall) Pages(ctx context.Context, f func(*ListFilteredBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsFilteredBidsService ¶
added in v0.154.0
type BuyersFilterSetsFilteredBidsService struct {
	Creatives *BuyersFilterSetsFilteredBidsCreativesService

	Details *BuyersFilterSetsFilteredBidsDetailsService
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsFilteredBidsService ¶
added in v0.154.0
func NewBuyersFilterSetsFilteredBidsService(s *Service) *BuyersFilterSetsFilteredBidsService
func (*BuyersFilterSetsFilteredBidsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsFilteredBidsService) List(filterSetName string) *BuyersFilterSetsFilteredBidsListCall

List: List all reasons for which bids were filtered, with the number of bids filtered for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsGetCall ¶
added in v0.154.0
type BuyersFilterSetsGetCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsGetCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsGetCall) Context(ctx context.Context) *BuyersFilterSetsGetCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsGetCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsGetCall) Do(opts ...googleapi.CallOption) (*FilterSet, error)

Do executes the "adexchangebuyer2.buyers.filterSets.get" call. Any non-2xx status code is an error. Response headers are in either *FilterSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsGetCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsGetCall) Fields(s ...googleapi.Field) *BuyersFilterSetsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsGetCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsGetCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsGetCall) IfNoneMatch(entityTag string) *BuyersFilterSetsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type BuyersFilterSetsImpressionMetricsListCall ¶
added in v0.154.0
type BuyersFilterSetsImpressionMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsImpressionMetricsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) Context(ctx context.Context) *BuyersFilterSetsImpressionMetricsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsImpressionMetricsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) Do(opts ...googleapi.CallOption) (*ListImpressionMetricsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.impressionMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *ListImpressionMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsImpressionMetricsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsImpressionMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsImpressionMetricsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsImpressionMetricsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsImpressionMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsImpressionMetricsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) PageSize(pageSize int64) *BuyersFilterSetsImpressionMetricsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsImpressionMetricsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) PageToken(pageToken string) *BuyersFilterSetsImpressionMetricsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListImpressionMetricsResponse.nextPageToken returned from the previous call to the impressionMetrics.list method.

func (*BuyersFilterSetsImpressionMetricsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsImpressionMetricsListCall) Pages(ctx context.Context, f func(*ListImpressionMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsImpressionMetricsService ¶
added in v0.154.0
type BuyersFilterSetsImpressionMetricsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsImpressionMetricsService ¶
added in v0.154.0
func NewBuyersFilterSetsImpressionMetricsService(s *Service) *BuyersFilterSetsImpressionMetricsService
func (*BuyersFilterSetsImpressionMetricsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsImpressionMetricsService) List(filterSetName string) *BuyersFilterSetsImpressionMetricsListCall

List: Lists all metrics that are measured in terms of number of impressions.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsListCall ¶
added in v0.154.0
type BuyersFilterSetsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) Context(ctx context.Context) *BuyersFilterSetsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) Do(opts ...googleapi.CallOption) (*ListFilterSetsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.list" call. Any non-2xx status code is an error. Response headers are in either *ListFilterSetsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) PageSize(pageSize int64) *BuyersFilterSetsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) PageToken(pageToken string) *BuyersFilterSetsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListFilterSetsResponse.nextPageToken returned from the previous call to the accounts.filterSets.list method.

func (*BuyersFilterSetsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsListCall) Pages(ctx context.Context, f func(*ListFilterSetsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsLosingBidsListCall ¶
added in v0.154.0
type BuyersFilterSetsLosingBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsLosingBidsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) Context(ctx context.Context) *BuyersFilterSetsLosingBidsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsLosingBidsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) Do(opts ...googleapi.CallOption) (*ListLosingBidsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.losingBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListLosingBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsLosingBidsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsLosingBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsLosingBidsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsLosingBidsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsLosingBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsLosingBidsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsLosingBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsLosingBidsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) PageToken(pageToken string) *BuyersFilterSetsLosingBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListLosingBidsResponse.nextPageToken returned from the previous call to the losingBids.list method.

func (*BuyersFilterSetsLosingBidsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsLosingBidsListCall) Pages(ctx context.Context, f func(*ListLosingBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsLosingBidsService ¶
added in v0.154.0
type BuyersFilterSetsLosingBidsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsLosingBidsService ¶
added in v0.154.0
func NewBuyersFilterSetsLosingBidsService(s *Service) *BuyersFilterSetsLosingBidsService
func (*BuyersFilterSetsLosingBidsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsLosingBidsService) List(filterSetName string) *BuyersFilterSetsLosingBidsListCall

List: List all reasons for which bids lost in the auction, with the number of bids that lost for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsNonBillableWinningBidsListCall ¶
added in v0.154.0
type BuyersFilterSetsNonBillableWinningBidsListCall struct {
	// contains filtered or unexported fields
}
func (*BuyersFilterSetsNonBillableWinningBidsListCall) Context ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Context(ctx context.Context) *BuyersFilterSetsNonBillableWinningBidsListCall

Context sets the context to be used in this call's Do method.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) Do ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Do(opts ...googleapi.CallOption) (*ListNonBillableWinningBidsResponse, error)

Do executes the "adexchangebuyer2.buyers.filterSets.nonBillableWinningBids.list" call. Any non-2xx status code is an error. Response headers are in either *ListNonBillableWinningBidsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) Fields ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Fields(s ...googleapi.Field) *BuyersFilterSetsNonBillableWinningBidsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) Header ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) IfNoneMatch(entityTag string) *BuyersFilterSetsNonBillableWinningBidsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) PageSize ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) PageSize(pageSize int64) *BuyersFilterSetsNonBillableWinningBidsListCall

PageSize sets the optional parameter "pageSize": Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) PageToken ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) PageToken(pageToken string) *BuyersFilterSetsNonBillableWinningBidsListCall

PageToken sets the optional parameter "pageToken": A token identifying a page of results the server should return. Typically, this is the value of ListNonBillableWinningBidsResponse.nextPageToken returned from the previous call to the nonBillableWinningBids.list method.

func (*BuyersFilterSetsNonBillableWinningBidsListCall) Pages ¶
added in v0.154.0
func (c *BuyersFilterSetsNonBillableWinningBidsListCall) Pages(ctx context.Context, f func(*ListNonBillableWinningBidsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type BuyersFilterSetsNonBillableWinningBidsService ¶
added in v0.154.0
type BuyersFilterSetsNonBillableWinningBidsService struct {
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsNonBillableWinningBidsService ¶
added in v0.154.0
func NewBuyersFilterSetsNonBillableWinningBidsService(s *Service) *BuyersFilterSetsNonBillableWinningBidsService
func (*BuyersFilterSetsNonBillableWinningBidsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsNonBillableWinningBidsService) List(filterSetName string) *BuyersFilterSetsNonBillableWinningBidsListCall

List: List all reasons for which winning bids were not billable, with the number of bids not billed for each reason.

filterSetName: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
type BuyersFilterSetsService ¶
added in v0.154.0
type BuyersFilterSetsService struct {
	BidMetrics *BuyersFilterSetsBidMetricsService

	BidResponseErrors *BuyersFilterSetsBidResponseErrorsService

	BidResponsesWithoutBids *BuyersFilterSetsBidResponsesWithoutBidsService

	FilteredBidRequests *BuyersFilterSetsFilteredBidRequestsService

	FilteredBids *BuyersFilterSetsFilteredBidsService

	ImpressionMetrics *BuyersFilterSetsImpressionMetricsService

	LosingBids *BuyersFilterSetsLosingBidsService

	NonBillableWinningBids *BuyersFilterSetsNonBillableWinningBidsService
	// contains filtered or unexported fields
}
func NewBuyersFilterSetsService ¶
added in v0.154.0
func NewBuyersFilterSetsService(s *Service) *BuyersFilterSetsService
func (*BuyersFilterSetsService) Create ¶
added in v0.154.0
func (r *BuyersFilterSetsService) Create(ownerName string, filterset *FilterSet) *BuyersFilterSetsCreateCall

Create: Creates the specified filter set for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter set to be created. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
func (*BuyersFilterSetsService) Delete ¶
added in v0.154.0
func (r *BuyersFilterSetsService) Delete(name string) *BuyersFilterSetsDeleteCall

Delete: Deletes the requested filter set from the account with the given account ID.

name: Full name of the resource to delete. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BuyersFilterSetsService) Get ¶
added in v0.154.0
func (r *BuyersFilterSetsService) Get(name string) *BuyersFilterSetsGetCall

Get: Retrieves the requested filter set for the account with the given account ID.

name: Full name of the resource being requested. For example: - For a bidder-level filter set for bidder 123: `bidders/123/filterSets/abc` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123/filterSets/abc` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456/filterSets/abc`.
func (*BuyersFilterSetsService) List ¶
added in v0.154.0
func (r *BuyersFilterSetsService) List(ownerName string) *BuyersFilterSetsListCall

List: Lists all filter sets for the account with the given account ID.

ownerName: Name of the owner (bidder or account) of the filter sets to be listed. For example: - For a bidder-level filter set for bidder 123: `bidders/123` - For an account-level filter set for the buyer account representing bidder 123: `bidders/123/accounts/123` - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: `bidders/123/accounts/456`.
type BuyersService ¶
added in v0.154.0
type BuyersService struct {
	FilterSets *BuyersFilterSetsService
	// contains filtered or unexported fields
}
func NewBuyersService ¶
added in v0.154.0
func NewBuyersService(s *Service) *BuyersService
type CalloutStatusRow ¶
type CalloutStatusRow struct {
	// CalloutStatusId: The ID of the callout status. See callout-status-codes
	// (https://developers.google.com/authorized-buyers/rtb/downloads/callout-status-codes).
	CalloutStatusId int64 `json:"calloutStatusId,omitempty"`
	// ImpressionCount: The number of impressions for which there was a bid request
	// or bid response with the specified callout status.
	ImpressionCount *MetricValue `json:"impressionCount,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CalloutStatusId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CalloutStatusId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CalloutStatusRow: The number of impressions with the specified dimension values where the corresponding bid request or bid response was not successful, as described by the specified callout status.

func (CalloutStatusRow) MarshalJSON ¶
func (s CalloutStatusRow) MarshalJSON() ([]byte, error)
type CancelNegotiationRequest ¶
type CancelNegotiationRequest struct {
}

CancelNegotiationRequest: Request to cancel an ongoing negotiation.

type Client ¶
type Client struct {
	// ClientAccountId: The globally-unique numerical ID of the client. The value
	// of this field is ignored in create and update operations.
	ClientAccountId int64 `json:"clientAccountId,omitempty,string"`
	// ClientName: Name used to represent this client to publishers. You may have
	// multiple clients that map to the same entity, but for each client the
	// combination of `clientName` and entity must be unique. You can specify this
	// field as empty. Maximum length of 255 characters is allowed.
	ClientName string `json:"clientName,omitempty"`
	// EntityId: Numerical identifier of the client entity. The entity can be an
	// advertiser, a brand, or an agency. This identifier is unique among all the
	// entities with the same type. The value of this field is ignored if the
	// entity type is not provided. A list of all known advertisers with their
	// identifiers is available in the advertisers.txt
	// (https://storage.googleapis.com/adx-rtb-dictionaries/advertisers.txt) file.
	// A list of all known brands with their identifiers is available in the
	// brands.txt (https://storage.googleapis.com/adx-rtb-dictionaries/brands.txt)
	// file. A list of all known agencies with their identifiers is available in
	// the agencies.txt
	// (https://storage.googleapis.com/adx-rtb-dictionaries/agencies.txt) file.
	EntityId int64 `json:"entityId,omitempty,string"`
	// EntityName: The name of the entity. This field is automatically fetched
	// based on the type and ID. The value of this field is ignored in create and
	// update operations.
	EntityName string `json:"entityName,omitempty"`
	// EntityType: An optional field for specifying the type of the client entity:
	// `ADVERTISER`, `BRAND`, or `AGENCY`.
	//
	// Possible values:
	//   "ENTITY_TYPE_UNSPECIFIED" - A placeholder for an undefined client entity
	// type. Should not be used.
	//   "ADVERTISER" - An advertiser.
	//   "BRAND" - A brand.
	//   "AGENCY" - An advertising agency.
	//   "ENTITY_TYPE_UNCLASSIFIED" - An explicit value for a client that was not
	// yet classified as any particular entity.
	EntityType string `json:"entityType,omitempty"`
	// PartnerClientId: Optional arbitrary unique identifier of this client buyer
	// from the standpoint of its Ad Exchange sponsor buyer. This field can be used
	// to associate a client buyer with the identifier in the namespace of its
	// sponsor buyer, lookup client buyers by that identifier and verify whether an
	// Ad Exchange counterpart of a given client buyer already exists. If present,
	// must be unique among all the client buyers for its Ad Exchange sponsor
	// buyer.
	PartnerClientId string `json:"partnerClientId,omitempty"`
	// Role: The role which is assigned to the client buyer. Each role implies a
	// set of permissions granted to the client. Must be one of
	// `CLIENT_DEAL_VIEWER`, `CLIENT_DEAL_NEGOTIATOR` or `CLIENT_DEAL_APPROVER`.
	//
	// Possible values:
	//   "CLIENT_ROLE_UNSPECIFIED" - A placeholder for an undefined client role.
	//   "CLIENT_DEAL_VIEWER" - Users associated with this client can see publisher
	// deal offers in the Marketplace. They can neither negotiate proposals nor
	// approve deals. If this client is visible to publishers, they can send deal
	// proposals to this client.
	//   "CLIENT_DEAL_NEGOTIATOR" - Users associated with this client can respond
	// to deal proposals sent to them by publishers. They can also initiate deal
	// proposals of their own.
	//   "CLIENT_DEAL_APPROVER" - Users associated with this client can approve
	// eligible deals on your behalf. Some deals may still explicitly require
	// publisher finalization. If this role is not selected, the sponsor buyer will
	// need to manually approve each of their deals.
	Role string `json:"role,omitempty"`
	// Status: The status of the client buyer.
	//
	// Possible values:
	//   "CLIENT_STATUS_UNSPECIFIED" - A placeholder for an undefined client
	// status.
	//   "DISABLED" - A client that is currently disabled.
	//   "ACTIVE" - A client that is currently active.
	Status string `json:"status,omitempty"`
	// VisibleToSeller: Whether the client buyer will be visible to sellers.
	VisibleToSeller bool `json:"visibleToSeller,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClientAccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientAccountId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Client: A client resource represents a client buyer—an agency, a brand, or an advertiser customer of the sponsor buyer. Users associated with the client buyer have restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the client buyer. All fields are required unless otherwise specified.

func (Client) MarshalJSON ¶
func (s Client) MarshalJSON() ([]byte, error)
type ClientUser ¶
type ClientUser struct {
	// ClientAccountId: Numerical account ID of the client buyer with which the
	// user is associated; the buyer must be a client of the current sponsor buyer.
	// The value of this field is ignored in an update operation.
	ClientAccountId int64 `json:"clientAccountId,omitempty,string"`
	// Email: User's email address. The value of this field is ignored in an update
	// operation.
	Email string `json:"email,omitempty"`
	// Status: The status of the client user.
	//
	// Possible values:
	//   "USER_STATUS_UNSPECIFIED" - A placeholder for an undefined user status.
	//   "PENDING" - A user who was already created but hasn't accepted the
	// invitation yet.
	//   "ACTIVE" - A user that is currently active.
	//   "DISABLED" - A user that is currently disabled.
	Status string `json:"status,omitempty"`
	// UserId: The unique numerical ID of the client user that has accepted an
	// invitation. The value of this field is ignored in an update operation.
	UserId int64 `json:"userId,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClientAccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientAccountId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClientUser: A client user is created under a client buyer and has restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the associated client buyer. The only way a new client user can be created is through accepting an email invitation (see the accounts.clients.invitations.create method). All fields are required unless otherwise specified.

func (ClientUser) MarshalJSON ¶
func (s ClientUser) MarshalJSON() ([]byte, error)
type ClientUserInvitation ¶
type ClientUserInvitation struct {
	// ClientAccountId: Numerical account ID of the client buyer that the invited
	// user is associated with. The value of this field is ignored in create
	// operations.
	ClientAccountId int64 `json:"clientAccountId,omitempty,string"`
	// Email: The email address to which the invitation is sent. Email addresses
	// should be unique among all client users under each sponsor buyer.
	Email string `json:"email,omitempty"`
	// InvitationId: The unique numerical ID of the invitation that is sent to the
	// user. The value of this field is ignored in create operations.
	InvitationId int64 `json:"invitationId,omitempty,string"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClientAccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientAccountId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClientUserInvitation: An invitation for a new client user to get access to the Authorized Buyers UI. All fields are required unless otherwise specified.

func (ClientUserInvitation) MarshalJSON ¶
func (s ClientUserInvitation) MarshalJSON() ([]byte, error)
type CompleteSetupRequest ¶
type CompleteSetupRequest struct {
}

CompleteSetupRequest: Request message for indicating that the proposal's setup step is complete.

type ContactInformation ¶
type ContactInformation struct {
	// Email: Email address for the contact.
	Email string `json:"email,omitempty"`
	// Name: The name of the contact.
	Name string `json:"name,omitempty"`
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

ContactInformation: Contains information on how a buyer or seller can be reached.

func (ContactInformation) MarshalJSON ¶
func (s ContactInformation) MarshalJSON() ([]byte, error)
type Correction ¶
type Correction struct {
	// Contexts: The contexts for the correction.
	Contexts []*ServingContext `json:"contexts,omitempty"`
	// Details: Additional details about what was corrected.
	Details []string `json:"details,omitempty"`
	// Type: The type of correction that was applied to the creative.
	//
	// Possible values:
	//   "CORRECTION_TYPE_UNSPECIFIED" - The correction type is unknown. Refer to
	// the details for more information.
	//   "VENDOR_IDS_ADDED" - The ad's declared vendors did not match the vendors
	// that were detected. The detected vendors were added.
	//   "SSL_ATTRIBUTE_REMOVED" - The ad had the SSL attribute declared but was
	// not SSL-compliant. The SSL attribute was removed.
	//   "FLASH_FREE_ATTRIBUTE_REMOVED" - The ad was declared as Flash-free but
	// contained Flash, so the Flash-free attribute was removed.
	//   "FLASH_FREE_ATTRIBUTE_ADDED" - The ad was not declared as Flash-free but
	// it did not reference any flash content, so the Flash-free attribute was
	// added.
	//   "REQUIRED_ATTRIBUTE_ADDED" - The ad did not declare a required creative
	// attribute. The attribute was added.
	//   "REQUIRED_VENDOR_ADDED" - The ad did not declare a required technology
	// vendor. The technology vendor was added.
	//   "SSL_ATTRIBUTE_ADDED" - The ad did not declare the SSL attribute but was
	// SSL-compliant, so the SSL attribute was added.
	//   "IN_BANNER_VIDEO_ATTRIBUTE_ADDED" - Properties consistent with In-banner
	// video were found, so an In-Banner Video attribute was added.
	//   "MRAID_ATTRIBUTE_ADDED" - The ad makes calls to the MRAID API so the MRAID
	// attribute was added.
	//   "FLASH_ATTRIBUTE_REMOVED" - The ad unnecessarily declared the Flash
	// attribute, so the Flash attribute was removed.
	//   "VIDEO_IN_SNIPPET_ATTRIBUTE_ADDED" - The ad contains video content.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Contexts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Contexts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Correction: Output only. Shows any corrections that were applied to this creative.

func (Correction) MarshalJSON ¶
func (s Correction) MarshalJSON() ([]byte, error)
type Creative ¶
type Creative struct {
	// AccountId: The account that this creative belongs to. Can be used to filter
	// the response of the creatives.list method.
	AccountId string `json:"accountId,omitempty"`
	// AdChoicesDestinationUrl: The link to AdChoices destination page.
	AdChoicesDestinationUrl string `json:"adChoicesDestinationUrl,omitempty"`
	// AdTechnologyProviders: Output only. The detected ad technology providers.
	AdTechnologyProviders *AdTechnologyProviders `json:"adTechnologyProviders,omitempty"`
	// AdvertiserName: The name of the company being advertised in the creative.
	AdvertiserName string `json:"advertiserName,omitempty"`
	// AgencyId: The agency ID for this creative.
	AgencyId int64 `json:"agencyId,omitempty,string"`
	// ApiUpdateTime: Output only. The last update timestamp of the creative
	// through the API.
	ApiUpdateTime string `json:"apiUpdateTime,omitempty"`
	// Attributes: All attributes for the ads that may be shown from this creative.
	// Can be used to filter the response of the creatives.list method.
	//
	// Possible values:
	//   "ATTRIBUTE_UNSPECIFIED" - Do not use. This is a placeholder value only.
	//   "IMAGE_RICH_MEDIA" - The creative is of type image/rich media. For
	// pretargeting.
	//   "ADOBE_FLASH_FLV" - The creative is of video type Adobe Flash FLV. For
	// pretargeting.
	//   "IS_TAGGED" - The creative is tagged.
	//   "IS_COOKIE_TARGETED" - The creative is cookie targeted.
	//   "IS_USER_INTEREST_TARGETED" - The creative is user interest targeted.
	//   "EXPANDING_DIRECTION_NONE" - The creative does not expand.
	//   "EXPANDING_DIRECTION_UP" - The creative expands up.
	//   "EXPANDING_DIRECTION_DOWN" - The creative expands down.
	//   "EXPANDING_DIRECTION_LEFT" - The creative expands left.
	//   "EXPANDING_DIRECTION_RIGHT" - The creative expands right.
	//   "EXPANDING_DIRECTION_UP_LEFT" - The creative expands up and left.
	//   "EXPANDING_DIRECTION_UP_RIGHT" - The creative expands up and right.
	//   "EXPANDING_DIRECTION_DOWN_LEFT" - The creative expands down and left.
	//   "EXPANDING_DIRECTION_DOWN_RIGHT" - The creative expands down and right.
	//   "CREATIVE_TYPE_HTML" - The creative type is HTML.
	//   "CREATIVE_TYPE_VAST_VIDEO" - The creative type is VAST video.
	//   "EXPANDING_DIRECTION_UP_OR_DOWN" - The creative expands up or down.
	//   "EXPANDING_DIRECTION_LEFT_OR_RIGHT" - The creative expands left or right.
	//   "EXPANDING_DIRECTION_ANY_DIAGONAL" - The creative expands on any diagonal.
	//   "EXPANDING_ACTION_ROLLOVER_TO_EXPAND" - The creative expands when rolled
	// over.
	//   "INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH" - The instream vast video type is
	// vpaid flash.
	//   "RICH_MEDIA_CAPABILITY_TYPE_MRAID" - The creative is MRAID.
	//   "RICH_MEDIA_CAPABILITY_TYPE_FLASH" - The creative is Flash.
	//   "RICH_MEDIA_CAPABILITY_TYPE_HTML5" - The creative is HTML5.
	//   "SKIPPABLE_INSTREAM_VIDEO" - The creative has an instream VAST video type
	// of skippable instream video. For pretargeting.
	//   "RICH_MEDIA_CAPABILITY_TYPE_SSL" - The creative is SSL.
	//   "RICH_MEDIA_CAPABILITY_TYPE_NON_SSL" - The creative is non-SSL.
	//   "RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL" - The creative is an
	// interstitial.
	//   "NON_SKIPPABLE_INSTREAM_VIDEO" - The creative has an instream VAST video
	// type of non-skippable instream video. For pretargeting.
	//   "NATIVE_ELIGIBILITY_ELIGIBLE" - The creative is eligible for native.
	//   "NON_VPAID" - The creative has an instream VAST video type of non-VPAID.
	// For pretargeting.
	//   "NATIVE_ELIGIBILITY_NOT_ELIGIBLE" - The creative is not eligible for
	// native.
	//   "ANY_INTERSTITIAL" - The creative has an interstitial size of any
	// interstitial. For pretargeting.
	//   "NON_INTERSTITIAL" - The creative has an interstitial size of non
	// interstitial. For pretargeting.
	//   "IN_BANNER_VIDEO" - The video type is in-banner video.
	//   "RENDERING_SIZELESS_ADX" - The creative can dynamically resize to fill a
	// variety of slot sizes.
	//   "OMSDK_1_0" - The open measurement SDK is supported.
	//   "RENDERING_PLAYABLE" - The creative is considered a playable display
	// creative.
	Attributes []string `json:"attributes,omitempty"`
	// ClickThroughUrls: The set of destination URLs for the creative.
	ClickThroughUrls []string `json:"clickThroughUrls,omitempty"`
	// Corrections: Output only. Shows any corrections that were applied to this
	// creative.
	Corrections []*Correction `json:"corrections,omitempty"`
	// CreativeId: The buyer-defined creative ID of this creative. Can be used to
	// filter the response of the creatives.list method.
	CreativeId string `json:"creativeId,omitempty"`
	// DealsStatus: Output only. The top-level deals status of this creative. If
	// disapproved, an entry for 'auctionType=DIRECT_DEALS' (or 'ALL') in
	// serving_restrictions will also exist. Note that this may be nuanced with
	// other contextual restrictions, in which case, it may be preferable to read
	// from serving_restrictions directly. Can be used to filter the response of
	// the creatives.list method.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - The status is unknown.
	//   "NOT_CHECKED" - The creative has not been checked.
	//   "CONDITIONALLY_APPROVED" - The creative has been conditionally approved.
	// See serving_restrictions for details.
	//   "APPROVED" - The creative has been approved.
	//   "DISAPPROVED" - The creative has been disapproved.
	//   "PENDING_REVIEW" - Placeholder for transition to v1beta1. Currently not
	// used.
	//   "STATUS_TYPE_UNSPECIFIED" - Placeholder for transition to v1beta1.
	// Currently not used.
	DealsStatus string `json:"dealsStatus,omitempty"`
	// DeclaredClickThroughUrls: The set of declared destination URLs for the
	// creative.
	DeclaredClickThroughUrls []string `json:"declaredClickThroughUrls,omitempty"`
	// DetectedAdvertiserIds: Output only. Detected advertiser IDs, if any.
	DetectedAdvertiserIds googleapi.Int64s `json:"detectedAdvertiserIds,omitempty"`
	// DetectedDomains: Output only. The detected domains for this creative.
	DetectedDomains []string `json:"detectedDomains,omitempty"`
	// DetectedLanguages: Output only. The detected languages for this creative.
	// The order is arbitrary. The codes are 2 or 5 characters and are documented
	// at https://developers.google.com/adwords/api/docs/appendix/languagecodes.
	DetectedLanguages []string `json:"detectedLanguages,omitempty"`
	// DetectedProductCategories: Output only. Detected product categories, if any.
	// See the ad-product-categories.txt file in the technical documentation for a
	// list of IDs.
	DetectedProductCategories []int64 `json:"detectedProductCategories,omitempty"`
	// DetectedSensitiveCategories: Output only. Detected sensitive categories, if
	// any. See the ad-sensitive-categories.txt file in the technical documentation
	// for a list of IDs. You should use these IDs along with the
	// excluded-sensitive-category field in the bid request to filter your bids.
	DetectedSensitiveCategories []int64 `json:"detectedSensitiveCategories,omitempty"`
	// Html: An HTML creative.
	Html *HtmlContent `json:"html,omitempty"`
	// ImpressionTrackingUrls: The set of URLs to be called to record an
	// impression.
	ImpressionTrackingUrls []string `json:"impressionTrackingUrls,omitempty"`
	// Native: A native creative.
	Native *NativeContent `json:"native,omitempty"`
	// OpenAuctionStatus: Output only. The top-level open auction status of this
	// creative. If disapproved, an entry for 'auctionType = OPEN_AUCTION' (or
	// 'ALL') in serving_restrictions will also exist. Note that this may be
	// nuanced with other contextual restrictions, in which case, it may be
	// preferable to read from serving_restrictions directly. Can be used to filter
	// the response of the creatives.list method.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - The status is unknown.
	//   "NOT_CHECKED" - The creative has not been checked.
	//   "CONDITIONALLY_APPROVED" - The creative has been conditionally approved.
	// See serving_restrictions for details.
	//   "APPROVED" - The creative has been approved.
	//   "DISAPPROVED" - The creative has been disapproved.
	//   "PENDING_REVIEW" - Placeholder for transition to v1beta1. Currently not
	// used.
	//   "STATUS_TYPE_UNSPECIFIED" - Placeholder for transition to v1beta1.
	// Currently not used.
	OpenAuctionStatus string `json:"openAuctionStatus,omitempty"`
	// RestrictedCategories: All restricted categories for the ads that may be
	// shown from this creative.
	//
	// Possible values:
	//   "NO_RESTRICTED_CATEGORIES" - The ad has no restricted categories
	//   "ALCOHOL" - The alcohol restricted category.
	RestrictedCategories []string `json:"restrictedCategories,omitempty"`
	// ServingRestrictions: Output only. The granular status of this ad in specific
	// contexts. A context here relates to where something ultimately serves (for
	// example, a physical location, a platform, an HTTPS versus HTTP request, or
	// the type of auction).
	ServingRestrictions []*ServingRestriction `json:"servingRestrictions,omitempty"`
	// VendorIds: All vendor IDs for the ads that may be shown from this creative.
	// See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for
	// possible values.
	VendorIds []int64 `json:"vendorIds,omitempty"`
	// Version: Output only. The version of this creative.
	Version int64 `json:"version,omitempty"`
	// Video: A video creative.
	Video *VideoContent `json:"video,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
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

Creative: A creative and its classification data.

func (Creative) MarshalJSON ¶
func (s Creative) MarshalJSON() ([]byte, error)
type CreativeDealAssociation ¶
type CreativeDealAssociation struct {
	// AccountId: The account the creative belongs to.
	AccountId string `json:"accountId,omitempty"`
	// CreativeId: The ID of the creative associated with the deal.
	CreativeId string `json:"creativeId,omitempty"`
	// DealsId: The externalDealId for the deal associated with the creative.
	DealsId string `json:"dealsId,omitempty"`
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

CreativeDealAssociation: The association between a creative and a deal.

func (CreativeDealAssociation) MarshalJSON ¶
func (s CreativeDealAssociation) MarshalJSON() ([]byte, error)
type CreativeRestrictions ¶
type CreativeRestrictions struct {
	// CreativeFormat: The format of the environment that the creatives will be
	// displayed in.
	//
	// Possible values:
	//   "CREATIVE_FORMAT_UNSPECIFIED" - A placeholder for an undefined creative
	// format.
	//   "DISPLAY" - A creative that will be displayed in environments such as a
	// browser.
	//   "VIDEO" - A video creative that will be displayed in environments such as
	// a video player.
	CreativeFormat         string                   `json:"creativeFormat,omitempty"`
	CreativeSpecifications []*CreativeSpecification `json:"creativeSpecifications,omitempty"`
	// SkippableAdType: Skippable video ads allow viewers to skip ads after 5
	// seconds.
	//
	// Possible values:
	//   "SKIPPABLE_AD_TYPE_UNSPECIFIED" - A placeholder for an undefined skippable
	// ad type.
	//   "SKIPPABLE" - This video ad can be skipped after 5 seconds.
	//   "INSTREAM_SELECT" - This video ad can be skipped after 5 seconds, and is
	// counted as engaged view after 30 seconds. The creative is hosted on YouTube
	// only, and viewcount of the YouTube video increments after the engaged view.
	//   "NOT_SKIPPABLE" - This video ad is not skippable.
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

CreativeRestrictions: Represents creative restrictions associated to Programmatic Guaranteed/ Preferred Deal in Ad Manager. This doesn't apply to Private Auction and AdX Preferred Deals.

func (CreativeRestrictions) MarshalJSON ¶
func (s CreativeRestrictions) MarshalJSON() ([]byte, error)
type CreativeSize ¶
type CreativeSize struct {
	// AllowedFormats: What formats are allowed by the publisher. If this repeated
	// field is empty then all formats are allowed. For example, if this field
	// contains AllowedFormatType.AUDIO then the publisher only allows an audio ad
	// (without any video).
	//
	// Possible values:
	//   "UNKNOWN" - A placeholder for an undefined allowed format.
	//   "AUDIO" - An audio-only ad (without any video).
	AllowedFormats []string `json:"allowedFormats,omitempty"`
	// CompanionSizes: For video creatives specifies the sizes of companion ads (if
	// present). Companion sizes may be filled in only when creative_size_type =
	// VIDEO
	CompanionSizes []*Size `json:"companionSizes,omitempty"`
	// CreativeSizeType: The creative size type.
	//
	// Possible values:
	//   "CREATIVE_SIZE_TYPE_UNSPECIFIED" - A placeholder for an undefined creative
	// size type.
	//   "REGULAR" - The creative is a regular desktop creative.
	//   "INTERSTITIAL" - The creative is an interstitial creative.
	//   "VIDEO" - The creative is a video creative.
	//   "NATIVE" - The creative is a native (mobile) creative.
	CreativeSizeType string `json:"creativeSizeType,omitempty"`
	// NativeTemplate: Output only. The native template for this creative. It will
	// have a value only if creative_size_type = CreativeSizeType.NATIVE.
	//
	// Possible values:
	//   "UNKNOWN_NATIVE_TEMPLATE" - A placeholder for an undefined native
	// template.
	//   "NATIVE_CONTENT_AD" - The creative is linked to native content ad.
	//   "NATIVE_APP_INSTALL_AD" - The creative is linked to native app install ad.
	//   "NATIVE_VIDEO_CONTENT_AD" - The creative is linked to native video content
	// ad.
	//   "NATIVE_VIDEO_APP_INSTALL_AD" - The creative is linked to native video app
	// install ad.
	NativeTemplate string `json:"nativeTemplate,omitempty"`
	// Size: For regular or video creative size type, specifies the size of the
	// creative
	Size *Size `json:"size,omitempty"`
	// SkippableAdType: The type of skippable ad for this creative. It will have a
	// value only if creative_size_type = CreativeSizeType.VIDEO.
	//
	// Possible values:
	//   "SKIPPABLE_AD_TYPE_UNSPECIFIED" - A placeholder for an undefined skippable
	// ad type.
	//   "GENERIC" - This video ad can be skipped after 5 seconds.
	//   "INSTREAM_SELECT" - This video ad can be skipped after 5 seconds, and
	// count as engaged view after 30 seconds. The creative is hosted on YouTube
	// only, and viewcount of the YouTube video increments after the engaged view.
	//   "NOT_SKIPPABLE" - This video ad is not skippable.
	SkippableAdType string `json:"skippableAdType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowedFormats") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedFormats") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreativeSize: Specifies the size of the creative.

func (CreativeSize) MarshalJSON ¶
func (s CreativeSize) MarshalJSON() ([]byte, error)
type CreativeSpecification ¶
type CreativeSpecification struct {
	// CreativeCompanionSizes: Companion sizes may be filled in only when this is a
	// video creative.
	CreativeCompanionSizes []*AdSize `json:"creativeCompanionSizes,omitempty"`
	// CreativeSize: The size of the creative.
	CreativeSize *AdSize `json:"creativeSize,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreativeCompanionSizes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeCompanionSizes") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreativeSpecification: Represents information for a creative that is associated with a Programmatic Guaranteed/Preferred Deal in Ad Manager.

func (CreativeSpecification) MarshalJSON ¶
func (s CreativeSpecification) MarshalJSON() ([]byte, error)
type CreativeStatusRow ¶
type CreativeStatusRow struct {
	// BidCount: The number of bids with the specified status.
	BidCount *MetricValue `json:"bidCount,omitempty"`
	// CreativeStatusId: The ID of the creative status. See creative-status-codes
	// (https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes).
	CreativeStatusId int64 `json:"creativeStatusId,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BidCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BidCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CreativeStatusRow: The number of bids with the specified dimension values that did not win the auction (either were filtered pre-auction or lost the auction), as described by the specified creative status.

func (CreativeStatusRow) MarshalJSON ¶
func (s CreativeStatusRow) MarshalJSON() ([]byte, error)
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

CriteriaTargeting: Generic targeting used for targeting dimensions that contains a list of included and excluded numeric IDs.

func (CriteriaTargeting) MarshalJSON ¶
func (s CriteriaTargeting) MarshalJSON() ([]byte, error)
type Date ¶
type Date struct {
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

Date: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp

func (Date) MarshalJSON ¶
func (s Date) MarshalJSON() ([]byte, error)
type DayPart ¶
type DayPart struct {
	// DayOfWeek: The day of the week to target. If unspecified, applicable to all
	// days.
	//
	// Possible values:
	//   "DAY_OF_WEEK_UNSPECIFIED" - A placeholder for when the day of the week is
	// not specified.
	//   "MONDAY" - Monday
	//   "TUESDAY" - Tuesday
	//   "WEDNESDAY" - Wednesday
	//   "THURSDAY" - Thursday
	//   "FRIDAY" - Friday
	//   "SATURDAY" - Saturday
	//   "SUNDAY" - Sunday
	DayOfWeek string `json:"dayOfWeek,omitempty"`
	// EndTime: The ending time of the day for the ad to show (minute level
	// granularity). The end time is exclusive. This field is not available for
	// filtering in PQL queries.
	EndTime *TimeOfDay `json:"endTime,omitempty"`
	// StartTime: The starting time of day for the ad to show (minute level
	// granularity). The start time is inclusive. This field is not available for
	// filtering in PQL queries.
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

DayPart: Daypart targeting message that specifies if the ad can be shown only during certain parts of a day/week.

func (DayPart) MarshalJSON ¶
func (s DayPart) MarshalJSON() ([]byte, error)
type DayPartTargeting ¶
type DayPartTargeting struct {
	// DayParts: A list of day part targeting criterion.
	DayParts []*DayPart `json:"dayParts,omitempty"`
	// TimeZoneType: The timezone to use for interpreting the day part targeting.
	//
	// Possible values:
	//   "TIME_ZONE_SOURCE_UNSPECIFIED" - A placeholder for an undefined time zone
	// source.
	//   "PUBLISHER" - Use publisher's time zone setting.
	//   "USER" - Use the user's time zone setting.
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

DayPartTargeting: Specifies the day part targeting criteria.

func (DayPartTargeting) MarshalJSON ¶
func (s DayPartTargeting) MarshalJSON() ([]byte, error)
type Deal ¶
type Deal struct {
	// AvailableEndTime: Proposed flight end time of the deal. This will generally
	// be stored in a granularity of a second. A value is not required for Private
	// Auction deals or Preferred Deals.
	AvailableEndTime string `json:"availableEndTime,omitempty"`
	// AvailableStartTime: Optional. Proposed flight start time of the deal. This
	// will generally be stored in the granularity of one second since deal serving
	// starts at seconds boundary. Any time specified with more granularity (for
	// example, in milliseconds) will be truncated towards the start of time in
	// seconds.
	AvailableStartTime string `json:"availableStartTime,omitempty"`
	// BuyerPrivateData: Buyer private data (hidden from seller).
	BuyerPrivateData *PrivateData `json:"buyerPrivateData,omitempty"`
	// CreateProductId: The product ID from which this deal was created. Note: This
	// field may be set only when creating the resource. Modifying this field while
	// updating the resource will result in an error.
	CreateProductId string `json:"createProductId,omitempty"`
	// CreateProductRevision: Optional. Revision number of the product that the
	// deal was created from. If present on create, and the server
	// `product_revision` has advanced since the passed-in
	// `create_product_revision`, an `ABORTED` error will be returned. Note: This
	// field may be set only when creating the resource. Modifying this field while
	// updating the resource will result in an error.
	CreateProductRevision int64 `json:"createProductRevision,omitempty,string"`
	// CreateTime: Output only. The time of the deal creation.
	CreateTime string `json:"createTime,omitempty"`
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
	// CreativeRestrictions: Output only. Restricitions about the creatives
	// associated with the deal (for example, size) This is available for
	// Programmatic Guaranteed/Preferred Deals in Ad Manager.
	CreativeRestrictions *CreativeRestrictions `json:"creativeRestrictions,omitempty"`
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
	// DealId: Output only. A unique deal ID for the deal (server-assigned).
	DealId string `json:"dealId,omitempty"`
	// DealServingMetadata: Output only. Metadata about the serving status of this
	// deal.
	DealServingMetadata *DealServingMetadata `json:"dealServingMetadata,omitempty"`
	// DealTerms: The negotiable terms of the deal.
	DealTerms *DealTerms `json:"dealTerms,omitempty"`
	// DeliveryControl: The set of fields around delivery control that are
	// interesting for a buyer to see but are non-negotiable. These are set by the
	// publisher.
	DeliveryControl *DeliveryControl `json:"deliveryControl,omitempty"`
	// Description: Description for the deal terms.
	Description string `json:"description,omitempty"`
	// DisplayName: The name of the deal.
	DisplayName string `json:"displayName,omitempty"`
	// ExternalDealId: Output only. The external deal ID assigned to this deal once
	// the deal is finalized. This is the deal ID that shows up in
	// serving/reporting etc.
	ExternalDealId string `json:"externalDealId,omitempty"`
	// IsSetupComplete: Output only. True, if the buyside inventory setup is
	// complete for this deal.
	IsSetupComplete bool `json:"isSetupComplete,omitempty"`
	// ProgrammaticCreativeSource: Output only. Specifies the creative source for
	// programmatic deals. PUBLISHER means creative is provided by seller and
	// ADVERTISER means creative is provided by buyer.
	//
	// Possible values:
	//   "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED" - A placeholder for an
	// undefined programmatic creative source.
	//   "ADVERTISER" - The advertiser provides the creatives.
	//   "PUBLISHER" - The publisher provides the creatives to be served.
	ProgrammaticCreativeSource string `json:"programmaticCreativeSource,omitempty"`
	// ProposalId: Output only. ID of the proposal that this deal is part of.
	ProposalId string `json:"proposalId,omitempty"`
	// SellerContacts: Output only. Seller contact information for the deal.
	SellerContacts []*ContactInformation `json:"sellerContacts,omitempty"`
	// SyndicationProduct: The syndication product associated with the deal. Note:
	// This field may be set only when creating the resource. Modifying this field
	// while updating the resource will result in an error.
	//
	// Possible values:
	//   "SYNDICATION_PRODUCT_UNSPECIFIED" - A placeholder for an undefined
	// syndication product.
	//   "CONTENT" - This typically represents a web page.
	//   "MOBILE" - This represents a mobile property.
	//   "VIDEO" - This represents video ad formats.
	//   "GAMES" - This represents ads shown within games.
	SyndicationProduct string `json:"syndicationProduct,omitempty"`
	// Targeting: Output only. Specifies the subset of inventory targeted by the
	// deal.
	Targeting *MarketplaceTargeting `json:"targeting,omitempty"`
	// TargetingCriterion: The shared targeting visible to buyers and sellers. Each
	// shared targeting entity is AND'd together.
	TargetingCriterion []*TargetingCriteria `json:"targetingCriterion,omitempty"`
	// UpdateTime: Output only. The time when the deal was last updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// WebPropertyCode: The web property code for the seller copied over from the
	// product.
	WebPropertyCode string `json:"webPropertyCode,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AvailableEndTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailableEndTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Deal: A deal represents a segment of inventory for displaying ads on. A proposal can contain multiple deals. A deal contains the terms and targeting information that is used for serving.

func (Deal) MarshalJSON ¶
func (s Deal) MarshalJSON() ([]byte, error)
type DealPauseStatus ¶
type DealPauseStatus struct {
	// BuyerPauseReason: The buyer's reason for pausing, if the buyer paused the
	// deal.
	BuyerPauseReason string `json:"buyerPauseReason,omitempty"`
	// FirstPausedBy: The role of the person who first paused this deal.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	FirstPausedBy string `json:"firstPausedBy,omitempty"`
	// HasBuyerPaused: True, if the buyer has paused the deal unilaterally.
	HasBuyerPaused bool `json:"hasBuyerPaused,omitempty"`
	// HasSellerPaused: True, if the seller has paused the deal unilaterally.
	HasSellerPaused bool `json:"hasSellerPaused,omitempty"`
	// SellerPauseReason: The seller's reason for pausing, if the seller paused the
	// deal.
	SellerPauseReason string `json:"sellerPauseReason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BuyerPauseReason") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BuyerPauseReason") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DealPauseStatus: Tracks which parties (if any) have paused a deal. The deal is considered paused if either hasBuyerPaused or hasSellPaused is true.

func (DealPauseStatus) MarshalJSON ¶
func (s DealPauseStatus) MarshalJSON() ([]byte, error)
type DealServingMetadata ¶
type DealServingMetadata struct {
	// DealPauseStatus: Output only. Tracks which parties (if any) have paused a
	// deal.
	DealPauseStatus *DealPauseStatus `json:"dealPauseStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DealPauseStatus") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DealPauseStatus") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DealServingMetadata: Message captures metadata about the serving status of a deal.

func (DealServingMetadata) MarshalJSON ¶
func (s DealServingMetadata) MarshalJSON() ([]byte, error)
type DealTerms ¶
type DealTerms struct {
	// BrandingType: Visibility of the URL in bid requests. (default: BRANDED)
	//
	// Possible values:
	//   "BRANDING_TYPE_UNSPECIFIED" - A placeholder for an undefined branding
	// type.
	//   "BRANDED" - Full URL is included in bid requests.
	//   "SEMI_TRANSPARENT" - A TopLevelDomain or masked URL is sent in bid
	// requests rather than the full one.
	BrandingType string `json:"brandingType,omitempty"`
	// Description: Publisher provided description for the terms.
	Description string `json:"description,omitempty"`
	// EstimatedGrossSpend: Non-binding estimate of the estimated gross spend for
	// this deal. Can be set by buyer or seller.
	EstimatedGrossSpend *Price `json:"estimatedGrossSpend,omitempty"`
	// EstimatedImpressionsPerDay: Non-binding estimate of the impressions served
	// per day. Can be set by buyer or seller.
	EstimatedImpressionsPerDay int64 `json:"estimatedImpressionsPerDay,omitempty,string"`
	// GuaranteedFixedPriceTerms: The terms for guaranteed fixed price deals.
	GuaranteedFixedPriceTerms *GuaranteedFixedPriceTerms `json:"guaranteedFixedPriceTerms,omitempty"`
	// NonGuaranteedAuctionTerms: The terms for non-guaranteed auction deals.
	NonGuaranteedAuctionTerms *NonGuaranteedAuctionTerms `json:"nonGuaranteedAuctionTerms,omitempty"`
	// NonGuaranteedFixedPriceTerms: The terms for non-guaranteed fixed price
	// deals.
	NonGuaranteedFixedPriceTerms *NonGuaranteedFixedPriceTerms `json:"nonGuaranteedFixedPriceTerms,omitempty"`
	// SellerTimeZone: The time zone name. For deals with Cost Per Day billing,
	// defines the time zone used to mark the boundaries of a day. It should be an
	// IANA TZ name, such as "America/Los_Angeles". For more information, see
	// https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.
	SellerTimeZone string `json:"sellerTimeZone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BrandingType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BrandingType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DealTerms: The deal terms specify the details of a Product/deal. They specify things like price per buyer, the type of pricing model (for example, fixed price, auction) and expected impressions from the publisher.

func (DealTerms) MarshalJSON ¶
func (s DealTerms) MarshalJSON() ([]byte, error)
type DeliveryControl ¶
type DeliveryControl struct {
	// CreativeBlockingLevel: Output only. Specified the creative blocking levels
	// to be applied.
	//
	// Possible values:
	//   "CREATIVE_BLOCKING_LEVEL_UNSPECIFIED" - A placeholder for an undefined
	// creative blocking level.
	//   "PUBLISHER_BLOCKING_RULES" - Publisher blocking rules will be applied.
	//   "ADX_POLICY_BLOCKING_ONLY" - The Ad Exchange policy blocking rules will be
	// applied.
	CreativeBlockingLevel string `json:"creativeBlockingLevel,omitempty"`
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
	// FrequencyCaps: Output only. Specifies any frequency caps.
	FrequencyCaps []*FrequencyCap `json:"frequencyCaps,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreativeBlockingLevel") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeBlockingLevel") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DeliveryControl: Message contains details about how the deals will be paced.

func (DeliveryControl) MarshalJSON ¶
func (s DeliveryControl) MarshalJSON() ([]byte, error)
type Disapproval ¶
type Disapproval struct {
	// Details: Additional details about the reason for disapproval.
	Details []string `json:"details,omitempty"`
	// Reason: The categorized reason for disapproval.
	//
	// Possible values:
	//   "LENGTH_OF_IMAGE_ANIMATION" - The length of the image animation is longer
	// than allowed.
	//   "BROKEN_URL" - The click through URL doesn't work properly.
	//   "MEDIA_NOT_FUNCTIONAL" - Something is wrong with the creative itself.
	//   "INVALID_FOURTH_PARTY_CALL" - The ad makes a fourth party call to an
	// unapproved vendor.
	//   "INCORRECT_REMARKETING_DECLARATION" - The ad targets consumers using
	// remarketing lists and/or collects data for subsequent use in retargeting,
	// but does not correctly declare that use.
	//   "LANDING_PAGE_ERROR" - Clicking on the ad leads to an error page.
	//   "AD_SIZE_DOES_NOT_MATCH_AD_SLOT" - The ad size when rendered does not
	// match the declaration.
	//   "NO_BORDER" - Ads with a white background require a border, which was
	// missing.
	//   "FOURTH_PARTY_BROWSER_COOKIES" - The creative attempts to set cookies from
	// a fourth party that is not certified.
	//   "LSO_OBJECTS" - The creative sets an LSO object.
	//   "BLANK_CREATIVE" - The ad serves a blank.
	//   "DESTINATION_URLS_UNDECLARED" - The ad uses rotation, but not all
	// destination URLs were declared.
	//   "PROBLEM_WITH_CLICK_MACRO" - There is a problem with the way the click
	// macro is used.
	//   "INCORRECT_AD_TECHNOLOGY_DECLARATION" - The ad technology declaration is
	// not accurate.
	//   "INCORRECT_DESTINATION_URL_DECLARATION" - The actual destination URL does
	// not match the declared destination URL.
	//   "EXPANDABLE_INCORRECT_DIRECTION" - The declared expanding direction does
	// not match the actual direction.
	//   "EXPANDABLE_DIRECTION_NOT_SUPPORTED" - The ad does not expand in a
	// supported direction.
	//   "EXPANDABLE_INVALID_VENDOR" - The ad uses an expandable vendor that is not
	// supported.
	//   "EXPANDABLE_FUNCTIONALITY" - There was an issue with the expandable ad.
	//   "VIDEO_INVALID_VENDOR" - The ad uses a video vendor that is not supported.
	//   "VIDEO_UNSUPPORTED_LENGTH" - The length of the video ad is not supported.
	//   "VIDEO_UNSUPPORTED_FORMAT" - The format of the video ad is not supported.
	//   "VIDEO_FUNCTIONALITY" - There was an issue with the video ad.
	//   "LANDING_PAGE_DISABLED" - The landing page does not conform to Ad Exchange
	// policy.
	//   "MALWARE_SUSPECTED" - The ad or the landing page may contain malware.
	//   "ADULT_IMAGE_OR_VIDEO" - The ad contains adult images or video content.
	//   "INACCURATE_AD_TEXT" - The ad contains text that is unclear or inaccurate.
	//   "COUNTERFEIT_DESIGNER_GOODS" - The ad promotes counterfeit designer goods.
	//   "POP_UP" - The ad causes a popup window to appear.
	//   "INVALID_RTB_PROTOCOL_USAGE" - The creative does not follow policies set
	// for the RTB protocol.
	//   "RAW_IP_ADDRESS_IN_SNIPPET" - The ad contains a URL that uses a numeric IP
	// address for the domain.
	//   "UNACCEPTABLE_CONTENT_SOFTWARE" - The ad or landing page contains
	// unacceptable content because it initiated a software or executable download.
	//   "UNAUTHORIZED_COOKIE_ON_GOOGLE_DOMAIN" - The ad set an unauthorized cookie
	// on a Google domain.
	//   "UNDECLARED_FLASH_OBJECTS" - Flash content found when no flash was
	// declared.
	//   "INVALID_SSL_DECLARATION" - SSL support declared but not working
	// correctly.
	//   "DIRECT_DOWNLOAD_IN_AD" - Rich Media - Direct Download in Ad (ex. PDF
	// download).
	//   "MAXIMUM_DOWNLOAD_SIZE_EXCEEDED" - Maximum download size exceeded.
	//   "DESTINATION_URL_SITE_NOT_CRAWLABLE" - Bad Destination URL: Site Not
	// Crawlable.
	//   "BAD_URL_LEGAL_DISAPPROVAL" - Bad URL: Legal disapproval.
	//   "PHARMA_GAMBLING_ALCOHOL_NOT_ALLOWED" - Pharmaceuticals, Gambling, Alcohol
	// not allowed and at least one was detected.
	//   "DYNAMIC_DNS_AT_DESTINATION_URL" - Dynamic DNS at Destination URL.
	//   "POOR_IMAGE_OR_VIDEO_QUALITY" - Poor Image / Video Quality.
	//   "UNACCEPTABLE_IMAGE_CONTENT" - For example, Image Trick to Click.
	//   "INCORRECT_IMAGE_LAYOUT" - Incorrect Image Layout.
	//   "IRRELEVANT_IMAGE_OR_VIDEO" - Irrelevant Image / Video.
	//   "DESTINATION_SITE_DOES_NOT_ALLOW_GOING_BACK" - Broken back button.
	//   "MISLEADING_CLAIMS_IN_AD" - Misleading/Inaccurate claims in ads.
	//   "RESTRICTED_PRODUCTS" - Restricted Products.
	//   "UNACCEPTABLE_CONTENT" - Unacceptable content. For example, malware.
	//   "AUTOMATED_AD_CLICKING" - The ad automatically redirects to the
	// destination site without a click, or reports a click when none were made.
	//   "INVALID_URL_PROTOCOL" - The ad uses URL protocols that do not exist or
	// are not allowed on AdX.
	//   "UNDECLARED_RESTRICTED_CONTENT" - Restricted content (for example,
	// alcohol) was found in the ad but not declared.
	//   "INVALID_REMARKETING_LIST_USAGE" - Violation of the remarketing list
	// policy.
	//   "DESTINATION_SITE_NOT_CRAWLABLE_ROBOTS_TXT" - The destination site's
	// robot.txt file prevents it from being crawled.
	//   "CLICK_TO_DOWNLOAD_NOT_AN_APP" - Click to download must link to an app.
	//   "INACCURATE_REVIEW_EXTENSION" - A review extension must be an accurate
	// review.
	//   "SEXUALLY_EXPLICIT_CONTENT" - Sexually explicit content.
	//   "GAINING_AN_UNFAIR_ADVANTAGE" - The ad tries to gain an unfair traffic
	// advantage.
	//   "GAMING_THE_GOOGLE_NETWORK" - The ad tries to circumvent Google's
	// advertising systems.
	//   "DANGEROUS_PRODUCTS_KNIVES" - The ad promotes dangerous knives.
	//   "DANGEROUS_PRODUCTS_EXPLOSIVES" - The ad promotes explosives.
	//   "DANGEROUS_PRODUCTS_GUNS" - The ad promotes guns & parts.
	//   "DANGEROUS_PRODUCTS_DRUGS" - The ad promotes recreational drugs/services &
	// related equipment.
	//   "DANGEROUS_PRODUCTS_TOBACCO" - The ad promotes tobacco products/services &
	// related equipment.
	//   "DANGEROUS_PRODUCTS_WEAPONS" - The ad promotes weapons.
	//   "UNCLEAR_OR_IRRELEVANT_AD" - The ad is unclear or irrelevant to the
	// destination site.
	//   "PROFESSIONAL_STANDARDS" - The ad does not meet professional standards.
	//   "DYSFUNCTIONAL_PROMOTION" - The promotion is unnecessarily difficult to
	// navigate.
	//   "INVALID_INTEREST_BASED_AD" - Violation of Google's policy for
	// interest-based ads.
	//   "MISUSE_OF_PERSONAL_INFORMATION" - Misuse of personal information.
	//   "OMISSION_OF_RELEVANT_INFORMATION" - Omission of relevant information.
	//   "UNAVAILABLE_PROMOTIONS" - Unavailable promotions.
	//   "MISLEADING_PROMOTIONS" - Misleading or unrealistic promotions.
	//   "INAPPROPRIATE_CONTENT" - Offensive or inappropriate content.
	//   "SENSITIVE_EVENTS" - Capitalizing on sensitive events.
	//   "SHOCKING_CONTENT" - Shocking content.
	//   "ENABLING_DISHONEST_BEHAVIOR" - Products & Services that enable dishonest
	// behavior.
	//   "TECHNICAL_REQUIREMENTS" - The ad does not meet technical requirements.
	//   "RESTRICTED_POLITICAL_CONTENT" - Restricted political content.
	//   "UNSUPPORTED_CONTENT" - Unsupported content.
	//   "INVALID_BIDDING_METHOD" - Invalid bidding method.
	//   "VIDEO_TOO_LONG" - Video length exceeds limits.
	//   "VIOLATES_JAPANESE_PHARMACY_LAW" - Unacceptable content: Japanese
	// healthcare.
	//   "UNACCREDITED_PET_PHARMACY" - Online pharmacy ID required.
	//   "ABORTION" - Unacceptable content: Abortion.
	//   "CONTRACEPTIVES" - Unacceptable content: Birth control.
	//   "NEED_CERTIFICATES_TO_ADVERTISE_IN_CHINA" - Restricted in China.
	//   "KCDSP_REGISTRATION" - Unacceptable content: Korean healthcare.
	//   "NOT_FAMILY_SAFE" - Non-family safe or adult content.
	//   "CLINICAL_TRIAL_RECRUITMENT" - Clinical trial recruitment.
	//   "MAXIMUM_NUMBER_OF_HTTP_CALLS_EXCEEDED" - Maximum number of HTTP calls
	// exceeded.
	//   "MAXIMUM_NUMBER_OF_COOKIES_EXCEEDED" - Maximum number of cookies exceeded.
	//   "PERSONAL_LOANS" - Financial service ad does not adhere to specifications.
	//   "UNSUPPORTED_FLASH_CONTENT" - Flash content was found in an unsupported
	// context.
	//   "MISUSE_BY_OMID_SCRIPT" - Misuse by an Open Measurement SDK script.
	//   "NON_WHITELISTED_OMID_VENDOR" - Use of an Open Measurement SDK vendor not
	// on approved vendor list.
	//   "DESTINATION_EXPERIENCE" - Unacceptable landing page.
	//   "UNSUPPORTED_LANGUAGE" - Unsupported language.
	//   "NON_SSL_COMPLIANT" - Non-SSL compliant.
	//   "TEMPORARY_PAUSE" - Temporary pausing of creative.
	//   "BAIL_BONDS" - Promotes services related to bail bonds.
	//   "EXPERIMENTAL_MEDICAL_TREATMENT" - Promotes speculative and/or
	// experimental medical treatments.
	Reason string `json:"reason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Details") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Details") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Disapproval: Output only. The reason and details for a disapproval.

func (Disapproval) MarshalJSON ¶
func (s Disapproval) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type FilterSet ¶
type FilterSet struct {
	// AbsoluteDateRange: An absolute date range, defined by a start date and an
	// end date. Interpreted relative to Pacific time zone.
	AbsoluteDateRange *AbsoluteDateRange `json:"absoluteDateRange,omitempty"`
	// BreakdownDimensions: The set of dimensions along which to break down the
	// response; may be empty. If multiple dimensions are requested, the breakdown
	// is along the Cartesian product of the requested dimensions.
	//
	// Possible values:
	//   "BREAKDOWN_DIMENSION_UNSPECIFIED" - A placeholder for an unspecified
	// dimension; should not be used.
	//   "PUBLISHER_IDENTIFIER" - The response should be broken down by publisher
	// identifier. This option is available only for Open Bidding buyers.
	BreakdownDimensions []string `json:"breakdownDimensions,omitempty"`
	// CreativeId: The ID of the creative on which to filter; optional. This field
	// may be set only for a filter set that accesses account-level troubleshooting
	// data, for example, one whose name matches the
	// `bidders/*/accounts/*/filterSets/*` pattern.
	CreativeId string `json:"creativeId,omitempty"`
	// DealId: The ID of the deal on which to filter; optional. This field may be
	// set only for a filter set that accesses account-level troubleshooting data,
	// for example, one whose name matches the `bidders/*/accounts/*/filterSets/*`
	// pattern.
	DealId int64 `json:"dealId,omitempty,string"`
	// Environment: The environment on which to filter; optional.
	//
	// Possible values:
	//   "ENVIRONMENT_UNSPECIFIED" - A placeholder for an undefined environment;
	// indicates that no environment filter will be applied.
	//   "WEB" - The ad impression appears on the web.
	//   "APP" - The ad impression appears in an app.
	Environment string `json:"environment,omitempty"`
	// Format: Creative format bidded on or allowed to bid on, can be empty.
	//
	// Possible values:
	//   "FORMAT_UNSPECIFIED" - A placeholder for an undefined format; indicates
	// that no format filter will be applied.
	//   "NATIVE_DISPLAY" - The ad impression is a native ad, and display (for
	// example, image) format.
	//   "NATIVE_VIDEO" - The ad impression is a native ad, and video format.
	//   "NON_NATIVE_DISPLAY" - The ad impression is not a native ad, and display
	// (for example, image) format.
	//   "NON_NATIVE_VIDEO" - The ad impression is not a native ad, and video
	// format.
	Format string `json:"format,omitempty"`
	// Formats: Creative formats bidded on or allowed to bid on, can be empty.
	// Although this field is a list, it can only be populated with a single item.
	// A HTTP 400 bad request error will be returned in the response if you specify
	// multiple items.
	//
	// Possible values:
	//   "FORMAT_UNSPECIFIED" - A placeholder for an undefined format; indicates
	// that no format filter will be applied.
	//   "NATIVE_DISPLAY" - The ad impression is a native ad, and display (for
	// example, image) format.
	//   "NATIVE_VIDEO" - The ad impression is a native ad, and video format.
	//   "NON_NATIVE_DISPLAY" - The ad impression is not a native ad, and display
	// (for example, image) format.
	//   "NON_NATIVE_VIDEO" - The ad impression is not a native ad, and video
	// format.
	Formats []string `json:"formats,omitempty"`
	// Name: A user-defined name of the filter set. Filter set names must be unique
	// globally and match one of the patterns: - `bidders/*/filterSets/*` (for
	// accessing bidder-level troubleshooting data) -
	// `bidders/*/accounts/*/filterSets/*` (for accessing account-level
	// troubleshooting data) This field is required in create operations.
	Name string `json:"name,omitempty"`
	// Platforms: The list of platforms on which to filter; may be empty. The
	// filters represented by multiple platforms are ORed together (for example, if
	// non-empty, results must match any one of the platforms).
	//
	// Possible values:
	//   "PLATFORM_UNSPECIFIED" - A placeholder for an undefined platform;
	// indicates that no platform filter will be applied.
	//   "DESKTOP" - The ad impression appears on a desktop.
	//   "TABLET" - The ad impression appears on a tablet.
	//   "MOBILE" - The ad impression appears on a mobile device.
	Platforms []string `json:"platforms,omitempty"`
	// PublisherIdentifiers: For Open Bidding partners only. The list of publisher
	// identifiers on which to filter; may be empty. The filters represented by
	// multiple publisher identifiers are ORed together.
	PublisherIdentifiers []string `json:"publisherIdentifiers,omitempty"`
	// RealtimeTimeRange: An open-ended realtime time range, defined by the
	// aggregation start timestamp.
	RealtimeTimeRange *RealtimeTimeRange `json:"realtimeTimeRange,omitempty"`
	// RelativeDateRange: A relative date range, defined by an offset from today
	// and a duration. Interpreted relative to Pacific time zone.
	RelativeDateRange *RelativeDateRange `json:"relativeDateRange,omitempty"`
	// SellerNetworkIds: For Authorized Buyers only. The list of IDs of the seller
	// (publisher) networks on which to filter; may be empty. The filters
	// represented by multiple seller network IDs are ORed together (for example,
	// if non-empty, results must match any one of the publisher networks). See
	// seller-network-ids
	// (https://developers.google.com/authorized-buyers/rtb/downloads/seller-network-ids)
	// file for the set of existing seller network IDs.
	SellerNetworkIds []int64 `json:"sellerNetworkIds,omitempty"`
	// TimeSeriesGranularity: The granularity of time intervals if a time series
	// breakdown is preferred; optional.
	//
	// Possible values:
	//   "TIME_SERIES_GRANULARITY_UNSPECIFIED" - A placeholder for an unspecified
	// interval; no time series is applied. All rows in response will contain data
	// for the entire requested time range.
	//   "HOURLY" - Indicates that data will be broken down by the hour.
	//   "DAILY" - Indicates that data will be broken down by the day.
	TimeSeriesGranularity string `json:"timeSeriesGranularity,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AbsoluteDateRange") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AbsoluteDateRange") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilterSet: A set of filters that is applied to a request for data. Within a filter set, an AND operation is performed across the filters represented by each field. An OR operation is performed across the filters represented by the multiple values of a repeated field, for example, "format=VIDEO AND deal_id=12 AND (seller_network_id=34 OR seller_network_id=56)".

func (FilterSet) MarshalJSON ¶
func (s FilterSet) MarshalJSON() ([]byte, error)
type FilteredBidCreativeRow ¶
type FilteredBidCreativeRow struct {
	// BidCount: The number of bids with the specified creative.
	BidCount *MetricValue `json:"bidCount,omitempty"`
	// CreativeId: The ID of the creative.
	CreativeId string `json:"creativeId,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BidCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BidCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilteredBidCreativeRow: The number of filtered bids with the specified dimension values that have the specified creative.

func (FilteredBidCreativeRow) MarshalJSON ¶
func (s FilteredBidCreativeRow) MarshalJSON() ([]byte, error)
type FilteredBidDetailRow ¶
type FilteredBidDetailRow struct {
	// BidCount: The number of bids with the specified detail.
	BidCount *MetricValue `json:"bidCount,omitempty"`
	// Detail: The ID of the detail, can be numeric or text. The associated value
	// can be looked up in the dictionary file corresponding to the DetailType in
	// the response message.
	Detail string `json:"detail,omitempty"`
	// DetailId: Note: this field will be deprecated, use "detail" field instead.
	// When "detail" field represents an integer value, this field is populated as
	// the same integer value "detail" field represents, otherwise this field will
	// be 0. The ID of the detail. The associated value can be looked up in the
	// dictionary file corresponding to the DetailType in the response message.
	DetailId int64 `json:"detailId,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BidCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BidCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilteredBidDetailRow: The number of filtered bids with the specified dimension values, among those filtered due to the requested filtering reason (for example, creative status), that have the specified detail.

func (FilteredBidDetailRow) MarshalJSON ¶
func (s FilteredBidDetailRow) MarshalJSON() ([]byte, error)
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

FirstPartyMobileApplicationTargeting: Represents a list of targeted and excluded mobile application IDs that publishers own. Mobile application IDs are from App Store and Google Play Store. Android App ID, for example, com.google.android.apps.maps, can be found in Google Play Store URL. iOS App ID (which is a number) can be found at the end of iTunes store URL. First party mobile applications is either included or excluded.

func (FirstPartyMobileApplicationTargeting) MarshalJSON ¶
func (s FirstPartyMobileApplicationTargeting) MarshalJSON() ([]byte, error)
type FrequencyCap ¶
type FrequencyCap struct {
	// MaxImpressions: The maximum number of impressions that can be served to a
	// user within the specified time period.
	MaxImpressions int64 `json:"maxImpressions,omitempty"`
	// NumTimeUnits: The amount of time, in the units specified by time_unit_type.
	// Defines the amount of time over which impressions per user are counted and
	// capped.
	NumTimeUnits int64 `json:"numTimeUnits,omitempty"`
	// TimeUnitType: The time unit. Along with num_time_units defines the amount of
	// time over which impressions per user are counted and capped.
	//
	// Possible values:
	//   "TIME_UNIT_TYPE_UNSPECIFIED" - A placeholder for an undefined time unit
	// type. This just indicates the variable with this value hasn't been
	// initialized.
	//   "MINUTE" - Minute
	//   "HOUR" - Hour
	//   "DAY" - Day
	//   "WEEK" - Week
	//   "MONTH" - Month
	//   "LIFETIME" - Lifetime
	//   "POD" - Pod
	//   "STREAM" - Stream
	TimeUnitType string `json:"timeUnitType,omitempty"`
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

FrequencyCap: Frequency cap.

func (FrequencyCap) MarshalJSON ¶
func (s FrequencyCap) MarshalJSON() ([]byte, error)
type GuaranteedFixedPriceTerms ¶
type GuaranteedFixedPriceTerms struct {
	// FixedPrices: Fixed price for the specified buyer.
	FixedPrices []*PricePerBuyer `json:"fixedPrices,omitempty"`
	// GuaranteedImpressions: Guaranteed impressions as a percentage. This is the
	// percentage of guaranteed looks that the buyer is guaranteeing to buy.
	GuaranteedImpressions int64 `json:"guaranteedImpressions,omitempty,string"`
	// GuaranteedLooks: Count of guaranteed looks. Required for deal, optional for
	// product. For CPD deals, buyer changes to guaranteed_looks will be ignored.
	GuaranteedLooks int64 `json:"guaranteedLooks,omitempty,string"`
	// ImpressionCap: The lifetime impression cap for CPM sponsorship deals. The
	// deal will stop serving when the cap is reached.
	ImpressionCap int64 `json:"impressionCap,omitempty,string"`
	// MinimumDailyLooks: Daily minimum looks for CPD deal types. For CPD deals,
	// buyer should negotiate on this field instead of guaranteed_looks.
	MinimumDailyLooks int64 `json:"minimumDailyLooks,omitempty,string"`
	// PercentShareOfVoice: For sponsorship deals, this is the percentage of the
	// seller's eligible impressions that the deal will serve until the cap is
	// reached.
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
	// ForceSendFields is a list of field names (e.g. "FixedPrices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FixedPrices") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GuaranteedFixedPriceTerms: Terms for Programmatic Guaranteed Deals.

func (GuaranteedFixedPriceTerms) MarshalJSON ¶
func (s GuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type HtmlContent ¶
type HtmlContent struct {
	// Height: The height of the HTML snippet in pixels.
	Height int64 `json:"height,omitempty"`
	// Snippet: The HTML snippet that displays the ad when inserted in the web
	// page.
	Snippet string `json:"snippet,omitempty"`
	// Width: The width of the HTML snippet in pixels.
	Width int64 `json:"width,omitempty"`
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

HtmlContent: HTML content for a creative.

func (HtmlContent) MarshalJSON ¶
func (s HtmlContent) MarshalJSON() ([]byte, error)
type Image ¶
type Image struct {
	// Height: Image height in pixels.
	Height int64 `json:"height,omitempty"`
	// Url: The URL of the image.
	Url string `json:"url,omitempty"`
	// Width: Image width in pixels.
	Width int64 `json:"width,omitempty"`
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

Image: An image resource. You may provide a larger image than was requested, so long as the aspect ratio is preserved.

func (Image) MarshalJSON ¶
func (s Image) MarshalJSON() ([]byte, error)
type ImpressionMetricsRow ¶
type ImpressionMetricsRow struct {
	// AvailableImpressions: The number of impressions available to the buyer on Ad
	// Exchange. In some cases this value may be unavailable.
	AvailableImpressions *MetricValue `json:"availableImpressions,omitempty"`
	// BidRequests: The number of impressions for which Ad Exchange sent the buyer
	// a bid request.
	BidRequests *MetricValue `json:"bidRequests,omitempty"`
	// InventoryMatches: The number of impressions that match the buyer's inventory
	// pretargeting.
	InventoryMatches *MetricValue `json:"inventoryMatches,omitempty"`
	// ResponsesWithBids: The number of impressions for which Ad Exchange received
	// a response from the buyer that contained at least one applicable bid.
	ResponsesWithBids *MetricValue `json:"responsesWithBids,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// SuccessfulResponses: The number of impressions for which the buyer
	// successfully sent a response to Ad Exchange.
	SuccessfulResponses *MetricValue `json:"successfulResponses,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AvailableImpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailableImpressions") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ImpressionMetricsRow: The set of metrics that are measured in numbers of impressions, representing how many impressions with the specified dimension values were considered eligible at each stage of the bidding funnel.

func (ImpressionMetricsRow) MarshalJSON ¶
func (s ImpressionMetricsRow) MarshalJSON() ([]byte, error)
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

InventorySizeTargeting: Represents the size of an ad unit that can be targeted on an ad request. It only applies to Private Auction, AdX Preferred Deals and Auction Packages. This targeting does not apply to Programmatic Guaranteed and Preferred Deals in Ad Manager.

func (InventorySizeTargeting) MarshalJSON ¶
func (s InventorySizeTargeting) MarshalJSON() ([]byte, error)
type ListBidMetricsResponse ¶
type ListBidMetricsResponse struct {
	// BidMetricsRows: List of rows, each containing a set of bid metrics.
	BidMetricsRows []*BidMetricsRow `json:"bidMetricsRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListBidMetricsRequest.pageToken field in the subsequent call to the
	// bidMetrics.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BidMetricsRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BidMetricsRows") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBidMetricsResponse: Response message for listing the metrics that are measured in number of bids.

func (ListBidMetricsResponse) MarshalJSON ¶
func (s ListBidMetricsResponse) MarshalJSON() ([]byte, error)
type ListBidResponseErrorsResponse ¶
type ListBidResponseErrorsResponse struct {
	// CalloutStatusRows: List of rows, with counts of bid responses aggregated by
	// callout status.
	CalloutStatusRows []*CalloutStatusRow `json:"calloutStatusRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListBidResponseErrorsRequest.pageToken field in the subsequent call
	// to the bidResponseErrors.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CalloutStatusRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CalloutStatusRows") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListBidResponseErrorsResponse: Response message for listing all reasons that bid responses resulted in an error.

func (ListBidResponseErrorsResponse) MarshalJSON ¶
func (s ListBidResponseErrorsResponse) MarshalJSON() ([]byte, error)
type ListBidResponsesWithoutBidsResponse ¶
type ListBidResponsesWithoutBidsResponse struct {
	// BidResponseWithoutBidsStatusRows: List of rows, with counts of bid responses
	// without bids aggregated by status.
	BidResponseWithoutBidsStatusRows []*BidResponseWithoutBidsStatusRow `json:"bidResponseWithoutBidsStatusRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListBidResponsesWithoutBidsRequest.pageToken field in the subsequent
	// call to the bidResponsesWithoutBids.list method to retrieve the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "BidResponseWithoutBidsStatusRows") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "BidResponseWithoutBidsStatusRows") to include in API requests with the JSON
	// null value. By default, fields with empty values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields for
	// more details.
	NullFields []string `json:"-"`
}

ListBidResponsesWithoutBidsResponse: Response message for listing all reasons that bid responses were considered to have no applicable bids.

func (ListBidResponsesWithoutBidsResponse) MarshalJSON ¶
func (s ListBidResponsesWithoutBidsResponse) MarshalJSON() ([]byte, error)
type ListClientUserInvitationsResponse ¶
type ListClientUserInvitationsResponse struct {
	// Invitations: The returned list of client users.
	Invitations []*ClientUserInvitation `json:"invitations,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListClientUserInvitationsRequest.pageToken field in the subsequent
	// call to the clients.invitations.list method to retrieve the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Invitations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Invitations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (ListClientUserInvitationsResponse) MarshalJSON ¶
func (s ListClientUserInvitationsResponse) MarshalJSON() ([]byte, error)
type ListClientUsersResponse ¶
type ListClientUsersResponse struct {
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListClientUsersRequest.pageToken field in the subsequent call to the
	// clients.invitations.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Users: The returned list of client users.
	Users []*ClientUser `json:"users,omitempty"`

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
func (ListClientUsersResponse) MarshalJSON ¶
func (s ListClientUsersResponse) MarshalJSON() ([]byte, error)
type ListClientsResponse ¶
type ListClientsResponse struct {
	// Clients: The returned list of clients.
	Clients []*Client `json:"clients,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListClientsRequest.pageToken field in the subsequent call to the
	// accounts.clients.list method to retrieve the next page of results.
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
func (ListClientsResponse) MarshalJSON ¶
func (s ListClientsResponse) MarshalJSON() ([]byte, error)
type ListCreativeStatusBreakdownByCreativeResponse ¶
type ListCreativeStatusBreakdownByCreativeResponse struct {
	// FilteredBidCreativeRows: List of rows, with counts of bids with a given
	// creative status aggregated by creative.
	FilteredBidCreativeRows []*FilteredBidCreativeRow `json:"filteredBidCreativeRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListCreativeStatusBreakdownByCreativeRequest.pageToken field in the
	// subsequent call to the filteredBids.creatives.list method to retrieve the
	// next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FilteredBidCreativeRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilteredBidCreativeRows") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListCreativeStatusBreakdownByCreativeResponse: Response message for listing all creatives associated with a given filtered bid reason.

func (ListCreativeStatusBreakdownByCreativeResponse) MarshalJSON ¶
func (s ListCreativeStatusBreakdownByCreativeResponse) MarshalJSON() ([]byte, error)
type ListCreativeStatusBreakdownByDetailResponse ¶
type ListCreativeStatusBreakdownByDetailResponse struct {
	// DetailType: The type of detail that the detail IDs represent.
	//
	// Possible values:
	//   "DETAIL_TYPE_UNSPECIFIED" - A placeholder for an undefined status. This
	// value will never be returned in responses.
	//   "CREATIVE_ATTRIBUTE" - Indicates that the detail ID refers to a creative
	// attribute; see
	// [publisher-excludable-creative-attributes](https://developers.google.com/auth
	// orized-buyers/rtb/downloads/publisher-excludable-creative-attributes).
	//   "VENDOR" - Indicates that the detail ID refers to a vendor; see
	// [vendors](https://developers.google.com/authorized-buyers/rtb/downloads/vendo
	// rs). This namespace is different from that of the `ATP_VENDOR` detail type.
	//   "SENSITIVE_CATEGORY" - Indicates that the detail ID refers to a sensitive
	// category; see
	// [ad-sensitive-categories](https://developers.google.com/authorized-buyers/rtb
	// /downloads/ad-sensitive-categories).
	//   "PRODUCT_CATEGORY" - Indicates that the detail ID refers to a product
	// category; see
	// [ad-product-categories](https://developers.google.com/authorized-buyers/rtb/d
	// ownloads/ad-product-categories).
	//   "DISAPPROVAL_REASON" - Indicates that the detail ID refers to a
	// disapproval reason; see DisapprovalReason enum in
	// [snippet-status-report-proto](https://developers.google.com/authorized-buyers
	// /rtb/downloads/snippet-status-report-proto).
	//   "POLICY_TOPIC" - Indicates that the detail ID refers to a policy topic.
	//   "ATP_VENDOR" - Indicates that the detail ID refers to an ad technology
	// provider (ATP); see [providers]
	// (https://storage.googleapis.com/adx-rtb-dictionaries/providers.csv). This
	// namespace is different from the `VENDOR` detail type; see [ad technology
	// providers](https://support.google.com/admanager/answer/9012903) for more
	// information.
	//   "VENDOR_DOMAIN" - Indicates that the detail string refers the domain of an
	// unknown vendor.
	//   "GVL_ID" - Indicates that the detail ID refers an IAB GVL ID which Google
	// did not detect in the latest TCF Vendor List. See [Global Vendor List]
	// (https://vendor-list.consensu.org/v2/vendor-list.json)
	DetailType string `json:"detailType,omitempty"`
	// FilteredBidDetailRows: List of rows, with counts of bids with a given
	// creative status aggregated by detail.
	FilteredBidDetailRows []*FilteredBidDetailRow `json:"filteredBidDetailRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListCreativeStatusBreakdownByDetailRequest.pageToken field in the
	// subsequent call to the filteredBids.details.list method to retrieve the next
	// page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DetailType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DetailType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListCreativeStatusBreakdownByDetailResponse: Response message for listing all details associated with a given filtered bid reason.

func (ListCreativeStatusBreakdownByDetailResponse) MarshalJSON ¶
func (s ListCreativeStatusBreakdownByDetailResponse) MarshalJSON() ([]byte, error)
type ListCreativesResponse ¶
type ListCreativesResponse struct {
	// Creatives: The list of creatives.
	Creatives []*Creative `json:"creatives,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListCreativesRequest.page_token field in the subsequent call to
	// `ListCreatives` method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Creatives") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Creatives") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListCreativesResponse: A response for listing creatives.

func (ListCreativesResponse) MarshalJSON ¶
func (s ListCreativesResponse) MarshalJSON() ([]byte, error)
type ListDealAssociationsResponse ¶
type ListDealAssociationsResponse struct {
	// Associations: The list of associations.
	Associations []*CreativeDealAssociation `json:"associations,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListDealAssociationsRequest.page_token field in the subsequent call
	// to 'ListDealAssociation' method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Associations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Associations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListDealAssociationsResponse: A response for listing creative and deal associations

func (ListDealAssociationsResponse) MarshalJSON ¶
func (s ListDealAssociationsResponse) MarshalJSON() ([]byte, error)
type ListFilterSetsResponse ¶
type ListFilterSetsResponse struct {
	// FilterSets: The filter sets belonging to the buyer.
	FilterSets []*FilterSet `json:"filterSets,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListFilterSetsRequest.pageToken field in the subsequent call to the
	// accounts.filterSets.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FilterSets") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterSets") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListFilterSetsResponse: Response message for listing filter sets.

func (ListFilterSetsResponse) MarshalJSON ¶
func (s ListFilterSetsResponse) MarshalJSON() ([]byte, error)
type ListFilteredBidRequestsResponse ¶
type ListFilteredBidRequestsResponse struct {
	// CalloutStatusRows: List of rows, with counts of filtered bid requests
	// aggregated by callout status.
	CalloutStatusRows []*CalloutStatusRow `json:"calloutStatusRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListFilteredBidRequestsRequest.pageToken field in the subsequent call
	// to the filteredBidRequests.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CalloutStatusRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CalloutStatusRows") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListFilteredBidRequestsResponse: Response message for listing all reasons that bid requests were filtered and not sent to the buyer.

func (ListFilteredBidRequestsResponse) MarshalJSON ¶
func (s ListFilteredBidRequestsResponse) MarshalJSON() ([]byte, error)
type ListFilteredBidsResponse ¶
type ListFilteredBidsResponse struct {
	// CreativeStatusRows: List of rows, with counts of filtered bids aggregated by
	// filtering reason (for example, creative status).
	CreativeStatusRows []*CreativeStatusRow `json:"creativeStatusRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListFilteredBidsRequest.pageToken field in the subsequent call to the
	// filteredBids.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreativeStatusRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeStatusRows") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListFilteredBidsResponse: Response message for listing all reasons that bids were filtered from the auction.

func (ListFilteredBidsResponse) MarshalJSON ¶
func (s ListFilteredBidsResponse) MarshalJSON() ([]byte, error)
type ListImpressionMetricsResponse ¶
type ListImpressionMetricsResponse struct {
	// ImpressionMetricsRows: List of rows, each containing a set of impression
	// metrics.
	ImpressionMetricsRows []*ImpressionMetricsRow `json:"impressionMetricsRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListImpressionMetricsRequest.pageToken field in the subsequent call
	// to the impressionMetrics.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ImpressionMetricsRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ImpressionMetricsRows") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListImpressionMetricsResponse: Response message for listing the metrics that are measured in number of impressions.

func (ListImpressionMetricsResponse) MarshalJSON ¶
func (s ListImpressionMetricsResponse) MarshalJSON() ([]byte, error)
type ListLosingBidsResponse ¶
type ListLosingBidsResponse struct {
	// CreativeStatusRows: List of rows, with counts of losing bids aggregated by
	// loss reason (for example, creative status).
	CreativeStatusRows []*CreativeStatusRow `json:"creativeStatusRows,omitempty"`
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListLosingBidsRequest.pageToken field in the subsequent call to the
	// losingBids.list method to retrieve the next page of results.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreativeStatusRows") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeStatusRows") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListLosingBidsResponse: Response message for listing all reasons that bids lost in the auction.

func (ListLosingBidsResponse) MarshalJSON ¶
func (s ListLosingBidsResponse) MarshalJSON() ([]byte, error)
type ListNonBillableWinningBidsResponse ¶
type ListNonBillableWinningBidsResponse struct {
	// NextPageToken: A token to retrieve the next page of results. Pass this value
	// in the ListNonBillableWinningBidsRequest.pageToken field in the subsequent
	// call to the nonBillableWinningBids.list method to retrieve the next page of
	// results.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// NonBillableWinningBidStatusRows: List of rows, with counts of bids not
	// billed aggregated by reason.
	NonBillableWinningBidStatusRows []*NonBillableWinningBidStatusRow `json:"nonBillableWinningBidStatusRows,omitempty"`

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

ListNonBillableWinningBidsResponse: Response message for listing all reasons for which a buyer was not billed for a winning bid.

func (ListNonBillableWinningBidsResponse) MarshalJSON ¶
func (s ListNonBillableWinningBidsResponse) MarshalJSON() ([]byte, error)
type ListProductsResponse ¶
type ListProductsResponse struct {
	// NextPageToken: List pagination support.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Products: The list of matching products at their head revision number.
	Products []*Product `json:"products,omitempty"`

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

ListProductsResponse: Response message for listing products visible to the buyer.

func (ListProductsResponse) MarshalJSON ¶
func (s ListProductsResponse) MarshalJSON() ([]byte, error)
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
	// NextPageToken: List pagination support
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
type LocationContext ¶
type LocationContext struct {
	// GeoCriteriaIds: IDs representing the geo location for this context. Refer to
	// the geo-table.csv
	// (https://storage.googleapis.com/adx-rtb-dictionaries/geo-table.csv) file for
	// different geo criteria IDs.
	GeoCriteriaIds []int64 `json:"geoCriteriaIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "GeoCriteriaIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GeoCriteriaIds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LocationContext: Output only. The Geo criteria the restriction applies to.

func (LocationContext) MarshalJSON ¶
func (s LocationContext) MarshalJSON() ([]byte, error)
type MarketplaceTargeting ¶
type MarketplaceTargeting struct {
	// GeoTargeting: Geo criteria IDs to be included/excluded.
	GeoTargeting *CriteriaTargeting `json:"geoTargeting,omitempty"`
	// InventorySizeTargeting: Inventory sizes to be included/excluded.
	InventorySizeTargeting *InventorySizeTargeting `json:"inventorySizeTargeting,omitempty"`
	// PlacementTargeting: Placement targeting information, for example, URL,
	// mobile applications.
	PlacementTargeting *PlacementTargeting `json:"placementTargeting,omitempty"`
	// TechnologyTargeting: Technology targeting information, for example,
	// operating system, device category.
	TechnologyTargeting *TechnologyTargeting `json:"technologyTargeting,omitempty"`
	// VideoTargeting: Video targeting information.
	VideoTargeting *VideoTargeting `json:"videoTargeting,omitempty"`
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

MarketplaceTargeting: Targeting represents different criteria that can be used by advertisers to target ad inventory. For example, they can choose to target ad requests only if the user is in the US. Multiple types of targeting are always applied as a logical AND, unless noted otherwise.

func (MarketplaceTargeting) MarshalJSON ¶
func (s MarketplaceTargeting) MarshalJSON() ([]byte, error)
type MetricValue ¶
type MetricValue struct {
	// Value: The expected value of the metric.
	Value int64 `json:"value,omitempty,string"`
	// Variance: The variance (for example, square of the standard deviation) of
	// the metric value. If value is exact, variance is 0. Can be used to calculate
	// margin of error as a percentage of value, using the following formula, where
	// Z is the standard constant that depends on the preferred size of the
	// confidence interval (for example, for 90% confidence interval, use Z =
	// 1.645): marginOfError = 100 * Z * sqrt(variance) / value
	Variance int64 `json:"variance,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "Value") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Value") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MetricValue: A metric value, with an expected value and a variance; represents a count that may be either exact or estimated (for example, when sampled).

func (MetricValue) MarshalJSON ¶
func (s MetricValue) MarshalJSON() ([]byte, error)
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
type NativeContent ¶
type NativeContent struct {
	// AdvertiserName: The name of the advertiser or sponsor, to be displayed in
	// the ad creative.
	AdvertiserName string `json:"advertiserName,omitempty"`
	// AppIcon: The app icon, for app download ads.
	AppIcon *Image `json:"appIcon,omitempty"`
	// Body: A long description of the ad.
	Body string `json:"body,omitempty"`
	// CallToAction: A label for the button that the user is supposed to click.
	CallToAction string `json:"callToAction,omitempty"`
	// ClickLinkUrl: The URL that the browser/SDK will load when the user clicks
	// the ad.
	ClickLinkUrl string `json:"clickLinkUrl,omitempty"`
	// ClickTrackingUrl: The URL to use for click tracking.
	ClickTrackingUrl string `json:"clickTrackingUrl,omitempty"`
	// Headline: A short title for the ad.
	Headline string `json:"headline,omitempty"`
	// Image: A large image.
	Image *Image `json:"image,omitempty"`
	// Logo: A smaller image, for the advertiser's logo.
	Logo *Image `json:"logo,omitempty"`
	// PriceDisplayText: The price of the promoted app including currency info.
	PriceDisplayText string `json:"priceDisplayText,omitempty"`
	// StarRating: The app rating in the app store. Must be in the range [0-5].
	StarRating float64 `json:"starRating,omitempty"`
	// StoreUrl: The URL to the app store to purchase/download the promoted app.
	StoreUrl string `json:"storeUrl,omitempty"`
	// VideoUrl: The URL to fetch a native video ad.
	VideoUrl string `json:"videoUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdvertiserName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdvertiserName") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NativeContent: Native content for a creative.

func (NativeContent) MarshalJSON ¶
func (s NativeContent) MarshalJSON() ([]byte, error)
func (*NativeContent) UnmarshalJSON ¶
func (s *NativeContent) UnmarshalJSON(data []byte) error
type NonBillableWinningBidStatusRow ¶
type NonBillableWinningBidStatusRow struct {
	// BidCount: The number of bids with the specified status.
	BidCount *MetricValue `json:"bidCount,omitempty"`
	// RowDimensions: The values of all dimensions associated with metric values in
	// this row.
	RowDimensions *RowDimensions `json:"rowDimensions,omitempty"`
	// Status: The status specifying why the winning bids were not billed.
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - A placeholder for an undefined status. This value
	// will never be returned in responses.
	//   "AD_NOT_RENDERED" - The buyer was not billed because the ad was not
	// rendered by the publisher.
	//   "INVALID_IMPRESSION" - The buyer was not billed because the impression won
	// by the bid was determined to be invalid.
	//   "FATAL_VAST_ERROR" - A video impression was served but a fatal error was
	// reported from the client during playback.
	//   "LOST_IN_MEDIATION" - The buyer was not billed because the ad was
	// outplaced in the mediation waterfall.
	//   "OVERDELIVERED_IMPRESSION" - The impression was not billed because it
	// exceeded a guaranteed deal delivery goal.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BidCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BidCount") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NonBillableWinningBidStatusRow: The number of winning bids with the specified dimension values for which the buyer was not billed, as described by the specified status.

func (NonBillableWinningBidStatusRow) MarshalJSON ¶
func (s NonBillableWinningBidStatusRow) MarshalJSON() ([]byte, error)
type NonGuaranteedAuctionTerms ¶
type NonGuaranteedAuctionTerms struct {
	// AutoOptimizePrivateAuction: True if open auction buyers are allowed to
	// compete with invited buyers in this private auction.
	AutoOptimizePrivateAuction bool `json:"autoOptimizePrivateAuction,omitempty"`
	// ReservePricesPerBuyer: Reserve price for the specified buyer.
	ReservePricesPerBuyer []*PricePerBuyer `json:"reservePricesPerBuyer,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoOptimizePrivateAuction")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoOptimizePrivateAuction") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NonGuaranteedAuctionTerms: Terms for Private Auctions. Note that Private Auctions can be created only by the seller, but they can be returned in a get or list request.

func (NonGuaranteedAuctionTerms) MarshalJSON ¶
func (s NonGuaranteedAuctionTerms) MarshalJSON() ([]byte, error)
type NonGuaranteedFixedPriceTerms ¶
type NonGuaranteedFixedPriceTerms struct {
	// FixedPrices: Fixed price for the specified buyer.
	FixedPrices []*PricePerBuyer `json:"fixedPrices,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FixedPrices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FixedPrices") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

NonGuaranteedFixedPriceTerms: Terms for Preferred Deals.

func (NonGuaranteedFixedPriceTerms) MarshalJSON ¶
func (s NonGuaranteedFixedPriceTerms) MarshalJSON() ([]byte, error)
type Note ¶
type Note struct {
	// CreateTime: Output only. The timestamp for when this note was created.
	CreateTime string `json:"createTime,omitempty"`
	// CreatorRole: Output only. The role of the person (buyer/seller) creating the
	// note.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	CreatorRole string `json:"creatorRole,omitempty"`
	// Note: The actual note to attach. (max-length: 1024 unicode code units) Note:
	// This field may be set only when creating the resource. Modifying this field
	// while updating the resource will result in an error.
	Note string `json:"note,omitempty"`
	// NoteId: Output only. The unique ID for the note.
	NoteId string `json:"noteId,omitempty"`
	// ProposalRevision: Output only. The revision number of the proposal when the
	// note is created.
	ProposalRevision int64 `json:"proposalRevision,omitempty,string"`

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

Note: A proposal may be associated to several notes.

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
type PauseProposalDealsRequest ¶
added in v0.48.0
type PauseProposalDealsRequest struct {
	// ExternalDealIds: The external_deal_id's of the deals to be paused. If empty,
	// all the deals in the proposal will be paused.
	ExternalDealIds []string `json:"externalDealIds,omitempty"`
	// Reason: The reason why the deals are being paused. This human readable
	// message will be displayed in the seller's UI. (Max length: 1000 unicode code
	// units.)
	Reason string `json:"reason,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalDealIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalDealIds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PauseProposalDealsRequest: Request message to pause serving for finalized deals.

func (PauseProposalDealsRequest) MarshalJSON ¶
added in v0.48.0
func (s PauseProposalDealsRequest) MarshalJSON() ([]byte, error)
type PauseProposalRequest ¶
type PauseProposalRequest struct {
	// Reason: The reason why the proposal is being paused. This human readable
	// message will be displayed in the seller's UI. (Max length: 1000 unicode code
	// units.)
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

PauseProposalRequest: Request message to pause serving for an already-finalized proposal.

func (PauseProposalRequest) MarshalJSON ¶
func (s PauseProposalRequest) MarshalJSON() ([]byte, error)
type PlacementTargeting ¶
type PlacementTargeting struct {
	// MobileApplicationTargeting: Mobile application targeting information in a
	// deal. This doesn't apply to Auction Packages.
	MobileApplicationTargeting *MobileApplicationTargeting `json:"mobileApplicationTargeting,omitempty"`
	// UrlTargeting: URLs to be included/excluded.
	UrlTargeting *UrlTargeting `json:"urlTargeting,omitempty"`
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
type PlatformContext ¶
type PlatformContext struct {
	// Platforms: The platforms this restriction applies to.
	//
	// Possible values:
	//   "DESKTOP" - Desktop platform.
	//   "ANDROID" - Android platform.
	//   "IOS" - iOS platform.
	Platforms []string `json:"platforms,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Platforms") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Platforms") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PlatformContext: Output only. The type of platform the restriction applies to.

func (PlatformContext) MarshalJSON ¶
func (s PlatformContext) MarshalJSON() ([]byte, error)
type Price ¶
type Price struct {
	// Amount: The actual price with currency specified.
	Amount *Money `json:"amount,omitempty"`
	// PricingType: The pricing type for the deal/product. (default: CPM)
	//
	// Possible values:
	//   "PRICING_TYPE_UNSPECIFIED" - A placeholder for an undefined pricing type.
	// If the pricing type is unspecified, `COST_PER_MILLE` will be used instead.
	//   "COST_PER_MILLE" - Cost per thousand impressions.
	//   "COST_PER_DAY" - Cost per day
	PricingType string `json:"pricingType,omitempty"`
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

Price: Represents a price and a pricing type for a product / deal.

func (Price) MarshalJSON ¶
func (s Price) MarshalJSON() ([]byte, error)
type PricePerBuyer ¶
type PricePerBuyer struct {
	// AdvertiserIds: The list of advertisers for this price when associated with
	// this buyer. If empty, all advertisers with this buyer pay this price.
	AdvertiserIds []string `json:"advertiserIds,omitempty"`
	// Buyer: The buyer who will pay this price. If unset, all buyers can pay this
	// price (if the advertisers match, and there's no more specific rule matching
	// the buyer).
	Buyer *Buyer `json:"buyer,omitempty"`
	// Price: The specified price.
	Price *Price `json:"price,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AdvertiserIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdvertiserIds") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

PricePerBuyer: Used to specify pricing rules for buyers/advertisers. Each PricePerBuyer in a product can become 0 or 1 deals. To check if there is a PricePerBuyer for a particular buyer or buyer/advertiser pair, we look for the most specific matching rule - we first look for a rule matching the buyer and advertiser, next a rule with the buyer but an empty advertiser list, and otherwise look for a matching rule where no buyer is set.

func (PricePerBuyer) MarshalJSON ¶
func (s PricePerBuyer) MarshalJSON() ([]byte, error)
type PrivateData ¶
type PrivateData struct {
	// ReferenceId: A buyer or seller specified reference ID. This can be queried
	// in the list operations (max-length: 1024 unicode code units).
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

PrivateData: Buyers are allowed to store certain types of private data in a proposal/deal.

func (PrivateData) MarshalJSON ¶
func (s PrivateData) MarshalJSON() ([]byte, error)
type Product ¶
type Product struct {
	// AvailableEndTime: The proposed end time for the deal. The field will be
	// truncated to the order of seconds during serving.
	AvailableEndTime string `json:"availableEndTime,omitempty"`
	// AvailableStartTime: Inventory availability dates. The start time will be
	// truncated to seconds during serving. Thus, a field specified as 3:23:34.456
	// (HH:mm:ss.SSS) will be truncated to 3:23:34 when serving.
	AvailableStartTime string `json:"availableStartTime,omitempty"`
	// CreateTime: Creation time.
	CreateTime string `json:"createTime,omitempty"`
	// CreatorContacts: Optional contact information for the creator of this
	// product.
	CreatorContacts []*ContactInformation `json:"creatorContacts,omitempty"`
	// DisplayName: The display name for this product as set by the seller.
	DisplayName string `json:"displayName,omitempty"`
	// HasCreatorSignedOff: If the creator has already signed off on the product,
	// then the buyer can finalize the deal by accepting the product as is. When
	// copying to a proposal, if any of the terms are changed, then auto_finalize
	// is automatically set to false.
	HasCreatorSignedOff bool `json:"hasCreatorSignedOff,omitempty"`
	// ProductId: The unique ID for the product.
	ProductId string `json:"productId,omitempty"`
	// ProductRevision: The revision number of the product (auto-assigned by
	// Marketplace).
	ProductRevision int64 `json:"productRevision,omitempty,string"`
	// PublisherProfileId: An ID which can be used by the Publisher Profile API to
	// get more information about the seller that created this product.
	PublisherProfileId string `json:"publisherProfileId,omitempty"`
	// Seller: Information about the seller that created this product.
	Seller *Seller `json:"seller,omitempty"`
	// SyndicationProduct: The syndication product associated with the deal.
	//
	// Possible values:
	//   "SYNDICATION_PRODUCT_UNSPECIFIED" - A placeholder for an undefined
	// syndication product.
	//   "CONTENT" - This typically represents a web page.
	//   "MOBILE" - This represents a mobile property.
	//   "VIDEO" - This represents video ad formats.
	//   "GAMES" - This represents ads shown within games.
	SyndicationProduct string `json:"syndicationProduct,omitempty"`
	// TargetingCriterion: Targeting that is shared between the buyer and the
	// seller. Each targeting criterion has a specified key and for each key there
	// is a list of inclusion value or exclusion values.
	TargetingCriterion []*TargetingCriteria `json:"targetingCriterion,omitempty"`
	// Terms: The negotiable terms of the deal.
	Terms *DealTerms `json:"terms,omitempty"`
	// UpdateTime: Time of last update.
	UpdateTime string `json:"updateTime,omitempty"`
	// WebPropertyCode: The web-property code for the seller. This needs to be
	// copied as is when adding a new deal to a proposal.
	WebPropertyCode string `json:"webPropertyCode,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AvailableEndTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailableEndTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Product: A product is a segment of inventory that a seller wants to sell. It is associated with certain terms and targeting information which helps the buyer know more about the inventory.

func (Product) MarshalJSON ¶
func (s Product) MarshalJSON() ([]byte, error)
type Proposal ¶
type Proposal struct {
	// BilledBuyer: Output only. Reference to the buyer that will get billed for
	// this proposal.
	BilledBuyer *Buyer `json:"billedBuyer,omitempty"`
	// Buyer: Reference to the buyer on the proposal. Note: This field may be set
	// only when creating the resource. Modifying this field while updating the
	// resource will result in an error.
	Buyer *Buyer `json:"buyer,omitempty"`
	// BuyerContacts: Contact information for the buyer.
	BuyerContacts []*ContactInformation `json:"buyerContacts,omitempty"`
	// BuyerPrivateData: Private data for buyer. (hidden from seller).
	BuyerPrivateData *PrivateData `json:"buyerPrivateData,omitempty"`
	// Deals: The deals associated with this proposal. For Private Auction
	// proposals (whose deals have NonGuaranteedAuctionTerms), there will only be
	// one deal.
	Deals []*Deal `json:"deals,omitempty"`
	// DisplayName: The name for the proposal.
	DisplayName string `json:"displayName,omitempty"`
	// IsRenegotiating: Output only. True if the proposal is being renegotiated.
	IsRenegotiating bool `json:"isRenegotiating,omitempty"`
	// IsSetupComplete: Output only. True, if the buyside inventory setup is
	// complete for this proposal.
	IsSetupComplete bool `json:"isSetupComplete,omitempty"`
	// LastUpdaterOrCommentorRole: Output only. The role of the last user that
	// either updated the proposal or left a comment.
	//
	// Possible values:
	//   "BUYER_SELLER_ROLE_UNSPECIFIED" - A placeholder for an undefined
	// buyer/seller role.
	//   "BUYER" - Specifies the role as buyer.
	//   "SELLER" - Specifies the role as seller.
	LastUpdaterOrCommentorRole string `json:"lastUpdaterOrCommentorRole,omitempty"`
	// Notes: Output only. The notes associated with this proposal.
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
	// PrivateAuctionId: Output only. Private auction ID if this proposal is a
	// private auction proposal.
	PrivateAuctionId string `json:"privateAuctionId,omitempty"`
	// ProposalId: Output only. The unique ID of the proposal.
	ProposalId string `json:"proposalId,omitempty"`
	// ProposalRevision: Output only. The revision number for the proposal. Each
	// update to the proposal or the deal causes the proposal revision number to
	// auto-increment. The buyer keeps track of the last revision number they know
	// of and pass it in when making an update. If the head revision number on the
	// server has since incremented, then an ABORTED error is returned during the
	// update operation to let the buyer know that a subsequent update was made.
	ProposalRevision int64 `json:"proposalRevision,omitempty,string"`
	// ProposalState: Output only. The current state of the proposal.
	//
	// Possible values:
	//   "PROPOSAL_STATE_UNSPECIFIED" - A placeholder for an undefined proposal
	// state.
	//   "PROPOSED" - The proposal is under negotiation or renegotiation.
	//   "BUYER_ACCEPTED" - The proposal has been accepted by the buyer.
	//   "SELLER_ACCEPTED" - The proposal has been accepted by the seller.
	//   "CANCELED" - The negotiations on the proposal were canceled and the
	// proposal was never finalized.
	//   "FINALIZED" - The proposal is finalized. During renegotiation, the
	// proposal may not be in this state.
	ProposalState string `json:"proposalState,omitempty"`
	// Seller: Reference to the seller on the proposal. Note: This field may be set
	// only when creating the resource. Modifying this field while updating the
	// resource will result in an error.
	Seller *Seller `json:"seller,omitempty"`
	// SellerContacts: Output only. Contact information for the seller.
	SellerContacts []*ContactInformation `json:"sellerContacts,omitempty"`
	// TermsAndConditions: Output only. The terms and conditions set by the
	// publisher for this proposal.
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

Proposal: Represents a proposal in the Marketplace. A proposal is the unit of negotiation between a seller and a buyer and contains deals which are served. Note: You can't update, create, or otherwise modify Private Auction deals through the API. Fields are updatable unless noted otherwise.

func (Proposal) MarshalJSON ¶
func (s Proposal) MarshalJSON() ([]byte, error)
type PublisherProfile ¶
type PublisherProfile struct {
	// AudienceDescription: Description on the publisher's audience.
	AudienceDescription string `json:"audienceDescription,omitempty"`
	// BuyerPitchStatement: Statement explaining what's unique about publisher's
	// business, and why buyers should partner with the publisher.
	BuyerPitchStatement string `json:"buyerPitchStatement,omitempty"`
	// DirectDealsContact: Contact information for direct reservation deals. This
	// is free text entered by the publisher and may include information like
	// names, phone numbers and email addresses.
	DirectDealsContact string `json:"directDealsContact,omitempty"`
	// DisplayName: Name of the publisher profile.
	DisplayName string `json:"displayName,omitempty"`
	// Domains: The list of domains represented in this publisher profile. Empty if
	// this is a parent profile. These are top private domains, meaning that these
	// will not contain a string like "photos.google.co.uk/123", but will instead
	// contain "google.co.uk".
	Domains []string `json:"domains,omitempty"`
	// GooglePlusUrl: URL to publisher's Google+ page.
	GooglePlusUrl string `json:"googlePlusUrl,omitempty"`
	// IsParent: Indicates if this profile is the parent profile of the seller. A
	// parent profile represents all the inventory from the seller, as opposed to
	// child profile that is created to brand a portion of inventory. One seller
	// should have only one parent publisher profile, and can have multiple child
	// profiles. Publisher profiles for the same seller will have same value of
	// field google.ads.adexchange.buyer.v2beta1.PublisherProfile.seller. See
	// https://support.google.com/admanager/answer/6035806 for details.
	IsParent bool `json:"isParent,omitempty"`
	// LogoUrl: A Google public URL to the logo for this publisher profile. The
	// logo is stored as a PNG, JPG, or GIF image.
	LogoUrl string `json:"logoUrl,omitempty"`
	// MediaKitUrl: URL to additional marketing and sales materials.
	MediaKitUrl string `json:"mediaKitUrl,omitempty"`
	// MobileApps: The list of apps represented in this publisher profile. Empty if
	// this is a parent profile.
	MobileApps []*PublisherProfileMobileApplication `json:"mobileApps,omitempty"`
	// Overview: Overview of the publisher.
	Overview string `json:"overview,omitempty"`
	// ProgrammaticDealsContact: Contact information for programmatic deals. This
	// is free text entered by the publisher and may include information like
	// names, phone numbers and email addresses.
	ProgrammaticDealsContact string `json:"programmaticDealsContact,omitempty"`
	// PublisherProfileId: Unique ID for publisher profile.
	PublisherProfileId string `json:"publisherProfileId,omitempty"`
	// RateCardInfoUrl: URL to a publisher rate card.
	RateCardInfoUrl string `json:"rateCardInfoUrl,omitempty"`
	// SamplePageUrl: URL to a sample content page.
	SamplePageUrl string `json:"samplePageUrl,omitempty"`
	// Seller: Seller of the publisher profile.
	Seller *Seller `json:"seller,omitempty"`
	// TopHeadlines: Up to three key metrics and rankings. Max 100 characters each.
	// For example "#1 Mobile News Site for 20 Straight Months".
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

PublisherProfile: Represents a publisher profile (https://support.google.com/admanager/answer/6035806) in Marketplace. All fields are read only. All string fields are free-form text entered by the publisher unless noted otherwise.

func (PublisherProfile) MarshalJSON ¶
func (s PublisherProfile) MarshalJSON() ([]byte, error)
type PublisherProfileMobileApplication ¶
added in v0.36.0
type PublisherProfileMobileApplication struct {
	// AppStore: The app store the app belongs to.
	//
	// Possible values:
	//   "APP_STORE_TYPE_UNSPECIFIED" - A placeholder for an unknown app store.
	//   "APPLE_ITUNES" - Apple iTunes
	//   "GOOGLE_PLAY" - Google Play
	//   "ROKU" - Roku
	//   "AMAZON_FIRETV" - Amazon Fire TV
	//   "PLAYSTATION" - Playstation
	//   "XBOX" - Xbox
	//   "SAMSUNG_TV" - Samsung TV
	//   "AMAZON" - Amazon Appstore
	//   "OPPO" - OPPO App Market
	//   "SAMSUNG" - Samsung Galaxy Store
	//   "VIVO" - VIVO App Store
	//   "XIAOMI" - Xiaomi GetApps
	//   "LG_TV" - LG TV
	AppStore string `json:"appStore,omitempty"`
	// ExternalAppId: The external ID for the app from its app store.
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
added in v0.36.0
func (s PublisherProfileMobileApplication) MarshalJSON() ([]byte, error)
type RealtimeTimeRange ¶
type RealtimeTimeRange struct {
	// StartTimestamp: The start timestamp of the real-time RTB metrics
	// aggregation.
	StartTimestamp string `json:"startTimestamp,omitempty"`
	// ForceSendFields is a list of field names (e.g. "StartTimestamp") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "StartTimestamp") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RealtimeTimeRange: An open-ended realtime time range specified by the start timestamp. For filter sets that specify a realtime time range RTB metrics continue to be aggregated throughout the lifetime of the filter set.

func (RealtimeTimeRange) MarshalJSON ¶
func (s RealtimeTimeRange) MarshalJSON() ([]byte, error)
type RelativeDateRange ¶
type RelativeDateRange struct {
	// DurationDays: The number of days in the requested date range, for example,
	// for a range spanning today: 1. For a range spanning the last 7 days: 7.
	DurationDays int64 `json:"durationDays,omitempty"`
	// OffsetDays: The end date of the filter set, specified as the number of days
	// before today, for example, for a range where the last date is today: 0.
	OffsetDays int64 `json:"offsetDays,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DurationDays") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DurationDays") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RelativeDateRange: A relative date range, specified by an offset and a duration. The supported range of dates begins 30 days before today and ends today, for example, the limits for these values are: offset_days >= 0 duration_days >= 1 offset_days + duration_days <= 30

func (RelativeDateRange) MarshalJSON ¶
func (s RelativeDateRange) MarshalJSON() ([]byte, error)
type RemoveDealAssociationRequest ¶
type RemoveDealAssociationRequest struct {
	// Association: The association between a creative and a deal that should be
	// removed.
	Association *CreativeDealAssociation `json:"association,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Association") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Association") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemoveDealAssociationRequest: A request for removing the association between a deal and a creative.

func (RemoveDealAssociationRequest) MarshalJSON ¶
func (s RemoveDealAssociationRequest) MarshalJSON() ([]byte, error)
type ResumeProposalDealsRequest ¶
added in v0.48.0
type ResumeProposalDealsRequest struct {
	// ExternalDealIds: The external_deal_id's of the deals to resume. If empty,
	// all the deals in the proposal will be resumed.
	ExternalDealIds []string `json:"externalDealIds,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalDealIds") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalDealIds") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ResumeProposalDealsRequest: Request message to resume (unpause) serving for already-finalized deals.

func (ResumeProposalDealsRequest) MarshalJSON ¶
added in v0.48.0
func (s ResumeProposalDealsRequest) MarshalJSON() ([]byte, error)
type ResumeProposalRequest ¶
type ResumeProposalRequest struct {
}

ResumeProposalRequest: Request message to resume (unpause) serving for an already-finalized proposal.

type RowDimensions ¶
type RowDimensions struct {
	// PublisherIdentifier: The publisher identifier for this row, if a breakdown
	// by BreakdownDimension.PUBLISHER_IDENTIFIER
	// (https://developers.google.com/authorized-buyers/apis/reference/rest/v2beta1/bidders.accounts.filterSets#FilterSet.BreakdownDimension)
	// was requested.
	PublisherIdentifier string `json:"publisherIdentifier,omitempty"`
	// TimeInterval: The time interval that this row represents.
	TimeInterval *TimeInterval `json:"timeInterval,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PublisherIdentifier") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PublisherIdentifier") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RowDimensions: A response may include multiple rows, breaking down along various dimensions. Encapsulates the values of all dimensions for a given row.

func (RowDimensions) MarshalJSON ¶
func (s RowDimensions) MarshalJSON() ([]byte, error)
type SecurityContext ¶
type SecurityContext struct {
	// Securities: The security types in this context.
	//
	// Possible values:
	//   "INSECURE" - Matches impressions that require insecure compatibility.
	//   "SSL" - Matches impressions that require SSL compatibility.
	Securities []string `json:"securities,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Securities") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Securities") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SecurityContext: Output only. A security context.

func (SecurityContext) MarshalJSON ¶
func (s SecurityContext) MarshalJSON() ([]byte, error)
type Seller ¶
type Seller struct {
	// AccountId: The unique ID for the seller. The seller fills in this field. The
	// seller account ID is then available to buyer in the product.
	AccountId string `json:"accountId,omitempty"`
	// SubAccountId: Output only. Ad manager network code for the seller.
	SubAccountId string `json:"subAccountId,omitempty"`
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

Seller: Represents a seller of inventory. Each seller is identified by a unique Ad Manager account ID.

func (Seller) MarshalJSON ¶
func (s Seller) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Accounts *AccountsService

	Bidders *BiddersService

	Buyers *BuyersService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type ServingContext ¶
type ServingContext struct {
	// All: Matches all contexts.
	//
	// Possible values:
	//   "SIMPLE_CONTEXT" - A simple context.
	All string `json:"all,omitempty"`
	// AppType: Matches impressions for a particular app type.
	AppType *AppContext `json:"appType,omitempty"`
	// AuctionType: Matches impressions for a particular auction type.
	AuctionType *AuctionContext `json:"auctionType,omitempty"`
	// Location: Matches impressions coming from users *or* publishers in a
	// specific location.
	Location *LocationContext `json:"location,omitempty"`
	// Platform: Matches impressions coming from a particular platform.
	Platform *PlatformContext `json:"platform,omitempty"`
	// SecurityType: Matches impressions for a particular security type.
	SecurityType *SecurityContext `json:"securityType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "All") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "All") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServingContext: The serving context for this restriction.

func (ServingContext) MarshalJSON ¶
func (s ServingContext) MarshalJSON() ([]byte, error)
type ServingRestriction ¶
type ServingRestriction struct {
	// Contexts: The contexts for the restriction.
	Contexts []*ServingContext `json:"contexts,omitempty"`
	// Disapproval: Disapproval bound to this restriction. Only present if
	// status=DISAPPROVED. Can be used to filter the response of the creatives.list
	// method.
	Disapproval *Disapproval `json:"disapproval,omitempty"`
	// DisapprovalReasons: Any disapprovals bound to this restriction. Only present
	// if status=DISAPPROVED. Can be used to filter the response of the
	// creatives.list method. Deprecated; use disapproval field instead.
	DisapprovalReasons []*Disapproval `json:"disapprovalReasons,omitempty"`
	// Status: The status of the creative in this context (for example, it has been
	// explicitly disapproved or is pending review).
	//
	// Possible values:
	//   "STATUS_UNSPECIFIED" - The status is not known.
	//   "DISAPPROVAL" - The ad was disapproved in this context.
	//   "PENDING_REVIEW" - The ad is pending review in this context.
	Status string `json:"status,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Contexts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Contexts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServingRestriction: Output only. A representation of the status of an ad in a specific context. A context here relates to where something ultimately serves (for example, a user or publisher geo, a platform, an HTTPS versus HTTP request, or the type of auction).

func (ServingRestriction) MarshalJSON ¶
func (s ServingRestriction) MarshalJSON() ([]byte, error)
type Size ¶
type Size struct {
	// Height: The height of the creative.
	Height int64 `json:"height,omitempty"`
	// Width: The width of the creative
	Width int64 `json:"width,omitempty"`
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

Size: Message depicting the size of the creative. The units of width and height depend on the type of the targeting.

func (Size) MarshalJSON ¶
func (s Size) MarshalJSON() ([]byte, error)
type StopWatchingCreativeRequest ¶
type StopWatchingCreativeRequest struct {
}

StopWatchingCreativeRequest: A request for stopping notifications for changes to creative Status.

type TargetingCriteria ¶
type TargetingCriteria struct {
	// Exclusions: The list of values to exclude from targeting. Each value is
	// AND'd together.
	Exclusions []*TargetingValue `json:"exclusions,omitempty"`
	// Inclusions: The list of value to include as part of the targeting. Each
	// value is OR'd together.
	Inclusions []*TargetingValue `json:"inclusions,omitempty"`
	// Key: The key representing the shared targeting criterion. Targeting criteria
	// defined by Google ad servers will begin with GOOG_. Third parties may define
	// their own keys. A list of permissible keys along with the acceptable values
	// will be provided as part of the external documentation.
	Key string `json:"key,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Exclusions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Exclusions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetingCriteria: Advertisers can target different attributes of an ad slot. For example, they can choose to show ads only if the user is in the U.S. Such targeting criteria can be specified as part of Shared Targeting.

func (TargetingCriteria) MarshalJSON ¶
func (s TargetingCriteria) MarshalJSON() ([]byte, error)
type TargetingValue ¶
type TargetingValue struct {
	// CreativeSizeValue: The creative size value to include/exclude. Filled in
	// when key = GOOG_CREATIVE_SIZE
	CreativeSizeValue *CreativeSize `json:"creativeSizeValue,omitempty"`
	// DayPartTargetingValue: The daypart targeting to include / exclude. Filled in
	// when the key is GOOG_DAYPART_TARGETING. The definition of this targeting is
	// derived from the structure used by Ad Manager.
	DayPartTargetingValue *DayPartTargeting `json:"dayPartTargetingValue,omitempty"`
	// LongValue: The long value to include/exclude.
	LongValue int64 `json:"longValue,omitempty,string"`
	// StringValue: The string value to include/exclude.
	StringValue string `json:"stringValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CreativeSizeValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreativeSizeValue") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TargetingValue: A polymorphic targeting value used as part of Shared Targeting.

func (TargetingValue) MarshalJSON ¶
func (s TargetingValue) MarshalJSON() ([]byte, error)
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
type TimeInterval ¶
type TimeInterval struct {
	// EndTime: The timestamp marking the end of the range (exclusive) for which
	// data is included.
	EndTime string `json:"endTime,omitempty"`
	// StartTime: The timestamp marking the start of the range (inclusive) for
	// which data is included.
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

TimeInterval: An interval of time, with an absolute start and end.

func (TimeInterval) MarshalJSON ¶
func (s TimeInterval) MarshalJSON() ([]byte, error)
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
type UrlTargeting ¶
type UrlTargeting struct {
	// ExcludedUrls: A list of URLs to be excluded.
	ExcludedUrls []string `json:"excludedUrls,omitempty"`
	// TargetedUrls: A list of URLs to be included.
	TargetedUrls []string `json:"targetedUrls,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludedUrls") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludedUrls") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UrlTargeting: Represents a list of targeted and excluded URLs (for example, google.com). For Private Auction and AdX Preferred Deals, URLs are either included or excluded. For Programmatic Guaranteed and Preferred Deals, this doesn't apply.

func (UrlTargeting) MarshalJSON ¶
func (s UrlTargeting) MarshalJSON() ([]byte, error)
type VideoContent ¶
type VideoContent struct {
	// VideoUrl: The URL to fetch a video ad.
	VideoUrl string `json:"videoUrl,omitempty"`
	// VideoVastXml: The contents of a VAST document for a video ad. This document
	// should conform to the VAST 2.0 or 3.0 standard.
	VideoVastXml string `json:"videoVastXml,omitempty"`
	// ForceSendFields is a list of field names (e.g. "VideoUrl") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "VideoUrl") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VideoContent: Video content for a creative.

func (VideoContent) MarshalJSON ¶
func (s VideoContent) MarshalJSON() ([]byte, error)
type VideoTargeting ¶
type VideoTargeting struct {
	// ExcludedPositionTypes: A list of video positions to be excluded. Position
	// types can either be included or excluded (XOR).
	//
	// Possible values:
	//   "POSITION_TYPE_UNSPECIFIED" - A placeholder for an undefined video
	// position.
	//   "PREROLL" - Ad is played before the video.
	//   "MIDROLL" - Ad is played during the video.
	//   "POSTROLL" - Ad is played after the video.
	ExcludedPositionTypes []string `json:"excludedPositionTypes,omitempty"`
	// TargetedPositionTypes: A list of video positions to be included. When the
	// included list is present, the excluded list must be empty. When the excluded
	// list is present, the included list must be empty.
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
type WatchCreativeRequest ¶
type WatchCreativeRequest struct {
	// Topic: The Pub/Sub topic to publish notifications to. This topic must
	// already exist and must give permission to
	// ad-exchange-buyside-reports@google.com to write to the topic. This should be
	// the full resource name in "projects/{project_id}/topics/{topic_id}" format.
	Topic string `json:"topic,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Topic") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Topic") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WatchCreativeRequest: A request for watching changes to creative Status.

func (WatchCreativeRequest) MarshalJSON ¶
func (s WatchCreativeRequest) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
adexchangebuyer2-gen.go
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
